# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)

class CTeCabecMsg(XMLNFe):
    def __init__(self):
        super(CTeCabecMsg, self).__init__()
        self.webservice = ''
        self.cUF = TagInteiro(nome=u'cUF', raiz=u'//cteCabecMsg', tamanho=[2, 2])
        self.versaoDados = TagDecimal(nome=u'versaoDados', raiz=u'//cteCabecMsg', tamanho=[1, 4], valor=u'3.00')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<cteCabecMsg xmlns="http://www.portalfiscal.inf.br/cte/wsdl/' + self.webservice + u'">'
        xml += self.cUF.xml
        xml += self.versaoDados.xml
        xml += u'</cteCabecMsg>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml = arquivo
            self.versaoDados.xml = arquivo

        return self.xml

    xml = property(get_xml, set_xml)

    
class CTeDadosMsg(XMLNFe):
    def __init__(self):
        super(CTeDadosMsg, self).__init__()
        self.webservice = ''
        self.dados = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<cteDadosMsg xmlns="http://www.portalfiscal.inf.br/cte/wsdl/' + self.webservice + '">'
        xml += tira_abertura(self.dados.xml)
        xml += '</cteDadosMsg>'
        return xml

    def set_xml(self, arquivo):
        pass

    xml = property(get_xml, set_xml)
    
    
class SOAPEnvio(XMLNFe):
    def __init__(self):
        super(SOAPEnvio, self).__init__()
        self.webservice = u''
        self.metodo = u''
        self.cUF    = None
        self.envio  = None
        self.cteCabecMsg = CTeCabecMsg()
        self.cteDadosMsg = CTeDadosMsg()
        self._header = {u'content-type': u'application/soap+xml; charset=utf-8'}

    def get_xml(self):
        self.cteCabecMsg.webservice = self.webservice
        self.cteCabecMsg.cUF.valor = self.cUF
        self.cteCabecMsg.versaoDados.valor = self.envio.versao.valor

        self.cteDadosMsg.webservice = self.webservice
        self.cteDadosMsg.dados = self.envio
        
        self._header[u'content-type'] = u'application/soap+xml; charset=utf-8; action="http://www.portalfiscal.inf.br/cte/wsdl/' + self.webservice + u'"'
        
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += u'<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     u'<soap:Header>'
        xml +=             self.cteCabecMsg.xml
        xml +=     u'</soap:Header>'
        xml +=     u'<soap:Body>'
        xml +=             self.cteDadosMsg.xml
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
        self.webservice = ''
        self.metodo = ''
        self.cteCabecMsg = CTeCabecMsg()
        self.resposta = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     '<soap:Header>'
        xml +=         '<cteCabecMsg xmlns="http://www.portalfiscal.inf.br/cte/wsdl/' + self.webservice + '">'
        xml +=             self.cteCabecMsg.xml
        xml +=         '</cteCabecMsg>'
        xml +=     '</soap:Header>'
        xml +=     '<soap:Body>'
        xml +=         '<' + self.metodo + 'Result xmlns="http://www.portalfiscal.inf.br/cte/wsdl/' + self.webservice + '">'
        xml +=             self.resposta.xml
        xml +=         '</' + self.metodo + 'Result>'
        xml +=     '</soap:Body>'
        xml += '</soap:Envelope>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cteCabecMsg.xml = arquivo
            self.resposta.xml = arquivo

    xml = property(get_xml, set_xml)