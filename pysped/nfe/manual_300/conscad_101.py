# -*- coding: utf-8 -*-

from pysped.xml_sped import *
#from soap_100 import SOAPEnvio, SOAPRetorno, conectar_servico
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os


DIRNAME = os.path.dirname(__file__)


class _InfConsEnviado(XMLNFe):
    xServ = TagCaracter(nome=u'xServ', codigo=u'GP04', tamanho=[8, 8]  , raiz=u'//ConsCad', valor=u'CONS-CAD')
    UF    = TagCaracter(nome=u'UF'   , codigo=u'GP05', tamanho=[2, 2]  , raiz=u'//ConsCad')
    IE    = TagCaracter(nome=u'IE'   , codigo=u'GP06', tamanho=[2, 14] , raiz=u'//ConsCad', obrigatorio=False)
    CNPJ  = TagCaracter(nome=u'CNPJ'  , codigo=u'GP07', tamanho=[3, 14], raiz=u'//ConsCad', obrigatorio=False)
    CPF   = TagCaracter(nome=u'CPF'   , codigo=u'GP08', tamanho=[3, 11], raiz=u'//ConsCad', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<infCons>'
        xml += self.xServ.xml
        xml += self.UF.xml
        xml += self.IE.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += u'</infCons>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xServ.xml = arquivo
            self.UF.xml    = arquivo
            self.IE.xml    = arquivo
            self.CNPJ.xml  = arquivo
            self.CPF.xml   = arquivo

    xml = property(get_xml, set_xml)
    

class ConsCad(XMLNFe):
    versao = TagDecimal(nome=u'ConsCad', codigo=u'GP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.01', raiz=u'/')
    infCons = _InfConsEnviado()
    caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL)
    arquivo_esquema = u'consCad_v1.01.xsd'
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infCons.xml
        xml += u'</ConsCad>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.infCons.xml = arquivo

    xml = property(get_xml, set_xml)


class _Ender(XMLNFe):
    xLgr    = TagCaracter(nome=u'xLgr'   , codigo=u'GR23', tamanho=[1, 255] , raiz=u'//retConsCad/infCons/infCad/ender', obrigatorio=False)
    nro     = TagCaracter(nome=u'nro'    , codigo=u'GR24', tamanho=[1, 60]  , raiz=u'//retConsCad/infCons/infCad/ender', obrigatorio=False)
    xCpl    = TagCaracter(nome=u'xCpl'   , codigo=u'GR25', tamanho=[1, 60]  , raiz=u'//retConsCad/infCons/infCad/ender', obrigatorio=False)
    xBairro = TagCaracter(nome=u'xBairro', codigo=u'GR26', tamanho=[1, 60]  , raiz=u'//retConsCad/infCons/infCad/ender', obrigatorio=False)
    cMun    = TagInteiro(nome=u'cMun'    , codigo=u'GR27', tamanho=[7, 7]   , raiz=u'//retConsCad/infCons/infCad/ender', obrigatorio=False)
    xMun    = TagCaracter(nome=u'xMun'   , codigo=u'GR28', tamanho=[1, 60]  , raiz=u'//retConsCad/infCons/infCad/ender', obrigatorio=False)
    CEP     = TagInteiro(nome=u'CEP'     , codigo=u'GR29', tamanho=[7, 8]   , raiz=u'//retConsCad/infCons/infCad/ender', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        if self.xLgr.valor or self.nro.valor or self.xCpl.valor or self.xBairro.valor or self.cMun.valor or self.xMun.valor or self.CEP.valor:
            xml += u'<ender>'
            xml += self.xLgr.xml
            xml += self.nro.xml
            xml += self.xCpl.xml
            xml += self.xBairro.xml
            xml += self.cMun.xml
            xml += self.xMun.xml
            xml += self.CEP.xml
            xml += u'</ender>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.CEP.xml     = arquivo

    xml = property(get_xml, set_xml)


class _InfCadRecebido(XMLNFe):
    IE       = TagCaracter(nome=u'IE'      , codigo=u'GR08' , tamanho=[2, 14], raiz=u'//retConsCad/infCons/infCad')
    CNPJ     = TagCaracter(nome=u'CNPJ'    , codigo=u'GR09' , tamanho=[3, 14], raiz=u'//retConsCad/infCons/infCad')
    CPF      = TagCaracter(nome=u'CPF'     , codigo=u'GR10' , tamanho=[3, 11], raiz=u'//retConsCad/infCons/infCad')
    UF       = TagCaracter(nome=u'UF'      , codigo=u'GR11' , tamanho=[2, 2] , raiz=u'//retConsCad/infCons/infCad')
    cSit     = TagInteiro(nome=u'cSit'     , codigo=u'GR12' , tamanho=[1, 1] , raiz=u'//retConsCad/infCons/infCad')
    xNome    = TagCaracter(nome=u'xNome'   , codigo=u'GR13' , tamanho=[1, 60], raiz=u'//retConsCad/infCons/infCad', obrigatorio=False)
    xFant    = TagCaracter(nome=u'xFant'   , codigo=u'GR13a', tamanho=[1, 60], raiz=u'//retConsCad/infCons/infCad', obrigatorio=False)
    xRegApur = TagCaracter(nome=u'xRegApur', codigo=u'GR14' , tamanho=[1, 60], raiz=u'//retConsCad/infCons/infCad', obrigatorio=False)
    CNAE     = TagInteiro(nome=u'CNAE'     , codigo=u'GR15' , tamanho=[6, 7] , raiz=u'//retConsCad/infCons/infCad', obrigatorio=False)
    dIniAtiv = TagData(nome=u'dIniAtiv'    , codigo=u'GR16' ,                  raiz=u'//retConsCad/infCons/infCad', obrigatorio=False)
    dUltSit  = TagData(nome=u'dUltSit'     , codigo=u'GR17' ,                  raiz=u'//retConsCad/infCons/infCad', obrigatorio=False)
    dBaixa   = TagData(nome=u'dBaixa'      , codigo=u'GR18' ,                  raiz=u'//retConsCad/infCons/infCad', obrigatorio=False)
    IEUnica  = TagCaracter(nome=u'IEUnica' , codigo=u'GR20' , tamanho=[2, 14], raiz=u'//retConsCad/infCons/infCad', obrigatorio=False)
    IEAtual  = TagCaracter(nome=u'IEAtual' , codigo=u'GR21' , tamanho=[2, 14], raiz=u'//retConsCad/infCons/infCad', obrigatorio=False)
    ender    = _Ender()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<infCad>'
        xml += self.IE.xml      
        xml += self.CNPJ.xml    
        xml += self.CPF.xml     
        xml += self.UF.xml      
        xml += self.cSit.xml    
        xml += self.xNome.xml   
        xml += self.xFant.xml   
        xml += self.xRegApur.xml
        xml += self.CNAE.xml
        xml += self.dIniAtiv.xml
        xml += self.dUltSit.xml 
        xml += self.dBaixa.xml
        xml += self.IEUnica.xml 
        xml += self.IEAtual.xml
        xml += self.ender.xml
        xml += u'</infCad>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.IE.xml       = arquivo
            self.CNPJ.xml     = arquivo
            self.CPF.xml      = arquivo
            self.UF.xml       = arquivo
            self.cSit.xml     = arquivo
            self.xNome.xml    = arquivo
            self.xFant.xml    = arquivo
            self.xRegApur.xml = arquivo
            self.CNAE.xml     = arquivo
            self.dIniAtiv.xml = arquivo
            self.dUltSit.xml  = arquivo
            self.dBaixa.xml   = arquivo
            self.IEUnica.xml  = arquivo
            self.IEAtual.xml  = arquivo
            self.ender.xml    = arquivo

    xml = property(get_xml, set_xml)


class _InfConsRecebido(XMLNFe):
    verAplic = TagCaracter(nome=u'verAplic', codigo=u'GR04' , tamanho=[1, 20]  , raiz=u'//retConsCad/infCons')
    cStat    = TagInteiro(nome=u'cStat'    , codigo=u'GR05' , tamanho=[3, 3, 3], raiz=u'//retConsCad/infCons')
    xMotivo  = TagCaracter(nome=u'xMotivo' , codigo=u'GR06' , tamanho=[1, 255] , raiz=u'//retConsCad/infCons')
    UF       = TagCaracter(nome=u'UF'      , codigo=u'GR06a', tamanho=[2, 2]   , raiz=u'//retConsCad/infCons')
    IE       = TagCaracter(nome=u'IE'      , codigo=u'GR06b', tamanho=[2, 14]  , raiz=u'//retConsCad/infCons', obrigatorio=False)
    CNPJ     = TagCaracter(nome=u'CNPJ'    , codigo=u'GR06c', tamanho=[3, 14]  , raiz=u'//retConsCad/infCons', obrigatorio=False)
    CPF      = TagCaracter(nome=u'CPF'     , codigo=u'GR06d', tamanho=[3, 11]  , raiz=u'//retConsCad/infCons', obrigatorio=False)
    dhCons   = TagDataHora(nome=u'dhCons'  , codigo=u'GR06e',                    raiz=u'//retConsCad/infCons')
    cUF      = TagInteiro(nome=u'cUF'      , codigo=u'GR06f', tamanho=[2, 2, 2], raiz=u'//retConsCad/infCons')
    infCad   = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<infCons>'
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.UF.xml
        xml += self.IE.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.dhCons.xml
        xml += self.cUF.xml
        
        if len(self.infCad) > 0:
            for ic in self.infCad:
                xml += ic.xml
                
        xml += u'</infCons>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.UF.xml        = arquivo
            self.IE.xml        = arquivo
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.dhCons.xml    = arquivo
            self.cUF.xml       = arquivo
            
            self.infCad = []
            cadastros = self._le_nohs('//retConsCad/infCons/infCad')
            
            if len(cadastros) > 0:
                for c in cadastros:
                    nc = _InfCadRecebido()
                    nc.xml = c
                    self.infCad.append(nc)

    xml = property(get_xml, set_xml)


class RetConsCad(XMLNFe):
    versao = TagDecimal(nome=u'retConsCad', codigo=u'GR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.01', raiz=u'/')
    infCons = _InfConsRecebido()
    caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL)
    arquivo_esquema = u'retConsCad_v1.01.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infCons.xml
        xml += u'</retConsCad>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            self.infCons.xml = arquivo

    xml = property(get_xml, set_xml)
