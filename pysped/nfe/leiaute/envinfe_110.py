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

from pysped.xml_sped import (ABERTURA, NAMESPACE_NFE, TagCaracter, TagDecimal,
                             TagDataHora, TagInteiro, XMLNFe, tira_abertura)
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_1 as ESQUEMA_ATUAL
import os
from .nfe_110 import NFe


DIRNAME = os.path.dirname(__file__)


class EnviNFe(XMLNFe):
    def __init__(self):
        super(EnviNFe, self).__init__()
        self.versao  = TagDecimal(nome='enviNFe', codigo='AP02', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.10', raiz='/')
        self.idLote  = TagInteiro(nome='idLote' , codigo='AP03', tamanho=[1, 15, 1], raiz='//enviNFe')
        self.NFe     = []
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'enviNFe_v1.10.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.idLote.xml

        for n in self.NFe:
            xml += tira_abertura(n.xml)

        xml += '</enviNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.idLote.xml    = arquivo
            self.NFe = self.le_grupo('//NFe', NFe)

        return self.xml

    xml = property(get_xml, set_xml)


class InfRec(XMLNFe):
    def __init__(self):
        super(InfRec, self).__init__()
        self.nRec     = TagCaracter(nome='nRec'     , codigo='AR08', tamanho=[1, 15, 1], raiz='//retEnviNFe/infRec')
        self.dhRecbto = TagDataHora(nome='dhRecbto', codigo='AR09'                    , raiz='//retEnviNFe/infRec')
        self.tMed     = TagInteiro(nome='tMed'     , codigo='AR10', tamanho=[1,  4, 1], raiz='//retEnviNFe/infRec')

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


class RetEnviNFe(XMLNFe):
    def __init__(self):
        super(RetEnviNFe, self).__init__()
        self.versao   = TagDecimal(nome='retEnviNFe', codigo='AR02' , propriedade='versao', namespace=NAMESPACE_NFE, valor='1.10', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'     , codigo='AR03' , tamanho=[1,   1, 1], raiz='//retEnviNFe')
        self.verAplic = TagCaracter(nome='verAplic' , codigo='AR04' , tamanho=[1,  20]   , raiz='//retEnviNFe')
        self.cStat    = TagCaracter(nome='cStat'    , codigo='AR05' , tamanho=[1,   3]   , raiz='//retEnviNFe')
        self.xMotivo  = TagCaracter(nome='xMotivo'  , codigo='AR06' , tamanho=[1, 255]   , raiz='//retEnviNFe')
        self.cUF      = TagCaracter(nome='cUF'      , codigo='AR06a', tamanho=[2,   2, 2], raiz='//retEnviNFe')
        self.infRec   = InfRec()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retEnviNFe_v1.10.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.infRec.xml
        xml += '</retEnviNFe>'
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
