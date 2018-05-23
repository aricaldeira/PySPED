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

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str
import os
from pysped.xml_sped import *
from pysped.esocial.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

DIRNAME = os.path.dirname(__file__)

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/lote/eventos/envio/v1_1_1'


class IdeTransmissor(XMLNFe):
    def __init__(self):
        super(IdeTransmissor, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//ideTransmissor', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//ideTransmissor', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideTransmissor>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideTransmissor>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEmpregador>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideEmpregador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class EnvioLoteEventos(XMLNFe):
    def __init__(self):
        super(EnvioLoteEventos, self).__init__()
        self.grupo = TagCaracter(nome='envioLoteEventos', propriedade='grupo', valor='1', raiz='//envioLoteEventos', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEmpregador = IdeEmpregador()
        self.ideTransmissor = IdeTransmissor()
        self.eventos = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.grupo.xml
        xml += self.ideEmpregador.xml
        xml += self.ideTransmissor.xml
        xml += '<eventos>'

        for e in self.eventos:
            xml += '<evento Id="' + e.id_evento + '">'
            xml += e.xml
            xml += '</evento>'

        xml += '</eventos>'
        xml += '</envioLoteEventos>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideEmpregador.xml = arquivo
            self.ideTransmissor.xml = arquivo

    xml = property(get_xml, set_xml)


class LoteEventosEsocial(XMLNFe):
    def __init__(self):
        super(LoteEventosEsocial, self).__init__()
        self.envioLoteEventos = EnvioLoteEventos()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'EnvioLoteEventos-v1_1_1.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.envioLoteEventos.xml
        xml += '</eSocial>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.envioLoteEventos.xml = arquivo

    xml = property(get_xml, set_xml)
