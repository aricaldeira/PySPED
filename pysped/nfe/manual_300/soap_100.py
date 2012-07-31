# -*- coding: utf-8 -*-


from __future__ import division, print_function, unicode_literals


from pysped.xml_sped import *
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


class CabecMsg(XMLNFe):
    def __init__(self):
        super(CabecMsg, self).__init__()
        self.versao      = TagDecimal(nome='cabecMsg'   , codigo=''   , propriedade='versao', namespace=NAMESPACE_NFE, valor='1.02', raiz='//cabecMsg')
        self.versaoDados = TagDecimal(nome='versaoDados', codigo='A01', raiz='//cabecMsg', tamanho=[1, 4])
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'cabecMsg_v1.02.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.versaoDados.xml
        xml += '</cabecMsg>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versaoDados.xml = arquivo

    xml = property(get_xml, set_xml)


class NFeCabecMsg(XMLNFe):
    def __init__(self):
        super(NFeCabecMsg, self).__init__()
        self.cabec = CabecMsg()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<nfeCabecMsg>'
        xml += tirar_acentos(self.cabec.xml)
        xml += '</nfeCabecMsg>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cabec.xml = arquivo

    xml = property(get_xml, set_xml)


class NFeDadosMsg(XMLNFe):
    def __init__(self):
        super(NFeDadosMsg, self).__init__()
        self.dados = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<nfeDadosMsg>'
        xml += tirar_acentos(self.dados.xml)
        xml += '</nfeDadosMsg>'

        return xml

    def set_xml(self, arquivo):
        pass

    xml = property(get_xml, set_xml)


class SOAPEnvio(XMLNFe):
    def __init__(self):
        super(SOAPEnvio, self).__init__()
        self.webservice = ''
        self.metodo = ''
        self.envio = None
        self.nfeCabecMsg = NFeCabecMsg()
        self.nfeDadosMsg = NFeDadosMsg()
        self._header = {b'content-type': b'application/soap+xml; charset=utf-8',
            b'Accept': b'application/soap+xml; charset=utf-8'}

    def get_xml(self):
        self.nfeDadosMsg.dados = self.envio
        self.nfeCabecMsg.cabec.versaoDados.valor = self.envio.versao.valor

        self._header[b'SOAPAction'] = self.metodo

        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     '<soap:Body>'
        xml +=         '<' + self.metodo + ' xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + '">'
        xml += self.nfeCabecMsg.xml
        xml += self.nfeDadosMsg.xml
        xml +=         '</' + self.metodo + '>'
        xml +=     '</soap:Body>'
        xml += '</soap:Envelope>'
        return xml

    def set_xml(self):
        pass

    xml = property(get_xml, set_xml)

    def get_header(self):
        header = self._header
        return header

    header = property(get_header)


class SOAPRetorno(XMLNFe):
    def __init__(self):
        super(SOAPRetorno, self).__init__()
        self.webservice = ''
        self.metodo = ''
        self.resposta = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     '<soap:Body>'
        xml +=         '<' + self.metodo + 'Response xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + '">'
        xml +=             '<' + self.metodo + 'Result>'
        xml += self.resposta.xml
        xml +=             '</' + self.metodo + 'Result>'
        xml +=         '</' + self.metodo + 'Response>'
        xml +=     '</soap:Body>'
        xml += '</soap:Envelope>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            resposta = por_acentos(self._le_tag('//*/res:' + self.metodo + 'Result',  ns=('http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice)))
            resposta = tira_abertura(resposta)
            #print resposta
            self.resposta.xml = resposta

        return self.xml

    xml = property(get_xml, set_xml)
