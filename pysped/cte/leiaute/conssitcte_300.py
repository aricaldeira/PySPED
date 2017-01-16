# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
import os

from .consrecicte_300 import ProtCTe as ProtCTe_300
from .canccte_300 import RetCancCTe as RetCancCTe_300
from .proceventocte_300 import ProcEventoCTe as ProcEventoCTe_300

DIRNAME = os.path.dirname(__file__)

class ConsSitCTe(XMLNFe):
    def __init__(self):
        super(ConsSitCTe, self).__init__()
        self.versao = TagDecimal(nome='consSitCTe', codigo='EP01', propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.tpAmb  = TagInteiro(nome='tpAmb'     , codigo='EP03', tamanho=[ 1,  1, 1], raiz='//consSitCTe', valor=2, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xServ  = TagCaracter(nome='xServ'    , codigo='EP04', tamanho=[ 9,  9]   , raiz='//consSitCTe', valor='CONSULTAR', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.chCTe  = TagCaracter(nome='chCTe'    , codigo='EP05', tamanho=[44, 44]   , raiz='//consSitCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consSitCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.chCTe.xml
        xml += '</consSitCTe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml  = arquivo
            self.chCTe.xml  = arquivo

    xml = property(get_xml, set_xml)


class RetConsSitCTe(XMLNFe):
    def __init__(self):
        super(RetConsSitCTe, self).__init__()
        self.versao     = TagDecimal(nome='retConsSitCTe', codigo='ER01', propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.tpAmb      = TagInteiro(nome='tpAmb'        , codigo='ER03' , tamanho=[1,   1, 1], raiz='//retConsSitCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.verAplic   = TagCaracter(nome='verAplic'    , codigo='ER04' , tamanho=[1,  20]   , raiz='//retConsSitCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cStat      = TagCaracter(nome='cStat'       , codigo='ER05' , tamanho=[1,   3]   , raiz='//retConsSitCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xMotivo    = TagCaracter(nome='xMotivo'     , codigo='ER06' , tamanho=[1, 2000]  , raiz='//retConsSitCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cUF        = TagInteiro(nome='cUF'          , codigo='ER07' , tamanho=[2,   2, 2], raiz='//retConsSitCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.protCTe    = None
        self.retCancCTe = None
        self.procEventoCTe = []
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsSitCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml

        if self.protCTe is not None:
            xml += self.protCTe.xml

        if self.retCancCTe is not None:
            xml += tira_abertura(self.retCancCTe.xml)

        if not (len(self.procEventoCTe)):
            for procenv in self.procEventoCTe:
                xml += procenv.xml

        xml += '</retConsSitCTe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.cUF.xml       = arquivo

            if self._le_noh('//retConsSitCTe/protCTe', ns=NAMESPACE_CTE) is not None:
                self.protCTe = ProtCTe_300()
                self.protCTe.xml = arquivo

            if self._le_noh('//retConsSitCTe/retCancCTe', ns=NAMESPACE_CTE) is not None:
                self.retCancCTe = RetCancCTe_300()
                self.retCancCTe.xml = arquivo

            self.procEventoCTe = self.le_grupo('//retConsSitCTe/procEventoCTe', ProcEventoCTe_300, sigla_ns='cte')

    xml = property(get_xml, set_xml)
