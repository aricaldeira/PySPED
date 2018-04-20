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
from uuid import uuid4
from builtins import str
from io import open


from ..nfe.processador_nfe import ProcessadorNFe, ProcessoNFe as ProcessoMDFe
from .damdfe import DAMDFE

from .webservices_flags import *
from . import webservices_3

from .leiaute import SOAPEnvio_200, SOAPRetorno_200
from .leiaute import EnviMDFe_300, RetEnviMDFe_300
from .leiaute import ConsReciMDFe_300, RetConsReciMDFe_300, ProcMDFe_300
from .leiaute import ConsSitMDFe_300, RetConsSitMDFe_300
from .leiaute import EventoEncMDFe_300, RetEventoEncMDFe_300, ProcEventoEncMDFe_300
from .leiaute import EventoCancMDFe_300, RetEventoCancMDFe_300, ProcEventoCancMDFe_300


class ProcessadorMDFe(ProcessadorNFe):
    def __init__(self):
        super().__init__()
        self.damdfe = DAMDFE()
        self.versao = '3.00'
        self.modelo = '58'

    def _configura_servico(self, servico, envio, resposta, ambiente=None, somente_ambiente_nacional=False):
        if ambiente is None:
            ambiente = self.ambiente

        webservices = webservices_3
        metodo_ws = webservices.METODO_WS

        self._soap_envio   = SOAPEnvio_200()
        self._soap_envio.versao = self.versao
        self._soap_envio.mdfeCabecMsg.versao = self.versao
        self._soap_retorno = SOAPRetorno_200()
        self._soap_envio.cUF = UF_CODIGO[self.estado]

        ws_a_usar = webservices.SVRS

        self._servidor = ws_a_usar[ambiente]['servidor']
        self._url      = ws_a_usar[ambiente][servico]

        self._soap_envio.webservice = metodo_ws[servico]['webservice']
        self._soap_envio.metodo     = metodo_ws[servico]['metodo']
        self._soap_envio.envio      = envio

        self._soap_retorno.webservice = self._soap_envio.webservice
        self._soap_retorno.metodo     = self._soap_envio.metodo
        self._soap_retorno.resposta   = resposta

    def enviar_lote(self, numero_lote=None, lista_mdfes=[]):
        envio = EnviMDFe_300()
        resposta = RetEnviMDFe_300()
        processo = ProcessoMDFe(webservice=WS_MDFE_AUTORIZACAO, envio=envio, resposta=resposta)

        #
        # Vamos assinar e validar todas as NF-e antes da transmissão, evitando
        # rejeição na SEFAZ por incorreção no schema dos arquivos
        #
        for mdfe in lista_mdfes:
            self.certificado.assina_xmlnfe(mdfe)
            mdfe.validar()

        envio.MDFe = lista_mdfes

        if numero_lote is None:
            numero_lote = datetime.now().strftime('%Y%m%d%H%M%S')

        envio.idLote.valor = numero_lote

        envio.validar()
        if self.salvar_arquivos:
            for n in lista_mdfes:
                n.monta_chave()
                arq = open(self.caminho + n.chave + '-mdfe.xml', 'w', encoding='utf-8')
                arq.write(n.xml)
                arq.close

            arq = open(self.caminho + str(envio.idLote.valor).strip().rjust(15, '0') + '-env-lot.xml', 'w')
            arq.write(envio.xml)
            arq.close()

        self._conectar_servico(WS_MDFE_AUTORIZACAO, envio, resposta)

        #resposta.validar()
        if self.salvar_arquivos:
            nome_arq = self.caminho + str(envio.idLote.valor).strip().rjust(15, '0') + '-rec'

            if resposta.cStat.valor != '103':
                nome_arq += '-rej.xml'
            else:
                nome_arq += '.xml'

            arq = open(nome_arq, 'w', encoding='utf-8')
            arq.write(resposta.xml)
            arq.close()

        return processo

    def consultar_recibo(self, ambiente=None, numero_recibo=None):
        envio = ConsReciMDFe_300()
        resposta = RetConsReciMDFe_300()

        processo = ProcessoMDFe(webservice=WS_MDFE_CONSULTA_AUTORIZACAO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        envio.tpAmb.valor = ambiente
        envio.nRec.valor  = numero_recibo

        #envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + str(envio.nRec.valor).strip().rjust(15, '0') + '-ped-rec.xml', 'w', encoding='utf-8')
            arq.write(envio.xml)
            arq.close()

        self._conectar_servico(WS_MDFE_CONSULTA_AUTORIZACAO, envio, resposta, ambiente)

        #resposta.validar()
        if self.salvar_arquivos:
            nome_arq = self.caminho + str(envio.nRec.valor).strip().rjust(15, '0') + '-pro-rec'

            if resposta.cStat.valor != '104':
                nome_arq += '-rej.xml'
            else:
                nome_arq += '.xml'

            arq = open(nome_arq, 'w', encoding='utf-8')
            arq.write(resposta.xml)
            arq.close()

            #
            # Salvar os resultados dos processamentos
            #
            for pn in resposta.protMDFe:
                nome_arq = self.caminho + str(pn.infProt.chMDFe.valor).strip().rjust(44, '0') + '-pro-mdfe-'

                # MDF-e autorizado
                if pn.infProt.cStat.valor == '100':
                    nome_arq += 'aut.xml'

                # MDF-e rejeitado
                else:
                    nome_arq += 'rej.xml'

                arq = open(nome_arq, 'w', encoding='utf-8')
                arq.write(pn.xml)
                arq.close()

        return processo

    def consultar_mdfe(self, ambiente=None, chave_mdfe=None, mdfe=None):
        envio = ConsSitMDFe_300()
        resposta = RetConsSitMDFe_300()

        processo = ProcessoMDFe(webservice=WS_MDFE_CONSULTA, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        caminho_original = self.caminho
        self.caminho = self.monta_caminho_nfe(ambiente, chave_mdfe)

        envio.tpAmb.valor = ambiente
        envio.chMDFe.valor = chave_mdfe

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + str(chave_mdfe).strip().rjust(44, '0') + '-ped-sit.xml', 'w', encoding='utf-8')
            arq.write(envio.xml)
            arq.close()

        self._conectar_servico(WS_MDFE_CONSULTA, envio, resposta, ambiente)

        #resposta.validar()
        if self.salvar_arquivos:
            nome_arq = self.caminho + str(chave_mdfe).strip().rjust(44, '0') + '-sit.xml'
            arq = open(nome_arq, 'w', encoding='utf-8')
            arq.write(resposta.xml)
            arq.close()

        self.caminho = caminho_original
        #
        # Se o MDF-e tiver sido informado, montar o processo do MDF-e
        #
        if mdfe:
           mdfe.procMDFe = self.montar_processo_um_mdfe(mdfe, protmdfe_recibo=resposta.protMDFe)

        return processo

    def processar_mdfes(self, lista_mdfes):
        #
        # Definir o caminho geral baseado na 1ª NF-e
        #
        caminho_original = self.caminho
        mdfe = lista_mdfes[0]
        mdfe.monta_chave()
        self.caminho = caminho_original
        ambiente = mdfe.infMDFe.ide.tpAmb.valor
        self.caminho = self.monta_caminho_nfe(mdfe.infMDFe.ide.tpAmb.valor, mdfe.chave)

        #
        # Verificar se os mdfes já não foram emitadas antes
        #
        for mdfe in lista_mdfes:
            mdfe.monta_chave()
            self.caminho = caminho_original
            proc_consulta = self.consultar_mdfe(ambiente=mdfe.infMDFe.ide.tpAmb.valor, chave_mdfe=mdfe.chave)
            yield proc_consulta

            #
            # Se o mdfe já constar na SEFAZ (autorizada ou denegada)
            #
            if proc_consulta.resposta.cStat.valor in ('100',):
                #
                # Interrompe todo o processo
                #
                return

        #
        # Nenhum dos mdfes estava já enviado, enviá-los então
        #
        mdfe = lista_mdfes[0]
        mdfe.monta_chave()
        self.caminho = caminho_original
        self.caminho = self.monta_caminho_nfe(mdfe.infMDFe.ide.tpAmb.valor, mdfe.chave)
        proc_envio = self.enviar_lote(lista_mdfes=lista_mdfes)
        yield proc_envio

        ret_envi_mdfe = proc_envio.resposta

        #
        # Deu errado?
        #
        if ret_envi_mdfe.cStat.valor != '103':
            #
            # Interrompe o processo
            #
            return

        #
        # Aguarda o tempo do processamento antes da consulta
        #
        time.sleep(ret_envi_mdfe.infRec.tMed.valor * 1.3)

        #
        # Consulta o recibo do lote, para ver o que aconteceu
        #
        proc_recibo = self.consultar_recibo(ambiente=ret_envi_mdfe.tpAmb.valor, numero_recibo=ret_envi_mdfe.infRec.nRec.valor)

        #
        # Tenta receber o resultado do processamento do lote, caso ainda
        # esteja em processamento
        #
        tentativa = 0
        while proc_recibo.resposta.cStat.valor == '105' and tentativa < self.maximo_tentativas_consulta_recibo:
            time.sleep(ret_envi_mdfe.infRec.tMed.valor * 1.5)
            tentativa += 1
            proc_recibo = self.consultar_recibo(ambiente=ret_envi_mdfe.tpAmb.valor, numero_recibo=ret_envi_mdfe.infRec.nRec.valor)

        # Montar os processos das NF-es
        dic_protMDFe = proc_recibo.resposta.dic_protMDFe
        dic_procMDFe = proc_recibo.resposta.dic_procMDFe

        self.caminho = caminho_original
        self.montar_processo_lista_mdfes(lista_mdfes, dic_protMDFe, dic_procMDFe)

        yield proc_recibo

    def montar_processo_lista_mdfes(self, lista_mdfes, dic_protMDFe, dic_procMDFe):
        for mdfe in lista_mdfes:
            if mdfe.chave in dic_protMDFe:
                protocolo = dic_protMDFe[mdfe.chave]
                processo = self.montar_processo_um_mdfe(mdfe, protmdfe_recibo=protocolo)

                if processo is not None:
                    dic_procMDFe[mdfe.chave] = processo

    def montar_processo_um_mdfe(self, mdfe, protmdfe_recibo=None):
        caminho_original = self.caminho
        self.caminho = self.monta_caminho_nfe(mdfe.infMDFe.ide.tpAmb.valor, mdfe.chave)

        processo = None
        #
        # Se mdfe foi autorizada ou denegada
        # 100 - autorizado
        #
        if protmdfe_recibo.infProt.cStat.valor in ('100',):
            if self.versao == '3.00':
                processo = ProcMDFe_300()

            processo.MDFe     = mdfe
            processo.protMDFe = protmdfe_recibo

            self.damdfe.MDFe     = mdfe
            self.damdfe.protMDFe = protmdfe_recibo
            self.damdfe.salvar_arquivo = False
            self.damdfe.gerar_damdfe()
            processo.damdfe_pdf = self.damdfe.conteudo_pdf

            if self.salvar_arquivos:
                nome_arq = self.caminho + str(mdfe.chave).strip().rjust(44, '0') + '-proc-mdfe.xml'
                arq = open(nome_arq, 'w', encoding='utf-8')
                arq.write(processo.xml)
                arq.close()

                if protmdfe_recibo.infProt.cStat.valor in ('100',):
                    nome_arq = self.caminho + str(mdfe.chave).strip().rjust(44, '0') + '-mdfe.xml'

                arq = open(nome_arq, 'w', encoding='utf-8')
                arq.write(processo.xml)
                arq.close()

                nome_arq = self.caminho + str(mdfe.chave).strip().rjust(44, '0') + '.pdf'
                arq = open(nome_arq, 'wb')
                arq.write(processo.damdfe_pdf)
                arq.close()

        self.caminho = caminho_original
        return processo

    def montar_processo_lista_eventos(self, lista_eventos, dic_retEvento, dic_procEvento, classe_procEvento):
        for evento in lista_eventos:
            chave = evento.infEvento.chMDFe.valor
            if chave in dic_retEvento:
                retorno = dic_retEvento[chave]
                processo = classe_procEvento()
                processo.evento = evento
                processo.retEvento = retorno
                dic_procEvento[chave] = processo

    def _enviar_evento(self, tipo_evento, evento):
        #
        # Determina o tipo do evento
        #
        if tipo_evento == 'enc':
            classe_procEvento = ProcEventoEncMDFe_300
            envio = EventoEncMDFe_300()
            resposta = RetEventoEncMDFe_300()

        elif tipo_evento == 'can':
            classe_procEvento = ProcEventoCancMDFe_300
            envio = EventoCancMDFe_300()
            resposta = RetEventoCancMDFe_300()

        #
        # Vamos assinar e validar o Evento antes da transmissão, evitando
        # rejeição na SEFAZ por incorreção no schema dos arquivos
        #
        self.certificado.assina_xmlnfe(evento)
        evento.validar()

        processo = ProcessoMDFe(webservice=WS_MDFE_RECEPCAO_EVENTO, envio=evento, resposta=resposta)

        numero_lote = datetime.now().strftime('%Y%m%d%H%M%S')

        if self.salvar_arquivos:
            chave = evento.infEvento.chMDFe.valor
            ambiente = evento.infEvento.tpAmb.valor
            caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=chave)
            numero_sequencia = evento.infEvento.nSeqEvento.valor
            nome_arq = caminho + chave + '-' + str(numero_sequencia).zfill(2)
            nome_arq += '-' + tipo_evento + '.xml'
            arq = open(nome_arq, 'w', encoding='utf-8')
            arq.write(evento.xml)
            arq.close

        self._conectar_servico(WS_MDFE_RECEPCAO_EVENTO, evento, resposta)

        #resposta.validar()
        if self.salvar_arquivos:
            chave = evento.infEvento.chMDFe.valor
            ambiente = evento.infEvento.tpAmb.valor
            caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=chave)
            numero_sequencia = evento.infEvento.nSeqEvento.valor
            nome_arq = caminho + chave + '-' + str(numero_sequencia).zfill(2)

            if resposta.infEvento.cStat.valor not in ('132', '134', '135', '136'):
                nome_arq += '-rej-' + tipo_evento
            else:
                #
                # Autorizou, vamos montar o processo
                #
                chave = evento.infEvento.chMDFe.valor
                procevento = classe_procEvento()
                procevento.eventoMDFe = evento
                procevento.retEventoMDFe = resposta
                processo.procEvento = procevento

                nome_arq += '-aut-' + tipo_evento

            nome_arq += '.xml'

            arq = open(nome_arq, 'w', encoding='utf-8')
            arq.write(resposta.xml)
            #arq.write(resposta.original.decode('utf-8'))
            arq.close()

            if resposta.infEvento.cStat.valor in ('132', '134', '135', '136'):
                chave = evento.infEvento.chMDFe.valor
                ambiente = evento.infEvento.tpAmb.valor
                caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=chave)
                numero_sequencia = evento.infEvento.nSeqEvento.valor
                nome_arq = caminho + chave + '-' + str(numero_sequencia).zfill(2)
                nome_arq += '-proc-' + tipo_evento + '.xml'

                #
                # Salva o processo do evento
                #
                arq = open(nome_arq, 'w', encoding='utf-8')
                arq.write(processo.procEvento.xml)
                arq.close

        return processo

    def enviar_cancelamento(self, evento):
        return self._enviar_evento('can', evento)

    def enviar_encerramento(self, evento):
        return self._enviar_evento('enc', evento)
