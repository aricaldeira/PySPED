# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
import os

from .cte_300 import CTe

DIRNAME = os.path.dirname(__file__)

class ConsReciCTe(XMLNFe):
    def __init__(self):
        super(ConsReciCTe, self).__init__()
        self.versao  = TagDecimal(nome='consReciCTe', codigo='BP02', propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.tpAmb   = TagInteiro(nome='tpAmb'      , codigo='BP03', tamanho=[1,   1, 1]  , raiz='//consReciCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nRec    = TagCaracter(nome='nRec'      , codigo='BP04', tamanho=[1, 15, 1]   , raiz='//consReciCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consReciCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.nRec.xml
        xml += '</consReciCTe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.nRec.xml   = arquivo

        return self.xml

    xml = property(get_xml, set_xml)



class InfProt(XMLNFe):
    def __init__(self):
        super(InfProt, self).__init__()
        self.Id        = TagCaracter(nome='infProt' , codigo='PR04', propriedade='Id'  , raiz='/'        , obrigatorio=False, namespace=NAMESPACE_CTE)
        self.tpAmb     = TagInteiro(nome='tpAmb'    , codigo='PR05', tamanho=[1,   1, 1], raiz='//infProt', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.verAplic  = TagCaracter(nome='verAplic', codigo='PR06', tamanho=[1,  20]   , raiz='//infProt', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.chCTe     = TagCaracter(nome='chCTe'   , codigo='PR07', tamanho=[44, 44]   , raiz='//infProt', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dhRecbto  = TagDataHora(nome='dhRecbto', codigo='PR08'                     , raiz='//infProt', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nProt     = TagCaracter(nome='nProt'   , codigo='PR09', tamanho=[15, 15]   , raiz='//infProt', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.digVal    = TagCaracter(nome='digVal'  , codigo='PR10', tamanho=[28, 28]   , raiz='//infProt', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cStat     = TagCaracter(nome='cStat'   , codigo='PR11' , tamanho=[1,   3]  , raiz='//infProt', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xMotivo   = TagCaracter(nome='xMotivo' , codigo='PR12' , tamanho=[1, 255]  , raiz='//infProt', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.valor:
            xml += self.Id.xml
        else:
            xml += '<infProt>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.chCTe.xml
        xml += self.dhRecbto.xml
        xml += self.nProt.xml
        xml += self.digVal.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += '</infProt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml        = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.chCTe.xml     = arquivo
            self.dhRecbto.xml  = arquivo
            self.nProt.xml     = arquivo
            self.digVal.xml    = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo

    xml = property(get_xml, set_xml)


class ProtCTe(XMLNFe):
    def __init__(self):
        super(ProtCTe, self).__init__()
        self.versao  = TagDecimal(nome='protCTe', codigo='PR02' , propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.infProt = InfProt()
        self.Signature = Signature()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.infProt.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != '#'):
            xml += self.Signature.xml

        xml += '</protCTe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            #
            # o grupo infProt é usado também no webservice de consulta da situação de uma CT-e
            # por isso, a raiz dele não pode ser assumida como sendo sempre o grupo
            # protCTe
            #
            self.infProt.xml = self._le_noh('//protCTe/infProt', ns=NAMESPACE_CTE)
            self.Signature.xml = self._le_noh('//protCTe/sig:Signature', ns=NAMESPACE_CTE)

    xml = property(get_xml, set_xml)

    def protocolo_formatado(self):
        if not self.infProt.nProt.valor:
            return ''

        formatado = self.infProt.nProt.valor
        formatado += ' - '
        formatado += self.infProt.dhRecbto.formato_danfe()
        return formatado


class RetConsReciCTe(XMLNFe):
    def __init__(self):
        super(RetConsReciCTe, self).__init__()
        self.versao   = TagDecimal(nome='retConsReciCTe', codigo='BR02' , propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'         , codigo='BR03' , tamanho=[1,   1, 1], raiz='//retConsReciCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.verAplic = TagCaracter(nome='verAplic'     , codigo='BR04' , tamanho=[1,  20]   , raiz='//retConsReciCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nRec     = TagCaracter(nome='nRec'         , codigo='BR04a', tamanho=[1, 15, 1] , raiz='//retConsReciCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cStat    = TagCaracter(nome='cStat'        , codigo='BR05' , tamanho=[1,   3]   , raiz='//retConsReciCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xMotivo  = TagCaracter(nome='xMotivo'      , codigo='BR06' , tamanho=[1, 255]   , raiz='//retConsReciCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cUF      = TagCaracter(nome='cUF'          , codigo='BR06a', tamanho=[2,   2, 2], raiz='//retConsReciCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.protCTe  = []

        #
        # Dicionário dos protocolos, com a chave sendo a chave de CT-e
        #
        self.dic_protCTe = {}
        #
        # Dicionário dos processos (CT-e + protocolo), com a chave sendo a chave da CT-e
        #
        self.dic_procCTe = {}

        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsReciCTe_v3.00.xsd'


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.nRec.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml

        for pn in self.protCTe:
            xml += pn.xml

        xml += '</retConsReciCTe>'
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
            self.protCTe      = self.le_grupo('//retConsReciCTe/protCTe', ProtCTe, sigla_ns='cte')

            #
            # Monta o dicionário dos protocolos
            #
            for pn in self.protCTe:
                self.dic_protCTe[pn.infProt.chCTe.valor] = pn

    xml = property(get_xml, set_xml)


class ProcCTe(XMLNFe):
    def __init__(self):
        super(ProcCTe, self).__init__()
        self.versao  = TagDecimal(nome='cteProc', propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.CTe     = CTe()
        self.protCTe = ProtCTe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.CTe.xml.replace(ABERTURA, '')
        xml += self.protCTe.xml.replace(ABERTURA, '')
        xml += '</cteProc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CTe.xml     = arquivo
            self.protCTe.xml = self._le_noh('//cteProc/protCTe', ns=NAMESPACE_CTE)

    xml = property(get_xml, set_xml)
