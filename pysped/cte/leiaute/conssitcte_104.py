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
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_104 as ESQUEMA_ATUAL
from pysped.cte.leiaute import ProtCTe_104, RetCancCTe_104
import os


DIRNAME = os.path.dirname(__file__)


class ConsSitCTe(XMLNFe):
    def __init__(self):
        super(ConsSitCTe, self).__init__()
        self.versao = TagDecimal(nome='consSitCTe', codigo='EP01', propriedade='versao', namespace=NAMESPACE_CTE, valor='1.04', raiz='/')
        self.tpAmb  = TagInteiro(nome='tpAmb'     , codigo='EP03', tamanho=[ 1,  1, 1], raiz='//consSitCTe', valor=2)
        self.xServ  = TagCaracter(nome='xServ'    , codigo='EP04', tamanho=[ 9,  9]   , raiz='//consSitCTe', valor='CONSULTAR')
        self.chNFe  = TagCaracter(nome='chCTe'    , codigo='EP05', tamanho=[44, 44]   , raiz='//consSitCTe')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consSitCte_v1.04.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.chNFe.xml
        xml += '</consSitNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml  = arquivo
            self.chNFe.xml  = arquivo

    xml = property(get_xml, set_xml)


class RetConsSitCTe(XMLNFe):
    def __init__(self):
        super(RetConsSitCTe, self).__init__()
        self.versao     = TagDecimal(nome='retConsSitCTe', codigo='ER01', propriedade='versao', namespace=NAMESPACE_CTE, valor='1.04', raiz='/')
        self.tpAmb      = TagInteiro(nome='tpAmb'        , codigo='ER03' , tamanho=[1,   1, 1], raiz='//retConsSitCTe')
        self.verAplic   = TagCaracter(nome='verAplic'    , codigo='ER04' , tamanho=[1,  20]   , raiz='//retConsSitCTe')
        self.cStat      = TagCaracter(nome='cStat'       , codigo='ER05' , tamanho=[1,   3]   , raiz='//retConsSitCTe')
        self.xMotivo    = TagCaracter(nome='xMotivo'     , codigo='ER06' , tamanho=[1, 2000]  , raiz='//retConsSitCTe')
        self.cUF        = TagInteiro(nome='cUF'          , codigo='ER07' , tamanho=[2,   2, 2], raiz='//retConsSitCTe')
        self.protCTe    = None
        self.retCancCTe = None
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsSitCte_v1.04.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml

        if self.protCTe is not None:
            xml += self.protCTe.xml

        if self.retCancCTe is not None:
            xml += tira_abertura(self.retCancCTe.xml)

        xml += '</retConsSitCTe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.cUF.xml       = arquivo

            if self._le_noh('//retConsSitCTe/protCTe') is not None:
                self.protCTe = ProtCTe_200()
                self.protCTe.xml = arquivo

            if self._le_noh('//retConsSitCTe/retCancCTe') is not None:
                self.retCancCTe = RetCancCTe_200()
                self.retCancCTe.xml = arquivo

    xml = property(get_xml, set_xml)
