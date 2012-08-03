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


class ConsStatServ(XMLNFe):
    def __init__(self):
        super(ConsStatServ, self).__init__()
        self.versao = TagDecimal(nome='consStatServ', codigo='FP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.07', raiz='/')
        self.tpAmb  = TagInteiro(nome='tpAmb'       , codigo='FP03', tamanho=[1, 1, 1], raiz='//consStatServ', valor=2)
        self.cUF    = TagInteiro(nome='cUF'         , codigo='FP04', tamanho=[2, 2, 2], raiz='//consStatServ', valor=35)
        self.xServ  = TagCaracter(nome='xServ'      , codigo='FP05', tamanho=[6, 6]   , raiz='//consStatServ', valor='STATUS')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consStatServ_v1.07.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.cUF.xml
        xml += self.xServ.xml
        xml += '</consStatServ>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.cUF.xml    = arquivo
            self.xServ.xml  = arquivo

    xml = property(get_xml, set_xml)
    

class RetConsStatServ(XMLNFe):
    def __init__(self):
        super(RetConsStatServ, self).__init__()
        self.versao    = TagDecimal(nome='retConsStatServ', codigo='FR01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.07', raiz='/')
        self.tpAmb     = TagInteiro(nome='tpAmb'          , codigo='FR03', tamanho=[1, 1, 1], raiz='//retConsStatServ', valor=2)
        self.verAplic  = TagCaracter(nome='verAplic'      , codigo='FR04', tamanho=[1, 20]  , raiz='//retConsStatServ')
        self.cStat     = TagCaracter(nome='cStat'         , codigo='FR05', tamanho=[3, 3, 3], raiz='//retConsStatServ')
        self.xMotivo   = TagCaracter(nome='xMotivo'       , codigo='FR06', tamanho=[1, 255] , raiz='//retConsStatServ')
        self.cUF       = TagInteiro(nome='cUF'            , codigo='FR07', tamanho=[2, 2, 2], raiz='//retConsStatServ')
        self.dhRecbto  = TagDataHora(nome='dhRecbto'      , codigo='FR08',                    raiz='//retConsStatServ')
        self.tMed      = TagInteiro(nome='tMed'           , codigo='FR09', tamanho=[1, 4]   , raiz='//retConsStatServ', obrigatorio=False)
        self.dhRetorno = TagDataHora(nome='dhRetorno'     , codigo='FR10',                    raiz='//retConsStatServ', obrigatorio=False)
        self.xObs      = TagCaracter(nome='xObs'          , codigo='FR11', tamanho=[1, 255] , raiz='//retConsStatServ', obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsStatServ_v1.07.xsd'

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
        xml += '</retConsStatServ>'
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
