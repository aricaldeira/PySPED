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

from pysped.xml_sped import (ABERTURA, TagDecimal, TagInteiro, XMLNFe,
                             tira_abertura)
import os

DIRNAME = os.path.dirname(__file__)


class NFeCabecMsg(XMLNFe):
    def __init__(self):
        super(NFeCabecMsg, self).__init__()
        self.webservice  = ''
        self.versao      = '3.10'
        self.cUF         = TagInteiro(nome='cUF'        , codigo='', raiz='//cabecMsg', tamanho=[2, 2], valor=35)
        self.versaoDados = TagDecimal(nome='versaoDados', codigo='', raiz='//cabecMsg', tamanho=[1, 4], valor='2.00')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<nfeCabecMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + '">'

        if self.versao == '3.10':
            xml += self.cUF.xml

        xml += self.versaoDados.xml
        xml += '</nfeCabecMsg>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml         = arquivo
            self.versaoDados.xml = arquivo

        return self.xml

    xml = property(get_xml, set_xml)


class NFeDadosMsg(XMLNFe):
    def __init__(self):
        super(NFeDadosMsg, self).__init__()
        self.webservice = ''
        self.dados = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<nfeDadosMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + '">'
        xml += tira_abertura(self.dados.xml)
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
        self.versao = '3.10'
        self.cUF    = None
        self.envio  = None
        self.nfeCabecMsg = NFeCabecMsg()
        self.nfeCabecMsg.versao = self.versao
        self.nfeDadosMsg = NFeDadosMsg()
        self._header = {b'content-type': b'application/soap+xml; charset=utf-8'}
        self.soap_action_webservice_e_metodo = False

    def get_xml(self):
        self.nfeCabecMsg.webservice = self.webservice
        self.nfeCabecMsg.cUF.valor = self.cUF
        self.nfeCabecMsg.versaoDados.valor = self.envio.versao.valor

        self.nfeDadosMsg.webservice = self.webservice
        self.nfeDadosMsg.dados = self.envio

        if self.soap_action_webservice_e_metodo:
            self._header[b'content-type'] = b'application/soap+xml; charset=utf-8; action="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice.encode('utf-8') + b'/' + self.metodo.encode('utf-8') + b'"'
        else:
            self._header[b'content-type'] = b'application/soap+xml; charset=utf-8; action="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice.encode('utf-8') + b'"'

        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     '<soap:Header>'
        xml +=             self.nfeCabecMsg.xml
        xml +=     '</soap:Header>'
        xml +=     '<soap:Body>'
        xml +=             self.nfeDadosMsg.xml
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
        self.nfeCabecMsg = NFeCabecMsg()
        self.resposta = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     '<soap:Header>'
        xml +=         '<nfeCabecMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + '">'
        xml +=             self.nfeCabecMsg.xml
        xml +=         '</nfeCabecMsg>'
        xml +=     '</soap:Header>'
        xml +=     '<soap:Body>'
        xml +=         '<' + self.metodo + 'Result xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + '">'
        xml +=             self.resposta.xml
        xml +=         '</' + self.metodo + 'Result>'
        xml +=     '</soap:Body>'
        xml += '</soap:Envelope>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nfeCabecMsg.xml = arquivo
            self.resposta.xml = arquivo

    xml = property(get_xml, set_xml)
