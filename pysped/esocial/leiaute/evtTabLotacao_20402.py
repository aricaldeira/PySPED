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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtTabLotacao/v02_04_02'


class NovaValidade(XMLNFe):
    def __init__(self):
        super(NovaValidade, self).__init__()
        self.iniValid = TagCaracter(nome='iniValid', raiz='//eSocial/evtTabRubrica/infoRubrica/novaValidade', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//eSocial/evtTabRubrica/infoRubrica/novaValidade', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<novaValidade>'
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</novaValidade>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoEmprParcial(XMLNFe):
    def __init__(self):
        super(InfoEmprParcial, self).__init__()
        self.tpInscContrat = TagCaracter(nome='tpInscContrat', tamanho=[1, 1], raiz='//infoEmprParcial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInscContrat = TagCaracter(nome='nrInscContrat', tamanho=[1, 14], raiz='//infoEmprParcial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpInscProp = TagCaracter(nome='tpInscProp', tamanho=[1, 1], raiz='//infoEmprParcial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInscProp = TagCaracter(nome='nrInscProp', tamanho=[1, 14], raiz='//infoEmprParcial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class ProcJudTerceiro(XMLNFe):
    def __init__(self):
        super(ProcJudTerceiro, self).__init__()
        self.codTerc = TagCaracter(nome='codTerc', tamanho=[1, 4], raiz='//procJudTerceiro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrProcJud = TagCaracter(nome='nrProcJud', tamanho=[1, 20], raiz='//procJudTerceiro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codSusp = TagCaracter(nome='codSusp', tamanho=[1, 14], raiz='//procJudTerceiro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<procJudTerceiro>'
        xml += self.codTerc.xml
        xml += self.nrProcJud.xml
        xml += self.codSusp.xml
        xml += '</procJudTerceiro>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codTerc.xml = arquivo
            self.nrProcJud.xml = arquivo
            self.codSusp.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoProcJudTerceiros(XMLNFe):
    def __init__(self):
        super(InfoProcJudTerceiros, self).__init__()
        self.procJudTerceiro = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoProcJudTerceiros>'
        if len(self.procJudTerceiro) > 0:
            for p in self.procJudTerceiro:
                xml += p.xml
        xml += '</infoProcJudTerceiros>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.procJudTerceiro = self.le_grupo('//eSocial/evtTabLotacao/infoLotacao/dadosLotacao/fpasLotacao', ProcJudTerceiro, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class FpasLotacao(XMLNFe):
    def __init__(self):
        super(FpasLotacao, self).__init__()
        self.fpas = TagCaracter(nome='fpas', tamanho=[1, 3], raiz='//eSocial/evtTabLotacao/infoLotacao/dadosLotacao/fpasLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codTercs = TagCaracter(nome='codTercs', tamanho=[1, 4], raiz='//eSocial/evtTabLotacao/infoLotacao/dadosLotacao/fpasLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codTercsSusp = TagCaracter(nome='codTercsSusp', tamanho=[1, 4], raiz='//eSocial/evtTabLotacao/infoLotacao/dadosLotacao/fpasLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.infoProcJudTerceiros = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<fpasLotacao>'
        xml += self.fpas.xml
        xml += self.codTercs.xml
        xml += self.codTercsSusp.xml
        if len(self.infoProcJudTerceiros) > 0:
            for p in self.infoProcJudTerceiros:
                xml += p.xml
        xml += '</fpasLotacao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.fpas.xml = arquivo
            self.codTercs.xml = arquivo
            self.codTercsSusp.xml = arquivo
            self.infoProcJudTerceiros = self.le_grupo('//eSocial/evtTabLotacao/infoLotacao/dadosLotacao/fpasLotacao/infoProcJudTerceiros', infoProcJudTerceiros, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class DadosLotacao(XMLNFe):
    def __init__(self):
        super(DadosLotacao, self).__init__()
        self.tpLotacao = TagCaracter(nome='tpLotacao', tamanho=[1, 2], raiz='//eSocial/evtTabLotacao/infoLotacao/dadosLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1, 1], raiz='//eSocial/evtTabLotacao/infoLotacao/dadosLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtTabLotacao/infoLotacao/dadosLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.fpasLotacao = FpasLotacao()
        self.infoEmprParcial = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosLotacao>'
        xml += self.tpLotacao.xml
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.fpasLotacao.xml
        if len(self.infoEmprParcial) > 0:
            for p in self.infoEmprParcial:
                xml += p.xml
        xml += '</dadosLotacao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpLotacao.xml = arquivo
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.fpasLotacao.xml = arquivo
            self.infoEmprParcial = self.le_grupo('//eSocial/evtTabLotacao/infoLotacao/dadosLotacao/infoEmprParcial', InfoEmprParcial, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeLotacao(XMLNFe):
    def __init__(self):
        super(IdeLotacao, self).__init__()
        self.codLotacao = TagCaracter(nome='codLotacao', tamanho=[1, 30], raiz='//eSocial/evtTabLotacao/infoLotacao/ideLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.iniValid = TagCaracter(nome='iniValid', raiz='//eSocial/evtTabLotacao/infoLotacao/ideLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//eSocial/evtTabLotacao/infoLotacao/ideLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideLotacao>'
        xml += self.codLotacao.xml
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</ideLotacao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codLotacao.xml = arquivo
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoLotacao(XMLNFe):
    def __init__(self):
        super(InfoLotacao, self).__init__()
        self.ideLotacao = IdeLotacao()
        self.dadosLotacao = DadosLotacao()
        self.novaValidade = NovaValidade()
        self.operacao = 'I'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoLotacao>'
        if self.operacao == 'I':
            xml += '<inclusao>'
            xml += self.ideLotacao.xml
            xml += self.dadosLotacao.xml
            xml += '</inclusao>'
        elif self.operacao == 'A':
            xml += '<alteracao>'
            xml += self.ideLotacao.xml
            xml += self.dadosLotacao.xml
            xml += self.novaValidade.xml
            xml += '</alteracao>'

        elif self.operacao == 'E':
            xml += '<exclusao>'
            xml += self.ideLotacao.xml
            xml += '</exclusao>'

        xml += '</infoLotacao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideLotacao.xml = arquivo
            self.dadosLotacao.xml = arquivo
            self.novaValidade.xml = arquivo
    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtTabLotacao/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtTabLotacao/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.tpAmb   = TagInteiro(nome='tpAmb'   , raiz='//eSocial/evtTabLotacao/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi' , raiz='//eSocial/evtTabLotacao/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc = TagCaracter(nome='verProc', raiz='//eSocial/evtTabLotacao/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtTabLotacao(XMLNFe):
    def __init__(self):
        super(EvtTabLotacao, self).__init__()
        self.Id = TagCaracter(nome='evtTabLotacao', propriedade='Id', raiz='//eSocial/evtTabLotacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.infoLotacao = InfoLotacao()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.infoLotacao.xml
        xml += '</evtTabLotacao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoLotacao.xml = arquivo

    xml = property(get_xml, set_xml)


class S1020(XMLNFe):
    def __init__(self):
        super(S1020, self).__init__()
        self.evtTabLotacao = EvtTabLotacao()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtTabLotacao.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtTabLotacao
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtTabLotacao.xml

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
            self.evtTabLotacao.xml = arquivo
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
        self.evtTabLotacao.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
