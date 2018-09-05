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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtAdmissao/v02_04_02'


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


class Desligamento(XMLNFe):
    def __init__(self):
        super(Desligamento, self).__init__()
        self.dtDeslig = TagData(nome='dtDeslig', raiz='//desligamento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<desligamento>'
        xml += self.dtDeslig.xml
        xml += '</desligamento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtDeslig.xml = arquivo

    xml = property(get_xml, set_xml)


class Afastamento(XMLNFe):
    def __init__(self):
        super(Afastamento, self).__init__()
        self.dtIniAfast  = TagData(    nome='dtIniAfast',                    raiz='//transfDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMotAfast = TagCaracter(nome='codMotAfast', tamanho=[1, 11],  raiz='//transfDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class TransfDom(XMLNFe):
    def __init__(self):
        super(TransfDom, self).__init__()
        self.cpfSubstituido = TagCaracter(nome='cpfSubstituido', tamanho=[1, 11],  raiz='//transfDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.matricAnt      = TagCaracter(nome='matricAnt',      tamanho=[1, 30],  raiz='//transfDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtTransf       = TagData(    nome='dtTransf',                         raiz='//transfDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<transfDom>'
        xml += self.cpfSubstituido.xml
        xml += self.matricAnt.xml
        xml += self.dtTransf.xml
        xml += '</transfDom>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfSubstituido.xml = arquivo
            self.matricAnt.xml = arquivo
            self.dtTransf.xml = arquivo

    xml = property(get_xml, set_xml)


class SucessaoVinc(XMLNFe):
    def __init__(self):
        super(SucessaoVinc, self).__init__()
        self.cnpjEmpregAnt = TagCaracter(nome='cnpjEmpregAnt', tamanho=[1, 14],  raiz='//sucessaoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.matricAnt     = TagCaracter(nome='matricAnt',     tamanho=[1, 30],  raiz='//sucessaoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtTransf      = TagData(    nome='dtTransf',                        raiz='//sucessaoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.observacao    = TagCaracter(nome='observacao',    tamanho=[1, 255], raiz='//sucessaoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<sucessaoVinc>'
        xml += self.cnpjEmpregAnt.xml
        xml += self.matricAnt.xml
        xml += self.dtTransf.xml
        xml += self.observacao.xml
        xml += '</sucessaoVinc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjEmpregAnt.xml = arquivo
            self.matricAnt.xml = arquivo
            self.dtTransf.xml = arquivo
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
        self.dia           = TagCaracter(nome='dia',           tamanho=[1, 1], raiz='//horario', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
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
        self.qtdHrsSem   = TagDecimal( nome='qtdHrsSem',   tamanho=[1, 4, 2], raiz='//horContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpJornada   = TagCaracter(nome='tpJornada',   tamanho=[1, 1],    raiz='//horContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscTpJorn   = TagCaracter(nome='dscTpJorn',   tamanho=[1, 100],  raiz='//horContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tmpParc     = TagCaracter(nome='tmpParc',     tamanho=[1, 1],    raiz='//horContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.horario     = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<horContratual>'
        xml += self.qtdHrsSem.xml
        xml += self.tpJornada.xml
        xml += self.dscTpJorn.xml
        xml += self.tmpParc.xml
        if len(self.horario) > 0:
            for h in self.horario:
                xml += h.xml
        xml += '</horContratual>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.qtdHrsSem.xml = arquivo
            self.tpJornada.xml = arquivo
            self.dscTpJorn.xml = arquivo
            self.tmpParc.xml = arquivo
            self.horario.xml = self.le_grupo('//horContratual/horario', Horario, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class LocalTrabDom(XMLNFe):
    def __init__(self):
        super(LocalTrabDom, self).__init__()
        self.tpLograd    = TagCaracter(nome='tpLograd',    tamanho=[1, 4],  raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscLograd   = TagCaracter(nome='dscLograd',   tamanho=[1, 80], raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrLograd    = TagCaracter(nome='nrLograd',    tamanho=[1, 10], raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.complemento = TagCaracter(nome='complemento', tamanho=[1, 30], raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.bairro      = TagCaracter(nome='bairro',      tamanho=[1, 60], raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.cep         = TagCaracter(nome='cep',         tamanho=[1, 8],  raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMunic    = TagCaracter(nome='codMunic',    tamanho=[1, 7],  raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.uf          = TagCaracter(nome='uf',          tamanho=[1, 2],  raiz='//localTrabDom', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1,  1], raiz='//localTrabGeral', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//localTrabGeral', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<localTrabGeral>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</localTrabGeral>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class LocalTrabalho(XMLNFe):
    def __init__(self):
        super(LocalTrabalho, self).__init__()
        self.localTrabGeral = []
        self.localTrabDom   = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<localTrabalho>'
        if len(self.localTrabGeral) > 0:
            for l in self.localTrabGeral:
                xml += l.xml
        if len(self.localTrabDom) > 0:
            for l in self.localTrabDom:
                xml += l.xml
        xml += '</localTrabalho>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.localTrabGeral = self.le_grupo('//eSocial/evtAdmissao/vinculo/infoContrato/localTrabalho/localTrabGeral', LocalTrabGeral, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.localTrabDom   = self.le_grupo('//eSocial/evtAdmissao/vinculo/infoContrato/localTrabalho/localTrabDom',   LocalTrabDom,   namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoContrato(XMLNFe):
    def __init__(self):
        super(InfoContrato, self).__init__()
        self.codCargo         = TagCaracter(nome='codCargo',    tamanho=[1, 30],    raiz='//eSocial/evtAdmissao/vinculo/infoContrato',             namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codFuncao        = TagCaracter(nome='codFuncao',   tamanho=[1, 30],    raiz='//eSocial/evtAdmissao/vinculo/infoContrato',             namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg         = TagCaracter(nome='codCateg',    tamanho=[1, 3],     raiz='//eSocial/evtAdmissao/vinculo/infoContrato',             namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codCarreira      = TagCaracter(nome='codCarreira', tamanho=[1, 30],    raiz='//eSocial/evtAdmissao/vinculo/infoContrato',             namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtIngrCarr       = TagData(    nome='dtIngrCarr',                      raiz='//eSocial/evtAdmissao/vinculo/infoContrato',             namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrSalFx          = TagDecimal( nome='vrSalFx',     tamanho=[1, 14, 2], raiz='//eSocial/evtAdmissao/vinculo/infoContrato/remuneracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.undSalFixo       = TagCaracter(nome='undSalFixo',  tamanho=[1, 1],     raiz='//eSocial/evtAdmissao/vinculo/infoContrato/remuneracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscSalVar        = TagCaracter(nome='dscSalVar',   tamanho=[1, 255],   raiz='//eSocial/evtAdmissao/vinculo/infoContrato/remuneracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpContr          = TagCaracter(nome='tpContr',     tamanho=[1, 1],     raiz='//eSocial/evtAdmissao/vinculo/infoContrato/duracao',     namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtTerm           = TagData(    nome='dtTerm',                          raiz='//eSocial/evtAdmissao/vinculo/infoContrato/duracao',     namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.clauAssec        = TagCaracter(nome='clauAssec',   tamanho=[1, 1],     raiz='//eSocial/evtAdmissao/vinculo/infoContrato/duracao',     namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.localTrabalho    = LocalTrabalho()
        self.horContratual    = []
        self.filiacaoSindical = []
        self.alvaraJudicial   = []
        self.observacoes      = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoContrato>'
        xml += self.codCargo.xml
        xml += self.codFuncao.xml
        xml += self.codCateg.xml
        xml += self.codCarreira.xml
        xml += self.dtIngrCarr.xml
        xml += '<remuneracao>'
        xml += self.vrSalFx.xml
        xml += self.undSalFixo.xml
        xml += self.dscSalVar.xml
        xml += '</remuneracao>'
        xml += '<duracao>'
        xml += self.tpContr.xml
        xml += self.dtTerm.xml
        xml += self.clauAssec.xml
        xml += '</duracao>'
        xml += self.localTrabalho.xml
        if len(self.horContratual) > 0:
            for h in self.horContratual:
                xml += h.xml
        if len(self.filiacaoSindical) > 0:
            for f in self.filiacaoSindical:
                xml += f.xml
        if len(self.alvaraJudicial) > 0:
            for a in self.alvaraJudicial:
                xml += a.xml
        if len(self.observacoes) > 0:
            for o in self.observacoes:
                xml += o.xml
        xml += '</infoContrato>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codCargo.xml = arquivo
            self.codFuncao.xml = arquivo
            self.codCateg.xml = arquivo
            self.codCarreira.xml = arquivo
            self.dtIngrCarr.xml = arquivo
            self.vrSalFx.xml = arquivo
            self.undSalFixo.xml = arquivo
            self.dscSalVar.xml = arquivo
            self.tpContr.xml = arquivo
            self.dtTerm.xml = arquivo
            self.clauAssec.xml = arquivo
            self.localTrabalho.xml = arquivo
            self.horContratual = self.le_grupo('//eSocial/evtAdmissao/vinculo/infoContrato/horContratual', HorContratual, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.filiacaoSindical = self.le_grupo('//eSocial/evtAdmissao/vinculo/infoContrato/filiacaoSindical', FiliacaoSindical, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.alvaraJudicial = self.le_grupo('//eSocial/evtAdmissao/vinculo/infoContrato/alvaraJudicial', AlvaraJudicial, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.observacoes = self.le_grupo('//eSocial/evtAdmissao/vinculo/infoContrato/observacoes', Observacoes, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoDecJud(XMLNFe):
    def __init__(self):
        super(InfoDecJud, self).__init__()
        self.nrProcJud = TagCaracter(nome='nrProcJud', tamanho=[1, 20], raiz='//infoDecJud', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoDecJud>'
        xml += self.nrProcJud.xml
        xml += '</infoDecJud>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrProcJud.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoEstatutario(XMLNFe):
    def __init__(self):
        super(InfoEstatutario, self).__init__()
        self.indProvim         = TagCaracter(nome='indProvim'        , tamanho=[1,  1], raiz='//infoEstatutario', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpProvim          = TagCaracter(nome='tpProvim'         , tamanho=[1,  2], raiz='//infoEstatutario', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtNomeacao        = TagData(    nome='dtNomeacao'       ,                  raiz='//infoEstatutario', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtPosse           = TagData(    nome='dtPosse'          ,                  raiz='//infoEstatutario', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtExercicio       = TagData(    nome='dtExercicio'      ,                  raiz='//infoEstatutario', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoDecJud        = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoEstatutario>'
        xml += self.indProvim.xml
        xml += self.tpProvim.xml
        xml += self.dtNomeacao.xml
        xml += self.dtPosse.xml
        xml += self.dtExercicio.xml
        if len(self.infoDecJud) > 0:
            for d in self.infoDecJud:
                xml += d.xml
        xml += '</infoEstatutario>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indProvim.xml = arquivo
            self.tpProvim.xml = arquivo
            self.dtNomeacao.xml = arquivo
            self.dtPosse.xml = arquivo
            self.dtExercicio.xml = arquivo
            self.infoDecJud = self.le_grupo('//infoEstatutario/infoDecJud', InfoDecJud, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Aprend(XMLNFe):
    def __init__(self):
        super(Aprend, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1,  1], raiz='//aprend', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
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


class IdeTrabSubstituido(XMLNFe):
    def __init__(self):
        super(IdeTrabSubstituido, self).__init__()
        self.cpfTrabSubst = TagCaracter(nome='cpfTrabSubst', tamanho=[1, 11], raiz='//ideTrabSubstituido', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideTrabSubstituido>'
        xml += self.cpfTrabSubst.xml
        xml += '</ideTrabSubstituido>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrabSubst.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEstabVinc(XMLNFe):
    def __init__(self):
        super(IdeEstabVinc, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1,  1], raiz='//ideEstabVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//ideEstabVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstabVinc>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideEstabVinc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class TrabTemporario(XMLNFe):
    def __init__(self):
        super(TrabTemporario, self).__init__()
        self.hipLeg             = TagCaracter(nome='higLeg'     , tamanho=[1,   1], raiz='//infoCeletista/trabTemporario'               , namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.justContr          = TagCaracter(nome='justContr'  , tamanho=[1, 999], raiz='//infoCeletista/trabTemporario'               , namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpInclContr        = TagCaracter(nome='tpInclContr', tamanho=[1,   1], raiz='//infoCeletista/trabTemporario'               , namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpInsc             = TagCaracter(nome='tpInsc'     , tamanho=[1,   1], raiz='//infoCeletista/trabTemporario/ideTomadorServ', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc             = TagCaracter(nome='nrInsc'     , tamanho=[1,  15], raiz='//infoCeletista/trabTemporario/ideTomadorServ', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEstabVinc       = []
        self.ideTrabSubstituido = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<trabTemporario>'
        xml += self.hipLeg.xml
        xml += self.justContr.xml
        xml += '<ideTomadorServ>'
        xml += self.tpInsc.xml
        xml += self.nrInsc
        if len(self.ideEstabVinc) > 0:
            for e in self.ideEstabVinc:
                xml += e.xml
        xml += '</ideTomadorServ>'
        if len(self.ideTrabSubstituido) > 0:
            for t in self.ideTrabSubstituido:
                xml += t.xml
        xml += '</trabTemporario>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.hipLeg.xml = arquivo
            self.justContr.xml = arquivo
            self.tpInclContr.xml = arquivo
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.ideEstabVinc = self.le_grupo('//infoCeletista/trabTemporario/ideTomadorServ/ideEstabVinc', IdeEstabVinc, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.ideTrabSubstituido = self.le_grupo('//infoCeletista/trabTemporario/ideTrabSubstituido', IdeEstabVinc, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class FGTS(XMLNFe):
    def __init__(self):
        super(FGTS, self).__init__()
        self.opcFGTS   = TagCaracter(nome='opcFGTS'  , tamanho=[1, 1], raiz='//infoCeletista/FGTS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtOpcFGTS = TagCaracter(nome='dtOpcFGTS',                 raiz='//infoCeletista/FGTS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<FGTS>'
        xml += self.opcFGTS.xml
        xml += self.dtOpcFGTS.xml
        xml += '</FGTS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.opcFGTS.xml = arquivo
            self.dtOpcFGTS.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoCeletista(XMLNFe):
    def __init__(self):
        super(InfoCeletista, self).__init__()
        self.dtAdm             = TagData(    nome='dtAdm'            ,                  raiz='//infoCeletista', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpAdmissao        = TagCaracter(nome='tpAdmissao'       , tamanho=[1,  1], raiz='//infoCeletista', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indAdmissao       = TagCaracter(nome='indAdmissao'      , tamanho=[1,  1], raiz='//infoCeletista', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpRegJor          = TagCaracter(nome='tpRegJor'         , tamanho=[1,  1], raiz='//infoCeletista', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.natAtividade      = TagCaracter(nome='natAtividade'     , tamanho=[1,  1], raiz='//infoCeletista', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtBase            = TagInteiro( nome='dtBase'           , tamanho=[1,  2], raiz='//infoCeletista', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.cnpjSindCategProf = TagCaracter(nome='cnpjSindCategProf', tamanho=[1, 14], raiz='//infoCeletista', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.FGTS              = FGTS()
        self.trabTemporario    = []
        self.aprend            = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCeletista>'
        xml += self.dtAdm.xml
        xml += self.tpAdmissao.xml
        xml += self.indAdmissao.xml
        xml += self.tpRegJor.xml
        xml += self.natAtividade.xml
        xml += self.dtBase.xml
        xml += self.cnpjSindCategProf.xml
        xml += self.FGTS.xml
        if len(self.trabTemporario) > 0:
            for t in self.trabTemporario:
                xml += t.xml
        if len(self.aprend) > 0:
            for a in self.aprend:
                xml += a.xml
        xml += '</infoCeletista>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtAdm.xml = arquivo
            self.tpAdmissao.xml = arquivo
            self.indAdmissao.xml = arquivo
            self.tpRegJor.xml = arquivo
            self.natAtividade.xml = arquivo
            self.dtBase.xml = arquivo
            self.cnpjSindCategProf.xml = arquivo
            self.FGTS.xml = arquivo
            self.trabTemporario = self.le_grupo('//infoCeletista/trabTemporario', TrabTemporario, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.aprend = self.le_grupo('//infoCeletista/aprend', Aprend, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoRegimeTrab(XMLNFe):
    def __init__(self):
        super(InfoRegimeTrab, self).__init__()
        self.infoCeletista = []
        self.infoEstatutario = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoRegimeTrab>'
        if len(self.infoCeletista) > 0:
            for c in self.infoCeletista:
                xml += c.xml
        if len(self.infoEstatutario) > 0:
            for e in self.infoEstatutario:
                xml += e.xml
        xml += '</infoRegimeTrab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infoCeletista = self.le_grupo('//eSocial/evtAdmissao/vinculo/infoRegimeTrab/infoCeletista', InfoCeletista, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoEstatutario = self.le_grupo('//eSocial/evtAdmissao/vinculo/infoRegimeTrab/infoEstatutario', InfoEstatutario, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Vinculo(XMLNFe):
    def __init__(self):
        super(Vinculo, self).__init__()
        self.matricula      = TagCaracter(nome='matricula'     , tamanho=[1, 30], raiz='//eSocial/evtAdmissao/vinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpRegTrab      = TagCaracter(nome='tpRegTrab'     , tamanho=[1,  1], raiz='//eSocial/evtAdmissao/vinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpRegPrev      = TagCaracter(nome='tpRegPrev'     , tamanho=[1,  1], raiz='//eSocial/evtAdmissao/vinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrRecInfPrelim = TagCaracter(nome='nrRecInfPrelim', tamanho=[1, 40], raiz='//eSocial/evtAdmissao/vinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.cadIni         = TagCaracter(nome='cadIni'        , tamanho=[1,  1], raiz='//eSocial/evtAdmissao/vinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoRegimeTrab = InfoRegimeTrab()
        self.infoContrato   = InfoContrato()
        self.sucessaoVinc   = []
        self.transfDom      = []
        self.afastamento    = []
        self.desligamento   = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<vinculo>'
        xml += self.matricula.xml
        xml += self.tpRegTrab.xml
        xml += self.tpRegPrev.xml
        xml += self.nrRecInfPrelim.xml
        xml += self.cadIni.xml
        xml += self.infoRegimeTrab.xml
        xml += self.infoContrato.xml
        if len(self.sucessaoVinc) > 0:
            for s in self.sucessaoVinc:
                xml += s.xml
        if len(self.transfDom) > 0:
            for d in self.transfDom:
                xml += d.xml
        if len(self.afastamento) > 0:
            for a in self.afastamento:
                xml += a.xml
        if len(self.desligamento) > 0:
            for d in self.desligamento:
                xml += d.xml
        xml += '</vinculo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.matricula.xml = arquivo
            self.tpRegTrab.xml = arquivo
            self.tpRegPrev.xml = arquivo
            self.nrRecInfPrelim.xml = arquivo
            self.cadIni.xml = arquivo
            self.infoRegimeTrab.xml = arquivo
            self.infoContrato.xml = arquivo
            self.sucessaoVinc = self.le_grupo('//eSocial/evtAdmissao/vinculo/sucessaoVinc', SucessaoVinc, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.transfDom = self.le_grupo('//eSocial/evtAdmissao/vinculo/transDom', TransfDom, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.afastamento = self.le_grupo('//eSocial/evtAdmissao/vinculo/afastamento', Afastamento, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.desligamento = self.le_grupo('//eSocial/evtAdmissao/vinculo/desligamento', Desligamento, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

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
            self.brasil = self.le_grupo('//eSocial/evtAdmissao/trabalhador/endereco/brasil', CTPS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.exterior = self.le_grupo('//eSocial/evtAdmissao/trabalhador/endereco/exterior', CTPS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

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
            self.CTPS = self.le_grupo('//eSocial/evtAdmissao/trabalhador/documentos/CTPS', CTPS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.RIC  = self.le_grupo('//eSocial/evtAdmissao/trabalhador/documentos/RIC' , RIC , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.RG   = self.le_grupo('//eSocial/evtAdmissao/trabalhador/documentos/RG'  , RG  , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.RNE  = self.le_grupo('//eSocial/evtAdmissao/trabalhador/documentos/RNE' , RNE , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.OC   = self.le_grupo('//eSocial/evtAdmissao/trabalhador/documentos/OC'  , OC  , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.CNH  = self.le_grupo('//eSocial/evtAdmissao/trabalhador/documentos/CNH' , CNH , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Nascimento(XMLNFe):
    def __init__(self):
        super(Nascimento, self).__init__()
        self.dtNascto    = TagData(    nome='dtNascto'  ,                  raiz='//eSocial/evtAdmissao/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMunic    = TagCaracter(nome='codMunic'  , tamanho=[1, 7] , raiz='//eSocial/evtAdmissao/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.uf          = TagCaracter(nome='uf'        , tamanho=[1, 2] , raiz='//eSocial/evtAdmissao/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.paisNascto  = TagCaracter(nome='paisNascto', tamanho=[1, 3] , raiz='//eSocial/evtAdmissao/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.paisNac     = TagCaracter(nome='paisNac'   , tamanho=[1, 3] , raiz='//eSocial/evtAdmissao/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmMae       = TagCaracter(nome='nmMae'     , tamanho=[1, 70], raiz='//eSocial/evtAdmissao/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmPai       = TagCaracter(nome='nmPai'     , tamanho=[1, 70], raiz='//eSocial/evtAdmissao/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

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
        self.cpfTrab    = TagCaracter(nome='cpfTrab'   , tamanho=[1, 11], raiz='//eSocial/evtAdmissao/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab    = TagCaracter(nome='nisTrab'   , tamanho=[1, 11], raiz='//eSocial/evtAdmissao/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmTrab     = TagCaracter(nome='nmTrab'    , tamanho=[1, 70], raiz='//eSocial/evtAdmissao/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.sexo       = TagCaracter(nome='sexo'      , tamanho=[1, 1] , raiz='//eSocial/evtAdmissao/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.racaCor    = TagCaracter(nome='racaCor'   , tamanho=[1, 1] , raiz='//eSocial/evtAdmissao/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.estCiv     = TagCaracter(nome='estCiv'    , tamanho=[1, 1] , raiz='//eSocial/evtAdmissao/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.grauInstr  = TagCaracter(nome='grauInstr' , tamanho=[1, 2] , raiz='//eSocial/evtAdmissao/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indPriEmpr = TagCaracter(nome='indPriEmpr', tamanho=[1, 1] , raiz='//eSocial/evtAdmissao/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmSoc      = TagCaracter(nome='nmSoc'     , tamanho=[1, 70], raiz='//eSocial/evtAdmissao/trabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
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
        xml += self.indPriEmpr.xml
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
            self.estCivil.xml = arquivo
            self.grauInstr.xml = arquivo
            self.indPriEmpr.xml = arquivo
            self.nmSoc.xml = arquivo
            self.nascimento.xml = arquivo
            self.documentos.xml = arquivo
            self.endereco.xml = arquivo
            self.trabEstrangeiro = self.le_grupo('//eSocial/evtAdmissao/trabalhador/trabEstrangeiro', TrabEstrangeiro, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoDeficiencia = self.le_grupo('//eSocial/evtAdmissao/trabalhador/infoDeficiencia', InfoDeficiencia, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.dependente = self.le_grupo('//eSocial/evtAdmissao/trabalhador/dependente', Dependente, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.aposentadoria = self.le_grupo('//eSocial/evtAdmissao/trabalhador/aposentadoria', Aposentadoria, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.contato = self.le_grupo('//eSocial/evtAdmissao/trabalhador/contato', Contato, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtAdmissao/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtAdmissao/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif = TagInteiro( nome='indRetif', raiz='//eSocial/evtAdmissao/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', raiz='//eSocial/evtAdmissao/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpAmb    = TagInteiro( nome='tpAmb'   , raiz='//eSocial/evtAdmissao/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi  = TagInteiro( nome='procEmi' , raiz='//eSocial/evtAdmissao/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc  = TagCaracter(nome='verProc' , raiz='//eSocial/evtAdmissao/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtAdmissao(XMLNFe):
    def __init__(self):
        super(EvtAdmissao, self).__init__()
        self.Id = TagCaracter(nome='evtAdmissao', propriedade='Id', raiz='//eSocial/evtAdmissao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.trabalhador = Trabalhador()
        self.vinculo = Vinculo()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.trabalhador.xml
        xml += self.vinculo.xml
        xml += '</evtAdmissao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.trabalhador.xml = arquivo
            self.vinculo.xml = arquivo

    xml = property(get_xml, set_xml)


class S2200(XMLNFe):
    def __init__(self):
        super(S2200, self).__init__()
        self.evtAdmissao = EvtAdmissao()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtAdmissao.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtAdmissao
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtAdmissao.xml

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
            self.evtAdmissao.xml = arquivo
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
        self.evtAdmissao.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
