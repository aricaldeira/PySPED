# -*- coding: utf-8 -*-

from httplib import HTTPSConnection, HTTPResponse
from OpenSSL import crypto
import socket
import ssl
from datetime import datetime
import os
from uuid import uuid4

from webservices_flags import *
import webservices_1
import webservices_2

from pysped.xml_sped.certificado import Certificado

#
# Manual do Contribuinte versão 3.00
# NF-e leiaute 1.10
#
from manual_300 import SOAPEnvio_110, SOAPRetorno_110
from manual_300 import EnviNFe_110, RetEnviNFe_110
from manual_300 import ConsReciNFe_110, RetConsReciNFe_110, ProtNFe_110, ProcNFe_110
from manual_300 import CancNFe_107, RetCancNFe_107, ProcCancNFe_107
from manual_300 import InutNFe_107, RetInutNFe_107, ProcInutNFe_107
from manual_300 import ConsSitNFe_107, RetConsSitNFe_107
from manual_300 import ConsStatServ_107, RetConsStatServ_107
#from manual_300 import ConsCad_101, RetConsCad_101

#
# Manual do Contribuinte versão 4.01
# NF-e leiaute 2.00
#
from manual_401 import SOAPEnvio_200, SOAPRetorno_200
from manual_401 import EnviNFe_200, RetEnviNFe_200
from manual_401 import ConsReciNFe_200, RetConsReciNFe_200, ProtNFe_200, ProcNFe_200
from manual_401 import CancNFe_200, RetCancNFe_200, ProcCancNFe_200
from manual_401 import InutNFe_200, RetInutNFe_200, ProcInutNFe_200
from manual_401 import ConsSitNFe_200, RetConsSitNFe_200
from manual_401 import ConsStatServ_200, RetConsStatServ_200
#from manual_401 import ConsCad_200, RetConsCad_200

#
# DANFE
#
from danfe.danferetrato import *
from StringIO import StringIO


class ProcessoNFe(object):
    def __init__(self, webservice=0, envio=u'', resposta=u''):
        self.webservice = webservice
        self.envio = envio
        self.resposta = resposta


class ConexaoHTTPS(HTTPSConnection):
    def connect(self):
        "Connect to a host on a given (SSL) port."

        sock = socket.create_connection((self.host, self.port),
                                        self.timeout, self.source_address)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file,
                                    ssl_version=ssl.PROTOCOL_SSLv3)


class ProcessadorNFe(object):
    def __init__(self):
        self.ambiente = 2
        self.estado = u'SP'
        self.versao = u'1.10'
        self.certificado = Certificado()
        self.caminho = u''
        self.salvar_arquivos = True
        self.contingencia_SCAN = False
        self.danfe = DANFE()
        self.caminho_temporario = u''

        self._servidor     = u''
        self._url          = u''
        self._soap_envio   = None
        self._soap_retorno = None

    def _conectar_servico(self, servico, envio, resposta, ambiente=None):
        if ambiente is None:
            ambiente = self.ambiente

        if self.versao == u'1.10':
            self._soap_envio   = SOAPEnvio_110()
            self._soap_envio.webservice = webservices_1.METODO_WS[servico]['webservice']
            self._soap_envio.metodo     = webservices_1.METODO_WS[servico]['metodo']
            self._soap_envio.envio      = envio
            #self._soap_envio.nfeDadosMsg.dados = envio
            #self._soap_envio.nfeCabecMsg.cabec.versaoDados.valor = envio.versao.valor

            self._soap_retorno = SOAPRetorno_110()
            self._soap_retorno.webservice = webservices_1.METODO_WS[servico]['webservice']
            self._soap_retorno.metodo     = webservices_1.METODO_WS[servico]['metodo']
            self._soap_retorno.resposta   = resposta

            if self.contingencia_SCAN:
                self._servidor = webservices_1.SCAN[ambiente][u'servidor']
                self._url      = webservices_1.SCAN[ambiente][servico]
            else:
                self._servidor = webservices_1.ESTADO_WS[self.estado][ambiente][u'servidor']
                self._url      = webservices_1.ESTADO_WS[self.estado][ambiente][servico]

        elif self.versao == u'2.00':
            self._soap_envio   = SOAPEnvio_200()
            self._soap_envio.webservice = webservices_2.METODO_WS[servico]['webservice']
            self._soap_envio.metodo     = webservices_2.METODO_WS[servico]['metodo']
            self._soap_envio.cUF        = UF_CODIGO[self.estado]
            self._soap_envio.envio      = envio

            self._soap_retorno = SOAPRetorno_200()
            self._soap_retorno.webservice = webservices_2.METODO_WS[servico]['webservice']
            self._soap_retorno.metodo     = webservices_2.METODO_WS[servico]['metodo']
            self._soap_retorno.resposta   = resposta

            if self.contingencia_SCAN:
                self._servidor = webservices_2.SCAN[ambiente][u'servidor']
                self._url      = webservices_2.SCAN[ambiente][servico]
            else:
                self._servidor = webservices_2.ESTADO_WS[self.estado][ambiente][u'servidor']
                self._url      = webservices_2.ESTADO_WS[self.estado][ambiente][servico]


        #try:
        self.certificado.prepara_certificado_arquivo_pfx()

        #
        # Salva o certificado e a chave privada para uso na conexão HTTPS
        # Salvamos como um arquivo de nome aleatório para evitar o conflito
        # de uso de vários certificados e chaves diferentes na mesma máquina
        # ao mesmo tempo
        #
        self.caminho_temporario = self.caminho_temporario or u'/tmp/'

        nome_arq_chave = self.caminho_temporario + uuid4().hex
        arq_tmp = open(nome_arq_chave, 'w')
        arq_tmp.write(self.certificado.chave)
        arq_tmp.close()

        nome_arq_certificado = self.caminho_temporario + uuid4().hex
        arq_tmp = open(nome_arq_certificado, 'w')
        arq_tmp.write(self.certificado.certificado)
        arq_tmp.close()

        #con = HTTPSConnection(self._servidor, key_file=nome_arq_chave, cert_file=nome_arq_certificado)
        con = ConexaoHTTPS(self._servidor, key_file=nome_arq_chave, cert_file=nome_arq_certificado)
        con.request(u'POST', u'/' + self._url, self._soap_envio.xml.encode(u'utf-8'), self._soap_envio.header)
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
        if self.versao == u'1.10':
            envio = EnviNFe_110()
            resposta = RetEnviNFe_110()

        elif self.versao == u'2.00':
            envio = EnviNFe_200()
            resposta = RetEnviNFe_200()

        processo = ProcessoNFe(webservice=WS_NFE_ENVIO_LOTE, envio=envio, resposta=resposta)

        #
        # Vamos assinar e validar todas as NF-e antes da transmissão, evitando
        # rejeição na SEFAZ por incorreção no schema dos arquivos
        #
        for nfe in lista_nfes:
            self.certificado.assina_xmlnfe(nfe)
            nfe.validar()

        envio.NFe = lista_nfes

        if numero_lote is None:
            numero_lote = datetime.now().strftime('%Y%m%d%H%M%S')

        envio.idLote.valor = numero_lote

        envio.validar()
        if self.salvar_arquivos:
            for n in lista_nfes:
                n.monta_chave()
                arq = open(self.caminho + n.chave + u'-nfe.xml', 'w')
                arq.write(n.xml.encode(u'utf-8'))
                arq.close

            arq = open(self.caminho + unicode(envio.idLote.valor).strip().rjust(15, u'0') + u'-env-lot.xml', 'w')
            arq.write(envio.xml.encode(u'utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_ENVIO_LOTE, envio, resposta)

        #resposta.validar()
        if self.salvar_arquivos:
            nome_arq = self.caminho + unicode(envio.idLote.valor).strip().rjust(15, u'0') + u'-rec'

            if resposta.cStat.valor != u'103':
                nome_arq += u'-rej.xml'
            else:
                nome_arq += u'.xml'

            arq = open(nome_arq, 'w')
            arq.write(resposta.xml.encode(u'utf-8'))
            arq.close()

        return processo

    def consultar_recibo(self, ambiente=None, numero_recibo=None):
        if self.versao == u'1.10':
            envio = ConsReciNFe_110()
            resposta = RetConsReciNFe_110()

        elif self.versao == u'2.00':
            envio = ConsReciNFe_200()
            resposta = RetConsReciNFe_200()

        processo = ProcessoNFe(webservice=WS_NFE_CONSULTA_RECIBO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        envio.tpAmb.valor = ambiente
        envio.nRec.valor  = numero_recibo

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + unicode(envio.nRec.valor).strip().rjust(15, u'0') + u'-ped-rec.xml', 'w')
            arq.write(envio.xml.encode(u'utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_CONSULTA_RECIBO, envio, resposta, ambiente)

        #resposta.validar()
        if self.salvar_arquivos:
            nome_arq = self.caminho + unicode(envio.nRec.valor).strip().rjust(15, u'0') + u'-pro-rec'

            if resposta.cStat.valor != u'104':
                nome_arq += u'-rej.xml'
            else:
                nome_arq += u'.xml'

            arq = open(nome_arq, 'w')
            arq.write(resposta.xml.encode(u'utf-8'))
            arq.close()

            #
            # Salvar os resultados dos processamentos
            #
            for pn in resposta.protNFe:
                nome_arq = self.caminho + unicode(pn.infProt.chNFe.valor).strip().rjust(44, u'0') + u'-pro-nfe-'

                # NF-e autorizada
                if pn.infProt.cStat.valor == u'100':
                    nome_arq += u'aut.xml'

                # NF-e denegada
                elif pn.infProt.cStat.valor in (u'110', u'301', u'302'):
                    nome_arq += u'den.xml'

                # NF-e rejeitada
                else:
                    nome_arq += u'rej.xml'

                arq = open(nome_arq, 'w')
                arq.write(pn.xml.encode(u'utf-8'))
                arq.close()

        return processo

    def cancelar_nota(self, ambiente=None, chave_nfe=None, numero_protocolo=None, justificativa=None):
        if self.versao == u'1.10':
            envio = CancNFe_107()
            resposta = RetCancNFe_107()

        elif self.versao == u'2.00':
            envio = CancNFe_200()
            resposta = RetCancNFe_200()

        processo = ProcessoNFe(webservice=WS_NFE_CANCELAMENTO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        self.caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=chave_nfe)

        envio.infCanc.tpAmb.valor = ambiente
        envio.infCanc.chNFe.valor = chave_nfe
        envio.infCanc.nProt.valor = numero_protocolo
        envio.infCanc.xJust.valor = justificativa

        self.certificado.assina_xmlnfe(envio)

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + unicode(envio.infCanc.chNFe.valor).strip().rjust(44, u'0') + u'-ped-can.xml', 'w')
            arq.write(envio.xml.encode(u'utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_CANCELAMENTO, envio, resposta, ambiente)

        #resposta.validar()

        # Se for autorizado, monta o processo de cancelamento
        if resposta.infCanc.cStat.valor == u'101':
            if self.versao == u'1.10':
                processo_cancelamento_nfe = ProcCancNFe_107()

            elif self.versao == u'2.00':
                processo_cancelamento_nfe = ProcCancNFe_200()

            nome_arq = self.caminho + unicode(envio.infCanc.chNFe.valor).strip().rjust(44, u'0') + u'-proc-canc-nfe.xml'
            processo_cancelamento_nfe.cancNFe = envio
            processo_cancelamento_nfe.retCancNFe = resposta

            processo_cancelamento_nfe.validar()

            processo.processo_cancelamento_nfe = processo_cancelamento_nfe

        if self.salvar_arquivos:
            nome_arq = self.caminho + unicode(envio.infCanc.chNFe.valor).strip().rjust(44, u'0') + u'-pro-can-'

            # Cancelamento autorizado
            if resposta.infCanc.cStat.valor == u'101':
                nome_arq += u'aut.xml'
            else:
                nome_arq += u'rej.xml'

            arq = open(nome_arq, 'w')
            arq.write(resposta.xml.encode(u'utf-8'))
            arq.close()

            # Se for autorizado, monta o processo de cancelamento
            if resposta.infCanc.cStat.valor == u'101':
                nome_arq = self.caminho + unicode(envio.infCanc.chNFe.valor).strip().rjust(44, u'0') + u'-proc-canc-nfe.xml'
                arq = open(nome_arq, 'w')
                arq.write(processo_cancelamento_nfe.xml.encode(u'utf-8'))
                arq.close()

                # Estranhamente, o nome desse arquivo, pelo manual, deve ser chave-can.xml
                nome_arq = self.caminho + unicode(envio.infCanc.chNFe.valor).strip().rjust(44, u'0') + u'-can.xml'
                arq = open(nome_arq, 'w')
                arq.write(processo_cancelamento_nfe.xml.encode(u'utf-8'))
                arq.close()

        return processo

    def inutilizar_nota(self, ambiente=None, codigo_estado=None, ano=None, cnpj=None, serie=None, numero_inicial=None, numero_final=None, justificativa=None):
        if self.versao == u'1.10':
            envio = InutNFe_107()
            resposta = RetInutNFe_107()

        elif self.versao == u'2.00':
            envio = InutNFe_200()
            resposta = RetInutNFe_200()

        processo = ProcessoNFe(webservice=WS_NFE_INUTILIZACAO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        if codigo_estado is None:
            codigo_estado = UF_CODIGO[self.estado]

        if ano is None:
            ano = datetime.now().strftime(u'%y')

        if numero_final is None:
            numero_final = numero_inicial

        self.caminho = self.monta_caminho_inutilizacao(ambiente=ambiente, serie=serie, numero_inicial=numero_inicial, numero_final=numero_final)

        envio.infInut.tpAmb.valor  = ambiente
        envio.infInut.cUF.valor    = codigo_estado
        envio.infInut.ano.valor    = ano
        envio.infInut.CNPJ.valor   = cnpj
        #envio.infInut.mod.valor    = 55
        envio.infInut.serie.valor  = serie
        envio.infInut.nNFIni.valor = numero_inicial
        envio.infInut.nNFFin.valor = numero_final
        envio.infInut.xJust.valor  = justificativa

        envio.gera_nova_chave()
        self.certificado.assina_xmlnfe(envio)

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + unicode(envio.chave).strip().rjust(41, u'0') + u'-ped-inu.xml', 'w')
            arq.write(envio.xml.encode(u'utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_INUTILIZACAO, envio, resposta, ambiente)

        #resposta.validar()

        # Se for autorizada, monta o processo de inutilização
        if resposta.infInut.cStat.valor == u'102':
            if self.versao == u'1.10':
                processo_inutilizacao_nfe = ProcInutNFe_107()

            elif self.versao == u'2.00':
                processo_inutilizacao_nfe = ProcInutNFe_200()

            processo_inutilizacao_nfe.inutNFe = envio
            processo_inutilizacao_nfe.retInutNFe = resposta

            processo_inutilizacao_nfe.validar()

            processo.processo_inutilizacao_nfe = processo_inutilizacao_nfe

        if self.salvar_arquivos:
            nome_arq = self.caminho + unicode(envio.chave).strip().rjust(41, u'0') + u'-pro-inu-'

            # Inutilização autorizada
            if resposta.infInut.cStat.valor == u'102':
                nome_arq += u'aut.xml'
            else:
                nome_arq += u'rej.xml'

            arq = open(nome_arq, 'w')
            arq.write(resposta.xml.encode(u'utf-8'))
            arq.close()

            # Se for autorizada, monta o processo de inutilização
            if resposta.infInut.cStat.valor == u'102':
                nome_arq = self.caminho + unicode(envio.chave).strip().rjust(41, u'0') + u'-proc-inut-nfe.xml'
                arq = open(nome_arq, 'w')
                arq.write(processo_inutilizacao_nfe.xml.encode(u'utf-8'))
                arq.close()

                # Estranhamente, o nome desse arquivo, pelo manual, deve ser chave-inu.xml
                nome_arq = self.caminho + unicode(envio.chave).strip().rjust(41, u'0') + u'-inu.xml'
                arq = open(nome_arq, 'w')
                arq.write(processo_inutilizacao_nfe.xml.encode(u'utf-8'))
                arq.close()

        return processo

    def consultar_nota(self, ambiente=None, chave_nfe=None, nfe=None):
        if self.versao == u'1.10':
            envio = ConsSitNFe_107()
            resposta = RetConsSitNFe_107()

        elif self.versao == u'2.00':
            envio = ConsSitNFe_200()
            resposta = RetConsSitNFe_200()

        processo = ProcessoNFe(webservice=WS_NFE_CONSULTA, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        self.caminho = self.monta_caminho_nfe(ambiente, chave_nfe)

        envio.tpAmb.valor = ambiente
        envio.chNFe.valor = chave_nfe

        envio.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + unicode(chave_nfe).strip().rjust(44, u'0') + u'-ped-sit.xml', 'w')
            arq.write(envio.xml.encode(u'utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_CONSULTA, envio, resposta, ambiente)

        #resposta.validar()

        if self.salvar_arquivos:
            nome_arq = self.caminho + unicode(chave_nfe).strip().rjust(44, u'0') + u'-sit.xml'
            arq = open(nome_arq, 'w')
            arq.write(resposta.xml.encode(u'utf-8'))
            arq.close()

        return processo

    def consultar_servico(self, ambiente=None, codigo_estado=None):
        if self.versao == u'1.10':
            envio = ConsStatServ_107()
            resposta = RetConsStatServ_107()

        elif self.versao == u'2.00':
            envio = ConsStatServ_200()
            resposta = RetConsStatServ_200()

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
            arq = open(self.caminho + envio.data.strftime(u'%Y%m%dT%H%M%S') + u'-ped-sta.xml', 'w')
            arq.write(envio.xml.encode(u'utf-8'))
            arq.close()

        self._conectar_servico(WS_NFE_SITUACAO, envio, resposta, ambiente)

        #resposta.validar()
        if self.salvar_arquivos:
            arq = open(self.caminho + envio.data.strftime(u'%Y%m%dT%H%M%S') + u'-sta.xml', 'w')
            arq.write(envio.xml.encode(u'utf-8'))
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

        proc_servico = self.consultar_servico(ambiente=ambiente)
        yield proc_servico

        #
        # Serviço em operação?
        #
        if proc_servico.resposta.cStat.valor == u'107':
            #
            # Verificar se as notas já não foram emitadas antes
            #
            for nfe in lista_nfes:
                nfe.monta_chave()
                self.caminho = caminho_original
                proc_consulta = self.consultar_nota(ambiente=nfe.infNFe.ide.tpAmb.valor, chave_nfe=nfe.chave)
                yield proc_consulta

                #
                # Se a nota já constar na SEFAZ
                #
                if not (
                    ((self.versao == u'1.10') and (proc_consulta.resposta.infProt.cStat.valor in (u'217', u'999',)))
                    or
                    ((self.versao == u'2.00') and (proc_consulta.resposta.cStat.valor in (u'217', u'999',)))
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
            # Deu certo?
            #
            if ret_envi_nfe.cStat.valor == u'103':
                proc_recibo = self.consultar_recibo(ambiente=ret_envi_nfe.tpAmb.valor, numero_recibo=ret_envi_nfe.infRec.nRec.valor)

                # Montar os processos das NF-es
                dic_protNFe = proc_recibo.resposta.dic_protNFe
                dic_procNFe = proc_recibo.resposta.dic_procNFe

                self.caminho = caminho_original
                self.montar_processo_lista_notas(lista_nfes, dic_protNFe, dic_procNFe)

                yield proc_recibo

    def montar_processo_lista_notas(self, lista_nfes, dic_protNFe, dic_procNFe):
        for nfe in lista_nfes:
            if dic_protNFe.has_key(nfe.chave):
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
            protnfe_recibo.infProt.tpAmb.valor = protnfe_consulta.infProt.tpAmb.valor
            protnfe_recibo.infProt.verAplic.valor = protnfe_consulta.infProt.verAplic.valor
            protnfe_recibo.infProt.chNFe.valor = protnfe_consulta.infProt.chNFe.valor
            protnfe_recibo.infProt.dhRecbto.valor = protnfe_consulta.infProt.dhRecbto.valor
            protnfe_recibo.infProt.cStat.valor = protnfe_consulta.infProt.cStat.valor
            protnfe_recibo.infProt.xMotivo.valor = protnfe_consulta.infProt.xMotivo.valor
            protnfe_recibo.infProt.nProt.valor = protnfe_consulta.infProt.nProt.valor
            protnfe_recibo.infProt.digVal.valor = protnfe_consulta.infProt.digVal.valor

        caminho_original = self.caminho
        self.caminho = self.monta_caminho_nfe(ambiente=nfe.infNFe.ide.tpAmb.valor, chave_nfe=nfe.chave)

        processo = None
        # Se nota foi autorizada ou denegada
        if protnfe_recibo.infProt.cStat.valor in (u'100', u'110', u'301', u'302'):
            if self.versao == u'1.10':
                processo = ProcNFe_110()

            elif self.versao == u'2.00':
                processo = ProcNFe_200()

            processo.NFe     = nfe
            processo.protNFe = protnfe_recibo

            self.danfe.NFe     = nfe
            self.danfe.protNFe = protnfe_recibo
            self.danfe.salvar_arquivo = False
            self.danfe.gerar_danfe()

            danfe_pdf = StringIO()
            self.danfe.danfe.generate_by(PDFGenerator, filename=danfe_pdf)
            processo.danfe_pdf = danfe_pdf.getvalue()
            danfe_pdf.close()

            if self.salvar_arquivos:
                nome_arq = self.caminho + unicode(nfe.chave).strip().rjust(44, u'0') + u'-proc-nfe.xml'
                arq = open(nome_arq, 'w')
                arq.write(processo.xml.encode(u'utf-8'))
                arq.close()

                # Estranhamente, o nome desse arquivo, pelo manual, deve ser chave-nfe.xml ou chave-den.xml
                # para notas denegadas
                if protnfe_recibo.infProt.cStat.valor == u'100':
                    nome_arq = self.caminho + unicode(nfe.chave).strip().rjust(44, u'0') + u'-nfe.xml'
                else:
                    nome_arq = self.caminho + unicode(nfe.chave).strip().rjust(44, u'0') + u'-den.xml'

                arq = open(nome_arq, 'w')
                arq.write(processo.xml.encode(u'utf-8'))
                arq.close()

                nome_arq = self.caminho + unicode(nfe.chave).strip().rjust(44, u'0') + u'.pdf'
                arq = open(nome_arq, 'w')
                arq.write(processo.danfe_pdf)
                arq.close()

        self.caminho = caminho_original
        return processo

    def monta_caminho_nfe(self, ambiente, chave_nfe):
        caminho = self.caminho

        if ambiente == 1:
            caminho = os.path.join(caminho, 'producao/')
        else:
            caminho = os.path.join(caminho, 'homologacao/')

        data = u'20' + chave_nfe[2:4] + u'-' + chave_nfe[4:6]
        serie = chave_nfe[22:25]
        numero = chave_nfe[25:34]

        caminho = os.path.join(caminho, data + u'/')
        caminho = os.path.join(caminho, serie + u'-' + numero + u'/')

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

        caminho = os.path.join(caminho, data.strftime(u'%Y-%m') + u'/')

        serie          = unicode(serie).strip().rjust(3, u'0')
        numero_inicial = unicode(numero_inicial).strip().rjust(9, u'0')
        numero_final   = unicode(numero_final).strip().rjust(9, u'0')

        caminho = os.path.join(caminho, serie + u'-' + numero_inicial + u'-' + numero_final + u'/')

        try:
            os.makedirs(caminho)
        except:
            pass

        return caminho


class DANFE(object):
    def __init__(self):
        self.imprime_canhoto        = True
        self.imprime_local_retirada = True
        self.imprime_local_entrega  = True
        self.imprime_fatura         = True
        self.imprime_duplicatas     = True
        self.imprime_issqn          = True

        self.caminho           = u''
        self.salvar_arquivo    = True

        self.NFe        = None
        self.protNFe    = None
        self.retCancNFe = None
        self.danfe      = None

        self.obs_impressao    = u'DANFE gerado em %(now:%d/%m/%Y, %H:%M:%S)s'
        self.nome_sistema     = u''
        self.site             = u''
        self.logo             = u''
        self.leiaute_logo_vertical = False
        self.dados_emitente   = []

    def gerar_danfe(self):
        if self.NFe is None:
            raise ValueError(u'Não é possível gerar um DANFE sem a informação de uma NF-e')

        if self.protNFe is None:
            self.protNFe = ProtNFe_200()

        if self.retCancNFe is None:
            self.retCancNFe = RetCancNFe_200()

        #
        # Prepara o queryset para impressão
        #
        self.NFe.monta_chave()
        self.NFe.monta_dados_contingencia_fsda()
        self.NFe.site = self.site

        for detalhe in self.NFe.infNFe.det:
            detalhe.NFe = self.NFe
            detalhe.protNFe = self.protNFe
            detalhe.retCancNFe = self.retCancNFe

        #
        # Prepara as bandas de impressão para cada formato
        #
        if self.NFe.infNFe.ide.tpImp.valor == 2:
            raise ValueError(u'DANFE em formato paisagem ainda não implementado')
        else:
            self.danfe = DANFERetrato()
            self.danfe.queryset = self.NFe.infNFe.det

        if self.imprime_canhoto:
            self.danfe.band_page_header = self.danfe.canhoto
            self.danfe.band_page_header.child_bands = []
            self.danfe.band_page_header.child_bands.append(self.danfe.remetente)
        else:
            self.danfe.band_page_header = self.danfe.remetente
            self.danfe.band_page_header.child_bands = []

        # Emissão para simples conferência / sem protocolo de autorização
        if not self.protNFe.infProt.nProt.valor:
            self.danfe.remetente.campo_variavel_conferencia()

        # NF-e denegada
        elif self.protNFe.infProt.cStat.valor == u'110':
            self.danfe.remetente.campo_variavel_denegacao()
            self.danfe.remetente.obs_denegacao()

        # Emissão em contingência com FS ou FSDA
        elif self.NFe.infNFe.ide.tpEmis.valor in (2, 5,):
            self.danfe.remetente.campo_variavel_contingencia_fsda()
            self.danfe.remetente.obs_contingencia_normal_scan()

        # Emissão em contingência com DPEC
        elif self.NFe.infNFe.ide.tpEmis.valor == 4:
            self.danfe.remetente.campo_variavel_contingencia_dpec()
            self.danfe.remetente.obs_contingencia_dpec()

        # Emissão normal ou contingência SCAN
        else:
            self.danfe.remetente.campo_variavel_normal()
            # Contingência SCAN
            if self.NFe.infNFe.ide.tpEmis.valor == 3:
                self.danfe.remetente.obs_contingencia_normal_scan()

        # A NF-e foi cancelada, no DANFE imprimir o "carimbo" de cancelamento
        if self.retCancNFe.infCanc.nProt.valor:
            self.danfe.remetente.obs_cancelamento()

        # Observação de ausência de valor fiscal
        # se não houver protocolo ou se o ambiente for de homologação
        if (not self.protNFe.infProt.nProt.valor) or self.NFe.infNFe.ide.tpAmb.valor == 2:
            self.danfe.remetente.obs_sem_valor_fiscal()

        self.danfe.band_page_header.child_bands.append(self.danfe.destinatario)

        if self.imprime_local_retirada and len(self.NFe.infNFe.retirada.xml):
            self.danfe.band_page_header.child_bands.append(self.danfe.local_retirada)

        if self.imprime_local_entrega and len(self.NFe.infNFe.entrega.xml):
            self.danfe.band_page_header.child_bands.append(self.danfe.local_entrega)

        if self.imprime_fatura:
            # Pagamento a prazo
            if (self.NFe.infNFe.ide.indPag.valor == 1) or \
                (len(self.NFe.infNFe.cobr.dup) > 1) or \
                ((len(self.NFe.infNFe.cobr.dup) == 1) and \
                (self.NFe.infNFe.cobr.dup[0].dVenc.xml > self.NFe.infNFe.ide.dEmi.xml)):

                if self.imprime_duplicatas:
                    self.danfe.fatura_a_prazo.elements.append(self.danfe.duplicatas)

                self.danfe.band_page_header.child_bands.append(self.danfe.fatura_a_prazo)

            # Pagamento a vista
            else:
                self.danfe.band_page_header.child_bands.append(self.danfe.fatura_a_vista)

        self.danfe.band_page_header.child_bands.append(self.danfe.calculo_imposto)
        self.danfe.band_page_header.child_bands.append(self.danfe.transporte)
        self.danfe.band_page_header.child_bands.append(self.danfe.cab_produto)

        if self.imprime_issqn and len(self.NFe.infNFe.total.ISSQNTot.xml):
            self.danfe.band_page_footer = self.danfe.iss
        else:
            self.danfe.band_page_footer = self.danfe.dados_adicionais

        self.danfe.band_detail = self.danfe.det_produto

        #
        # Observação de impressão
        #
        if self.nome_sistema:
            self.danfe.ObsImpressao.expression = self.nome_sistema + u' - ' + self.obs_impressao
        else:
            self.danfe.ObsImpressao.expression = self.obs_impressao

        #
        # Quadro do emitente
        #
        # Personalizado?
        if self.dados_emitente:
            self.danfe.remetente.monta_quadro_emitente(self.dados_emitente)
        else:
            # Sem logotipo
            if not self.logo:
                self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_sem_logo())

            # Logotipo na vertical
            elif self.leiaute_logo_vertical:
                self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_logo_vertical(self.logo))

            # Logotipo na horizontal
            else:
                self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_logo_horizontal(self.logo))

        if self.salvar_arquivo:
            nome_arq = self.caminho + self.NFe.chave + u'.pdf'
            self.danfe.generate_by(PDFGenerator, filename=nome_arq)
