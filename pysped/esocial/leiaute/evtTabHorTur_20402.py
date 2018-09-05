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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtTabHorTur/v02_04_02'


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


class HorarioIntervalo(XMLNFe):
    def __init__(self):
        super(HorarioIntervalo, self).__init__()
        self.tpInterv = TagCaracter(nome='tpInterv', tamanho=[1, 1], raiz='//horarioIntervalo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.durInterv = TagCaracter(nome='durInterv', tamanho=[1, 3], raiz='//horarioIntervalo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.iniInterv = TagCaracter(nome='iniInterv', tamanho=[1, 4], raiz='//horarioIntervalo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.termInterv = TagCaracter(nome='termInterv', tamanho=[1, 4], raiz='//horarioIntervalo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<horarioIntervalo>'
        xml += self.tpInterv.xml
        xml += self.durInterv.xml
        xml += self.iniInterv.xml
        xml += self.termInterv.xml
        xml += '</horarioIntervalo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInterv.xml = arquivo
            self.durInterv.xml = arquivo
            self.iniInterv.xml = arquivo
            self.termInterv.xml = arquivo

    xml = property(get_xml, set_xml)


class DadosHorContratual(XMLNFe):
    def __init__(self):
        super(DadosHorContratual, self).__init__()
        self.hrEntr = TagCaracter(nome='hrEntr', tamanho=[1, 4], raiz='//eSocial/evtTabHorTur/infoHorContratual/dadosHorContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.hrSaida = TagCaracter(nome='hrSaida', tamanho=[1, 4], raiz='//eSocial/evtTabHorTur/infoHorContratual/dadosHorContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.durJornada = TagCaracter(nome='durJornada', tamanho=[1, 4], raiz='//eSocial/evtTabHorTur/infoHorContratual/dadosHorContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.perHorFlexivel = TagCaracter(nome='perHorFlexivel', tamanho=[1, 1], raiz='//eSocial/evtTabHorTur/infoHorContratual/dadosHorContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.horarioIntervalo = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosHorContratual>'
        xml += self.hrEntr.xml
        xml += self.hrSaida.xml
        xml += self.durJornada.xml
        xml += self.perHorFlexivel.xml
        if len(self.horarioIntervalo) > 0:
            for h in self.horarioIntervalo:
                xml += h.xml
        xml += '</dadosHorContratual>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.hrEntr.xml = arquivo
            self.hrSaida.xml = arquivo
            self.durJornada.xml = arquivo
            self.perHorFlexivel.xml = arquivo
            self.horarioIntervalo = self.le_grupo('//eSocial/evtTabHorTur/infoHorContratual/dadosHorContratual/horarioIntervalo', HorarioIntervalo, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeHorContratual(XMLNFe):
    def __init__(self):
        super(IdeHorContratual, self).__init__()
        self.codHorContrat = TagCaracter(nome='codHorContrat', tamanho=[1, 30], raiz='//eSocial/evtTabHorTur/infoHorContratual/ideHorContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.iniValid = TagCaracter(nome='iniValid', raiz='//eSocial/evtTabHorTur/infoHorContratual/ideHorContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//eSocial/evtTabHorTur/infoHorContratual/ideHorContratual', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideHorContratual>'
        xml += self.codHorContrat.xml
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</ideHorContratual>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codHorContrat.xml = arquivo
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoHorContratual(XMLNFe):
    def __init__(self):
        super(InfoHorContratual, self).__init__()
        self.ideHorContratual = IdeHorContratual()
        self.dadosHorContratual = DadosHorContratual()
        self.novaValidade = NovaValidade()
        self.operacao = 'I'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoHorContratual>'
        if self.operacao == 'I':
            xml += '<inclusao>'
            xml += self.ideHorContratual.xml
            xml += self.dadosHorContratual.xml
            xml += '</inclusao>'
        elif self.operacao == 'A':
            xml += '<alteracao>'
            xml += self.ideHorContratual.xml
            xml += self.dadosHorContratual.xml
            xml += self.novaValidade.xml
            xml += '</alteracao>'

        elif self.operacao == 'E':
            xml += '<exclusao>'
            xml += self.ideCargo.xml
            xml += '</exclusao>'

        xml += '</infoHorContratual>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideHorContratual.xml = arquivo
            self.dadosHorContratual.xml = arquivo
            self.novaValidade.xml = arquivo
    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtTabHorTur/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtTabHorTur/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.tpAmb   = TagInteiro(nome='tpAmb'   , raiz='//eSocial/evtTabHorTur/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi' , raiz='//eSocial/evtTabHorTur/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc = TagCaracter(nome='verProc', raiz='//eSocial/evtTabHorTur/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtTabHorTur(XMLNFe):
    def __init__(self):
        super(EvtTabHorTur, self).__init__()
        self.Id = TagCaracter(nome='evtTabHorTur', propriedade='Id', raiz='//eSocial/evtTabHorTur', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.infoHorContratual = InfoHorContratual()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.infoHorContratual.xml
        xml += '</evtTabHorTur>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoHorContratual.xml = arquivo

    xml = property(get_xml, set_xml)


class S1050(XMLNFe):
    def __init__(self):
        super(S1050, self).__init__()
        self.evtTabHorTur = EvtTabHorTur()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtTabHorTur.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtTabHorTur
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtTabHorTur.xml

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
        self.evtTabHorTur.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
