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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtPgtos/v02_04_02'


class IdePgtoExt(XMLNFe):
    def __init__(self):
        super(IdePgtoExt, self).__init__()
        self.codPais   = TagCaracter(nome='codPais',   tamanho=[1, 3],     raiz='//idePgtoExt/idePais', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indNIF    = TagCaracter(nome='indNIF',    tamanho=[1, 1],     raiz='//idePgtoExt/idePais', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nifBenef  = TagCaracter(nome='nifBenef',  tamanho=[1, 1],     raiz='//idePgtoExt/idePais', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dscLograd = TagCaracter(nome='dscLograd', tamanho=[1, 80],    raiz='//idePgtoExt/endExt',  namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrLograd  = TagCaracter(nome='nrLograd',  tamanho=[1, 10],    raiz='//idePgtoExt/endExt',  namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.complem   = TagCaracter(nome='complem',   tamanho=[1, 30],    raiz='//idePgtoExt/endExt',  namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.bairro    = TagCaracter(nome='bairro',    tamanho=[1, 60],    raiz='//idePgtoExt/endExt',  namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmCid     = TagCaracter(nome='nmCid',     tamanho=[1, 50],    raiz='//idePgtoExt/endExt',  namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codPostal = TagCaracter(nome='codPostal', tamanho=[1, 12],    raiz='//idePgtoExt/endExt',  namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePgtoExt>'
        xml += '<idePais>'
        xml += self.codPais.xml
        xml += self.indNIF.xml
        xml += self.nifBenef.xml
        xml += '</idePais>'
        xml += '<endExt>'
        xml += self.dscLograd.xml
        xml += self.nrLograd.xml
        xml += self.complem.xml
        xml += self.bairro.xml
        xml += self.nmCid.xml
        xml += self.codPostal.xml
        xml += '</endExt>'
        xml += '</idePgtoExt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codPais.xml = arquivo
            self.indNIF.xml = arquivo
            self.nifBenef.xml = arquivo
            self.dscLograd.xml = arquivo
            self.nrLograd.xml = arquivo
            self.complem.xml = arquivo
            self.bairro.xml = arquivo
            self.nmCid.xml = arquivo
            self.codPostal.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoPgtoAnt(XMLNFe):
    def __init__(self):
        super(InfoPgtoAnt, self).__init__()
        self.tpBcIRRF = TagCaracter(nome='tpBcIRRF', tamanho=[1, 2],     raiz='//infoPgtoAnt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcIRRF = TagDecimal( nome='vrBcIRRF', tamanho=[1, 14, 2], raiz='//infoPgtoAnt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPgtoAnt>'
        xml += self.tpBcIRRF.xml
        xml += self.vrBcIRRF.xml
        xml += '</infoPgtoAnt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpBcIRRF.xml = arquivo
            self.vrBcIRRF.xml = arquivo

    xml = property(get_xml, set_xml)


class DetPgtoAnt(XMLNFe):
    def __init__(self):
        super(DetPgtoAnt, self).__init__()
        self.codCateg  = TagCaracter(nome='codCateg',  tamanho=[1, 3],     raiz='//detPgtoAnt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoPgtoAnt = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detPgtoAnt>'
        xml += self.codCateg.xml
        if len(self.infoPgtoAnt) > 0 :
            for r in self.infoPgtoAnt:
                xml += r.xml
        xml += '</detPgtoAnt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codCateg.xml = arquivo
            self.infoPgtoAnt = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoAnt/infoPgtoAnt', InfoPgtoAnt, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class DetRubrFerPenAlim(XMLNFe):
    def __init__(self):
        super(DetRubrFerPenAlim, self).__init__()
        self.cpfBenef      = TagCaracter(nome='cpfBenef',      tamanho=[1, 11],    raiz='//penAlim', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtNasctoBenef = TagData(    nome='dtNasctoBenef',                     raiz='//penAlim', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmBenefic     = TagCaracter(nome='nmBenefic',     tamanho=[1, 70],    raiz='//penAlim', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrPensao     = TagDecimal( nome='vlrPensao',     tamanho=[1, 14, 2], raiz='//penAlim', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<penAlim>'
        xml += self.cpfBenef.xml
        xml += self.dtNasctoBenef.xml
        xml += self.nmBenefic.xml
        xml += self.vlrPensao.xml
        xml += '</penAlim>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfBenef.xml = arquivo
            self.dtNasctoBenef.xml = arquivo
            self.nmBenefic.xml = arquivo
            self.vlrPensao.xml = arquivo

    xml = property(get_xml, set_xml)


class DetRubrFer(XMLNFe):
    def __init__(self):
        super(DetRubrFer, self).__init__()
        self.codRubr    = TagCaracter(nome='codRubr',    tamanho=[1, 30],    raiz='//detRubrFer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideTabRubr = TagCaracter(nome='ideTabRubr', tamanho=[1, 8],     raiz='//detRubrFer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.qtdRubr    = TagDecimal( nome='qtdRubr',    tamanho=[1, 6, 2],  raiz='//detRubrFer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.fatorRubr  = TagDecimal( nome='fatorRubr' , tamanho=[1, 5, 2],  raiz='//detRubrFer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrUnit     = TagDecimal( nome='vrUnit'    , tamanho=[1, 14, 2], raiz='//detRubrFer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrRubr     = TagDecimal( nome='vrRubr'    , tamanho=[1, 14, 2], raiz='//detRubrFer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.penAlim    = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detRubrFer>'
        xml += self.codRubr.xml
        xml += self.ideTabRubr.xml
        xml += self.qtdRubr.xml
        xml += self.fatorRubr.xml
        xml += self.vrUnit.xml
        xml += self.vrRubr.xml
        if len(self.penAlim) > 0:
            for p in self.penAlim:
                xml += p.xml
        xml += '</detRubrFer>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codRubr.xml = arquivo
            self.ideTabRubr.xml = arquivo
            self.qtdRubr.xml = arquivo
            self.fatorRubr.xml = arquivo
            self.vrUnit.xml = arquivo
            self.vrRubr.xml = arquivo
            self.penAlim = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoFer/detRubrFer/penAlim', DetRubrFerPenAlim, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class DetPgtoFer(XMLNFe):
    def __init__(self):
        super(DetPgtoFer, self).__init__()
        self.codCateg  = TagCaracter(nome='codCateg',  tamanho=[1, 3],     raiz='//detPgtoFer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.matricula = TagCaracter(nome='matricula', tamanho=[1, 30],    raiz='//detPgtoFer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtIniGoz  = TagData(    nome='dtIniGoz',                      raiz='//detPgtoFer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.qtDias    = TagCaracter(nome='qtDias',    tamanho=[1, 2],     raiz='//detPgtoFer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrLiq     = TagDecimal( nome='vrLiq',     tamanho=[1, 14, 2], raiz='//detPgtoFer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.detRubrFer = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detPgtoFer>'
        xml += self.codCateg.xml
        xml += self.matricula.xml
        xml += self.dtIniGoz.xml
        xml += self.qtDias.xml
        xml += self.vrLiq.xml
        if len(self.detRubrFer) > 0 :
            for r in self.detRubrFer:
                xml += r.xml
        xml += '</detPgtoFer>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codCateg.xml = arquivo
            self.matricula.xml = arquivo
            self.dtIniGoz.xml = arquivo
            self.qtDias.xml = arquivo
            self.vrLiq.xml = arquivo
            self.detRubrFer = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoFer/detRubrFer', DetRubrFer, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class DetPgtoBenPrInfoPgtoParc(XMLNFe):
    def __init__(self):
        super(DetPgtoBenPrInfoPgtoParc, self).__init__()
        self.codRubr    = TagCaracter(nome='codRubr',    tamanho=[1, 30],    raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideTabRubr = TagCaracter(nome='ideTabRubr', tamanho=[1, 8],     raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.qtdRubr    = TagDecimal( nome='qtdRubr',    tamanho=[1, 6, 2],  raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.fatorRubr  = TagDecimal( nome='fatorRubr' , tamanho=[1, 5, 2],  raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrUnit     = TagDecimal( nome='vrUnit'    , tamanho=[1, 14, 2], raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrRubr     = TagDecimal( nome='vrRubr'    , tamanho=[1, 14, 2], raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPgtoParc>'
        xml += self.codRubr.xml
        xml += self.ideTabRubr.xml
        xml += self.qtdRubr.xml
        xml += self.fatorRubr.xml
        xml += self.vrUnit.xml
        xml += self.vrRubr.xml
        xml += '</infoPgtoParc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codRubr.xml = arquivo
            self.ideTabRubr.xml = arquivo
            self.qtdRubr.xml = arquivo
            self.fatorRubr.xml = arquivo
            self.vrUnit.xml = arquivo
            self.vrRubr.xml = arquivo

    xml = property(get_xml, set_xml)


class DetPgtoBenPrRetPgtoTot(XMLNFe):
    def __init__(self):
        super(DetPgtoBenPrRetPgtoTot, self).__init__()
        self.codRubr    = TagCaracter(nome='codRubr',    tamanho=[1, 30],    raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideTabRubr = TagCaracter(nome='ideTabRubr', tamanho=[1, 8],     raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.qtdRubr    = TagDecimal( nome='qtdRubr',    tamanho=[1, 6, 2],  raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.fatorRubr  = TagDecimal( nome='fatorRubr',  tamanho=[1, 5, 2],  raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrUnit     = TagCaracter(nome='vrUnit',     tamanho=[1, 40],    raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrRubr     = TagDecimal( nome='vrRubr',     tamanho=[1, 14, 2], raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<retPgtoTot>'
        xml += self.codRubr.xml
        xml += self.ideTabRubr.xml
        xml += self.qtdRubr.xml
        xml += self.fatorRubr.xml
        xml += self.vrUnit.xml
        xml += self.vrRubr.xml
        xml += '</retPgtoTot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codRubr.xml = arquivo
            self.ideTabRubr.xml = arquivo
            self.qtdRubr.xml = arquivo
            self.fatorRubr.xml = arquivo
            self.vrUnit.xml = arquivo
            self.vrRubr.xml = arquivo

    xml = property(get_xml, set_xml)


class DetPgtoBenPr(XMLNFe):
    def __init__(self):
        super(DetPgtoBenPr, self).__init__()
        self.perRef    = TagCaracter(nome='perRef',    tamanho=[1, 7],     raiz='//detPgtoBenPr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideDmDev  = TagCaracter(nome='ideDmDev',  tamanho=[1, 30],    raiz='//detPgtoBenPr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indPgtoTt = TagCaracter(nome='indPgtoTt', tamanho=[1, 1],     raiz='//detPgtoBenPr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrLiq     = TagDecimal( nome='vrLiq',     tamanho=[1, 14, 2], raiz='//detPgtoBenPr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.retPgtoTot   = []
        self.infoPgtoParc = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detPgtoBenPr>'
        xml += self.perRef.xml
        xml += self.ideDmDev.xml
        xml += self.indPgtoTt.xml
        xml += self.vrLiq.xml
        if len(self.retPgtoTot) > 0 :
            for p in self.retPgtoTot:
                xml += p.xml
        if len(self.infoPgtoParc) > 0:
            for p in self.infoPgtoParc:
                xml += p.xml
        xml += '</detPgtoBenPr>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.perRef.xml = arquivo
            self.ideDmDev.xml = arquivo
            self.indPgtoTt.xml = arquivo
            self.vrLiq.xml = arquivo
            self.retPgtoTot = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoBenPr/retPgtoTot', DetPgtoBenPrRetPgtoTot, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoPgtoParc = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoBenPr/infoPgtoParc', DetPgtoBenPrInfoPgtoParc, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoPgtoParc(XMLNFe):
    def __init__(self):
        super(InfoPgtoParc, self).__init__()
        self.matricula  = TagCaracter(nome='matricula',  tamanho=[1, 30],    raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codRubr    = TagCaracter(nome='codRubr',    tamanho=[1, 30],    raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideTabRubr = TagCaracter(nome='ideTabRubr', tamanho=[1, 8],     raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.qtdRubr    = TagDecimal( nome='qtdRubr',    tamanho=[1, 6, 2],  raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.fatorRubr  = TagDecimal( nome='fatorRubr' , tamanho=[1, 5, 2],  raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrUnit     = TagDecimal( nome='vrUnit'    , tamanho=[1, 14, 2], raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrRubr     = TagDecimal( nome='vrRubr'    , tamanho=[1, 14, 2], raiz='//infoPgtoParc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPgtoParc>'
        xml += self.matricula.xml
        xml += self.codRubr.xml
        xml += self.ideTabRubr.xml
        xml += self.qtdRubr.xml
        xml += self.fatorRubr.xml
        xml += self.vrUnit.xml
        xml += self.vrRubr.xml
        xml += '</infoPgtoParc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.matricula.xml = arquivo
            self.codRubr.xml = arquivo
            self.ideTabRubr.xml = arquivo
            self.qtdRubr.xml = arquivo
            self.fatorRubr.xml = arquivo
            self.vrUnit.xml = arquivo
            self.vrRubr.xml = arquivo

    xml = property(get_xml, set_xml)


class PenAlim(XMLNFe):
    def __init__(self):
        super(PenAlim, self).__init__()
        self.cpfBenef      = TagCaracter(nome='cpfBenef',      tamanho=[1, 11],    raiz='//penAlim', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtNasctoBenef = TagData(    nome='dtNasctoBenef',                     raiz='//penAlim', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmBenefic     = TagCaracter(nome='nmBenefic',     tamanho=[1, 70],    raiz='//penAlim', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrPensao     = TagDecimal( nome='vlrPensao',     tamanho=[1, 14, 2], raiz='//penAlim', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<penAlim>'
        xml += self.cpfBenef.xml
        xml += self.dtNasctoBenef.xml
        xml += self.nmBenefic.xml
        xml += self.vlrPensao.xml
        xml += '</penAlim>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfBenef.xml = arquivo
            self.dtNasctoBenef.xml = arquivo
            self.nmBenefic.xml = arquivo
            self.vlrPensao.xml = arquivo

    xml = property(get_xml, set_xml)


class RetPgtoTot(XMLNFe):
    def __init__(self):
        super(RetPgtoTot, self).__init__()
        self.codRubr    = TagCaracter(nome='codRubr',    tamanho=[1, 30],    raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideTabRubr = TagCaracter(nome='ideTabRubr', tamanho=[1, 8],     raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.qtdRubr    = TagDecimal( nome='qtdRubr',    tamanho=[1, 6, 2],  raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.fatorRubr  = TagDecimal( nome='fatorRubr',  tamanho=[1, 5, 2],  raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrUnit     = TagCaracter(nome='vrUnit',     tamanho=[1, 40],    raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrRubr     = TagDecimal( nome='vrRubr',     tamanho=[1, 14, 2], raiz='//retPgtoTot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.penAlim    = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<retPgtoTot>'
        xml += self.codRubr.xml
        xml += self.ideTabRubr.xml
        xml += self.qtdRubr.xml
        xml += self.fatorRubr.xml
        xml += self.vrUnit.xml
        xml += self.vrRubr.xml
        if len(self.penAlim) > 0:
            for p in self.penAlim:
                xml += p.xml
        xml += '</retPgtoTot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codRubr.xml = arquivo
            self.ideTabRubr.xml = arquivo
            self.qtdRubr.xml = arquivo
            self.fatorRubr.xml = arquivo
            self.vrUnit.xml = arquivo
            self.vrRubr.xml = arquivo
            self.penAlim = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoFl/retPgtoTot/penAlim', PenAlim, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class DetPgtoFl(XMLNFe):
    def __init__(self):
        super(DetPgtoFl, self).__init__()
        self.perRef    = TagCaracter(nome='perRef',     tamanho=[1, 7],     raiz='//detPgtoFl', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.ideDmDev  = TagCaracter(nome='ideDmDev',   tamanho=[1, 30],    raiz='//detPgtoFl', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indPgtoTt = TagCaracter(nome='indPgtoTt',  tamanho=[1, 1],     raiz='//detPgtoFl', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrLiq     = TagDecimal( nome='vrLiq',      tamanho=[1, 14, 2], raiz='//detPgtoFl', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrRecArq  = TagCaracter(nome='nrRecArq',   tamanho=[1, 40],    raiz='//detPgtoFl', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.retPgtoTot = []
        self.infoPgtoParc = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detPgtoFl>'
        xml += self.perRef.xml
        xml += self.ideDmDev.xml
        xml += self.indPgtoTt.xml
        xml += self.vrLiq.xml
        xml += self.nrRecArq.xml
        if len(self.retPgtoTot) > 0:
            for p in self.retPgtoTot:
                xml += p.xml
        if len(self.infoPgtoParc) > 0:
            for p in self.infoPgtoParc:
                xml += p.xml
        xml += '</detPgtoFl>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.perRef.xml = arquivo
            self.ideDmDev.xml = arquivo
            self.indPgtoTt.xml = arquivo
            self.vrLiq.xml = arquivo
            self.nrRecArq.xml = arquivo
            self.retPgtoTot = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoFl/retPgtoTot', RetPgtoTot, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoPgtoParc = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoFl/infoPgtoParc', InfoPgtoParc, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoPgto(XMLNFe):
    def __init__(self):
        super(InfoPgto, self).__init__()
        self.dtPgto    = TagData(    nome='dtPgto',                   raiz='//infoPgto', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpPgto    = TagCaracter(nome='tpPgto',   tamanho=[1, 2], raiz='//infoPgto', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indResBr  = TagCaracter(nome='indResBr', tamanho=[1, 1], raiz='//infoPgto', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.detPgtoFl    = []
        self.detPgtoBenPr = []
        self.detPgtoFer   = []
        self.detPgtoAnt   = []
        self.idePgtoExt   = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPgto>'
        xml += self.dtPgto.xml
        xml += self.tpPgto.xml
        xml += self.indResBr.xml
        if len(self.detPgtoFl) > 0:
            for p in self.detPgtoFl:
                xml += p.xml
        if len(self.detPgtoBenPr) > 0:
            for p in self.detPgtoBenPr:
                xml += p.xml
        if len(self.detPgtoFer) > 0:
            for p in self.detPgtoFer:
                xml += p.xml
        if len(self.detPgtoAnt) > 0:
            for p in self.detPgtoAnt:
                xml += p.xml
        if len(self.idePgtoExt) > 0:
            for p in self.idePgtoExt:
                xml += p.xml
        xml += '</infoPgto>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtPgto.xml = arquivo
            self.tpPgto.xml = arquivo
            self.indResBr.xml = arquivo
            self.detPgtoFl = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoFl', DetPgtoFl, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.detPgtoBenPr = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoBenPr', DetPgtoBenPr, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.detPgtoFer = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoFer', DetPgtoFer, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.detPgtoAnt = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/detPgtoAnt', DetPgtoAnt, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.idePgtoExt = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto/idePgtoExt', IdePgtoExt, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeBenef(XMLNFe):
    def __init__(self):
        super(IdeBenef, self).__init__()
        self.cpfBenef       = TagCaracter(nome='cpfBenef', tamanho=[1, 11],    raiz='//eSocial/evtPgtos/ideBenef',      namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrDedDep       = TagDecimal( nome='vrDedDep', tamanho=[1, 14, 2], raiz='//eSocial/evtPgtos/ideBenef/deps', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.infoPgto       = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideBenef>'
        xml += self.cpfBenef.xml
        if self.vrDedDep.valor:
            xml += '<deps>'
            xml += self.vrDedDep.xml
            xml += '</deps>'
        if len(self.infoPgto) > 0:
            for p in self.infoPgto:
                xml += p.xml
        xml += '</ideBenef>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfBenef.xml = arquivo
            self.vrDedDep.xml = arquivo
            self.infoPgto = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto', InfoPgto, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1, 1],  raiz='//eSocial/evtPgtos/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtPgtos/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif    = TagInteiro( nome='indRetif',    tamanho=[1,  1], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrRecibo    = TagCaracter(nome='nrRecibo',    tamanho=[1, 40], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indApuracao = TagCaracter(nome='indApuracao', tamanho=[1,  1], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.perApur     = TagCaracter(nome='perApur',     tamanho=[1,  7], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpAmb       = TagInteiro( nome='tpAmb',       tamanho=[1,  1], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi     = TagInteiro( nome='procEmi',     tamanho=[1,  1], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc     = TagCaracter(nome='verProc',     tamanho=[1, 20], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.indRetif.xml
        xml += self.nrRecibo.xml
        xml += self.indApuracao.xml
        xml += self.perApur.xml
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indRetif.xml = arquivo
            self.nrRecibo.xml = arquivo
            self.indApuracao.xml = arquivo
            self.perApur.xml = arquivo
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtPgtos(XMLNFe):
    def __init__(self):
        super(EvtPgtos, self).__init__()
        self.Id = TagCaracter(nome='evtPgtos', propriedade='Id', raiz='//eSocial/evtPgtos', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideBenef = IdeBenef()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideBenef.xml
        xml += '</evtPgtos>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideBenef.xml = arquivo

    xml = property(get_xml, set_xml)


class S1210(XMLNFe):
    def __init__(self):
        super(S1210, self).__init__()
        self.evtPgtos = EvtPgtos()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtPgtos.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtPgtos
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtPgtos.xml

        #
        # Define a URI a ser assinada
        #
        # self.Signature.URI = '#' + self.evtInfoEmpregador.Id.valor
        # xml += self.Signature.xml
        xml += '</eSocial>'

        # Define o método de assinatura
        # self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtPgtos.xml = arquivo
            # self.Signature.xml = self._le_noh('//eSocial/sig:Signature')

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
        self.evtPgtos.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
