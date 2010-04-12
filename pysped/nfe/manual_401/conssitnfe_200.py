# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_401 import ESQUEMA_ATUAL
from pysped.nfe.manual_300 import conssitnfe_107
import os


DIRNAME = os.path.dirname(__file__)


class ConsSitNFe(conssitnfe_107.ConsSitNFe):
    def __init__(self):
        super(ConsSitNFe, self).__init__()
        self.versao = TagDecimal(nome=u'consSitNFe', codigo=u'EP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'consSitNFe_v2.00.xsd'
   

class RetConsSitNFe(conssitnfe_107.RetConsSitNFe):
    def __init__(self):
        super(RetConsSitNFe, self).__init__()
        self.versao     = TagDecimal(nome=u'retConsSitNFe', codigo=u'ER01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.tpAmb      = TagInteiro(nome=u'tpAmb'        , codigo=u'ER03' , tamanho=[1,   1, 1], raiz=u'//retConsSitNFe')
        self.verAplic   = TagCaracter(nome=u'verAplic'    , codigo=u'ER04' , tamanho=[1,  20]   , raiz=u'//retConsSitNFe')
        self.cStat      = TagCaracter(nome=u'cStat'       , codigo=u'ER05' , tamanho=[1,   3]   , raiz=u'//retConsSitNFe')
        self.xMotivo    = TagCaracter(nome=u'xMotivo'     , codigo=u'ER06' , tamanho=[1, 255]   , raiz=u'//retConsSitNFe')
        self.cUF        = TagInteiro(nome=u'cUF'          , codigo=u'ER07' , tamanho=[2,   2, 2], raiz=u'//retConsSitNFe')
        self.chNFe      = TagCaracter(nome=u'chNFe'       , codigo=u'ER07a', tamanho=[44,  44]  , raiz=u'//retConsSitNFe', obrigatorio=False)
        self.protNFe    = None
        self.retCancNFe = None
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retConsSitNFe_v2.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.chNFe.xml
       
        xml += u'</retConsSitNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.cUF.xml       = arquivo
            self.chNFe.xml     = arquivo

    xml = property(get_xml, set_xml)
 
