# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Wagner Pereira <wagner.pereira at tauga.com.br>
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
from ..nfe.processador_nfe import ProcessadorNFe, ProcessoNFe as ProcessoEFDReinf

from .webservices_flags import *
from . import webservices_3
from .leiaute import SOAPEnvio_10100, SOAPRetorno_10100
from .leiaute import LoteEventoEFDReinf_v1_03_02


class ProcessadorEFDReinf(ProcessadorNFe):
    def __init__(self):
        super(ProcessadorEFDReinf, self).__init__()

    def _configura_servico(self, servico, envio, resposta, ambiente=None, somente_ambiente_nacional=False):
        if ambiente is None:
            ambiente = self.ambiente

        webservices = webservices_3
        metodo_ws = webservices.METODO_WS

        self._soap_envio   = SOAPEnvio_10100()
        self._soap_retorno = SOAPRetorno_10100()

        ws_a_usar = webservices.SVEFDREINF

        self._servidor = ws_a_usar[ambiente]['servidor']
        self._url      = ws_a_usar[ambiente][servico]

        self._soap_envio.webservice = metodo_ws[servico]['webservice']
        self._soap_envio.metodo     = metodo_ws[servico]['metodo']
        self._soap_envio.envio      = envio

        self._soap_retorno.webservice = self._soap_envio.webservice
        self._soap_retorno.metodo     = self._soap_envio.metodo
        self._soap_retorno.resposta   = resposta

    def enviar_lote(self, lista_eventos=[]):
        envio = LoteEventoEFDReinf_v1_03_02()
        resposta = LoteEventoEFDReinf_v1_03_02()
        processo = ProcessoEFDReinf(webservice=WS_EFDREINF_ENVIO, envio=envio, resposta=resposta)
        envio.envioLoteEventos.ideContri.tpInsc.valor      = lista_eventos[0].evtInfoContri.ideContri.tpInsc.valor
        envio.envioLoteEventos.ideContri.nrInsc.valor      = lista_eventos[0].evtInfoContri.ideContri.nrInsc.valor
        envio.envioLoteEventos.ideTransmissor.tpInsc.valor = lista_eventos[0].evtInfoContri.ideContri.tpInsc.valor
        envio.envioLoteEventos.ideTransmissor.nrInsc.valor = lista_eventos[0].evtInfoContri.ideContri.nrInsc.valor

        self.ambiente = lista_eventos[0].evtInfoContri.ideEvento.tpAmb.valor
                
        for evento in lista_eventos:            
            self.certificado.assina_xmlnfe(evento)
            evento.validar()
            
        envio.envioLoteEventos.eventos = lista_eventos
        envio.validar()
        print(envio.xml)

        if self.salvar_arquivos:
            for n in lista_eventos:                
                self.caminho = self.monta_caminho_efdreinf(ambiente=self.ambiente, id_evento=n.id_evento)
                arq = open(self.caminho + n.id_evento + '.xml', 'w', encoding='utf-8')
                arq.write(n.xml)
                arq.close()
                # arq.closeConsReciEFDReinf_300

            arq = open(self.caminho + n.id_evento + '-env-lot.xml', 'w')
            arq.write(envio.xml)
            arq.close()

        self._conectar_servico(WS_EFDREINF_ENVIO, envio, resposta)
        ## resposta.validar()
        # if self.salvar_arquivos:
        #     nome_arq = self.caminho + str(envio.idLote.valor).strip().rjust(15, '0') + '-rec'
        #
        #     if resposta.cStat.valor != '103':
        #         nome_arq += '-rej.xml'
        #     else:
        #         nome_arq += '.xml'
        #
        #     arq = open(nome_arq, 'w', encoding='utf-8')
        #     arq.write(resposta.xml)
        #     arq.close()

        if self.salvar_arquivos:
            nome_arq = self.caminho + id_evento + '-rec'

            if resposta.retornoEnvioLoteEventos.status.cdResposta.valor != '201':
                nome_arq += '-rej.xml'
            else:
                nome_arq += '.xml'

            arq = open(nome_arq, 'w', encoding='utf-8')
            arq.write(resposta.xml)
            arq.close()

        return processo

    def monta_caminho_efdreinf(self, ambiente, id_evento):
        caminho = self.caminho

        if ambiente == 1:
            caminho = os.path.join(caminho, 'producao/')
        else:
            caminho = os.path.join(caminho, 'homologacao/')

        # ID2035418760001332018050212504900001
        data = '20' + id_evento[19:21] + '-' + id_evento[21:23]
        caminho = os.path.join(caminho, data + '/')
        caminho = os.path.join(caminho, id_evento + '/')
        try:
            os.makedirs(caminho)
        except:
            pass

        return caminho

    # def consultar_recibo(self, ambiente=None, numero_recibo=None):
    #     envio = ConsReciEFDReinf_300()
    #     resposta = RetConsReciEFDReinf_300()
    #
    #     processo = ProcessoEFDReinf(webservice=WS_MDFE_CONSULTA_AUTORIZACAO, envio=envio, resposta=resposta)
    #
    #     if ambiente is None:
    #         ambiente = self.ambiente
    #
    #     envio.tpAmb.valor = ambiente
    #     envio.nRec.valor  = numero_recibo
    #
    #     #envio.validar()
    #     if self.salvar_arquivos:
    #         arq = open(self.caminho + str(envio.nRec.valor).strip().rjust(15, '0') + '-ped-rec.xml', 'w', encoding='utf-8')
    #         arq.write(envio.xml)
    #         arq.close()
    #
    #     self._conectar_servico(WS_MDFE_CONSULTA_AUTORIZACAO, envio, resposta, ambiente)
    #
    #     #resposta.validar()
    #     if self.salvar_arquivos:
    #         nome_arq = self.caminho + str(envio.nRec.valor).strip().rjust(15, '0') + '-pro-rec'
    #
    #         if resposta.cStat.valor != '104':
    #             nome_arq += '-rej.xml'
    #         else:
    #             nome_arq += '.xml'
    #
    #         arq = open(nome_arq, 'w', encoding='utf-8')
    #         arq.write(resposta.xml)
    #         arq.close()
    #
    #         #
    #         # Salvar os resultados dos processamentos
    #         #
    #         for pn in resposta.protMDFe:
    #             nome_arq = self.caminho + str(pn.infProt.chMDFe.valor).strip().rjust(44, '0') + '-pro-mdfe-'
    #
    #             # MDF-e autorizado
    #             if pn.infProt.cStat.valor == '100':
    #                 nome_arq += 'aut.xml'
    #
    #             # MDF-e rejeitado
    #             else:
    #                 nome_arq += 'rej.xml'
    #
    #             arq = open(nome_arq, 'w', encoding='utf-8')
    #             arq.write(pn.xml)
    #             arq.close()
    #
    #     return processo

    # def consultar_mdfe(self, ambiente=None, chave_mdfe=None, mdfe=None):
    #
    #     # TODO Métodos do MDFe funcionam mesmo ?
    #     envio = ConsSitMDFe_300()
    #     resposta = RetConsSitMDFe_300()
    #
    #     processo = ProcessoEFDReinf(webservice=WS_MDFE_CONSULTA, envio=envio, resposta=resposta)
    #
    #     if ambiente is None:
    #         ambiente = self.ambiente
    #
    #     caminho_original = self.caminho
    #     self.caminho = self.monta_caminho_nfe(ambiente, chave_mdfe)
    #
    #     envio.tpAmb.valor = ambiente
    #     envio.chMDFe.valor = chave_mdfe
    #
    #     envio.validar()
    #     if self.salvar_arquivos:
    #         arq = open(self.caminho + str(chave_mdfe).strip().rjust(44, '0') + '-ped-sit.xml', 'w', encoding='utf-8')
    #         arq.write(envio.xml)
    #         arq.close()
    #
    #     self._conectar_servico(WS_MDFE_CONSULTA, envio, resposta, ambiente)
    #
    #     #resposta.validar()
    #     if self.salvar_arquivos:
    #         nome_arq = self.caminho + str(chave_mdfe).strip().rjust(44, '0') + '-sit.xml'
    #         arq = open(nome_arq, 'w', encoding='utf-8')
    #         arq.write(resposta.xml)
    #         arq.close()
    #
    #     self.caminho = caminho_original
    #     #
    #     # Se o MDF-e tiver sido informado, montar o processo do MDF-e
    #     #
    #     if mdfe:
    #        mdfe.procMDFe = self.montar_processo_um_mdfe(mdfe, protmdfe_recibo=resposta.protMDFe)
    #
    #     return processo

    # def processar_mdfes(self, lista_mdfes):
    #     #
    #     # Definir o caminho geral baseado na 1ª NF-e
    #     #
    #     caminho_original = self.caminho
    #     mdfe = lista_mdfes[0]
    #     mdfe.monta_chave()
    #     self.caminho = caminho_original
    #     ambiente = mdfe.infMDFe.ide.tpAmb.valor
    #     self.caminho = self.monta_caminho_nfe(mdfe.infMDFe.ide.tpAmb.valor, mdfe.chave)
    #
    #     #
    #     # Verificar se os mdfes já não foram emitadas antes
    #     #
    #     for mdfe in lista_mdfes:
    #         mdfe.monta_chave()
    #         self.caminho = caminho_original
    #         proc_consulta = self.consultar_mdfe(ambiente=mdfe.infMDFe.ide.tpAmb.valor, chave_mdfe=mdfe.chave)
    #         yield proc_consulta
    #
    #         #
    #         # Se o mdfe já constar na SEFAZ (autorizada ou denegada)
    #         #
    #         if proc_consulta.resposta.cStat.valor in ('100',):
    #             #
    #             # Interrompe todo o processo
    #             #
    #             return
    #
    #     #
    #     # Nenhum dos mdfes estava já enviado, enviá-los então
    #     #
    #     mdfe = lista_mdfes[0]
    #     mdfe.monta_chave()
    #     self.caminho = caminho_original
    #     self.caminho = self.monta_caminho_nfe(mdfe.infMDFe.ide.tpAmb.valor, mdfe.chave)
    #     proc_envio = self.enviar_lote(lista_mdfes=lista_mdfes)
    #     yield proc_envio
    #
    #     ret_envi_mdfe = proc_envio.resposta
    #
    #     #
    #     # Deu errado?
    #     #
    #     if ret_envi_mdfe.cStat.valor != '103':
    #         #
    #         # Interrompe o processo
    #         #
    #         return
    #
    #     #
    #     # Aguarda o tempo do processamento antes da consulta
    #     #
    #     time.sleep(ret_envi_mdfe.infRec.tMed.valor * 1.3)
    #
    #     #
    #     # Consulta o recibo do lote, para ver o que aconteceu
    #     #
    #     proc_recibo = self.consultar_recibo(ambiente=ret_envi_mdfe.tpAmb.valor, numero_recibo=ret_envi_mdfe.infRec.nRec.valor)
    #
    #     #
    #     # Tenta receber o resultado do processamento do lote, caso ainda
    #     # esteja em processamento
    #     #
    #     tentativa = 0
    #     while proc_recibo.resposta.cStat.valor == '105' and tentativa < self.maximo_tentativas_consulta_recibo:
    #         time.sleep(ret_envi_mdfe.infRec.tMed.valor * 1.5)
    #         tentativa += 1
    #         proc_recibo = self.consultar_recibo(ambiente=ret_envi_mdfe.tpAmb.valor, numero_recibo=ret_envi_mdfe.infRec.nRec.valor)
    #
    #     # Montar os processos das NF-es
    #     dic_protMDFe = proc_recibo.resposta.dic_protMDFe
    #     dic_procMDFe = proc_recibo.resposta.dic_procMDFe
    #
    #     self.caminho = caminho_original
    #     self.montar_processo_lista_mdfes(lista_mdfes, dic_protMDFe, dic_procMDFe)
    #
    #     yield proc_recibo
    
    # def enviar_cancelamento(self, evento):
    #     return self._enviar_evento('can', evento)
    #
    # def enviar_encerramento(self, evento):
    #     return self._enviar_evento('enc', evento)
