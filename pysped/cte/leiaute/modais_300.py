# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)

class EmiOcc(XMLNFe):
    def __init__(self):
        super(EmiOcc, self).__init__()
        self.CNPJ   = TagCaracter(nome='CNPJ', tamanho=[ 0, 14], raiz='//emiOcc', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.cInt   = TagCaracter(nome='cInt', tamanho=[ 1, 10], raiz='//emiOcc', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.IE     = TagCaracter(nome='IE', tamanho=[ 2, 14], raiz='//emiOcc', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.UF     = TagCaracter(nome='UF', tamanho=[ 2,  2]   , raiz='//emiOcc', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.fone   = TagInteiro(nome='fone', tamanho=[ 6, 14], raiz='//emiOcc', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<emiOcc>'
        xml += self.CNPJ.xml
        xml += self.cInt.xml
        xml += self.IE.xml
        xml += self.UF.xml
        xml += self.fone.xml
        xml += '</emiOcc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml   = arquivo
            self.cInt.xml   = arquivo
            self.IE.xml     = arquivo
            self.UF.xml     = arquivo
            self.fone.xml   = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class Occ(XMLNFe):
    def __init__(self):
        super(Occ, self).__init__()
        self.serie = TagCaracter(nome='serie' , tamanho=[ 8, 8, 8], raiz='//occ', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.nOcc  = TagInteiro(nome='nOcc' , tamanho=[ 1,  6], raiz='//occ', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dEmi  = TagData(nome='dEmi', raiz='//occ', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.emiOcc = EmiOcc()
        
    def get_xml(self):
        if not (self.nOcc.valor or self.dEmi.valor or self.emiOcc is not None):
            return ''
            
        xml = XMLNFe.get_xml(self)
        xml += u'<occ>'
        xml += self.serie.xml
        xml += self.nOcc.xml
        xml += self.dEmi.xml
        xml += self.emiOcc.xml
        xml += '</occ>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.serie.xml  = arquivo
            self.nOcc.xml   = arquivo
            self.dEmi.xml   = arquivo
            self.emiOcc.xml = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class Rodo(XMLNFe):
    def __init__(self):
        super(Rodo, self).__init__()
        self.RNTRC = TagCaracter(nome='RNTRC' , tamanho=[ 8, 8, 8], raiz='//rodo', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.occ = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<rodo>'
        xml += self.RNTRC.xml
        for o in self.occ:
            xml += o.xml
            
        xml += '</rodo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.RNTRC.xml = arquivo
            self.occ = self.le_grupo('//CTe/infCte/infCTeNorm/infModal/rodo/occ', Occ, sigla_ns='cte')
            
    xml = property(get_xml, set_xml)
    

class InfTotAP(XMLNFe):
    def __init__(self):
        super(InfTotAP, self).__init__()
        self.qTotProd = TagCaracter(nome='qTotProd' , tamanho=[ 1, 1, 1], raiz='//infTotAP', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.uniAP = TagCaracter(nome='uniAP' , tamanho=[ 1, 4], raiz='//infTotAP', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<infTotAP>'
        xml += self.qTotProd.xml
        xml += self.uniAP.xml
        xml += '</infTotAP>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.qTotProd.xml = arquivo
            self.uniAP.xml    = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class Peri(XMLNFe):
    def __init__(self):
        super(Peri, self).__init__()
        self.nONU = TagCaracter(nome='nONU' , tamanho=[ 4, 4, 4], raiz='//peri', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.qTotEmb = TagCaracter(nome='qTotEmb' , tamanho=[ 1, 20], raiz='//peri', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.infTotAP = InfTotAP()
        
    def get_xml(self):
        if not (self.nONU.valor or self.qTotEmb.valor or self.infTotAP is not None):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += u'<peri>'
        xml += self.nONU.xml
        xml += self.qTotEmb.xml
        xml += self.infTotAP.xml
        xml += '</peri>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nONU.xml      = arquivo
            self.qTotEmb.xml   = arquivo
            self.infTotAP.xml  = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class Tarifa(XMLNFe):
    def __init__(self):
        super(Tarifa, self).__init__()
        self.CL = TagCaracter(nome='CL' , tamanho=[ 1, 1, 1], raiz='//tarifa', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cTar = TagCaracter(nome='cTar' , tamanho=[ 1, 4], raiz='//tarifa', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.vTar = TagDecimal(nome='vTar', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//tarifa', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<tarifa>'
        xml += self.CL.xml
        xml += self.cTar.xml
        xml += self.vTar.xml
        xml += '</tarifa>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CL.xml     = arquivo
            self.cTar.xml   = arquivo
            self.vTar.xml   = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class TagCInfManu(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagCInfManu, self).__init__(*args, **kwargs)
        self.nome = 'cInfManu'
        self.tamanho = [2, 2]
        self.raiz = '//natCarga'
        
    
class NatCarga(XMLNFe):
    def __init__(self):
        super(NatCarga, self).__init__()
        self.xDime = TagCaracter(nome='xDime' , tamanho=[ 5, 14], raiz='//natCarga', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.cInfManu = []
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<natCarga>'
        xml += self.xDime.xml
        for c in self.cInfManu:
            xml += c.xml
            
        xml += '</natCarga>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xDime.xml = arquivo
            self.cInfManu = self.le_grupo('//CTe/infCte/infCTeNorm/infModal/aereo/natCarga/cInfManu', TagCInfManu, sigla_ns='cte')
            
    xml = property(get_xml, set_xml)
    
    
class Aereo(XMLNFe):
    def __init__(self):
        super(Aereo, self).__init__()
        self.nMinu = TagInteiro(nome='nMinu' , tamanho=[ 9, 9, 9], raiz='//aereo', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.nOCA = TagInteiro(nome='nOCA' , tamanho=[ 11, 11, 11], raiz='//aereo', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.dPrevAereo = TagData(nome='dPrevAereo' , raiz='//aereo', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.natCarga = NatCarga()
        self.tarifa   = Tarifa()
        self.peri     = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<aereo>'
        xml += self.nMinu.xml
        xml += self.nOCA.xml
        xml += self.dPrevAereo.xml
        xml += self.natCarga.xml
        xml += self.tarifa.xml
        for p in self.peri:
            xml += p.xml
            
        xml += '</aereo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nMinu.xml      = arquivo
            self.nOCA.xml       = arquivo
            self.dPrevAereo.xml = arquivo
            self.natCarga.xml   = arquivo
            self.tarifa.xml     = arquivo
            self.peri = self.le_grupo('//CTe/infCte/infCTeNorm/infModal/aereo/peri', Peri, sigla_ns='cte')
            
    xml = property(get_xml, set_xml)
    

class InfNFeAquav(XMLNFe):
    def __init__(self):
        super(InfNFeAquav, self).__init__()
        self.chave = TagCaracter(nome='chave', tamanho=[ 44, 44], raiz='//CTe/infCte/infCTeNorm/infModal/aquav/detCont/infDoc/infNFe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.unidRat = TagDecimal(nome='unidRat', tamanho=[1, 3, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/infCTeNorm/infModal/aquav/detCont/infDoc/infNFe', obrigatorio=False)
        
    def get_xml(self):
        if not (self.chave.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += u'<infNF>'
        xml += self.chave.xml            
        xml += self.unidRat.xml            
        xml += '</infNF>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chave.xml = arquivo
            self.unidRat.xml = arquivo
            
    xml = property(get_xml, set_xml)
    

class InfNFAquav(XMLNFe):
    def __init__(self):
        super(InfNFAquav, self).__init__()
        self.serie = TagCaracter(nome='serie', tamanho=[ 1, 3], raiz='//CTe/infCte/infCTeNorm/infModal/aquav/detCont/infDoc/infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nDoc = TagCaracter(nome='nDoc', tamanho=[ 1, 20], raiz='//CTe/infCte/infCTeNorm/infModal/aquav/detCont/infDoc/infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.unidRat = TagDecimal(nome='unidRat', tamanho=[1, 3, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/infCTeNorm/infModal/aquav/detCont/infDoc/infNF', obrigatorio=False)
        
    def get_xml(self):
        if not (self.serie.valor or self.nDoc.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += u'<infNF>'
        xml += self.serie.xml            
        xml += self.nDoc.xml            
        xml += self.unidRat.xml            
        xml += '</infNF>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.serie.xml = arquivo
            self.nDoc.xml = arquivo
            self.unidRat.xml = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class InfDocAquav(XMLNFe):
    def __init__(self):
        super(InfDocAquav, self).__init__()
        self.infNF  = []
        self.infNFe = []
        
    def get_xml(self):
        if (len(self.infNF)==0 and len(self.infNFe)==0):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += u'<infDoc>'
        for inf in self.infNF:
            xml += inf.xml
        for infe in self.infNFe:
            xml += infe.xml
        xml += '</infDoc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infNF = self.le_grupo('//CTe/infCte/infCTeNorm/infModal/aquav/detCont/infDoc/infNF', InfNFAquav, sigla_ns='cte')
            self.infNFe = self.le_grupo('//CTe/infCte/infCTeNorm/infModal/aquav/detCont/infDoc/infNFe', InfNFeAquav, sigla_ns='cte')
            
    xml = property(get_xml, set_xml)
    
    
class Lacre(XMLNFe):
    def __init__(self):
        super(Lacre, self).__init__()
        self.nLacre = TagCaracter(nome='nLacre' , tamanho=[ 1, 20], raiz='//lacre', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        
    def get_xml(self):
        if not (self.nLacre.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += u'<lacre>'
        xml += self.nLacre.xml            
        xml += '</lacre>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nLacre.xml = arquivo
            
    xml = property(get_xml, set_xml)

    
class DetCont(XMLNFe):
    def __init__(self):
        super(DetCont, self).__init__()
        self.nCont = TagCaracter(nome='xBalsa' , tamanho=[ 1, 20], raiz='//detCont', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.lacre = []
        ##Evitar conflito de nome com InfDoc
        self.infDoc = InfDocAquav()
        
    def get_xml(self):
        if not (self.nCont.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += u'<detCont>'
        xml += self.nCont.xml            
        for l in self.lacre:
            xml += l.xml
            
        xml += self.infDoc.xml            
        xml += '</detCont>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nCont.xml = arquivo
            self.infDoc.xml = arquivo
            self.lacre = self.le_grupo('//CTe/infCte/infCTeNorm/infModal/aquav/detCont/lacre', Lacre, sigla_ns='cte')
            
    xml = property(get_xml, set_xml)

    
class Balsa(XMLNFe):
    def __init__(self):
        super(Balsa, self).__init__()
        self.xBalsa = TagCaracter(nome='xBalsa' , tamanho=[ 1, 60], raiz='//balsa', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        
    def get_xml(self):
        if not (self.xBalsa.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += u'<balsa>'
        xml += self.xBalsa.xml            
        xml += '</balsa>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xBalsa.xml = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class Aquav(XMLNFe):
    def __init__(self):
        super(Aquav, self).__init__()
        self.vPrest = TagDecimal(nome='vPrest', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//aquav', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vAFRMM = TagDecimal(nome='vAFRMM', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//aquav', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xNavio = TagCaracter(nome='xNavio' , tamanho=[1, 60], raiz='//aquav', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.balsa   = []
        self.nViag  = TagInteiro(nome='nViag', tamanho=[1, 10], raiz='//aquav', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.direc  = TagCaracter(nome='direc', tamanho=[1, 1, 1], raiz='//aquav', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.irin  = TagCaracter(nome='irin', tamanho=[1, 10], raiz='//aquav', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.detCont = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<aquav>'
        xml += self.vPrest.xml
        xml += self.vAFRMM.xml
        xml += self.xNavio.xml
        for b in self.balsa:
            xml += b.xml
        for d in self.detCont:
            xml += d.xml
            
        xml += self.nViag.xml
        xml += self.direc.xml
        xml += self.irin.xml
        xml += '</aquav>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vPrest.xml  = arquivo
            self.vAFRMM.xml  = arquivo
            self.xNavio.xml  = arquivo
            self.nViag.xml   = arquivo
            self.direc.xml   = arquivo
            self.irin.xml    = arquivo
            self.balsa = self.le_grupo('//CTe/infCte/infCTeNorm/infModal/aquav/balsa', Balsa, sigla_ns='cte')
            self.detCont = self.le_grupo('//CTe/infCte/infCTeNorm/infModal/aquav/detCont', DetCont, sigla_ns='cte')
            
    xml = property(get_xml, set_xml)

    
class EnderFerro(XMLNFe):
    def __init__(self):
        super(EnderFerro, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , tamanho=[ 2, 255]  , raiz='//enderFerro', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nro     = TagCaracter(nome='nro'    , tamanho=[ 1, 60]   , raiz='//enderFerro', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.xCpl    = TagCaracter(nome='xCpl'   , tamanho=[ 1, 60]   , raiz='//enderFerro', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', tamanho=[ 2, 60]   , raiz='//enderFerro', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.cMun    = TagInteiro(nome='cMun'    , tamanho=[ 7,  7, 7], raiz='//enderFerro', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xMun    = TagCaracter(nome='xMun'   , tamanho=[ 2, 60]   , raiz='//enderFerro', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.CEP     = TagCaracter(nome='CEP'    , tamanho=[ 8,  8, 8], raiz='//enderFerro', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , tamanho=[ 2,  2]   , raiz='//enderFerro', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderFerro>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += '</enderFerro>'
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
            self.UF.xml      = arquivo
            
    xml = property(get_xml, set_xml)    


class FerroEnv(XMLNFe):
    def __init__(self):
        super(FerroEnv, self).__init__()
        self.CNPJ   = TagCaracter(nome='CNPJ', tamanho=[ 0, 14], raiz='//ferroEnv', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.cInt   = TagCaracter(nome='cInt', tamanho=[ 1, 10], raiz='//ferroEnv', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.IE     = TagCaracter(nome='IE', tamanho=[ 2, 14], raiz='//ferroEnv', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', tamanho=[ 2,  60]   , raiz='//ferroEnv', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.enderFerro   = EnderFerro()
        
    def get_xml(self):
        if not (self.CNPJ.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += u'<ferroEnv>'
        xml += self.CNPJ.xml            
        xml += self.cInt.xml            
        xml += self.IE.xml            
        xml += self.xNome.xml
        xml += self.enderFerro.xml
        xml += '</ferroEnv>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml   = arquivo
            self.cInt.xml   = arquivo
            self.IE.xml     = arquivo
            self.xNome.xml  = arquivo
            self.enderFerro.xml = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class TrafMut(XMLNFe):
    def __init__(self):
        super(TrafMut, self).__init__()
        self.respFat    = TagInteiro(nome='respFat' , tamanho=[ 1, 1, 1], raiz='//trafMut', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.ferrEmi    = TagInteiro(nome='ferrEmi' , tamanho=[ 1, 1, 1], raiz='//trafMut', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vFrete     = TagDecimal(nome='vFrete', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//trafMut', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.chCTeFerroOrigem = TagCaracter(nome='chCTeFerroOrigem' , tamanho=[ 44, 44], raiz='//trafMut', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.ferroEnv = []
        
    def get_xml(self):
        if not (self.respFat.valor or self.ferrEmi.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += u'<trafMut>'
        xml += self.respFat.xml            
        xml += self.ferrEmi.xml            
        xml += self.vFrete.xml            
        xml += self.chCTeFerroOrigem.xml
        for f in self.ferroEnv:
            xml += f.xml
            
        xml += '</trafMut>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.respFat.xml = arquivo
            self.ferrEmi.xml = arquivo
            self.vFrete.xml = arquivo
            self.chCTeFerroOrigem.xml = arquivo
            self.ferroEnv = self.le_grupo('//CTe/infCte/infCTeNorm/infModal/ferrov/trafMut/ferroEnv', FerroEnv, sigla_ns='cte')
            
    xml = property(get_xml, set_xml)    
    
    
class Ferrov(XMLNFe):
    def __init__(self):
        super(Ferrov, self).__init__()
        self.tpTraf = TagInteiro(nome='tpTraf', tamanho=[1, 1, 1], raiz='//ferrov', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.trafMut = TrafMut()
        self.fluxo = TagCaracter(nome='fluxo', tamanho=[ 1, 10], raiz='//ferrov', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<ferrov>'
        xml += self.tpTraf.xml
        xml += self.trafMut.xml
        xml += self.fluxo.xml
        xml += '</ferrov>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpTraf.xml  = arquivo
            self.trafMut.xml  = arquivo
            self.fluxo.xml  = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class Duto(XMLNFe):
    def __init__(self):
        super(Duto, self).__init__()
        self.vTar = TagDecimal(nome='vTar', tamanho=[1, 9, 1], decimais=[0, 6, 6], raiz='//duto', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.dIni = TagData(nome='dIni', raiz='//duto', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dFim = TagData(nome='dFim', raiz='//duto', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<duto>'
        xml += self.vTar.xml
        xml += self.dIni.xml
        xml += self.dFim.xml
        xml += '</duto>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vTar.xml = arquivo
            self.dIni.xml = arquivo
            self.dFim.xml = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class InfSeg(XMLNFe):
    def __init__(self):
        super(Seg, self).__init__()
        self.xSeg = TagCaracter(nome='xSeg', tamanho=[1, 30], raiz='//infSeg', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.CNPJ = TagCaracter(nome='CNPJ', tamanho=[ 0, 14], raiz='//infSeg', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<infSeg>'
        xml += self.xSeg.xml
        xml += self.CNPJ.xml
        xml += '</infSeg>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xSeg.xml = arquivo
            self.CNPJ.xml  = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class Seg(XMLNFe):
    def __init__(self):
        super(Seg, self).__init__()
        self.infSeg = InfSeg()
        self.nApol = TagCaracter(nome='nApol', tamanho=[1, 20], raiz='//seg', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nAver = TagCaracter(nome='nAver', tamanho=[1, 20], raiz='//seg', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.nApol.valor or self.infSeg is not None):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += u'<seg>'
        xml += self.infSeg.xml
        xml += self.nApol.xml
        xml += self.nAver.xml
        xml += '</seg>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infSeg.xml = arquivo
            self.nApol.xml  = arquivo
            self.nAver.xml  = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class Multimodal(XMLNFe):
    def __init__(self):
        super(Multimodal, self).__init__()
        self.COTM = TagCaracter(nome='COTM', tamanho=[1, 20], raiz='//multimodal', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.indNegociavel = TagInteiro(nome='indNegociavel', tamanho=[1, 1, 1], raiz='//multimodal', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.seg = Seg()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<multimodal>'
        xml += self.COTM.xml
        xml += self.indNegociavel.xml
        xml += self.seg.xml
        xml += '</multimodal>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.COTM.xml = arquivo
            self.indNegociavel.xml = arquivo
            self.seg.xml = arquivo
            
    xml = property(get_xml, set_xml)
    
