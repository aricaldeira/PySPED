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
from pysped.xml_sped import TagCaracter, XMLNFe
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL
from pysped.nfe.leiaute.eventonfe_100 import (DetEvento, EnvEvento,
                                              Evento, InfEvento,
                                              InfEventoRecebido,
                                              ProcEvento,
                                              RetEvento,
                                              RetEnvEvento)
DIRNAME = os.path.dirname(__file__)


CONF_RECEBIMENTO_CONFIRMAR_OPERACAO = '210200'
CONF_RECEBIMENTO_CIENCIA_OPERACAO = '210210'
CONF_RECEBIMENTO_DESCONHECIMENTO_OPERACAO = '210220'
CONF_RECEBIMENTO_OPERACAO_NAO_REALIZADA = '210240'

DESCEVENTO_CONF_RECEBIMENTO = {
    CONF_RECEBIMENTO_CONFIRMAR_OPERACAO: 'Confirmacao da Operacao',
    CONF_RECEBIMENTO_CIENCIA_OPERACAO: 'Ciencia da Operacao',
    CONF_RECEBIMENTO_DESCONHECIMENTO_OPERACAO: 'Desconhecimento da Operacao',
    CONF_RECEBIMENTO_OPERACAO_NAO_REALIZADA: 'Operacao nao Realizada',
    }


class DetEventoConfRecebimento(DetEvento):
    def __init__(self):
        super(DetEventoConfRecebimento, self).__init__()
        self.xJust = TagCaracter(nome='xJust'  , codigo='HP20', tamanho=[15, 255]   , raiz='//detEvento', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.descEvento.xml

        #
        # A justificativa só deve ser enviada no evento CONF_RECEBIMENTO_OPERACAO_NAO_REALIZADA
        #
        if self.descEvento.valor == DESCEVENTO_CONF_RECEBIMENTO[CONF_RECEBIMENTO_OPERACAO_NAO_REALIZADA]:
            xml += self.xJust.xml

        xml += '</detEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.descEvento.xml = arquivo
            self.xJust.xml = arquivo

    xml = property(get_xml, set_xml)


class InfEventoConfRecebimento(InfEvento):
    def __init__(self):
        super(InfEventoConfRecebimento, self).__init__()
        self.detEvento  = DetEventoConfRecebimento()


class EventoConfRecebimento(Evento):
    def __init__(self):
        super(EventoConfRecebimento, self).__init__()
        self.infEvento = InfEventoConfRecebimento()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'confRecebto_v1.00.xsd'


class InfEventoRecebidoConfRecebimento(InfEventoRecebido):
    def __init__(self):
        super(InfEventoRecebidoConfRecebimento, self).__init__()


class RetEventoConfRecebimento(RetEvento):
    def __init__(self):
        super(RetEventoConfRecebimento, self).__init__()


class ProcEventoConfRecebimento(ProcEvento):
    def __init__(self):
        super(ProcEventoConfRecebimento, self).__init__()
        self.evento = EventoConfRecebimento()
        self.retEvento = RetEventoConfRecebimento()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procConfRecebtoNFe_v1.00.xsd'


class EnvEventoConfRecebimento(EnvEvento):
    def __init__(self):
        super(EnvEventoConfRecebimento, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'envConfRecebto_v1.00.xsd'

    def get_xml(self):
        return super(EnvEventoConfRecebimento, self).get_xml()

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.idLote.xml    = arquivo
            self.evento = self.le_grupo('//envEvento/evento', EventoConfRecebimento)

    xml = property(get_xml, set_xml)


class RetEnvEventoConfRecebimento(RetEnvEvento):
    def __init__(self):
        super(RetEnvEventoConfRecebimento, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retEnvConfRecebto_v1.00.xsd'
