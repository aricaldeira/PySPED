# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)

class ConsStatServCTe(XMLNFe):
    def __init__(self):
        super(ConsStatServCTe, self).__init__()
        self.versao  = TagDecimal(nome=u'consStatServCte', codigo=u'FP02', propriedade=u'versao', namespace=NAMESPACE_CTE, valor=u'3.00', raiz=u'/')
        self.tpAmb = TagInteiro(nome=u'tpAmb', codigo=u'FP03', tamanho=[1, 1, 1], raiz=u'//consStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, valor=2)
        self.xServ = TagCaracter(nome=u'xServ', codigo=u'FP04', tamanho=[6, 6], raiz=u'//consStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, valor=u'STATUS')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'consStatServCTe_v3.00.xsd'
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += u'</consStatServCte>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml  = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class RetConsStatServCTe(XMLNFe):
    def __init__(self):
        super(RetConsStatServCTe, self).__init__()
        self.versao  = TagDecimal(nome=u'retConsStatServCte', codigo=u'FR02', propriedade=u'versao', namespace=NAMESPACE_CTE, valor=u'3.00', raiz=u'/')
        self.tpAmb = TagInteiro(nome=u'tpAmb', codigo=u'FR03', tamanho=[1, 1, 1], raiz=u'//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, valor=2)
        self.verAplic = TagCaracter(nome=u'verAplic', codigo=u'FR04', tamanho=[1, 20], raiz=u'//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cStat = TagInteiro(nome=u'cStat', codigo=u'FR05', tamanho=[3, 3, 3], raiz=u'//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xMotivo = TagCaracter(nome=u'xMotivo', codigo=u'FR06', tamanho=[1, 255], raiz=u'//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cUF = TagInteiro(nome=u'cUF', codigo=u'FR07', tamanho=[2, 2, 2], raiz=u'//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dhRecbto = TagDataHora(nome=u'dhRecbto', codigo=u'FR08', raiz=u'//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.tMed = TagInteiro(nome=u'tMed', codigo=u'FR09', tamanho=[1, 4], raiz=u'//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.dhRetorno = TagDataHora(nome='dhRetorno', codigo='FR10', raiz='//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.xObs = TagCaracter(nome=u'xObs', codigo=u'FR11', tamanho=[1, 255], raiz=u'//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'consStatServCTe_v3.00.xsd'
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.dhRecbto.xml
        xml += self.tMed.xml
        xml += self.dhRetorno.xml
        xml += self.xObs.xml
        xml += u'</retConsStatServCte>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.cUF.xml       = arquivo
            self.dhRecbto.xml  = arquivo
            self.tMed.xml      = arquivo
            self.dhRetorno.xml = arquivo
            self.xObs.xml      = arquivo
            
    xml = property(get_xml, set_xml)
    