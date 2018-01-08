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

from io import open
import sys
import os
import base64
import signxml
from OpenSSL import crypto
from lxml import etree
from datetime import datetime
from pytz import UTC
from pysped.xml_sped import XMLNFe, NAMESPACE_SIG, ABERTURA, tira_abertura
from pysped.xml_sped.assinatura import Signature


DIRNAME = os.path.dirname(__file__)


class Certificado(object):
    def __init__(self):
        self.stream_certificado = None
        self.arquivo     = ''
        self.senha       = ''
        self.chave       = ''
        self.certificado = ''
        self._emissor     = {}
        self._proprietario = {}
        self._data_inicio_validade = None
        self._data_fim_validade    = None
        self._numero_serie = None
        self._extensoes = {}
        self._doc_xml    = None
        self._certificado_preparado = False

    def prepara_certificado_arquivo_pfx(self):
        if self._certificado_preparado:
            return

        # Lendo o arquivo pfx no formato pkcs12 como binário
        if self.stream_certificado is None:
            self.stream_certificado = open(self.arquivo, 'rb').read()

        pkcs12 = crypto.load_pkcs12(self.stream_certificado, self.senha)

        # Retorna a string decodificada da chave privada
        self.chave = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())

        # Retorna a string decodificada do certificado
        certificado = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate())

        if sys.version_info.major == 3:
            certificado = certificado.decode('utf-8')

        self.prepara_certificado_txt(certificado)

        self._certificado_preparado = True

    def prepara_certificado_arquivo_pem(self):
        if self._certificado_preparado:
            return

        if self.stream_certificado is None:
            self.stream_certificado = open(self.arquivo, 'rb').read()

        self.prepara_certificado_txt(self.stream_certificado)

        self._certificado_preparado = True

    def prepara_certificado_txt(self, cert_txt):
        #
        # Para dar certo a leitura pelo xmlsec, temos que separar o certificado
        # em linhas de 64 caracteres de extensão...
        #
        cert_txt = cert_txt.replace('\n', '')
        cert_txt = cert_txt.replace('-----BEGIN CERTIFICATE-----', '')
        cert_txt = cert_txt.replace('-----END CERTIFICATE-----', '')

        linhas_certificado = ['-----BEGIN CERTIFICATE-----\n']
        for i in range(0, len(cert_txt), 64):
            linhas_certificado.append(cert_txt[i:i+64] + '\n')
        linhas_certificado.append('-----END CERTIFICATE-----\n')

        self.certificado = ''.join(linhas_certificado)

        cert_openssl = crypto.load_certificate(crypto.FILETYPE_PEM, self.certificado)
        self.cert_openssl = cert_openssl
        self._numero_serie = cert_openssl.get_serial_number()

        for i in range(cert_openssl.get_extension_count()):
            extensao = cert_openssl.get_extension(i)
            self._extensoes[extensao.get_short_name()] = extensao.get_data()

        self._emissor = {}
        for chave, valor in cert_openssl.get_issuer().get_components():
            chave = chave.decode('utf-8')
            valor = valor.decode('utf-8')
            self._emissor[chave] = valor

        self._proprietario = {}
        for chave, valor in cert_openssl.get_subject().get_components():
            chave = chave.decode('utf-8')
            valor = valor.decode('utf-8')
            self._proprietario[chave] = valor

        if sys.version_info.major == 3:
            self._data_inicio_validade = \
                datetime.strptime(cert_openssl.get_notBefore().decode('utf-8'), '%Y%m%d%H%M%SZ')
            self._data_fim_validade    = \
                datetime.strptime(cert_openssl.get_notAfter().decode('utf-8'), '%Y%m%d%H%M%SZ')

        else:
            #self._emissor = dict(cert_openssl.get_issuer().get_components())
            #self._proprietario = dict(cert_openssl.get_subject().get_components())
            self._data_inicio_validade = \
                datetime.strptime(cert_openssl.get_notBefore(), '%Y%m%d%H%M%SZ')
            self._data_fim_validade    = \
                datetime.strptime(cert_openssl.get_notAfter(), '%Y%m%d%H%M%SZ')

        self._data_inicio_validade = \
            UTC.localize(self._data_inicio_validade)
        self._data_fim_validade    = \
            UTC.localize(self._data_fim_validade)

    def _set_arquivo(self, arquivo):
        self._arquivo = arquivo
        self._certificado_preparado = False

    def _get_arquivo(self):
        return self._arquivo

    arquivo = property(_get_arquivo, _set_arquivo)

    def _set_senha(self, senha):
        self._senha = senha
        self._certificado_preparado = False

    def _get_senha(self):
        return self._senha

    senha = property(_get_senha, _set_senha)

    def _set_chave(self, chave):
        self._chave = chave

    def _get_chave(self):
        try:
            if self._chave:
                return self._chave
            else:
                raise AttributeError("'chave' precisa ser regenerada")
        except AttributeError:
            if self.arquivo:    # arquivo disponível
                self.prepara_certificado_arquivo_pfx()
                return self._chave  # agora já disponível
            else:
                return ''

    chave = property(_get_chave, _set_chave)

    def _set_certificado(self, certificado):
        self._certificado = certificado

    def _get_certificado(self):
        try:
            if self._certificado:
                return self._certificado
            else:
                raise AttributeError("'certificado' precisa ser regenerado")
        except AttributeError:
            if self.arquivo:    # arquivo disponível
                self.prepara_certificado_arquivo_pfx()
                return self._certificado  # agora já disponível
            else:
                return ''

    certificado = property(_get_certificado, _set_certificado)

    @property
    def proprietario_nome(self):
        if 'CN' in self.proprietario:
            #
            # Alguns certificados não têm o CNPJ na propriedade CN, somente o
            # nome do proprietário
            #
            if ':' in self.proprietario['CN']:
                return self.proprietario['CN'].rsplit(':',1)[0]
            else:
                return self.proprietario['CN']
        else: # chave CN ainda não disponível
            try:
                self.prepara_certificado_arquivo_pfx()
                return self.proprietario['CN'].rsplit(':',1)[0]
            except IOError:  # arquivo do certificado não disponível
                return ''

    @property
    def proprietario_cnpj(self):
        if 'CN' in self.proprietario:
            #
            # Alguns certificados não têm o CNPJ na propriedade CN, somente o
            # nome do proprietário
            #
            if ':' in self.proprietario['CN']:
                return self.proprietario['CN'].rsplit(':',1)[1]
            else:
                return ''
        else: #chave CN ainda não disponível
            try:
                self.prepara_certificado_arquivo_pfx()
                return self.proprietario['CN'].rsplit(':',1)[1]
            except IOError:  # arquivo do certificado não disponível
                return ''

    @property
    def proprietario(self):
        if self._proprietario:
            return self._proprietario
        else:
            try:
                self.prepara_certificado_arquivo_pfx()
                return self._proprietario
            except IOError:  # arquivo do certificado não disponível
                return dict()

    @property
    def emissor(self):
        if self._emissor:
            return self._emissor
        else:
            try:
                self.prepara_certificado_arquivo_pfx()
                return self._emissor
            except IOError:  # arquivo do certificado não disponível
                return dict()

    @property
    def data_inicio_validade(self):
        if self._data_inicio_validade:
            return self._data_inicio_validade
        else:
            try:
                self.prepara_certificado_arquivo_pfx()
                return self._data_inicio_validade
            except IOError:  # arquivo do certificado não disponível
                return None

    @property
    def data_fim_validade(self):
        if self._data_fim_validade:
            return self._data_fim_validade
        else:
            try:
                self.prepara_certificado_arquivo_pfx()
                return self._data_fim_validade
            except IOError:  # arquivo do certificado não disponível
                return None

    @property
    def numero_serie(self):
        if self._numero_serie:
            return self._numero_serie
        else:
            try:
                self.prepara_certificado_arquivo_pfx()
                return self._numero_serie
            except IOError:  # arquivo do certificado não disponível
                return None

    @property
    def extensoes(self):
        if self._extensoes:
            return self._extensoes
        else:
            try:
                self.prepara_certificado_arquivo_pfx()
                return self._extensoes
            except IOError:  # arquivo do certificado não disponível
                return dict()

    def assina_xmlnfe(self, doc):
        if not isinstance(doc, XMLNFe):
            raise ValueError('O documento nao e do tipo esperado: XMLNFe')

        # Realiza a assinatura
        xml = self.assina_xml(doc.xml)

        # Devolve os valores para a instância doc
        doc.Signature.xml = xml

    def assina_arquivo(self, doc):
        xml = open(doc, 'r', encoding='utf-8').read()
        xml = self.assina_xml(xml)
        return xml

    def _obtem_doctype(self, xml):
        """Obtém DOCTYPE do XML

        Determina o tipo de arquivo que vai ser assinado, procurando pela tag
        correspondente.
        """
        doctype = None

        #
        # XML da NF-e
        #
        if '</NFe>' in xml:
            doctype = '<!DOCTYPE NFe [<!ATTLIST infNFe Id ID #IMPLIED>]>'
        elif '</cancNFe>' in xml:
            doctype = '<!DOCTYPE cancNFe [<!ATTLIST infCanc Id ID #IMPLIED>]>'
        elif '</inutNFe>' in xml:
            doctype = '<!DOCTYPE inutNFe [<!ATTLIST infInut Id ID #IMPLIED>]>'
        elif '</infEvento>' in xml:
            doctype = '<!DOCTYPE evento [<!ATTLIST infEvento Id ID #IMPLIED>]>'

        #
        # XML do CT-e
        #
        elif '</CTe>' in xml:
            doctype = '<!DOCTYPE CTe [<!ATTLIST infCte Id ID #IMPLIED>]>'
        elif '</cancCTe>' in xml:
            doctype = '<!DOCTYPE cancCTe [<!ATTLIST infCanc Id ID #IMPLIED>]>'
        elif '</inutCTe>' in xml:
            doctype = '<!DOCTYPE inutCTe [<!ATTLIST infInut Id ID #IMPLIED>]>'
        #elif 'infEvento' in xml:
            #doctype = '<!DOCTYPE evento [<!ATTLIST infEvento Id ID #IMPLIED>]>'

        #
        # XML da NFS-e
        #
        elif 'ReqEnvioLoteRPS' in xml:
            doctype = '<!DOCTYPE Lote [<!ATTLIST Lote Id ID #IMPLIED>]>'
        elif 'EnviarLoteRpsEnvio' in xml:
            doctype = '<!DOCTYPE EnviarLoteRpsEnvio>'
        elif 'CancelarNfseEnvio' in xml:
            doctype = '<!DOCTYPE CancelarNfseEnvio>'

        else:
            raise ValueError('Tipo de arquivo desconhecido para assinatura/validacao')

        return doctype

    def _prepara_doc_xml(self, xml):
        if sys.version_info.major == 2:
            if isinstance(xml, str):
                xml = unicode(xml.encode('utf-8'))

        doctype = self._obtem_doctype(xml)

        #
        # Importantíssimo colocar o encode, pois do contário não é possível
        # assinar caso o xml tenha letras acentuadas
        #
        xml = tira_abertura(xml)
        xml = ABERTURA + xml
        xml = xml.replace(ABERTURA, ABERTURA + doctype)

        #
        # Remove todos os \n
        #
        xml = xml.replace('\n', '')
        xml = xml.replace('\r', '')

        return xml

    def _finaliza_xml(self, xml):
        if sys.version_info.major == 2:
            if isinstance(xml, str):
                xml = unicode(xml.decode('utf-8'))

        doctype = self._obtem_doctype(xml)

        #
        # Remove o doctype e os \n
        #
        xml = xml.replace('\n', '')
        xml = xml.replace('\r', '')
        xml = xml.replace(ABERTURA + doctype, ABERTURA)

        return xml

    def assina_xml(self, xml):
        xml = self._prepara_doc_xml(xml)

        assinatura = Signature()
        assinatura.xml = xml

        #
        # Tiramos a tag de assinatura, o signxml vai colocar de novo
        #
        if '<Signature ' in xml:
            partes = xml.split('<Signature ')
            xml_sem_assinatura = ''.join(partes[:-1])
            partes = partes[-1].split('</Signature>')
            xml_sem_assinatura += ''.join(partes[-1])
            xml = xml_sem_assinatura

        #
        # Colocamos o texto no avaliador XML
        #
        doc_xml = etree.fromstring(xml.encode('utf-8'))

        assinador = signxml.XMLSigner(
            method=signxml.methods.enveloped,
            signature_algorithm='rsa-sha1',
            digest_algorithm='sha1',
            c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315'
        )
        assinador.namespaces = {None: assinador.namespaces['ds']}

        doc_xml = assinador.sign(doc_xml, key=self.chave, cert=self.certificado, reference_uri=assinatura.URI)

        #
        # Retransforma o documento xml em texto
        #
        xml = etree.tounicode(doc_xml)

        xml = self._finaliza_xml(xml)

        return xml

    def verifica_assinatura_xmlnfe(self, doc):
        if not isinstance(doc, XMLNFe):
            raise ValueError('O documento nao e do tipo esperado: XMLNFe')

        return self.verifica_assinatura_xml(doc.xml)

    def verifica_assinatura_arquivo(self, doc):
        xml = open(doc, 'r').read().decode('utf-8')
        return self.verifica_assinatura_xml(xml)

    def verifica_assinatura_xml(self, xml):
        xml = self._prepara_doc_xml(xml)

        #
        # Colocamos o texto no avaliador XML
        #
        doc_xml = etree.fromstring(xml.encode('utf-8'))

        #
        # A validação deve ser feita somente pela tag assinada, assim, se a
        # tag assinada estiver dentro de outras, precisamos tirar ela de lá
        # pra poder valira corretamente a assinatura
        #
        assinatura = doc_xml.xpath('//sig:Signature', namespaces={'sig': 'http://www.w3.org/2000/09/xmldsig#'})
        doc_xml = assinatura[0].getparent()

        verificador = signxml.XMLVerifier()

        #
        # Separa o certificado da assinatura
        #
        noh_certificado = verificador._findall(doc_xml, 'X509Certificate', anywhere=True)

        if not noh_certificado:
            raise ValueError(u'XML sem nó X509Certificate!')

        noh_certificado = noh_certificado[0]

        self.prepara_certificado_txt(noh_certificado.text)

        #
        # Vai levantar exceção caso a assinatura seja inválida
        #
        verificador.verify(
            doc_xml,
            ca_pem_file=os.path.join(DIRNAME,'cadeia.pem'),
            x509_cert=self.cert_openssl,
        )

        return True

    def assina_texto(self, texto):
        #
        # Carrega o arquivo do certificado
        #
        pkcs12 = crypto.load_pkcs12(open(self.arquivo, 'rb').read(), self.senha)

        assinatura = crypto.sign(pkcs12.get_privatekey(), texto, 'sha1')

        return base64.encode(assinatura)

    def verifica_assinatura_texto(self, texto, assinatura):
        #
        # Carrega o arquivo do certificado
        #
        pkcs12 = crypto.load_pkcs12(open(self.arquivo, 'rb').read(), self.senha)

        try:
            crypto.verify(pkcs12.get_certificate(), assinatura, texto, 'sha1')
        except:
            return False

        return True

