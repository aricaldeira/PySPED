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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtBasesTrab/v02_04_02'


class CalcTerc(XMLNFe):
    def __init__(self):
        super(CalcTerc, self).__init__()
        self.tpCR        = TagCaracter(nome='tpCR',        tamanho=[1, 6],     raiz='//calcTerc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCsSegTerc = TagCaracter(nome='vrCsSegTerc', tamanho=[1, 14, 2], raiz='//calcTerc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrDescTerc  = TagDecimal( nome='vrDescTerc',  tamanho=[1, 14, 2], raiz='//calcTerc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<calcTerc>'
        xml += self.tpCR.xml
        xml += self.vrCsSegTerc.xml
        xml += self.vrDescTerc.xml
        xml += '</calcTerc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpCR.xml = arquivo
            self.vrCsSegTerc.xml = arquivo
            self.vrDescTerc.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoBaseCS(XMLNFe):
    def __init__(self):
        super(InfoBaseCS, self).__init__()
        self.ind13     = TagCaracter(nome='ind13',    tamanho=[1, 1],     raiz='//infoBaseCS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpValor   = TagCaracter(nome='tpValor',  tamanho=[1, 2],     raiz='//infoBaseCS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.valor     = TagDecimal( nome='valor',    tamanho=[1, 14, 2], raiz='//infoBaseCS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoBaseCS>'
        xml += self.ind13.xml
        xml += self.tpValor.xml
        xml += self.valor.xml
        xml += '</infoBaseCS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ind13.xml = arquivo
            self.tpValor.xml = arquivo
            self.valor.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoCategIncid(XMLNFe):
    def __init__(self):
        super(InfoCategIncid, self).__init__()
        self.matricula  = TagCaracter(nome='matricula',  tamanho=[1, 30],    raiz='//infoCategIncid', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg   = TagCaracter(nome='codCateg',   tamanho=[1, 3],     raiz='//infoCategIncid', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indSimples = TagCaracter(nome='indSimples', tamanho=[1, 1],     raiz='//infoCategIncid', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.infoBaseCS = []
        self.calcTerc   = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCategIncid>'
        xml += self.matricula.xml
        xml += self.codCateg.xml
        xml += self.indSimples.xml
        if len(self.infoBaseCS):
            for i in self.infoBaseCS:
                xml += i.xml
        if len(self.calcTerc):
            for c in self.calcTerc:
                xml += c.xml
        xml += '</infoCategIncid>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.matricula.xml = arquivo
            self.codCateg.xml = arquivo
            self.indSimples.xml = arquivo
            self.infoBaseCS = self.le_grupo('//infoCategIncid/infoBaseCS', InfoBaseCS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.calcTerc = self.le_grupo('//infoCategIncid/calcTerc', CalcTerc, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEstabLot(XMLNFe):
    def __init__(self):
        super(IdeEstabLot, self).__init__()
        self.tpInsc     = TagCaracter(nome='tpInsc',     tamanho=[1, 1],  raiz='//ideEstabLot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc     = TagCaracter(nome='nrInsc',     tamanho=[1, 15], raiz='//ideEstabLot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codLotacao = TagCaracter(nome='codLotacao', tamanho=[1, 30], raiz='//ideEstabLot', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoCategIncid = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstabLot>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.codLotacao.xml
        if len(self.infoCategIncid) > 0:
            for i in self.infoCategIncid:
                xml += i.xml
        xml += '</ideEstabLot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.codLotacao.xml = arquivo
            self.infoCategIncid = self.le_grupo('//ideEstabLot/infoCategIncid', InfoCategIncid, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoCp(XMLNFe):
    def __init__(self):
        super(InfoCp, self).__init__()
        self.ideEstabLot = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCp>'
        if len(self.ideEstabLot) > 0:
            for p in self.ideEstabLot:
                xml += p.xml
        xml += '</infoCp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideEstabLot = self.le_grupo('//eSocial/evtBasesTrab/infoCp/ideEstabLot', IdeEstabLot, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoCpCalc(XMLNFe):
    def __init__(self):
        super(InfoCpCalc, self).__init__()
        self.tpCR      = TagCaracter(nome='tpCR',      tamanho=[1, 6],     raiz='//infoCpCalc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCpSeg   = TagDecimal( nome='vrCpSeg',   tamanho=[1, 14, 2], raiz='//infoCpCalc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrDescSeg = TagDecimal( nome='vrDescSeg', tamanho=[1, 14, 2], raiz='//infoCpCalc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCpCalc>'
        xml += self.tpCR.xml
        xml += self.vrCpSeg.xml
        xml += self.vrDescSeg.xml
        xml += '</infoCpCalc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpCR.xml = arquivo
            self.vrCpSeg.xml = arquivo
            self.vrDescSeg.xml = arquivo

    xml = property(get_xml, set_xml)


class ProcJudTrab(XMLNFe):
    def __init__(self):
        super(ProcJudTrab, self).__init__()
        self.nrProcJud = TagCaracter(nome='nrProdJuc', tamanho=[1, 20], raiz='//procJudTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codSusp   = TagCaracter(nome='codSusp',   tamanho=[1, 14], raiz='//procJudTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<procJudTrab>'
        xml += self.nrProcJud.xml
        xml += self.codSusp.xml
        xml += '</procJudTrab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrProcJud.xml = arquivo
            self.codSusp.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeTrabalhador(XMLNFe):
    def __init__(self):
        super(IdeTrabalhador, self).__init__()
        self.cpfTrab     = TagCaracter(nome='cpfTrab', tamanho=[1, 11],    raiz='//eSocial/evtBasesTrab/ideTrabalhador',      namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.procJudTrab = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideTrabalhador>'
        xml += self.cpfTrab.xml
        if len(self.procJudTrab) > 0:
            for p in self.procJudTrab:
                xml += p.xml
        xml += '</ideTrabalhador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrab.xml = arquivo
            self.procJudTrab = self.le_grupo('//eSocial/evtBasesTrab/ideTrabalhador/procJudTrab', ProcJudTrab, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1, 1],  raiz='//eSocial/evtBasesTrab/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtBasesTrab/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.nrRecArqBase = TagCaracter(nome='nrRecArqBase', tamanho=[1, 40], raiz='//eSocial/evtBasesTrab/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indApuracao  = TagCaracter(nome='indApuracao',  tamanho=[1,  1], raiz='//eSocial/evtBasesTrab/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.perApur      = TagCaracter(nome='perApur',      tamanho=[1,  7], raiz='//eSocial/evtBasesTrab/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.nrRecArqBase.xml
        xml += self.indApuracao.xml
        xml += self.perApur.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRecArqBase.xml = arquivo
            self.indApuracao.xml = arquivo
            self.perApur.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtBasesTrab(XMLNFe):
    def __init__(self):
        super(EvtBasesTrab, self).__init__()
        self.Id = TagCaracter(nome='evtBasesTrab', propriedade='Id', raiz='//eSocial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideTrabalhador = IdeTrabalhador()
        self.infoCpCalc = []
        self.infoCp = InfoCp()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideTrabalhador.xml
        if len(self.infoCpCalc):
            for i in self.infoCpCalc:
                xml += i.xml
        xml += self.infoCp.xml
        xml += '</evtBasesTrab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideTrabalhador.xml = arquivo
            self.infoCpCalc = self.le_grupo('//eSocial/evtBasesTrab/infoCpCalc', InfoCpCalc, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoCp.xml = arquivo

    xml = property(get_xml, set_xml)


class S5001(XMLNFe):
    def __init__(self):
        super(S5001, self).__init__()
        self.evtBasesTrab = EvtBasesTrab()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtBasesTrab.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        self.Signature = Signature()
        self.evento = self.evtBasesTrab
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtBasesTrab.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtBasesTrab.Id.valor
        xml += self.Signature.xml
        xml += '</eSocial>'

        # Define o método de assinatura
        # self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtBasesTrab.xml = arquivo
            self.Signature.xml = self._le_noh('//eSocial/sig:Signature')

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
        self.evtBasesTrab.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
