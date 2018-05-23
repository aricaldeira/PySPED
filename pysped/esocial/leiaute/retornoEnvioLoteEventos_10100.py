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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/lote/eventos/envio/retornoEnvio/v1_1_0'


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
        self.codigo      = TagCaracter(nome='codigo'     , raiz='//ocorrencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.descricao   = TagCaracter(nome='descricao'  , raiz='//ocorrencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tipo        = TagCaracter(nome='tipo'       , raiz='//ocorrencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.localizacao = TagCaracter(nome='localizacao', raiz='//ocorrencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ocorrencia>'
        xml += self.codigo.xml
        xml += self.descricao.xml
        xml += self.tipo.xml
        xml += self.localizacao.xml
        xml += '</ocorrencia>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codigo.xml = arquivo
            self.descricao.xml = arquivo
            self.tipo.xml = arquivo
            self.localizacao.xml = arquivo

    xml = property(get_xml, set_xml)


class Status(XMLNFe):
    def __init__(self):
        super(Status, self).__init__()
        self.cdResposta   = TagCaracter(nome='cdResposta', raiz='//eSocial/retornoEnvioLoteEventos/status', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.descResposta = TagCaracter(nome='descResposta', raiz='//eSocial/retornoEnvioLoteEventos/status', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ocorrencias  = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<status>'
        xml += self.cdResposta.xml
        xml += self.descResposta.xml

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


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/retornoEnvioLoteEventos/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/retornoEnvioLoteEventos/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.tpInsc.valor and self.nrInsc.valor):
            return ''

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


class RetornoEnvioLoteEventos(XMLNFe):
    def __init__(self):
        super(RetornoEnvioLoteEventos, self).__init__()
        self.ideEmpregador = IdeEmpregador()
        self.ideTransmissor = IdeTransmissor()
        self.status = Status()
        self.dadosRecepcaoLote = DadosRecepcaoLote()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<retornoEnvioLoteEventos>'
        xml += self.ideEmpregador.xml
        xml += self.ideTransmissor.xml
        xml += self.status.xml
        xml += self.dadosRecepcaoLote.xml
        xml += '</retornoEnvioLoteEventos>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideEmpregador.xml = arquivo
            self.ideTransmissor.xml = arquivo
            self.status.xml = arquivo
            self.dadosRecepcaoLote.xml = arquivo

    xml = property(get_xml, set_xml)


class RetornoLoteEventosEsocial(XMLNFe):
    def __init__(self):
        super(RetornoLoteEventosEsocial, self).__init__()
        self.retornoEnvioLoteEventos = RetornoEnvioLoteEventos()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'RetornoEnvioLoteEventos-v1_1_0.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.retornoEnvioLoteEventos.xml
        xml += '</eSocial>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.retornoEnvioLoteEventos.xml = arquivo

    xml = property(get_xml, set_xml)
