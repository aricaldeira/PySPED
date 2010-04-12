# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os
from nfe_110 import NFe


DIRNAME = os.path.dirname(__file__)


class EnviNFe(XMLNFe):
    def __init__(self):
        super(EnviNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'enviNFe', codigo=u'AP02', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.10', raiz=u'/')
        self.idLote  = TagInteiro(nome=u'idLote' , codigo=u'AP03', tamanho=[1, 15, 1], raiz=u'//enviNFe')
        self.NFe     = []
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/') 
        self.arquivo_esquema = u'enviNFe_v1.10.xsd'
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.idLote.xml
        
        for n in self.NFe:
            xml += tira_abertura(n.xml)
            
        xml += u'</enviNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.idLote.xml    = arquivo
            self.NFe = self.le_grupo('//enviLote/NFe', NFe)
            
        return self.xml

    xml = property(get_xml, set_xml)


class InfRec(XMLNFe):
    def __init__(self):
        super(InfRec, self).__init__()
        self.nRec     = TagCaracter(nome=u'nRec'     , codigo=u'AR08', tamanho=[1, 15, 1], raiz=u'//retEnviNFe/infRec')
        self.dhRecbto = TagDataHora(nome=u'dhRecbto', codigo=u'AR09'                    , raiz=u'//retEnviNFe/infRec')
        self.tMed     = TagInteiro(nome=u'tMed'     , codigo=u'AR10', tamanho=[1,  4, 1], raiz=u'//retEnviNFe/infRec')          
        
    def get_xml(self):
        if not self.nRec.valor:
            return u''
        
        xml = XMLNFe.get_xml(self)
        xml += u'<infRec>'
        xml += self.nRec.xml
        xml += self.dhRecbto.xml
        xml += self.tMed.xml
        xml += u'</infRec>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nRec.xml     = arquivo
            self.dhRecbto.xml = arquivo
            self.tMed.xml     = arquivo
       
    xml = property(get_xml, set_xml)
    

class RetEnviNFe(XMLNFe):
    def __init__(self):
        super(RetEnviNFe, self).__init__()
        self.versao   = TagDecimal(nome=u'retEnviNFe', codigo=u'AR02' , propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.10', raiz=u'/')
        self.tpAmb    = TagInteiro(nome=u'tpAmb'     , codigo=u'AR03' , tamanho=[1,   1, 1], raiz=u'//retEnviNFe')
        self.verAplic = TagCaracter(nome=u'verAplic' , codigo=u'AR04' , tamanho=[1,  20]   , raiz=u'//retEnviNFe')
        self.cStat    = TagCaracter(nome=u'cStat'    , codigo=u'AR05' , tamanho=[1,   3]   , raiz=u'//retEnviNFe')
        self.xMotivo  = TagCaracter(nome=u'xMotivo'  , codigo=u'AR06' , tamanho=[1, 255]   , raiz=u'//retEnviNFe')
        self.cUF      = TagCaracter(nome=u'cUF'      , codigo=u'AR06a', tamanho=[2,   2, 2], raiz=u'//retEnviNFe')
        self.infRec   = InfRec()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/') 
        self.arquivo_esquema = u'retEnviNFe_v1.10.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
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
            self.infRec.xml   = arquivo
       
    xml = property(get_xml, set_xml)
             