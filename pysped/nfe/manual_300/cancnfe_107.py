# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os


DIRNAME = os.path.dirname(__file__)


class InfCancEnviado(XMLNFe):
    def __init__(self):
        super(InfCancEnviado, self).__init__()
        self.Id    = TagCaracter(nome=u'infCanc', codigo=u'CP03', tamanho=[46, 46]    , raiz=u'//cancNFe', propriedade=u'Id')
        self.tpAmb = TagInteiro(nome=u'tpAmb'   , codigo=u'CP05', tamanho=[ 1,  1, 1] , raiz=u'//cancNFe/infCanc', valor=2)
        self.xServ = TagCaracter(nome=u'xServ'  , codigo=u'CP06', tamanho=[ 8,  8]    , raiz=u'//cancNFe/infCanc', valor=u'CANCELAR')
        self.chNFe = TagCaracter(nome=u'chNFe'   , codigo=u'CP07', tamanho=[44, 44, 44], raiz=u'//cancNFe/infCanc')
        self.nProt = TagCaracter(nome=u'nProt'   , codigo=u'CP08', tamanho=[15, 15, 15], raiz=u'//cancNFe/infCanc')
        self.xJust = TagCaracter(nome=u'xJust'  , codigo=u'CP09', tamanho=[15, 255]   , raiz=u'//cancNFe/infCanc')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        self.Id.valor = u'ID' + self.chNFe.valor

        xml += self.Id.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.chNFe.xml
        xml += self.nProt.xml
        xml += self.xJust.xml
        xml += u'</infCanc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml    = arquivo
            self.tpAmb.xml = arquivo
            self.xServ.xml = arquivo
            self.chNFe.xml = arquivo
            self.nProt.xml = arquivo
            self.xJust.xml = arquivo

    xml = property(get_xml, set_xml)


class CancNFe(XMLNFe):
    def __init__(self):
        super(CancNFe, self).__init__()
        self.versao    = TagDecimal(nome=u'cancNFe', codigo=u'CP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.07', raiz=u'/')
        self.infCanc   = InfCancEnviado()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'cancNFe_v1.07.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infCanc.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = u'#' + self.infCanc.Id.valor

        xml += self.Signature.xml
        xml += u'</cancNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infCanc.xml = arquivo
            self.Signature.xml = self._le_noh('//cancNFe/sig:Signature')

    xml = property(get_xml, set_xml)


class InfCancRecebido(XMLNFe):
    def __init__(self):
        super(InfCancRecebido, self).__init__()
        self.Id       = TagCaracter(nome=u'infCanc' , codigo=u'CR03' , tamanho=[17, 17]    , raiz=u'//retCancNFe', propriedade=u'Id', obrigatorio=False)
        self.tpAmb    = TagInteiro(nome=u'tpAmb'    , codigo=u'CR05' , tamanho=[1, 1, 1]   , raiz=u'//retCancNFe/infCanc', valor=2)
        self.verAplic = TagCaracter(nome=u'verAplic', codigo=u'CR06' , tamanho=[1, 20]     , raiz=u'//retCancNFe/infCanc')
        self.cStat    = TagCaracter(nome=u'cStat'    , codigo=u'CR07' , tamanho=[3, 3, 3]   , raiz=u'//retCancNFe/infCanc')
        self.xMotivo  = TagCaracter(nome=u'xMotivo' , codigo=u'CR08' , tamanho=[1, 255]    , raiz=u'//retCancNFe/infCanc')
        self.cUF      = TagInteiro(nome=u'cUF'      , codigo=u'CR08a', tamanho=[2, 2, 2]   , raiz=u'//retCancNFe/infCanc')
        self.chNFe    = TagCaracter(nome=u'chNFe'    , codigo=u'CR09' , tamanho=[44, 44, 44], raiz=u'//retcancNFe/infCanc', obrigatorio=False)
        self.dhRecbto = TagDataHora(nome=u'dhRecbto', codigo=u'CR10' ,                       raiz=u'//retCancNFe/infCanc', obrigatorio=False)
        self.nProt    = TagCaracter(nome=u'nProt'    , codigo=u'CR11' , tamanho=[15, 15, 15], raiz=u'//retCancNFe/infCanc', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.xml:
            xml += self.Id.xml
        else:
            xml += u'<infCanc>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.chNFe.xml
        xml += self.dhRecbto.xml
        xml += self.nProt.xml
        xml += u'</infCanc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml       = arquivo
            self.tpAmb.xml    = arquivo
            self.verAplic.xml = arquivo
            self.cStat.xml    = arquivo
            self.xMotivo.xml  = arquivo
            self.cUF.xml      = arquivo
            self.chNFe.xml    = arquivo
            self.dhRecbto.xml = arquivo
            self.nProt.xml    = arquivo

    xml = property(get_xml, set_xml)


class RetCancNFe(XMLNFe):
    def __init__(self):
        super(RetCancNFe, self).__init__()
        self.versao = TagDecimal(nome=u'retCancNFe', codigo=u'CR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.07', raiz=u'/')
        self.infCanc = InfCancRecebido()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retCancNFe_v1.07.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infCanc.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != u'#'):
            xml += self.Signature.xml

        xml += u'</retCancNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infCanc.xml   = arquivo
            self.Signature.xml = self._le_noh('//retCancNFe/sig:Signature')

    xml = property(get_xml, set_xml)

    def protocolo_formatado(self):
        if not self.infCanc.nProt.valor:
            return u''

        formatado = self.infCanc.nProt.valor
        formatado += u' - '
        formatado += self.infCanc.dhRecbto.formato_danfe()
        return formatado


class ProcCancNFe(XMLNFe):
    def __init__(self):
        super(ProcCancNFe, self).__init__()
        #
        # Atenção --- a tag procCancNFe tem que começar com letra minúscula, para
        # poder validar no XSD.
        #
        self.versao = TagDecimal(nome=u'procCancNFe', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.07', raiz=u'/')
        self.cancNFe = CancNFe()
        self.retCancNFe = RetCancNFe()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'procCancNFe_v1.07.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.cancNFe.xml.replace(ABERTURA, u'')
        xml += self.retCancNFe.xml.replace(ABERTURA, u'')
        xml += u'</procCancNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cancNFe.xml = arquivo
            self.retCancNFe.xml = arquivo

    xml = property(get_xml, set_xml)
