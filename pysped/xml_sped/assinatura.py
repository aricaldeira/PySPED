# -*- coding: utf-8 -*-

from pysped.xml_sped import XMLNFe, NAMESPACE_SIG, ABERTURA, tira_abertura
import libxml2
import xmlsec
import os


DIRNAME = os.path.dirname(__file__)


class Signature(XMLNFe):
    def __init__(self):
        super(Signature, self).__init__()
        self.URI = u''
        self.DigestValue = u''
        self.SignatureValue = u''
        self.X509Certificate = u''
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/')
        self.arquivo_esquema = u'xmldsig-core-schema_v1.01.xsd'
    
    def get_xml(self):
        if not len(self.URI):
            self.URI = u'#'
        
        if self.URI[0] != u'#':
            self.URI = u'#' + self.URI
        
        xml  = u'<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">'
        xml +=     u'<SignedInfo>'
        xml +=         u'<CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />'
        xml +=         u'<SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" />'
        xml +=         u'<Reference URI="' + self.URI + u'">'
        xml +=             u'<Transforms>'
        xml +=                 u'<Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />'
        xml +=                 u'<Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />'
        xml +=             u'</Transforms>'
        xml +=             u'<DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" />'
        xml +=             u'<DigestValue>' + self.DigestValue + u'</DigestValue>'
        xml +=         u'</Reference>'
        xml +=     u'</SignedInfo>'
        xml +=     u'<SignatureValue>' + self.SignatureValue + u'</SignatureValue>'
        xml +=     u'<KeyInfo>'
        xml +=         u'<X509Data>'
        xml +=             u'<X509Certificate>' + self.X509Certificate + u'</X509Certificate>'
        xml +=         u'</X509Data>'
        xml +=     u'</KeyInfo>'
        xml += u'</Signature>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.URI = self._le_tag(u'//sig:Signature/sig:SignedInfo/sig:Reference', u'URI')
            self.DigestValue = self._le_tag(u'//sig:Signature/sig:SignedInfo/sig:Reference/sig:DigestValue')
            self.SignatureValue = self._le_tag(u'//sig:Signature/sig:SignatureValue')
            self.X509Certificate = self._le_tag(u'//sig:Signature/sig:KeyInfo/sig:X509Data/sig:X509Certificate')

        return self.xml
        
    xml = property(get_xml, set_xml)


def assinar(tipo, doc, arquivo_certificado, senha):
    doc_xml, ctxt, noh_assinatura, assinador=_antes_de_assinar_ou_verificar(tipo, doc, arquivo_certificado, senha)
        
    # Realiza a assinatura
    assinador.sign(noh_assinatura)
    
    # Coloca na instância Signature os valores calculados
    doc.Signature.DigestValue = ctxt.xpathEval(u'//sig:DigestValue')[0].content.replace(u'\n', u'')
    doc.Signature.SignatureValue = ctxt.xpathEval(u'//sig:SignatureValue')[0].content.replace(u'\n', u'')
    # Provavelmente retornarão vários certificados, já que o xmlsec inclui a cadeia inteira
    # Vamos considerar somente o último, que é o certificado do cliente; os demais não devem ser incluí­dos
    certificados = ctxt.xpathEval(u'//sig:X509Data/sig:X509Certificate')
    doc.Signature.X509Certificate = certificados[len(certificados)-1].content.replace(u'\n', u'')
    
    resultado = assinador.status == xmlsec.DSigStatusSucceeded

    _depois_de_assinar_ou_verificar(doc_xml, ctxt, assinador)
    
    return resultado
    
def verificar_assinatura(tipo, doc, arquivo_certificado, senha):
    doc_xml, ctxt, noh_assinatura, assinador = _antes_de_assinar_ou_verificar(tipo, doc, arquivo_certificado, senha)

    # Verifica a assinatura
    assinador.verify(noh_assinatura)
    resultado = assinador.status == xmlsec.DSigStatusSucceeded
    
    _depois_de_assinar_ou_verificar(doc_xml, ctxt, assinador)
    
    return resultado

def _antes_de_assinar_ou_verificar(tipo, doc, arquivo_certificado, senha):
    if tipo == u'NFe':
        doctype = u'<!DOCTYPE NFe [<!ATTLIST infNFe Id ID #IMPLIED>]>'
        #doc.Signature.URI = doc.infNFe.Id.valor
    elif tipo == u'cancNFe':
        doctype = u'<!DOCTYPE cancNFe [<!ATTLIST infCanc Id ID #IMPLIED>]>'
        #doc.Signature.URI = doc.infCanc.Id.valor
    elif tipo == u'inutNFe':
        doctype = u'<!DOCTYPE inutNFe [<!ATTLIST infInut Id ID #IMPLIED>]>'
        #doc.Signature.URI = doc.infInut.Id.valor
    
    #
    # O documento é um arquivo ou uma instância?
    #
    if isinstance(doc, basestring):
        if doc[0] == u'<':
            xml = doc
        else:
            arq = open(doc)
            xml = ''.join(arq.readlines())
            xml = xml.decode(u'utf-8')
            arq.close()
    else:
        xml = doc.xml
    
    #
    # Importantíssimo colocar o encode, pois do contário não é possível
    # assinar caso o xml tenha letras acentuadas
    #
    xml = tira_abertura(xml)
    xml = ABERTURA + xml
    xml = xml.replace(ABERTURA, ABERTURA + doctype).encode(u'utf-8')
    
    # Ativa as funções de análise de arquivos XML
    libxml2.initParser()
    libxml2.substituteEntitiesDefault(1)

    # Ativa as funções da API de criptografia
    xmlsec.init()
    xmlsec.cryptoAppInit(None)
    xmlsec.cryptoInit()
        
    # Colocamos o texto no avaliador XML
    doc_xml = libxml2.parseMemory(xml, len(xml))
    
    # Cria o contexto para manipulação do XML via sintaxe XPATH
    ctxt = doc_xml.xpathNewContext()
    ctxt.xpathRegisterNs(u'sig', NAMESPACE_SIG)
    
    # Separa o nó da assinatura
    noh_assinatura = ctxt.xpathEval(u'//*/sig:Signature')[0]
    
    # Carrega a cadeia certificadora
    #certificados_confiaveis = xmlsec.KeysMngr()
    #xmlsec.cryptoAppDefaultKeysMngrInit(certificados_confiaveis)
    #caminho_cadeia = u'/home/ari/python/pysped/cadeia-certificacao/separados/'
    #for arq in os.listdir(caminho_cadeia):
        #arq = caminho_cadeia + arq
        #certificados_confiaveis.certLoad(filename=str(arq), format=xmlsec.KeyDataFormatPem, type=xmlsec.KeyDataTypeTrusted)
    
    # Cria a variável de chamada (callable) da função de assinatura
    #assinador = xmlsec.DSigCtx(certificados_confiaveis)
    assinador = xmlsec.DSigCtx()

    # Buscamos a chave no arquivo do certificado
    chave = xmlsec.cryptoAppKeyLoad(filename=str(arquivo_certificado), format=xmlsec.KeyDataFormatPkcs12, pwd=str(senha), pwdCallback=None, pwdCallbackCtx=None)
    # Atribui a chave ao assinador
    assinador.signKey = chave
    
    return doc_xml, ctxt, noh_assinatura, assinador

def _depois_de_assinar_ou_verificar(doc_xml, ctxt, assinador):
    ''' Desativa as funções criptográficas e de análise XML
    As funções devem ser chamadas aproximadamente na ordem inversa da ativação
    '''
    # Libera a memória do assinador; isso é necessário, pois na verdade foi feita uma chamada
    # a uma função em C cujo código não é gerenciado pelo Python
    #ctxt.xpathFreeContext()
    doc_xml.freeDoc()
    assinador.destroy()

    #
    # Atenção!!! Pela documentação da biblioteca xmlsec as 2 linhas comentadas são necessárias
    # mas, se elas forem descomentadas, a biblioteca OpenSSL começará a dar erro na transmissão
    # dos arquivos para os webservices
    #

    #xmlsec.cryptoShutdown()
    #xmlsec.cryptoAppShutdown()
    xmlsec.shutdown()
    
    # Shutdown LibXML2
    libxml2.cleanupParser()
