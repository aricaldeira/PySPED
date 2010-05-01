# -*- coding: utf-8 -*-


from pysped.xml_sped import *
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


class CabecMsg(XMLNFe):
    def __init__(self):
        super(CabecMsg, self).__init__()
        self.versao      = TagDecimal(nome=u'cabecMsg'   , codigo=u''   , propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.02', raiz=u'//cabecMsg')
        self.versaoDados = TagDecimal(nome=u'versaoDados', codigo=u'A01', raiz=u'//cabecMsg', tamanho=[1, 4])
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'cabecMsg_v1.02.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.versaoDados.xml
        xml += u'</cabecMsg>'
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
        xml += u'<nfeCabecMsg>'
        xml += tirar_acentos(self.cabec.xml)
        xml += u'</nfeCabecMsg>'
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
        xml += u'<nfeDadosMsg>'
        xml += tirar_acentos(self.dados.xml)
        xml += u'</nfeDadosMsg>'

        return xml

    def set_xml(self, arquivo):
        pass

    xml = property(get_xml, set_xml)


class SOAPEnvio(XMLNFe):
    def __init__(self):
        super(SOAPEnvio, self).__init__()
        self.webservice = u''
        self.metodo = u''
        self.envio = None
        self.nfeCabecMsg = NFeCabecMsg()
        self.nfeDadosMsg = NFeDadosMsg()
        self._header = {u'content-type': u'application/soap+xml; charset=utf-8',
            u'Accept': u'application/soap+xml; charset=utf-8'}

    def get_xml(self):
        self.nfeDadosMsg.dados = self.envio
        self.nfeCabecMsg.cabec.versaoDados.valor = self.envio.versao.valor

        self._header['SOAPAction'] = self.metodo

        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += u'<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     u'<soap:Body>'
        xml +=         u'<' + self.metodo + u' xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + u'">'
        xml += self.nfeCabecMsg.xml
        xml += self.nfeDadosMsg.xml
        xml +=         u'</' + self.metodo + u'>'
        xml +=     u'</soap:Body>'
        xml += u'</soap:Envelope>'
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
        self.webservice = u''
        self.metodo = u''
        self.resposta = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += u'<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     u'<soap:Body>'
        xml +=         u'<' + self.metodo + u'Response xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + u'">'
        xml +=             u'<' + self.metodo + u'Result>'
        xml += self.resposta.xml
        xml +=             u'</' + self.metodo + u'Result>'
        xml +=         u'</' + self.metodo + u'Response>'
        xml +=     u'</soap:Body>'
        xml += u'</soap:Envelope>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            resposta = por_acentos(self._le_tag(u'//*/res:' + self.metodo + u'Result',  ns=(u'http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice)))
            resposta = tira_abertura(resposta)
            #print resposta
            self.resposta.xml = resposta

        return self.xml

    xml = property(get_xml, set_xml)
