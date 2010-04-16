# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os
from nfe_110 import NFe


DIRNAME = os.path.dirname(__file__)


class ConsReciNFe(XMLNFe):
    def __init__(self):
        super(ConsReciNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'consReciNFe', codigo=u'BP02', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.10', raiz=u'/')
        self.tpAmb   = TagInteiro(nome=u'tpAmb'      , codigo=u'BP03', tamanho=[1,   1, 1]  , raiz=u'//consReciNFe')
        self.nRec    = TagCaracter(nome=u'nRec'      , codigo=u'BP04', tamanho=[1, 15, 1]   , raiz=u'//consReciNFe')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/') 
        self.arquivo_esquema = u'consReciNFe_v1.10.xsd'
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.nRec.xml
        xml += u'</consReciNFe>'
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
        self.Id        = TagCaracter(nome=u'infProt' , codigo=u'PR04', propriedade=u'Id'  , raiz=u'/'        , obrigatorio=False)
        self.tpAmb     = TagInteiro(nome=u'tpAmb'    , codigo=u'PR05', tamanho=[1,   1, 1], raiz=u'//infProt')
        self.verAplic  = TagCaracter(nome=u'verAplic', codigo=u'PR06', tamanho=[1,  20]   , raiz=u'//infProt')
        self.chNFe     = TagCaracter(nome=u'chNFe'   , codigo=u'PR07', tamanho=[44, 44]   , raiz=u'//infProt')
        self.dhRecbto  = TagDataHora(nome=u'dhRecbto', codigo=u'PR08'                     , raiz=u'//infProt')
        self.nProt     = TagCaracter(nome=u'nProt'   , codigo=u'PR09', tamanho=[15, 15]   , raiz=u'//infProt', obrigatorio=False)
        self.digVal    = TagCaracter(nome=u'digVal'  , codigo=u'PR10', tamanho=[28, 28]   , raiz=u'//infProt', obrigatorio=False)
        self.cStat     = TagCaracter(nome=u'cStat'   , codigo=u'PR11' , tamanho=[1,   3]  , raiz=u'//infProt')
        self.xMotivo   = TagCaracter(nome=u'xMotivo' , codigo=u'PR12' , tamanho=[1, 255]  , raiz=u'//infProt')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.valor:
            xml += self.Id.xml
        else:
            xml += u'<infProt>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.chNFe.xml
        xml += self.dhRecbto.xml
        xml += self.nProt.xml
        xml += self.digVal.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += u'</infProt>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml        = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.chNFe.xml     = arquivo
            self.dhRecbto.xml  = arquivo
            self.nProt.xml     = arquivo
            self.digVal.xml    = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
       
    xml = property(get_xml, set_xml)
    

class ProtNFe(XMLNFe):
    def __init__(self):
        super(ProtNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'protNFe', codigo=u'PR02' , propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.10', raiz=u'/')
        self.infProt = InfProt()
        self.Signature = Signature()
                
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.infProt.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != u'#'):
            xml += self.Signature.xml
        
        xml += u'</protNFe>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            #
            # o grupo infProt é usado também no webservice de consulta da situação de uma NF-e
            # por isso, a raiz dele não pode ser assumida como sendo sempre o grupo
            # protNFe
            #
            self.infProt.xml = self._le_noh(u'//protNFe/infProt')
            self.Signature.xml = self._le_noh(u'//protNFe/sig:Signature')
       
    xml = property(get_xml, set_xml)
    
    def protocolo_formatado(self):
        if not self.infProt.nProt.valor:
            return u''
            
        formatado = self.infProt.nProt.valor
        formatado += u' - ' 
        formatado += self.infProt.dhRecbto.formato_danfe()
        return formatado


class RetConsReciNFe(XMLNFe):
    def __init__(self):
        super(RetConsReciNFe, self).__init__()
        self.versao   = TagDecimal(nome=u'retConsReciNFe', codigo=u'BR02' , propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.10', raiz=u'/')
        self.tpAmb    = TagInteiro(nome=u'tpAmb'         , codigo=u'BR03' , tamanho=[1,   1, 1], raiz=u'//retConsReciNFe')
        self.verAplic = TagCaracter(nome=u'verAplic'     , codigo=u'BR04' , tamanho=[1,  20]   , raiz=u'//retConsReciNFe')
        self.nRec     = TagCaracter(nome=u'nRec'         , codigo=u'BR04a', tamanho=[1, 15, 1] , raiz=u'//retConsReciNFe')
        self.cStat    = TagCaracter(nome=u'cStat'        , codigo=u'BR05' , tamanho=[1,   3]   , raiz=u'//retConsReciNFe')
        self.xMotivo  = TagCaracter(nome=u'xMotivo'      , codigo=u'BR06' , tamanho=[1, 255]   , raiz=u'//retConsReciNFe')
        self.cUF      = TagCaracter(nome=u'cUF'          , codigo=u'BR06a', tamanho=[2,   2, 2], raiz=u'//retConsReciNFe')
        self.protNFe  = []
        
        #
        # Dicionário dos protocolos, com a chave sendo a chave de NF-e
        #
        self.dic_protNFe = {}
        #
        # Dicionário dos processos (NF-e + protocolo), com a chave sendo a chave da NF-e
        #
        self.dic_procNFe = {}
        
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/') 
        self.arquivo_esquema = u'retConsReciNFe_v1.10.xsd'
        

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.nRec.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        
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
            self.protNFe      = self.le_grupo('//retConsReciNFe/protNFe', ProtNFe)

            #
            # Monta o dicionário dos protocolos
            #
            for pn in self.protNFe:
                self.dic_protNFe[pn.infProt.chNFe.valor] = pn
       
    xml = property(get_xml, set_xml)


class ProcNFe(XMLNFe):
    def __init__(self):
        super(ProcNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'nfeProc', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.10', raiz=u'/')
        self.NFe     = NFe()
        self.protNFe = ProtNFe()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/') 
        self.arquivo_esquema = u'procNFe_v1.10.xsd'
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.NFe.xml.replace(ABERTURA, u'')
        xml += self.protNFe.xml.replace(ABERTURA, u'')
        xml += u'</nfeProc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.NFe.xml     = arquivo
            self.protNFe.xml = arquivo
        
    xml = property(get_xml, set_xml)
    