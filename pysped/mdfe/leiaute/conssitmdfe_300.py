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

from pysped.xml_sped import (ABERTURA, NAMESPACE_MDFE, Signature, TagCaracter,
                             TagDataHora, TagDecimal, TagInteiro, XMLNFe)
from pysped.mdfe.leiaute import ESQUEMA_ATUAL_VERSAO_3 as ESQUEMA_ATUAL
from pysped.mdfe.leiaute import ProtMDFe_300
import os


DIRNAME = os.path.dirname(__file__)


class ConsSitMDFe(XMLNFe):
    def __init__(self):
        super(ConsSitMDFe, self).__init__()
        self.versao = TagDecimal(nome='consSitMDFe', propriedade='versao', namespace=NAMESPACE_MDFE, valor='3.00', raiz='/')
        self.tpAmb  = TagInteiro(nome='tpAmb'      , tamanho=[ 1,  1, 1], raiz='//consSitMDFe', valor=2, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.xServ  = TagCaracter(nome='xServ'     , tamanho=[ 9,  9]   , raiz='//consSitMDFe', valor='CONSULTAR', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.chMDFe  = TagCaracter(nome='chMDFe'   , tamanho=[44, 44]   , raiz='//consSitMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consSitMDFe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.chMDFe.xml
        xml += '</consSitMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml  = arquivo
            self.chMDFe.xml  = arquivo

    xml = property(get_xml, set_xml)


class RetConsSitMDFe(XMLNFe):
    def __init__(self):
        super(RetConsSitMDFe, self).__init__()
        self.versao    = TagDecimal(nome='retConsSitMDFe', propriedade='versao', namespace=NAMESPACE_MDFE, valor='3.00', raiz='/')
        self.tpAmb      = TagInteiro(nome='tpAmb'        , tamanho=[1,   1, 1], raiz='//retConsSitMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.verAplic   = TagCaracter(nome='verAplic'    , tamanho=[1,  20]   , raiz='//retConsSitMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cStat      = TagCaracter(nome='cStat'       , tamanho=[1,   3]   , raiz='//retConsSitMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.xMotivo    = TagCaracter(nome='xMotivo'     , tamanho=[1, 2000]  , raiz='//retConsSitMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cUF        = TagInteiro(nome='cUF'          , tamanho=[2,   2, 2], raiz='//retConsSitMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.protMDFe    = None
        self.procEventoMDFe = None
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsSitMDFe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml

        if self.protMDFe is not None:
            xml += self.protMDFe.xml

        if self.procEventoMDFe is not None:
            for pen in self.procEventoMDFe:
                xml += tira_abertura(pen.xml)

        if len(self.Signature.URI) and (self.Signature.URI.strip() != '#'):
            xml += self.Signature.xml

        xml += '</retConsSitMDFe>'
        return xml

    def le_grupo(self, raiz_grupo):
        tags = []

        grupos = self._le_nohs(raiz_grupo, ns=NAMESPACE_MDFE)

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

            if self._le_noh('//retConsSitMDFe/protMDFe', ns=NAMESPACE_MDFE) is not None:
                self.protMDFe = ProtMDFe_300()
                self.protMDFe.xml = arquivo

            if self._le_nohs('//retConsSitMDFe/procEventoMDFe') is not None:
                self.procEventoMDFe = self.le_grupo('//retConsSitMDFe/procEventoMDFe')

            self.Signature.xml = self._le_noh('//retConsSitMDFe/sig:Signature')

    xml = property(get_xml, set_xml)
