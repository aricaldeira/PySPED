# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os


DIRNAME = os.path.dirname(__file__)


class ConsStatServ(XMLNFe):
    def __init__(self):
        super(ConsStatServ, self).__init__()
        self.versao = TagDecimal(nome=u'consStatServ', codigo=u'FP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.07', raiz=u'/')
        self.tpAmb  = TagInteiro(nome=u'tpAmb'       , codigo=u'FP03', tamanho=[1, 1, 1], raiz=u'//consStatServ', valor=2)
        self.cUF    = TagInteiro(nome=u'cUF'         , codigo=u'FP04', tamanho=[2, 2, 2], raiz=u'//consStatServ', valor=35)
        self.xServ  = TagCaracter(nome=u'xServ'      , codigo=u'FP05', tamanho=[6, 6]   , raiz=u'//consStatServ', valor=u'STATUS')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'consStatServ_v1.07.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.cUF.xml
        xml += self.xServ.xml
        xml += u'</consStatServ>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.cUF.xml    = arquivo
            self.xServ.xml  = arquivo

    xml = property(get_xml, set_xml)
    

class RetConsStatServ(XMLNFe):
    def __init__(self):
        super(RetConsStatServ, self).__init__()
        self.versao    = TagDecimal(nome=u'retConsStatServ', codigo=u'FR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.07', raiz=u'/')
        self.tpAmb     = TagInteiro(nome=u'tpAmb'          , codigo=u'FR03', tamanho=[1, 1, 1], raiz=u'//retConsStatServ', valor=2)
        self.verAplic  = TagCaracter(nome=u'verAplic'      , codigo=u'FR04', tamanho=[1, 20]  , raiz=u'//retConsStatServ')
        self.cStat     = TagCaracter(nome=u'cStat'         , codigo=u'FR05', tamanho=[3, 3, 3], raiz=u'//retConsStatServ')
        self.xMotivo   = TagCaracter(nome=u'xMotivo'       , codigo=u'FR06', tamanho=[1, 255] , raiz=u'//retConsStatServ')
        self.cUF       = TagInteiro(nome=u'cUF'            , codigo=u'FR07', tamanho=[2, 2, 2], raiz=u'//retConsStatServ')
        self.dhRecbto  = TagDataHora(nome=u'dhRecbto'      , codigo=u'FR08',                    raiz=u'//retConsStatServ')
        self.tMed      = TagInteiro(nome=u'tMed'           , codigo=u'FR09', tamanho=[1, 4]   , raiz=u'//retConsStatServ', obrigatorio=False)
        self.dhRetorno = TagDataHora(nome=u'dhRetorno'     , codigo=u'FR10',                    raiz=u'//retConsStatServ', obrigatorio=False)
        self.xObs      = TagCaracter(nome=u'xObs'          , codigo=u'FR11', tamanho=[1, 255] , raiz=u'//retConsStatServ', obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retConsStatServ_v1.07.xsd'

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
        xml += u'</retConsStatServ>'
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
