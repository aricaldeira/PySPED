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
from .retornoTotalizadorEvento_10302 import RetornoTotalizadorEvento

DIRNAME = os.path.dirname(__file__)

NAMESPACE_LOTE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/retornoLoteEventos/v1_03_02'


# class Evento(XMLNFe):
#     def __init__(self):
#         super(Evento, self).__init__()
#         self.Id = TagCaracter(nome='evento', propriedade='id', raiz='//Reinf/retornoLoteEventos/retornoEventos', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
#         self.eventos = []
#         # self.evtTotal = RetornoTotalizadorEvento()
#
#     def get_xml(self):
#         xml = XMLNFe.get_xml(self)
#         if len(self.eventos) >= 1:
#             for evento in self.eventos:
#                 xml += evento.Id.xml
#                 xml += evento.xml
#                 xml += '</evento>'
#         return xml
#
#     def set_xml(self, arquivo):
#         if self._le_xml(arquivo):
#             self.Id.xml = arquivo
#             self.eventos = self.le_grupo('//Reinf/retornoLoteEventos/retornoEventos/evento', RetornoTotalizadorEvento, namespace=NAMESPACE_LOTE_EFDREINF, sigla_ns='res')
#         return True
#
#     xml = property(get_xml, set_xml)


class RetornoEventos(XMLNFe):
    def __init__(self):
        super(RetornoEventos, self).__init__()
        self.Id = TagCaracter(nome='retornoLoteEventos', propriedade='id', raiz='//Reinf/retornoLoteEventos', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
        self.eventos = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        # xml += '<retornoLoteEventos>'
        if len(self.eventos) >=1:
            for evento in self.eventos:
                # import ipdb; ipdb.set_trace();
                # xml += evento.Id.xml
                xml += evento.xml
                xml += '</evento>'
        xml += '</retornoLoteEventos>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            # self.evento.xml = arquivo
            self.eventos = self.le_grupo('//Reinf/retornoLoteEventos/retornoEventos/evento', RetornoTotalizadorEvento, namespace=NAMESPACE_LOTE_EFDREINF, sigla_ns='res')
        return True

    xml = property(get_xml, set_xml)


class Ocorrencias(XMLNFe):
    def __init__(self):
        super(Ocorrencias, self).__init__()
        self.codigo               = TagCaracter(nome='codigo'              , raiz='//ocorrencias', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
        self.descricao            = TagCaracter(nome='descricao'           , raiz='//ocorrencias', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
        self.tipo                 = TagCaracter(nome='tipo'                , raiz='//ocorrencias', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
        self.localizacaoErroAviso = TagCaracter(nome='localizacaoErroAviso', raiz='//ocorrencias', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ocorrencias>'
        xml += self.codigo.xml
        xml += self.descricao.xml
        xml += self.tipo.xml
        xml += self.localizacaoErroAviso.xml
        xml += '</ocorrencias>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codigo.xml = arquivo
            self.descricao.xml = arquivo
            self.tipo.xml = arquivo
            self.localizacaoErroAviso.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class DadosRegistroOcorrenciaLote(XMLNFe):
    def __init__(self):
        super(DadosRegistroOcorrenciaLote, self).__init__()
        self.ocorrencias = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosRegistroOcorrenciaLote>'
        if len(self.ocorrencias) >= 1:
            xml += '<ocorrencias>'

            for o in self.ocorrencias:
                xml += o.xml

            xml += '</ocorrencias>'

        xml += '</dadosRegistroOcorrenciaLote>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ocorrencias = self.le_grupo('//Reinf/retornoLoteEventos/status/dadosRegistroOcorrenciaLote/ocorrencias', Ocorrencias, namespace=NAMESPACE_LOTE_EFDREINF, sigla_ns='res')
        return True

    xml = property(get_xml, set_xml)


class RetornoStatus(XMLNFe):
    def __init__(self):
        super(RetornoStatus, self).__init__()
        self.cdRetorno = TagInteiro(nome='cdRetorno', tamanho=[1, 1, 1], raiz='//Reinf/retornoLoteEventos/status', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
        self.descRetorno = TagCaracter(nome='descRetorno', tamanho=[1, 255], raiz='//Reinf/retornoLoteEventos/status', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
        self.dadosRegistroOcorrenciaLote = DadosRegistroOcorrenciaLote()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<status>'
        xml += self.cdRetorno.xml
        xml += self.descRetorno.xml
        xml += self.dadosRegistroOcorrenciaLote.xml
        xml += '</status>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cdRetorno.xml = arquivo
            self.descRetorno.xml = arquivo
            self.dadosRegistroOcorrenciaLote.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class IdeTransmissor(XMLNFe):
    def __init__(self):
        super(IdeTransmissor, self).__init__()
        self.idTransmissor = TagCaracter(nome='IdTransmissor', raiz='//Reinf/retornoLoteEventos/ideTransmissor', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        if not self.idTransmissor.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ideTransmissor>'
        xml += self.idTransmissor.xml
        xml += '</ideTransmissor>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.idTransmissor.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class RetornoLoteEventos(XMLNFe):
    def __init__(self):
        super(RetornoLoteEventos, self).__init__()
        self.Id = TagCaracter(nome='retornoLoteEventos', propriedade='id', raiz='//Reinf', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
        self.ideTransmissor = IdeTransmissor()
        self.retornoStatus = RetornoStatus()
        # self.retornoEventos = RetornoEventos()
        self.retornoEventos = []
        # self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        # self.arquivo_esquema = 'RetornoLoteEventos.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Reinf xmlns="' + NAMESPACE_LOTE_EFDREINF + '">'
        xml += self.Id.xml
        xml += self.ideTransmissor.xml
        xml += self.retornoStatus.xml
        xml += '<retornoEventos>'
        if len(self.retornoEventos) >= 1:
            for r in self.retornoEventos:
                xml += r.xml
        xml += '</retornoEventos>'
        xml += '</retornoLoteEventos>'
        xml += '</Reinf>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideTransmissor.xml = arquivo
            self.retornoStatus.xml = arquivo
            self.retornoEventos = self.le_grupo('//Reinf/retornoLoteEventos/retornoEventos/evento', RetornoTotalizadorEvento, namespace=NAMESPACE_LOTE_EFDREINF, sigla_ns='res')
        return True

    xml = property(get_xml, set_xml)
