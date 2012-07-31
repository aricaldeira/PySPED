# -*- coding: utf-8 -*-


from __future__ import division, print_function, unicode_literals


from pysped.xml_sped import *
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os
from nfe_110 import NFe


DIRNAME = os.path.dirname(__file__)


class EnviNFe(XMLNFe):
    def __init__(self):
        super(EnviNFe, self).__init__()
        self.versao  = TagDecimal(nome='enviNFe', codigo='AP02', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.10', raiz='/')
        self.idLote  = TagInteiro(nome='idLote' , codigo='AP03', tamanho=[1, 15, 1], raiz='//enviNFe')
        self.NFe     = []
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/') 
        self.arquivo_esquema = 'enviNFe_v1.10.xsd'
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.idLote.xml
        
        for n in self.NFe:
            xml += tira_abertura(n.xml)
            
        xml += '</enviNFe>'
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
        self.nRec     = TagCaracter(nome='nRec'     , codigo='AR08', tamanho=[1, 15, 1], raiz='//retEnviNFe/infRec')
        self.dhRecbto = TagDataHora(nome='dhRecbto', codigo='AR09'                    , raiz='//retEnviNFe/infRec')
        self.tMed     = TagInteiro(nome='tMed'     , codigo='AR10', tamanho=[1,  4, 1], raiz='//retEnviNFe/infRec')          
        
    def get_xml(self):
        if not self.nRec.valor:
            return ''
        
        xml = XMLNFe.get_xml(self)
        xml += '<infRec>'
        xml += self.nRec.xml
        xml += self.dhRecbto.xml
        xml += self.tMed.xml
        xml += '</infRec>'
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
        self.versao   = TagDecimal(nome='retEnviNFe', codigo='AR02' , propriedade='versao', namespace=NAMESPACE_NFE, valor='1.10', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'     , codigo='AR03' , tamanho=[1,   1, 1], raiz='//retEnviNFe')
        self.verAplic = TagCaracter(nome='verAplic' , codigo='AR04' , tamanho=[1,  20]   , raiz='//retEnviNFe')
        self.cStat    = TagCaracter(nome='cStat'    , codigo='AR05' , tamanho=[1,   3]   , raiz='//retEnviNFe')
        self.xMotivo  = TagCaracter(nome='xMotivo'  , codigo='AR06' , tamanho=[1, 255]   , raiz='//retEnviNFe')
        self.cUF      = TagCaracter(nome='cUF'      , codigo='AR06a', tamanho=[2,   2, 2], raiz='//retEnviNFe')
        self.infRec   = InfRec()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/') 
        self.arquivo_esquema = 'retEnviNFe_v1.10.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.infRec.xml
        xml += '</retEnviNFe>'
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
             