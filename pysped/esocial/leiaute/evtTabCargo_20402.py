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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtTabCargo/v02_04_02'


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


class CargoPublico(XMLNFe):
    def __init__(self):
        super(CargoPublico, self).__init__()
        self.acumCargo = TagCaracter(nome='acumCargo', tamanho=[1, 1], raiz='//cargoPublico', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.contagemEsp = TagCaracter(nome='contagemEsp', tamanho=[1, 1], raiz='//cargoPublico', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dedicExcl = TagCaracter(nome='dedicExcl', tamanho=[1, 1], raiz='//cargoPublico', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrLei = TagCaracter(nome='nrLei', tamanho=[1, 12], raiz='//cargoPublico/leiCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtLei = TagData(nome='dtLei', raiz='//cargoPublico/leiCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.sitCargo = TagCaracter(nome='sitCargo', tamanho=[1, 1], raiz='//cargoPublico/leiCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<cargoPublico>'
        xml += self.acumCargo.xml
        xml += self.contagemEsp.xml
        xml += self.dedicExcl.xml
        xml += '<leiCargo>'
        xml += self.nrLei.xml
        xml += self.dtLei.xml
        xml += self.sitCargo.xml
        xml += '</leiCargo>'
        xml += '</cargoPublico>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.acumCargo.xml = arquivo
            self.contagemEsp.xml = arquivo
            self.dedicExcl.xml = arquivo
            self.nrLei.xml = arquivo
            self.dtLei.xml = arquivo
            self.sitCargo.xml = arquivo

    xml = property(get_xml, set_xml)


class DadosCargo(XMLNFe):
    def __init__(self):
        super(DadosCargo, self).__init__()
        self.nmCargo = TagCaracter(nome='nmCargo', tamanho=[1, 100], raiz='//eSocial/evtTabCargo/infoCargo/dadosCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codCBO = TagCaracter(nome='codCBO', tamanho=[1, 6], raiz='//eSocial/evtTabCargo/infoCargo/dadosCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cargoPublico = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosCargo>'
        xml += self.nmCargo.xml
        xml += self.codCBO.xml
        if len(self.cargoPublico) > 0:
            for c in self.cargoPublico:
                xml += c.xml
        xml += '</dadosCargo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nmCargo.xml = arquivo
            self.codCBO.xml = arquivo
            self.cargoPublico = self.le_grupo('//eSocial/evtTabCargo/infoCargo/dadosCargo/cargoPublico', CargoPublico, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeCargo(XMLNFe):
    def __init__(self):
        super(IdeCargo, self).__init__()
        self.codCargo = TagCaracter(nome='codCargo', tamanho=[1, 30], raiz='//eSocial/evtTabCargo/infoCargo/ideCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.iniValid = TagCaracter(nome='iniValid', raiz='//eSocial/evtTabCargo/infoCargo/ideCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//eSocial/evtTabCargo/infoCargo/ideCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideCargo>'
        xml += self.codCargo.xml
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</ideCargo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codCargo.xml = arquivo
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoCargo(XMLNFe):
    def __init__(self):
        super(InfoCargo, self).__init__()
        self.ideCargo = IdeCargo()
        self.dadosCargo = DadosCargo()
        self.novaValidade = NovaValidade()
        self.operacao = 'I'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCargo>'
        if self.operacao == 'I':
            xml += '<inclusao>'
            xml += self.ideCargo.xml
            xml += self.dadosCargo.xml
            xml += '</inclusao>'
        elif self.operacao == 'A':
            xml += '<alteracao>'
            xml += self.ideCargo.xml
            xml += self.dadosCargo.xml
            xml += self.novaValidade.xml
            xml += '</alteracao>'

        elif self.operacao == 'E':
            xml += '<exclusao>'
            xml += self.ideCargo.xml
            xml += '</exclusao>'

        xml += '</infoCargo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideCargo.xml = arquivo
            self.dadosCargo.xml = arquivo
            self.novaValidade.xml = arquivo
    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtTabCargo/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtTabCargo/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.tpAmb   = TagInteiro(nome='tpAmb'   , raiz='//eSocial/evtTabCargo/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi' , raiz='//eSocial/evtTabCargo/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc = TagCaracter(nome='verProc', raiz='//eSocial/evtTabCargo/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtTabCargo(XMLNFe):
    def __init__(self):
        super(EvtTabCargo, self).__init__()
        self.Id = TagCaracter(nome='evtTabCargo', propriedade='Id', raiz='//eSocial/evtTabCargo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.infoCargo = InfoCargo()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.infoCargo.xml
        xml += '</evtTabCargo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoCargo.xml = arquivo

    xml = property(get_xml, set_xml)


class S1030(XMLNFe):
    def __init__(self):
        super(S1030, self).__init__()
        self.evtTabCargo = EvtTabCargo()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtTabCargo.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtTabCargo
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtTabCargo.xml

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
            self.evtTabCargo.xml = arquivo
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
        self.evtTabCargo.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
