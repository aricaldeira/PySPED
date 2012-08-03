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



class SOAPEnvio(XMLNFe):
    def __init__(self):
        super(SOAPEnvio, self).__init__()
        self.metodo = ''
        self.envio = None
        self._header = {'content-type': 'application/soap+xml; charset=utf-8',
            'Accept': 'application/soap+xml; charset=utf-8'}

    def get_xml(self):
        self._header['SOAPAction'] = self.metodo

        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:nfse="http://wsnfe2.dsfnet.com.br">'
        xml +=     '<soap:Body>'
        xml +=         '<nfse:' + self.metodo + '>'
        xml +=             '<mensagemXml>'
        xml += tirar_acentos(self.envio.xml)
        xml +=             '</mensagemXml>'
        xml +=         '</nfse:' + self.metodo + '>'
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
        self.metodo = ''
        self.resposta = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:nfse="http://wsnfe2.dsfnet.com.br">'
        xml +=     '<soap:Body>'
        xml +=         '<nfse:' + self.metodo + 'Response xmlns:nfse="http://wsnfe2.dsfnet.com.br">'
        xml +=             '<sr:result xmlns:sr="http://www.w3.org/2003/05/soap-rpc">'
        xml +=                 self.metodo + 'Return'
        xml +=             '</sr:result>'
        xml +=             '<' + self.metodo + 'Return>'
        xml += tirar_acentos(self.resposta.xml)
        xml +=             '</' + self.metodo + 'Return>'
        xml +=         '</nfse:' + self.metodo + 'Response>'
        xml +=     '</soap:Body>'
        xml += '</soap:Envelope>'
        return xml

    def set_xml(self, arquivo):        
        if self._le_xml(arquivo):
            resposta = por_acentos(self._le_tag('//*/' + self.metodo + 'Return'))
            resposta = tira_abertura(resposta)
            self.resposta.xml = resposta

        return self.xml

    xml = property(get_xml, set_xml)
