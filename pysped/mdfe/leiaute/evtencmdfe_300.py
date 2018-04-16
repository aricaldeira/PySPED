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

import os
from pysped.xml_sped import TagCaracter, XMLNFe, NAMESPACE_MDFE, TagData, TagInteiro
from pysped.mdfe.leiaute import ESQUEMA_ATUAL_VERSAO_3 as ESQUEMA_ATUAL
from pysped.mdfe.leiaute.eventomdfe_300 import *

DIRNAME = os.path.dirname(__file__)


class EvEncMDFe(DetEvento):
    def __init__(self):
        super(EvEncMDFe, self).__init__()
        self.descEvento = TagCaracter(nome='descEvento', tamanho=[ 5,  60, 5], raiz='//evEncMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, valor='Encerramento')
        self.nProt      = TagCaracter(nome='nProt'     , tamanho=[15, 15, 15], raiz='//evEncMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.dtEnc      = TagData(nome='dtEnc'                               , raiz='//evEncMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cUF        = TagCaracter(nome='cUF'       , tamanho=[2, 2]      , raiz='//evEncMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cMun       = TagInteiro(nome='cMun'       , tamanho=[ 7,  7, 7] , raiz='//evEncMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)

    def get_xml(self):
        xml = '<evEncMDFe>'
        xml += self.descEvento.xml
        xml += self.nProt.xml
        xml += self.dtEnc.xml
        xml += self.cUF.xml
        xml += self.cMun.xml
        xml += '</evEncMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.descEvento.xml = arquivo
            self.nProt.xml = arquivo
            self.dtEnc.xml = arquivo
            self.cUF.xml   = arquivo
            self.cMun.xml  = arquivo

    xml = property(get_xml, set_xml)


class DetEventoEncMDFe(DetEvento):
    def __init__(self):
        super(DetEventoEncMDFe, self).__init__()
        self.evEncMDFe = EvEncMDFe()

    def get_xml(self):
        xml = self.versaoEvento.xml
        xml += self.evEncMDFe.xml
        xml += '</detEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versaoEvento.xml = arquivo
            self.evEncMDFe.xml = arquivo

    xml = property(get_xml, set_xml)


class InfEventoEncMDFe(InfEvento):
    def __init__(self):
        super(InfEventoEncMDFe, self).__init__()
        self.detEvento  = DetEventoEncMDFe()
        self.tpEvento.valor = '110112'


class EventoEncMDFe(Evento):
    def __init__(self):
        super(EventoEncMDFe, self).__init__()
        self.infEvento = InfEventoEncMDFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evEncMDFe_v3.00.xsd'


class InfEventoRecebidoEncMDFe(InfEventoRecebido):
    def __init__(self):
        super(InfEventoRecebidoEncMDFe, self).__init__()


class RetEventoEncMDFe(RetEvento):
    def __init__(self):
        super(RetEventoEncMDFe, self).__init__()


class ProcEventoEncMDFe(ProcEvento):
    def __init__(self):
        super(ProcEventoEncMDFe, self).__init__()
        self.eventoMDFe = EventoEncMDFe()
        self.retEventoMDFe = RetEventoEncMDFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procEventoEncMDFe_v3.00.xsd'
