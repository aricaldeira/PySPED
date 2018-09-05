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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtTSVAltContr/v02_04_02'

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
            self.natEstagio.xml = arquivo
            self.nivEstagio.xml = arquivo
            self.areaAtuacao.xml = arquivo
            self.nrApol.xml = arquivo
            self.areaAtuacao.xml = arquivo
            self.nrApol.xml = arquivo
            self.vlrBolsa.xml = arquivo
            self.dtPrevTerm.xml = arquivo
            self.instEnsino.xml = arquivo
            self.ageIntegracao.xml = self.le_grupo('//eSocial/evtTSVAltContr/infoTSVAlteracao/infoComplementares/infoEstagiario/ageIntegracao', AgeIntegracao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.supervisorEstagio.xml = self.le_grupo('//eSocial/evtTSVAltContr/infoTSVAlteracao/infoComplementares/infoEstagiario/supervisorEstagio', AgeIntegracao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

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


class Remuneracao(XMLNFe):
    def __init__(self):
        super(Remuneracao, self).__init__()
        self.vrSalFx = TagDecimal(nome='vrSalFx', tamanho=[1, 14, 2], raiz='//vrSalFx', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.undSalFixo = TagInteiro(nome='undSalFixo', tamanho=[1, 1], raiz='//undSalFixo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscSalVar = TagCaracter(nome='dscSalVar', tamanho=[0, 255], raiz='//dscSalVar', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

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
        self.codFuncao = TagCaracter(nome='codFuncao', tamanho=[0, 30], raiz='//codCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

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
        if self.infoTrabCedido:
            for i in self.infoTrabCedido:
                xml += i.xml
        if self.infoEstagiario:
            for e in self.infoEstagiario:
                xml += e.xml
        xml += '</infoComplementares>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cargoFuncao.xml = self.le_grupo('//eSocial/evtTSVAltContr/infoTSVAlteracao/infoComplementares/cargoFuncao', CargoFuncao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.remuneracao.xml = self.le_grupo('//eSocial/evtTSVAltContr/infoTSVAlteracao/infoComplementares/remuneracao', Remuneracao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoTrabCedido.xml = self.le_grupo('//eSocial/evtTSVAltContr/infoTSVAlteracao/infoComplementares/infoTrabCedido', Remuneracao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoEstagiario.xml = self.le_grupo('//eSocial/evtTSVAltContr/infoTSVAlteracao/infoComplementares/infoTrabCedido', Remuneracao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoTSVAlteracao(XMLNFe):
    def __init__(self):
        super(InfoTSVAlteracao, self).__init__()
        self.dtAlteracao = TagData(nome='dtAlteracao', raiz='//eSocial/evtAltContratual/infoTSVAlteracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.natAtividade = TagInteiro(nome='natAtividade', raiz='//eSocial/evtAltContratual/infoTSVAlteracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoComplementares = InfoComplementares()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoTSVAlteracao>'
        xml += self.dtAlteracao.xml
        xml += self.natAtividade.xml
        xml += self.infoComplementares.xml
        xml += '</infoTSVAlteracao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtAlteracao.xml = arquivo
            self.natAtividade.xml = arquivo
            self.infoComplementares.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeTrabSemVinculo(XMLNFe):
    def __init__(self):
        super(IdeTrabSemVinculo, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', tamanho=[1, 11], raiz='//eSocial/evtTSVAltContr/ideTrabSemVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab = TagCaracter(nome='nisTrab', tamanho=[1, 11], raiz='//eSocial/evtTSVAltContr/ideTrabSemVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codCateg = TagInteiro(nome='codCateg', tamanho=[1, 3], raiz='//eSocial/evtTSVAltContr/ideTrabSemVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideTrabSemVinculo>'
        xml += self.cpfTrab.xml
        xml += self.nisTrab.xml
        xml += self.codCateg.xml
        xml += '</ideTrabSemVinculo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrab.xml = arquivo
            self.nisTrab.xml = arquivo
            self.codCateg.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtAltContratual/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtAltContratual/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif = TagInteiro( nome='indRetif', raiz='//eSocial/evtTSVAltContr/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', raiz='//eSocial/evtTSVAltContr/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpAmb    = TagInteiro( nome='tpAmb'   , raiz='//eSocial/evtTSVAltContr/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi  = TagInteiro( nome='procEmi' , raiz='//eSocial/evtTSVAltContr/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc  = TagCaracter(nome='verProc' , raiz='//eSocial/evtTSVAltContr/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtTSVAltContr(XMLNFe):
    def __init__(self):
        super(EvtTSVAltContr, self).__init__()
        self.Id = TagCaracter(nome='evtTSVAltContr', propriedade='Id', raiz='//eSocial/evtTSVAltContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideTrabSemVinculo = IdeTrabSemVinculo()
        self.infoTSVAlteracao = InfoTSVAlteracao()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideTrabSemVinculo.xml
        xml += self.infoTSVAlteracao.xml
        xml += '</evtTSVAltContr>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideTrabSemVinculo.xml = arquivo
            self.infoTSVAlteracao.xml = arquivo

    xml = property(get_xml, set_xml)


class S2306(XMLNFe):
    def __init__(self):
        super(S2306, self).__init__()
        self.evtTSVAltContr = EvtTSVAltContr()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtTSVAltContr.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtTSVAltContr
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtTSVAltContr.xml
        xml += '</eSocial>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtTSVAltContr.xml = arquivo

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
        self.evtTSVAltContr.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
