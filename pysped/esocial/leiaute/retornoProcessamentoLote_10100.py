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
from .evtBasesTrab_20402 import S5001
from .evtIrrfBenef_20402 import S5002
from .evtCS_20402 import S5011
from .evtIrrf import S5012

DIRNAME = os.path.dirname(__file__)

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/lote/eventos/envio/retornoProcessamento/v1_3_0'
NAMESPACE_ESOCIAL_RETORNO_EVENTO = 'http://www.esocial.gov.br/schema/evt/retornoEvento/v1_2_0'
NAMESPACE_ESOCIAL_S5001 = 'http://www.esocial.gov.br/schema/evt/evtBasesTrab/v02_04_02'
NAMESPACE_ESOCIAL_S5002 = 'http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v02_04_02'
NAMESPACE_ESOCIAL_S5011 = 'http://www.esocial.gov.br/schema/evt/evtCS/v02_04_02'
NAMESPACE_ESOCIAL_S5012 = 'http://www.esocial.gov.br/schema/evt/evtIrrf/v02_04_02'


class Recibo(XMLNFe):
    def __init__(self):
        super(Recibo, self).__init__()
        self.nrRecibo    = TagCaracter(nome='nrRecibo', raiz='//recibo', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)
        self.hash        = TagCaracter(nome='hash'    , raiz='//recibo', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<recibo>'
        xml += self.nrRecibo.xml
        xml += self.hash.xml
        xml += '</recibo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRecibo.xml = arquivo
            self.hash.xml = arquivo

    xml = property(get_xml, set_xml)


class Ocorrencia2(XMLNFe):
    def __init__(self):
        super(Ocorrencia2, self).__init__()
        self.codigo      = TagCaracter(nome='codigo'     , raiz='//ocorrencia', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)
        self.descricao   = TagCaracter(nome='descricao'  , raiz='//ocorrencia', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)
        self.tipo        = TagCaracter(nome='tipo'       , raiz='//ocorrencia', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)
        self.localizacao = TagCaracter(nome='localizacao', raiz='//ocorrencia', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False, obrigatorio=False)

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


class Processamento(XMLNFe):
    def __init__(self):
        super(Processamento, self).__init__()
        self.cdResposta   = TagCaracter(nome='cdResposta', raiz='//eSocial/retornoEvento/processamento', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)
        self.descResposta = TagCaracter(nome='descResposta', raiz='//eSocial/retornoEvento/processamento', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)
        self.versaoAppProcessamento = TagCaracter(nome='versaoAppProcessamento', raiz='//eSocial/retornoEvento/processamento', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)
        self.dhProcessamento = TagCaracter(nome='dhProcessamento', raiz='//eSocial/retornoEvento/processamento', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)
        self.ocorrencias  = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<processamento>'
        xml += self.cdResposta.xml
        xml += self.descResposta.xml
        xml += self.versaoAppProcessamento.xml
        xml += self.dhProcessamento.xml
        if len(self.ocorrencias) >= 1:
            xml += '<ocorrencias>'

            for o in self.ocorrencias:
                xml += o.xml

            xml += '</ocorrencias>'

        xml += '</processamento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cdResposta.xml = arquivo
            self.descResposta.xml = arquivo
            self.versaoAppProcessamento.xml = arquivo
            self.dhProcessamento.xml = arquivo
            self.ocorrencias = self.le_grupo('//eSocial/retornoEvento/processamento/ocorrencias/ocorrencia', Ocorrencia2, namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Recepcao(XMLNFe):
    def __init__(self):
        super(Recepcao, self).__init__()
        self.tpAmb = TagInteiro(nome='tpAmb', raiz='//eSocial/retornoEvento/recepcao', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False, valor=2)
        self.dhRecepcao = TagCaracter(nome='dhRecepcao', raiz='//eSocial/retornoEvento/recepcao', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)
        self.versaoAppRecepcao = TagCaracter(nome='versaoAppRecepcao', raiz='//eSocial/retornoEvento/recepcao', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)
        self.protocoloEnvioLote = TagCaracter(nome='protocoloEnvioLote', raiz='//eSocial/retornoEvento/recepcao', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<recepcao>'
        xml += self.tpAmb.xml
        xml += self.dhRecepcao.xml
        xml += self.versaoAppRecepcao.xml
        xml += self.protocoloEnvioLote.xml
        xml += '</recepcao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpAmb.xml = arquivo
            self.dhRecepcao.xml = arquivo
            self.versaoAppRecepcao.xml = arquivo
            self.protocoloEnvioLote.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEmpregador2(XMLNFe):
    def __init__(self):
        super(IdeEmpregador2, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/retornoEvento/ideEmpregador', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/retornoEvento/ideEmpregador', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)

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


class RetornoEvento2(XMLNFe):
    def __init__(self):
        super(RetornoEvento2, self).__init__()
        self.Id = TagCaracter(nome='retornoEvento', propriedade='Id', raiz='//eSocial', namespace=NAMESPACE_ESOCIAL_RETORNO_EVENTO, namespace_obrigatorio=False)
        self.ideEmpregador = IdeEmpregador2()
        self.recepcao = Recepcao()
        self.processamento = Processamento()
        self.recibo = Recibo()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        # xml += '<retornoEvento>'
        xml += self.Id.xml
        xml += self.ideEmpregador.xml
        xml += self.recepcao.xml
        xml += self.processamento.xml
        xml += self.recibo.xml
        xml += '</retornoEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.recepcao.xml = arquivo
            self.processamento.xml = arquivo
            self.recibo.xml = arquivo

    xml = property(get_xml, set_xml)


class Tot(XMLNFe):
    def __init__(self):
        super(Tot, self).__init__()
        self.tipo = TagCaracter(nome='tot', propriedade='tipo', raiz='/', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.eSocial = S5001()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.tipo.xml
        xml += self.eSocial.xml
        xml += '</tot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tipo.xml = arquivo
            if self.tipo.valor == 'S5001':
                self.eSocial = S5001()
            if self.tipo.valor == 'S5002':
                self.eSocial = S5002()
            if self.tipo.valor == 'S5011':
                self.eSocial = S5011()
            if self.tipo.valor == 'S5012':
                self.eSocial = S5012()
            if self.tipo.valor:
                self.eSocial.xml = self._le_nohs('//tot', ns=NAMESPACE_ESOCIAL)[0][0]

    xml = property(get_xml, set_xml)


class ESocial(XMLNFe):
    def __init__(self):
        super(ESocial, self).__init__()
        self.retornoEvento = RetornoEvento2()
        self.Signature = Signature()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL_RETORNO_EVENTO + '">'
        xml += self.retornoEvento.xml
        xml += self.Signature.xml
        xml += '</eSocial>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.retornoEvento.xml = arquivo
            self.Signature.xml = self._le_noh('//sig:Signature')

    xml = property(get_xml, set_xml)


class RetornoEvento(XMLNFe):
    def __init__(self):
        super(RetornoEvento, self).__init__()
        self.eSocial = ESocial()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<retornoEvento>'
        xml += self.eSocial.xml
        xml += '</retornoEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.eSocial.xml = self._le_nohs('//evento/retornoEvento', ns=NAMESPACE_ESOCIAL)[0][0]

    xml = property(get_xml, set_xml)


class Evento(XMLNFe):
    def __init__(self):
        super(Evento, self).__init__()
        self.Id = TagCaracter(nome='evento', propriedade='Id', raiz='/', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.retornoEvento = RetornoEvento()
        self.tot = []
        self.resposta = self.retornoEvento.eSocial.retornoEvento.processamento.cdResposta.valor
        self.descricao = self.retornoEvento.eSocial.retornoEvento.processamento.descResposta.valor
        self.ocorrencias = self.retornoEvento.eSocial.retornoEvento.processamento.ocorrencias
        self.totalizadores = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.retornoEvento.xml
        if len(self.tot) > 0:
            for t in self.tot:
                xml += t.xml
        xml += '</evento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.retornoEvento.xml = arquivo
            self.totalizadores = self._le_nohs('//tot', ns=NAMESPACE_ESOCIAL)
            if self.totalizadores and len(self.totalizadores) > 0:
                for t in self.totalizadores:
                    tot = Tot()
                    tot.xml = t
                    self.tot.append(tot)

    xml = property(get_xml, set_xml)

    @property
    def codigo_retorno(self):
        return self.retornoEvento.eSocial.retornoEvento.processamento.cdResposta.valor

    @property
    def descricao_retorno(self):
        return self.retornoEvento.eSocial.retornoEvento.processamento.descResposta.valor

    @property
    def recibo(self):
        return self.retornoEvento.eSocial.retornoEvento.recibo.nrRecibo.valor

    @property
    def hash(self):
        return self.retornoEvento.eSocial.retornoEvento.recibo.hash.valor

    @property
    def lista_ocorrencias(self):
        ocorrencias = []
        if self.retornoEvento.eSocial.retornoEvento.processamento.ocorrencias:
            for ocorrencia in self.retornoEvento.eSocial.retornoEvento.processamento.ocorrencias:
                ocorrencias.append({
                    'tipo': ocorrencia.tipo.valor,
                    'codigo': ocorrencia.codigo.valor,
                    'descricao': ocorrencia.descricao.valor,
                    'localizacao': ocorrencia.localizacao.valor,
                })

        return ocorrencias

    @property
    def dh_processamento(self):
        return self.retornoEvento.eSocial.retornoEvento.processamento.dhProcessamento.valor


class DadosProcessamentoLote(XMLNFe):
    def __init__(self):
        super(DadosProcessamentoLote, self).__init__()
        self.versaoAplicativoProcessamentoLote = TagCaracter(nome='versaoAplicativoProcessamentoLote', raiz='//eSocial/retornoProcessamentoLoteEventos/dadosProcessamentoLote', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        if not (self.versaoAplicativoProcessamentoLote.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<dadosProcessamentoLote>'
        xml += self.versaoAplicativoProcessamentoLote.xml
        xml += '</dadosProcessamentoLote>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versaoAplicativoProcessamentoLote.xml = arquivo

    xml = property(get_xml, set_xml)


class DadosRecepcaoLote(XMLNFe):
    def __init__(self):
        super(DadosRecepcaoLote, self).__init__()
        self.dhRecepcao = TagCaracter(nome='dhRecepcao', raiz='//eSocial/retornoProcessamentoLoteEventos/dadosRecepcaoLote', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.versaoAplicativoRecepcao = TagCaracter(nome='versaoAplicativoRecepcao', raiz='//eSocial/retornoProcessamentoLoteEventos/dadosRecepcaoLote', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.protocoloEnvio = TagCaracter(nome='protocoloEnvio', raiz='//eSocial/retornoProcessamentoLoteEventos/dadosRecepcaoLote', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.cdResposta   = TagCaracter(nome='cdResposta', raiz='//eSocial/retornoProcessamentoLoteEventos/status', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.descResposta = TagCaracter(nome='descResposta', raiz='//eSocial/retornoProcessamentoLoteEventos/status', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tempoEstimadoConclusao = TagInteiro(nome='tempoEstimadoConclusao', raiz='//eSocial/retornoProcessamentoLoteEventos/status', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.ocorrencias  = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<status>'
        xml += self.cdResposta.xml
        xml += self.descResposta.xml
        xml += self.tempoEstimadoConclusao.xml

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
            self.tempoEstimadoConclusao.xml = arquivo
            self.ocorrencias = self.le_grupo('//eSocial/retornoProcessamentoLoteEventos/status/ocorrencias/ocorrencia', Ocorrencia, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeTransmissor(XMLNFe):
    def __init__(self):
        super(IdeTransmissor, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/retornoProcessamentoLoteEventos/ideTransmissor', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/retornoProcessamentoLoteEventos/ideTransmissor', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/retornoProcessamentoLoteEventos/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/retornoProcessamentoLoteEventos/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class RetornoProcessamentoLoteEventos(XMLNFe):
    def __init__(self):
        super(RetornoProcessamentoLoteEventos, self).__init__()
        self.ideEmpregador = IdeEmpregador()
        self.ideTransmissor = IdeTransmissor()
        self.status = Status()
        self.dadosRecepcaoLote = DadosRecepcaoLote()
        self.dadosProcessamentoLote = DadosProcessamentoLote()
        self.retornoEventos = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<retornoProcessamentoLoteEventos>'
        xml += self.ideEmpregador.xml
        xml += self.ideTransmissor.xml
        xml += self.status.xml
        xml += self.dadosRecepcaoLote.xml
        xml += self.dadosProcessamentoLote.xml
        xml += '<retornoEventos>'
        for o in self.retornoEventos:
            xml += o.xml
        xml += '</retornoEventos>'

        xml += '</retornoProcessamentoLoteEventos>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideEmpregador.xml = arquivo
            self.ideTransmissor.xml = arquivo
            self.status.xml = arquivo
            self.dadosRecepcaoLote.xml = arquivo
            self.retornoEventos = self.le_grupo('//eSocial/retornoProcessamentoLoteEventos/retornoEventos/evento', Evento, namespace=NAMESPACE_ESOCIAL)

    xml = property(get_xml, set_xml)


class RetornoProcessamentoLoteEsocial(XMLNFe):
    def __init__(self):
        super(RetornoProcessamentoLoteEsocial, self).__init__()
        self.retornoProcessamentoLoteEventos = RetornoProcessamentoLoteEventos()
        self.cdResposta = ''
        self.descResposta = ''
        self.tempoEstimadoConclusao = ''
        self.dhRecepcao = ''
        self.protocoloEnvio = ''
        self.ocorrencias = []
        self.versaoAplicativoRecepcao = ''
        self.versaoAplicativoProcessamentoLote = ''
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'RetornoProcessamentoLote-v1_3_0.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.retornoProcessamentoLoteEventos.xml
        xml += '</eSocial>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.retornoProcessamentoLoteEventos.xml = arquivo
            self.cdResposta = self.retornoProcessamentoLoteEventos.status.cdResposta.valor
            self.descResposta = self.retornoProcessamentoLoteEventos.status.descResposta.valor
            self.tempoEstimadoConclusao = self.retornoProcessamentoLoteEventos.status.tempoEstimadoConclusao.valor
            self.dhRecepcao = self.retornoProcessamentoLoteEventos.dadosRecepcaoLote.dhRecepcao.valor
            self.versaoAplicativoRecepcao = self.retornoProcessamentoLoteEventos.dadosRecepcaoLote.versaoAplicativoRecepcao.valor
            self.protocoloEnvio = self.retornoProcessamentoLoteEventos.dadosRecepcaoLote.protocoloEnvio.valor
            self.ocorrencias = self.retornoProcessamentoLoteEventos.status.ocorrencias
            self.versaoAplicativoProcessamentoLote = self.retornoProcessamentoLoteEventos.dadosProcessamentoLote.versaoAplicativoProcessamentoLote.valor

    xml = property(get_xml, set_xml)

    @property
    def lista_eventos(self):
        eventos = []

        for evento in self.retornoProcessamentoLoteEventos.retornoEventos:
            eventos.append(evento)

        return eventos
