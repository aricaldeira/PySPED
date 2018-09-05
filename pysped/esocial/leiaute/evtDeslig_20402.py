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
# Copyright (C) Luiz Felipe do Divino <luiz.divino@abgf.gov.br>
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

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str
import os
from pysped.xml_sped import *
from pysped.esocial.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

DIRNAME = os.path.dirname(__file__)

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtDeslig/v02_04_02'


class DetVerbas(XMLNFe):
    def __init__(self):
        super(DetVerbas, self).__init__()
        self.codRubr = TagCaracter(nome='codRubr', tamanho=[1, 30], raiz='//detVerbas', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideTabRubr = TagCaracter(nome='ideTabRubr', tamanho=[1, 8], raiz='//detVerbas', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.qtdRubr = TagInteiro(nome='qtdRubr', raiz='//detVerbas', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.fatorRubr = TagInteiro(nome='fatorRubr', raiz='//detVerbas', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrUnit = TagInteiro(nome='vrUnit', raiz='//detVerbas', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrRubr = TagDecimal(nome='vrRubr', raiz='//detVerbas', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detVerbas>'
        xml += self.codRubr.xml
        xml += self.ideTabRubr.xml
        xml += self.qtdRubr.xml
        xml += self.fatorRubr.xml
        xml += self.vrUnit.xml
        xml += self.vrRubr.xml
        xml += '</detVerbas>'

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


class DetPlano(XMLNFe):
    def __init__(self):
        super(DetPlano, self).__init__()
        self.tpDep = TagCaracter(name='tpDep', tamanho=[1, 2], raiz='//dtPlano', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cpfDep = TagCaracter(name='cpfDep', tamanho=[1, 11], raiz='//dtPlano', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmDep = TagCaracter(name='nmDep', tamanho=[1, 70], raiz='//dtPlano', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtNascto = TagData(name='dtNascto', raiz='//dtPlano', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlorPgDep = TagInteiro(name='vlorPgDep', raiz='//dtPlano', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detPlano>'
        xml += self.tpDep.xml
        xml += self.cpfDep.xml
        xml += self.nmDep.xml
        xml += self.dtNascto.xml
        xml += self.vlorPgDep.xml

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpDep.xml = arquivo
            self.cpfDep.xml = arquivo
            self.nmDep.xml = arquivo
            self.dtNascto.xml = arquivo
            self.vlorPgDep.xml = arquivo

    xml = property(get_xml, set_xml)


class DetOper(XMLNFe):
    def __init__(self):
        super(DetOper, self).__init__()
        self.cnpjOper = TagCaracter(name='cnpjOper', tamanho=[1, 14], raiz='//detOper', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.regANS = TagCaracter(name='regANS', tamanho=[1, 6], raiz='//detOper', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrPgTit = TagInteiro(name='vrPgTit', raiz='//detOper', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.detPlano = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detOper>'
        xml += self.cnpjOper.xml
        xml += self.regANS.xml
        xml += self.vrPgTit.xml
        if self.detPlano:
            for plano in self.detPlano:
                xml += plano.xml
        xml += '</detOper>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjOper.xml = arquivo
            self.regANS.xml = arquivo
            self.vrPgTit.xml = arquivo
            self.detPlano = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerApur/ideEstabLot/infoSaudeCelet/detOper/detPlano', DetPlano, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoSaudeColet(XMLNFe):
    def __init__(self):
        super(InfoSaudeColet, self).__init__()
        self.detOper = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoSaudeColet>'
        if self.detOper:
            for detalhamento in self.detOper:
                xml += detalhamento.xml
        xml += '</infoSaudeColet>'

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.detOper = self.infoSaudeCelet = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerApur/ideEstabLot/infoSaudeCelet/detOper', DetOper, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoAgNocivo(XMLNFe):
    def __init__(self):
        super(InfoAgNocivo, self).__init__()
        self.grauExp = TagInteiro(nome='grauExp', raiz='//grauExp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoAgNocivo>'
        xml += self.grauExp.xml
        xml += '</infoAgNocivo>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.grauExp.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoSimples(XMLNFe):
    def __init__(self):
        super(InfoSimples, self).__init__()
        self.indSimples = TagInteiro(name='indSimples', raiz='//indSimples', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoSimples>'
        xml += self.indSimples.xml
        xml += '</infoSimples>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indSimples.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEstabLotApur(XMLNFe):
    def __init__(self):
        super(IdeEstabLotApur, self).__init__()
        self.tpInsc = TagInteiro(nome='tpInsc', raiz='//ideEstabLot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//ideEstabLot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codLotacao = TagCaracter(nome='codLotacao', tamanho=[1, 30], raiz='//ideEstabLot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.detVerbas = []
        self.infoSaudeColet = []
        self.infoAgNocivo = []
        self.infoSimples = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstabLot>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.codLotacao.xml
        if self.detVerbas:
            for verba in self.detVerbas:
                xml += verba.xml
        if self.infoAgNocivo:
            for agente in self.infoAgNocivo:
                xml += agente.xml
        if self.infoSaudeColet:
            for info in self.infoSaudeColet:
                xml += info.xml
        xml += '</ideEstabLot>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.codLotacao.xml = arquivo
            self.detVerbas = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerApur/ideEstabLot/detVerbas', DetVerbas, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoSaudeColet = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerApur/ideEstabLot/infoSaudeCelet', InfoSaudeColet, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoAgNocivo = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerApur/ideEstabLot/infoAgNocivo', InfoAgNocivo, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoSimples = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerApur/ideEstabLot/infoSimples', InfoSimples, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoPerApur(XMLNFe):
    def __init__(self):
        super(InfoPerApur, self).__init__()
        self.ideEstabLot = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPerApur>'
        if self.ideEstabLot:
            for ide in self.ideEstabLot:
                xml += ide.xml
        xml += '</infoPerApur>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideEstabLot = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerApur/ideEstabLot', IdeEstabLotApur, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEstabLot(XMLNFe):
    def __init__(self):
        super(IdeEstabLot, self).__init__()
        self.tpInsc = TagInteiro(nome='tpInsc', raiz='//ideEstabLot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//ideEstabLot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codLotacao = TagCaracter(nome='codLotacao', tamanho=[1, 30], raiz='//ideEstabLot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.detVerbas = []
        self.infoAgNocivo = []
        self.infoSimples = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstabLot>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.codLotacao.xml
        if self.detVerbas:
            for verba in self.detVerbas:
                xml += verba.xml
        if self.infoAgNocivo:
            for info in self.infoAgNocivo:
                xml += info.xml
        if self.infoSimples:
            for info_simples in self.infoSimples:
                xml += info_simples.xml
        xml += '</ideEstabLot>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.codLotacao.xml = arquivo
            self.detVerbas = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerApur/ideEstabLot/detVerbas', DetVerbas, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')


class IdePeriodo(XMLNFe):
    def __init__(self):
        super(IdePeriodo, self).__init__()
        self.perRef = TagCaracter(nome='perRef', tamanho=[1, 7], raiz='//idePeriodo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEstabLot = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePeriodo>'
        xml += self.perRef.xml
        if self.ideEstabLot:
            for estabelecimento in self.ideEstabLot:
                xml += estabelecimento.xml
        xml += '</idePeriodo>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.perRef.xml = arquivo
            self.ideEstabLot = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerAnt/ideADC/idePeriodo/ideEstabLot', IdeEstabLot, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')


class IdeADC(XMLNFe):
    def __init__(self):
        super(IdeADC, self).__init__()
        self.dtAcConv = TagData(name='dtAcConv', raiz='//ideADC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpAcConv = TagCaracter(name='tpAcConv', tamanho=[1, 1], raiz='//ideADC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.compAcConv = TagCaracter(name='compAcConv', tamanho=[1, 7], raiz='//ideADC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtEfAcConv = TagData(name='dtEfAcConv', raiz='//ideADC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dsc = TagCaracter(name='dsc', tamanho=[1, 255], raiz='//ideADC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.idePeriodo = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideADC>'
        xml += self.dtAcConv.xml
        xml += self.tpAcConv.xml
        xml += self.compAcConv.xml
        xml += self.dtEfAcConv.xml
        xml += self.dsc.xml
        if self.idePeriodo:
            for periodo in self.idePeriodo:
                xml += periodo.xml
        xml += '</ideADC>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtAcConv.xml = arquivo
            self.tpAcConv.xml = arquivo
            self.compAcConv.xml = arquivo
            self.dtEfAcConv.xml = arquivo
            self.dsc.xml = arquivo
            self.idePeriodo = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerAnt/ideADC/idePeriodo', IdePeriodo, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')


class InfoPerAnt(XMLNFe):
    def __init__(self):
        super(InfoPerAnt, self).__init__()
        self.ideADC = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPerAnt>'
        if self.ideADC:
            for ide in self.ideADC:
                xml += ide.xml
        xml += '</infoPerAnt>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideADC = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerAnt/ideADC', IdeADC, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')


class InfoTrabInterm(XMLNFe):
    def __init__(self):
        super(InfoTrabInterm, self).__init__()
        self.codConv = TagCaracter(name='codConv', tamanho=[1, 30], raiz='//codConv', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoTrabInterm>'
        xml += self.codConv.xml
        xml += '</infoTrabInterm>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codConv.xml = arquivo

    xml = property(get_xml, set_xml)


class DmDev(XMLNFe):
    def __init__(self):
        super(DmDev, self).__init__()
        self.ideDmDev = TagCaracter(nome='ideDmDev', tamanho=[1, 30], raiz='//dmDev', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoPerApur = []
        self.infoPerAnt = []
        self.infoTrabInterm = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dmDev>'
        xml += self.ideDmDev.xml
        if self.infoPerApur:
            for info in self.infoPerApur:
                xml += info.xml
        if self.infoPerAnt:
            for ant in self.infoPerAnt:
                xml += ant.xml
        if self.infoTrabInterm:
            for trabalho_intermitente in self.infoTrabInterm:
                xml += trabalho_intermitente.xml
        xml += '</dmDev>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideDmDev.xml = arquivo
            self.infoPerApur = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerApur', InfoPerApur, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoPerAnt = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoPerAnt', InfoPerAnt, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoTrabInterm = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev/infoTrabInterm', InfoTrabInterm, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class ProcJudTrab(XMLNFe):
    def __init__(self):
        super(ProcJudTrab, self).__init__()
        self.tpTrib = TagInteiro(name='tpTrib', raiz='//procJudTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrProcJud = TagCaracter(name='nrProcJud', tamanho=[1, 20], raiz='//procJudTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codSusp = TagInteiro(name='codSusp', raiz='//procJudTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

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


class RemunOutrEmpr(XMLNFe):
    def __init__(self):
        super(RemunOutrEmpr, self).__init__()
        self.tpInsc = TagInteiro(name='tpInsc', raiz='//remunOutrEmpr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(name='nrInsc', tamanho=[1, 15], raiz='//remunOutrEmpr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codCateg = TagInteiro(name='codCateg', raiz='//remunOutrEmpr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrRemunOE = TagInteiro(name='vlrRemunOE', raiz='//remunOutrEmpr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<remunOutrEmpr>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.codCateg.xml
        xml += self.vlrRemunOE.xml
        xml += '</remunOutrEmpr>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.codCateg.xml = arquivo
            self.vlrRemunOE.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoMV(XMLNFe):
    def __init__(self):
        super(InfoMV, self).__init__()
        self.indMV = TagInteiro(name='indMV', raiz='//infoMV', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.remunOutrEmpr = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoMV>'
        xml += self.indMV.xml
        if self.remunOutrEmpr:
            for remuneracao in self.remunOutrEmpr:
                xml += remuneracao.xml
        xml += '</infoMV>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indMV.xml = arquivo
            self.remunOutrEmpr = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/infoMV/remunOutrEmpr', RemunOutrEmpr, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class ProcCS(XMLNFe):
    def __init__(self):
        super(ProcCS, self).__init__()
        self.nrProcJud = TagCaracter(nome='nrProcJud', tamanho=[1, 20], raiz='//procCS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<procCS>'
        xml += self.nrProcJud.xml
        xml += '</procCS>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrProcJud.xml = arquivo

    xml = property(get_xml, set_xml)


class VerbasResc(XMLNFe):
    def __init__(self):
        super(VerbasResc, self).__init__()
        self.dmDev = []
        self.procJudTrab = []
        self.infoMV = []
        self.procCS = []
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<verbasResc>'
        if len(self.dmDev) > 0:
            for demostrativo in self.dmDev:
                xml += demostrativo.xml
        if len(self.procJudTrab) > 0:
            for processoJud in self.procJudTrab:
                xml += processoJud.xml
        if len(self.infoMV) > 0:
            for info in self.infoMV:
                xml += info.xml
        if len(self.procCS) > 0:
            for processo in self.procCS:
                xml += processo.xml
        xml += '</verbasResc>'
        
        return xml
    
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dmDev = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/dmDev', DmDev, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.procJudTrab = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/procJudTrab', ProcJudTrab, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoMV = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/infoMV', HorarioIntervalo, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.procCS = self.le_grupo('//eSocial/evtDeslig/inforDeslig/verbasResc/procCs', HorarioIntervalo, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Observacoes(XMLNFe):
    def __init__(self):
        super(Observacoes, self).__init__()
        self.observacao = TagCaracter(nome='observacao', tamanho=[1, 255], raiz='//observacoes', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<observacao>'
        xml += self.observacao.xml
        xml += '</observacao>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.observacao.xml = arquivo

    xml = property(get_xml, set_xml)


class SucessaoVinc(XMLNFe):
    def __init__(self):
        super(SucessaoVinc, self).__init__()
        self.cnpjSucessora = TagCaracter(nome='cnpjSucessora', tamanho=[1, 14], raiz='//sucessaoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<sucessaoVinc>'
        xml += self.cnpjSucessora.xml
        xml += '</sucessaoVinc>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjSucessora.xml = arquivo

    xml = property(get_xml, set_xml)


class TransfTit(XMLNFe):
    def __init__(self):
        super(TransfTit, self).__init__()
        self.cpfSubstituto = TagCaracter(name='cpfSubstituto', tamanho=[1, 11], raiz='//transfTit', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtNascto = TagData(name='dtNascto', raiz='//transfTit', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<transfTit>'
        xml += self.cpfSubstituto.xml
        xml += self.dtNascto.xml
        xml += '</transfTit>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfSubstituto.xml = arquivo
            self.dtNascto.xml = arquivo

    xml = property(get_xml, set_xml)


class Quarentena(XMLNFe):
    def __init__(self):
        super(Quarentena, self).__init__()
        self.dtFimQuar = TagData(name='dtFimQuar', raiz='//quarentena', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<quarentena>'
        xml += self.dtFimQuar.xml
        xml += '</quarentena>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtFimQuar.xml = arquivo

    xml = property(get_xml, set_xml)


class ConsigFGTS(XMLNFe):
    def __init__(self):
        super(ConsigFGTS, self).__init__()
        self.insConsig = TagCaracter(nome='insConsig', tamanho=[1, 5], raiz='//consigFGTS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrContr = TagCaracter(nome='nrContr', tamanho=[1, 40], raiz='//consigFGTS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<consigFGTS>'
        xml += self.insConsig.xml
        xml += self.nrContr
        xml += '</consigFGTS>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.insConsig.xml = arquivo
            self.nrContr.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoDeslig(XMLNFe):
    def __init__(self):
        super(InfoDeslig, self).__init__()
        self.mtvDeslig = TagCaracter(nome='mtvDeslig', tamanho=[1, 2], raiz='//eSocial/evtDeslig/inforDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtDeslig = TagData(nome='dtDeslig', raiz='//eSocial/evtDeslig/inforDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indPagtoAPI = TagCaracter(nome='indPagtoAPI', tamanho=[1, 1], raiz='//eSocial/evtDeslig/inforDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtProjFimAPI = TagData(nome='dtProjFimAPI', raiz='//eSocial/evtDeslig/inforDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.pensAlim = TagCaracter(nome='pensAlim', tamanho=[1, 1], raiz='//eSocial/evtDeslig/inforDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.percAliment = TagInteiro(nome='percAliment', raiz='//eSocial/evtDeslig/inforDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrAlim = TagInteiro(nome='vrAlim', raiz='//eSocial/evtDeslig/inforDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nrCertObito = TagCaracter(nome='nrCertObito', raiz='//eSocial/evtDeslig/inforDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nrProcTrab = TagCaracter(nome='nrProcTrab', tamanho=[1, 20], raiz='//eSocial/evtDeslig/inforDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indCumprParc = TagInteiro(nome='indCumprParc', raiz='//eSocial/evtDeslig/inforDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.qtdDiasInterm = TagInteiro(nome='qtdDiasInterm', raiz='//eSocial/evtDeslig/inforDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.observacoes = []
        self.sucessaoVinc = []
        self.transfTit = []
        self.verbaResc = []
        self.quarentena = []
        self.consigFGTS = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoDeslig>'
        xml += self.mtvDeslig.xml
        xml += self.dtDeslig.xml
        xml += self.indPagtoAPI.xml
        xml += self.dtProjFimAPI.xml
        xml += self.pensAlim.xml
        xml += self.percAliment.xml
        xml += self.vrAlim.xml
        xml += self.nrCertObito.xml
        xml += self.nrProcTrab.xml
        xml += self.indCumprParc.xml
        xml += self.qtdDiasInterm.xml
        if len(self.observacoes) > 0:
            for observacao in self.observacoes:
                xml += observacao.xml
        if len(self.sucessaoVinc) > 0:
            for sucessao in self.sucessaoVinc:
                xml += sucessao.xml
        if len(self.transfTit) > 0:
            for transferencia in self.transfTit:
                xml += transferencia.xml
        if len(self.verbaResc) > 0:
            for verba in self.verbaResc:
                xml += verba.xml
        if len(self.quarentena) > 0:
            for quaren in self.quarentena:
                xml += quaren.xml
        if len(self.consigFGTS) > 0:
            for consig in self.consigFGTS:
                xml += consig.xml
        xml += '</infoDeslig>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.mtvDeslig.xml = arquivo
            self.dtDeslig.xml = arquivo
            self.indPagtoAPI.xml = arquivo
            self.dtProjFimAPI.xml = arquivo
            self.pensAlim.xml = arquivo
            self.percAliment.xml = arquivo
            self.vrAlim.xml = arquivo
            self.nrCertObito.xml = arquivo
            self.nrProcTrab.xml = arquivo
            self.indCumprParc.xml = arquivo
            self.qtdDiasInterm.xml = arquivo
            self.observacoes = self.le_grupo('//eSocial/evtDeslig/inforDeslig/observacoes', Observacoes, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.sucessaoVinc = self.le_grupo('//eSocial/evtDeslig/inforDeslig/sucessaoVinc', SucessaoVinc, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.transfTit = self.le_grupo('//eSocial/evtDeslig/inforDeslig/transfTit', TransfTit, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.quarentena = self.le_grupo('//eSocial/evtDeslig/inforDeslig/quarentena', Quarentena, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.consigFGTS = self.le_grupo('//eSocial/evtDeslig/inforDeslig/consigFGTS', ConsigFGTS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeVinculo(XMLNFe):
    def __init__(self):
        super(IdeVinculo, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', tamanho=[1, 11], raiz='//eSocial/evtDeslig/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab = TagCaracter(nome='nisTrab', tamanho=[1, 11], raiz='//eSocial/evtDeslig/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.matricula = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//eSocial/evtDeslig/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideVinculo>'
        xml += self.cpfTrab.xml
        xml += self.nisTrab.xml
        xml += self.matricula.xml
        xml += '</ideVinculo>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrab.xml = arquivo
            self.nisTrab.xml = arquivo
            self.matricula.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagInteiro(nome='tpInsc', raiz='//eSocial/evtDeslig/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtDeslig/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif = TagInteiro(nome='indRetif', raiz='//eSocial/evtDeslig/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', tamanho=[1, 40], raiz='//eSocial/evtDeslig/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpAmb   = TagInteiro(nome='tpAmb'   , raiz='//eSocial/evtDeslig/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi' , raiz='//eSocial/evtDeslig/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20], raiz='//eSocial/evtDeslig/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.indRetif.xml
        xml += self.nrRecibo.xml
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indRetif.xml = arquivo
            self.nrRecibo.xml = arquivo
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtDeslig(XMLNFe):
    def __init__(self):
        super(EvtDeslig, self).__init__()
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideVinculo = IdeVinculo()
        self.infoDeslig = InfoDeslig()
        self.Id = TagCaracter(nome='evtDeslig', propriedade='Id', tamanho=[1, 36], raiz='//eSocial/evtDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideVinculo.xml
        xml += self.infoDeslig.xml
        xml += '</evtDeslig>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoDeslig.xml = arquivo

    xml = property(get_xml, set_xml)


class S2299(XMLNFe):
    def __init__(self):
        super(S2299, self).__init__()
        self.evtDeslig = EvtDeslig()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtDeslig.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtDeslig
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        # xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtDeslig.xml

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
            self.evtTabHorTur.xml = arquivo
            # self.Signature.xml = self._le_noh('//eSocial/sig:Signature')

    def gera_id_evento(self, data_hora, sequencia=False):
        # A identificação única do evento (Id) é composta por 36 caracteres, conforme o que segue: IDTNNNNNNNNNNNNNNAAAAMMDDHHMMSSQQQQQ
        # ID - Texto Fixo "ID";
        # T - Tipo de Inscrição do Empregador (1 - CNPJ; 2 - CPF);
        # NNNNNNNNNNNNNN - Número do CNPJ ou CPF do empregador - Completar com
        # zeros à direita. No caso de pessoas jurídicas, o CNPJ informado deve conter 8 ou 14
        # posições de acordo com o enquadramento do contribuinte para preenchimento do campo
        # {ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se
        # necessário.
        # AAAAMMDD - Ano, mês e dia da geração do evento;
        # HHMMSS - Hora, minuto e segundo da geração do evento;
        # QQQQQ - Número sequencial da chave. Incrementar somente quando ocorrer geração de
        # eventos na mesma data/hora, completando com zeros à esquerda.
        # OBS.: No caso de pessoas jurídicas, o CNPJ informado deverá conter 8 ou 14 posições de
        # acordo com o enquadramento do contribuinte para preenchimento do campo {ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se necessário.

        if not sequencia:
            sequencia=1

        id_evento = 'ID'
        id_evento += self.tpInsc
        id_evento += self.nrInsc[0:8] + '000000'
        id_evento += data_hora
        id_evento += str(sequencia).zfill(5)

        # Define o Id
        #
        self.evtDeslig.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
