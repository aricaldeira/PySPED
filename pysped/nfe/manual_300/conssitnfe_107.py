# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os


DIRNAME = os.path.dirname(__file__)


class ConsSitNFe(XMLNFe):
    def __init__(self):
        super(ConsSitNFe, self).__init__()
        self.versao = TagDecimal(nome=u'consSitNFe', codigo=u'EP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.07', raiz=u'/')
        self.tpAmb  = TagInteiro(nome=u'tpAmb'     , codigo=u'EP03', tamanho=[ 1,  1, 1], raiz=u'//consSitNFe', valor=2)
        self.xServ  = TagCaracter(nome=u'xServ'    , codigo=u'EP04', tamanho=[ 9,  9]   , raiz=u'//consSitNFe', valor=u'CONSULTAR')
        self.chNFe  = TagCaracter(nome=u'chNFe'    , codigo=u'EP05', tamanho=[44, 44]   , raiz=u'//consSitNFe') 
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'consSitNFe_v1.07.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.chNFe.xml
        xml += u'</consSitNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml  = arquivo
            self.chNFe.xml  = arquivo

    xml = property(get_xml, set_xml)


class InfProt(XMLNFe):
    '''Atenção!!!
    
    Este grupo infProt é DIFERENTE do infProt do retorno do recibo do lote
    
    Colocar esse infProt dentro do arquivo procNFe vai fazer com que o procNFe gerado
    seja INVALIDADO pelo XSD!!!

    Para transportar os valores desta infProt para a infProt do procNFe, é preciso usar
    
    procNFe.protNFe.infProt.xml = este_infProt.xml
    
    '''
    def __init__(self):
        super(InfProt, self).__init__()
        self.Id        = TagCaracter(nome=u'infProt' , codigo=u'ER04' , propriedade=u'Id'  , raiz=u'/'        , obrigatorio=False)
        self.tpAmb     = TagInteiro(nome=u'tpAmb'    , codigo=u'ER05' , tamanho=[1,   1, 1], raiz=u'//infProt')
        self.verAplic  = TagCaracter(nome=u'verAplic', codigo=u'ER06' , tamanho=[1,  20]   , raiz=u'//infProt')
        self.cStat     = TagCaracter(nome=u'cStat'   , codigo=u'ER07' , tamanho=[1,   3]   , raiz=u'//infProt')
        self.xMotivo   = TagCaracter(nome=u'xMotivo' , codigo=u'ER08' , tamanho=[1, 255]   , raiz=u'//infProt')
        self.cUF       = TagInteiro(nome=u'cUF'      , codigo=u'ER08a', tamanho=[2,   2, 2], raiz=u'//infProt')
        self.chNFe     = TagCaracter(nome=u'chNFe'   , codigo=u'ER09' , tamanho=[44, 44]   , raiz=u'//infProt', obrigatorio=False)
        self.dhRecbto  = TagDataHora(nome=u'dhRecbto', codigo=u'ER10'                      , raiz=u'//infProt', obrigatorio=False)
        self.nProt     = TagCaracter(nome=u'nProt'   , codigo=u'ER11' , tamanho=[15, 15]   , raiz=u'//infProt', obrigatorio=False)
        self.digVal    = TagCaracter(nome=u'digVal'  , codigo=u'ER12' , tamanho=[28, 28]   , raiz=u'//infProt', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.valor:
            xml += self.Id.xml
        else:
            xml += u'<infProt>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.chNFe.xml
        xml += self.dhRecbto.xml
        xml += self.nProt.xml
        xml += self.digVal.xml
        xml += u'</infProt>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml        = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.cUF.xml       = arquivo
            self.chNFe.xml     = arquivo
            self.dhRecbto.xml  = arquivo
            self.nProt.xml     = arquivo
            self.digVal.xml    = arquivo
       
    xml = property(get_xml, set_xml)
    

class RetConsSitNFe(XMLNFe):
    def __init__(self):
        super(RetConsSitNFe, self).__init__()
        self.versao    = TagDecimal(nome=u'retConsSitNFe', codigo=u'ER01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.07', raiz=u'/')
        self.infProt   = InfProt()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retConsSitNFe_v1.07.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infProt.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != u'#'):
            xml += self.Signature.xml
        
        xml += u'</retConsSitNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            #
            # o grupo infProt é usado também no webservice de consulta do recibo de lote de NF-e
            # por isso, a raiz dele não pode ser assumida como sendo sempre o grupo
            # retConsSitNFe
            #
            self.infProt.xml   = self._le_noh(u'//retConsSitNFe/infProt')
            self.Signature.xml = self._le_noh(u'//retConsSitNFe/sig:Signature')

    xml = property(get_xml, set_xml)
