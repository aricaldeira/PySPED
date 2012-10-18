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

import os
from pysped.xml_sped import *
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL
from pysped.nfe.leiaute import ProtNFe_200, RetCancNFe_200
from pysped.nfe.leiaute import ProcEventoCancNFe_100, ProcEventoCCe_100
from pysped.nfe.leiaute import ProcEventoConfRecebimento_100, ProcEvento_100
from pysped.nfe.leiaute import conssitnfe_200

DIRNAME = os.path.dirname(__file__)


class ConsSitNFe(conssitnfe_200.ConsSitNFe):
    def __init__(self):
        super(ConsSitNFe, self).__init__()
        self.versao = TagDecimal(nome='consSitNFe', codigo='EP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='2.01', raiz='/')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consSitNFe_v2.01.xsd'


class RetConsSitNFe(conssitnfe_200.RetConsSitNFe):
    def __init__(self):
        super(RetConsSitNFe, self).__init__()
        self.versao     = TagDecimal(nome='retConsSitNFe', codigo='ER01', propriedade='versao', namespace=NAMESPACE_NFE, valor='2.01', raiz='/')
        self.tpAmb      = TagInteiro(nome='tpAmb'        , codigo='ER03' , tamanho=[1,   1, 1], raiz='//retConsSitNFe')
        self.verAplic   = TagCaracter(nome='verAplic'    , codigo='ER04' , tamanho=[1,  20]   , raiz='//retConsSitNFe')
        self.cStat      = TagCaracter(nome='cStat'       , codigo='ER05' , tamanho=[1,   3]   , raiz='//retConsSitNFe')
        self.xMotivo    = TagCaracter(nome='xMotivo'     , codigo='ER06' , tamanho=[1, 2000]   , raiz='//retConsSitNFe')
        self.cUF        = TagInteiro(nome='cUF'          , codigo='ER07' , tamanho=[2,   2, 2], raiz='//retConsSitNFe')
        self.chNFe      = TagCaracter(nome='chNFe'       , codigo='ER07a', tamanho=[44,  44]  , raiz='//retConsSitNFe', obrigatorio=False)
        self.protNFe    = None
        self.retCancNFe = None
        self.procEventoNFe = None
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsSitNFe_v2.01.xsd'

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

        if self.procEventoNFe is not None:
            for pen in self.procEventoNFe:
                xml += tira_abertura(pen.xml)

        xml += '</retConsSitNFe>'
        return xml

    def le_grupo(self, raiz_grupo):
        tags = []

        grupos = self._le_nohs(raiz_grupo)

        if grupos is not None:
            #tags = [classe_grupo() for g in grupos]
            #for i in range(len(grupos)):
                #tags[i].xml = grupos[i]
            for g in grupos:
                tag = ProcEvento_100()
                tag.xml = g

                #
                # Aqui temos um grupo heterogêneo, com tags diferentes em cada
                # situação
                #
                if tag.evento.infEvento.tpEvento.valor == '110110':
                    tag = ProcEventoCCe_100()
                    tag.xml = g

                elif tag.evento.infEvento.tpEvento.valor == '110111':
                    tag = ProcEventoCancNFe_100()
                    tag.xml = g

                elif tag.evento.infEvento.tpEvento.valor in ('210200', '210210', '210220', '210240'):
                    tag = ProcEventoConfRecebimento_100()
                    tag.xml = g

                tags.append(tag)

        return tags

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.cUF.xml       = arquivo
            self.chNFe.xml     = arquivo

            if self._le_noh('//retConsSitNFe/protNFe') is not None:
                self.protNFe = ProtNFe_200()
                self.protNFe.xml = arquivo

            if self._le_noh('//retConsSitNFe/retCancNFe') is not None:
                self.retCancNFe = RetCancNFe_200()
                self.retCancNFe.xml = arquivo

            if self._le_nohs('//retConsSitNFe/procEventoNFe') is not None:
                self.procEventoNFe = self.le_grupo('//retConsSitNFe/procEventoNFe')

    xml = property(get_xml, set_xml)
