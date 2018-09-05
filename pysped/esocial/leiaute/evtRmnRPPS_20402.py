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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtRmnRPPS/v02_04_02'


class RemunPerAntItensRemun(XMLNFe):
    def __init__(self):
        super(RemunPerAntItensRemun, self).__init__()
        self.codRubr    = TagCaracter(nome='codRubr',    tamanho=[1, 30],    raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideTabRubr = TagCaracter(nome='ideTabRubr', tamanho=[1, 8],     raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.qtdRubr    = TagInteiro( nome='qtdRubr',    tamanho=[1, 6],     raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.fatorRubr  = TagInteiro( nome='fatorRubr',  tamanho=[1, 5, 2],  raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrUnit     = TagDecimal( nome='vrUnit',     tamanho=[1, 14, 2], raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrRubr     = TagDecimal( nome='vrRubr',     tamanho=[1, 14, 2], raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<itensRemun>'
        xml += self.codRubr.xml
        xml += self.ideTabRubr.xml
        xml += self.qtdRubr.xml
        xml += self.fatorRubr.xml
        xml += self.vrUnit.xml
        xml += self.vrRubr.xml
        xml += '</itensRemun>'
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


class RemunPerAnt(XMLNFe):
    def __init__(self):
        super(RemunPerAnt, self).__init__()
        self.matricula = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//ideEstab/remunPerApur', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg  = TagCaracter(nome='codCateg',  tamanho=[1, 3],  raiz='//ideEstab/remunPerApur', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.itensRemun     = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<remunPerAnt>'
        xml += self.matricula.xml
        xml += self.codCateg.xml
        if len(self.itensRemun) > 0:
            for r in self.itensRemun:
                xml += r.xml
        xml += '</remunPerAnt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.matricula.xml = arquivo
            self.codCateg.xml = arquivo
            self.itensRemun = self.le_grupo('//eSocial/evtRmnRPPS/dmDev/infoPerAnt/ideADC/idePeriodo/ideEstab/remunPerAnt/itensRemun', RemunPerAntItensRemun, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdePeriodoIdeEstab(XMLNFe):
    def __init__(self):
        super(IdePeriodoIdeEstab, self).__init__()
        self.tpInsc      = TagCaracter(nome='tpInsc',     tamanho=[1, 1],  raiz='//ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc      = TagCaracter(nome='nrInsc',     tamanho=[1, 15], raiz='//ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.remunPerAnt = RemunPerAnt()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePeriodo>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.remunPerAnt.xml
        xml += '</idePeriodo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.remunPerAnt.xml = arquivo

    xml = property(get_xml, set_xml)


class IdePeriodo(XMLNFe):
    def __init__(self):
        super(IdePeriodo, self).__init__()
        self.perRef   = TagCaracter(nome='perRef', tamanho=[1, 7], raiz='//idePeriodo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEstab = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePeriodo>'
        xml += self.perRef.xml
        if len(self.ideEstab) > 0:
            for e in self.ideEstab:
                xml += e.xml
        xml += '</idePeriodo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.perRef.xml = arquivo
            self.ideEstab = self.le_grupo('//eSocial/evtRmnRPPS/dmDev/infoPerAnt/ideADC/idePeriodo/ideEstab', IdePeriodoIdeEstab, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeADC(XMLNFe):
    def __init__(self):
        super(IdeADC, self).__init__()
        self.dtLei = TagData(    nome='dtLei',                   raiz='//ideADC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrLei = TagCaracter(nome='nrLei', tamanho=[1, 12],  raiz='//ideADC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtEf  = TagData(    nome='dtEf',                    raiz='//ideADC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.idePeriodo = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideADC>'
        xml += self.dtLei.xml
        xml += self.nrLei.xml
        xml += self.dtEf.xml
        if len(self.idePeriodo) > 0:
            for p in self.idePeriodo:
                xml += p.xml
        xml += '</ideADC>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.idePeriodo = self.le_grupo('//eSocial/evtRmnRPPS/dmDev/infoPerAnt/ideADC/idePeriodo', IdePeriodo, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoPerAnt(XMLNFe):
    def __init__(self):
        super(InfoPerAnt, self).__init__()
        self.ideADC = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPerAnt>'
        if len(self.ideADC) > 0:
            for i in self.ideADC:
                xml += i.xml
        xml += '</infoPerAnt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideADC = self.le_grupo('//eSocial/evtRmnRPPS/dmDev/infoPerAnt/ideADC', IdeADC, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class DetPlano(XMLNFe):
    def __init__(self):
        super(DetPlano, self).__init__()
        self.tpDep    = TagCaracter(nome='tpDep',    tamanho=[1, 1],     raiz='//detPlano', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cpfDep   = TagCaracter(nome='cpfDep',   tamanho=[1, 11],    raiz='//detPlano', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmDep    = TagCaracter(nome='nmDep',    tamanho=[1, 70],    raiz='//detPlano', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtNascto = TagData(    nome='dtNascto', tamanho=[1, 70],    raiz='//detPlano', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrPgDep  = TagDecimal( nome='vrPgDep',  tamanho=[1, 14, 2], raiz='//detPlano', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detPlano>'
        xml += self.tpDep.xml
        xml += self.cpfDep.xml
        xml += self.nmDep.xml
        xml += self.dtNascto.xml
        xml += self.vrPgDep.xml
        xml += '</detPlano>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpDep.xml = arquivo
            self.cpfDep.xml = arquivo
            self.nmDep.xml = arquivo
            self.dtNascto.xml = arquivo
            self.vrPgDep.xml = arquivo

    xml = property(get_xml, set_xml)


class DetOper(XMLNFe):
    def __init__(self):
        super(DetOper, self).__init__()
        self.cnpjOper = TagCaracter(nome='cnpjOper', tamanho=[1, 14],    raiz='//detOper', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.regANS   = TagCaracter(nome='regANS',   tamanho=[1, 6],     raiz='//detOper', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrPgTit  = TagDecimal( nome='vrPgTit',  tamanho=[1, 14, 2], raiz='//detOper', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.detPlano = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detOper>'
        xml += self.cnpjOper.xml
        xml += self.regANS.xml
        xml += self.vrPgTit.xml
        if len(self.detPlano) > 0:
            for d in self.detPlano:
                xml += d.xml
        xml += '</detOper>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjOper.xml = arquivo
            self.regANS.xml = arquivo
            self.vrPgTit.xml = arquivo
            self.detPlano = self.le_grupo('//eSocial/evtRmnRPPS/dmDev/ideEstab/remunPerApur/infoSaudeColet/detOper/detPlano', DetPlano, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoSaudeColet(XMLNFe):
    def __init__(self):
        super(InfoSaudeColet, self).__init__()
        self.detOper = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoSaudeColet>'
        if len(self.detOper) > 0:
            for d in self.detOper:
                xml += d.xml
        xml += '</infoSaudeColet>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.detOper = self.le_grupo('//eSocial/evtRmnRPPS/dmDev/ideEstab/remunPerApur/infoSaudeColet/detOper', DetOper, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class ItensRemun(XMLNFe):
    def __init__(self):
        super(ItensRemun, self).__init__()
        self.codRubr    = TagCaracter(nome='codRubr',    tamanho=[1, 30],    raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideTabRubr = TagCaracter(nome='ideTabRubr', tamanho=[1, 8],     raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.qtdRubr    = TagInteiro( nome='qtdRubr',    tamanho=[1, 6],     raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.fatorRubr  = TagInteiro( nome='fatorRubr',  tamanho=[1, 5],     raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrUnit     = TagDecimal( nome='vrUnit',     tamanho=[1, 14, 2], raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrRubr     = TagDecimal( nome='vrRubr',     tamanho=[1, 14, 2], raiz='//itensRemun', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<itensRemun>'
        xml += self.codRubr.xml
        xml += self.ideTabRubr.xml
        xml += self.qtdRubr.xml
        xml += self.fatorRubr.xml
        xml += self.vrUnit.xml
        xml += self.vrRubr.xml
        xml += '</itensRemun>'
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


class RemunPerApur(XMLNFe):
    def __init__(self):
        super(RemunPerApur, self).__init__()
        self.matricula = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//infoPerApur/ideEstab/remunPerApur', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg  = TagCaracter(nome='codCateg',  tamanho=[1, 3],  raiz='//infoPerApur/ideEstab/remunPerApur', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.itensRemun = []
        self.infoSaudeColet = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<remunPerApur>'
        xml += self.matricula.xml
        xml += self.codCateg.xml
        if len(self.itensRemun) > 0:
            for i in self.itensRemun:
                xml += i.xml
        if len(self.infoSaudeColet) > 0:
            for i in self.infoSaudeColet:
                xml += i.xml
        xml += '</remunPerApur>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.matricula.xml = arquivo
            self.codCateg.xml = arquivo
            self.itensRemun = self.le_grupo('//eSocial/evtRmnRPPS/dmDev/ideEstab/remunPerApur/itensRemun', ItensRemun, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoSaudeColet = self.le_grupo('//eSocial/evtRmnRPPS/dmDev/ideEstab/remunPerApur/infoSaudeColet ', InfoSaudeColet, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEstab(XMLNFe):
    def __init__(self):
        super(IdeEstab, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1, 1],  raiz='//infoPerApur/ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//infoPerApur/ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.remunPerApur = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstab>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        if len(self.remunPerApur) > 0:
            for r in self.remunPerApur:
                xml += r.xml
        xml += '</ideEstab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.remunPerApur = self.le_grupo('//eSocial/evtRmnRPPS/dmDev/infoPerApur/ideEstab/remunPerApur', RemunPerApur, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoPerApur(XMLNFe):
    def __init__(self):
        super(InfoPerApur, self).__init__()
        self.ideEstab = IdeEstab()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPerApur>'
        xml += self.ideEstab.xml
        xml += '</infoPerApur>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideEstab.xml = arquivo

    xml = property(get_xml, set_xml)


class DmDev(XMLNFe):
    def __init__(self):
        super(DmDev, self).__init__()
        self.ideDmDev = TagCaracter(nome='ideDmDev', tamanho=[1, 30], raiz='//eSocial/evtRmnRPPS/dmDev', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoPerApur   = []
        self.infoPerAnt    = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dmDev>'
        xml += self.ideDmDev.xml
        if len(self.infoPerApur) > 0:
            for i in self.infoPerApur:
                xml += i.xml
        if len(self.infoPerAnt) > 0:
            for i in self.infoPerAnt:
                xml += i.xml
        xml += '</dmDev>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideDmDev.xml = arquivo
            self.infoPerApur = self.le_grupo('//eSocial/evtRmnRPPS/dmDev/infoPerApur', InfoPerApur, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoPerAnt = self.le_grupo('//eSocial/evtRmnRPPS/dmDev/infoPerAnt', InfoPerAnt, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class ProcJudTrab(XMLNFe):
    def __init__(self):
        super(ProcJudTrab, self).__init__()
        self.tpTrib    = TagCaracter(nome='tpTrib',    tamanho=[1, 1],  raiz='//procJudTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrProcJud = TagCaracter(nome='nrProcJud', tamanho=[1, 20], raiz='//procJudTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codSusp   = TagCaracter(nome='codSusp',   tamanho=[1, 14], raiz='//procJudTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<procJudTrab>'
        xml += self.tpTrib.xml
        xml += self.nrProcJud.xml
        xml += self.codSusp.xml
        xml += '</procJudTrab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpTrib.xml = arquivo
            self.nrProcJud.xml = arquivo
            self.codSusp.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeTrabalhador(XMLNFe):
    def __init__(self):
        super(IdeTrabalhador, self).__init__()
        self.cpfTrab        = TagCaracter(nome='cpfTrab',  tamanho=[1, 11], raiz='//eSocial/evtRmnRPPS/ideTrabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab        = TagCaracter(nome='nisTrab',  tamanho=[1, 11], raiz='//eSocial/evtRmnRPPS/ideTrabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.qtdDepFP       = TagInteiro( nome='qtdDepFP', tamanho=[1, 2],  raiz='//eSocial/evtRmnRPPS/ideTrabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.procJudTrab    = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideTrabalhador>'
        xml += self.cpfTrab.xml
        xml += self.nisTrab.xml
        xml += self.qtdDepFP.xml
        if len(self.procJudTrab) > 0:
            for p in self.procJudTrab:
                xml += p.xml
        xml += '</ideTrabalhador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrab.xml = arquivo
            self.nisTrab.xml = arquivo
            self.qtdDepFP.xml = arquivo
            self.procJudTrab = self.le_grupo('//eSocial/evtRmnRPPS/ideTrabalhador/procJudTrab', ProcJudTrab, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1, 1],  raiz='//eSocial/evtRmnRPPS/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtRmnRPPS/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif    = TagInteiro( nome='indRetif',    tamanho=[1,  1], raiz='//eSocial/evtRmnRPPS/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrRecibo    = TagCaracter(nome='nrRecibo',    tamanho=[1, 40], raiz='//eSocial/evtRmnRPPS/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indApuracao = TagCaracter(nome='indApuracao', tamanho=[1,  1], raiz='//eSocial/evtRmnRPPS/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.perApur     = TagCaracter(nome='perApur',     tamanho=[1,  7], raiz='//eSocial/evtRmnRPPS/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpAmb       = TagInteiro( nome='tpAmb',       tamanho=[1,  1], raiz='//eSocial/evtRmnRPPS/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi     = TagInteiro( nome='procEmi',     tamanho=[1,  1], raiz='//eSocial/evtRmnRPPS/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc     = TagCaracter(nome='verProc',     tamanho=[1, 20], raiz='//eSocial/evtRmnRPPS/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtRmnRPPS(XMLNFe):
    def __init__(self):
        super(EvtRmnRPPS, self).__init__()
        self.Id = TagCaracter(nome='evtRmnRPPS', propriedade='Id', raiz='//eSocial/evtRmnRPPS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideTrabalhador = IdeTrabalhador()
        self.dmDev = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideTrabalhador.xml
        if len(self.dmDev) > 0:
            for d in self.dmDev:
                xml += d.xml
        xml += '</evtRmnRPPS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideTrabalhador.xml = arquivo
            self.dmDev = self.le_grupo('//eSocial/evtRmnRPPS/dmDev', DmDev, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class S1202(XMLNFe):
    def __init__(self):
        super(S1202, self).__init__()
        self.evtRmnRPPS = EvtRmnRPPS()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtRmnRPPS.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtRmnRPPS
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtRmnRPPS.xml

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
            self.evtRmnRPPS.xml = arquivo
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
        self.evtRmnRPPS.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
