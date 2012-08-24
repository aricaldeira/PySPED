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
from pysped.nfe.leiaute.eventonfe_100 import *

DIRNAME = os.path.dirname(__file__)


_TEXTO_FIXO = 'A Carta de Correção é disciplinada pelo § 1º-A do art. 7º do Convênio S/N, de 15 de dezembro de 1970 e pode ser utilizada para regularização de erro ocorrido na emissão de documento fiscal, desde que o erro não esteja relacionado com: I - as variáveis que determinam o valor do imposto tais como: base de cálculo, alíquota, diferença de preço, quantidade, valor da operação ou da prestação; II - a correção de dados cadastrais que implique mudança do remetente ou do destinatário; III - a data de emissão ou de saída.'

class DetEventoCCe(DetEvento):
    def __init__(self):
        super(DetEventoCCe, self).__init__()
        self.xCorrecao = TagCaracter(nome='xCorrecao', codigo='', tamanho=[15, 1000, 15], raiz='//detEvento')
        self.xCondUso = TagCaracter(nome='xCondUso', codigo='', raiz='//detEvento', valor=_TEXTO_FIXO)
        self.descEvento.valor = 'Carta de Correção'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.descEvento.xml
        xml += self.xCorrecao.xml
        xml += self.xCondUso.xml
        xml += '</detEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.descEvento.xml = arquivo
            self.xCorrecao.xml = arquivo
            self.xCondUso.xml = arquivo

    xml = property(get_xml, set_xml)


class InfEventoCCe(InfEvento):
    def __init__(self):
        super(InfEventoCCe, self).__init__()
        self.detEvento  = DetEventoCCe()
        self.tpEvento.valor = '110110'


class EventoCCe(Evento):
    def __init__(self):
        super(EventoCCe, self).__init__()
        self.infEvento = InfEventoCCe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'CCe_v1.00.xsd'


class InfEventoRecebidoCCe(InfEventoRecebido):
    def __init__(self):
        super(InfEventoRecebidoCCe, self).__init__()


class RetEventoCCe(RetEvento):
    def __init__(self):
        super(RetEventoCCe, self).__init__()


class ProcEventoCCe(ProcEvento):
    def __init__(self):
        super(ProcEventoCCe, self).__init__()
        self.evento = EventoCCe()
        self.retEvento = RetEventoCCe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procCCeNFe_v1.00.xsd'


class EnvEventoCCe(EnvEvento):
    def __init__(self):
        super(EnvEventoCCe, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'envCCe_V1.00.xsd'

    def get_xml(self):
        return super(EnvEventoCCe, self).get_xml()

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.idLote.xml    = arquivo
            self.evento = self.le_grupo('//envEvento/evento', EventoCCe)

    xml = property(get_xml, set_xml)


class RetEnvEventoCCe(RetEnvEvento):
    def __init__(self):
        super(RetEnvEventoCCe, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retEnvCCe_V1.00.xsd'
