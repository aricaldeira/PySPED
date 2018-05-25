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

NAMESPACE_EFDREINF = 'http://www.reinf.esocial.gov.br/schema/lote/eventos/envio/v1_03_02'


class DadosRecepcaoLote(XMLNFe):
    def __init__(self):
        super(DadosRecepcaoLote, self).__init__()
        self.dhRecepcao = TagCaracter(nome='dhRecepcao', raiz='//eSocial/retornoEnvioLoteEventos/dadosRecepcaoLote', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.versaoAplicativoRecepcao = TagCaracter(nome='versaoAplicativoRecepcao', raiz='//eSocial/retornoEnvioLoteEventos/dadosRecepcaoLote', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.protocoloEnvio = TagCaracter(nome='protocoloEnvio', raiz='//eSocial/retornoEnvioLoteEventos/dadosRecepcaoLote', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.dhRecepcao.valor and self.versaoAplicativoRecepcao.valor and self.protocoloEnvio.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<dadosRecepcaoLote>'
        xml += self.dhRecepcao.xml
        xml += self.versaoAplicativoRecepcao.xml
        xml += self.protocoloEnvio.xml
        xml += '</dadosRecepcaoLote>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dhRecepcao.xml = arquivo
            self.versaoAplicativoRecepcao.xml = arquivo
            self.protocoloEnvio.xml = arquivo

    xml = property(get_xml, set_xml)


class Ocorrencia(XMLNFe):
    def __init__(self):
        super(Ocorrencia, self).__init__()
        self.codigo               = TagCaracter(nome='codigo'              , raiz='//ocorrencia', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.descricao            = TagCaracter(nome='descricao'           , raiz='//ocorrencia', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.tipo                 = TagCaracter(nome='tipo'                , raiz='//ocorrencia', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.localizacaoErroAviso = TagCaracter(nome='localizacaoErroAviso', raiz='//ocorrencia', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ocorrencia>'
        xml += self.codigo.xml
        xml += self.descricao.xml
        xml += self.tipo.xml
        xml += self.localizacaoErroAviso.xml
        xml += '</ocorrencia>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codigo.xml = arquivo
            self.descricao.xml = arquivo
            self.tipo.xml = arquivo
            self.localizacaoErroAviso.xml = arquivo

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
            self.ocorrencias = self.le_grupo('//Reinf/retornoLoteEventos/status/dadosRegistroOcorrenciaLote/ocorrencias/ocorrencia', Ocorrencia, namespace=NAMESPACE_EFDREINF, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Status(XMLNFe):
    def __init__(self):
        super(Status, self).__init__()
        self.cdStatus    = TagCaracter(nome='cdStatus', raiz='//Reinf/retornoLoteEventos/status', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.descRetorno = TagCaracter(nome='descRetorno', raiz='//Reinf/retornoLoteEventos/status', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.dadosRegistroOcorrenciaLote = DadosRegistroOcorrenciaLote()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<status>'
        xml += self.cdStatus.xml
        xml += self.descRetorno.xml
        xml += self.dadosRegistroOcorrenciaLote.xml

        if len(self.ocorrencias) >= 1:
            xml += '<ocorrencias>'

            for o in self.ocorrencias:
                xml += o.xml

            xml += '</ocorrencias>'

        xml += '</status>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cdResposta.xml = arquivo
            self.descResposta.xml = arquivo
            self.ocorrencias = self.le_grupo('//eSocial/retornoEnvioLoteEventos/status/ocorrencias/ocorrencia', Ocorrencia, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeTransmissor(XMLNFe):
    def __init__(self):
        super(IdeTransmissor, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/retornoEnvioLoteEventos/ideTransmissor', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/retornoEnvioLoteEventos/ideTransmissor', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.tpInsc.valor and self.nrInsc.valor):
            return ''

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


class RetornoLoteEventos(XMLNFe):
    def __init__(self):
        super(RetornoLoteEventos, self).__init__()
        self.ideTransmissor = IdeTransmissor()
        self.status = Status()
        self.dadosRecepcaoLote = DadosRecepcaoLote()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<retornoLoteEventos>'
        xml += self.ideTransmissor.xml
        xml += self.status.xml
        xml += self.dadosRecepcaoLote.xml
        xml += '</retornoLoteEventos>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideTransmissor.xml = arquivo
            self.status.xml = arquivo
            self.dadosRecepcaoLote.xml = arquivo

    xml = property(get_xml, set_xml)


class RetornoLoteEventosEsocial(XMLNFe):
    def __init__(self):
        super(RetornoLoteEventosEsocial, self).__init__()
        self.retornoLoteEventos = RetornoLoteEventos()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'RetornoLoteEventos.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<Reinf xmlns="' + NAMESPACE_EFDREINF + '">'
        xml += self.retornoLoteEventos.xml
        xml += '</Reinf>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.retornoLoteEventos.xml = arquivo

    xml = property(get_xml, set_xml)
