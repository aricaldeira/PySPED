# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
from .modais_300 import Multimodal, Duto, Ferrov, Aquav, Aereo, Rodo
import os

DIRNAME = os.path.dirname(__file__)


class AutXML(XMLNFe):
    def __init__(self):
        super(AutXML, self).__init__()
        self.CNPJ       = TagCaracter(nome='CNPJ' , tamanho=[ 0, 14], raiz='//autXML', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.CPF        = TagCaracter(nome='CPF'  , tamanho=[11, 11], raiz='//autXML', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<autXML>'
        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml
        xml += '</autXML>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml = arquivo
            self.CPF.xml = arquivo

    xml = property(get_xml, set_xml)


class InfCTeAnu(XMLNFe):
    def __init__(self):
        super(InfCTeAnu, self).__init__()
        self.chCte = TagCaracter(nome='chCte', tamanho=[ 44, 44], raiz='//infCTeAnu', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dEmi  = TagData(nome='dEmi', raiz='//infCTeAnu', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.chCte.valor or self.dEmi.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += '<infCteAnu>'
        xml += self.chCte.xml
        xml += self.dEmi.xml
        xml += '</infCteAnu>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chCte.xml = arquivo
            self.dEmi.xml = arquivo

    xml = property(get_xml, set_xml)


class InfCTeComp(XMLNFe):
    def __init__(self):
        super(InfCTeComp, self).__init__()
        self.chCTe = TagCaracter(nome='chCTe', tamanho=[ 44, 44], raiz='//infCteComp', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.chCTe.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += '<infCteComp>'
        xml += self.chCTe.xml
        xml += '</infCteComp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chCTe.xml = arquivo

    xml = property(get_xml, set_xml)


class InfCTeMultimodal(XMLNFe):
    def __init__(self):
        super(InfCTeMultimodal, self).__init__()
        self.chCTeMultimodal = TagCaracter(nome='chCTeMultimodal', tamanho=[ 44, 44], raiz='//infCTeMultimodal', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCTeMultimodal>'
        xml += self.chCTeMultimodal.xml
        xml += '</infCTeMultimodal>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chCTeMultimodal.xml = arquivo

    xml = property(get_xml, set_xml)


class InfServVinc(XMLNFe):
    def __init__(self):
        super(InfServVinc, self).__init__()
        self.infCTeMultimodal = []

    def get_xml(self):
        if not (len(self.infCTeMultimodal)):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += '<infServVinc>'
        for i in self.infCTeMultimodal:
            xml += i.xml
        xml += '</infServVinc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infCTeMultimodal = self.le_grupo('//CTe/infCte/infCTeNorm/infServVinc/infCTeMultimodal', InfCTeMultimodal, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class InfGlobalizado(XMLNFe):
    def __init__(self):
        super(InfGlobalizado, self).__init__()
        self.xObs = TagCaracter(nome='xObs' , tamanho=[ 15, 256], raiz='//infGlobalizado', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.xObs.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += '<infGlobalizado>'
        xml += self.xObs.xml
        xml += '</infGlobalizado>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xObs.xml = arquivo

    xml = property(get_xml, set_xml)


class RefNF(XMLNFe):
    def __init__(self):
        super(RefNF, self).__init__()
        self.CNPJ       = TagCaracter(nome='CNPJ' , tamanho=[ 0, 14], raiz='//refNF', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.CPF        = TagCaracter(nome='CPF'  , tamanho=[11, 11], raiz='//refNF', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.mod        = TagCaracter(nome='mod'  , tamanho=[ 2,  2, 2], raiz='//refNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.serie      = TagCaracter(nome='serie' , tamanho=[ 1, 3, 1], raiz='//refNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.subserie   = TagCaracter(nome='subserie', tamanho=[1, 3], raiz='//refNF', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nro        = TagCaracter(nome='nro', tamanho=[ 1, 6]   , raiz='//refNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.valor      = TagDecimal(nome='valor', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//refNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dEmi       = TagData(nome='dEmi', raiz='//refNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''
        xml = XMLNFe.get_xml(self)
        xml += '<refNF>'
        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.subserie.xml
        xml += self.nro.xml
        xml += self.valor.xml
        xml += self.dEmi.xml
        xml += '</refNF>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.mod.xml       = arquivo
            self.serie.xml     = arquivo
            self.subserie.xml  = arquivo
            self.nro.xml       = arquivo
            self.valor.xml     = arquivo
            self.dEmi.xml      = arquivo

    xml = property(get_xml, set_xml)


class TomaICMS(XMLNFe):
    def __init__(self):
        super(TomaICMS, self).__init__()
        self.refNFe  = TagCaracter(nome='refNFe', tamanho=[44, 44], raiz='//tomaICMS', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.refNF = RefNF()
        self.refCte = TagCaracter(nome='refCte', tamanho=[44, 44], raiz='//tomaICMS', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        if not (self.refNFe.valor and self.refNF.xml and self.refCte.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += '<tomaICMS>'
        xml += self.refNFe.xml
        xml += self.refNF.xml
        xml += self.refCte.xml

        xml += '</tomaICMS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.refNFe.xml  = arquivo
            self.refNF.xml = arquivo
            self.refCte.xml  = arquivo

    xml = property(get_xml, set_xml)


class InfCTeSub(XMLNFe):
    def __init__(self):
        super(InfCTeSub, self).__init__()
        self.chCte  = TagCaracter(nome='chCte', tamanho=[44, 44], raiz='//infCteSub', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.refCteAnu = TagCaracter(nome='refCteAnu', tamanho=[44, 44], raiz='//infCteSub', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.tomaICMS  = TomaICMS()
        #self.indAlteraToma = TagInteiro(nome='indAlteraToma', tamanho=[0, 1], raiz='//infCteSub', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        if not (self.chCte.valor) or not (self.refCteAnu.valor and self.tomaICMS.xml):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += '<infCteSub>'
        xml += self.chCte.xml
        xml += self.refCteAnu.xml
        xml += self.tomaICMS.xml
        #xml += self.indAlteraToma.xml
        xml += '</infCteSub>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chCte.xml  = arquivo
            self.refCteAnu.xml = arquivo
            self.tomaICMS.xml  = arquivo
            #self.indAlteraToma.xml = arquivo

    xml = property(get_xml, set_xml)


class Dup(XMLNFe):
    def __init__(self):
        super(Dup, self).__init__()
        self.nDup  = TagCaracter(nome='nDup', tamanho=[1, 60], raiz='//dup', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dVenc = TagData(nome='dVenc', raiz='//dup', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vDup  = TagDecimal(nome='vDup', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//dup', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.nDup.valor or self.dVenc.valor or self.vDup.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<dup>'
        xml += self.nDup.xml
        xml += self.dVenc.xml
        xml += self.vDup.xml
        xml += '</dup>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nDup.xml  = arquivo
            self.dVenc.xml = arquivo
            self.vDup.xml  = arquivo

    xml = property(get_xml, set_xml)


class Fat(XMLNFe):
    def __init__(self):
        super(Fat, self).__init__()
        self.nFat  = TagCaracter(nome='nFat', tamanho=[1, 60], raiz='//CTe/infCte/infCTeNorm/cobr/fat', obrigatorio=False)
        self.vOrig = TagDecimal(nome='vOrig', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/infCTeNorm/cobr/fat', obrigatorio=False)
        self.vDesc = TagDecimal(nome='vDesc', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/infCTeNorm/cobr/fat', obrigatorio=False)
        self.vLiq  = TagDecimal(nome='vLiq' , tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/infCTeNorm/cobr/fat', obrigatorio=False)

    def get_xml(self):
        if not (self.nFat.valor or self.vOrig.valor or self.vDesc.valor or self.vLiq.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<fat>'
        xml += self.nFat.xml
        xml += self.vOrig.xml
        xml += self.vDesc.xml
        xml += self.vLiq.xml
        xml += '</fat>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nFat.xml  = arquivo
            self.vOrig.xml = arquivo
            self.vDesc.xml = arquivo
            self.vLiq.xml  = arquivo

    xml = property(get_xml, set_xml)


class Cobr(XMLNFe):
    def __init__(self):
        super(Cobr, self).__init__()
        self.fat = Fat()
        self.dup = []

    def get_xml(self):
        if not (self.fat.xml or len(self.dup)):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += '<cobr>'
        xml += self.fat.xml
        for d in self.dup:
            xml += d.xml

        xml += '</cobr>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.fat.xml  = arquivo
            self.dup = self.le_grupo('//CTe/infCte/infCTeNorm/cobr/dup', Dup, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class VeicNovos(XMLNFe):
    def __init__(self):
        super(VeicNovos, self).__init__()
        self.chassi  = TagCaracter(nome='chassi', tamanho=[17, 17, 17], raiz='//veicNovos', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cCor = TagCaracter(nome='cCor', tamanho=[1, 4]   , raiz='//veicNovos', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xCor = TagCaracter(nome='xCor', tamanho=[1, 40]   , raiz='//veicNovos', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cMod = TagCaracter(nome='cMod', tamanho=[1, 6]   , raiz='//veicNovos', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vUnit = TagDecimal(nome='vUnit', tamanho=[1 , 13, 1], decimais=[0, 2, 2], raiz='//veicNovos', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vFrete = TagDecimal(nome='vFrete', tamanho=[1 , 13, 1], decimais=[0, 2, 2], raiz='//veicNovos', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.chassi.valor or self.cCor.valor or self.xCor.valor or self.cMod.valor or self.vUnit.valor or self.vFrete.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += '<veicNovos>'
        xml += self.chassi.xml
        xml += self.cCor.xml
        xml += self.xCor.xml
        xml += self.cMod.xml
        xml += self.vUnit.xml
        xml += self.vFrete.xml
        xml += '</veicNovos>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chassi.xml = arquivo
            self.cCor.xml   = arquivo
            self.xCor.xml   = arquivo
            self.cMod.xml   = arquivo
            self.vUnit.xml  = arquivo
            self.vFrete.xml = arquivo

    xml = property(get_xml, set_xml)


class InfModal(XMLNFe):
    def __init__(self):
        super(InfModal, self).__init__()
        self.versaoModal  = TagDecimal(nome='infModal', propriedade='versaoModal', raiz='/', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, valor='3.00')
        self.modal = None

    def get_xml(self):
        if not self.modal:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += u'<infModal versaoModal="' + unicode(self.versaoModal.valor) + '">'
        xml += self.modal.xml
        xml += '</infModal>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versaoModal.xml   = arquivo
            if ('<rodo>' in arquivo and '</rodo>' in arquivo):
                self.modal = Rodo()
                self.modal.xml = arquivo
            elif ('<aereo>' in arquivo and '</aereo>' in arquivo):
                self.modal = Aereo()
                self.modal.xml = arquivo
            elif ('<aquav>' in arquivo and '</aquav>' in arquivo):
                self.modal = Aquav()
                self.modal.xml = arquivo
            elif ('<ferrov>' in arquivo and '</ferrov>' in arquivo):
                self.modal = Ferrov()
                self.modal.xml = arquivo
            elif ('<duto>' in arquivo and '</duto>' in arquivo):
                self.modal = Duto()
                self.modal.xml = arquivo


    xml = property(get_xml, set_xml)


class IdDocAntEle(XMLNFe):
    def __init__(self):
        super(IdDocAntEle, self).__init__()
        self.chCTe = TagCaracter(nome='chCTe', tamanho=[44, 44], raiz='//idDocAntEle', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not self.chCTe.valor:
            return ''
        xml = XMLNFe.get_xml(self)
        xml += '<idDocAntEle>'
        xml += self.chCTe.xml
        xml += '</idDocAntEle>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chCTe.xml  = arquivo

    xml = property(get_xml, set_xml)


class IdDocAntPap(XMLNFe):
    def __init__(self):
        super(IdDocAntPap, self).__init__()
        self.tpDoc = TagInteiro(nome='tpDoc', tamanho=[2, 2, 2]   , raiz='//idDocAntPap', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.serie = TagCaracter(nome='serie' , tamanho=[ 1,  3], raiz='//idDocAntPap', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.subser = TagCaracter(nome='subser' , tamanho=[ 1, 2], raiz='//idDocAntPap', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.nDoc = TagCaracter(nome='nDoc', tamanho=[1, 30]   , raiz='//idDocAntPap', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dEmi = TagData(nome='dEmi', raiz='//idDocAntPap', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.toDoc.valor or self.serie.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<idDocAntPap>'
        xml += self.tpDoc.xml
        xml += self.serie.xml
        xml += self.subser.xml
        xml += self.nDoc.xml
        xml += self.dEmi.xml
        xml += '</idDocAntPap>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpDoc.xml  = arquivo
            self.serie.xml  = arquivo
            self.subser.xml = arquivo
            self.nDoc.xml   = arquivo
            self.dEmi.xml   = arquivo

    xml = property(get_xml, set_xml)


class IdDocAnt(XMLNFe):
    def __init__(self):
        super(IdDocAnt, self).__init__()
        self.idDocAntPap = []
        self.idDocAntEle = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idDocAnt>'
        for ipap in self.idDocAntPap:
            xml += ipap.xml
        for iele in self.idDocAntEle:
            xml += iele.xml

        xml += '</idDocAnt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.idDocAntPap = self.le_grupo('//CTe/infCte/infCTeNorm/docAnt/emitDocAnt/idDocAnt/idDocAntPap', IdDocAntPap, sigla_ns='cte')
            self.idDocAntEle = self.le_grupo('//CTe/infCte/infCTeNorm/docAnt/emitDocAnt/idDocAnt/idDocAntEle', IdDocAntEle, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class EmitDocAnt(XMLNFe):
    def __init__(self):
        super(EmitDocAnt, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , tamanho=[ 0, 14], raiz='//emitDocAnt', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , tamanho=[11, 11], raiz='//emitDocAnt', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , tamanho=[ 2, 14], raiz='//emitDocAnt', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.UF        = TagCaracter(nome='UF'   , tamanho=[ 2,  2], raiz='//emitDocAnt')
        self.xNome     = TagCaracter(nome='xNome', tamanho=[ 2, 60], raiz='//emitDocAnt')
        self.idDocAnt  = []

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<emitDocAnt>'
        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.IE.xml
        xml += self.UF.xml
        xml += self.xNome.xml
        for iant in self.idDocAnt:
            xml += iant.xml

        xml += '</emitDocAnt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CPF.xml  = arquivo
            self.CNPJ.xml  = arquivo
            self.IE.xml  = arquivo
            self.UF.xml  = arquivo
            self.xNome.xml  = arquivo
            self.idDocAnt = self.le_grupo('//CTe/infCte/infCTeNorm/docAnt/emitDocAnt/idDocAnt', IdDocAnt, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class DocAnt(XMLNFe):
    def __init__(self):
        super(DocAnt, self).__init__()
        self.emitDocAnt   = []

    def get_xml(self):
        if not (len(self.emitDocAnt)):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<docAnt>'
        for e in self.emitDocAnt:
            xml += e.xml
        xml += '</docAnt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.emitDocAnt  = self.le_grupo('//CTe/infCte/infCTeNorm/docAnt/emitDocAnt', EmitDocAnt, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class InfOutros(XMLNFe):
    def __init__(self):
        super(InfOutros, self).__init__()
        self.tpDoc  = TagInteiro(nome='tpDoc', tamanho=[2, 2, 2], raiz='//infOutros', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.descOutros = TagCaracter(nome='descOutros', tamanho=[ 1, 100], raiz='//infOutros', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.nDoc  = TagCaracter(nome='nDoc', tamanho=[2, 2, 2], raiz='//infOutros', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dEmi  = TagData(nome='dEmi', raiz='//infOutros', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vDocFisc  = TagDecimal(nome='vDocFisc', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infOutros', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dPrev  = TagData(nome='dPrev', raiz='//infOutros', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.infUnidCarga  = []
        self.infUnidTransp = []

    def get_xml(self):
        if not (self.tpDoc.valor or self.descOutros.valor or self.nDoc.valor or self.dEmi.valor or self.vDocFisc.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infOutros>'
        xml += self.tpDoc.xml
        xml += self.descOutros.xml
        xml += self.nDoc.xml
        xml += self.dEmi.xml
        xml += self.vDocFisc.xml
        xml += self.dPred.xml

        for c in self.infUnidCarga:
            xml += c.xml
        for t in self.infUnidTransp:
            xml += t.xml

        xml += '</infOutros>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpDoc.xml   = arquivo
            self.descOutros.xml     = arquivo
            self.nDoc.xml     = arquivo
            self.dEmi.xml     = arquivo
            self.vDocFisc.xml     = arquivo
            self.dPred.xml   = arquivo
            self.infUnidCarga  = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infOutros/infUnidCarga', InfUnidCarga, sigla_ns='cte')
            self.infUnidTransp = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infOutros/infUnidTransp', InfUnidTransp, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class InfNFe(XMLNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.chave  = TagCaracter(nome='chave', codigo='B16', tamanho=[44, 44]   , raiz='//infNFe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.PIN    = TagInteiro(nome='PIN'   , codigo='B20', tamanho=[ 2, 9]    , raiz='//infNFe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.dPrev  = TagData(nome='dPrev', raiz='//infNFe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.infUnidCarga  = []
        self.infUnidTransp = []

    def get_xml(self):
        if not self.chave.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infNFe>'
        xml += self.chave.xml
        xml += self.PIN.xml
        xml += self.dPred.xml
        for c in self.infUnidCarga:
            xml += c.xml
        for t in self.infUnidTransp:
            xml += t.xml

        xml += '</infNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chave.xml   = arquivo
            self.PIN.xml     = arquivo
            self.dPred.xml   = arquivo
            self.infUnidCarga  = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infNFe/infUnidCarga', InfUnidCarga, sigla_ns='cte')
            self.infUnidTransp = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infNFe/infUnidTransp', InfUnidTransp, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class LacUnidTransp(XMLNFe):
    def __init__(self):
        super(LacUnidTransp, self).__init__()
        self.nLacre   = TagInteiro(nome='nLacre', tamanho=[ 1, 20], raiz='//lacUnidTransp', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.nLacre.valor):
            return ''
        xml = XMLNFe.get_xml(self)
        xml += '<lacUnidTransp>'
        xml += self.nLacre.xml
        xml += '</lacUnidTransp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nLacre.xml  = arquivo

    xml = property(get_xml, set_xml)


class InfUnidTransp(XMLNFe):
    def __init__(self):
        super(InfUnidTransp, self).__init__()
        self.tpUnidTransp   = TagInteiro(nome='tpUnidTransp',   tamanho=[ 1, 1, 1]   , raiz='//infUnidTransp', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.idUnidTransp   = TagCaracter(nome='idUnidTransp' , tamanho=[ 1, 20]   , raiz='//infUnidTransp', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.lacUnidTransp  = []
        self.infUnidCarga   = []
        self.qtdRat        = TagDecimal(nome='qtdRat', tamanho=[1, 3, 1], decimais=[0, 2, 2], raiz='//infUnidTransp', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        if not (self.tpUnidTransp.valor or self.idUnidTransp.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infUnidTransp>'
        xml += self.tpUnidTransp.xml
        xml += self.idUnidTransp.xml

        for l in self.lacUnidTransp:
            xml += l.xml

        for i in self.infUnidCarga:
            xml += i.xml

        xml += self.qtdRat.xml
        xml += '</infUnidTransp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpUnidTransp.xml = arquivo
            self.idUnidTransp.xml = arquivo
            self.qtdRat.xml      = arquivo
            self.infUnidCarga = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infNF/infUnidTransp/infUnidCarga', InfUnidCarga, sigla_ns='cte')
            self.lacUnidTransp = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infNF/infUnidTransp/lacUnidTransp', LacUnidTransp, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class LacUnidCarga(XMLNFe):
    def __init__(self):
        super(LacUnidCarga, self).__init__()
        self.nLacre   = TagInteiro(nome='nLacre', tamanho=[ 1, 20], raiz='//lacUnidCarga', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.nLacre.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<lacUnidCarga>'
        xml += self.nLacre.xml
        xml += '</lacUnidCarga>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nLacre.xml  = arquivo

    xml = property(get_xml, set_xml)


class InfUnidCarga(XMLNFe):
    def __init__(self):
        super(InfUnidCarga, self).__init__()
        self.tpUnidCarga   = TagInteiro(nome='tpUnidCarga',   tamanho=[ 1, 1, 1]   , raiz='//infUnidCarga', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.idUnidCarga   = TagCaracter(nome='idUnidCarga' , tamanho=[ 1, 20]   , raiz='//infUnidCarga', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.lacUnidCarga  = []
        self.qtdRat        = TagDecimal(nome='qtdRat', tamanho=[1, 3, 1], decimais=[0, 2, 2], raiz='//infUnidCarga', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        if not (self.tpUnidCarga.valor or self.idUnidCarga.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infUnidCarga>'
        xml += self.tpUnidCarga.xml
        xml += self.idUnidCarga.xml

        for l in self.lacUnidCarga:
            xml += l.xml

        xml += self.qtdRat.xml
        xml += '</infUnidCarga>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpUnidCarga.xml = arquivo
            self.idUnidCarga.xml = arquivo
            self.qtdRat.xml      = arquivo
            self.lacUnidCarga = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infNF/infUnidCarga/lacUnidCarga', LacUnidCarga, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class InfNF(XMLNFe):
    def __init__(self):
        super(InfNF, self).__init__()
        self.nRoma  = TagCaracter(nome='nRoma', codigo='B16', tamanho=[ 1, 20], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.nPed   = TagCaracter(nome='nPed' , codigo='B16', tamanho=[ 1, 20], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.mod    = TagCaracter(nome='mod'  , codigo='B18', tamanho=[ 2,  2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.serie  = TagCaracter(nome='serie' , codigo='B19', tamanho=[ 1,  3, 1], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nDoc   = TagInteiro(nome='nDoc'  , codigo='B20', tamanho=[ 1, 20], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dEmi   = TagData(nome='dEmi'     , codigo='B09', raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vBC    = TagDecimal(nome='vBC'   , codigo='W03', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vICMS  = TagDecimal(nome='vICMS' , codigo='W04', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vBCST  = TagDecimal(nome='vBCST' , codigo='W05', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vST    = TagDecimal(nome='vST'   , codigo='W06', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vProd  = TagDecimal(nome='vProd' , codigo='W07', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vNF    = TagDecimal(nome='vNF'   , codigo='W16', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nCFOP  = TagInteiro(nome='nCFOP' , codigo='I08', tamanho=[4,  4, 4]                    , raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nPeso  = TagDecimal(nome='nPeso' , codigo='W16', tamanho=[1, 12, 1], decimais=[0, 3, 3], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.PIN    = TagInteiro(nome='PIN'   , codigo='B20', tamanho=[ 2, 9]    , raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        #self.locRet = LocRet()
        self.dPrev  = TagData(nome='dPrev', raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.infUnidCarga = []
        self.infUnidTransp = []

    def get_xml(self):
        if not self.mod.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infNF>'
        xml += self.nRoma.xml
        xml += self.nPed.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nDoc.xml
        xml += self.dEmi.xml
        xml += self.vBC.xml
        xml += self.vICMS.xml
        xml += self.vBCST.xml
        xml += self.vST.xml
        xml += self.vProd.xml
        xml += self.vNF.xml
        xml += self.nCFOP.xml
        xml += self.nPeso.xml
        xml += self.PIN.xml
        #xml += self.locRet.xml
        xml += self.dPrev.xml

        for c in self.infUnidCarga:
            xml += c.xml
        for t in self.infUnidTransp:
            xml += t.xml

        xml += '</infNF>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nRoma.xml   = arquivo
            self.nPed.xml    = arquivo
            self.mod.xml     = arquivo
            self.serie.xml   = arquivo
            self.nDoc.xml    = arquivo
            self.dEmi.xml    = arquivo
            self.vBC.xml     = arquivo
            self.vICMS.xml   = arquivo
            self.vBCST.xml   = arquivo
            self.vST.xml     = arquivo
            self.vProd.xml   = arquivo
            self.vNF.xml     = arquivo
            self.nCFOP.xml   = arquivo
            self.nPeso.xml   = arquivo
            self.PIN.xml     = arquivo
            #self.locRet.xml  = arquivo
            self.dPrev.xml   = arquivo
            self.infUnidCarga  = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infNF/infUnidCarga', InfUnidCarga, sigla_ns='cte')
            self.infUnidTransp = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infNF/infUnidTransp', InfUnidTransp, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class InfDoc(XMLNFe):
    def __init__(self):
        super(InfDoc, self).__init__()
        self.infNF      = []
        self.infNFe     = []
        self.infOutros  = []

    def get_xml(self):
        if not (len(self.infNF) or len(self.infNFe) or len(self.infOutros)):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infDoc>'
        for inf in self.infNF:
            xml += inf.xml
        for infe in self.infNFe:
            xml += infe.xml
        for o in self.infOutros:
            xml += o.xml

        xml += '</infDoc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infNF = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infNF', InfNF, sigla_ns='cte')
            self.infNFe = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infNFe', InfNFe, sigla_ns='cte')
            self.infOutros = self.le_grupo('//CTe/infCte/infCTeNorm/infDoc/infOutros', InfOutros, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class InfQ(XMLNFe):
    def __init__(self):
        super(InfQ, self).__init__()
        self.cUnid  = TagCaracter(nome='cUnid', tamanho=[2, 2, 2] , raiz='//infQ', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.tpMed  = TagCaracter(nome='tpMed', tamanho=[1, 20]   , raiz='//infQ', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.qCarga = TagDecimal(nome='qCarga', tamanho=[1, 11, 1], decimais=[0, 4, 4], raiz='//infQ', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infQ>'
        xml += self.cUnid.xml
        xml += self.tpMed.xml
        xml += self.qCarga.xml
        xml += '</infQ>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUnid.xml  = arquivo
            self.tpMed.xml = arquivo
            self.qCarga.xml = arquivo

    xml = property(get_xml, set_xml)


class InfCarga(XMLNFe):
    def __init__(self):
        super(InfCarga, self).__init__()
        self.vCarga  = TagDecimal(nome='vCarga'  , tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/infCTeNorm/infCarga', obrigatorio=False)
        self.proPred = TagCaracter(nome='proPred', tamanho=[1, 60]   , raiz='//CTe/infCte/infCTeNorm/infCarga')
        self.xOutCat = TagCaracter(nome='xOutCat', tamanho=[1, 30]   , raiz='//CTe/infCte/infCTeNorm/infCarga', obrigatorio=False)
        self.infQ    = []
        self.vCargaAverb = TagDecimal(nome='vCargaAverb', tamanho=[1 , 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/infCTeNorm/infCarga', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCarga>'
        xml += self.vCarga.xml
        xml += self.proPred.xml
        xml += self.xOutCat.xml
        for i in self.infQ:
            xml += i.xml

        xml += self.vCargaAverb.xml
        xml += '</infCarga>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vCarga.xml  = arquivo
            self.proPred.xml = arquivo
            self.xOutCat.xml = arquivo
            self.vCargaAverb.xml = arquivo
            self.infQ = self.le_grupo('//CTe/infCte/infCTeNorm/infCarga/infQ', InfQ, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class InfCTeNorm(XMLNFe):
    def __init__(self):
        super(InfCTeNorm, self).__init__()
        self.infCarga = InfCarga()
        self.infDoc   = InfDoc()
        self.docAnt = DocAnt()
        self.infModal = InfModal()
        self.veicNovos = []
        self.cobr = Cobr()
        self.infCteSub = InfCTeSub()
        self.infGlobalizado = InfGlobalizado()
        self.infServVinc = InfServVinc()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCTeNorm>'
        xml += self.infCarga.xml
        xml += self.infDoc.xml
        xml += self.docAnt.xml
        xml += self.infModal.xml
        for v in self.veicNovos:
            xml += v.xml
        xml += self.cobr.xml
        xml += self.infCteSub.xml
        xml += self.infGlobalizado.xml
        xml += self.infServVinc.xml

        xml += '</infCTeNorm>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infCarga.xml = arquivo
            self.infDoc.xml   = arquivo
            self.docAnt.xml   = arquivo
            self.infModal.xml = arquivo
            self.cobr.xml     = arquivo
            self.infCteSub.xml = arquivo
            self.infGlobalizado.xml = arquivo
            self.infServVinc.xml = arquivo
            self.veicNovos = self.le_grupo('//CTe/infCte/infCTeNorm/veicNovos', VeicNovos, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class ICMSUFFim(XMLNFe):
    def __init__(self):
        super(ICMSUFFim, self).__init__()
        self.vBCUFFim       = TagDecimal(nome='vBCUFFim', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/imp/ICMSUFFim')
        self.pFCPUFFim      = TagDecimal(nome='pFCPUFFim', tamanho=[1, 5, 1],  decimais=[0, 2, 2], raiz='//CTe/infCte/imp/ICMSUFFim')
        self.pICMSUFFim     = TagDecimal(nome='pICMSUFFim', tamanho=[1, 5, 1],  decimais=[0, 2, 2], raiz='//CTe/infCte/imp/ICMSUFFim')
        self.pICMSInter     = TagDecimal(nome='pICMSInter', tamanho=[1, 5, 1],  decimais=[0, 2, 2], raiz='//CTe/infCte/imp/ICMSUFFim')
        self.pICMSInterPart = TagDecimal(nome='pICMSInterPart', tamanho=[1, 5, 1],  decimais=[0, 2, 2], raiz='//CTe/infCte/imp/ICMSUFFim')
        self.vFCPUFFim      = TagDecimal(nome='vFCPUFFim', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/imp/ICMSUFFim')
        self.vICMSUFFim     = TagDecimal(nome='vICMSUFFim', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/imp/ICMSUFFim')
        self.vICMSUFIni     = TagDecimal(nome='vICMSUFIni', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/imp/ICMSUFFim')

    def get_xml(self):
        if not (self.vBCUFFim.valor or self.pFCPUFFim.valor or self.pICMSUFFim.valor or self.pICMSInter.valor or self.pICMSInterPart.valor or self.vFCPUFFim.valor or
                self.vICMSUFFim.valor or self.vICMSUFIni.valor):
                return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ICMSUFFim>'
        xml += self.vBCUFFim.xml
        xml += self.pFCPUFFim.xml
        xml += self.pICMSUFFim.xml
        xml += self.pICMSInter.xml
        xml += self.pICMSInterPart.xml
        xml += self.vFCPUFFim.xml
        xml += self.vICMSUFFim.xml
        xml += self.vICMSUFIni.xml
        xml += '</ICMSUFFim>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBCUFFim.xml       = arquivo
            self.pFCPUFFim.xml      = arquivo
            self.pICMSUFFim.xml     = arquivo
            self.pICMSInter.xml     = arquivo
            self.pICMSInterPart.xml = arquivo
            self.vFCPUFFim.xml      = arquivo
            self.vICMSUFFim.xml     = arquivo
            self.vICMSUFIni.xml     = arquivo

    xml = property(get_xml, set_xml)


class TagCSTICMS(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagCSTICMS, self).__init__(*args, **kwargs)
        self.nome = 'CST'
        self.codigo = 'N12'
        self.tamanho = [2, 2]
        self.raiz = ''
        self.grupo_icms = None

    def set_valor(self, novo_valor):
        super(TagCSTICMS, self).set_valor(novo_valor)

        if not self.grupo_icms:
            return None
        #
        # Definimos todas as tags como não obrigatórias
        #
        #self.grupo_icms.modBC.obrigatorio    = False
        self.grupo_icms.pRedBC.obrigatorio   = False
        self.grupo_icms.vBC.obrigatorio      = False
        self.grupo_icms.pICMS.obrigatorio    = False
        self.grupo_icms.vICMS.obrigatorio    = False
        #self.grupo_icms.modBCST.obrigatorio  = False
        #self.grupo_icms.pMVAST.obrigatorio   = False
        #self.grupo_icms.pRedBCST.obrigatorio = False
        self.grupo_icms.vBCSTRet.obrigatorio    = False
        self.grupo_icms.pICMSSTRet.obrigatorio  = False
        self.grupo_icms.vICMSSTRet.obrigatorio  = False
        self.grupo_icms.vCred.obrigatorio  = False

        self.grupo_icms.vBCOutraUF.obrigatorio      = False
        self.grupo_icms.pICMSOutraUF.obrigatorio    = False
        self.grupo_icms.vICMSOutraUF.obrigatorio    = False

        self.grupo_icms.indSN.obrigatorio   = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo ICMS ao redefinirmos o código da situação
        # tributária
        #
        #self.grupo_icms.modBC.valor    = 3
        self.grupo_icms.pRedBC.valor   = '0.00'
        self.grupo_icms.vBC.valor      = '0.00'
        self.grupo_icms.pICMS.valor    = '0.00'
        self.grupo_icms.vICMS.valor    = '0.00'
        #self.grupo_icms.modBCST.valor  = 4
        #self.grupo_icms.pMVAST.valor   = '0.00'
        #self.grupo_icms.pRedBCST.valor = '0.00'
        self.grupo_icms.vBCSTRet.valor    = '0.00'
        self.grupo_icms.pICMSSTRet.valor  = '0.00'
        self.grupo_icms.vICMSSTRet.valor  = '0.00'

        self.grupo_icms.vBCOutraUF.valor      = '0.00'
        self.grupo_icms.pICMSOutraUF.valor    = '0.00'
        self.grupo_icms.vICMSOutraUF.valor    = '0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de ICMS
        #
        if self.valor == '00':
            self.grupo_icms.nome_tag = 'ICMS00'
            self.grupo_icms.nome_tag_txt = 'N02'
            self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS00'
            #self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True

        elif self.valor == '20':
            self.grupo_icms.nome_tag = 'ICMS20'
            self.grupo_icms.nome_tag_txt = 'N04'
            self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS20'
            #self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.pRedBC.obrigatorio   = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True

        elif self.valor in ('40', '41', '51'):
            self.grupo_icms.nome_tag = 'ICMS45'
            self.grupo_icms.nome_tag_txt = 'N06'
            self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS45'

        elif self.valor == '60':
            self.grupo_icms.nome_tag = 'ICMS60'
            self.grupo_icms.nome_tag_txt = 'N08'
            self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS60'
            self.grupo_icms.vBCSTRet.obrigatorio   = True
            self.grupo_icms.pICMSSTRet.obrigatorio   = True
            self.grupo_icms.vICMSSTRet.obrigatorio = True

        elif self.valor == '90':
            if self.grupo_icms.icms_outra_uf:
                self.grupo_icms.nome_tag = 'ICMSOutraUF'
                self.grupo_icms.nome_tag_txt = 'N10'
                self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMSOutraUF'
                self.grupo_icms.vBCOutraUF.obrigatorio      = True
                self.grupo_icms.pICMSOutraUF.obrigatorio    = True
                self.grupo_icms.vICMSOutraUF.obrigatorio    = True
            elif self.grupo_icms.icms_sn:
                self.grupo_icms.nome_tag = 'ICMSSN'
                self.grupo_icms.nome_tag_txt = 'N10'
                self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMSSN'
                self.grupo_icms.indSN.obrigatorio      = True
            else:
                self.grupo_icms.nome_tag = 'ICMS90'
                self.grupo_icms.nome_tag_txt = 'N10'
                self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS90'
                #self.grupo_icms.pRedBC.obrigatorio   = True
                self.grupo_icms.vBC.obrigatorio      = True
                self.grupo_icms.pICMS.obrigatorio    = True
                self.grupo_icms.vICMS.obrigatorio    = True

        #
        # Redefine a raiz para todas as tags do grupo ICMS
        #
        #self.grupo_icms.orig.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.CST.raiz      = self.grupo_icms.raiz_tag
        #self.grupo_icms.modBC.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBC.raiz   = self.grupo_icms.raiz_tag
        self.grupo_icms.vBC.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMS.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMS.raiz    = self.grupo_icms.raiz_tag
        #self.grupo_icms.modBCST.raiz  = self.grupo_icms.raiz_tag
        #self.grupo_icms.pMVAST.raiz   = self.grupo_icms.raiz_tag
        #self.grupo_icms.pRedBCST.raiz = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCSTRet.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMSSTRet.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSSTRet.raiz  = self.grupo_icms.raiz_tag

        self.grupo_icms.vBCOutraUF.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMSOutraUF.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSOutraUF.raiz    = self.grupo_icms.raiz_tag

        self.grupo_icms.indSN.raiz = self.grupo_icms.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class ICMS(XMLNFe):
    def __init__(self):
        super(ICMS, self).__init__()
        #self.orig     = TagInteiro(nome='orig'     , tamanho=[1,  1, 1],                     raiz='')
        #self.modBC    = TagInteiro(nome='modBC'    , tamanho=[1,  1, 1],                     raiz='')
        self.pRedBC   = TagDecimal(nome='pRedBC'    , tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vBC      = TagDecimal(nome='vBC'       , tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.pICMS    = TagDecimal(nome='pICMS'     , tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vICMS    = TagDecimal(nome='vICMS'     , tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        #self.modBCST  = TagInteiro(nome='modBCST'  , tamanho=[1,  1, 1],                     raiz='')
        #self.pMVAST   = TagDecimal(nome='pMVAST'   , tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        #self.pRedBCST = TagDecimal(nome='pRedBCST' , tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vBCSTRet   = TagDecimal(nome='vBCSTRet'  , tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.pICMSSTRet = TagDecimal(nome='pICMSSTRet', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vICMSSTRet = TagDecimal(nome='vICMSSTRet', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.vCred      = TagDecimal(nome='vCred'     , tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')

        #Campos ICMSOutraUF
        self.pRedBCOutraUF   = TagDecimal(nome='pRedBCOutraUF', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='', obrigatorio=False)
        self.vBCOutraUF      = TagDecimal(nome='vBCOutraUF', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.pICMSOutraUF    = TagDecimal(nome='pICMSOutraUF', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vICMSOutraUF    = TagDecimal(nome='vICMSOutraUF', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')

        #Campo ICMSSN:
        self.indSN  = TagInteiro(nome='indSN', tamanho=[1, 1, 1], raiz='')

        self.CST      = TagCSTICMS()
        self.CST.grupo_icms = self
        #self.CST.valor = '40'
        self.nome_tag = 'ICMS45'
        self.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS45'
        self.nome_tag_txt = 'N06'

        self.icms_outra_uf  = False #Para grupo ICMSOutraUF
        self.icms_sn        = False #Para grupo ICMSSN (Simples Nacional)

    def get_xml(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += '<ICMS><' + self.nome_tag + '>'
        #xml += self.orig.xml
        xml += self.CST.xml

        if self.CST.valor == '00':
            #xml += self.modBC.xml
            xml += self.vBC.xml
            xml += self.pICMS.xml
            xml += self.vICMS.xml

        elif self.CST.valor == '20':
            #xml += self.modBC.xml
            xml += self.pRedBC.xml
            xml += self.vBC.xml
            xml += self.pICMS.xml
            xml += self.vICMS.xml

        elif self.CST.valor in ('40', '41', '51'):
            pass

        elif self.CST.valor == '60':
            xml += self.vBCSTRet.xml
            xml += self.pICMSSTRet.xml
            xml += self.vICMSSTRet.xml

        elif self.CST.valor == '90':
            if self.icms_outra_uf:
                xml += self.pRedBCOutraUF.xml
                xml += self.vBCOutraUF.xml
                xml += self.pICMSOutraUF.xml
                xml += self.vICMSOutraUF.xml
            elif self.icms_sn:
                xml += self.indSN.xml
            else:
                #xml += self.modBC.xml
                xml += self.pRedBC.xml
                xml += self.vBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml
                xml += self.vCred.xml

        xml += '</' + self.nome_tag + '></ICMS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o ICMS, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            if self._le_noh('//CTe/infCte/imp/ICMS/ICMS00') is not None:
                self.CST.valor = '00'
            elif self._le_noh('//CTe/infCte/imp/ICMS/ICMS20') is not None:
                self.CST.valor = '20'
            elif self._le_noh('//CTe/infCte/imp/ICMS/ICMS45') is not None:
                self.CST.valor = '40'
            elif self._le_noh('//CTe/infCte/imp/ICMS/ICMS60') is not None:
                self.CST.valor = '60'
            elif self._le_noh('//CTe/infCte/imp/ICMS/ICMS90') is not None:
                self.CST.valor = '90'
            elif self._le_noh('//CTe/infCte/imp/ICMS/ICMSOutraUF') is not None:
                self.CST.valor = '90'
            elif self._le_noh('//CTe/infCte/imp/ICMS/ICMSSN') is not None:
                self.CST.valor = '90'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            #self.orig.xml     = arquivo
            self.CST.xml      = arquivo
            #self.modBC.xml    = arquivo
            self.pRedBC.xml   = arquivo
            self.vBC.xml      = arquivo
            self.pICMS.xml    = arquivo
            self.vICMS.xml    = arquivo
            #self.modBCST.xml  = arquivo
            #self.pMVAST.xml   = arquivo
            #self.pRedBCST.xml = arquivo
            self.vBCSTRet.xml    = arquivo
            self.pICMSSTRet.xml  = arquivo
            self.vICMSSTRet.xml  = arquivo
            self.vCred.xml       = arquivo

            self.pRedBCOutraUF.xml  = arquivo
            self.vBCOutraUF.xml     = arquivo
            self.pICMSOutraUF.xml   = arquivo
            self.vICMSOutraUF.xml   = arquivo

            self.indSN.xml = arquivo

    xml = property(get_xml, set_xml)


class Imp(XMLNFe):
    def __init__(self):
        super(Imp, self).__init__()
        self.ICMS     = ICMS()
        self.vTotTrib   = TagDecimal(nome='vTotTrib', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/imp', obrigatorio=False)
        self.infAdFisco = TagCaracter(nome='infAdFisco', tamanho=[1, 2000], raiz='//CTe/infCte/imp', obrigatorio=False)
        self.ICMSUFFim  = ICMSUFFim()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<imp>'
        xml += self.ICMS.xml
        xml += self.vTotTrib.xml
        xml += self.infAdFisco.xml
        xml += self.ICMSUFFim.xml
        xml += '</imp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ICMS.xml       = arquivo
            self.infAdFisco.xml = arquivo
            self.vTotTrib.xml   = arquivo
            self.ICMSUFFim.xml  = arquivo

    xml = property(get_xml, set_xml)


class Comp(XMLNFe):
    def __init__(self):
        super(Comp, self).__init__()
        self.xNome = TagCaracter(nome='xNome', tamanho=[1, 15], raiz='//CTe/infCte/vPrest/Comp')
        self.vComp = TagDecimal(nome='vComp', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/vPrest/Comp')

    def get_xml(self):
        if not (self.xNome.valor or self.vComp.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<Comp>'
        xml += self.xNome.xml
        xml += self.vComp.xml
        xml += '</Comp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xNome.xml  = arquivo
            self.vComp.xml  = arquivo

    xml = property(get_xml, set_xml)


class VPrest(XMLNFe):
    def __init__(self):
        super(VPrest, self).__init__()
        self.vTPrest = TagDecimal(nome='vTPrest', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/vPrest')
        self.vRec = TagDecimal(nome='vRec', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/vPrest')
        self.Comp = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<vPrest>'
        xml += self.vTPrest.xml
        xml += self.vRec.xml
        for c in self.Comp:
            xml += c.xml

        xml += '</vPrest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vTPrest.xml  = arquivo
            self.vRec.xml = arquivo
            self.Comp = self.le_grupo('//CTe/infCte/vPrest/Comp', Comp, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class EnderDest(XMLNFe):
    def __init__(self):
        super(EnderDest, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='E06', tamanho=[ 2, 255]  , raiz='//CTe/infCte/dest/enderDest')
        self.nro     = TagCaracter(nome='nro'    , codigo='E07', tamanho=[ 1, 60]   , raiz='//CTe/infCte/dest/enderDest')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='E08', tamanho=[ 1, 60]   , raiz='//CTe/infCte/dest/enderDest', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='E09', tamanho=[ 2, 60]   , raiz='//CTe/infCte/dest/enderDest')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='E10', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/dest/enderDest')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='E11', tamanho=[ 2, 60]   , raiz='//CTe/infCte/dest/enderDest')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='E13', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/dest/enderDest', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='E12', tamanho=[ 2,  2]   , raiz='//CTe/infCte/dest/enderDest')
        self.cPais   = TagInteiro(nome='cPais'   , codigo='E14', tamanho=[ 4,  4, 4], raiz='//CTe/infCte/dest/enderDest', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , codigo='E15', tamanho=[ 2, 60]   , raiz='//CTe/infCte/dest/enderDest', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderDest>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += '</enderDest>'
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
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo

    xml = property(get_xml, set_xml)


class Dest(XMLNFe):
    def __init__(self):
        super(Dest, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='E02', tamanho=[ 0, 14], raiz='//CTe/infCte/dest', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , codigo='E03', tamanho=[11, 11], raiz='//CTe/infCte/dest', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , codigo='E17', tamanho=[ 2, 14], raiz='//CTe/infCte/dest', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='E04', tamanho=[ 2, 60], raiz='//CTe/infCte/dest')
        self.fone      = TagInteiro(nome='fone'  , codigo='E16', tamanho=[ 6, 14], raiz='//CTe/infCte/dest', obrigatorio=False)
        self.ISUF      = TagCaracter(nome='ISUF' , codigo='E18', tamanho=[ 8,  9], raiz='//CTe/infCte/dest', obrigatorio=False)
        self.enderDest = EnderDest()
        self.email     = TagCaracter(nome='email', codigo='E19', tamanho=[ 1, 60], raiz='//CTe/infCte/dest', obrigatorio=False)
        #self.locEnt    = LocEnt()

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<dest>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.IE.xml
        xml += self.xNome.xml
        xml += self.fone.xml
        xml += self.ISUF.xml
        xml += self.enderDest.xml
        xml += self.email.xml
        #xml += self.locEnt.xml
        xml += '</dest>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.fone.xml      = arquivo
            self.ISUF.xml      = arquivo
            self.enderDest.xml = arquivo
            self.email.xml     = arquivo
            #self.locEnt.xml    = arquivo

    xml = property(get_xml, set_xml)


class EnderReceb(XMLNFe):
    def __init__(self):
        super(EnderReceb, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='E06', tamanho=[ 2, 255]  , raiz='//CTe/infCte/receb/enderReceb')
        self.nro     = TagCaracter(nome='nro'    , codigo='E07', tamanho=[ 1, 60]   , raiz='//CTe/infCte/receb/enderReceb')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='E08', tamanho=[ 1, 60]   , raiz='//CTe/infCte/receb/enderReceb', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='E09', tamanho=[ 2, 60]   , raiz='//CTe/infCte/receb/enderReceb')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='E10', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/receb/enderReceb')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='E11', tamanho=[ 2, 60]   , raiz='//CTe/infCte/receb/enderReceb')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='E13', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/receb/enderReceb', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='E12', tamanho=[ 2,  2]   , raiz='//CTe/infCte/receb/enderReceb')
        self.cPais   = TagInteiro(nome='cPais'   , codigo='E14', tamanho=[ 4,  4, 4], raiz='//CTe/infCte/receb/enderReceb', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , codigo='E15', tamanho=[ 2, 60]   , raiz='//CTe/infCte/receb/enderReceb', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderReceb>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += '</enderReceb>'
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
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo

    xml = property(get_xml, set_xml)


class Receb(XMLNFe):
    def __init__(self):
        super(Receb, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='E02', tamanho=[ 0, 14], raiz='//CTe/infCte/receb', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , codigo='E03', tamanho=[11, 11], raiz='//CTe/infCte/receb', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , codigo='E17', tamanho=[ 2, 14], raiz='//CTe/infCte/receb', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='E04', tamanho=[ 2, 60], raiz='//CTe/infCte/receb')
        self.fone      = TagInteiro(nome='fone'  , codigo='E16', tamanho=[ 6, 14], raiz='//CTe/infCte/receb', obrigatorio=False)
        self.enderReceb = EnderReceb()
        self.email     = TagCaracter(nome='email', codigo='E19', tamanho=[ 1, 60], raiz='//CTe/infCte/receb', obrigatorio=False)

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<receb>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.IE.xml
        xml += self.xNome.xml
        xml += self.fone.xml
        xml += self.enderReceb.xml
        xml += self.email.xml
        xml += '</receb>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.fone.xml      = arquivo
            self.enderReceb.xml = arquivo
            self.email.xml     = arquivo

    xml = property(get_xml, set_xml)


class EnderExped(XMLNFe):
    def __init__(self):
        super(EnderExped, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='E06', tamanho=[ 2, 255]  , raiz='//CTe/infCte/exped/enderExped')
        self.nro     = TagCaracter(nome='nro'    , codigo='E07', tamanho=[ 1, 60]   , raiz='//CTe/infCte/exped/enderExped')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='E08', tamanho=[ 1, 60]   , raiz='//CTe/infCte/exped/enderExped', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='E09', tamanho=[ 2, 60]   , raiz='//CTe/infCte/exped/enderExped')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='E10', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/exped/enderExped')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='E11', tamanho=[ 2, 60]   , raiz='//CTe/infCte/exped/enderExped')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='E13', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/exped/enderExped', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='E12', tamanho=[ 2,  2]   , raiz='//CTe/infCte/exped/enderExped')
        self.cPais   = TagInteiro(nome='cPais'   , codigo='E14', tamanho=[ 4,  4, 4], raiz='//CTe/infCte/exped/enderExped', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , codigo='E15', tamanho=[ 1, 60]   , raiz='//CTe/infCte/exped/enderExped', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderExped>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += '</enderExped>'
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
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo

    xml = property(get_xml, set_xml)


class Exped(XMLNFe):
    def __init__(self):
        super(Exped, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='E02', tamanho=[ 0, 14], raiz='//CTe/infCte/exped', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , codigo='E03', tamanho=[11, 11], raiz='//CTe/infCte/exped', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , codigo='E17', tamanho=[ 2, 14], raiz='//CTe/infCte/exped', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='E04', tamanho=[ 2, 60], raiz='//CTe/infCte/exped')
        self.fone      = TagInteiro(nome='fone'  , codigo='E16', tamanho=[ 6, 14], raiz='//CTe/infCte/exped', obrigatorio=False)
        self.enderExped = EnderExped()
        self.email     = TagCaracter(nome='email', codigo='E19', tamanho=[ 1, 60], raiz='//CTe/infCte/exped', obrigatorio=False)

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<exped>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.IE.xml
        xml += self.xNome.xml
        xml += self.fone.xml
        xml += self.enderExped.xml
        xml += self.email.xml
        xml += '</exped>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.fone.xml      = arquivo
            self.enderExped.xml = arquivo
            self.email.xml     = arquivo

    xml = property(get_xml, set_xml)


class EnderReme(XMLNFe):
    def __init__(self):
        super(EnderReme, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='E06', tamanho=[ 2, 255]  , raiz='//CTe/infCte/rem/enderReme')
        self.nro     = TagCaracter(nome='nro'    , codigo='E07', tamanho=[ 1, 60]   , raiz='//CTe/infCte/rem/enderReme')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='E08', tamanho=[ 1, 60]   , raiz='//CTe/infCte/rem/enderReme', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='E09', tamanho=[ 2, 60]   , raiz='//CTe/infCte/rem/enderReme')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='E10', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/rem/enderReme')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='E11', tamanho=[ 2, 60]   , raiz='//CTe/infCte/rem/enderReme')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='E13', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/rem/enderReme', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='E12', tamanho=[ 2,  2]   , raiz='//CTe/infCte/rem/enderReme')
        self.cPais   = TagInteiro(nome='cPais'   , codigo='E14', tamanho=[ 4,  4, 4], raiz='//CTe/infCte/rem/enderReme', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , codigo='E15', tamanho=[ 1, 60]   , raiz='//CTe/infCte/rem/enderReme', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderReme>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += '</enderReme>'
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
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo

    xml = property(get_xml, set_xml)


class Rem(XMLNFe):
    def __init__(self):
        super(Rem, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='E02', tamanho=[ 0, 14], raiz='//CTe/infCte/rem', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , codigo='E03', tamanho=[11, 11], raiz='//CTe/infCte/rem', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , codigo='E17', tamanho=[ 2, 14], raiz='//CTe/infCte/rem', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='E04', tamanho=[ 2, 60], raiz='//CTe/infCte/rem')
        self.xFant     = TagCaracter(nome='xFant', codigo='E04', tamanho=[ 1, 60], raiz='//CTe/infCte/rem', obrigatorio=False)
        self.fone      = TagInteiro(nome='fone'  , codigo='E16', tamanho=[ 6, 14], raiz='//CTe/infCte/rem', obrigatorio=False)
        self.enderReme = EnderReme()
        self.email     = TagCaracter(nome='email', codigo='E19', tamanho=[ 1, 60], raiz='//CTe/infCte/rem', obrigatorio=False)
        #self.infNF     = []
        #self.infNFe    = []
        #self.infOutros = []

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<rem>'
        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.IE.xml
        xml += self.xNome.xml
        xml += self.xFant.xml
        xml += self.fone.xml
        xml += self.enderReme.xml
        xml += self.email.xml

        xml += '</rem>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.xFant.xml     = arquivo
            self.fone.xml      = arquivo
            self.enderReme.xml = arquivo
            self.email.xml     = arquivo
            #self.infNF  = self.le_grupo('//CTe/infCte/rem/infNF', InfNF, sigla_ns='cte')
            #self.infNFe = self.le_grupo('//CTe/infCte/rem/infNFe', InfNFe, sigla_ns='cte')
            #self.infOutros = self.le_grupo('//CTe/infCte/rem/infOutros', InfOutros, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class EnderEmit(XMLNFe):
    def __init__(self):
        super(EnderEmit, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='C06', tamanho=[ 2, 60]   , raiz='//CTe/infCte/emit/enderEmit')
        self.nro     = TagCaracter(nome='nro'    , codigo='C07', tamanho=[ 1, 60]   , raiz='//CTe/infCte/emit/enderEmit')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='C08', tamanho=[ 1, 60]   , raiz='//CTe/infCte/emit/enderEmit', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='C09', tamanho=[ 2, 60]   , raiz='//CTe/infCte/emit/enderEmit')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='C10', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/emit/enderEmit')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='C11', tamanho=[ 2, 60]   , raiz='//CTe/infCte/emit/enderEmit')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='C13', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/emit/enderEmit', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='C12', tamanho=[ 2,  2]   , raiz='//CTe/infCte/emit/enderEmit')
        #self.cPais   = TagInteiro(nome='cPais'   , codigo='C14', tamanho=[ 4,  4, 4], raiz='//CTe/infCte/emit/enderEmit', obrigatorio=False)
        #self.xPais   = TagCaracter(nome='xPais'  , codigo='C15', tamanho=[ 1, 60]   , raiz='//CTe/infCte/emit/enderEmit', obrigatorio=False)
        self.fone    = TagInteiro(nome='fone'    , codigo='C16', tamanho=[ 6, 14]   , raiz='//CTe/infCte/emit/enderEmit', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderEmit>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        #xml += self.cPais.xml
        #xml += self.xPais.xml
        xml += self.fone.xml
        xml += '</enderEmit>'
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
            #self.cPais.xml   = arquivo
            #self.xPais.xml   = arquivo
            self.fone.xml    = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'C05|'
        txt += self.xLgr.txt + '|'
        txt += self.nro.txt + '|'
        txt += self.xCpl.txt + '|'
        txt += self.xBairro.txt + '|'
        txt += self.cMun.txt + '|'
        txt += self.xMun.txt + '|'
        txt += self.CEP.txt + '|'
        txt += self.UF.txt + '|'
        #txt += self.cPais.txt + '|'
        #txt += self.xPais.txt + '|'
        txt += self.fone.txt + '|'
        txt += '\n'

        return txt

    txt = property(get_txt)


class Emit(XMLNFe):
    def __init__(self):
        super(Emit, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='C02' , tamanho=[14, 14], raiz='//CTe/infCte/emit', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , codigo='C17' , tamanho=[ 2, 14], raiz='//CTe/infCte/emit', obrigatorio=False)
        self.IEST      = TagInteiro(nome='IEST', tamanho=[14, 14], raiz='//CTe/infCte/emit', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='C03' , tamanho=[ 2, 60], raiz='//CTe/infCte/emit')
        self.xFant     = TagCaracter(nome='xFant', codigo='C04' , tamanho=[ 1, 60], raiz='//CTe/infCte/emit', obrigatorio=False)
        self.enderEmit = EnderEmit()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<emit>'
        xml += self.CNPJ.xml
        xml += self.IE.xml
        xml += self.IEST.xml
        xml += self.xNome.xml
        xml += self.xFant.xml
        xml += self.enderEmit.xml
        xml += '</emit>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.IE.xml        = arquivo
            self.IEST.xml      = arquivo
            self.xNome.xml     = arquivo
            self.xFant.xml     = arquivo
            self.enderEmit.xml = arquivo

    xml = property(get_xml, set_xml)


class ObsFisco(XMLNFe):
    def __init__(self):
        super(ObsFisco, self).__init__()
        self.xCampo = TagCaracter(nome='ObsFisco', codigo='Z08', propriedade='xCampo', tamanho=[1, 20], raiz='/', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xTexto = TagCaracter(nome='xTexto', codigo='Z09', tamanho=[1, 60], raiz='//ObsFisco', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.xCampo.valor or self.xTexto.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ObsFisco xCampo="' + self.xCampo.valor + '">'
        xml += self.xTexto.xml
        xml += '</ObsFisco>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xCampo.xml = arquivo
            self.xTexto.xml = arquivo

    xml = property(get_xml, set_xml)


class ObsCont(XMLNFe):
    def __init__(self):
        super(ObsCont, self).__init__()
        self.xCampo = TagCaracter(nome='ObsCont', propriedade='xCampo', tamanho=[1,  20], raiz='/', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xTexto = TagCaracter(nome='xTexto', codigo='Z06', tamanho=[1, 160], raiz='//ObsCont', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.xCampo.valor or self.xTexto.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ObsCont xCampo="' + self.xCampo.valor + '">'
        xml += self.xTexto.xml
        xml += '</ObsCont>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xCampo.xml = arquivo
            self.xTexto.xml = arquivo

    xml = property(get_xml, set_xml)


class Entrega(XMLNFe):
    def __init__(self):
        super(Entrega, self).__init__()
        #
        # Data da entrega
        #
        self.tpPer = TagCaracter(nome='tpPer', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/semData')
        self.tpPerSemData = TagCaracter(nome='tpPer', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/semData', obrigatorio=False)
        self.tpPerComData = TagCaracter(nome='tpPer', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/comData', obrigatorio=False)
        self.dProg = TagData(nome='dProg', raiz='//CTe/infCte/compl/Entrega/comData')
        self.tpPerNoPeriodo = TagCaracter(nome='tpPer', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/noPeriodo', obrigatorio=False)
        self.dIni = TagData(nome='dIni', raiz='//CTe/infCte/compl/Entrega/noPeriodo')
        self.dFim = TagData(nome='dFim', raiz='//CTe/infCte/compl/Entrega/noPeriodo')

        #
        # Hora da entrega
        #
        self.tpHor = TagCaracter(nome='tpHor', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/semHora')
        self.tpHorSemHora = TagCaracter(nome='tpHor', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/semHora', obrigatorio=False)
        self.tpHorComHora = TagCaracter(nome='tpHor', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/comHora', obrigatorio=False)
        self.hProg = TagHora(nome='hProg', raiz='//CTe/infCte/compl/Entrega/comHora')
        self.tpHorNoInter = TagCaracter(nome='tpHor', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/noInter', obrigatorio=False)
        self.hIni = TagHora(nome='hIni', raiz='//CTe/infCte/compl/Entrega/noInter')
        self.hFim = TagHora(nome='hFim', raiz='//CTe/infCte/compl/Entrega/noInter')


    def get_xml(self):
        if not (self.tpPer.valor and self.tpHor.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<Entrega>'

        if self.tpPer.valor == '0':
            xml += '<semData>'
            xml += self.tpPer.xml
            xml += '</semData>'

        elif self.tpPer.valor <= '3':
            xml += '<comData>'
            xml += self.tpPer.xml
            xml += self.dProg.xml
            xml += '</comData>'

        else:
            xml += '<noPeriodo>'
            xml += self.tpPer.xml
            xml += self.dIni.xml
            xml += self.dFim.xml
            xml += '</noPeriodo>'

        if self.tpHor.valor == '0':
            xml += '<semHora>'
            xml += self.tpHor.xml
            xml += '</semHora>'

        elif self.tpHor.valor <= '3':
            xml += '<comHora>'
            xml += self.tpHor.xml
            xml += self.hProg.xml
            xml += '</comHora>'

        else:
            xml += '<noInter>'
            xml += self.tpHor.xml
            xml += self.hIni.xml
            xml += self.hFim.xml
            xml += '</noInter>'

        xml += '</Entrega>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):

            if self._le_noh('//CTe/infCte/compl/Entrega/semData') is not None:
                self.tpPerSemData.xml = arquivo
                self.tpPer.valor = self.tpPerSemData.valor
            elif self._le_noh('//CTe/infCte/compl/Entrega/comData') is not None:
                self.tpPerComData.xml = arquivo
                self.tpPer.valor = self.tpPerComData.valor
            else:
                self.tpPerNoPeriodo.xml = arquivo
                self.tpPer.valor = self.tpPerNoPeriodo.valor

            self.dProg.xml = arquivo
            self.dIni.xml = arquivo
            self.dFim.xml = arquivo

            if self._le_noh('//CTe/infCte/compl/Entrega/semHora') is not None:
                self.tpHorSemHora.xml = arquivo
                self.tpHor.valor = self.tpHorSemHora.valor
            elif self._le_noh('//CTe/infCte/compl/Entrega/comHora') is not None:
                self.tpHorComHora.xml = arquivo
                self.tpHor.valor = self.tpHorComHora.valor
            else:
                self.tpHorNoInter.xml = arquivo
                self.tpHor.valor = self.tpHorNoInter.valor

            self.hProg.xml = arquivo
            self.hIni.xml = arquivo
            self.hFim.xml = arquivo

    xml = property(get_xml, set_xml)


class Pass(XMLNFe):
    def __init__(self):
        super(Pass, self).__init__()
        self.xPass = TagCaracter(nome='xPass', tamanho=[1,  15], raiz='//pass', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not self.xPass.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<pass>'
        xml += self.xPass.xml
        xml += '</pass>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xPass.xml = arquivo

    xml = property(get_xml, set_xml)


class Fluxo(XMLNFe):
    def __init__(self):
        super(Fluxo, self).__init__()
        self.xOrig = TagCaracter(nome='xOrig', tamanho=[1,  60], raiz='//CTe/infCte/compl/fluxo', obrigatorio=False)
        self.passagem = []
        self.xDest = TagCaracter(nome='xDest', tamanho=[1,  60], raiz='//CTe/infCte/compl/fluxo', obrigatorio=False)
        self.xRota = TagCaracter(nome='xRota', tamanho=[1,  10], raiz='//CTe/infCte/compl/fluxo', obrigatorio=False)

    def get_xml(self):
        if not (self.xOrig.valor or self.xDest.valor or self.xRota.valor or len(self.passagem)):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<fluxo>'
        xml += self.xOrig.xml

        if len(self.passagem):
            for p in self.passagem:
                xml += p.xml

        xml += self.xDest.xml
        xml += self.xRota.xml
        xml += '</fluxo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xOrig.xml = arquivo
            self.passagem = self.le_grupo('//CTe/infCte/compl/fluxo/pass', Pass, sigla_ns='cte')
            self.xDest.xml = arquivo
            self.xRota.xml = arquivo

    xml = property(get_xml, set_xml)


class Compl(XMLNFe):
    def __init__(self):
        super(Compl, self).__init__()
        self.xCaracAd = TagCaracter(nome='xCaracAd', tamanho=[ 1, 15], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.xCaracSer = TagCaracter(nome='xCaracSer', tamanho=[ 1, 30], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.xEmi = TagCaracter(nome='xEmi', tamanho=[ 1, 20], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.fluxo = Fluxo()
        self.Entrega = Entrega()
        self.origCalc = TagCaracter(nome='origCalc', tamanho=[ 2, 40], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.destCalc = TagCaracter(nome='destCalc', tamanho=[ 2, 40], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.xObs = TagCaracter(nome='xObs', tamanho=[ 1, 2000], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.ObsCont = []
        self.ObsFisco = []

    def get_xml(self):
        if not (self.xCaracAd.valor or self.xCaracSer.valor or self.xEmi.valor or self.origCalc.valor or self.destCalc.valor or
            self.xObs.valor or len(self.ObsCont) or len(self.ObsFisco) or self.fluxo is not None or self.Entrega is not None):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<compl>'
        xml += self.xCaracAd.xml
        xml += self.xCaracSer.xml
        xml += self.xEmi.xml
        xml += self.fluxo.xml
        xml += self.Entrega.xml
        xml += self.origCalc.xml
        xml += self.destCalc.xml
        xml += self.xObs.xml

        for o in self.ObsCont:
            xml += o.xml

        for o in self.ObsFisco:
            xml += o.xml

        xml += '</compl>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xCaracAd.xml = arquivo
            self.xCaracSer.xml = arquivo
            self.xEmi.xml = arquivo
            self.fluxo.xml = arquivo
            self.Entrega.xml = arquivo
            self.origCalc.xml = arquivo
            self.destCalc.xml = arquivo
            self.xObs.xml = arquivo
            self.ObsCont = self.le_grupo('//CTe/infCte/compl/ObsCont', ObsCont, sigla_ns='cte')
            self.ObsFisco = self.le_grupo('//CTe/infCte/compl/ObsFisco', ObsFisco, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class EnderToma(XMLNFe):
    def __init__(self):
        super(EnderToma, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , tamanho=[ 2, 255]  , raiz='//CTe/infCte/ide/toma4/enderToma')
        self.nro     = TagCaracter(nome='nro'    , tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide/toma4/enderToma')
        self.xCpl    = TagCaracter(nome='xCpl'   , tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide/toma4/enderToma', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', tamanho=[ 2, 60]   , raiz='//CTe/infCte/ide/toma4/enderToma')
        self.cMun    = TagInteiro(nome='cMun'    , tamanho=[ 7,  7, 7], raiz='//CTe/infCte/ide/toma4/enderToma')
        self.xMun    = TagCaracter(nome='xMun'   , tamanho=[ 2, 60]   , raiz='//CTe/infCte/ide/toma4/enderToma')
        self.CEP     = TagCaracter(nome='CEP'    , tamanho=[ 8,  8, 8], raiz='//CTe/infCte/ide/toma4/enderToma', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , tamanho=[ 2,  2]   , raiz='//CTe/infCte/ide/toma4/enderToma')
        self.cPais   = TagInteiro(nome='cPais'   , tamanho=[ 4,  4, 4], raiz='//CTe/infCte/ide/toma4/enderToma', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , tamanho=[ 2, 60]   , raiz='//CTe/infCte/ide/toma4/enderToma', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderToma>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += '</enderToma>'
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
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo

    xml = property(get_xml, set_xml)


class Tomador(XMLNFe):
    def __init__(self):
        super(Tomador, self).__init__()
        self.toma      = TagInteiro(nome='toma', tamanho=[1, 1, 1], raiz='//CTe/infCte/ide/toma3', valor=0)
        self.toma3     = TagInteiro(nome='toma', tamanho=[1, 1, 1], raiz='//CTe/infCte/ide/toma3', valor=0)
        self.toma4     = TagInteiro(nome='toma', tamanho=[1, 1, 1], raiz='//CTe/infCte/ide/toma4', valor=4)
        self.CNPJ      = TagCaracter(nome='CNPJ' , tamanho=[ 0, 14], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , tamanho=[11, 11], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , tamanho=[ 2, 14], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', tamanho=[ 2, 60], raiz='//CTe/infCte/ide/toma4')
        self.xFant     = TagCaracter(nome='xFant', tamanho=[ 2, 60], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)
        self.fone      = TagInteiro(nome='fone'  , tamanho=[ 6, 14], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)
        self.enderToma = EnderToma()
        self.email     = TagCaracter(nome='email', tamanho=[ 1, 60], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.toma.valor < 4:
            xml += '<toma3>'
            xml += self.toma.xml
            xml += '</toma3>'

        else:
            xml += '<toma4>'
            xml += self.toma.xml

            if self.CPF.valor:
                xml += self.CPF.xml
            else:
                xml += self.CNPJ.xml

            xml += self.IE.xml
            xml += self.xNome.xml
            xml += self.xFant.xml
            xml += self.fone.xml
            xml += self.enderToma.xml
            xml += self.email.xml
            xml += '</toma4>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.xFant.xml     = arquivo
            self.fone.xml      = arquivo
            self.enderToma.xml = arquivo
            self.email.xml     = arquivo

            if self._le_noh('//CTe/infCte/ide/toma3/toma') is not None:
                self.toma3.xml = arquivo
                self.toma.valor = self.toma3.valor
            else:
                self.toma4.xml = arquivo
                self.toma.valor = self.toma4.valor

    xml = property(get_xml, set_xml)


class Ide(XMLNFe):
    def __init__(self):
        super(Ide, self).__init__()
        self.cUF     = TagInteiro(nome='cUF', tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide')
        self.cCT     = TagCaracter(nome='cCT', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/ide')
        self.CFOP    = TagCaracter(nome='CFOP', tamanho=[4,   4, 4], raiz='//CTe/infCte/ide')
        self.natOp   = TagCaracter(nome='natOp', tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide')
        self.mod     = TagInteiro(nome='mod'     , tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide', valor=57)
        self.serie   = TagInteiro(nome='serie'   , tamanho=[ 1,  3, 1], raiz='//CTe/infCte/ide')
        self.nCT     = TagInteiro(nome='nCT'     , tamanho=[ 1,  9, 1], raiz='//CTe/infCte/ide')
        self.dhEmi   = TagDataHoraUTC(nome='dhEmi'  ,                      raiz='//CTe/infCte/ide')
        self.tpImp   = TagInteiro(nome='tpImp'   , tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=1)
        self.tpEmis  = TagInteiro(nome='tpEmis'  , tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=1)
        self.cDV     = TagInteiro(nome='cDV'     , tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide')
        self.tpAmb   = TagInteiro(nome='tpAmb'   , tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=2)
        self.tpCTe   = TagInteiro(nome='tpCTe'   , tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=1)
        self.procEmi = TagInteiro(nome='procEmi' , tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide')
        self.verProc = TagCaracter(nome='verProc', tamanho=[ 1, 20]   , raiz='//CTe/infCte/ide')
        self.indGlobalizado = TagInteiro(nome='indGlobalizado', tamanho=[1, 1, 1], raiz='//CTe/infCte/ide', obrigatorio=False)
        self.cMunEnv = TagInteiro(nome='cMunEnv' , tamanho=[ 7,  7, 7], raiz='//CTe/infCte/ide')
        self.xMunEnv = TagCaracter(nome='xMunEnv', tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide')
        self.UFEnv   = TagCaracter(nome='UFEnv'  , tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide')
        self.modal   = TagCaracter(nome='modal'  , tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide', default='01')
        self.tpServ  = TagInteiro(nome='tpServ'  , tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=0)
        self.cMunIni = TagInteiro(nome='cMunIni' , tamanho=[ 7,  7, 7], raiz='//CTe/infCte/ide')
        self.xMunIni = TagCaracter(nome='xMunIni', tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide')
        self.UFIni   = TagCaracter(nome='UFIni'  , tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide')
        self.cMunFim = TagInteiro(nome='cMunFim' , tamanho=[ 7,  7, 7], raiz='//CTe/infCte/ide')
        self.xMunFim = TagCaracter(nome='xMunFim', tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide')
        self.UFFim   = TagCaracter(nome='UFFim'  , tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide')
        self.retira  = TagInteiro(nome='retira'  , tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=0)
        self.xDetRetira  = TagCaracter(nome='xDetRetira', tamanho=[ 1, 160], raiz='//CTe/infCte/ide', obrigatorio=False)
        self.indIEToma = TagInteiro(nome='indIEToma', tamanho=[1, 1, 1], raiz='//CTe/infCte/ide')
        self.tomador  = Tomador()
        self.dhCont   = TagDataHora(nome='dhCont', raiz='//CTe/infCte/ide', obrigatorio=False)
        self.xJust    = TagCaracter(nome='xJust', raiz='//CTe/infCte/ide', tamanho=[15, 256], obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ide>'
        xml += self.cUF.xml
        xml += self.cCT.xml
        xml += self.CFOP.xml
        xml += self.natOp.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nCT.xml
        xml += self.dhEmi.xml
        xml += self.tpImp.xml
        xml += self.tpEmis.xml
        xml += self.cDV.xml
        xml += self.tpAmb.xml
        xml += self.tpCTe.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += self.indGlobalizado.xml
        xml += self.cMunEnv.xml
        xml += self.xMunEnv.xml
        xml += self.UFEnv.xml
        xml += self.modal.xml
        xml += self.tpServ.xml
        xml += self.cMunIni.xml
        xml += self.xMunIni.xml
        xml += self.UFIni.xml
        xml += self.cMunFim.xml
        xml += self.xMunFim.xml
        xml += self.UFFim.xml
        xml += self.retira.xml
        xml += self.xDetRetira.xml
        xml += self.indIEToma.xml
        xml += self.tomador.xml
        xml += self.dhCont.xml
        xml += self.xJust.xml

        xml += '</ide>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml     = arquivo
            self.cCT.xml     = arquivo
            self.CFOP.xml     = arquivo
            self.natOp.xml   = arquivo
            self.mod.xml     = arquivo
            self.serie.xml   = arquivo
            self.nCT.xml     = arquivo
            self.dhEmi.xml    = arquivo
            self.tpImp.xml   = arquivo
            self.tpEmis.xml  = arquivo
            self.cDV.xml     = arquivo
            self.tpAmb.xml   = arquivo
            self.tpCTe.xml   = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo
            self.indGlobalizado.xml  = arquivo
            self.cMunEnv.xml = arquivo
            self.xMunEnv.xml = arquivo
            self.UFEnv.xml   = arquivo
            self.modal.xml   = arquivo
            self.tpServ.xml  = arquivo
            self.cMunIni.xml = arquivo
            self.xMunIni.xml = arquivo
            self.UFIni.xml   = arquivo
            self.cMunFim.xml = arquivo
            self.xMunFim.xml = arquivo
            self.UFFim.xml   = arquivo
            self.retira.xml  = arquivo
            self.xDetRetira.xml = arquivo
            self.indIEToma.xml = arquivo
            self.tomador.xml   = arquivo
            self.dhCont.xml  = arquivo
            self.xJust.xml   = arquivo

    xml = property(get_xml, set_xml)


class InfCTe(XMLNFe):
    def __init__(self):
        super(InfCTe, self).__init__()
        self.versao   = TagDecimal(nome='infCte', propriedade='versao', raiz='//CTe', namespace=NAMESPACE_CTE, valor='3.00')
        self.Id       = TagCaracter(nome='infCte', propriedade='Id', raiz='//CTe', namespace=NAMESPACE_CTE)
        self.ide      = Ide()
        self.compl    = Compl()
        self.emit     = Emit()
        self.rem      = Rem()
        self.exped    = Exped()
        self.receb    = Receb()
        self.dest     = Dest()
        self.vPrest   = VPrest()
        self.imp      = Imp()
        self.autXML   = []
        ##Escolha tipo CT-e:
        #0 - CT-e Normal ou Substituto
        #1 - CT-e Complemento de valores
        #2 - CT-e de Anulação
        self.tipo_cte = 0
        self.infCTeNorm = InfCTeNorm()
        self.infCTeComp = InfCTeComp()
        self.infCTeAnu  = InfCTeAnu()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<infCte versao="' + unicode(self.versao.valor) + '" Id="' + self.Id.valor + '">'
        xml += self.ide.xml
        xml += self.compl.xml
        xml += self.emit.xml
        xml += self.rem.xml
        xml += self.exped.xml
        xml += self.receb.xml
        xml += self.dest.xml
        xml += self.vPrest.xml
        xml += self.imp.xml

        if self.tipo_cte == 1:
            xml += self.infCTeComp.xml
        elif self.tipo_cte == 2:
            xml += self.infCTeAnu.xml
        else:
            xml += self.infCTeNorm.xml

        xml += '</infCte>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.Id.xml       = arquivo
            self.ide.xml      = arquivo
            self.compl.xml    = arquivo
            self.emit.xml     = arquivo
            self.rem.xml      = arquivo
            self.exped.xml    = arquivo
            self.receb.xml    = arquivo
            self.dest.xml     = arquivo
            self.vPrest.xml   = arquivo
            self.imp.xml      = arquivo
            self.infCTeNorm.xml = arquivo
            self.infCTeComp.xml = arquivo
            self.infCTeAnu.xml = arquivo

            if self.ide.tomador.toma.valor != 4:
                if self.ide.tomador.toma.valor == 0:
                    tomador = self.rem
                    endertoma = self.rem.enderReme
                elif self.ide.tomador.toma.valor == 1:
                    tomador = self.exped
                    endertoma = self.exped.enderExped
                elif self.ide.tomador.toma.valor == 2:
                    tomador = self.receb
                    endertoma = self.receb.enderReceb
                elif self.ide.tomador.toma.valor == 3:
                    tomador = self.dest
                    endertoma = self.dest.enderDest

                self.ide.tomador.CNPJ.valor = tomador.CNPJ.valor
                self.ide.tomador.CPF.valor = tomador.CPF.valor
                self.ide.tomador.IE.valor = tomador.IE.valor
                self.ide.tomador.xNome.valor = tomador.xNome.valor

                try:
                    self.ide.tomador.xFant.valor = tomador.xFant.valor4
                except:
                    pass

                self.ide.tomador.fone.valor = tomador.fone.valor
                self.ide.tomador.email.valor = tomador.email.valor
                self.ide.tomador.enderToma.xLgr.valor = endertoma.xLgr.valor
                self.ide.tomador.enderToma.nro.valor = endertoma.nro.valor
                self.ide.tomador.enderToma.xCpl.valor = endertoma.xCpl.valor
                self.ide.tomador.enderToma.xBairro.valor = endertoma.xBairro.valor
                self.ide.tomador.enderToma.cMun.valor = endertoma.cMun.valor
                self.ide.tomador.enderToma.xMun.valor = endertoma.xMun.valor
                self.ide.tomador.enderToma.CEP.valor = endertoma.CEP.valor
                self.ide.tomador.enderToma.UF.valor = endertoma.UF.valor
                self.ide.tomador.enderToma.cPais.valor = endertoma.cPais.valor
                self.ide.tomador.enderToma.xPais.valor = endertoma.xPais.valor

    xml = property(get_xml, set_xml)


class CTe(XMLNFe):
    def __init__(self):
        super(CTe, self).__init__()
        self.infCte = InfCTe()
        self.Signature = Signature()

        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'cte_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += u'<CTe xmlns="' + NAMESPACE_CTE + u'">'
        xml += self.infCte.xml
        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = u'#' + self.infCte.Id.valor

        xml += self.Signature.xml
        xml += u'</CTe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infCte.xml    = arquivo
            self.Signature.xml = self._le_noh('//CTe/sig:Signature')


    xml = property(get_xml, set_xml)

    def _calcula_dv(self, valor):
        soma = 0
        m = 2
        for i in range(len(valor)-1, -1, -1):
            c = valor[i]
            soma += int(c) * m
            m += 1
            if m > 9:
                m = 2

        digito = 11 - (soma % 11)
        if digito > 9:
            digito = 0

        return digito

    def gera_nova_chave(self):
        chave = unicode(self.infCte.ide.cUF.valor).zfill(2)
        chave += unicode(self.infCte.ide.dhEmi.valor.strftime('%y%m')).zfill(4)
        chave += unicode(self.infCte.emit.CNPJ.valor).zfill(14)
        chave += unicode(self.infCte.ide.mod.valor).zfill(2)
        chave += unicode(self.infCte.ide.serie.valor).zfill(3)
        chave += unicode(self.infCte.ide.nCT.valor).zfill(9)
        chave += unicode(self.infCte.ide.tpEmis.valor).zfill(1)

        #
        # O código numério é um número aleatório
        #
        #chave += unicode(random.randint(0, 99999999)).strip().rjust(8, '0')

        #
        # Mas, por segurança, é preferível que esse número não seja aleatório de todo
        #
        soma = 0
        for c in chave:
            soma += int(c) ** 3 ** 2

        codigo = unicode(soma)
        if len(codigo) > 8:
            codigo = codigo[-8:]
        else:
            codigo = codigo.rjust(8, '0')

        chave += codigo

        #
        # Define na estrutura do XML o campo cCT
        #
        #self.infCte.ide.cCT.valor = unicode(self.infCte.ide.tpEmis.valor).zfill(1) + codigo
        self.infCte.ide.cCT.valor = chave[-8:]

        #
        # Gera o dígito verificador
        #
        digito = self._calcula_dv(chave)

        #
        # Define na estrutura do XML o campo cDV
        #
        self.infCte.ide.cDV.valor = digito

        chave += unicode(digito)
        self.chave = chave

        #
        # Define o Id
        #
        self.infCte.Id.valor = 'CTe' + chave

    def monta_chave(self):
        self.gera_nova_chave()
        chave = unicode(self.infCte.ide.cUF.valor).zfill(2)
        chave += unicode(self.infCte.ide.dhEmi.valor.strftime('%y%m')).zfill(4)
        chave += unicode(self.infCte.emit.CNPJ.valor).zfill(14)
        chave += unicode(self.infCte.ide.mod.valor).zfill(2)
        chave += unicode(self.infCte.ide.serie.valor).zfill(3)
        chave += unicode(self.infCte.ide.nCT.valor).zfill(9)
        chave += unicode(self.infCte.ide.tpEmis.valor).zfill(1)
        chave += unicode(self.infCte.ide.cCT.valor).zfill(8)
        chave += unicode(self.infCte.ide.cDV.valor).zfill(1)
        self.chave = chave


