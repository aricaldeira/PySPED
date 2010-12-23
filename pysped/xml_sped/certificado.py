# -*- coding: utf-8 -*-

from pysped.xml_sped import XMLNFe, NAMESPACE_SIG, ABERTURA, tira_abertura
import libxml2
import xmlsec
import os
from datetime import datetime
from time import mktime
from OpenSSL import crypto


DIRNAME = os.path.dirname(__file__)


class Certificado(object):
    def __init__(self):
        self.arquivo     = u''
        self.senha       = u''
        self.chave       = u''
        self.certificado = u''
        self.emissor     = {}
        self.proprietario = {}
        self.data_inicio_validade = None
        self.data_fim_validade    = None
        self._doc_xml    = None

    def prepara_certificado_arquivo_pfx(self):
        # Lendo o arquivo pfx no formato pkcs12 como binário
        pkcs12 = crypto.load_pkcs12(open(self.arquivo, 'rb').read(), self.senha)

        # Retorna a string decodificada da chave privada
        self.chave = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())

        # Retorna a string decodificada do certificado
        self.prepara_certificado_txt(crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate()))

    def prepara_certificado_arquivo_pem(self):
        self.prepara_certificado_txt(open(self.arquivo, 'rb').read())

    def prepara_certificado_txt(self, cert_txt):
        #
        # Para dar certo a leitura pelo xmlsec, temos que separar o certificado
        # em linhas de 64 caracteres de extensão...
        #
        cert_txt = cert_txt.replace(u'\n', u'')
        cert_txt = cert_txt.replace(u'-----BEGIN CERTIFICATE-----', u'')
        cert_txt = cert_txt.replace(u'-----END CERTIFICATE-----', u'')

        linhas_certificado = [u'-----BEGIN CERTIFICATE-----\n']
        for i in range(0, len(cert_txt), 64):
            linhas_certificado.append(cert_txt[i:i+64] + '\n')
        linhas_certificado.append(u'-----END CERTIFICATE-----\n')

        self.certificado = u''.join(linhas_certificado)

        cert_openssl = crypto.load_certificate(crypto.FILETYPE_PEM, self.certificado)

        self.emissor = dict(cert_openssl.get_issuer().get_components())
        self.proprietario = dict(cert_openssl.get_subject().get_components())

        self.data_inicio_validade = datetime.strptime(cert_openssl.get_notBefore(), '%Y%m%d%H%M%SZ')
        self.data_fim_validade    = datetime.strptime(cert_openssl.get_notAfter(), '%Y%m%d%H%M%SZ')

    def _inicia_funcoes_externas(self):
        # Ativa as funções de análise de arquivos XML
        libxml2.initParser()
        libxml2.substituteEntitiesDefault(1)

        # Ativa as funções da API de criptografia
        xmlsec.init()
        xmlsec.cryptoAppInit(None)
        xmlsec.cryptoInit()

    def _finaliza_funcoes_externas(self):
        ''' Desativa as funções criptográficas e de análise XML
        As funções devem ser chamadas na ordem inversa da ativação
        '''
        #xmlsec.cryptoShutdown()
        #xmlsec.cryptoAppShutdown()
        xmlsec.shutdown()

        libxml2.cleanupParser()

    def assina_xmlnfe(self, doc):
        if not isinstance(doc, XMLNFe):
            raise ValueError('O documento nao e do tipo esperado: XMLNFe')

        # Realiza a assinatura
        xml = self.assina_xml(doc.xml)

        # Devolve os valores para a instância doc
        doc.Signature.xml = xml

    def assina_arquivo(self, doc):
        xml = open(doc, 'r').read()
        xml = self.assina_xml(xml)
        return xml

    def _prepara_doc_xml(self, xml):
        if isinstance(xml, str):
            xml = unicode(xml.encode('utf-8'))

        #
        # Determina o tipo de arquivo que vai ser assinado, procurando
        # pela tag correspondente
        #
        
        #
        # XML da NF-e nacional
        #
        if u'infNFe' in xml:
            doctype = u'<!DOCTYPE NFe [<!ATTLIST infNFe Id ID #IMPLIED>]>'
        elif u'infCanc' in xml:
            doctype = u'<!DOCTYPE cancNFe [<!ATTLIST infCanc Id ID #IMPLIED>]>'
        elif u'infInut' in xml:
            doctype = u'<!DOCTYPE inutNFe [<!ATTLIST infInut Id ID #IMPLIED>]>'
            
        #
        # XML da NFS-e
        #
        elif u'ReqEnvioLoteRPS' in xml:
            doctype = u'<!DOCTYPE Lote [<!ATTLIST Lote Id ID #IMPLIED>]>'
            
        else:
            raise ValueError('Tipo de arquivo desconhecido para assinatura/validacao')

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
        xml = xml.replace(u'\n', u'')

        return xml

    def _finaliza_xml(self, xml):
        if isinstance(xml, str):
            xml = unicode(xml.decode('utf-8'))

        #
        # Determina o tipo de arquivo que vai ser assinado, procurando
        # pela tag correspondente
        #

        #
        # XML da NF-e nacional
        #
        if u'infNFe' in xml:
            doctype = u'<!DOCTYPE NFe [<!ATTLIST infNFe Id ID #IMPLIED>]>'
        elif u'infCanc' in xml:
            doctype = u'<!DOCTYPE cancNFe [<!ATTLIST infCanc Id ID #IMPLIED>]>'
        elif u'infInut' in xml:
            doctype = u'<!DOCTYPE inutNFe [<!ATTLIST infInut Id ID #IMPLIED>]>'

        #
        # XML da NFS-e
        #
        elif u'ReqEnvioLoteRPS' in xml:
            doctype = u'<!DOCTYPE Lote [<!ATTLIST Lote Id ID #IMPLIED>]>'

        else:
            raise ValueError('Tipo de arquivo desconhecido para assinatura/validacao')

        #
        # Remove o doctype e os \n acrescentados pela libxml2
        #
        xml = xml.replace(u'\n', u'')
        xml = xml.replace(ABERTURA + doctype, ABERTURA)

        return xml

    def assina_xml(self, xml):
        self._inicia_funcoes_externas()
        xml = self._prepara_doc_xml(xml)

        #
        # Colocamos o texto no avaliador XML
        #
        doc_xml = libxml2.parseMemory(xml.encode('utf-8'), len(xml.encode('utf-8')))

        #
        # Separa o nó da assinatura
        #
        noh_assinatura = xmlsec.findNode(doc_xml.getRootElement(), xmlsec.NodeSignature, xmlsec.DSigNs)

        #
        # Cria a variável de chamada (callable) da função de assinatura
        #
        assinador = xmlsec.DSigCtx()

        #
        # Buscamos a chave no arquivo do certificado
        #
        chave = xmlsec.cryptoAppKeyLoad(filename=str(self.arquivo), format=xmlsec.KeyDataFormatPkcs12, pwd=str(self.senha), pwdCallback=None, pwdCallbackCtx=None)

        #
        # Atribui a chave ao assinador
        #
        assinador.signKey = chave

        #
        # Realiza a assinatura
        #
        assinador.sign(noh_assinatura)

        #
        # Guarda o status
        #
        status = assinador.status

        #
        # Libera a memória ocupada pelo assinador manualmente
        #
        assinador.destroy()

        if status != xmlsec.DSigStatusSucceeded:
            #
            # Libera a memória ocupada pelo documento xml manualmente
            #
            doc_xml.freeDoc()
            self._finaliza_funcoes_externas()
            raise RuntimeError('Erro ao realizar a assinatura do arquivo; status: "' + str(status) + '"')

        #
        # Elimina do xml assinado a cadeia certificadora, deixando somente
        # o certificado que assinou o documento
        #
        xpath = doc_xml.xpathNewContext()
        xpath.xpathRegisterNs(u'sig', NAMESPACE_SIG)
        certificados = xpath.xpathEval(u'//sig:X509Data/sig:X509Certificate')
        for i in range(len(certificados)-1):
            certificados[i].unlinkNode()
            certificados[i].freeNode()

        #
        # Retransforma o documento xml em texto
        #
        xml = doc_xml.serialize()

        #
        # Libera a memória ocupada pelo documento xml manualmente
        #
        doc_xml.freeDoc()
        self._finaliza_funcoes_externas()

        xml = self._finaliza_xml(xml)

        return xml

    def verifica_assinatura_xmlnfe(self, doc):
        if not isinstance(doc, XMLNFe):
            raise ValueError('O documento nao e do tipo esperado: XMLNFe')

        return self.verifica_assinatura_xml(doc.xml)

    def verifica_assinatura_arquivo(self, doc):
        xml = open(doc, 'r').read()
        return self.verifica_assinatura_xml(xml)

    def verifica_assinatura_xml(self, xml):
        self._inicia_funcoes_externas()
        xml = self._prepara_doc_xml(xml)

        #
        # Colocamos o texto no avaliador XML
        #
        doc_xml = libxml2.parseMemory(xml, len(xml))

        #
        # Separa o nó da assinatura
        #
        noh_assinatura = xmlsec.findNode(doc_xml.getRootElement(), xmlsec.NodeSignature, xmlsec.DSigNs)

        #
        # Prepara o gerenciador dos certificados confiáveis para verificação
        #
        certificados_confiaveis = xmlsec.KeysMngr()
        xmlsec.cryptoAppDefaultKeysMngrInit(certificados_confiaveis)

        #
        # Prepara a cadeia certificadora
        #
        certificados = os.listdir(DIRNAME + '/cadeia-certificadora/certificados')
        certificados.sort()
        for certificado in certificados:
            certificados_confiaveis.certLoad(filename=str(DIRNAME + '/cadeia-certificadora/certificados/' + certificado), format=xmlsec.KeyDataFormatPem, type=xmlsec.KeyDataTypeTrusted)

        #
        # Cria a variável de chamada (callable) da função de assinatura/verificação,
        # agora passando quais autoridades certificadoras são consideradas
        # confiáveis
        #
        verificador = xmlsec.DSigCtx(certificados_confiaveis)

        #
        # Separa o certificado que assinou o arquivo, e prepara a instância
        # com os dados desse certificado
        #
        certificado = xmlsec.findNode(noh_assinatura, xmlsec.NodeX509Certificate, xmlsec.DSigNs).content
        self.prepara_certificado_txt(certificado)

        #
        # Recupera a chave do certificado que assinou o documento, e altera
        # a data que será usada para fazer a verificação, para que a assinatura
        # seja validada mesmo que o certificado já tenha expirado
        # Para isso, define a data de validação para a data de início da validade
        # do certificado
        # Essa data deve ser informada como um inteiro tipo "unixtime"
        #
        noh_chave = xmlsec.findNode(noh_assinatura, xmlsec.NodeKeyInfo, xmlsec.DSigNs)
        manipulador_chave = xmlsec.KeyInfoCtx(mngr=certificados_confiaveis)
        manipulador_chave.certsVerificationTime = mktime(self.data_inicio_validade.timetuple())

        #
        # Cria uma chave vazia e recupera a chave, dizendo ao verificador que
        # é essa a chave que deve ser usada na validação da assinatura
        #
        verificador.signKey = xmlsec.Key()
        xmlsec.keyInfoNodeRead(noh_chave, verificador.signKey, manipulador_chave)

        #
        # Realiza a verificação
        #
        verificador.verify(noh_assinatura)

        #
        # Guarda o status
        #
        status = verificador.status
        resultado = status == xmlsec.DSigStatusSucceeded

        #
        # Libera a memória ocupada pelo verificador manualmente
        #
        verificador.destroy()
        certificados_confiaveis.destroy()

        if status != xmlsec.DSigStatusSucceeded:
            #
            # Libera a memória ocupada pelo documento xml manualmente
            #
            doc_xml.freeDoc()
            self._finaliza_funcoes_externas()
            raise RuntimeError('Erro ao validar a assinatura do arquivo; status: "' + str(status) + '"')

        #
        # Libera a memória ocupada pelo documento xml manualmente
        #
        doc_xml.freeDoc()
        self._finaliza_funcoes_externas()

        return resultado
