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


class DetEventoCancNFe(DetEvento):
    def __init__(self):
        super(DetEventoCancNFe, self).__init__()
        self.nProt = TagCaracter(nome='nProt'   , codigo='CP08', tamanho=[15, 15, 15], raiz='//detEvento')
        self.xJust = TagCaracter(nome='xJust'  , codigo='CP09', tamanho=[15, 255]   , raiz='//detEvento')
        self.descEvento.valor = 'Cancelamento'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.descEvento.xml
        xml += self.nProt.xml
        xml += self.xJust.xml
        xml += '</detEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.descEvento.xml = arquivo
            self.nProt.xml = arquivo
            self.xJust.xml = arquivo

    xml = property(get_xml, set_xml)

    @property
    def texto_formatado(self):
        txt = '<b>Motivo do cancelamento:</b><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + self.xJust.valor
        txt += '<br/><br/>'
        return txt


class InfEventoCancNFe(InfEvento):
    def __init__(self):
        super(InfEventoCancNFe, self).__init__()
        self.detEvento  = DetEventoCancNFe()
        self.tpEvento.valor = '110111'


class EventoCancNFe(Evento):
    def __init__(self):
        super(EventoCancNFe, self).__init__()
        self.infEvento = InfEventoCancNFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'eventoCancNFe_v1.00.xsd'


class InfEventoRecebidoCancNFe(InfEventoRecebido):
    def __init__(self):
        super(InfEventoRecebidoCancNFe, self).__init__()


class RetEventoCancNFe(RetEvento):
    def __init__(self):
        super(RetEventoCancNFe, self).__init__()


class ProcEventoCancNFe(ProcEvento):
    def __init__(self):
        super(ProcEventoCancNFe, self).__init__()
        self.evento = EventoCancNFe()
        self.retEvento = RetEventoCancNFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procEventoCancNFe_v1.00.xsd'


class EnvEventoCancNFe(EnvEvento):
    def __init__(self):
        super(EnvEventoCancNFe, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'envEventoCancNFe_v1.00.xsd'

    def get_xml(self):
        return super(EnvEventoCancNFe, self).get_xml()

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.idLote.xml    = arquivo
            self.evento = self.le_grupo('//envEvento/evento', EventoCancNFe)

    xml = property(get_xml, set_xml)


class RetEnvEventoCancNFe(RetEnvEvento):
    def __init__(self):
        super(RetEnvEventoCancNFe, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retEnvEventoCancNFe_v1.00.xsd'
