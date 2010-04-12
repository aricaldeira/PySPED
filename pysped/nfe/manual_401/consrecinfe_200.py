# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_401 import ESQUEMA_ATUAL
from pysped.nfe.manual_300 import consrecinfe_110
import os
from nfe_200 import NFe


DIRNAME = os.path.dirname(__file__)


class ConsReciNFe(consrecinfe_110.ConsReciNFe):
    def __init__(self):
        super(ConsReciNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'consReciNFe', codigo=u'BP02', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/') 
        self.arquivo_esquema = u'consReciNFe_v2.00.xsd'


class InfProt(consrecinfe_110.InfProt):
    def __init__(self):
        super(InfProt, self).__init__()
    

class ProtNFe(consrecinfe_110.ProtNFe):
    def __init__(self):
        super(ProtNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'protNFe', codigo=u'PR02' , propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
    

class RetConsReciNFe(consrecinfe_110.RetConsReciNFe):
    def __init__(self):
        super(RetConsReciNFe, self).__init__()
        self.versao   = TagDecimal(nome=u'retConsReciNFe', codigo=u'BR02' , propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.cMsg     = TagCaracter(nome=u'cMsg'         , codigo=u'BR06b', tamanho=[4,   4], raiz=u'//retConsReciNFe', obrigatorio=False)
        self.xMsg     = TagCaracter(nome=u'xMsg'         , codigo=u'BR06c', tamanho=[1, 200], raiz=u'//retConsReciNFe', obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/') 
        self.arquivo_esquema = u'retConsReciNFe_v2.00.xsd'
        

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.nRec.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.cMsg.xml
        xml += self.xMsg.xml
        
        for pn in self.protNFe:
            xml += pn.xml
            
        xml += u'</retConsReciNFe>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.tpAmb.xml    = arquivo
            self.verAplic.xml = arquivo
            self.nRec.xml     = arquivo
            self.cStat.xml    = arquivo
            self.xMotivo.xml  = arquivo
            self.cUF.xml      = arquivo
            self.cMsg.xml     = arquivo
            self.xMsg.xml     = arquivo
            self.protNFe      = self.le_grupo('//retConsReciNFe/protNFe', ProtNFe)

            #
            # Monta o dicionário dos protocolos
            #
            for pn in self.protNFe:
                self.dic_protNFe[pn.infProt.chNFe.valor] = pn
       
    xml = property(get_xml, set_xml)


class ProcNFe(consrecinfe_110.ProcNFe):
    def __init__(self):
        super(ProcNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'nfeProc', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.NFe     = NFe()
        self.protNFe = ProtNFe()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/') 
        self.arquivo_esquema = u'procNFe_v2.00.xsd'
    