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
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


class ConsNFeDest(XMLNFe):
    def __init__(self):
        super(ConsNFeDest, self).__init__()
        self.versao    = TagDecimal(nome='consNFeDest', codigo='IP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.01', raiz='/')
        self.tpAmb = TagInteiro(nome='tpAmb'   , codigo='IP03', tamanho=[ 1,  1, 1] , raiz='//consNFeDest', valor=2)
        self.xServ = TagCaracter(nome='xServ'  , codigo='IP04', tamanho=[18, 18]    , raiz='//consNFeDest', valor='CONSULTAR NFE DEST')
        self.CNPJ  = TagCaracter(nome='CNPJ'  , codigo='IP05', tamanho=[14, 14], raiz='//consNFeDest')
        self.indNFe = TagInteiro(nome='indNFe'   , codigo='IP06', tamanho=[ 1,  1, 1] , raiz='//consNFeDest', valor=0)
        self.indEmi = TagInteiro(nome='indEmi'   , codigo='IP07', tamanho=[ 1,  1, 1] , raiz='//consNFeDest', valor=0)
        self.ultNSU = TagCaracter(nome='ultNSU'   , codigo='IP08', tamanho=[1, 15], raiz='//consNFeDest', valor='0')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consNFeDest_v1.01.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.CNPJ.xml
        xml += self.indNFe.xml
        xml += self.indEmi.xml
        xml += self.ultNSU.xml
        xml += '</consNFeDest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml = arquivo
            self.xServ.xml = arquivo
            self.CNPJ.xml = arquivo
            self.indNFe.xml = arquivo
            self.indEmi.xml = arquivo
            self.ultNSU.xml = arquivo

    xml = property(get_xml, set_xml)


class RetConsNFeDest(XMLNFe):
    def __init__(self):
        super(RetConsNFeDest, self).__init__()
        self.versao = TagDecimal(nome='retConsNFeDest', codigo='IR01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.01', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'         , codigo='IR03', tamanho=[1,   1, 1], raiz='//retConsNFeDest')
        self.verAplic = TagCaracter(nome='verAplic'     , codigo='IR04', tamanho=[1,  20]   , raiz='//retConsNFeDest')
        self.cStat    = TagCaracter(nome='cStat'        , codigo='IR05', tamanho=[1,   3]   , raiz='//retConsNFeDest')
        self.xMotivo  = TagCaracter(nome='xMotivo'      , codigo='IR06', tamanho=[1, 255]   , raiz='//retConsNFeDest')
        self.dhResp   = TagDataHora(nome='dhResp'       , codigo='IR07',                      raiz='//retConsNFeDest')
        self.indCont  = TagCaracter(nome='indCont'      , codigo='IR08', tamanho=[1,   1, 1], raiz='//retConsNFeDest', obrigatorio=False)
        self.ultNSU   = TagCaracter(nome='ultNSU'       , codigo='IP09', tamanho=[1, 15]    , raiz='//retConsNFeDest', obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsNFeDest_v1.01.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.dhResp.xml
        xml += self.indCont.xml
        xml += self.ultNSU.xml

        xml += '</retConsNFeDest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.tpAmb.xml   = arquivo
            self.verAplic.xml   = arquivo
            self.cStat.xml   = arquivo
            self.xMotivo.xml   = arquivo
            self.dhResp.xml   = arquivo
            self.indCont.xml   = arquivo
            self.ultNSU.xml   = arquivo

    xml = property(get_xml, set_xml)
