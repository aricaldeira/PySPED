# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtTSVInicio/v02_04_02'


class SupervisorEstagio(XMLNFe):
    def __init__(self):
        super(SupervisorEstagio, self).__init__()
        self.cpfSupervisor = TagCaracter(nome='cpfSupervisor', tamanho=[1, 11], raiz='//cpfSupervisor', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmSupervisor = TagCaracter(nome='nmSupervisor', tamanho=[1, 70], raiz='//nmSupervisor', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<supervisorEstagio>'
        xml += self.cpfSupervisor.xml
        xml += self.nmSupervisor.xml
        xml += '</supervisorEstagio>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfSupervisor.xml = arquivo
            self.nmSupervisor.xml = arquivo

    xml = property(get_xml, set_xml)


class AgeIntegracao(XMLNFe):
    def __init__(self):
        super(InstEnsino, self).__init__()
        self.cnpjAgntInteg = TagCaracter(nome='cnpjAgntInteg', tamanho=[1, 14], raiz='//cnpjAgntInteg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmRazao = TagCaracter(nome='nmRazao', tamanho=[1, 100], raiz='//nmRazao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscLograd = TagCaracter(nome='dscLograd', tamanho=[1, 14], raiz='//dscLograd', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nrLograd = TagInteiro(nome='nrLograd', tamanho=[1, 1], raiz='//nrLograd', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.bairro = TagCaracter(nome='bairro', tamanho=[1, 60], raiz='//bairro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.cep = TagCaracter(nome='cep', tamanho=[1, 8], raiz='//cep', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMunic = TagCaracter(nome='codMunic', tamanho=[1,  7], raiz='//codMunic', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.uf = TagCaracter(nome='uf', tamanho=[1,  2], raiz='//uf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<instEnsino>'
        xml += self.cnpjInstEnsino.xml
        xml += self.nmRazao.xml
        xml += self.dscLograd.xml
        xml += self.nrLograd.xml
        xml += self.bairro.xml
        xml += self.cep.xml
        xml += self.codMunic.xml
        xml += self.uf.xml
        xml += '</instEnsino>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjInstEnsino.xml = arquivo
            self.nmRazao.xml = arquivo
            self.dscLograd.xml = arquivo
            self.nrLograd.xml = arquivo
            self.bairro.xml = arquivo
            self.cep.xml = arquivo
            self.codMunic.xml = arquivo
            self.uf.xml = arquivo

    xml = property(get_xml, set_xml)


class InstEnsino(XMLNFe):
    def __init__(self):
        super(InstEnsino, self).__init__()
        self.cnpjInstEnsino = TagCaracter(nome='cnpjInstEnsino', tamanho=[1, 14], raiz='//cnpjInstEnsino', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmRazao = TagCaracter(nome='nmRazao', tamanho=[1, 100], raiz='//nmRazao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscLograd = TagCaracter(nome='dscLograd', tamanho=[1, 14], raiz='//dscLograd', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nrLograd = TagInteiro(nome='nrLograd', tamanho=[1, 1], raiz='//nrLograd', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.bairro = TagCaracter(nome='bairro', tamanho=[1, 60], raiz='//bairro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.cep = TagCaracter(nome='cep', tamanho=[1, 8], raiz='//cep', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMunic = TagCaracter(nome='codMunic', tamanho=[1,  7], raiz='//codMunic', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.uf = TagCaracter(nome='uf', tamanho=[1,  2], raiz='//uf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<instEnsino>'
        xml += self.cnpjInstEnsino.xml
        xml += self.nmRazao.xml
        xml += self.dscLograd.xml
        xml += self.nrLograd.xml
        xml += self.bairro.xml
        xml += self.cep.xml
        xml += self.codMunic.xml
        xml += self.uf.xml
        xml += '</instEnsino>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjInstEnsino.xml = arquivo
            self.nmRazao.xml = arquivo
            self.dscLograd.xml = arquivo
            self.nrLograd.xml = arquivo
            self.bairro.xml = arquivo
            self.cep.xml = arquivo
            self.codMunic.xml = arquivo
            self.uf.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoEstagiario(XMLNFe):
    def __init__(self):
        super(InfoEstagiario, self).__init__()
        self.natEstagio = TagCaracter(nome='natEstagio', tamanho=[1, 1], raiz='//natEstagio', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nivEstagio = TagInteiro(nome='nivEstagio', tamanho=[1, 1], raiz='//nivEstagio', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.areaAtuacao = TagInteiro(nome='areaAtuacao', tamanho=[0, 50], raiz='//areaAtuacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nrApol = TagCaracter(nome='nrApol', tamanho=[0, 30], raiz='//nrApol', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrBolsa = TagDecimal(nome='vlrBolsa', tamanho=[1, 14, 2], raiz='//vlrBolsa', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtPrevTerm = TagData(nome='dtPrevTerm', raiz='//dtPrevTerm', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.instEnsino = InstEnsino()
        self.ageIntegracao = []
        self.supervisorEstagio = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoEstagiario>'
        xml += self.natEstagio.xml
        xml += self.nivEstagio.xml
        xml += self.areaAtuacao.xml
        xml += self.nrApol.xml
        xml += self.vlrBolsa.xml
        xml += self.dtPrevTerm.xml
        xml += self.instEnsino.xml
        if self.ageIntegracao:
            for age in self.ageIntegracao:
                xml += age.xml
        if self.supervisorEstagio:
            xml += self.supervisorEstagio[0].xml
        xml += '</infoEstagiario>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.opcFGTS.xml = arquivo
            self.dtOpcFGTS.xml = arquivo
            self.natEstagio.xml = arquivo
            self.nivEstagio.xml = arquivo
            self.areaAtuacao.xml = arquivo
            self.nrApol.xml = arquivo
            self.vlrBolsa.xml = arquivo
            self.dtPrevTerm.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoTrabCedido(XMLNFe):
    def __init__(self):
        super(InfoTrabCedido, self).__init__()
        self.categOrig = TagCaracter(nome='categOrig', raiz='//categOrig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cnpjCednt = TagCaracter(nome='cnpjCednt', raiz='//cnpjCednt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.matricCed = TagCaracter(nome='matricCed', raiz='//matricCed', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtAdmCed = TagData(nome='dtAdmCed', raiz='//dtAdmCed', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpRegTrab = TagCaracter(nome='tpRegTrab', raiz='//tpRegTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpRegPrev = TagCaracter(nome='tpRegPrev', raiz='//tpRegPrev', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infOnus = TagCaracter(nome='infOnus', tamanho=[1, 1], raiz='//infOnus', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoTrabCedido>'
        xml += self.categOrig.xml
        xml += self.cnpjCednt.xml
        xml += self.matricCed.xml
        xml += self.dtAdmCed.xml
        xml += self.tpRegTrab.xml
        xml += self.tpRegPrev.xml
        xml += self.infOnus.xml
        xml += '</infoTrabCedido>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.categOrig.xml = arquivo
            self.cnpjCednt.xml = arquivo
            self.matricCed.xml = arquivo
            self.dtAdmCed.xml = arquivo
            self.tpRegTrab.xml = arquivo
            self.tpRegPrev.xml = arquivo
            self.infOnus.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoDirigenteSindical(XMLNFe):
    def __init__(self):
        super(InfoDirigenteSindical, self).__init__()
        self.categOrig = TagCaracter(nome='categOrig', raiz='//categOrig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cnpjOrigem = TagCaracter(nome='cnpjOrigem', raiz='//cnpjOrigem', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtAdmOrig = TagData(nome='dtAdmOrig', raiz='//dtAdmOrig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.matricOrig = TagCaracter(nome='matricOrig', raiz='//matricOrig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoDirigenteSindical>'
        xml += self.categOrig.xml
        xml += self.cnpjOrigem.xml
        xml += self.dtAdmOrig.xml
        xml += self.matricOrig.xml
        xml += '</infoDirigenteSindical>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.categOrig.xml = arquivo
            self.cnpjOrigem.xml = arquivo
            self.dtAdmOrig.xml = arquivo
            self.matricOrig.xml = arquivo

    xml = property(get_xml, set_xml)


class FGTS(XMLNFe):
    def __init__(self):
        super(FGTS, self).__init__()
        self.opcFGTS   = TagCaracter(nome='opcFGTS'  , tamanho=[1, 1], raiz='//infoCeletista/fgts', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtOpcFGTS = TagCaracter(nome='dtOpcFGTS', raiz='//infoCeletista/fgts', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<fgts>'
        xml += self.opcFGTS.xml
        xml += self.dtOpcFGTS.xml
        xml += '</fgts>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.opcFGTS.xml = arquivo
            self.dtOpcFGTS.xml = arquivo

    xml = property(get_xml, set_xml)


class Remuneracao(XMLNFe):
    def __init__(self):
        super(Remuneracao, self).__init__()
        self.vrSalFx = TagDecimal(nome='vrSalFx', tamanho=[1, 14, 2], raiz='//vrSalFx', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.undSalFixo = TagInteiro(nome='undSalFixo', tamanho=[1, 1], raiz='//undSalFixo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscSalVar = TagCaracter(nome='dscSalVar', raiz='//dscSalVar', tamanho=[0, 255], namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<remuneracao>'
        xml += self.vrSalFx.xml
        xml += self.undSalFixo.xml
        xml += self.dscSalVar.xml
        xml += '</remuneracao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vrSalFx.xml = arquivo
            self.undSalFixo.xml = arquivo
            self.dscSalVar.xml = arquivo

    xml = property(get_xml, set_xml)


class CargoFuncao(XMLNFe):
    def __init__(self):
        super(CargoFuncao, self).__init__()
        self.codCargo = TagCaracter(nome='codCargo', tamanho=[1, 30], raiz='//codCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codFuncao = TagCaracter(nome='codFuncao', tamanho=[1, 1], raiz='//codCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<cargoFuncao>'
        xml += self.codCargo.xml
        xml += self.codFuncao.xml
        xml += '</cargoFuncao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codCargo.xml = arquivo
            self.codFuncao.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoComplementares(XMLNFe):
    def __init__(self):
        super(InfoComplementares, self).__init__()
        self.cargoFuncao = []
        self.remuneracao = []
        self.fgts = []
        self.infoDirigenteSindical = []
        self.infoTrabCedido = []
        self.infoEstagiario = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoComplementares>'
        if self.cargoFuncao:
            for cf in self.cargoFuncao:
                xml += cf.xml
        if self.remuneracao:
            for r in self.remuneracao:
                xml += r.xml
        if self.fgts:
            for f in self.fgts:
                xml += f.xml
        if self.infoDirigenteSindical:
            for info in self.infoDirigenteSindical:
                xml += info.xml
        if self.infoTrabCedido:
            for info in self.infoTrabCedido:
                xml += info.xml
        if self.infoEstagiario:
            for estag in self.infoEstagiario:
                xml += estag.xml
        xml += '</infoComplementares>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cargoFuncao.xml = self.le_grupo('//eSocial/', CargoFuncao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.remuneracao.xml = self.le_grupo('//eSocial/', Remuneracao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.fgts.xml = self.le_grupo('//eSocial/', FGTS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoDirigenteSindical.xml = arquivo
            self.infoTrabCedido.xml = arquivo
            self.infoEstagiario.xml = arquivo

    xml = property(get_xml, set_xml)


class Afastamento(XMLNFe):
    def __init__(self):
        super(Afastamento, self).__init__()
        self.dtIniAfast = TagData(nome='dtIniAfast', raiz='//dtIniAfast', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMotAfast = TagCaracter(nome='codMotAfast', tamanho=[1, 2], raiz='//codMotAfast', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<afastamento>'
        xml += self.dtIniAfast.xml
        xml += self.codMotAfast.xml
        xml += '</afastamento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtIniAfast.xml = arquivo
            self.codMotAfast.xml = arquivo

    xml = property(get_xml, set_xml)


class Termino(XMLNFe):
    def __init__(self):
        super(Termino, self).__init__()
        self.dtTerm = TagData(nome='dtTerm', raiz='//dtTerm', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<termino>'
        xml += self.dtTerm.xml
        xml += '</termino>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtTerm.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoTSVInicio(XMLNFe):
    def __init__(self):
        super(InfoTSVInicio, self).__init__()
        self.cadIni = TagCaracter(nome='cadIni', tamanho=[1, 1], raiz='//eSocial/evtTSVInicio/infoTSVInicio', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg = TagInteiro(nome='codCateg', raiz='//eSocial/evtTSVInicio/infoTSVInicio', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtInicio = TagData(nome='dtInicio', raiz='//eSocial/evtTSVInicio/infoTSVInicio', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.natAtividade = TagInteiro(nome='natAtividade', raiz='//eSocial/evtTSVInicio/infoTSVInicio', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.infoComplementares = []
        self.afastamento = []
        self.termino = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoTSVInicio>'
        xml += self.cadIni.xml
        xml += self.codCateg.xml
        xml += self.dtInicio.xml
        xml += self.natAtividade.xml
        if self.infoComplementares:
            for info in self.infoComplementares:
                xml += info.xml
        if self.afastamento:
            for a in self.afastamento:
                xml += a.xml
        if self.termino:
            for t in self.termino:
                xml += t.xml
        xml += '</infoTSVInicio>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cadIni.xml = arquivo
            self.codCateg.xml = arquivo
            self.dtInicio.xml = arquivo
            self.natAtividade.xml = arquivo
            self.infoComplementares = self.le_grupo('//eSocial/', InfoComplementares, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.afastamento = self.le_grupo('//eSocial/', Afastamento, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.termino = self.le_grupo('//eSocial/', Termino, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Contato(XMLNFe):
    def __init__(self):
        super(Contato, self).__init__()
        self.fonePrinc     = TagCaracter(nome='fonePrinc'    , tamanho=[1, 13], raiz='//contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.foneAlternat  = TagCaracter(nome='foneAlternat' , tamanho=[1, 13], raiz='//contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.emailPrinc    = TagCaracter(nome='emailPrinc'   , tamanho=[1, 60], raiz='//contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.emailAlternat = TagCaracter(nome='emailAlternat', tamanho=[1, 60], raiz='//contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<contato>'
        xml += self.fonePrinc.xml
        xml += self.foneAlternat.xml
        xml += self.emailPrinc.xml
        xml += self.emailAlternat.xml
        xml += '</contato>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.fonePrinc.xml = arquivo
            self.foneAlternat.xml = arquivo
            self.emailPrinc.xml = arquivo
            self.emailAlternat.xml = arquivo

    xml = property(get_xml, set_xml)


class Aposentadoria(XMLNFe):
    def __init__(self):
        super(Aposentadoria, self).__init__()
        self.trabAposent = TagCaracter(nome='trabAposent', tamanho=[1, 1], raiz='//aposentadoria', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<aposentadoria>'
        xml += self.trabAposent.xml
        xml += '</aposentadori>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.trabAposent.xml = arquivo

    xml = property(get_xml, set_xml)


class Dependente(XMLNFe):
    def __init__(self):
        super(Dependente, self).__init__()
        self.tpDep            = TagCaracter(nome='tpDep'           , tamanho=[1,  2], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmDep            = TagCaracter(nome='nmDep'           , tamanho=[1, 70], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtNascto         = TagData(    nome='dtNascto'        ,                  raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cpfDep           = TagCaracter(nome='cpfDep'          , tamanho=[1, 11], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.depIRRF          = TagCaracter(nome='depIRRF'         , tamanho=[1,  1], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.depSF            = TagCaracter(nome='depSF'           , tamanho=[1,  1], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.incTrab          = TagCaracter(nome='incTrab'         , tamanho=[1,  1], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dependente>'
        xml += self.tpDep.xml
        xml += self.nmDep.xml
        xml += self.dtNascto.xml
        xml += self.cpfDep.xml
        xml += self.depIRRF.xml
        xml += self.depSF.xml
        xml += self.incTrab.xml
        xml += '</dependente>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpDep.xml = arquivo
            self.nmDep.xml = arquivo
            self.dtNascto.xml = arquivo
            self.cpfDep.xml = arquivo
            self.depIRRF.xml = arquivo
            self.depSF.xml = arquivo
            self.incTrab.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoDeficiencia(XMLNFe):
    def __init__(self):
        super(InfoDeficiencia, self).__init__()
        self.defFisica        = TagCaracter(nome='defFisica'       , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.defVisual        = TagCaracter(nome='defVisual'       , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.defAuditiva      = TagCaracter(nome='defAuditiva'     , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.defMental        = TagCaracter(nome='defMental'       , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.defIntelectual   = TagCaracter(nome='defIntelectual'  , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.reabReadp        = TagCaracter(nome='reabReadp'       , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoCota         = TagCaracter(nome='infoCota'        , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.observacao       = TagCaracter(nome='observacao'      , tamanho=[1, 255], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoDeficiencia>'
        xml += self.defFisica.xml
        xml += self.defVisual.xml
        xml += self.defAuditiva.xml
        xml += self.defMental.xml
        xml += self.defIntelectual.xml
        xml += self.reabReadp.xml
        xml += self.infoCota.xml
        xml += self.observacao.xml
        xml += '</infoDeficiencia>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.defFisica.xml = arquivo
            self.defVisual.xml = arquivo
            self.defAuditiva.xml = arquivo
            self.defMental.xml = arquivo
            self.defIntelectual.xml = arquivo
            self.reabReadp.xml = arquivo
            self.infoCota.xml = arquivo
            self.observacao.xml = arquivo

    xml = property(get_xml, set_xml)


class TrabEstrangeiro(XMLNFe):
    def __init__(self):
        super(TrabEstrangeiro, self).__init__()
        self.dtChegada        = TagData(    nome='dtChegada'       ,                 raiz='//trabEstrangeiro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.classTrabEstrang = TagCaracter(nome='classTrabEstrang', tamanho=[1, 2], raiz='//trabEstrangeiro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.casadoBr         = TagCaracter(nome='casadoBr'        , tamanho=[1, 1], raiz='//trabEstrangeiro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.filhosBr         = TagCaracter(nome='filhosBr'        , tamanho=[1, 1], raiz='//trabEstrangeiro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<trabEstrangeiro>'
        xml += self.dtChegada.xml
        xml += self.classTrabEstrang.xml
        xml += self.casadoBr.xml
        xml += self.filhosBr.xml
        xml += '</trabEstrangeiro>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtChegada.xml = arquivo
            self.classTrabEstrang.xml = arquivo
            self.casadoBr.xml = arquivo
            self.filhosBr.xml = arquivo

    xml = property(get_xml, set_xml)


class Exterior(XMLNFe):
    def __init__(self):
        super(Exterior, self).__init__()
        self.paisResid    = TagCaracter(nome='paisResid'   , tamanho=[1,  3], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscLograd    = TagCaracter(nome='dscLograd'   , tamanho=[1, 80], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrLograd     = TagCaracter(nome='nrLograd'    , tamanho=[1, 10], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.complemento  = TagCaracter(nome='complemento' , tamanho=[1, 30], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.bairro       = TagCaracter(nome='bairro'      , tamanho=[1, 60], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmCid        = TagCaracter(nome='nmCid'       , tamanho=[1, 50], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codPostal    = TagCaracter(nome='codPostal'   , tamanho=[1, 12], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<exterior>'
        xml += self.paisResid.xml
        xml += self.dscLograd.xml
        xml += self.nrLograd.xml
        xml += self.complemento.xml
        xml += self.bairro.xml
        xml += self.nmCid.xml
        xml += self.codPostal.xml
        xml += '</exterior>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.paisResid.xml = arquivo
            self.dscLograd.xml = arquivo
            self.nrLograd.xml = arquivo
            self.complemento.xml = arquivo
            self.bairro.xml = arquivo
            self.nmCid.xml = arquivo
            self.codPostal.xml = arquivo

    xml = property(get_xml, set_xml)


class Brasil(XMLNFe):
    def __init__(self):
        super(Brasil, self).__init__()
        self.tpLograd     = TagCaracter(nome='tpLograd'    , tamanho=[1,  4], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscLograd    = TagCaracter(nome='dscLograd'   , tamanho=[1, 80], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrLograd     = TagCaracter(nome='nrLograd'    , tamanho=[1, 10], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.complemento  = TagCaracter(nome='complemento' , tamanho=[1, 30], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.bairro       = TagCaracter(nome='bairro'      , tamanho=[1, 60], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.cep          = TagCaracter(nome='cep'         , tamanho=[1,  8], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMunic     = TagCaracter(nome='codMunic'    , tamanho=[1,  7], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.uf           = TagCaracter(nome='uf'          , tamanho=[1,  2], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<brasil>'
        xml += self.tpLograd.xml
        xml += self.dscLograd.xml
        xml += self.nrLograd.xml
        xml += self.complemento.xml
        xml += self.bairro.xml
        xml += self.cep.xml
        xml += self.codMunic.xml
        xml += self.uf.xml
        xml += '</brasil>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpLograd.xml = arquivo
            self.dscLograd.xml = arquivo
            self.nrLograd.xml = arquivo
            self.complemento.xml = arquivo
            self.bairro.xml = arquivo
            self.cep.xml = arquivo
            self.codMunic.xml = arquivo
            self.uf.xml = arquivo

    xml = property(get_xml, set_xml)


class CNH(XMLNFe):
    def __init__(self):
        super(CNH, self).__init__()
        self.nrRegCnh     = TagCaracter(nome='nrRegCnh'    , tamanho=[1, 12], raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtExped      = TagData(    nome='dtExped'     ,                  raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.ufCnh        = TagCaracter(nome='ufCnh'       , tamanho=[1,  2], raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtValid      = TagData(    nome='dtValid'     ,                  raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtPriHab     = TagData(    nome='dtPriHab'    ,                  raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.categoriaCnh = TagCaracter(nome='categoriaCnh', tamanho=[1,  2], raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<CNH>'
        xml += self.nrRegCnh.xml
        xml += self.dtExped.xml
        xml += self.ufCnh.xml
        xml += self.dtValid.xml
        xml += self.dtPriHab.xml
        xml += self.categoriaCnh.xml
        xml += '</CNH>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRegCnh.xml = arquivo
            self.dtExped.xml = arquivo
            self.ufCnh.xml = arquivo
            self.dtValid.xml = arquivo
            self.dtPriHab.xml = arquivo
            self.categoriaCnh.xml = arquivo

    xml = property(get_xml, set_xml)


class OC(XMLNFe):
    def __init__(self):
        super(OC, self).__init__()
        self.nrOc         = TagCaracter(nome='nrOc'        , tamanho=[1, 14], raiz='//OC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.orgaoEmissor = TagCaracter(nome='orgaoEmissor', tamanho=[1, 20], raiz='//OC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtExped      = TagData(    nome='dtExped'     ,                  raiz='//OC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtValid      = TagData(    nome='dtValid'     ,                  raiz='//OC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<OC>'
        xml += self.nrOc.xml
        xml += self.orgaoEmissor.xml
        xml += self.dtExped.xml
        xml += self.dtValid.xml
        xml += '</OC>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrOc.xml = arquivo
            self.orgaoEmissor.xml = arquivo
            self.dtExped.xml = arquivo
            self.dtValid.xml = arquivo

    xml = property(get_xml, set_xml)


class RNE(XMLNFe):
    def __init__(self):
        super(RNE, self).__init__()
        self.nrRne        = TagCaracter(nome='nrRne'       , tamanho=[1, 14], raiz='//RNE', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.orgaoEmissor = TagCaracter(nome='orgaoEmissor', tamanho=[1, 20], raiz='//RNE', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtExped      = TagData(    nome='dtExped'     ,                  raiz='//RNE', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RNE>'
        xml += self.nrRne.xml
        xml += self.orgaoEmissor.xml
        xml += self.dtExped.xml
        xml += '</RNE>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRne.xml = arquivo
            self.orgaoEmissor.xml = arquivo
            self.dtExped.xml = arquivo

    xml = property(get_xml, set_xml)


class RG(XMLNFe):
    def __init__(self):
        super(RG, self).__init__()
        self.nrRg         = TagCaracter(nome='nrRg'        , tamanho=[1, 14], raiz='//RG', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.orgaoEmissor = TagCaracter(nome='orgaoEmissor', tamanho=[1, 20], raiz='//RG', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtExped      = TagData(    nome='dtExped'     ,                  raiz='//RG', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RG>'
        xml += self.nrRg.xml
        xml += self.orgaoEmissor.xml
        xml += self.dtExped.xml
        xml += '</RG>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRg.xml = arquivo
            self.orgaoEmissor.xml = arquivo
            self.dtExped.xml = arquivo

    xml = property(get_xml, set_xml)


class RIC(XMLNFe):
    def __init__(self):
        super(RIC, self).__init__()
        self.nrRic        = TagCaracter(nome='nrRic'       , tamanho=[1, 14], raiz='//RIC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.orgaoEmissor = TagCaracter(nome='orgaoEmissor', tamanho=[1, 20], raiz='//RIC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtExped      = TagData(    nome='dtExped'     ,                  raiz='//RIC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RIC>'
        xml += self.nrRic.xml
        xml += self.orgaoEmissor.xml
        xml += self.dtExped.xml
        xml += '</RIC>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRic.xml = arquivo
            self.orgaoEmissor.xml = arquivo
            self.dtExped.xml = arquivo

    xml = property(get_xml, set_xml)


class CTPS(XMLNFe):
    def __init__(self):
        super(CTPS, self).__init__()
        self.nrCtps    = TagCaracter(nome='nrCtps'   , tamanho=[1, 11], raiz='//CTPS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.serieCtps = TagCaracter(nome='serieCtps', tamanho=[1,  5], raiz='//CTPS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ufCtps    = TagCaracter(nome='ufCtps'   , tamanho=[1,  2], raiz='//CTPS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<CTPS>'
        xml += self.nrCtps.xml
        xml += self.serieCtps.xml
        xml += self.ufCtps.xml
        xml += '</CTPS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrCtps.xml = arquivo
            self.serieCtps.xml = arquivo
            self.ufCtps.xml = arquivo

    xml = property(get_xml, set_xml)


class Endereco(XMLNFe):
    def __init__(self):
        super(Endereco, self).__init__()
        self.brasil = []
        self.exterior = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<endereco>'
        if len(self.brasil) > 0:
            for b in self.brasil:
                xml += b.xml
        if len(self.exterior) > 0:
            for e in self.exterior:
                xml += e.xml
        xml += '</endereco>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.brasil = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/endereco/brasil', CTPS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.exterior = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/endereco/exterior', CTPS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Documentos(XMLNFe):
    def __init__(self):
        super(Documentos, self).__init__()
        self.CTPS        = []
        self.RIC         = []
        self.RG          = []
        self.RNE         = []
        self.OC          = []
        self.CNH         = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<documentos>'
        if len(self.CTPS) > 0:
            for c in self.CTPS:
                xml += c.xml
        if len(self.RIC) > 0:
            for r in self.RIC:
                xml += r.xml
        if len(self.RG) > 0:
            for r in self.RG:
                xml += r.xml
        if len(self.RNE) > 0:
            for r in self.RNE:
                xml += r.xml
        if len(self.OC) > 0:
            for o in self.OC:
                xml += o.xml
        if len(self.CNH) > 0:
            for c in self.CNH:
                xml += c.xml
        xml += '</documentos>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CTPS = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/documentos/CTPS', CTPS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.RIC  = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/documentos/RIC' , RIC , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.RG   = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/documentos/RG'  , RG  , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.RNE  = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/documentos/RNE' , RNE , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.OC   = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/documentos/OC'  , OC  , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.CNH  = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/documentos/CNH' , CNH , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Nascimento(XMLNFe):
    def __init__(self):
        super(Nascimento, self).__init__()
        self.dtNascto    = TagData(    nome='dtNascto', raiz='//eSocial/evtTSVInicio/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMunic    = TagCaracter(nome='codMunic', tamanho=[1, 7] , raiz='//eSocial/evtTSVInicio/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.uf          = TagCaracter(nome='uf', tamanho=[1, 2] , raiz='//eSocial/evtTSVInicio/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.paisNascto  = TagCaracter(nome='paisNascto', tamanho=[1, 3] , raiz='//eSocial/evtTSVInicio/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.paisNac     = TagCaracter(nome='paisNac', tamanho=[1, 3] , raiz='//eSocial/evtTSVInicio/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmMae       = TagCaracter(nome='nmMae', tamanho=[1, 70], raiz='//eSocial/evtTSVInicio/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmPai       = TagCaracter(nome='nmPai', tamanho=[1, 70], raiz='//eSocial/evtTSVInicio/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<nascimento>'
        xml += self.dtNascto.xml
        xml += self.codMunic.xml
        xml += self.uf.xml
        xml += self.paisNascto.xml
        xml += self.paisNac.xml
        xml += self.nmMae.xml
        xml += self.nmPai.xml
        xml += '</nascimento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtNascto.xml = arquivo
            self.codMunic.xml = arquivo
            self.uf.xml = arquivo
            self.paisNascto.xml = arquivo
            self.paisNac.xml = arquivo
            self.nmMae.xml = arquivo
            self.nmPai.xml = arquivo

    xml = property(get_xml, set_xml)


class Trabalhador(XMLNFe):
    def __init__(self):
        super(Trabalhador, self).__init__()
        self.cpfTrab    = TagCaracter(nome='cpfTrab'   , tamanho=[1, 11], raiz='//eSocial/evtTSVInicio/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab    = TagCaracter(nome='nisTrab'   , tamanho=[1, 11], raiz='//eSocial/evtTSVInicio/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmTrab     = TagCaracter(nome='nmTrab'    , tamanho=[1, 70], raiz='//eSocial/evtTSVInicio/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.sexo       = TagCaracter(nome='sexo'      , tamanho=[1, 1] , raiz='//eSocial/evtTSVInicio/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.racaCor    = TagCaracter(nome='racaCor'   , tamanho=[1, 1] , raiz='//eSocial/evtTSVInicio/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.estCiv     = TagCaracter(nome='estCiv'    , tamanho=[1, 1] , raiz='//eSocial/evtTSVInicio/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.grauInstr  = TagCaracter(nome='grauInstr' , tamanho=[1, 2] , raiz='//eSocial/evtTSVInicio/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmSoc      = TagCaracter(nome='nmSoc'     , tamanho=[1, 70], raiz='//eSocial/evtTSVInicio/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nascimento = Nascimento()
        self.documentos = Documentos()
        self.endereco   = Endereco()
        self.trabEstrangeiro = []
        self.infoDeficiencia = []
        self.dependente      = []
        self.aposentadoria   = []
        self.contato         = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<trabalhador>'
        xml += self.cpfTrab.xml
        xml += self.nisTrab.xml
        xml += self.nmTrab.xml
        xml += self.sexo.xml
        xml += self.racaCor.xml
        xml += self.estCiv.xml
        xml += self.grauInstr.xml
        xml += self.nmSoc.xml
        xml += self.nascimento.xml
        xml += self.documentos.xml
        xml += self.endereco.xml
        if len(self.trabEstrangeiro) > 0:
            for t in self.trabEstrangeiro:
                xml += t.xml
        if len(self.infoDeficiencia) > 0:
            for i in self.infoDeficiencia:
                xml += i.xml
        if len(self.dependente) > 0:
            for d in self.dependente:
                xml += d.xml
        if len(self.aposentadoria) > 0:
            for a in self.aposentadoria:
                xml += a.xml
        if len(self.contato) > 0:
            for c in self.contato:
                xml += c.xml
        xml += '</trabalhador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrab.xml = arquivo
            self.nisTrab.xml = arquivo
            self.nmTrab.xml = arquivo
            self.sexo.xml = arquivo
            self.racaCor.xml = arquivo
            self.estCiv.xml = arquivo
            self.grauInstr.xml = arquivo
            self.nmSoc.xml = arquivo
            self.nascimento.xml = arquivo
            self.documentos.xml = arquivo
            self.endereco.xml = arquivo
            self.trabEstrangeiro = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/trabEstrangeiro', TrabEstrangeiro, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoDeficiencia = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/infoDeficiencia', InfoDeficiencia, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.dependente = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/dependente', Dependente, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.aposentadoria = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/aposentadoria', Aposentadoria, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.contato = self.le_grupo('//eSocial/evtTSVInicio/trabalhador/contato', Contato, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtTSVInicio/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtTSVInicio/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif = TagInteiro( nome='indRetif', raiz='//eSocial/evtTSVInicio/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', raiz='//eSocial/evtTSVInicio/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpAmb    = TagInteiro( nome='tpAmb'   , raiz='//eSocial/evtTSVInicio/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi  = TagInteiro( nome='procEmi' , raiz='//eSocial/evtTSVInicio/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc  = TagCaracter(nome='verProc' , raiz='//eSocial/evtTSVInicio/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtTSVInicio(XMLNFe):
    def __init__(self):
        super(EvtTSVInicio, self).__init__()
        self.Id = TagCaracter(nome='evtTSVInicio', propriedade='Id', raiz='//eSocial/evtTSVInicio', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.trabalhador = Trabalhador()
        self.infoTSVInicio = InfoTSVInicio()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.trabalhador.xml
        xml += self.infoTSVInicio.xml
        xml += '</evtTSVInicio>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.trabalhador.xml = arquivo
            self.infoTSVInicio.xml = arquivo

    xml = property(get_xml, set_xml)


class S2300(XMLNFe):
    def __init__(self):
        super(S2300, self).__init__()
        self.evtTSVInicio = EvtTSVInicio()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtTSVInicio.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtTSVInicio
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtTSVInicio.xml

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
            self.evtTSVInicio.xml = arquivo
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
        self.evtTSVInicio.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
