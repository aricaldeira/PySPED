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
import sys
from datetime import datetime
import time
from builtins import str
from io import open
from ..nfe.processador_nfe import ProcessadorNFe, ProcessoNFe as ProcessoESocial

from .webservices_flags import *
from . import webservices_3
from .leiaute import SOAPEnvio_10100, SOAPRetorno_10100, SOAPConsulta_10100
from .leiaute import LoteEventosEsocial_10101
from .leiaute import RetornoLoteEventosEsocial_10100
from .leiaute import ConsultaLoteEventosEsocial_10000
from .leiaute import RetornoProcessamentoLoteEsocial_10000
import pybrasil


class ProcessadorESocial(ProcessadorNFe):
    def __init__(self):
        super(ProcessadorESocial, self).__init__()
        self.tpInsc = ''
        self.nrInsc = ''
        self.certificado = pybrasil.certificado.Certificado()

    def _configura_servico(self, servico, envio, resposta, ambiente=None, somente_ambiente_nacional=False):
        if ambiente is None:
            ambiente = self.ambiente

        webservices = webservices_3
        metodo_ws = webservices.METODO_WS

        # Se for Consulta deve usar o SOAPConsulta ao invés do SOAPEnvio
        if servico == WS_ESOCIAL_CONSULTA:
            self._soap_envio = SOAPConsulta_10100()
            servidor = 'consulta'
        else:
            self._soap_envio = SOAPEnvio_10100()
            servidor = 'envio'
        self._soap_retorno = SOAPRetorno_10100()

        ws_a_usar = webservices.SVESOCIAL

        self._servidor = ws_a_usar[ambiente][servidor]
        self._url      = ws_a_usar[ambiente][servico]

        self._soap_envio.webservice = metodo_ws[servico]['webservice']
        self._soap_envio.metodo     = metodo_ws[servico]['metodo']
        self._soap_envio.envio      = envio

        self._soap_retorno.webservice = self._soap_envio.webservice
        self._soap_retorno.metodo     = self._soap_envio.metodo
        self._soap_retorno.resposta   = resposta

    def monta_caminho_esocial(self, ambiente, registro, id_evento, cnpj):
        caminho = os.path.join(self.caminho, 'esocial/')
        caminho = os.path.join(caminho, cnpj + '/')

        if ambiente == 1:
            caminho = os.path.join(caminho, 'producao/')
        else:
            caminho = os.path.join(caminho, 'homologacao/')

        if registro:
            caminho = os.path.join(caminho, registro + '/')
        caminho = os.path.join(caminho, id_evento + '/')
        try:
            os.makedirs(caminho)
        except:
            pass

        return caminho

    def enviar_lote(self, lista_eventos=[], grupo='1'):
        envio = LoteEventosEsocial_10101()
        resposta = RetornoLoteEventosEsocial_10100()

        processo = ProcessoESocial(webservice=WS_ESOCIAL_ENVIO, envio=envio, resposta=resposta)

        # Popula o grupo de Eventos conforme tabela
        # 1-Eventos de Tabela
        # 2-Eventos não Periódicos
        # 3-Eventos Periódicos
        envio.envioLoteEventos.grupo.valor = grupo

        envio.envioLoteEventos.ideEmpregador.tpInsc.valor  = self.tpInsc
        envio.envioLoteEventos.ideEmpregador.nrInsc.valor  = self.nrInsc[0:8]
        envio.envioLoteEventos.ideTransmissor.tpInsc.valor = self.tpInsc
        envio.envioLoteEventos.ideTransmissor.nrInsc.valor = self.nrInsc

        # namespaces = {
        #     'evtInfoEmpregador': 'http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v02_04_02',
        # }

        for evento in lista_eventos:
            evento.xml_assinado = self.certificado.assina_xml(evento.xml, assinar_raiz=True, metodo='sha256')

        envio.envioLoteEventos.eventos = lista_eventos
        envio.validar()

        # Salva os registros enviados pelo Lote
        if self.salvar_arquivos:
            for n in lista_eventos:
                id_evento = n.id_evento
                caminho = self.monta_caminho_esocial(
                    ambiente=self.ambiente, registro=False, id_evento=id_evento, cnpj=self.nrInsc,
                )
                arq = open(caminho + id_evento + '-envio.xml', 'w', encoding='utf-8')
                arq.write(n.xml_assinado)
                arq.close()

            # arq = open(caminho + id_evento + '-env-lot.xml', 'w')
            # arq.write(envio.xml)
            # arq.close()

        self._conectar_servico(WS_ESOCIAL_ENVIO, envio, resposta)

        # Salva o XML de envio do próprio Lote
        if self.salvar_arquivos and processo.resposta.protocoloEnvio:
            caminho = self.monta_caminho_esocial(
                ambiente=self.ambiente, registro='Lotes', id_evento=processo.resposta.protocoloEnvio, cnpj=self.nrInsc,
            )
            arq = open(caminho + processo.resposta.protocoloEnvio + '-envio.xml', 'w')
            arq.write(envio.xml)
            arq.close()

        return processo

    def consultar_lote(self, protocolo):
        envio = ConsultaLoteEventosEsocial_10000()
        resposta = RetornoProcessamentoLoteEsocial_10000()

        processo = ProcessoESocial(webservice=WS_ESOCIAL_CONSULTA, envio=envio, resposta=resposta)

        envio.consultaLoteEventos.protocoloEnvio.valor = protocolo

        envio.validar()
        # if self.salvar_arquivos:
        #     arq = open(caminho + protocolo + '-consulta.xml', 'w')
        #     arq.write(envio.xml)
        #     arq.close()

        self._conectar_servico(WS_ESOCIAL_CONSULTA, envio, resposta)

        caminho = self.monta_caminho_esocial(
            ambiente=self.ambiente, registro='Lotes', id_evento=protocolo, cnpj=self.nrInsc,
        )
        if self.salvar_arquivos:
            arq = open(caminho + protocolo + '-resposta.xml', 'w')
            arq.write(resposta.xml)
            arq.close()

        # Grava os retornos de cada registro do lote
        for evento in processo.resposta.lista_eventos:
            caminho = self.monta_caminho_esocial(
                ambiente=self.ambiente, registro=False, id_evento=evento.Id.valor, cnpj=self.nrInsc,
            )
            if evento.codigo_retorno in ['201', '202']:
                msg = '-sucesso.xml'
            else:
                msg = '-erro.xml'
            arq = open(caminho + evento.Id.valor + msg, 'w')
            arq.write(evento.xml)
            arq.close()

        return processo
