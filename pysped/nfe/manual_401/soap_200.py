# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Affero General Public License,
# publicada pela Free Software Foundation, em sua versão 3 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Affero General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Affero General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import *
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


class NFeCabecMsg(XMLNFe):
    def __init__(self):
        super(NFeCabecMsg, self).__init__()
        self.webservice = u''
        self.cUF         = TagInteiro(nome=u'cUF'        , codigo=u'', raiz=u'//cabecMsg', tamanho=[2, 2], valor=35)
        self.versaoDados = TagDecimal(nome=u'versaoDados', codigo=u'', raiz=u'//cabecMsg', tamanho=[1, 4], valor=u'2.00')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<nfeCabecMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + u'">'
        xml += self.cUF.xml
        xml += self.versaoDados.xml
        xml += u'</nfeCabecMsg>'
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
        self.webservice = u''
        self.dados = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<nfeDadosMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + u'">'
        xml += tira_abertura(self.dados.xml)
        xml += u'</nfeDadosMsg>'
        return xml

    def set_xml(self, arquivo):
        pass

    xml = property(get_xml, set_xml)


class SOAPEnvio(XMLNFe):
    def __init__(self):
        super(SOAPEnvio, self).__init__()
        self.webservice = u''
        self.metodo = u''
        self.cUF    = None
        self.envio  = None
        self.nfeCabecMsg = NFeCabecMsg()
        self.nfeDadosMsg = NFeDadosMsg()
        self._header = {u'content-type': u'application/soap+xml; charset=utf-8'}

    def get_xml(self):
        self.nfeCabecMsg.webservice = self.webservice
        self.nfeCabecMsg.cUF.valor = self.cUF
        self.nfeCabecMsg.versaoDados.valor = self.envio.versao.valor

        self.nfeDadosMsg.webservice = self.webservice
        self.nfeDadosMsg.dados = self.envio

        self._header[u'content-type'] = u'application/soap+xml; charset=utf-8; action="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + u'"'

        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += u'<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     u'<soap:Header>'
        xml +=             self.nfeCabecMsg.xml
        xml +=     u'</soap:Header>'
        xml +=     u'<soap:Body>'
        xml +=             self.nfeDadosMsg.xml
        xml +=     u'</soap:Body>'
        xml += u'</soap:Envelope>'
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
        self.webservice = u''
        self.metodo = u''
        self.nfeCabecMsg = NFeCabecMsg()
        self.resposta = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += u'<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     u'<soap:Header>'
        xml +=         u'<nfeCabecMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + u'">'
        xml +=             self.nfeCabecMsg.xml
        xml +=         u'</nfeCabecMsg>'
        xml +=     u'</soap:Header>'
        xml +=     u'<soap:Body>'
        xml +=         u'<' + self.metodo + u'Result xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + u'">'
        xml +=             self.resposta.xml
        xml +=         u'</' + self.metodo + u'Result>'
        xml +=     u'</soap:Body>'
        xml += u'</soap:Envelope>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nfeCabecMsg.xml = arquivo
            self.resposta.xml = arquivo

    xml = property(get_xml, set_xml)
