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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtAltContratual/v02_04_02'


class ServPubl(XMLNFe):
    def __init__(self):
        super(ServPubl, self).__init__()
        self.mtvAlter = TagInteiro(nome='mtvAlter', raiz='//servPubl', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<servPubl>'
        xml += self.mtvAlter.xml
        xml += '</servPubl>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.mtvAlter.xml = arquivo

    xml = property(get_xml, set_xml)


class Observacoes(XMLNFe):
    def __init__(self):
        super(Observacoes, self).__init__()
        self.observacao = TagCaracter(nome='observacao', tamanho=[1, 255], raiz='//observacoes', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<observacoes>'
        xml += self.observacao.xml
        xml += '</observacoes>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.observacao.xml = arquivo

    xml = property(get_xml, set_xml)


class AlvaraJudicial(XMLNFe):
    def __init__(self):
        super(AlvaraJudicial, self).__init__()
        self.nrProcJud = TagCaracter(nome='nrProcJud', tamanho=[1, 20], raiz='//alvaraJudicial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<alvaraJudicial>'
        xml += self.nrProcJud.xml
        xml += '</alvaraJudicial>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrProcJud.xml = arquivo

    xml = property(get_xml, set_xml)


class FiliacaoSindical(XMLNFe):
    def __init__(self):
        super(FiliacaoSindical, self).__init__()
        self.cnpjSindTrab = TagCaracter(nome='cnpjSindTrab', tamanho=[1, 14], raiz='//filiacaoSindical', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<filiacaoSindical>'
        xml += self.cnpjSindTrab.xml
        xml += '</filiacaoSindical>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjSindTrab.xml = arquivo

    xml = property(get_xml, set_xml)


class Horario(XMLNFe):
    def __init__(self):
        super(Horario, self).__init__()
        self.dia = TagInteiro(nome='dia', raiz='//horario', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codHorContrat = TagCaracter(nome='codHorContrat', tamanho=[1, 30], raiz='//horario', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<horario>'
        xml += self.dia.xml
        xml += self.codHorContrat.xml
        xml += '</horario>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dia.xml = arquivo
            self.codHorContrat.xml = arquivo

    xml = property(get_xml, set_xml)


class HorContratual(XMLNFe):
    def __init__(self):
        super(HorContratual, self).__init__()
        self.qtdHrsSem = TagInteiro(nome='qtdHrsSem', raiz='//horContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpJornada = TagInteiro(nome='tpJornada', raiz='//horContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscTpJorn = TagCaracter(nome='dscTpJorn', tamanh=[1, 100], raiz='//horContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tmpParc = TagCaracter(nome='tmpParc', tamanho=[1, 1], raiz='//horContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.horario = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<horContratual>'
        xml += self.qtdHrsSem.xml
        xml += self.tpJornada.xml
        xml += self.dscTpJorn.xml
        xml += self.tmpParc.xml
        for horario in self.horario:
            xml += horario.xml
        xml += '</horContratual>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.qtdHrsSem.xml = arquivo
            self.tpJornada.xml = arquivo
            self.dscTpJorn.xml = arquivo
            self.tmpParc.xml = arquivo
            self.horario = self.le_grupo('//eSocial/evtAltContratual/altContratual/infoContrato/horContratual/horario', Horario, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class LocalTrabDom(XMLNFe):
    def __init__(self):
        super(LocalTrabDom, self).__init__()
        self.tpLograd = TagCaracter(nome='tpLograd', tamanho=[1, 4], raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscLograd = TagCaracter(nome='dscLograd', tamanho=[1, 80], raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrLograd = TagCaracter(nome='nrLograd', tamanho=[1, 10], raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.complemento = TagCaracter(nome='complemento', tamanho=[1, 30], raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.bairro = TagCaracter(nome='bairro', tamanho=[1, 60], raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.cep = TagCaracter(nome='cep', tamanho=[1, 60], raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMunic = TagInteiro(nome='codMunic', raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.uf = TagCaracter(nome='uf', tamanho=[1, 2], raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<localTrabDom>'
        xml += self.tpLograd.xml
        xml += self.dscLograd.xml
        xml += self.nrLograd.xml
        xml += self.complemento.xml
        xml += self.bairro.xml
        xml += self.cep.xml
        xml += self.codMunic.xml
        xml += self.uf.xml
        xml += '</localTrabDom>'

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


class LocalTrabGeral(XMLNFe):
    def __init__(self):
        super(LocalTrabGeral, self).__init__()
        self.tpInsc = TagInteiro(nome='tpInsc', raiz='//localTrabGeral', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//localTrabGeral', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.descComp = TagCaracter(nome='descComp', tamanho=[1, 80], raiz='//localTrabGeral', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<localTrabGeral>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.descComp.xml
        xml += '</localTrabGeral>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.descComp.xml = arquivo

    xml = property(get_xml, set_xml)


class LocalTrabalho(XMLNFe):
    def __init__(self):
        super(LocalTrabalho, self).__init__()
        self.localTrabGeral = []
        self.localTrabDom = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<localTrabalho>'
        for geral in self.localTrabGeral:
            xml += geral.xml
        for domestico in self.localTrabDom:
            xml += domestico.xml
        xml += '</localTrabalho>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.localTrabGeral = self.le_grupo('//eSocial/evtAltContratual/altContratual/infoContrato/localTrabalho/localTrabGeral', LocalTrabGeral, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.localTrabDom = self.le_grupo('//eSocial/evtAltContratual/altContratual/infoContrato/localTrabalho/localTrabDom', LocalTrabDom, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Duracao(XMLNFe):
    def __init__(self):
        super(Duracao, self).__init__()
        self.tpContr = TagInteiro(nome='tpContr', raiz='//duracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtTerm = TagData(nome='dtTerm', raiz='//duracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<duracao>'
        xml += self.tpContr.xml
        xml += self.dtTerm.xml
        xml += '</duracao>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(self, arquivo):
            self.tpContr.xml = arquivo
            self.dtTerm.xml = arquivo

    xml = property(get_xml, set_xml)


class Remuneracao(XMLNFe):
    def __init__(self):
        super(Remuneracao, self).__init__()
        self.vrSalFx = TagDecimal(nome='vrSalFx', tamanho=[1, 14, 2], raiz='//remuneracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.undSalFixo = TagInteiro(nome='undSalFixo', raiz='//remuneracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.descSalVar = TagCaracter(nome='descSalVar', tamanho=[1, 255], raiz='//remuneracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<remuneracao>'
        xml += self.vrSalFx.xml
        xml += self.undSalFixo.xml
        xml += self.descSalVar.xml
        xml += '</remuneracao>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vrSalFx.xml = arquivo
            self.undSalFixo.xml = arquivo
            self.descSalVar.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoContrato(XMLNFe):
    def __init__(self):
        super(InfoContrato, self).__init__()
        self.codCargo = TagCaracter(nome='codCargo', tamanho=[1, 30], raiz='//infoContrato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codFuncao = TagCaracter(nome='codFuncao', tamanho=[1, 30], raiz='//infoContrato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg = TagInteiro(nome='codCateg', raiz='//infoContrato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codCarreira = TagCaracter(nome='codCarreira', tamanho=[1, 30], raiz='//infoContrato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtIngrCarr = TagData(nome='dtIngrCarr', raiz='//infoContrato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.remuneracao = Remuneracao()
        self.duracao = Duracao()
        self.localTrabalho = LocalTrabalho()
        self.horContratual = []
        self.filiacaoSindical = []
        self.alvaraJudicial = []
        self.observacoes = []
        self.servPubl = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoContrato>'
        xml += self.codCargo.xml
        xml += self.codFuncao.xml
        xml += self.codCateg.xml
        xml += self.codCarreira.xml
        xml += self.dtIngrCarr.xml
        xml += self.remuneracao.xml
        xml += self.duracao.xml
        xml += self.localTrabalho.xml
        for horario in self.horContratual:
            xml += horario.xml
        for filiacao in self.filiacaoSindical:
            xml += filiacao.xml
        for alvara in self.alvaraJudicial:
            xml += alvara.xml
        for observacao in self.observacoes:
            xml += observacao.xml
        for serv in self.servPubl:
            xml += serv.xml
        xml += '</infoContrato>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codCargo.xml = arquivo
            self.codFuncao.xml = arquivo
            self.codCateg.xml = arquivo
            self.codCarreira.xml = arquivo
            self.dtIngrCarr.xml = arquivo
            self.remuneracao.xml = arquivo
            self.duracao.xml = arquivo
            self.localTrabalho.xml = arquivo
            self.horContratual.xml = self.le_grupo('//eSocial/evtAltContratual/altContratual/infoContrato/horContratual', HorContratual, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.filiacaoSindical.xml = self.le_grupo('//eSocial/evtAltContratual/altContratual/infoContrato/filiacaoSindical', FiliacaoSindical, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.alvaraJudicial.xml = self.le_grupo('//eSocial/evtAltContratual/altContratual/infoContrato/alvaraJudicial', AlvaraJudicial, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.observacoes.xml = self.le_grupo('//eSocial/evtAltContratual/altContratual/infoContrato/observacoes', Observacoes, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.servPubl.xml = self.le_grupo('//eSocial/evtAltContratual/altContratual/infoContrato/servPubl', ServPubl, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoEstatutario(XMLNFe):
    def __init__(self):
        super(InfoEstatutario, self).__init__()
        self.tpPlanRP = TagInteiro(nome='tpPlanRP', raiz='//tpPlanRP', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoEstatutario>'
        xml += self.tpPlanRP.xml
        xml += '</infoEstatutario>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpPlanRP.xml = arquivo

    xml = property(get_xml, set_xml)


class Aprend(XMLNFe):
    def __init__(self):
        super(Aprend, self).__init__()
        self.tpInsc = TagInteiro(nome='tpInsc', raiz='//aprend', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//aprend', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<aprend>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</aprend>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class TrabTemp(XMLNFe):
    def __init__(self):
        super(TrabTemp, self).__init__()
        self.justProrr = TagCaracter(nome='justProrr', tamanho=[1, 999], raiz='//trabTemp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<trabTemp>'
        xml += self.justProrr.xml
        xml += '</trabTemp>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.justProrr.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoCeletista(XMLNFe):
    def __init__(self):
        super(InfoCeletista, self).__init__()
        self.tpRegJor = TagInteiro(nome='tpRegJor', raiz='//infoCeletista', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.natAtividade = TagInteiro(nome='natAtividade', raiz='//infoCeletista', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtBase = TagInteiro(nome='dtBase', raiz='//infoCeletista', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.cnpjSindCategProf = TagCaracter(nome='cnpjSindCategProf', tamanho=[1, 14], raiz='//infoCeletista', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.trabTemp = []
        self.aprend = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCeletista>'
        xml += self.tpRegJor.xml
        xml += self.natAtividade.xml
        xml += self.dtBase.xml
        xml += self.cnpjSindCategProf.xml
        for temporario in self.trabTemp:
            xml += temporario.xml
        for aprendiz in self.aprend:
            xml += aprendiz.xml
        xml += '</infoCeletista>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpRegJor.xml = arquivo
            self.natAtividade.xml = arquivo
            self.dtBase.xml = arquivo
            self.cnpjSindCategProf.xml = arquivo
            self.trabTemp = self.le_grupo('//eSocial/evtAltContratual/altContratual/vinculo/infoCeletista/trabTemp', TrabTemp, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.aprend = self.le_grupo('//eSocial/evtAltContratual/altContratual/vinculo/infoCeletista/aprend', Aprend, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoRegimeTrab(XMLNFe):
    def __init__(self):
        super(InfoRegimeTrab, self).__init__()
        self.infoCeletista = []
        self.infoEstatutario = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoRegimeTrab>'
        for infoCele in self.infoCeletista:
            xml += infoCele.xml
        for infoEsta in self.infoEstatutario:
            xml += infoEsta.xml
        xml += '</infoRegimeTrab>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infoCeletista = self.le_grupo('//eSocial/evtAltContratual/altContratual/vinculo/infoCeletista', InfoCeletista, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoEstatutario = self.le_grupo('//eSocial/evtAltContratual/altContratual/vinculo/infoEstatutario', InfoEstatutario, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Vinculo(XMLNFe):
    def __init__(self):
        super(Vinculo, self).__init__()
        self.tpRegPrev = TagInteiro(nome='tpRegPrev', raiz='//vinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<vinculo>'
        xml += self.tpRegPrev.xml
        xml += '</vinculo>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpRegPrev.xml = arquivo

    xml = property(get_xml, set_xml)


class AltContratual(XMLNFe):
    def __init__(self):
        super(AltContratual, self).__init__()
        self.dtAlteracao = TagData(nome='dtAlteracao', raiz='//eSocial/evtAltContratual/altContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtEf = TagData(nome='dtEf', raiz='//eSocial/evtAltContratual/altContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dscAlt = TagCaracter(nome='dscAlt', tamanho=[1, 150], raiz='//eSocial/evtAltContratual/altContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vinculo = []
        self.infoRegimeTrab = []
        self.infoContrato = InfoContrato()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<altContratual>'
        xml += self.dtAlteracao.xml
        xml += self.dtEf.xml
        xml += self.dscAlt.xml
        for vinculo in self.vinculo:
            xml += vinculo.xml
        for infoReg in self.infoRegimeTrab:
            xml += infoReg.xml
        xml += self.infoContrato.xml
        xml += '</altContratual>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtAlteracao.xml = arquivo
            self.dtEf.xml = arquivo
            self.dscAlt.xml = arquivo
            self.vinculo = self.le_grupo('//eSocial/evtAltContratual/altContratual/vinculo', Vinculo, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoRegimeTrab = self.le_grupo('//eSocial/evtAltContratual/altContratual/infoRegimeTrab', InfoRegimeTrab, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoContrato = arquivo

    xml = property(get_xml, set_xml)


class IdeVinculo(XMLNFe):
    def __init__(self):
        super(IdeVinculo, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', tamanho=[1, 11], raiz='//eSocial/evtAltContratual/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab = TagCaracter(nome='nisTrab', tamanho=[1, 11], raiz='//eSocial/evtAltContratual/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.matricula = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//eSocial/evtAltContratual/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.tpInsc = TagInteiro(nome='tpInsc', raiz='//eSocial/evtAltContratual/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtAltContratual/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif = TagInteiro(nome='indRetif', raiz='//eSocial/evtAltContratual/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrRecibo = TagCaracter(nome='nrRecibo', tamanho=[1, 40], raiz='//eSocial/evtAltContratual/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpAmb = TagInteiro(nome='tpAmb', raiz='//eSocial/evtAltContratual/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.procEmi = TagInteiro(nome='procEmi', raiz='//eSocial/evtAltContratual/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', raiz='//eSocial/evtAltContratual/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtAltContratual(XMLNFe):
    def __init__(self):
        super(EvtAltContratual, self).__init__()
        self.Id = TagCaracter(nome='evtAltContratual', propriedade='Id', raiz='//eSocial/evtAltContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideVinculo = IdeVinculo()
        self.altContratual = AltContratual()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideVinculo.xml
        xml += self.altContratual.xml
        xml += '</evtAltContratual>'

        return xml

    def set_xml(self, arquivo):
        if self._le_arquivo(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = self.le_grupo('//eSocial/evtAltContratual/ideEvento', IdeEvento, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.ideEmpregador.xml = self.le_grupo('//eSocial/evtAltContratual/ideEmpregador', IdeEmpregador, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.ideVinculo.xml = self.le_grupo('//eSocial/evtAltContratual/ideVinculo', IdeVinculo, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.altContratual = self.le_grupo('//eSocial/evtAltContratual/altContratual', AltContratual, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class S2206(XMLNFe):
    def __init__(self):
        super(S2206, self).__init__()
        self.evtAltCadastral = EvtAltContratual()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtAltContratual.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtAltCadastral
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtAltCadastral.xml
        xml += '</eSocial>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtAltCadastral.xml = arquivo

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
        self.evtAltCadastral.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
