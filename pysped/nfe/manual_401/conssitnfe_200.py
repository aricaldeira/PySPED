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
from pysped.nfe.manual_401 import ESQUEMA_ATUAL
from pysped.nfe.manual_300 import conssitnfe_107
from pysped.nfe.manual_401 import ProtNFe_200, RetCancNFe_200
import os


DIRNAME = os.path.dirname(__file__)


class ConsSitNFe(conssitnfe_107.ConsSitNFe):
    def __init__(self):
        super(ConsSitNFe, self).__init__()
        self.versao = TagDecimal(nome=u'consSitNFe', codigo=u'EP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'consSitNFe_v2.00.xsd'


class RetConsSitNFe(conssitnfe_107.RetConsSitNFe):
    def __init__(self):
        super(RetConsSitNFe, self).__init__()
        self.versao     = TagDecimal(nome=u'retConsSitNFe', codigo=u'ER01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.tpAmb      = TagInteiro(nome=u'tpAmb'        , codigo=u'ER03' , tamanho=[1,   1, 1], raiz=u'//retConsSitNFe')
        self.verAplic   = TagCaracter(nome=u'verAplic'    , codigo=u'ER04' , tamanho=[1,  20]   , raiz=u'//retConsSitNFe')
        self.cStat      = TagCaracter(nome=u'cStat'       , codigo=u'ER05' , tamanho=[1,   3]   , raiz=u'//retConsSitNFe')
        self.xMotivo    = TagCaracter(nome=u'xMotivo'     , codigo=u'ER06' , tamanho=[1, 2000]   , raiz=u'//retConsSitNFe')
        self.cUF        = TagInteiro(nome=u'cUF'          , codigo=u'ER07' , tamanho=[2,   2, 2], raiz=u'//retConsSitNFe')
        self.chNFe      = TagCaracter(nome=u'chNFe'       , codigo=u'ER07a', tamanho=[44,  44]  , raiz=u'//retConsSitNFe', obrigatorio=False)
        self.protNFe    = None
        self.retCancNFe = None
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retConsSitNFe_v2.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.chNFe.xml

        if self.protNFe is not None:
            xml += self.protNFe.xml

        if self.retCancNFe is not None:
            xml += tira_abertura(self.retCancNFe.xml)

        xml += u'</retConsSitNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.cUF.xml       = arquivo
            self.chNFe.xml     = arquivo

            if self._le_noh(u'//retConsSitNFe/protNFe') is not None:
                self.protNFe = ProtNFe_200()
                self.protNFe.xml = arquivo

            if self._le_noh(u'//retConsSitNFe/retCancNFe') is not None:
                self.retCancNFe = RetCancNFe_200()
                self.retCancNFe.xml = arquivo

    xml = property(get_xml, set_xml)

