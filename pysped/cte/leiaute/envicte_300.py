# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
import os

from .cte_300 import CTe

DIRNAME = os.path.dirname(__file__)

class EnviCTe(XMLNFe):
    def __init__(self):
        super(EnviCTe, self).__init__()
        self.versao = TagDecimal(nome='enviCTe', codigo='AP01', propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.idLote  = TagInteiro(nome='idLote' , codigo='AP03', tamanho=[1, 15, 1], raiz='//enviCTe')
        self.CTe  = []
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'enviCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.idLote.xml

        for n in self.CTe:
            xml += tira_abertura(n.xml)

        xml += '</enviCTe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.idLote.xml    = arquivo
            self.CTe = self.le_grupo('//enviLote/CTe', CTe)

    xml = property(get_xml, set_xml)


class InfRec(XMLNFe):
    def __init__(self):
        super(InfRec, self).__init__()
        self.nRec     = TagCaracter(nome='nRec'     , codigo='AR08', tamanho=[1, 15, 1], raiz='//retEnviCte/infRec', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dhRecbto = TagDataHora(nome='dhRecbto', codigo='AR09'                    , raiz='//retEnviCte/infRec', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.tMed     = TagInteiro(nome='tMed'     , codigo='AR10', tamanho=[1,  4, 1], raiz='//retEnviCte/infRec', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

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


class RetEnviCTe(XMLNFe):
    def __init__(self):
        super(RetEnviCTe, self).__init__()
        self.versao   = TagDecimal(nome='retEnviCte', codigo='AR02' , propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'     , codigo='AR03' , tamanho=[1,   1, 1], raiz='//retEnviCte')
        self.cUF      = TagCaracter(nome='cUF'      , codigo='AR03a', tamanho=[2,   2, 2], raiz='//retEnviCte')
        self.verAplic = TagCaracter(nome='verAplic' , codigo='AR04' , tamanho=[1,  20]   , raiz='//retEnviCte')
        self.cStat    = TagCaracter(nome='cStat'    , codigo='AR05' , tamanho=[1,   3]   , raiz='//retEnviCte')
        self.xMotivo  = TagCaracter(nome='xMotivo'  , codigo='AR06' , tamanho=[1, 255]   , raiz='//retEnviCte')
        self.infRec   = InfRec()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retEnviCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.infRec.xml
        xml += '</retEnviCte>'
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
