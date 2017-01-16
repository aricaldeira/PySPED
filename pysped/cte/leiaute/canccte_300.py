# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


class InfCancRecebido(XMLNFe):
    def __init__(self):
        super(InfCancRecebido, self).__init__()
        self.Id       = TagCaracter(nome='infCanc' , codigo='CR03' , tamanho=[17, 17]    , raiz='//retCancCTe', namespace=NAMESPACE_CTE, propriedade='Id', obrigatorio=False)
        self.tpAmb    = TagInteiro(nome='tpAmb'    , codigo='CR05' , tamanho=[1, 1, 1]   , raiz='//retCancCTe/infCanc', namespace=NAMESPACE_CTE, valor=2)
        self.verAplic = TagCaracter(nome='verAplic', codigo='CR06' , tamanho=[1, 20]     , raiz='//retCancCTe/infCanc', namespace=NAMESPACE_CTE)
        self.cStat    = TagCaracter(nome='cStat'    , codigo='CR07' , tamanho=[3, 3, 3]   , raiz='//retCancCTe/infCanc', namespace=NAMESPACE_CTE)
        self.xMotivo  = TagCaracter(nome='xMotivo' , codigo='CR08' , tamanho=[1, 255]    , raiz='//retCancCTe/infCanc', namespace=NAMESPACE_CTE)
        self.cUF      = TagInteiro(nome='cUF'      , codigo='CR08a', tamanho=[2, 2, 2]   , raiz='//retCancCTe/infCanc', namespace=NAMESPACE_CTE)
        self.chCTe    = TagCaracter(nome='chCTe'    , codigo='CR09' , tamanho=[44, 44, 44], raiz='//retcancCTe/infCanc', namespace=NAMESPACE_CTE, obrigatorio=False)
        self.dhRecbto = TagDataHora(nome='dhRecbto', codigo='CR10' ,                       raiz='//retCancCTe/infCanc', namespace=NAMESPACE_CTE, obrigatorio=False)
        self.nProt    = TagCaracter(nome='nProt'    , codigo='CR11' , tamanho=[15, 15, 15], raiz='//retCancCTe/infCanc', namespace=NAMESPACE_CTE, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.xml:
            xml += self.Id.xml
        else:
            xml += '<infCanc>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.chCTe.xml
        xml += self.dhRecbto.xml
        xml += self.nProt.xml
        xml += '</infCanc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml       = arquivo
            self.tpAmb.xml    = arquivo
            self.verAplic.xml = arquivo
            self.cStat.xml    = arquivo
            self.xMotivo.xml  = arquivo
            self.cUF.xml      = arquivo
            self.chCTe.xml    = arquivo
            self.dhRecbto.xml = arquivo
            self.nProt.xml    = arquivo

    xml = property(get_xml, set_xml)


class RetCancCTe(XMLNFe):
    def __init__(self):
        super(RetCancCTe, self).__init__()
        self.versao = TagDecimal(nome='retCancCTe', codigo='CR01', propriedade='versao', namespace=NAMESPACE_CTE, valor='1.04', raiz='/')
        self.infCanc = InfCancRecebido()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', 'PL_CTe_104c/')
        self.arquivo_esquema = 'retCancCTe_v1.04.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infCanc.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != '#'):
            xml += self.Signature.xml

        xml += '</retCancCTe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infCanc.xml   = arquivo
            self.Signature.xml = self._le_noh('//retCancCTe/sig:Signature')

    xml = property(get_xml, set_xml)

    def protocolo_formatado(self):
        if not self.infCanc.nProt.valor:
            return ''

        formatado = self.infCanc.nProt.valor
        formatado += ' - '
        formatado += self.infCanc.dhRecbto.formato_danfe()
        return formatado
