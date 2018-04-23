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
import socket
import ssl
from datetime import datetime
import time
from uuid import uuid4
from builtins import str
from io import open
import json


if sys.version_info.major == 2:
    from httplib import HTTPSConnection, HTTPConnection

else:
    from http.client import HTTPSConnection, HTTPConnection

from .danfse import DANFSE

import pybrasil


class ConexaoHTTPS(HTTPSConnection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.protocolo = ssl.PROTOCOL_SSLv23

    def connect(self):
        #
        # source_address é atributo incluído na versão 2.7 do Python
        # Verificando a existência para funcionar em versões anteriores à 2.7
        #
        if hasattr(self, 'source_address'):
            sock = socket.create_connection((self.host, self.port), self.timeout, self.source_address)
        else:
            sock = socket.create_connection((self.host, self.port), self.timeout)

        if self._tunnel_host:
            self.sock = sock
            self._tunnel()

        protocolo = getattr(self, 'protocolo', ssl.PROTOCOL_SSLv23)

        if getattr(self, 'forca_cadeia_conexao', False):
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=self.protocolo,
                                        do_handshake_on_connect=False, ca_certs=self.ca_certs)
        else:
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=self.protocolo,
                                        do_handshake_on_connect=False)


class Conexao(object):
    def __init__(self, certificado=None, servidor='', url='', metodo=''):
        self.certificado = certificado or pybrasil.certificado.Certificado()
        self.servidor = servidor
        self.porta = 443
        self.url = url
        self.metodo = metodo
        self.header = {}
        self.forca_tls = False
        self.forca_http = False
        self.forca_cadeia_conexao = False
        self.sem_certificado = False

        self.xml_envio = ''
        self.xml_resposta = ''
        self.response = None
        self.resposta = None

        self.erros = []
        self.mensagem_erro = ''

        self.codigo_verificacao = ''
        self.numero_nfse = '0'
        self.data_nfse = ''

    def conectar_servico(self, envelope):
        self.xml_envio = envelope

        #
        # Salva o certificado e a chave privada para uso na conexão HTTPS
        # Salvamos como um arquivo de nome aleatório para evitar o conflito
        # de uso de vários certificados e chaves diferentes na mesma máquina
        # ao mesmo tempo
        #
        if not self.sem_certificado:
            self.certificado.prepara_certificado_arquivo_pfx()
            self.certificado.salva_arquivo_conexao(inclui_cadeia=self.forca_cadeia_conexao)

        if self.forca_http:
            con = HTTPConnection(self.servidor)

        else:
            if self.sem_certificado:
                con = HTTPSConnection(self.servidor, port=self.porta)

            else:
                con = ConexaoHTTPS(self.servidor, port=self.porta, key_file=self.certificado.arquivo_chave_conexao,
                                   cert_file=self.certificado.arquivo_certificado_conexao)

                if self.forca_cadeia_conexao:
                    con.forca_cadeia_conexao
                    con.ca_certs = self.certificado.arquivo_cadeia_conexao

                if self.forca_tls:
                    con.protocolo = ssl.PROTOCOLO_TSL

        #
        # É preciso definir o POST abaixo como bytestring, já que importamos
        # os unicode_literals... Dá um pau com xml com acentos sem isso...
        #
        #con.set_debuglevel(1)

        if sys.version_info.major == 2:
            con.request(b'POST', b'/' + self.url.encode('utf-8'), self.xml_envio.encode('utf-8'), self.header)
        else:
            con.request('POST', '/' + self.url, self.xml_envio.encode('utf-8'), self.header)

        con.sock.settimeout(600.0)

        self.response = con.getresponse()

        if not self.sem_certificado:
            self.certificado.exclui_arquivo_conexao()

        self.xml_resposta = self.response.read().decode('utf-8')

        con.close()


class ProcessadorNFSe(object):
    def __init__(self, certificado=None):
        self.certificado = certificado or pybrasil.certificado.Certificado()
        self.salvar_arquivos = True
        self.danfse = DANFSE()
        self.darl = DANFSE()
        self.caminho_temporario = ''
        self._nfe = None

    def configuracao_municipio(self, nfe):
        if self._nfe is None or self._nfe != nfe:
            self.configuracao = pybrasil.base.DicionarioObjeto(json.load(open(nfe.configuracao_json)))

    def prepara_conexao(self, operacao):
        conexao = Conexao()
        conexao.certificado = self.certificado

        configuracao = pybrasil.base.DicionarioObjeto(self.configuracao[operacao].conexao)

        conexao.servidor = configuracao.servidor or ''
        conexao.porta = configuracao.porta or 443
        conexao.url = configuracao.url or ''
        conexao.metodo = configuracao.metodo or ''
        conexao.header = configuracao.header or {}
        conexao.forca_tls = configuracao.forca_tls or False
        conexao.forca_http = configuracao.forca_http or False
        conexao.forca_cadeia_conexao = configuracao.forca_cadeia_conexao or False
        conexao.sem_certificado = configuracao.sem_certificado or False

        return conexao

    def limpa_namespace(self, operacao, xml):
        xml = pybrasil.base.xml.tira_namespaces(xml)

        if not (self.configuracao[operacao].assinatura and self.configuracao[operacao].assinatura.namespaces):
            return xml

        for namespace, url in self.configuracao[operacao].assinatura.namespaces.items():
            xml = xml.replace(f'xmlns:{namespace}="{url}"', '')
            xml = xml.replace(f'xmlns="{url}"', '')

        return xml

    def unescape_xml(self, xml):
        xml = pybrasil.base.xml.unescape_xml(xml)
        xml = xml.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
        xml = xml.replace('<?xml version="1.0" encoding="utf-8"?>', '')
        xml = xml.replace('<?xml version="1.0" encoding="UTF-8" ?>', '')
        xml = xml.replace('<?xml version="1.0" encoding="utf-8" ?>', '')
        return xml

    #
    # Envio de RPS síncrono
    #
    def assina_xml_rps(self, nfe):
        self.configuracao_municipio(nfe)

        if not (self.configuracao.envio_rps and self.configuracao.envio_rps.assina):
            return nfe.xml_rps

        configuracao = self.configuracao.envio_rps.assinatura

        #
        # São Paulo - SP tem uma assinatura específica
        #
        if str(nfe.infNFe.emit.enderEmit.cMun.valor) == '3550308':
            assinatura = self.assinatura_nfse_sp(nfe)
            assinatura = self.certificado.assina_texto(assinatura.upper())
            nfe.assinatura_servico = assinatura

        conteudo = pybrasil.base.tira_acentos(nfe.xml_rps)
        conteudo = self.certificado.assina_xml(conteudo, **configuracao)

        return conteudo

    def assinatura_nfse_sp(self, NFe):
        assinatura = NFe.infNFe.emit.IM.valor.zfill(8)[:8]
        assinatura += NFe.infNFe.ide.serie_rps.valor.strip().ljust(5)[:5]
        assinatura += str(NFe.infNFe.ide.nRPS.valor).zfill(12)[:12]
        assinatura += NFe.infNFe.ide.dhEmi.formato_iso[:10].replace('-', '')

        if NFe.infNFe.ide.natureza_nfse == '1':
            assinatura += 'F'
        elif NFe.infNFe.ide.natureza_nfse == '2':
            assinatura += 'A'
        elif NFe.infNFe.ide.natureza_nfse == '4':
            assinatura += 'J'
        else:
            assinatura += 'T'

        #assinatura += 'C' if nota.cancelada else 'N'
        assinatura += 'N'
        assinatura += 'S' if NFe.infNFe.total.ISSQNTot.vISSRet.valor > 0 else 'N'
        assinatura += str(int(NFe.infNFe.total.ISSQNTot.vServ.valor * 100)).zfill(15)
        assinatura += str(int(NFe.infNFe.total.ISSQNTot.vDeducao.valor * 100)).zfill(15)
        assinatura += NFe.infNFe.det[0].imposto.ISSQN.cServico.valor.zfill(5)[:5]

        if NFe.infNFe.dest.CPF.valor:
            assinatura += '1'
            assinatura += NFe.infNFe.dest.CPF.valor.zfill(14)[:14]

        elif NFe.infNFe.dest.CNPJ.valor:
            assinatura += '2'
            assinatura += NFe.infNFe.dest.CNPJ.valor.zfill(14)[:14]

        else:
            assinatura += '3'
            assinatura += ''.zfill(14)

        return assinatura

    def envia_rps(self, nfe):
        self.configuracao_municipio(nfe)
        conteudo = self.assina_xml_rps(nfe)

        configuracao = self.configuracao['envio_rps']

        if configuracao.escapa_envio:
            conteudo = pybrasil.base.xml.escape_xml(conteudo)

        envelope = nfe.render_template('envelope_rps.xml', {'body': conteudo})

        conexao = self.prepara_conexao('envio_rps')

        conexao.conectar_servico(envelope)

        xml = conexao.xml_resposta
        if configuracao.escapa_resposta:
            xml = self.unescape_xml(xml)

        xml = self.limpa_namespace('envio_rps', xml)

        resposta = pybrasil.base.xml.gera_objeto_xml(xml)

        if configuracao.tag_erro:
            tag_erro = resposta.getroottree().findall('//' + configuracao.tag_erro)
        else:
            tag_erro = []

        if configuracao.tag_alerta:
            tag_alerta = resposta.getroottree().findall('//' + configuracao.tag_alerta)
        else:
            tag_alerta = []

        if configuracao.tag_sucesso:
            tag_sucesso = resposta.getroottree().findall('//' + configuracao.tag_sucesso)
        else:
            tag_sucesso = []

        if tag_sucesso:
            tag_sucesso = tag_sucesso[0]

            if configuracao.tag_sucesso_codigo_verificacao:
                conexao.codigo_verificacao = getattr(tag_sucesso, configuracao.tag_sucesso_codigo_verificacao, '')

            if configuracao.tag_sucesso_numero_nfse:
                conexao.numero_nfse = getattr(tag_sucesso, configuracao.tag_sucesso_numero_nfse, '')

            if configuracao.tag_sucesso_data_nfse:
                conexao.data_nfse = getattr(tag_sucesso, configuracao.tag_sucesso_data_nfse, '')

        elif tag_erro:
            mensagem_erro = ''

            for erro in tag_erro:
                conexao.erros.append(erro)

                if configuracao.tag_erro_codigo:
                    texto_erro = getattr(erro, configuracao.tag_erro_codigo, '')
                    mensagem_erro += f'Código de retorno: {texto_erro}\n'

                if configuracao.tag_erro_descricao:
                    texto_erro = getattr(erro, configuracao.tag_erro_descricao, '')
                    mensagem_erro += f'Mensagem: {texto_erro}\n'

            conexao.mensagem_erro = mensagem_erro

        elif tag_alerta:
            mensagem_alerta = ''

            for alerta in tag_alerta:
                conexao.erros.append(alerta)

                if configuracao.tag_alerta_codigo:
                    texto_alerta = getattr(alerta, configuracao.tag_alerta_codigo, '')
                    mensagem_alerta += f'Código de retorno: {texto_alerta}\n'

                if configuracao.tag_alerta_descricao:
                    texto_alerta = getattr(alerta, configuracao.tag_alerta_descricao, '')
                    mensagem_alerta += f'Mensagem: {texto_alerta}\n'

            conexao.mensagem_erro = mensagem_alerta

        return conexao

    #
    # Cancelamento síncrono
    #
    def assina_xml_cancelamento(self, nfe):
        self.configuracao_municipio(nfe)

        if not (self.configuracao.envio_cancelamento and self.configuracao.envio_cancelamento.assina):
            return nfe.xml_cancelamento

        configuracao = self.configuracao.envio_cancelamento.assinatura

        #
        # São Paulo - SP tem uma assinatura específica
        #
        if str(nfe.infNFe.emit.enderEmit.cMun.valor) == '3550308':
            assinatura = self.assinatura_cancelamento_nfse_sp(nfe)
            assinatura = self.certificado.assina_texto(assinatura.upper())
            nfe.assinatura_servico = assinatura

        conteudo = pybrasil.base.tira_acentos(nfe.xml_cancelamento)
        conteudo = self.certificado.assina_xml(conteudo, **configuracao)

        return conteudo

    def assinatura_cancelamento_nfse_sp(self, NFe):
        assinatura = NFe.infNFe.emit.IM.valor.zfill(8)[:8]
        assinatura += str(NFe.infNFe.ide.nNF.valor).zfill(12)[:12]

        return assinatura

    def envia_cancelamento(self, nfe):
        self.configuracao_municipio(nfe)
        conteudo = self.assina_xml_cancelamento(nfe)

        configuracao = self.configuracao['envio_cancelamento']

        if configuracao.escapa_envio:
            conteudo = pybrasil.base.xml.escape_xml(conteudo)

        envelope = nfe.render_template('envelope_cancelamento.xml', {'body': conteudo})

        conexao = self.prepara_conexao('envio_cancelamento')

        conexao.conectar_servico(envelope)

        xml = conexao.xml_resposta
        if configuracao.escapa_resposta:
            xml = self.unescape_xml(xml)

        xml = self.limpa_namespace('envio_cancelamento', xml)

        resposta = pybrasil.base.xml.gera_objeto_xml(xml)

        if configuracao.tag_erro:
            tag_erro = resposta.getroottree().findall('//' + configuracao.tag_erro)
        else:
            tag_erro = []

        if configuracao.tag_alerta:
            tag_alerta = resposta.getroottree().findall('//' + configuracao.tag_alerta)
        else:
            tag_alerta = []

        if configuracao.tag_sucesso:
            tag_sucesso = resposta.getroottree().findall('//' + configuracao.tag_sucesso)
        else:
            tag_sucesso = []

        if tag_sucesso:
            tag_sucesso = tag_sucesso[0]

            if configuracao.tag_sucesso_codigo_verificacao:
                conexao.codigo_verificacao = getattr(tag_sucesso, configuracao.tag_sucesso_codigo_verificacao, '')

            if configuracao.tag_sucesso_numero_nfse:
                conexao.numero_nfse = getattr(tag_sucesso, configuracao.tag_sucesso_numero_nfse, '')

            if configuracao.tag_sucesso_data_nfse:
                conexao.data_nfse = getattr(tag_sucesso, configuracao.tag_sucesso_data_nfse, '')

        elif tag_erro:
            mensagem_erro = ''

            for erro in tag_erro:
                if configuracao.tag_erro_codigo:
                    texto_erro = str(getattr(erro, configuracao.tag_erro_codigo, ''))

                    #
                    # Se a prefeitura reponder que a nota já havia sido cancelada, tudo bem
                    #
                    if configuracao.tag_erro_codigo_ja_cancelado and \
                        configuracao.tag_erro_codigo_ja_cancelado == texto_erro:
                        mensagem_erro = ''
                        conexao.erros = []
                        break

                    mensagem_erro += f'Código de retorno: {texto_erro}\n'

                if configuracao.tag_erro_descricao:
                    texto_erro = getattr(erro, configuracao.tag_erro_descricao, '')
                    mensagem_erro += f'Mensagem: {texto_erro}\n'

                conexao.erros.append(erro)

            conexao.mensagem_erro = mensagem_erro

        elif tag_alerta:
            mensagem_alerta = ''

            for alerta in tag_alerta:
                if configuracao.tag_alerta_codigo:
                    texto_alerta = str(getattr(alerta, configuracao.tag_alerta_codigo, ''))

                    #
                    # Se a prefeitura reponder que a nota já havia sido cancelada, tudo bem
                    #
                    if configuracao.tag_alerta_codigo_ja_cancelado and \
                        configuracao.tag_alerta_codigo_ja_cancelado == texto_alerta:
                        mensagem_alerta = ''
                        conexao.erros = []
                        break

                    mensagem_alerta += f'Código de retorno: {texto_alerta}\n'

                if configuracao.tag_alerta_descricao:
                    texto_alerta = getattr(alerta, configuracao.tag_alerta_descricao, '')
                    mensagem_alerta += f'Mensagem: {texto_alerta}\n'

                conexao.erros.append(alerta)

            conexao.mensagem_erro = mensagem_alerta

        return conexao
