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
import os


DIRNAME = os.path.dirname(__file__)


class ConsStatServCTe(XMLNFe):
    def __init__(self):
        super(ConsStatServCTe, self).__init__()
        self.versao = TagDecimal(nome='consStatServCte', codigo='FP01', propriedade='versao', namespace=NAMESPACE_CTE, valor='1.04', raiz='/')
        self.tpAmb  = TagInteiro(nome='tpAmb'       , codigo='FP03', tamanho=[1, 1, 1], raiz='//consStatServCte', valor=2)
        self.cUF    = TagInteiro(nome='cUF'         , codigo='FP04', tamanho=[2, 2, 2], raiz='//consStatServCte', valor=35)
        self.xServ  = TagCaracter(nome='xServ'      , codigo='FP05', tamanho=[6, 6]   , raiz='//consStatServCte', valor='STATUS')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consStatServCte_v1.04.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.cUF.xml
        xml += self.xServ.xml
        xml += '</consStatServCte>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.cUF.xml    = arquivo
            self.xServ.xml  = arquivo

    xml = property(get_xml, set_xml)


class RetConsStatServCTe(XMLNFe):
    def __init__(self):
        super(RetConsStatServCTe, self).__init__()
        self.versao    = TagDecimal(nome='retConsStatServCte', codigo='FR01', propriedade='versao', namespace=NAMESPACE_CTE, valor='1.04', raiz='/')
        self.tpAmb     = TagInteiro(nome='tpAmb'          , codigo='FR03', tamanho=[1, 1, 1], raiz='//retConsStatServCte', valor=2)
        self.verAplic  = TagCaracter(nome='verAplic'      , codigo='FR04', tamanho=[1, 20]  , raiz='//retConsStatServCte')
        self.cStat     = TagCaracter(nome='cStat'         , codigo='FR05', tamanho=[3, 3, 3], raiz='//retConsStatServCte')
        self.xMotivo   = TagCaracter(nome='xMotivo'       , codigo='FR06', tamanho=[1, 255] , raiz='//retConsStatServCte')
        self.cUF       = TagInteiro(nome='cUF'            , codigo='FR07', tamanho=[2, 2, 2], raiz='//retConsStatServCte')
        self.dhRecbto  = TagDataHora(nome='dhRecbto'      , codigo='FR08',                    raiz='//retConsStatServCte')
        self.tMed      = TagInteiro(nome='tMed'           , codigo='FR09', tamanho=[1, 4]   , raiz='//retConsStatServCte', obrigatorio=False)
        self.dhRetorno = TagDataHora(nome='dhRetorno'     , codigo='FR10',                    raiz='//retConsStatServCte', obrigatorio=False)
        self.xObs      = TagCaracter(nome='xObs'          , codigo='FR11', tamanho=[1, 255] , raiz='//retConsStatServCte', obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsStatServCte_v1.04.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.dhRecbto.xml
        xml += self.tMed.xml
        xml += self.dhRetorno.xml
        xml += self.xObs.xml
        xml += '</retConsStatServCte>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.cUF.xml       = arquivo
            self.dhRecbto.xml  = arquivo
            self.tMed.xml      = arquivo
            self.dhRetorno.xml = arquivo
            self.xObs.xml      = arquivo

    xml = property(get_xml, set_xml)
