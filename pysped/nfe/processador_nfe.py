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
from httplib import HTTPSConnection
import socket
import ssl
from datetime import datetime
import time
from uuid import uuid4

from webservices_flags import (UF_CODIGO,
                               #WS_NFE_CANCELAMENTO,
                               WS_NFE_CONSULTA,
                               WS_NFE_CONSULTA_CADASTRO,
                               WS_NFE_CONSULTA_RECIBO,
                               WS_NFE_CONSULTA_DESTINADAS,
                               WS_NFE_DOWNLOAD,
                               WS_NFE_RECEPCAO_EVENTO,
                               WS_NFE_SITUACAO,
                               WS_NFE_ENVIO_LOTE,
                               WS_NFE_INUTILIZACAO,
                               WS_NFE_AUTORIZACAO,
                               WS_NFE_CONSULTA_AUTORIZACAO,
                               WS_DFE_DISTRIBUICAO,
                               )
import webservices_1
import webservices_2
import webservices_3
import webservices_nfce_3

from pysped.xml_sped.certificado import Certificado

#
# Manual do Contribuinte versão 2.1.00
# NF-e leiaute 1.10
#
from leiaute import SOAPEnvio_110, SOAPRetorno_110
from leiaute import EnviNFe_110, RetEnviNFe_110
from leiaute import ConsReciNFe_110, RetConsReciNFe_110, ProtNFe_110, ProcNFe_110
from leiaute import CancNFe_107, RetCancNFe_107, ProcCancNFe_107
from leiaute import InutNFe_107, RetInutNFe_107, ProcInutNFe_107
from leiaute import ConsSitNFe_107, RetConsSitNFe_107
from leiaute import ConsStatServ_107, RetConsStatServ_107
from leiaute import ConsCad_101, RetConsCad_101

#
# Manual do Contribuinte versão 4.01
# NF-e leiaute 2.00
#
from leiaute import SOAPEnvio_200, SOAPRetorno_200
from leiaute import EnviNFe_200, RetEnviNFe_200
from leiaute import ConsReciNFe_200, RetConsReciNFe_200, ProcNFe_200
from leiaute import CancNFe_200, RetCancNFe_200, ProcCancNFe_200
from leiaute import InutNFe_200, RetInutNFe_200, ProcInutNFe_200
from leiaute import ConsSitNFe_201, RetConsSitNFe_201
from leiaute import ConsStatServ_200, RetConsStatServ_200
from leiaute import ConsCad_200, RetConsCad_200

from leiaute import EventoCCe_100, EnvEventoCCe_100, RetEnvEventoCCe_100, ProcEventoCCe_100
from leiaute import EventoCancNFe_100, EnvEventoCancNFe_100, RetEnvEventoCancNFe_100, ProcEventoCancNFe_100
from leiaute import EventoConfRecebimento_100, EnvEventoConfRecebimento_100, RetEnvEventoConfRecebimento_100, ProcEventoConfRecebimento_100
from leiaute import CONF_RECEBIMENTO_CONFIRMAR_OPERACAO
from leiaute import CONF_RECEBIMENTO_CIENCIA_OPERACAO
from leiaute import CONF_RECEBIMENTO_DESCONHECIMENTO_OPERACAO
from leiaute import CONF_RECEBIMENTO_OPERACAO_NAO_REALIZADA
from leiaute import DESCEVENTO_CONF_RECEBIMENTO

from leiaute import ConsNFeDest_101, RetConsNFeDest_101
from leiaute import DownloadNFe_100, RetDownloadNFe_100, TagChNFe_100


#
# NF-e leiaute 3.10
#
from leiaute import EnviNFe_310, RetEnviNFe_310
from leiaute import ConsReciNFe_310, RetConsReciNFe_310, ProcNFe_310
from leiaute import InutNFe_310, RetInutNFe_310, ProcInutNFe_310
from leiaute import ConsSitNFe_310, RetConsSitNFe_310
from leiaute import ConsStatServ_310, RetConsStatServ_310

from leiaute import DistDFeInt_100, RetDistDFeInt_100, SOAPEnvioDistDFe_100, SOAPRetornoDistDFe_100

#
# DANFE
#
from danfe import DANFE, DAEDE, DANFCE


class ProcessoNFe(object):
    def __init__(self, webservice=0, envio='', resposta=''):
        self.webservice = webservice
        self.envio = envio
        self.resposta = resposta

    def __repr__(self):
        return 'Processo: ' + webservices_3.METODO_WS[self.webservice]['metodo']

    def __unicode__(self):
        return unicode(self.__repr__())


class ConexaoHTTPS(HTTPSConnection):
    #
    # O objetivo dessa derivação da classe HTTPSConnection é o seguinte:
    #
    # No estado do PR, o webservice deles anuncia que aceita os protocolos SSLv2 e SSLv3
    # A classe HTTPSConnection, nesse caso, assume que pode ser usado SSLv2, anunciando pelo servidor
    # MAS... se você não usar SSLv3 é impossível a conexão...
    # Bem vindos ao estado do Paraná...
    #
    #
    def connect(self):
        "Connect to a host on a given (SSL) port."

        #
        # source_address é atributo incluído na versão 2.7 do Python
        # Verificando a existência para funcionar em versões anteriores à 2.7
        #
        print(self.host, self.port, self.source_address)
        if hasattr(self, 'source_address'):
            sock = socket.create_connection((self.host, self.port), self.timeout, self.source_address)
        else:
            sock = socket.create_connection((self.host, self.port), self.timeout)

        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_TLS, do_handshake_on_connect=False)


class ProcessadorNFe(object):
    def __init__(self):
        self.ambiente = 2
        self.estado = 'SP'
        self.versao = '3.10'
        self.modelo = '55'
        self.certificado = Certificado()
        self.caminho = ''
        self.salvar_arquivos = True
        self.contingencia_SCAN = False
        self.contingencia = False
        self.danfe = DANFE()
        self.daede = DAEDE()
        self.danfce = DANFCE()
        self.caminho_temporario = ''
        self.maximo_tentativas_consulta_recibo = 5
        self.consulta_servico_ao_enviar = False

        self._servidor     = ''
        self._url          = ''
        self._soap_envio   = None
        self._soap_retorno = None

    def _conectar_servico(self, servico, envio, resposta, ambiente=None, somente_ambiente_nacional=False):
        if ambiente is None:
            ambiente = self.ambiente

        if self.versao == '1.10':
            metodo_ws = webservices_1.METODO_WS
            self._soap_envio   = SOAPEnvio_110()
            self._soap_retorno = SOAPRetorno_110()

            if self.contingencia_SCAN:
                self._servidor = webservices_1.SCAN[ambiente]['servidor']
                self._url      = webservices_1.SCAN[ambiente][servico]
            else:
                self._servidor = webservices_1.ESTADO_WS[self.estado][ambiente]['servidor']
                self._url      = webservices_1.ESTADO_WS[self.estado][ambiente][servico]

        elif self.versao == '2.00':
            metodo_ws = webservices_2.METODO_WS
            self._soap_envio   = SOAPEnvio_200()
            self._soap_retorno = SOAPRetorno_200()
            self._soap_envio.cUF = UF_CODIGO[self.estado]

            if somente_ambiente_nacional:
                self._servidor = webservices_2.AN[ambiente]['servidor']
                self._url      = webservices_2.AN[ambiente][servico]

            elif servico == WS_NFE_DOWNLOAD:
                self._servidor = webservices_2.SVAN[ambiente]['servidor']
                self._url      = webservices_2.SVAN[ambiente][servico]

            elif self.contingencia_SCAN or self.contingencia:
                self._servidor = webservices_2.ESTADO_WS_CONTINGENCIA[ambiente]['servidor']
                self._url      = webservices_2.ESTADO_WS_CONTINGENCIA[ambiente][servico]

            else:
                #
                # Testa a opção de um estado, para determinado serviço, usar o WS
                # de outro estado
                #
                if type(webservices_2.ESTADO_WS[self.estado][ambiente][servico]) == dict:
                    ws_a_usar = webservices_2.ESTADO_WS[self.estado][ambiente][servico]
                else:
                    ws_a_usar = webservices_2.ESTADO_WS[self.estado]

                self._servidor = ws_a_usar[ambiente]['servidor']
                self._url      = ws_a_usar[ambiente][servico]

        elif self.versao == '3.10':
            metodo_ws = webservices_3.METODO_WS

            if servico == WS_DFE_DISTRIBUICAO:
                self._soap_envio   = SOAPEnvioDistDFe_100()
                self._soap_retorno = SOAPRetornoDistDFe_100()

            else:
                self._soap_envio   = SOAPEnvio_200()
                self._soap_retorno = SOAPRetorno_200()

            self._soap_envio.cUF = UF_CODIGO[self.estado]

            if self.modelo == '55':
                if somente_ambiente_nacional:
                    ws_a_usar = webservices_3.AN
                if ambiente == 1 and servico == WS_DFE_DISTRIBUICAO:
                    self._servidor = 'www1.nfe.fazenda.gov.br'

                elif servico == WS_NFE_DOWNLOAD:
                    ws_a_usar = webservices_3.SVAN

                elif self.contingencia_SCAN or self.contingencia:
                    ws_a_usar = webservices_3.ESTADO_WS_CONTINGENCIA

                else:
                    #
                    # Testa a opção de um estado, para determinado serviço, usar o WS
                    # de outro estado
                    #
                    if type(webservices_3.ESTADO_WS[self.estado][ambiente][servico]) == dict:
                        ws_a_usar = webservices_3.ESTADO_WS[self.estado][ambiente][servico]
                    else:
                        ws_a_usar = webservices_3.ESTADO_WS[self.estado]

                if 'servidor%s' % servico in ws_a_usar[ambiente]:
                    self._servidor = ws_a_usar[ambiente]['servidor%s' % servico]
                else:
                    self._servidor = ws_a_usar[ambiente]['servidor']
                self._url      = ws_a_usar[ambiente][servico]

            elif self.modelo == '65':
                if self.contingencia_SCAN or self.contingencia:
                    ws_a_usar = webservices_nfce_3.ESTADO_WS_CONTINGENCIA

                else:
                    #
                    # Testa a opção de um estado, para determinado serviço, usar o WS
                    # de outro estado
                    #
                    if type(webservices_nfce_3.ESTADO_WS[self.estado][ambiente][servico]) == dict:
                        ws_a_usar = webservices_nfce_3.ESTADO_WS[self.estado][ambiente][servico]
                    else:
                        ws_a_usar = webservices_nfce_3.ESTADO_WS[self.estado]

                if 'servidor%s' % servico in ws_a_usar[ambiente]:
                    self._servidor = ws_a_usar[ambiente]['servidor%s' % servico]
                else:
                    self._servidor = ws_a_usar[ambiente]['servidor']
                self._url      = ws_a_usar[ambiente][servico]                
                
                if self.estado == 'RS' and servico == WS_NFE_CONSULTA_CADASTRO:
                    self._servidor = 'sef.sefaz.rs.gov.br'
                if (self.estado == 'SC' or self.estado == 'RJ') and servico == WS_NFE_CONSULTA_CADASTRO:
                    self._servidor = 'cad.svrs.rs.gov.br'

        self._soap_envio.webservice = metodo_ws[servico]['webservice']
        self._soap_envio.metodo     = metodo_ws[servico]['metodo']
        self._soap_envio.envio      = envio

        #
        # Ceará começou a dar pau, e não aceita o SOAPAction como os demais
        # estados...
        #
        if self.estado == 'CE' or servico == WS_DFE_DISTRIBUICAO:
            self._soap_envio.soap_action_webservice_e_metodo = True

            if servico == WS_NFE_AUTORIZACAO:
                self._soap_envio.metodo = 'nfeAutorizacaoLote'
            elif servico == WS_NFE_CONSULTA_AUTORIZACAO:
                self._soap_envio.metodo = 'nfeRetAutorizacaoLote'

        self._soap_retorno.webservice = self._soap_envio.webservice
        self._soap_retorno.metodo     = self._soap_envio.metodo
        self._soap_retorno.resposta   = resposta

        #try:
        self.certificado.prepara_certificado_arquivo_pfx()

        #
        # Salva o certificado e a chave privada para uso na conexão HTTPS
        # Salvamos como um arquivo de nome aleatório para evitar o conflito
        # de uso de vários certificados e chaves diferentes na mesma máquina
        # ao mesmo tempo
        #
        self.caminho_temporario = self.caminho_temporario or '/tmp/'

        nome_arq_chave = self.caminho_temporario + uuid4().hex
        arq_tmp = open(nome_arq_chave, 'w')
        arq_tmp.write(self.certificado.chave)
        arq_tmp.close()

        nome_arq_certificado = self.caminho_temporario + uuid4().hex
        arq_tmp = open(nome_arq_certificado, 'w')
        arq_tmp.write(self.certificado.certificado)
        arq_tmp.close()
        #import StringIO
        #nome_arq_chave = StringIO.StringIO()
        #nome_arq_chave.write(self.certificado.chave)
        #nome_arq_certificado = StringIO.StringIO()
        #nome_arq_certificado.write(self.certificado.certificado)

        #con = HTTPSConnection(self._servidor, key_file=nome_arq_chave, cert_file=nome_arq_certificado)
        con = ConexaoHTTPS(self._servidor, key_file=nome_arq_chave, cert_file=nome_arq_certificado)
        #con.request('POST', '/' + self._url, self._soap_envio.xml.decode('utf-8'), self._soap_envio.header)
        #
        # É preciso definir o POST abaixo como bytestring, já que importamos
        # os unicode_literals... Dá um pau com xml com acentos sem isso...
        #
        con.request(b'POST', b'/' + self._url.encode('utf-8'), self._soap_envio.xml.encode('utf-8'), self._soap_envio.header)
        resp = con.getresponse()

        #
        # Apagamos os arquivos do certificado e o da chave privada, para evitar
        # um potencial risco de segurança; muito embora o uso da chave privada
        # para assinatura exija o uso da senha, pode haver serviços que exijam
        # apenas o uso do certificado para validar a identidade, independente
        # da existência de assinatura digital
        #
        os.remove(nome_arq_chave)
        os.remove(nome_arq_certificado)

        # Dados do envelope de envio salvos para possível debug
        envio.original = self._soap_envio.xml

        # Dados da resposta salvos para possível debug
        self._soap_retorno.resposta.version  = resp.version
        self._soap_retorno.resposta.status   = resp.status
        self._soap_retorno.resposta.reason   = unicode(resp.reason.decode('utf-8'))
        self._soap_retorno.resposta.msg      = resp.msg
        self._soap_retorno.resposta.original = unicode(resp.read().decode('utf-8'))

        # Tudo certo!
        if self._soap_retorno.resposta.status == 200:
            self._soap_retorno.xml = self._soap_retorno.resposta.original
        #except Exception, e:
            #raise e
        #else:
        con.close()

    def enviar_lote(self, numero_lote=None, lista_nfes=[]):
        if self.versao == '1.10':
            envio = EnviNFe_110()
            resposta = RetEnviNFe_110()

        elif self.versao == '2.00':
            envio = EnviNFe_200()
            resposta = RetEnviNFe_200()

        elif self.versao == '3.10':
            envio = EnviNFe_310()
            resposta = RetEnviNFe_310()

        if self.ambiente == 2: # Homologação tem detalhes especificos desde a NT2011_002
            for nfe in lista_nfes:
                if nfe.infNFe.ide.mod.valor != 55:
                    if (not nfe.infNFe.dest.CNPJ.valor) and (not nfe.infNFe.dest.CPF.valor) and (not nfe.infNFe.dest.idEstrangeiro.valor):
                        continue

                #nfe.infNFe.dest.CNPJ.valor = '99999999000191'
                nfe.infNFe.dest.xNome.valor = 'NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL'
                #nfe.infNFe.dest.IE.valor = ''
                #if self.versao == '3.10':
                    #nfe.infNFe.dest.indIEDest.valor = '2'

        processo = ProcessoNFe(webservice=WS_NFE_ENVIO_LOTE, envio=envio, resposta=resposta)

        #
        # Vamos assinar e validar todas as NF-e antes da transmissão, evitando
        # rejeição na SEFAZ por incorreção no schema dos arquivos
        #
        for nfe in lista_nfes:
            self.certificado.assina_xmlnfe(nfe)

            if nfe.infNFe.ide.mod._valor_string == '65':
                nfe.monta_qrcode()

            nfe.validar()

        envio.NFe = lista_nfes

        if numero_lote is None:
            numero_lote = datetime.now().strftime('%Y%m%d%H%M%S')

        envio.idLote.valor = numero_lote

        envio.validar()
        if self.salvar_arquivos:
            for n in lista_nfes:
                n.monta_chave()
                arq = open(self.caminho + n.chave + '-nfe.xml', 'w')
                arq.write(n.xml.encode('utf-8'))
                arq.close

            arq = open(self.caminho + unicode(envio.idLote.valor).strip().rjust(15, '0') + '-env-lot.xml', 'w')
            arq.write(envio.xml.encode('utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_ENVIO_LOTE, envio, resposta)

        #resposta.validar()
        if self.salvar_arquivos:
            nome_arq = self.caminho + unicode(envio.idLote.valor).strip().rjust(15, '0') + '-rec'

            if resposta.cStat.valor != '103':
                nome_arq += '-rej.xml'
            else:
                nome_arq += '.xml'

            arq = open(nome_arq, 'w')
            arq.write(resposta.xml.encode('utf-8'))
            arq.close()

        return processo

    def consultar_recibo(self, ambiente=None, numero_recibo=None):
        if self.versao == '1.10':
            envio = ConsReciNFe_110()
            resposta = RetConsReciNFe_110()

        elif self.versao == '2.00':
            envio = ConsReciNFe_200()
            resposta = RetConsReciNFe_200()

        elif self.versao == '3.10':
            envio = ConsReciNFe_310()
            resposta = RetConsReciNFe_310()

        processo = ProcessoNFe(webservice=WS_NFE_CONSULTA_RECIBO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        envio.tpAmb.valor = ambiente
        envio.nRec.valor  = numero_recibo

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + unicode(envio.nRec.valor).strip().rjust(15, '0') + '-ped-rec.xml', 'w')
            arq.write(envio.xml.encode('utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_CONSULTA_RECIBO, envio, resposta, ambiente)

        #resposta.validar()
        if self.salvar_arquivos:
            nome_arq = self.caminho + unicode(envio.nRec.valor).strip().rjust(15, '0') + '-pro-rec'

            if resposta.cStat.valor != '104':
                nome_arq += '-rej.xml'
            else:
                nome_arq += '.xml'

            arq = open(nome_arq, 'w')
            arq.write(resposta.xml.encode('utf-8'))
            arq.close()

            #
            # Salvar os resultados dos processamentos
            #
            for pn in resposta.protNFe:
                nome_arq = self.caminho + unicode(pn.infProt.chNFe.valor).strip().rjust(44, '0') + '-pro-nfe-'

                # NF-e autorizada
                if pn.infProt.cStat.valor == '100':
                    nome_arq += 'aut.xml'

                # NF-e denegada
                elif pn.infProt.cStat.valor in ('110', '301', '302', '303'):
                    nome_arq += 'den.xml'

                # NF-e rejeitada
                else:
                    nome_arq += 'rej.xml'

                arq = open(nome_arq, 'w')
                arq.write(pn.xml.encode('utf-8'))
                arq.close()

        return processo

    def cancelar_nota(self, ambiente=None, chave_nfe=None, numero_protocolo=None, justificativa=None):
        raise ValueError('Cancelamento agora deve ser feito via registro de eventos')
        #if self.versao == '1.10':
            #envio = CancNFe_107()
            #resposta = RetCancNFe_107()

        #elif self.versao == '2.00':
            #envio = CancNFe_200()
            #resposta = RetCancNFe_200()

        #processo = ProcessoNFe(webservice=WS_NFE_CANCELAMENTO, envio=envio, resposta=resposta)

        #if ambiente is None:
            #ambiente = self.ambiente

        #self.caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=chave_nfe)

        #envio.infCanc.tpAmb.valor = ambiente
        #envio.infCanc.chNFe.valor = chave_nfe
        #envio.infCanc.nProt.valor = numero_protocolo
        #envio.infCanc.xJust.valor = justificativa

        #self.certificado.assina_xmlnfe(envio)

        #envio.validar()
        #if self.salvar_arquivos:
            #arq = open(self.caminho + unicode(envio.infCanc.chNFe.valor).strip().rjust(44, '0') + '-ped-can.xml', 'w')
            #arq.write(envio.xml.encode('utf-8'))
            #arq.close()

        #self._conectar_servico(WS_NFE_CANCELAMENTO, envio, resposta, ambiente)

        ##resposta.validar()

        ##
        ## Se for autorizado, monta o processo de cancelamento
        ## 101 - cancelado dentro do prazo
        ## 151 - cancelado fora do prazo
        ##
        #if resposta.infCanc.cStat.valor in ('101', '151'):
            #if self.versao == '1.10':
                #processo_cancelamento_nfe = ProcCancNFe_107()

            #elif self.versao == '2.00':
                #processo_cancelamento_nfe = ProcCancNFe_200()

            #nome_arq = self.caminho + unicode(envio.infCanc.chNFe.valor).strip().rjust(44, '0') + '-proc-canc-nfe.xml'
            #processo_cancelamento_nfe.cancNFe = envio
            #processo_cancelamento_nfe.retCancNFe = resposta

            #processo_cancelamento_nfe.validar()

            #processo.processo_cancelamento_nfe = processo_cancelamento_nfe

        #if self.salvar_arquivos:
            #nome_arq = self.caminho + unicode(envio.infCanc.chNFe.valor).strip().rjust(44, '0') + '-pro-can-'

            ## Cancelamento autorizado
            #if resposta.infCanc.cStat.valor == '101':
                #nome_arq += 'aut.xml'
            #else:
                #nome_arq += 'rej.xml'

            #arq = open(nome_arq, 'w')
            #arq.write(resposta.xml.encode('utf-8'))
            #arq.close()

            ## Se for autorizado, monta o processo de cancelamento
            #if resposta.infCanc.cStat.valor == '101':
                #nome_arq = self.caminho + unicode(envio.infCanc.chNFe.valor).strip().rjust(44, '0') + '-proc-canc-nfe.xml'
                #arq = open(nome_arq, 'w')
                #arq.write(processo_cancelamento_nfe.xml.encode('utf-8'))
                #arq.close()

                ## Estranhamente, o nome desse arquivo, pelo manual, deve ser chave-can.xml
                #nome_arq = self.caminho + unicode(envio.infCanc.chNFe.valor).strip().rjust(44, '0') + '-can.xml'
                #arq = open(nome_arq, 'w')
                #arq.write(processo_cancelamento_nfe.xml.encode('utf-8'))
                #arq.close()

        #return processo

    def inutilizar_nota(self, ambiente=None, codigo_estado=None, ano=None, cnpj=None, serie=None, numero_inicial=None, numero_final=None, justificativa=None):
        if self.versao == '1.10':
            envio = InutNFe_107()
            resposta = RetInutNFe_107()

        elif self.versao == '2.00':
            envio = InutNFe_200()
            resposta = RetInutNFe_200()

        elif self.versao == '3.10':
            envio = InutNFe_310()
            resposta = RetInutNFe_310()

        processo = ProcessoNFe(webservice=WS_NFE_INUTILIZACAO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        if codigo_estado is None:
            codigo_estado = UF_CODIGO[self.estado]

        if ano is None:
            ano = datetime.now().strftime('%y')

        if numero_final is None:
            numero_final = numero_inicial

        self.caminho = self.monta_caminho_inutilizacao(ambiente=ambiente, serie=serie, numero_inicial=numero_inicial, numero_final=numero_final)

        envio.infInut.tpAmb.valor  = ambiente
        envio.infInut.cUF.valor    = codigo_estado
        envio.infInut.ano.valor    = ano
        envio.infInut.CNPJ.valor   = cnpj
        envio.infInut.mod.valor    = int(self.modelo)
        envio.infInut.serie.valor  = serie
        envio.infInut.nNFIni.valor = numero_inicial
        envio.infInut.nNFFin.valor = numero_final
        envio.infInut.xJust.valor  = justificativa

        envio.gera_nova_chave()
        self.certificado.assina_xmlnfe(envio)

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + unicode(envio.chave).strip().rjust(41, '0') + '-ped-inu.xml', 'w')
            arq.write(envio.xml.encode('utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_INUTILIZACAO, envio, resposta, ambiente)

        #resposta.validar()

        # Se for autorizada, monta o processo de inutilização
        if resposta.infInut.cStat.valor == '102':
            if self.versao == '1.10':
                processo_inutilizacao_nfe = ProcInutNFe_107()

            elif self.versao == '2.00':
                processo_inutilizacao_nfe = ProcInutNFe_200()

            elif self.versao == '3.10':
                processo_inutilizacao_nfe = ProcInutNFe_310()

            processo_inutilizacao_nfe.inutNFe = envio
            processo_inutilizacao_nfe.retInutNFe = resposta

            processo_inutilizacao_nfe.validar()

            processo.processo_inutilizacao_nfe = processo_inutilizacao_nfe

        if self.salvar_arquivos:
            nome_arq = self.caminho + unicode(envio.chave).strip().rjust(41, '0') + '-pro-inu-'

            # Inutilização autorizada
            if resposta.infInut.cStat.valor == '102':
                nome_arq += 'aut.xml'
            else:
                nome_arq += 'rej.xml'

            arq = open(nome_arq, 'w')
            arq.write(resposta.xml.encode('utf-8'))
            arq.close()

            # Se for autorizada, monta o processo de inutilização
            if resposta.infInut.cStat.valor == '102':
                nome_arq = self.caminho + unicode(envio.chave).strip().rjust(41, '0') + '-proc-inut-nfe.xml'
                arq = open(nome_arq, 'w')
                arq.write(processo_inutilizacao_nfe.xml.encode('utf-8'))
                arq.close()

                # Estranhamente, o nome desse arquivo, pelo manual, deve ser chave-inu.xml
                nome_arq = self.caminho + unicode(envio.chave).strip().rjust(41, '0') + '-inu.xml'
                arq = open(nome_arq, 'w')
                arq.write(processo_inutilizacao_nfe.xml.encode('utf-8'))
                arq.close()

        return processo

    def consultar_nota(self, ambiente=None, chave_nfe=None, nfe=None):
        if self.versao == '1.10':
            envio = ConsSitNFe_107()
            resposta = RetConsSitNFe_107()

        elif self.versao == '2.00':
            envio = ConsSitNFe_201()
            resposta = RetConsSitNFe_201()

        elif self.versao == '3.10':
            envio = ConsSitNFe_310()
            resposta = RetConsSitNFe_310()

        processo = ProcessoNFe(webservice=WS_NFE_CONSULTA, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        caminho_original = self.caminho
        self.caminho = self.monta_caminho_nfe(ambiente, chave_nfe)

        envio.tpAmb.valor = ambiente
        envio.chNFe.valor = chave_nfe

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + unicode(chave_nfe).strip().rjust(44, '0') + '-ped-sit.xml', 'w')
            arq.write(envio.xml.encode('utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_CONSULTA, envio, resposta, ambiente)

        #resposta.validar()
        if self.salvar_arquivos:
            nome_arq = self.caminho + unicode(chave_nfe).strip().rjust(44, '0') + '-sit.xml'
            arq = open(nome_arq, 'w')
            arq.write(resposta.xml.encode('utf-8'))
            arq.close()

        self.caminho = caminho_original
        #
        # Se a NF-e tiver sido informada, montar o processo da NF-e
        #
        if nfe:
           nfe.procNFe = self.montar_processo_uma_nota(nfe, protnfe_recibo=resposta.protNFe)

        return processo

    def consultar_servico(self, ambiente=None, codigo_estado=None):
        if self.versao == '1.10':
            envio = ConsStatServ_107()
            resposta = RetConsStatServ_107()

        elif self.versao == '2.00':
            envio = ConsStatServ_200()
            resposta = RetConsStatServ_200()

        elif self.versao == '3.10':
            envio = ConsStatServ_310()
            resposta = RetConsStatServ_310()

        processo = ProcessoNFe(webservice=WS_NFE_SITUACAO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        if codigo_estado is None:
            codigo_estado = UF_CODIGO[self.estado]

        envio.tpAmb.valor = ambiente
        envio.cUF.valor   = codigo_estado
        envio.data        = datetime.now()

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + envio.data.strftime('%Y%m%dT%H%M%S') + '-ped-sta.xml', 'w')
            arq.write(envio.xml.encode('utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_SITUACAO, envio, resposta, ambiente)

        #resposta.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + envio.data.strftime('%Y%m%dT%H%M%S') + '-sta.xml', 'w')
            arq.write(resposta.xml.encode('utf-8'))
            arq.close()

        return processo

    def processar_notas(self, lista_nfes):
        #
        # Definir o caminho geral baseado na 1ª NF-e
        #
        caminho_original = self.caminho
        nfe = lista_nfes[0]
        nfe.monta_chave()
        self.caminho = caminho_original
        ambiente = nfe.infNFe.ide.tpAmb.valor
        self.caminho = self.monta_caminho_nfe(ambiente=nfe.infNFe.ide.tpAmb.valor, chave_nfe=nfe.chave)

        if self.consulta_servico_ao_enviar:
            proc_servico = self.consultar_servico(ambiente=ambiente)
            yield proc_servico
            #
            # Se o serviço não estiver em operação
            #
            if proc_servico.resposta.cStat.valor != '107':
                #
                # Interrompe todo o processo
                #
                return

        #
        # Verificar se as notas já não foram emitadas antes
        #
        for nfe in lista_nfes:
            nfe.monta_chave()
            self.caminho = caminho_original
            proc_consulta = self.consultar_nota(ambiente=nfe.infNFe.ide.tpAmb.valor, chave_nfe=nfe.chave)
            yield proc_consulta

            #
            # Se a nota já constar na SEFAZ (autorizada ou denegada)
            #
            #if not (
                #((self.versao == '1.10') and (proc_consulta.resposta.infProt.cStat.valor in ('217', '999',)))
                #or
                #((self.versao in ['2.00', '3.10']) and (proc_consulta.resposta.cStat.valor in ('217', '999',)))
            #):
            if (
                 ((self.versao == '1.10') and (proc_consulta.resposta.infProt.cStat.valor in ('217', '999',)))
                 or
                ((self.versao in ['2.00', '3.10']) and (proc_consulta.resposta.cStat.valor in ('100', '150', '110', '301', '302')))
             ):
                #
                # Interrompe todo o processo
                #
                return

        #
        # Nenhuma das notas estava já enviada, enviá-las então
        #
        nfe = lista_nfes[0]
        nfe.monta_chave()
        self.caminho = caminho_original
        self.caminho = self.monta_caminho_nfe(ambiente=nfe.infNFe.ide.tpAmb.valor, chave_nfe=nfe.chave)
        proc_envio = self.enviar_lote(lista_nfes=lista_nfes)
        yield proc_envio

        ret_envi_nfe = proc_envio.resposta

        #
        # Deu errado?
        #
        if ret_envi_nfe.cStat.valor != '103':
            #
            # Interrompe o processo
            #
            return

        #
        # Aguarda o tempo do processamento antes da consulta
        #
        time.sleep(ret_envi_nfe.infRec.tMed.valor * 1.3)

        #
        # Consulta o recibo do lote, para ver o que aconteceu
        #
        proc_recibo = self.consultar_recibo(ambiente=ret_envi_nfe.tpAmb.valor, numero_recibo=ret_envi_nfe.infRec.nRec.valor)

        #
        # Tenta receber o resultado do processamento do lote, caso ainda
        # esteja em processamento
        #
        tentativa = 0
        while proc_recibo.resposta.cStat.valor == '105' and tentativa < self.maximo_tentativas_consulta_recibo:
            time.sleep(ret_envi_nfe.infRec.tMed.valor * 1.5)
            tentativa += 1
            proc_recibo = self.consultar_recibo(ambiente=ret_envi_nfe.tpAmb.valor, numero_recibo=ret_envi_nfe.infRec.nRec.valor)

        # Montar os processos das NF-es
        dic_protNFe = proc_recibo.resposta.dic_protNFe
        dic_procNFe = proc_recibo.resposta.dic_procNFe

        self.caminho = caminho_original
        self.montar_processo_lista_notas(lista_nfes, dic_protNFe, dic_procNFe)

        yield proc_recibo

    def montar_processo_lista_notas(self, lista_nfes, dic_protNFe, dic_procNFe):
        for nfe in lista_nfes:
            if nfe.chave in dic_protNFe:
                protocolo = dic_protNFe[nfe.chave]
                processo = self.montar_processo_uma_nota(nfe, protnfe_recibo=protocolo)

                if processo is not None:
                    dic_procNFe[nfe.chave] = processo

    def montar_processo_uma_nota(self, nfe, protnfe_recibo=None, protnfe_consulta_110=None, retcancnfe=None):
        #
        # Somente para a versão 1.10
        # Caso processarmos o protocolo vindo de uma consulta,
        # temos que converter esse protocolo no formato
        # do protocolo que retorna quando o recibo do lote é consultado.
        #
        # Sim, as informações são as mesmas, mas o leiaute não...
        # Vai entender...
        #
        if protnfe_consulta_110 is not None:
            protnfe_recibo = ProtNFe_110()
            protnfe_recibo.infProt.tpAmb.valor = protnfe_consulta_110.infProt.tpAmb.valor
            protnfe_recibo.infProt.verAplic.valor = protnfe_consulta_110.infProt.verAplic.valor
            protnfe_recibo.infProt.chNFe.valor = protnfe_consulta_110.infProt.chNFe.valor
            protnfe_recibo.infProt.dhRecbto.valor = protnfe_consulta_110.infProt.dhRecbto.valor
            protnfe_recibo.infProt.cStat.valor = protnfe_consulta_110.infProt.cStat.valor
            protnfe_recibo.infProt.xMotivo.valor = protnfe_consulta_110.infProt.xMotivo.valor
            protnfe_recibo.infProt.nProt.valor = protnfe_consulta_110.infProt.nProt.valor
            protnfe_recibo.infProt.digVal.valor = protnfe_consulta_110.infProt.digVal.valor

        caminho_original = self.caminho
        self.caminho = self.monta_caminho_nfe(ambiente=nfe.infNFe.ide.tpAmb.valor, chave_nfe=nfe.chave)

        processo = None
        #
        # Se nota foi autorizada ou denegada
        # 100 - autorizada
        # 150 - autorizada fora do prazo
        # 110 - denegada
        # 301 - denegada por irregularidade do emitente
        # 302 - denegada por irregularidade do destinatário
        # 303 - Uso Denegado: Destinatário não habilitado a operar na UF
        #
        if protnfe_recibo.infProt.cStat.valor in ('100', '150', '110', '301', '302', '303'):
            if self.versao == '1.10':
                processo = ProcNFe_110()

            elif self.versao == '2.00':
                processo = ProcNFe_200()

            elif self.versao == '3.10':
                processo = ProcNFe_310()

            processo.NFe     = nfe
            processo.protNFe = protnfe_recibo

            if nfe.infNFe.ide.mod.valor == '55':
                self.danfe.NFe     = nfe
                self.danfe.protNFe = protnfe_recibo
                self.danfe.salvar_arquivo = False
                self.danfe.gerar_danfe()
                processo.danfe_pdf = self.danfe.conteudo_pdf
            elif nfe.infNFe.ide.mod.valor == '65':
                print('vai gerar o danfce', nfe, protnfe_recibo)

                self.danfce.NFe     = nfe
                self.danfce.protNFe = protnfe_recibo
                self.danfce.salvar_arquivo = False
                self.danfce.gerar_danfce()
                processo.danfce_pdf = self.danfce.conteudo_pdf

            if self.salvar_arquivos:
                nome_arq = self.caminho + unicode(nfe.chave).strip().rjust(44, '0') + '-proc-nfe.xml'
                arq = open(nome_arq, 'w')
                arq.write(processo.xml.encode('utf-8'))
                arq.close()

                # Estranhamente, o nome desse arquivo, pelo manual, deve ser chave-nfe.xml ou chave-den.xml
                # para notas denegadas
                if protnfe_recibo.infProt.cStat.valor in ('100', '150'):
                    nome_arq = self.caminho + unicode(nfe.chave).strip().rjust(44, '0') + '-nfe.xml'
                else:
                    nome_arq = self.caminho + unicode(nfe.chave).strip().rjust(44, '0') + '-den.xml'

                arq = open(nome_arq, 'w')
                arq.write(processo.xml.encode('utf-8'))
                arq.close()

                nome_arq = self.caminho + unicode(nfe.chave).strip().rjust(44, '0') + '.pdf'
                arq = open(nome_arq, 'w')

                if nfe.infNFe.ide.mod.valor == '55':
                    arq.write(processo.danfe_pdf)
                elif nfe.infNFe.ide.mod.valor == '65':
                    arq.write(processo.danfce_pdf)

                arq.close()

        self.caminho = caminho_original
        return processo

    def monta_caminho_nfe(self, ambiente, chave_nfe):
        caminho = self.caminho

        if ambiente == 1:
            caminho = os.path.join(caminho, 'producao/')
        else:
            caminho = os.path.join(caminho, 'homologacao/')

        data = '20' + chave_nfe[2:4] + '-' + chave_nfe[4:6]
        serie = chave_nfe[22:25]
        numero = chave_nfe[25:34]

        caminho = os.path.join(caminho, data + '/')
        caminho = os.path.join(caminho, serie + '-' + numero + '/')

        try:
            os.makedirs(caminho)
        except:
            pass

        return caminho

    def monta_caminho_inutilizacao(self, ambiente=None, data=None, serie=None, numero_inicial=None, numero_final=None):
        caminho = self.caminho

        if ambiente == 1:
            caminho = os.path.join(caminho, 'producao/')
        else:
            caminho = os.path.join(caminho, 'homologacao/')

        if data is None:
            data = datetime.now()

        caminho = os.path.join(caminho, data.strftime('%Y-%m') + '/')

        serie          = unicode(serie).strip().rjust(3, '0')
        numero_inicial = unicode(numero_inicial).strip().rjust(9, '0')
        numero_final   = unicode(numero_final).strip().rjust(9, '0')

        caminho = os.path.join(caminho, serie + '-' + numero_inicial + '-' + numero_final + '/')

        try:
            os.makedirs(caminho)
        except:
            pass

        return caminho

    def montar_processo_lista_eventos(self, lista_eventos, dic_retEvento, dic_procEvento, classe_procEvento):
        for evento in lista_eventos:
            chave = evento.infEvento.chNFe.valor
            if chave in dic_retEvento:
                retorno = dic_retEvento[chave]
                processo = classe_procEvento()
                processo.evento = evento
                processo.retEvento = retorno
                dic_procEvento[chave] = processo

    def _enviar_lote_evento(self, tipo_evento, numero_lote=None, lista_eventos=[]):
        #
        # Determina o tipo do evento
        #
        if tipo_evento == 'cce':
            classe_evento = ProcEventoCCe_100
            envio = EnvEventoCCe_100()
            resposta = RetEnvEventoCCe_100()

        elif tipo_evento == 'can':
            classe_evento = ProcEventoCancNFe_100
            envio = EnvEventoCancNFe_100()
            resposta = RetEnvEventoCancNFe_100()

        elif tipo_evento == 'confrec':
            classe_evento = ProcEventoConfRecebimento_100
            envio = EnvEventoConfRecebimento_100()
            resposta = RetEnvEventoConfRecebimento_100()

        processo = ProcessoNFe(webservice=WS_NFE_RECEPCAO_EVENTO, envio=envio, resposta=resposta)

        #
        # Vamos assinar e validar todas os Eventos antes da transmissão, evitando
        # rejeição na SEFAZ por incorreção no schema dos arquivos
        #
        for evento in lista_eventos:
            #
            # No caso de eventos de confirmação de recebimento, só é possível o
            # envio para o ambiente nacional, então é preciso forçar o cOrgao
            # nos eventos
            #
            if tipo_evento == 'confrec':
                evento.infEvento.cOrgao.valor = UF_CODIGO['RFB']

            self.certificado.assina_xmlnfe(evento)
            #evento.validar()

        envio.evento = lista_eventos

        if numero_lote is None:
            numero_lote = datetime.now().strftime('%Y%m%d%H%M%S')

        envio.idLote.valor = numero_lote

        #envio.validar()
        if self.salvar_arquivos:
            for evento in lista_eventos:
                chave = evento.infEvento.chNFe.valor
                ambiente = evento.infEvento.tpAmb.valor
                caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=chave)
                numero_sequencia = evento.infEvento.nSeqEvento.valor
                nome_arq = caminho + chave + '-' + unicode(numero_sequencia).zfill(2)
                arq = open(nome_arq + '-' + tipo_evento + '.xml', 'w')
                arq.write(evento.xml.encode('utf-8'))
                arq.close

            arq = open(caminho + unicode(envio.idLote.valor).strip().rjust(15, '0') + '-env-' + tipo_evento + '.xml', 'w')
            arq.write(envio.xml.encode('utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_RECEPCAO_EVENTO, envio, resposta, somente_ambiente_nacional=tipo_evento=='confrec')

        #resposta.validar()
        if self.salvar_arquivos:
            nome_arq = caminho + unicode(envio.idLote.valor).strip().rjust(15, '0') + '-rec-' + tipo_evento

            if resposta.cStat.valor not in ('129', '128'):
                nome_arq += '-rej.xml'
            else:
                nome_arq += '.xml'

            arq = open(nome_arq, 'w')
            arq.write(resposta.xml.encode('utf-8'))
            arq.close()

            self.montar_processo_lista_eventos(lista_eventos, processo.resposta.dic_retEvento, processo.resposta.dic_procEvento, classe_evento)

            #
            # Salva o processamento de cada arquivo
            #
            for ret in resposta.retEvento:
                chave = ret.infEvento.chNFe.valor
                ambiente = ret.infEvento.tpAmb.valor
                caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=chave)
                nome_arq = caminho + ret.infEvento.chNFe.valor + '-' + unicode(ret.infEvento.nSeqEvento.valor).zfill(2)

                #
                # O evento foi aceito e vinculado à NF-e
                #
                if ret.infEvento.cStat.valor == '135':
                    arq = open(nome_arq + '-ret-' + tipo_evento + '.xml', 'w')
                    arq.write(ret.xml.encode('utf-8'))
                    arq.close

                    #
                    # Salva o processo do evento
                    #
                    arq = open(nome_arq + '-proc-' + tipo_evento + '.xml', 'w')
                    arq.write(processo.resposta.dic_procEvento[chave].xml.encode('utf-8'))
                    arq.close

                #
                # O evento foi aceito, mas não foi vinculado à NF-e
                #
                elif ret.infEvento.cStat.valor == '136':
                    arq = open(nome_arq + '-ret-' + tipo_evento + '-sv.xml', 'w') # -sv = sem vínculo
                    arq.write(ret.xml.encode('utf-8'))
                    arq.close

                    #
                    # Salva o processo do evento
                    #
                    arq = open(nome_arq + '-proc-' + tipo_evento + '.xml', 'w')
                    arq.write(processo.resposta.dic_procEvento[chave].xml.encode('utf-8'))
                    arq.close

                #
                # O evento foi aceito e vinculado à NF-e, é um cancelamento for do prazo
                #
                elif ret.infEvento.cStat.valor == '155':
                    arq = open(nome_arq + '-ret-' + tipo_evento + '.xml', 'w')
                    arq.write(ret.xml.encode('utf-8'))
                    arq.close

                    #
                    # Salva o processo do evento
                    #
                    arq = open(nome_arq + '-proc-' + tipo_evento + '.xml', 'w')
                    arq.write(processo.resposta.dic_procEvento[chave].xml.encode('utf-8'))
                    arq.close

                #
                # O evento foi rejeitado
                #
                else:
                    arq = open(nome_arq + '-ret-' + tipo_evento + '-rej.xml', 'w')
                    arq.write(ret.xml.encode('utf-8'))
                    arq.close

        return processo

    def enviar_lote_cce(self, numero_lote=None, lista_eventos=[]):
        return self._enviar_lote_evento('cce', numero_lote, lista_eventos)

    def enviar_lote_cancelamento(self, numero_lote=None, lista_eventos=[]):
        return self._enviar_lote_evento('can', numero_lote, lista_eventos)

    def enviar_lote_confirmacao_recebimento(self, numero_lote=None, lista_eventos=[]):
        return self._enviar_lote_evento('confrec', numero_lote, lista_eventos)

    def consultar_notas_destinadas(self, ambiente=None, cnpj=None, ultimo_nsu='0', tipo_emissao='0', tipo_nfe='0'):
        envio = ConsNFeDest_101()
        resposta = RetConsNFeDest_101()

        envio.tpAmb.valor = ambiente or self.ambiente
        envio.CNPJ.valor = cnpj
        envio.ultNSU.valor = ultimo_nsu
        envio.indNFe.valor = tipo_nfe
        envio.indEmi.valor = tipo_emissao

        processo = ProcessoNFe(webservice=WS_NFE_CONSULTA_DESTINADAS, envio=envio, resposta=resposta)

        numero_lote = datetime.now().strftime('%Y%m%d%H%M%S')

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + unicode(numero_lote).strip().rjust(15, '0') + '-consnfedest.xml', 'w')
            arq.write(envio.xml.encode('utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_CONSULTA_DESTINADAS, envio, resposta, somente_ambiente_nacional=True)

        #resposta.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + unicode(numero_lote).strip().rjust(15, '0') + '-consnfedest-resp.xml', 'w')
            arq.write(resposta.original.encode('utf-8'))
            arq.close()

        return processo

    def baixar_notas_destinadas(self, ambiente=None, cnpj=None, lista_chaves=[]):
        envio = DownloadNFe_100()
        resposta = RetDownloadNFe_100()

        envio.tpAmb.valor = ambiente or self.ambiente
        envio.CNPJ.valor = cnpj
        envio.chNFe = [TagChNFe_100(valor=ch) for ch in lista_chaves]

        processo = ProcessoNFe(webservice=WS_NFE_DOWNLOAD, envio=envio, resposta=resposta)

        numero_lote = datetime.now().strftime('%Y%m%d%H%M%S')

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + unicode(numero_lote).strip().rjust(15, '0') + '-downloadnfe.xml', 'w')
            arq.write(envio.xml.encode('utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_DOWNLOAD, envio, resposta, somente_ambiente_nacional=True)

        #resposta.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + unicode(numero_lote).strip().rjust(15, '0') + '-downloadnfe-resp.xml', 'w')
            arq.write(resposta.original.encode('utf-8'))
            arq.close()

        return processo

    def cancelar_nota_evento(self, ambiente=None, chave_nfe=None, numero_protocolo=None, justificativa=None, data=None):
        evento = EventoCancNFe_100()
        evento.infEvento.tpAmb.valor = ambiente or self.ambiente
        evento.infEvento.cOrgao.valor = UF_CODIGO[self.estado]
        evento.infEvento.CNPJ.valor = chave_nfe[6:20] # Extrai o CNPJ da própria chave da NF-e
        evento.infEvento.chNFe.valor = chave_nfe
        evento.infEvento.dhEvento.valor = data or datetime.now()
        evento.infEvento.detEvento.nProt.valor = numero_protocolo
        evento.infEvento.detEvento.xJust.valor = justificativa

        processo = self.enviar_lote_cancelamento(lista_eventos=[evento])
        return processo

    def corrigir_nota_evento(self, ambiente=None, chave_nfe=None, numero_sequencia=None, correcao=None, data=None):
        evento = EventoCCe_100()
        evento.infEvento.tpAmb.valor = ambiente or self.ambiente
        evento.infEvento.cOrgao.valor = UF_CODIGO[self.estado]
        evento.infEvento.CNPJ.valor = chave_nfe[6:20] # Extrai o CNPJ da própria chave da NF-e
        evento.infEvento.chNFe.valor = chave_nfe
        evento.infEvento.dhEvento.valor = data or datetime.now()
        evento.infEvento.detEvento.xCorrecao.valor = correcao
        evento.infEvento.nSeqEvento.valor = numero_sequencia or 1

        processo = self.enviar_lote_cce(lista_eventos=[evento])
        return processo

    def confirmar_operacao_evento(self, ambiente=None, chave_nfe=None, cnpj=None, data=None):
        evento = EventoConfRecebimento_100()
        evento.infEvento.tpAmb.valor = ambiente or self.ambiente
        evento.infEvento.cOrgao.valor = UF_CODIGO[self.estado]
        evento.infEvento.CNPJ.valor = cnpj
        evento.infEvento.chNFe.valor = chave_nfe
        evento.infEvento.dhEvento.valor = data or datetime.now()
        evento.infEvento.tpEvento.valor = CONF_RECEBIMENTO_CONFIRMAR_OPERACAO
        evento.infEvento.detEvento.descEvento.valor = DESCEVENTO_CONF_RECEBIMENTO[evento.infEvento.tpEvento.valor]

        processo = self.enviar_lote_confirmacao_recebimento(lista_eventos=[evento])
        return processo

    def conhecer_operacao_evento(self, ambiente=None, chave_nfe=None, cnpj=None, data=None):
        evento = EventoConfRecebimento_100()
        evento.infEvento.tpAmb.valor = ambiente or self.ambiente
        evento.infEvento.cOrgao.valor = UF_CODIGO[self.estado]
        evento.infEvento.CNPJ.valor = cnpj
        evento.infEvento.chNFe.valor = chave_nfe
        evento.infEvento.dhEvento.valor = data or datetime.now()
        evento.infEvento.tpEvento.valor = CONF_RECEBIMENTO_CIENCIA_OPERACAO
        evento.infEvento.detEvento.descEvento.valor = DESCEVENTO_CONF_RECEBIMENTO[evento.infEvento.tpEvento.valor]

        processo = self.enviar_lote_confirmacao_recebimento(lista_eventos=[evento])
        return processo

    def desconhecer_operacao_evento(self, ambiente=None, chave_nfe=None, cnpj=None, data=None):
        evento = EventoConfRecebimento_100()
        evento.infEvento.tpAmb.valor = ambiente or self.ambiente
        evento.infEvento.cOrgao.valor = UF_CODIGO[self.estado]
        evento.infEvento.CNPJ.valor = cnpj
        evento.infEvento.chNFe.valor = chave_nfe
        evento.infEvento.dhEvento.valor = data or datetime.now()
        evento.infEvento.tpEvento.valor = CONF_RECEBIMENTO_DESCONHECIMENTO_OPERACAO
        evento.infEvento.detEvento.descEvento.valor = DESCEVENTO_CONF_RECEBIMENTO[evento.infEvento.tpEvento.valor]

        processo = self.enviar_lote_confirmacao_recebimento(lista_eventos=[evento])
        return processo

    def nao_realizar_operacao_evento(self, ambiente=None, chave_nfe=None, cnpj=None, justificativa=None, data=None):
        evento = EventoConfRecebimento_100()
        evento.infEvento.tpAmb.valor = ambiente or self.ambiente
        evento.infEvento.cOrgao.valor = UF_CODIGO[self.estado]
        evento.infEvento.CNPJ.valor = cnpj
        evento.infEvento.chNFe.valor = chave_nfe
        evento.infEvento.dhEvento.valor = data or datetime.now()
        evento.infEvento.tpEvento.valor = CONF_RECEBIMENTO_OPERACAO_NAO_REALIZADA
        evento.infEvento.detEvento.descEvento.valor = DESCEVENTO_CONF_RECEBIMENTO[evento.infEvento.tpEvento.valor]
        evento.infEvento.detEvento.xJust.valor = justificativa

        processo = self.enviar_lote_confirmacao_recebimento(lista_eventos=[evento])
        return processo

    def consultar_cadastro(self, estado=None, ie=None, cnpj_cpf=None):
        if self.versao == '1.10':
            envio = ConsCad_101()
            resposta = RetConsCad_101()

        elif self.versao == '2.00':
            envio = ConsCad_200()
            resposta = RetConsCad_200()

        elif self.versao == '3.10':
            envio = ConsCad_200()
            resposta = RetConsCad_200()

        processo = ProcessoNFe(webservice=WS_NFE_CONSULTA_CADASTRO, envio=envio, resposta=resposta)

        if estado is None:
            estado = self.estado

        envio.infCons.UF.valor = estado

        if ie is not None:
            envio.infCons.IE.valor = ie
            nome = 'IE_' + ie
        elif cnpj_cpf is not None:
            if len(cnpj_cpf) == 11:
                envio.infCons.CPF.valor = cnpj_cpf
                nome = 'CPF_' + cnpj_cpf
            else:
                envio.infCons.CNPJ.valor = cnpj_cpf
                nome = 'CNPJ_' + cnpj_cpf

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + nome + '-cons-cad.xml', 'w')
            arq.write(envio.xml.encode('utf-8'))
            arq.close()

        # Consulta de cadastro é sempre feita em ambiente de produção
        self._conectar_servico(WS_NFE_CONSULTA_CADASTRO, envio, resposta, 1)

        #resposta.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + nome + '-cad.xml', 'w')
            arq.write(resposta.xml.encode('utf-8'))
            arq.close()

        return processo

    def consultar_distribuicao(self, estado=None, cnpj_cpf=None, ultimo_nsu=None, nsu=None, ambiente=None):
        envio = DistDFeInt_100()
        resposta = RetDistDFeInt_100()
        
        envio.tpAmb.valor = ambiente or self.ambiente
        envio.cUFAutor.valor = UF_CODIGO[estado or self.estado]

        if len(cnpj_cpf) == 14:
            envio.CNPJ.valor = cnpj_cpf
        else:
            envio.CPF.valor = cnpj_cpf

        if ultimo_nsu is not None:
            envio.distNSU.ultNSU.valor = unicode(ultimo_nsu)
        else:
            envio.consNSU.NSU.valor = unicode(nsu)

        processo = ProcessoNFe(webservice=WS_DFE_DISTRIBUICAO, envio=envio, resposta=resposta)

        envio.validar()
        
        #Monta caminhos
        if (ambiente or self.ambiente) == 1:
            self.caminho = os.path.join(self.caminho, 'producao/dfe/')
        else:
            self.caminho = os.path.join(self.caminho, 'homologacao/dfe/')
        self.caminho = os.path.join(self.caminho, datetime.now().strftime('%Y-%m') + '/')
        try:
            os.makedirs(self.caminho)
        except:
            pass
        
        nome_arq = self.caminho + datetime.now().strftime('%Y%m%dT%H%M%S')
        if self.salvar_arquivos:
            arq = open(nome_arq + '-cons-dist-dfe.xml', 'w')
            arq.write(envio.xml.encode('utf-8'))
            arq.close()

        self._conectar_servico(WS_DFE_DISTRIBUICAO, envio, resposta, somente_ambiente_nacional=True)

        #resposta.validar()
        if self.salvar_arquivos:
            arq = open(nome_arq + '-ret-dist-dfe.xml', 'w')
            arq.write(resposta.original.encode('utf-8'))
            arq.close()

        return processo
