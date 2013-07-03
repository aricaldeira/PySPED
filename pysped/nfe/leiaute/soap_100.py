# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2.1 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Library General Public License,
# publicada pela Free Software Foundation, em sua versão 2.1 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Library General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Library General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import (ABERTURA, NAMESPACE_NFE, TagDecimal, XMLNFe,
                             tira_abertura, tirar_acentos, por_acentos)
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_1 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


class CabecMsg(XMLNFe):
    def __init__(self):
        super(CabecMsg, self).__init__()
        self.versao      = TagDecimal(nome='cabecMsg'   , codigo=''   , propriedade='versao', namespace=NAMESPACE_NFE, valor='1.02', raiz='//cabecMsg')
        self.versaoDados = TagDecimal(nome='versaoDados', codigo='A01', raiz='//cabecMsg', tamanho=[1, 4])
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'cabecMsg_v1.02.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.versaoDados.xml
        xml += '</cabecMsg>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versaoDados.xml = arquivo

    xml = property(get_xml, set_xml)


class NFeCabecMsg(XMLNFe):
    def __init__(self):
        super(NFeCabecMsg, self).__init__()
        self.cabec = CabecMsg()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<nfeCabecMsg>'
        xml += tirar_acentos(self.cabec.xml)
        xml += '</nfeCabecMsg>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cabec.xml = arquivo

    xml = property(get_xml, set_xml)


class NFeDadosMsg(XMLNFe):
    def __init__(self):
        super(NFeDadosMsg, self).__init__()
        self.dados = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<nfeDadosMsg>'
        xml += tirar_acentos(self.dados.xml)
        xml += '</nfeDadosMsg>'

        return xml

    def set_xml(self, arquivo):
        pass

    xml = property(get_xml, set_xml)


class SOAPEnvio(XMLNFe):
    def __init__(self):
        super(SOAPEnvio, self).__init__()
        self.webservice = ''
        self.metodo = ''
        self.envio = None
        self.nfeCabecMsg = NFeCabecMsg()
        self.nfeDadosMsg = NFeDadosMsg()
        self._header = {b'content-type': b'application/soap+xml; charset=utf-8',
            b'Accept': b'application/soap+xml; charset=utf-8'}

    def get_xml(self):
        self.nfeDadosMsg.dados = self.envio
        self.nfeCabecMsg.cabec.versaoDados.valor = self.envio.versao.valor

        self._header[b'SOAPAction'] = self.metodo

        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     '<soap:Body>'
        xml +=         '<' + self.metodo + ' xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + '">'
        xml += self.nfeCabecMsg.xml
        xml += self.nfeDadosMsg.xml
        xml +=         '</' + self.metodo + '>'
        xml +=     '</soap:Body>'
        xml += '</soap:Envelope>'
        return xml

    def set_xml(self):
        pass

    xml = property(get_xml, set_xml)

    def get_header(self):
        header = self._header
        return header

    header = property(get_header)


class SOAPRetorno(XMLNFe):
    def __init__(self):
        super(SOAPRetorno, self).__init__()
        self.webservice = ''
        self.metodo = ''
        self.resposta = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     '<soap:Body>'
        xml +=         '<' + self.metodo + 'Response xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + '">'
        xml +=             '<' + self.metodo + 'Result>'
        xml += self.resposta.xml
        xml +=             '</' + self.metodo + 'Result>'
        xml +=         '</' + self.metodo + 'Response>'
        xml +=     '</soap:Body>'
        xml += '</soap:Envelope>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            resposta = por_acentos(self._le_tag('//*/res:' + self.metodo + 'Result',  ns=('http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice)))
            resposta = tira_abertura(resposta)
            #print resposta
            self.resposta.xml = resposta

        return self.xml

    xml = property(get_xml, set_xml)
