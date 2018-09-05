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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v02_04_02'


class EndExt(XMLNFe):
    def __init__(self):
        super(EndExt, self).__init__()
        self.dscLograd = TagCaracter(nome='dscLograd', tamanho=[1, 80], raiz='//idePgtoExt/endExt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrLograd  = TagCaracter(nome='nrLograd',  tamanho=[1, 10], raiz='//idePgtoExt/endExt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.complem   = TagCaracter(nome='complem',   tamanho=[1, 30], raiz='//idePgtoExt/endExt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.bairro    = TagCaracter(nome='bairro',    tamanho=[1, 60], raiz='//idePgtoExt/endExt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmCid     = TagCaracter(nome='nmCid',     tamanho=[1, 50], raiz='//idePgtoExt/endExt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codPostal = TagCaracter(nome='codPostal', tamanho=[1, 12], raiz='//idePgtoExt/endExt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<endExt>'
        xml += self.dscLograd.xml
        xml += self.nrLograd.xml
        xml += self.complem.xml
        xml += self.bairro.xml
        xml += self.nmCid.xml
        xml += self.codPostal.xml
        xml += '</endExt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dscLograd.xml = arquivo
            self.nrLograd.xml = arquivo
            self.complem.xml = arquivo
            self.bairro.xml = arquivo
            self.nmCid.xml = arquivo
            self.codPostal.xml = arquivo

    xml = property(get_xml, set_xml)


class IdePais(XMLNFe):
    def __init__(self):
        super(IdePais, self).__init__()
        self.codPais    = TagCaracter(nome='codPais',  tamanho=[1, 30], raiz='//idePgtoExt/idePais', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indNIF     = TagCaracter(nome='indNIF',   tamanho=[1, 1],  raiz='//idePgtoExt/idePais', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nifBenif   = TagCaracter(nome='nifBenif', tamanho=[1, 20], raiz='//idePgtoExt/idePais', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePais>'
        xml += self.codPais.xml
        xml += self.indNIF.xml
        xml += self.nifBenif.xml
        xml += '</idePais>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codPais.xml = arquivo
            self.indNIF.xml = arquivo
            self.nifBenif.xml = arquivo

    xml = property(get_xml, set_xml)


class IdePgtoExt(XMLNFe):
    def __init__(self):
        super(IdePgtoExt, self).__init__()
        self.idePais = IdePais()
        self.endExt  = EndExt()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePgtoExt>'
        xml += self.idePais.xml
        xml += self.endExt.xml
        xml += '</idePgtoExt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.idePais.xml = arquivo
            self.endExt.xml = arquivo

    xml = property(get_xml, set_xml)


class Irrf(XMLNFe):
    def __init__(self):
        super(Irrf, self).__init__()
        self.tpCR       = TagCaracter(nome='tpCR',                           raiz='//irrf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrIrrfDesc = TagDecimal( nome='vrIrrfDesc', tamanho=[1, 14, 2], raiz='//irrf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<irrf>'
        xml += self.tpCR.xml
        xml += self.vrIrrfDesc.xml
        xml += '</irrf>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpCR.xml = arquivo
            self.vrIrrfDesc.xml = arquivo

    xml = property(get_xml, set_xml)


class BasesIrrf(XMLNFe):
    def __init__(self):
        super(BasesIrrf, self).__init__()
        self.tpValor = TagCaracter(nome='tpValor', tamanho=[1, 2],     raiz='//basesIrrf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.valor   = TagDecimal( nome='valor',   tamanho=[1, 14, 2], raiz='//basesIrrf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<basesIrrf>'
        xml += self.tpValor.xml
        xml += self.valor.xml
        xml += '</basesIrrf>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpValor.xml = arquivo
            self.valor.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoIrrf(XMLNFe):
    def __init__(self):
        super(InfoIrrf, self).__init__()
        self.codCateg   = TagCaracter(nome='codCateg', tamanho=[1, 3], raiz='//infoIrrf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indResBr   = TagCaracter(nome='indResBr', tamanho=[1, 1], raiz='//infoIrrf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.basesIrrf  = []
        self.irrf       = []
        self.idePgtoExt = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoIrrf>'
        xml += self.codCateg.xml
        xml += self.indResBr.xml
        if len(self.basesIrrf):
            for b in self.basesIrrf:
                xml += b.xml
        if len(self.irrf):
            for i in self.irrf:
                xml += i.xml
        if len(self.idePgtoExt):
            for i in self.idePgtoExt:
                xml += i.xml
        xml += '</infoIrrf>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codCateg.xml = arquivo
            self.indResBr.xml = arquivo
            self.basesIrrf = self.le_grupo('//infoIrrf/basesIrrf', BasesIrrf, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.irrf = self.le_grupo('//infoIrrf/irrf', Irrf, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.idePgtoExt = self.le_grupo('//infoIrrf/idePgtoExt', IdePgtoExt, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoDep(XMLNFe):
    def __init__(self):
        super(InfoDep, self).__init__()
        self.vrDedDep = TagDecimal(nome='vrDedDep', tamanho=[1, 14, 2], raiz='//infoDep', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoDep>'
        xml += self.vrDedDep.xml
        xml += '</infoDep>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vrDedDep.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeTrabalhador(XMLNFe):
    def __init__(self):
        super(IdeTrabalhador, self).__init__()
        self.cpfTrab     = TagCaracter(nome='cpfTrab', tamanho=[1, 11],    raiz='//eSocial/evtIrrfBenef/ideTrabalhador',      namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideTrabalhador>'
        xml += self.cpfTrab.xml
        xml += '</ideTrabalhador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrab.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1, 1],  raiz='//eSocial/evtIrrfBenef/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtIrrfBenef/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.nrRecArqBase = TagCaracter(nome='nrRecArqBase', tamanho=[1, 40], raiz='//eSocial/evtIrrfBenef/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.perApur      = TagCaracter(nome='perApur',      tamanho=[1,  7], raiz='//eSocial/evtIrrfBenef/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.nrRecArqBase.xml
        xml += self.perApur.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRecArqBase.xml = arquivo
            self.perApur.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtIrrfBenef(XMLNFe):
    def __init__(self):
        super(EvtIrrfBenef, self).__init__()
        self.Id = TagCaracter(nome='evtIrrfBenef', propriedade='Id', raiz='//eSocial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideTrabalhador = IdeTrabalhador()
        self.infoDep = []
        self.infoIrrf = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideTrabalhador.xml
        if len(self.infoDep):
            for i in self.infoDep:
                xml += i.xml
        if len(self.infoIrrf):
            for i in self.infoIrrf:
                xml += i.xml
        xml += '</evtIrrfBenef>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideTrabalhador.xml = arquivo
            self.infoDep = self.le_grupo('//eSocial/evtIrrfBenef/infoDep', InfoDep, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoIrrf = self.le_grupo('//eSocial/evtIrrfBenef/infoIrrf', InfoIrrf, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class S5002(XMLNFe):
    def __init__(self):
        super(S5002, self).__init__()
        self.evtIrrfBenef = EvtIrrfBenef()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtIrrfBenef.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        self.Signature = Signature()
        self.evento = self.evtIrrfBenef
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtIrrfBenef.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtIrrfBenef.Id.valor
        xml += self.Signature.xml
        xml += '</eSocial>'

        # Define o método de assinatura
        # self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtIrrfBenef.xml = arquivo
            self.Signature.xml = self._le_noh('//sig:Signature')

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
        self.evtIrrfBenef.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
