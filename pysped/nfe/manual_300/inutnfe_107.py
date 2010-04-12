# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os


DIRNAME = os.path.dirname(__file__)


class InfInutEnviado(XMLNFe):
    def __init__(self):
        super(InfInutEnviado, self).__init__()
        self.Id     = TagCaracter(nome=u'infInut', codigo=u'DP03', tamanho=[41, 41] , raiz=u'//inutNFe', propriedade=u'Id')
        self.tpAmb  = TagInteiro(nome=u'tpAmb'   , codigo=u'DP05', tamanho=[1, 1, 1], raiz=u'//inutNFe/infInut', valor=2)
        self.xServ  = TagCaracter(nome=u'xServ'  , codigo=u'DP06', tamanho=[10, 10] , raiz=u'//inutNFe/infInut', valor=u'INUTILIZAR')
        self.cUF    = TagInteiro(nome=u'cUF'     , codigo=u'DP07', tamanho=[2, 2, 2], raiz=u'//inutNFe/infInut')
        self.ano    = TagCaracter(nome=u'ano'    , codigo=u'DP08', tamanho=[2, 2]   , raiz=u'//inutNFe/infInut')
        self.CNPJ   = TagCaracter(nome=u'CNPJ'   , codigo=u'DP09', tamanho=[3, 14]  , raiz=u'//inutNFe/infInut')
        self.mod    = TagInteiro(nome=u'mod'     , codigo=u'DP10', tamanho=[2, 2, 2], raiz=u'//inutNFe/infInut', valor=55)
        self.serie  = TagInteiro(nome=u'serie'   , codigo=u'DP11', tamanho=[1, 3]   , raiz=u'//inutNFe/infInut')
        self.nNFIni = TagInteiro(nome=u'nNFIni'  , codigo=u'DP12', tamanho=[1, 9]   , raiz=u'//inutNFe/infInut')
        self.nNFFin = TagInteiro(nome=u'nNFFin'  , codigo=u'DP13', tamanho=[1, 9]   , raiz=u'//inutNFe/infInut')
        self.xJust  = TagCaracter(nome=u'xJust'  , codigo=u'DP14', tamanho=[15, 255], raiz=u'//inutNFe/infInut')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.cUF.xml
        xml += self.ano.xml
        xml += self.CNPJ.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNFIni.xml
        xml += self.nNFFin.xml
        xml += self.xJust.xml
        xml += u'</infInut>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml     = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml  = arquivo
            self.cUF.xml    = arquivo
            self.ano.xml    = arquivo
            self.CNPJ.xml   = arquivo
            self.mod.xml    = arquivo
            self.serie.xml  = arquivo
            self.nNFIni.xml = arquivo
            self.nNFFin.xml = arquivo
            self.xJust.xml  = arquivo
        
    xml = property(get_xml, set_xml)


class InutNFe(XMLNFe):
    def __init__(self):
        super(InutNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'inutNFe', codigo=u'DP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.07', raiz=u'/')
        self.infInut = InfInutEnviado()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'inutNFe_v1.07.xsd'
        
        self.chave = u''
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infInut.xml
        
        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = u'#' + self.infInut.Id.valor

        xml += self.Signature.xml
        xml += u'</inutNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infInut.xml   = arquivo
            self.Signature.xml = self._le_noh('//inutNFe/sig:Signature')

    xml = property(get_xml, set_xml)
    
    def monta_chave(self):
        chave = unicode(self.infInut.cUF.valor).zfill(2)
        chave += self.infInut.ano.valor.zfill(2)
        chave += self.infInut.CNPJ.valor.zfill(14)
        chave += unicode(self.infInut.mod.valor).zfill(2)
        chave += unicode(self.infInut.serie.valor).zfill(3)
        chave += unicode(self.infInut.nNFIni.valor).zfill(9)
        chave += unicode(self.infInut.nNFFin.valor).zfill(9)
        
        self.chave = chave
        return chave
        
    def gera_nova_chave(self):
        chave = self.monta_chave()
        
        #
        # Na versão 1.07 da NF-e a chave de inutilização não tem
        # o ano
        #
        chave = chave[0:2] + chave[4:]
        
        #
        # Define o Id
        #
        self.infInut.Id.valor = u'ID' + chave


class InfInutRecebido(XMLNFe):
    def __init__(self):
        super(InfInutRecebido, self).__init__()
        self.Id       = TagCaracter(nome=u'infInut' , codigo=u'DR03', tamanho=[17, 17]    , raiz=u'//retInutNFe', propriedade=u'Id', obrigatorio=False)
        self.tpAmb    = TagInteiro(nome=u'tpAmb'    , codigo=u'DR05', tamanho=[1, 1, 1]   , raiz=u'//retInutNFe/infInut', valor=2)
        self.verAplic = TagCaracter(nome=u'verAplic', codigo=u'DR06', tamanho=[1, 20]     , raiz=u'//retInutNFe/infInut')
        self.cStat    = TagCaracter(nome=u'cStat'   , codigo=u'DR07', tamanho=[3, 3, 3]   , raiz=u'//retInutNFe/infInut')
        self.xMotivo  = TagCaracter(nome=u'xMotivo' , codigo=u'DR08', tamanho=[1, 255]    , raiz=u'//retInutNFe/infInut')
        self.cUF      = TagInteiro(nome=u'cUF'      , codigo=u'DR09', tamanho=[2, 2, 2]   , raiz=u'//retInutNFe/infInut')
        self.ano      = TagCaracter(nome=u'ano'     , codigo=u'DR10', tamanho=[2, 2]      , raiz=u'//retInutNFe/infInut', obrigatorio=False)
        self.CNPJ     = TagCaracter(nome=u'CNPJ'    , codigo=u'DR11', tamanho=[3, 14]     , raiz=u'//retInutNFe/infInut', obrigatorio=False)
        self.mod      = TagInteiro(nome=u'mod'      , codigo=u'DR12', tamanho=[2, 2, 2]   , raiz=u'//retInutNFe/infInut', obrigatorio=False)
        self.serie    = TagInteiro(nome=u'serie'    , codigo=u'DR13', tamanho=[1, 3]      , raiz=u'//retInutNFe/infInut', obrigatorio=False)
        self.nNFIni   = TagInteiro(nome=u'nNFIni'   , codigo=u'DR14', tamanho=[1, 9]      , raiz=u'//retInutNFe/infInut', obrigatorio=False)
        self.nNFFin   = TagInteiro(nome=u'nNFFin'   , codigo=u'DR15', tamanho=[1, 9]      , raiz=u'//retInutNFe/infInut', obrigatorio=False)
        self.dhRecbto = TagDataHora(nome=u'dhRecbto', codigo=u'DR16',                       raiz=u'//retInutNFe/infInut', obrigatorio=False)
        self.nProt    = TagInteiro(nome=u'nProt'    , codigo=u'DR17', tamanho=[15, 15, 15], raiz=u'//retInutNFe/infInut', obrigatorio=False)
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.xml:
            xml += self.Id.xml
        else:
            xml += u'<infInut>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.ano.xml
        xml += self.CNPJ.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNFIni.xml
        xml += self.nNFFin.xml
        xml += self.dhRecbto.xml
        xml += self.nProt.xml
        xml += u'</infInut>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml       = arquivo
            self.tpAmb.xml    = arquivo
            self.verAplic.xml = arquivo
            self.cStat.xml    = arquivo
            self.xMotivo.xml  = arquivo
            self.cUF.xml      = arquivo
            self.ano.xml      = arquivo
            self.CNPJ.xml     = arquivo
            self.mod.xml      = arquivo
            self.serie.xml    = arquivo
            self.nNFIni.xml   = arquivo
            self.nNFFin.xml   = arquivo
            self.dhRecbto.xml = arquivo
            self.nProt.xml    = arquivo

    xml = property(get_xml, set_xml)

    
class RetInutNFe(XMLNFe):
    def __init__(self):
        super(RetInutNFe, self).__init__()
        self.versao = TagDecimal(nome=u'retInutNFe', codigo=u'DR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.07', raiz=u'/')
        self.infInut = InfInutRecebido()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retInutNFe_v1.07.xsd'
        
        self.chave = u''
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infInut.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != u'#'):
            xml += self.Signature.xml

        xml += u'</retInutNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infInut.xml   = arquivo
            self.Signature.xml = self._le_noh('//retInutNFe/sig:Signature')

    xml = property(get_xml, set_xml)

    def monta_chave(self):
        chave = unicode(self.infInut.cUF.valor).zfill(2)
        chave += self.infInut.ano.valor.zfill(2)
        chave += self.infInut.CNPJ.valor.zfill(14)
        chave += unicode(self.infInut.mod.valor).zfill(2)
        chave += unicode(self.infInut.serie.valor).zfill(3)
        chave += unicode(self.infInut.nNFIni.valor).zfill(9)
        chave += unicode(self.infInut.nNFFin.valor).zfill(9)
        
        self.chave = chave
        return chave


class ProcInutNFe(XMLNFe):
    def __init__(self):
        super(ProcInutNFe, self).__init__()
        #
        # Atenção --- a tag ProcInutNFe tem que começar com letra maiúscula, para
        # poder validar no XSD. Os outros arquivos proc, procCancNFe, e procNFe
        # começam com minúscula mesmo
        #
        self.versao = TagDecimal(nome=u'ProcInutNFe', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.07', raiz=u'/')
        self.inutNFe = InutNFe()
        self.retInutNFe = RetInutNFe()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'procInutNFe_v1.07.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.inutNFe.xml.replace(ABERTURA, u'')
        xml += self.retInutNFe.xml.replace(ABERTURA, u'')
        xml += u'</ProcInutNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.inutNFe.xml    = arquivo
            self.retInutNFe.xml = arquivo

    xml = property(get_xml, set_xml)
