# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_401 import ESQUEMA_ATUAL
from pysped.nfe.manual_300 import envinfe_110
import os
from nfe_200 import NFe


DIRNAME = os.path.dirname(__file__)


class EnviNFe(envinfe_110.EnviNFe):
    def __init__(self):
        super(EnviNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'enviNFe', codigo=u'AP02', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/') 
        self.arquivo_esquema = u'enviNFe_v2.00.xsd'


class InfRec(envinfe_110.InfRec):
    def __init__(self):
        super(InfRec, self).__init__()
        
    def get_xml(self):
        if not self.nRec.valor:
            return u''
        
        xml = XMLNFe.get_xml(self)
        xml += u'<infRec>'
        xml += self.nRec.xml
        xml += self.tMed.xml
        xml += u'</infRec>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nRec.xml     = arquivo
            self.tMed.xml     = arquivo
       
    xml = property(get_xml, set_xml)
    

class RetEnviNFe(envinfe_110.RetEnviNFe):
    def __init__(self):
        super(RetEnviNFe, self).__init__()
        self.versao   = TagDecimal(nome=u'retEnviNFe', codigo=u'AR02' , propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.dhRecbto = TagDataHora(nome=u'dhRecbto' , codigo=u'AR09'                        , raiz=u'//retEnviNFe')
        self.infRec   = InfRec()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/') 
        self.arquivo_esquema = u'retEnviNFe_v2.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.dhRecbto.xml
        xml += self.infRec.xml
        xml += u'</retEnviNFe>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.tpAmb.xml    = arquivo
            self.verAplic.xml = arquivo
            self.cStat.xml    = arquivo
            self.xMotivo.xml  = arquivo
            self.cUF.xml      = arquivo
            self.dhRecbto.xml = arquivo
            self.infRec.xml   = arquivo
       
    xml = property(get_xml, set_xml)
             