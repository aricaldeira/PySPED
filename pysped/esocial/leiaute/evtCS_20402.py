# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2.1 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Library General Public License,
# publicada pela Free Software Foundation, em sua versão 2.1 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Library General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Library General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str
import os
from pysped.xml_sped import *
from pysped.esocial.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

DIRNAME = os.path.dirname(__file__)

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtCS/v02_04_02'


class InfoCRContrib(XMLNFe):
    def __init__(self):
        super(InfoCRContrib, self).__init__()
        self.tpCR     = TagCaracter(nome='tpCR',    tamanho=[1, 6],     raiz='//infoCRContrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCR     = TagDecimal(nome='vrCR',     tamanho=[1, 14, 2], raiz='//infoCRContrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSuspCR = TagDecimal(nome='vrSuspCR', tamanho=[1, 14, 2], raiz='//infoCRContrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCREstab>'
        xml += self.tpCR.xml
        xml += self.vrCR.xml
        xml += self.vrSuspCR.xml
        xml += '</infoCREstab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpCR.xml = arquivo
            self.vrCR.xml = arquivo
            self.vrSuspCR.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoCREstab(XMLNFe):
    def __init__(self):
        super(InfoCREstab, self).__init__()
        self.tpCR     = TagCaracter(nome='tpCR',    tamanho=[1, 6],     raiz='//infoCREstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCR     = TagDecimal(nome='vrCR',     tamanho=[1, 14, 2], raiz='//infoCREstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSuspCR = TagDecimal(nome='vrSuspCR', tamanho=[1, 14, 2], raiz='//infoCREstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCREstab>'
        xml += self.tpCR.xml
        xml += self.vrCR.xml
        xml += self.vrSuspCR.xml
        xml += '</infoCREstab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpCR.xml = arquivo
            self.vrCR.xml = arquivo
            self.vrSuspCR.xml = arquivo

    xml = property(get_xml, set_xml)


class BasesComerc(XMLNFe):
    def __init__(self):
        super(BasesComerc, self).__init__()
        self.indComerc   = TagCaracter(nome='indComerc',  tamanho=[1, 1],     raiz='//basesComerc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcComPR   = TagDecimal(nome='vrBcComPR',   tamanho=[1, 14, 2], raiz='//basesComerc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCPSusp    = TagDecimal(nome='vrCPSusp',    tamanho=[1, 14, 2], raiz='//basesComerc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrRatSusp   = TagDecimal(nome='vrRatSusp',   tamanho=[1, 14, 2], raiz='//basesComerc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrSenarSusp = TagDecimal(nome='vrSenarSusp', tamanho=[1, 14, 2], raiz='//basesComerc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<basesComerc>'
        xml += self.indComerc.xml
        xml += self.vrBcComPR.xml
        xml += self.vrCPSusp.xml
        xml += self.vrRatSusp.xml
        xml += self.vrSenarSusp.xml
        xml += '</basesComerc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indComerc.xml = arquivo
            self.vrBcComPR.xml = arquivo
            self.vrCPSusp.xml = arquivo
            self.vrRatSusp.xml = arquivo
            self.vrSenarSusp.xml = arquivo

    xml = property(get_xml, set_xml)


class BasesAquis(XMLNFe):
    def __init__(self):
        super(BasesAquis, self).__init__()
        self.indAquis    = TagCaracter(nome='indAquis',   tamanho=[1, 1],     raiz='//basesAquis', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrAquis    = TagDecimal(nome='vlrAquis',    tamanho=[1, 14, 2], raiz='//basesAquis', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCPDescPR  = TagDecimal(nome='vrCPDescPR',  tamanho=[1, 14, 2], raiz='//basesAquis', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrRatNRet   = TagDecimal(nome='vrRatNRet',   tamanho=[1, 14, 2], raiz='//basesAquis', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSenarNRet = TagDecimal(nome='vrSenarNRet', tamanho=[1, 14, 2], raiz='//basesAquis', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCPCalcPR  = TagDecimal(nome='vrCPCalcPR',  tamanho=[1, 14, 2], raiz='//basesAquis', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrRatDescPR = TagDecimal(nome='vrRatDescPR', tamanho=[1, 14, 2], raiz='//basesAquis', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrRatCalcPR = TagDecimal(nome='vrRatCalcPR', tamanho=[1, 14, 2], raiz='//basesAquis', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSenarDesc = TagDecimal(nome='vrSenarDesc', tamanho=[1, 14, 2], raiz='//basesAquis', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSenarCalc = TagDecimal(nome='vrSenarCalc', tamanho=[1, 14, 2], raiz='//basesAquis', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<basesAquis>'
        xml += self.indAquis.xml
        xml += self.vlrAquis.xml
        xml += self.vrCPDescPR.xml
        xml += self.vrRatNRet.xml
        xml += self.vrSenarNRet.xml
        xml += self.vrCPCalcPR.xml
        xml += self.vrRatDescPR.xml
        xml += self.vrRatCalcPR.xml
        xml += self.vrSenarDesc.xml
        xml += self.vrSenarCalc.xml
        xml += '</basesAquis>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indAquis.xml = arquivo
            self.vlrAquis.xml = arquivo
            self.vrCPDescPR.xml = arquivo
            self.vrRatNRet.xml = arquivo
            self.vrSenarNRet.xml = arquivo
            self.vrCPCalcPR.xml = arquivo
            self.vrRatDescPR.xml = arquivo
            self.vrRatCalcPR.xml = arquivo
            self.vrSenarDesc.xml = arquivo
            self.vrSenarCalc.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoSubstPatrOpPort(XMLNFe):
    def __init__(self):
        super(InfoSubstPatrOpPort, self).__init__()
        self.cnpjOpPortuario = TagCaracter(nome='cnpjOpPortuario', tamanho=[1, 14], raiz='//infoSubstPatrOpPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoSubstPatrOpPort>'
        xml += self.cnpjOpPortuario.xml
        xml += '</infoSubstPatrOpPort>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjOpPortuario.xml = arquivo

    xml = property(get_xml, set_xml)


class BasesAvNPort(XMLNFe):
    def __init__(self):
        super(BasesAvNPort, self).__init__()
        self.vrBcCp00 = TagDecimal(nome='vrBcCp00', tamanho=[1, 14, 2], raiz='//basesANPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcCp15 = TagDecimal(nome='vrBcCp15', tamanho=[1, 14, 2], raiz='//basesANPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcCp20 = TagDecimal(nome='vrBcCp20', tamanho=[1, 14, 2], raiz='//basesANPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcCp25 = TagDecimal(nome='vrBcCp25', tamanho=[1, 14, 2], raiz='//basesANPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcCp13 = TagDecimal(nome='vrBcCp13', tamanho=[1, 14, 2], raiz='//basesANPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcFgts = TagDecimal(nome='vrBcFgts', tamanho=[1, 14, 2], raiz='//basesANPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrDescCP = TagDecimal(nome='vrDescCP', tamanho=[1, 14, 2], raiz='//basesANPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<basesAvNPort>'
        xml += self.vrBcCp00.xml
        xml += self.vrBcCp15.xml
        xml += self.vrBcCp20.xml
        xml += self.vrBcCp25.xml
        xml += self.vrBcCp13.xml
        xml += self.vrBcFgts.xml
        xml += self.vrDescCP.xml
        xml += '</basesAvNPort>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vrBcCp00.xml = arquivo
            self.vrBcCp15.xml = arquivo
            self.vrBcCp20.xml = arquivo
            self.vrBcCp25.xml = arquivo
            self.vrBcCp13.xml = arquivo
            self.vrBcFgts.xml = arquivo
            self.vrDescCP.xml = arquivo

    xml = property(get_xml, set_xml)


class BasesCp(XMLNFe):
    def __init__(self):
        super(BasesCp, self).__init__()
        self.vrBcCp00     = TagDecimal(nome='vrBcCp00'    , tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcCp15     = TagDecimal(nome='vrBcCp15'    , tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcCp20     = TagDecimal(nome='vrBcCp20'    , tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcCp25     = TagDecimal(nome='vrBcCp25'    , tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSuspBcCp00 = TagDecimal(nome='vrSuspBcCp00', tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSuspBcCp15 = TagDecimal(nome='vrSuspBcCp15', tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSuspBcCp20 = TagDecimal(nome='vrSuspBcCp20', tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSuspBcCp25 = TagDecimal(nome='vrSuspBcCp25', tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrDescSest   = TagDecimal(nome='vrDescSest'  , tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCalcSest   = TagDecimal(nome='vrCalcSest'  , tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrDescSenat  = TagDecimal(nome='vrDescSenat' , tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCalcSenat  = TagDecimal(nome='vrCalcSenat' , tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSalFam     = TagDecimal(nome='vrSalFam'    , tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSalMat     = TagDecimal(nome='vrSalMat'    , tamanho=[1, 14, 2], raiz='//basesRemun/basesCp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<basesRemun>'
        xml += self.vrBcCp00.xml
        xml += self.vrBcCp15.xml
        xml += self.vrBcCp20.xml
        xml += self.vrBcCp25.xml
        xml += self.vrSuspBcCp00.xml
        xml += self.vrSuspBcCp15.xml
        xml += self.vrSuspBcCp20.xml
        xml += self.vrSuspBcCp25.xml
        xml += self.vrDescSest.xml
        xml += self.vrCalcSest.xml
        xml += self.vrDescSenat.xml
        xml += self.vrCalcSenat.xml
        xml += self.vrSalFam.xml
        xml += self.vrSalMat.xml
        xml += '</basesRemun>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vrBcCp00.xml = arquivo
            self.vrBcCp15.xml = arquivo
            self.vrBcCp20.xml = arquivo
            self.vrBcCp25.xml = arquivo
            self.vrSuspBcCp00.xml = arquivo
            self.vrSuspBcCp15.xml = arquivo
            self.vrSuspBcCp20.xml = arquivo
            self.vrSuspBcCp25.xml = arquivo
            self.vrDescSest.xml = arquivo
            self.vrCalcSest.xml = arquivo
            self.vrDescSenat.xml = arquivo
            self.vrCalcSenat.xml = arquivo
            self.vrSalFam.xml = arquivo
            self.vrSalMat.xml = arquivo

    xml = property(get_xml, set_xml)


class BasesRemun(XMLNFe):
    def __init__(self):
        super(BasesRemun, self).__init__()
        self.indIncid = TagCaracter(nome='indIncid', tamanho=[1, 1], raiz='//basesRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codCateg = TagDecimal( nome='codCateg', tamanho=[1, 3], raiz='//basesRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.basesCp  = BasesCp()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<basesRemun>'
        xml += self.indIncid.xml
        xml += self.codCateg.xml
        xml += self.basesCp.xml
        xml += '</basesRemun>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indIncid.xml = arquivo
            self.codCateg.xml = arquivo
            self.basesCp.xml = arquivo

    xml = property(get_xml, set_xml)


class DadosOpPort(XMLNFe):
    def __init__(self):
        super(DadosOpPort, self).__init__()
        self.cnpjOpPortuario = TagCaracter(nome='cnpjOpPortuario', tamanho=[1, 14],   raiz='//dadosOpPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.aliqRat         = TagDecimal( nome='aliqRat',         tamanho=[1, 1],    raiz='//dadosOpPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fap             = TagDecimal( nome='fap',             tamanho=[1, 5, 4], raiz='//dadosOpPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.aliqRatAjust    = TagDecimal( nome='aliqRatAjust',    tamanho=[1, 5, 4], raiz='//dadosOpPort', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosOpPort>'
        xml += self.cnpjOpPortuario.xml
        xml += self.aliqRat.xml
        xml += self.fap.xml
        xml += self.aliqRatAjust.xml
        xml += '</dadosOpPort>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjOpPortuario.xml = arquivo
            self.aliqRat.xml = arquivo
            self.fap.xml = arquivo
            self.aliqRatAjust.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoEmprParcial(XMLNFe):
    def __init__(self):
        super(InfoEmprParcial, self).__init__()
        self.tpInscContrat = TagCaracter(nome='tpInscContrat', tamanho=[1, 1],  raiz='//infoEmprParcial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInscContrat = TagCaracter(nome='nrInscContrat', tamanho=[1, 14], raiz='//infoEmprParcial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpInscProp    = TagCaracter(nome='tpInscProp',    tamanho=[1, 1],  raiz='//infoEmprParcial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInscProp    = TagCaracter(nome='nrInscProp',    tamanho=[1, 14], raiz='//infoEmprParcial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoEmprParcial>'
        xml += self.tpInscContrat.xml
        xml += self.nrInscContrat.xml
        xml += self.tpInscProp.xml
        xml += self.nrInscProp.xml
        xml += '</infoEmprParcial>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInscContrat.xml = arquivo
            self.nrInscContrat.xml = arquivo
            self.tpInscProp.xml = arquivo
            self.nrInscProp.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoTercSusp(XMLNFe):
    def __init__(self):
        super(InfoTercSusp, self).__init__()
        self.codTerc = TagCaracter(nome='codTerc', tamanho=[1, 4], raiz='//infoTercSusp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoTercSusp>'
        xml += self.codTerc.xml
        xml += '</infoTercSusp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codTerc.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeLotacao(XMLNFe):
    def __init__(self):
        super(IdeLotacao, self).__init__()
        self.codLotacao   = TagCaracter(nome='codLotacao',   tamanho=[1, 30], raiz='//ideLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fpas         = TagCaracter(nome='fpas',         tamanho=[1, 3],  raiz='//ideLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codTercs     = TagCaracter(nome='codTercs',     tamanho=[1, 4],  raiz='//ideLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codTercsSusp = TagCaracter(nome='codTercSsusp', tamanho=[1, 4],  raiz='//ideLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.infoTercSusp = []
        self.infoEmprParcial = []
        self.dadosOpPort = []
        self.basesRemun = []
        self.basesAvNPort = []
        self.infoSubstPatrOpPort = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideLotacao>'
        xml += self.codLotacao.xml
        xml += self.fpas.xml
        xml += self.codTercs.xml
        xml += self.codTercsSusp.xml
        if len(self.infoTercSusp) > 0:
            for i in self.infoTercSusp:
                xml += i.xml
        if len(self.infoEmprParcial) > 0:
            for i in self.infoEmprParcial:
                xml += i.xml
        if len(self.dadosOpPort) > 0:
            for i in self.dadosOpPort:
                xml += i.xml
        if len(self.basesRemun) > 0:
            for i in self.basesRemun:
                xml += i.xml
        if len(self.basesAvNPort) > 0:
            for i in self.basesAvNPort:
                xml += i.xml
        if len(self.infoSubstPatrOpPort) > 0:
            for i in self.infoSubstPatrOpPort:
                xml += i.xml
        xml += '</ideLotacao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codLotacao.xml = arquivo
            self.fpas.xml = arquivo
            self.codTercs.xml = arquivo
            self.codTercsSusp.xml = arquivo
            self.infoTercSusp = self.le_grupo('//ideLotacao/infoTercSusp', InfoTercSusp, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoEmprParcial = self.le_grupo('//ideLotacao/infoEmprParcial', InfoEmprParcial, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.dadosOpPort = self.le_grupo('//ideLotacao/dadosOpPort', DadosOpPort, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.basesRemun = self.le_grupo('//ideLotacao/basesRemun', BasesRemun, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.basesAvNPort = self.le_grupo('//ideLotacao/basesAvNPort', BasesAvNPort, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoSubstPatrOpPort = self.le_grupo('//ideLotacao/infoSubstPatrOpPort', InfoSubstPatrOpPort, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoComplObra(XMLNFe):
    def __init__(self):
        super(InfoComplObra, self).__init__()
        self.indSubstPatrObra = TagCaracter(nome='indSubstPatrObra', tamanho=[1, 1], raiz='//infoComplObra', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoComplObra>'
        xml += self.indSubstPatrObra.xml
        xml += '</infoComplObra>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indSubstPatrObra.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoEstab(XMLNFe):
    def __init__(self):
        super(InfoEstab, self).__init__()
        self.cnaePrep      = TagCaracter(nome='cnaePrep',     tamanho=[1, 7],    raiz='//infoEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.aliqRat       = TagDecimal( nome='aliqRat',      tamanho=[1, 1],    raiz='//infoEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fap           = TagDecimal( nome='fap',          tamanho=[1, 5, 4], raiz='//infoEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.aliqRatAjust  = TagDecimal( nome='aliqRatAjust', tamanho=[1, 5, 4], raiz='//infoEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoComplObra = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoEstab>'
        xml += self.cnaePrep.xml
        xml += self.aliqRat.xml
        xml += self.fap.xml
        xml += self.aliqRatAjust.xml
        if len(self.infoComplObra):
            for i in self.infoComplObra:
                xml += i.xml
        xml += '</infoEstab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnaePrep.xml = arquivo
            self.aliqRat.xml = arquivo
            self.fap.xml = arquivo
            self.aliqRatAjust.xml = arquivo
            self.infoComplObra = self.le_grupo('//infoEstab/infoComplObra', InfoComplObra, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEstab(XMLNFe):
    def __init__(self):
        super(IdeEstab, self).__init__()
        self.tpInsc      = TagCaracter(nome='tpInsc', tamanho=[1, 1],  raiz='//ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc      = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoEstab   = []
        self.ideLotacao  = []
        self.basesAquis  = []
        self.basesComerc = []
        self.infoCREstab = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstab>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        if len(self.infoEstab) > 0:
            for i in self.infoEstab:
                xml += i.xml
        if len(self.ideLotacao) > 0:
            for i in self.ideLotacao:
                xml += i.xml
        if len(self.basesAquis) > 0:
            for b in self.basesAquis:
                xml += b.xml
        if len(self.basesComerc) > 0:
            for b in self.basesComerc:
                xml += b.xml
        if len(self.infoCREstab) > 0:
            for i in self.infoCREstab:
                xml += i.xml
        xml += '</ideEstab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.infoEstab = self.le_grupo('//ideEstab/infoEstab', InfoEstab, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.ideLotacao = self.le_grupo('//ideEstab/ideLotacao', IdeLotacao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.basesAquis = self.le_grupo('//ideEstab/basesAquis', BasesAquis, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.basesComerc = self.le_grupo('//ideEstab/basesComerc', BasesComerc, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoAtConc(XMLNFe):
    def __init__(self):
        super(InfoAtConc, self).__init__()
        self.fatorMes = TagCaracter(nome='fatorMes', tamanho=[1, 1], raiz='//infoAtConc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fator13  = TagCaracter(nome='fator13',  tamanho=[1, 1], raiz='//infoAtConc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoAtConc>'
        xml += self.fatorMes.xml
        xml += self.fator13.xml
        xml += '</infoAtConc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.fatorMes.xml = arquivo
            self.fator13.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoPJ(XMLNFe):
    def __init__(self):
        super(InfoPJ, self).__init__()
        self.indCoop        = TagCaracter(nome='indCoop',        tamanho=[1, 1],    raiz='//infoPJ', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indConstr      = TagCaracter(nome='indConstr',      tamanho=[1, 1],    raiz='//infoPJ', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indSubstPatr   = TagCaracter(nome='indSubstPatr',   tamanho=[1, 1],    raiz='//infoPJ', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.percRedContrib = TagDecimal( nome='percRedContrib', tamanho=[1, 5, 2], raiz='//infoPJ', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.infoAtConc     = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPJ>'
        xml += self.indCoop.xml
        xml += self.indConstr.xml
        xml += self.indSubstPatr.xml
        xml += self.percRedContrib.xml
        if len(self.infoAtConc) > 0:
            for p in self.infoAtConc:
                xml += p.xml
        xml += '</infoPJ>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indCoop.xml = arquivo
            self.indConstr.xml = arquivo
            self.indSubstPatr.xml = arquivo
            self.percRedContrib.xml = arquivo
            self.infoAtConc = self.le_grupo('//infoPJ/infoAtConc', InfoAtConc, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoContrib(XMLNFe):
    def __init__(self):
        super(InfoContrib, self).__init__()
        self.classTrib = TagCaracter(nome='classTrib', tamanho=[1, 2],     raiz='//eSocial/evtCS/infoCS/infoContrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoPJ    = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoContrib>'
        xml += self.classTrib.xml
        if len(self.infoPJ) > 0:
            for i in self.infoPJ:
                xml += i.xml
        xml += '</infoContrib>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.classTrib.xml = arquivo
            self.infoPJ = self.le_grupo('//eSocial/evtCS/infoCS/infoContrib/infoPJ', InfoPJ, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoCPSeg(XMLNFe):
    def __init__(self):
        super(InfoCPSeg, self).__init__()
        self.vrDescCP = TagDecimal(nome='vrDescCP', tamanho=[1, 14, 2], raiz='//infoCPSeg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCpSeg  = TagDecimal(nome='vrCpSeg',  tamanho=[1, 14, 2], raiz='//infoCPSeg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCPSeg>'
        xml += self.vrDescCP.xml
        xml += self.vrCpSeg.xml
        xml += '</infoCPSeg>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vrDescCP.xml = arquivo
            self.vrCpSeg.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoCS(XMLNFe):
    def __init__(self):
        super(InfoCS, self).__init__()
        self.nrRecArqBase  = TagCaracter(nome='nrRecArqBase', tamanho=[1, 40], raiz='//eSocial/evtCS/infoCS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indExistInfo  = TagCaracter(nome='indExistInfo', tamanho=[1, 1],  raiz='//eSocial/evtCS/infoCS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoCPSeg     = []
        self.infoContrib   = InfoContrib()
        self.ideEstab      = []
        self.infoCRContrib = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCS>'
        xml += self.nrRecArqBase.xml
        xml += self.indExistInfo.xml
        if len(self.infoCPSeg) > 0:
            for i in self.infoCPSeg:
                xml += i.xml
        xml += self.infoContrib.xml
        if len(self.ideEstab) > 0:
            for i in self.ideEstab:
                xml += i.xml
        if len(self.infoCRContrib) > 0:
            for i in self.infoCRContrib:
                xml += i.xml
        xml += '</infoCS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRecArqBase.xml = arquivo
            self.indExistInfo.xml = arquivo
            self.infoCPSeg = self.le_grupo('//eSocial/evtCS/infoCS/infoCPSeg', InfoCPSeg, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoContrib.xml = arquivo
            self.ideEstab = self.le_grupo('//eSocial/evtCS/infoCS/ideEstab', IdeEstab, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoCRContrib = self.le_grupo('//eSocial/evtCS/infoCS/infoCRContrib', InfoCRContrib, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1, 1],  raiz='//eSocial/evtCS/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtCS/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEmpregador>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideEmpregador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEvento(XMLNFe):
    def __init__(self):
        super(IdeEvento, self).__init__()
        self.indApuracao  = TagCaracter(nome='indApuracao',  tamanho=[1,  1], raiz='//eSocial/evtCS/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.perApur      = TagCaracter(nome='perApur',      tamanho=[1,  7], raiz='//eSocial/evtCS/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.indApuracao.xml
        xml += self.perApur.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indApuracao.xml = arquivo
            self.perApur.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtCS(XMLNFe):
    def __init__(self):
        super(EvtCS, self).__init__()
        self.Id = TagCaracter(nome='evtCS', propriedade='Id', raiz='//eSocial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.infoCS = InfoCS()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.infoCS.xml
        xml += '</evtCS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoCS.xml = arquivo

    xml = property(get_xml, set_xml)


class S5011(XMLNFe):
    def __init__(self):
        super(S5011, self).__init__()
        self.evtCS = EvtCS()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtCS.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        self.Signature = Signature()
        self.evento = self.evtCS
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtCS.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtCS.Id.valor
        xml += self.Signature.xml
        xml += '</eSocial>'

        # Define o método de assinatura
        # self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtCS.xml = arquivo
            self.Signature.xml = self._le_noh('//sig:Signature')

    def gera_id_evento(self, data_hora, sequencia=False):
        #A identificação única do evento (Id) é composta por 36 caracteres, conforme o que segue: IDTNNNNNNNNNNNNNNAAAAMMDDHHMMSSQQQQQ
        #ID - Texto Fixo "ID";
        #T - Tipo de Inscrição do Empregador (1 - CNPJ; 2 - CPF);
        #NNNNNNNNNNNNNN - Número do CNPJ ou CPF do empregador - Completar com
        #zeros à direita. No caso de pessoas jurídicas, o CNPJ informado deve conter 8 ou 14
        #posições de acordo com o enquadramento do contribuinte para preenchimento do campo
        #{ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se
        #necessário.
        #AAAAMMDD - Ano, mês e dia da geração do evento;
        #HHMMSS - Hora, minuto e segundo da geração do evento;
        #QQQQQ - Número sequencial da chave. Incrementar somente quando ocorrer geração de
        #eventos na mesma data/hora, completando com zeros à esquerda.
        #OBS.: No caso de pessoas jurídicas, o CNPJ informado deverá conter 8 ou 14 posições de
        #acordo com o enquadramento do contribuinte para preenchimento do campo {ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se necessário.

        if not sequencia:
            sequencia=1

        id_evento = 'ID'
        id_evento += self.tpInsc
        id_evento += self.nrInsc[0:8] + '000000'
        id_evento += data_hora
        id_evento += str(sequencia).zfill(5)

        # Define o Id
        #
        self.evtCS.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
