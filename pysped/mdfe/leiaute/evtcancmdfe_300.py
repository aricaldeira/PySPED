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
from pysped.xml_sped import TagCaracter, XMLNFe, NAMESPACE_MDFE
from pysped.mdfe.leiaute import ESQUEMA_ATUAL_VERSAO_3 as ESQUEMA_ATUAL
from pysped.mdfe.leiaute.eventomdfe_300 import *

DIRNAME = os.path.dirname(__file__)


class EvCancMDFe(DetEvento):
    def __init__(self):
        super(EvCancMDFe, self).__init__()
        self.descEvento = TagCaracter(nome='descEvento', tamanho=[ 5,  60, 5], raiz='//evCancMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, valor='Cancelamento')
        self.nProt = TagCaracter(nome='nProt'          , tamanho=[15, 15, 15], raiz='//evCancMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.xJust = TagCaracter(nome='xJust'          , tamanho=[15, 255]   , raiz='//evCancMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)

    def get_xml(self):
        xml = '<evCancMDFe>'
        xml += self.descEvento.xml
        xml += self.nProt.xml
        xml += self.xJust.xml
        xml += '</evCancMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.descEvento.xml = arquivo
            self.nProt.xml = arquivo
            self.xJust.xml = arquivo

    xml = property(get_xml, set_xml)

class DetEventoCancMDFe(DetEvento):
    def __init__(self):
        super(DetEventoCancMDFe, self).__init__()
        self.evCancMDFe = EvCancMDFe()

    def get_xml(self):
        xml = self.versaoEvento.xml
        xml += self.evCancMDFe.xml
        xml += '</detEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versaoEvento.xml = arquivo
            self.evCancMDFe.xml = arquivo

    xml = property(get_xml, set_xml)

    @property
    def texto_formatado(self):
        txt = '<b>Motivo do cancelamento:</b><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + self.evCancMDFe.xJust.valor
        txt += '<br/><br/>'
        return txt


class InfEventoCancMDFe(InfEvento):
    def __init__(self):
        super(InfEventoCancMDFe, self).__init__()
        self.detEvento  = DetEventoCancMDFe()
        self.tpEvento.valor = '110111'


class EventoCancMDFe(Evento):
    def __init__(self):
        super(EventoCancMDFe, self).__init__()
        self.infEvento = InfEventoCancMDFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evCancMDFe_v3.00.xsd'


class InfEventoRecebidoCancMDFe(InfEventoRecebido):
    def __init__(self):
        super(InfEventoRecebidoCancMDFe, self).__init__()


class RetEventoCancMDFe(RetEvento):
    def __init__(self):
        super(RetEventoCancMDFe, self).__init__()


class ProcEventoCancMDFe(ProcEvento):
    def __init__(self):
        super(ProcEventoCancMDFe, self).__init__()
        self.eventoMDFe = EventoCancMDFe()
        self.retEventoMDFe = RetEventoCancMDFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procEventoCancMDFe_v3.00.xsd'
