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

from pysped.xml_sped import (ABERTURA, NAMESPACE_MDFE, TagCaracter, TagDecimal,
                             TagDataHora, TagInteiro, XMLNFe, tira_abertura, TagDataHoraUTC)
from pysped.mdfe.leiaute import ESQUEMA_ATUAL_VERSAO_3 as ESQUEMA_ATUAL
import os
from .mdfe_300 import MDFe


DIRNAME = os.path.dirname(__file__)


class EnviMDFe(XMLNFe):
    def __init__(self):
        super(EnviMDFe, self).__init__()
        self.versao  = TagDecimal(nome='enviMDFe', propriedade='versao', namespace=NAMESPACE_MDFE, valor='3.00', raiz='/')
        self.idLote  = TagInteiro(nome='idLote',tamanho=[1, 15, 1], raiz='//enviMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.MDFe     = []
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'enviMDFe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.idLote.xml

        for n in self.MDFe:
            xml += tira_abertura(n.xml)

        xml += '</enviMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.idLote.xml    = arquivo
            self.MDFe = self.le_grupo('//MDFe', MDFe, sigla_ns='mdfe')

        return self.xml

    xml = property(get_xml, set_xml)


class InfRec(XMLNFe):
    def __init__(self):
        super(InfRec, self).__init__()
        self.nRec     = TagCaracter(nome='nRec'    , tamanho=[1, 15, 1], raiz='//retEnviMDFe/infRec', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.dhRecbto = TagDataHoraUTC(nome='dhRecbto'                 , raiz='//retEnviMDFe/infRec', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.tMed     = TagInteiro(nome='tMed'     , tamanho=[1,  4, 1], raiz='//retEnviMDFe/infRec', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)

    def get_xml(self):
        if not self.nRec.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infRec>'
        xml += self.nRec.xml
        xml += self.dhRecbto.xml
        xml += self.tMed.xml
        xml += '</infRec>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nRec.xml     = arquivo
            self.dhRecbto.xml = arquivo
            self.tMed.xml     = arquivo

    xml = property(get_xml, set_xml)


class RetEnviMDFe(XMLNFe):
    def __init__(self):
        super(RetEnviMDFe, self).__init__()
        self.versao   = TagDecimal(nome='retEnviMDFe', codigo='AR02' , propriedade='versao', namespace=NAMESPACE_MDFE, valor='3.00', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'     , codigo='AR03' , tamanho=[1,   1, 1], raiz='//retEnviMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.verAplic = TagCaracter(nome='verAplic' , codigo='AR04' , tamanho=[1,  20]   , raiz='//retEnviMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cStat    = TagCaracter(nome='cStat'    , codigo='AR05' , tamanho=[1,   3]   , raiz='//retEnviMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.xMotivo  = TagCaracter(nome='xMotivo'  , codigo='AR06' , tamanho=[1, 255]   , raiz='//retEnviMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cUF      = TagCaracter(nome='cUF'      , codigo='AR06a', tamanho=[2,   2, 2], raiz='//retEnviMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.infRec   = InfRec()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retEnviMDFe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.infRec.xml
        xml += '</retEnviMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.tpAmb.xml    = arquivo
            self.verAplic.xml = arquivo
            self.cStat.xml    = arquivo
            self.xMotivo.xml  = arquivo
            self.cUF.xml      = arquivo
            self.infRec.xml   = arquivo

    xml = property(get_xml, set_xml)
