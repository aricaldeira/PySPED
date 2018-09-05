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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtFechaEvPer/v02_04_02'


class InfoFech(XMLNFe):
    def __init__(self):
        super(InfoFech, self).__init__()
        self.evtRemun        = TagCaracter(nome='evtRemun',        tamanho=[1, 1], raiz='//eSocial/evrFechaEvPer/infoFech', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.evtPgtos        = TagCaracter(nome='evtPgtos',        tamanho=[1, 1], raiz='//eSocial/evrFechaEvPer/infoFech', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.evtAqProd       = TagCaracter(nome='evtAqProd',       tamanho=[1, 1], raiz='//eSocial/evrFechaEvPer/infoFech', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.evtComProd      = TagCaracter(nome='evtComProd',      tamanho=[1, 1], raiz='//eSocial/evrFechaEvPer/infoFech', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.evtContratAvNP  = TagCaracter(nome='evtContratAvNP',  tamanho=[1, 1], raiz='//eSocial/evrFechaEvPer/infoFech', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.evtInfoComplPer = TagCaracter(nome='evtInfoComplPer', tamanho=[1, 1], raiz='//eSocial/evrFechaEvPer/infoFech', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.compSemMovto    = TagCaracter(nome='compSemMovto',    tamanho=[1, 1], raiz='//eSocial/evrFechaEvPer/infoFech', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoFech>'
        xml += self.evtRemun.xml
        xml += self.evtPgtos.xml
        xml += self.evtAqProd.xml
        xml += self.evtComProd.xml
        xml += self.evtContratAvNP.xml
        xml += self.evtInfoComplPer.xml
        xml += self.compSemMovto.xml
        xml += '</infoFech>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtRemun.xml = arquivo
            self.evtPgtos.xml = arquivo
            self.evtAqProd.xml = arquivo
            self.evtComProd.xml = arquivo
            self.evtContratAvNP.xml = arquivo
            self.evtInfoComplPer.xml = arquivo
            self.compSemMovto.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeRespInf(XMLNFe):
    def __init__(self):
        super(IdeRespInf, self).__init__()
        self.nmResp    = TagCaracter(nome='nmResp',   tamanho=[1, 60], raiz='//eSocial/evtFechaEvPer/ideRespInf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cpfResp   = TagCaracter(nome='cpfResp',  tamanho=[1, 11], raiz='//eSocial/evtFechaEvPer/ideRespInf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.telefone  = TagCaracter(nome='telefone', tamanho=[1, 13], raiz='//eSocial/evtFechaEvPer/ideRespInf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.email     = TagCaracter(nome='email',    tamanho=[1, 60], raiz='//eSocial/evtFechaEvPer/ideRespInf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideRespInf>'
        xml += self.nmResp.xml
        xml += self.cpfResp.xml
        xml += self.telefone.xml
        xml += self.email.xml
        xml += '</ideRespInf>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nmResp.xml = arquivo
            self.cpfResp.xml = arquivo
            self.telefone.xml = arquivo
            self.email.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1, 1],  raiz='//eSocial/evtFechaEvPer/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtFechaEvPer/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indApuracao = TagCaracter(nome='indApuracao', tamanho=[1,  1], raiz='//eSocial/evtFechaEvPer/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.perApur     = TagCaracter(nome='perApur',     tamanho=[1,  7], raiz='//eSocial/evtFechaEvPer/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpAmb       = TagInteiro( nome='tpAmb',       tamanho=[1,  1], raiz='//eSocial/evtFechaEvPer/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi     = TagInteiro( nome='procEmi',     tamanho=[1,  1], raiz='//eSocial/evtFechaEvPer/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc     = TagCaracter(nome='verProc',     tamanho=[1, 20], raiz='//eSocial/evtFechaEvPer/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.indApuracao.xml
        xml += self.perApur.xml
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indApuracao.xml = arquivo
            self.perApur.xml = arquivo
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtFechaEvPer(XMLNFe):
    def __init__(self):
        super(EvtFechaEvPer, self).__init__()
        self.Id = TagCaracter(nome='evtFechaEvPer', propriedade='Id', raiz='//eSocial/evtFechaEvPer', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideRespInf = IdeRespInf()
        self.infoFech = InfoFech()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideRespInf.xml
        xml += self.infoFech.xml
        xml += '</evtFechaEvPer>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoEmpregador.xml = arquivo

    xml = property(get_xml, set_xml)


class S1299(XMLNFe):
    def __init__(self):
        super(S1299, self).__init__()
        self.evtFechaEvPer = EvtFechaEvPer()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtFechaEvPer.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtFechaEvPer
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtFechaEvPer.xml

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
            self.evtFechaEvPer.xml = arquivo
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
        self.evtFechaEvPer.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
