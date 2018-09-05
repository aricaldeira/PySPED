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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtExclusao/v02_04_02'


class IdeFolhaPagto(XMLNFe):
    def __init__(self):
        super(IdeFolhaPagto, self).__init__()
        self.indApuracao = TagCaracter(nome='indApuracao', tamanho=[1, 1], raiz='//ideFolhaPagto', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.perApur = TagCaracter(nome='perApur',     tamanho=[1, 7], raiz='//ideFolhaPagto', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideFolhaPagto>'
        xml += self.indApuracao.xml
        xml += self.perApur.xml
        xml += '</ideFolhaPagto>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indApuracao.xml = arquivo
            self.perApur.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeTrabalhador(XMLNFe):
    def __init__(self):
        super(IdeTrabalhador, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', tamanho=[1, 11], raiz='//ideTrabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab = TagCaracter(nome='nisTrab', tamanho=[1, 11], raiz='//ideTrabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideTrabalhador>'
        xml += self.cpfTrab.xml
        xml += self.nisTrab.xml
        xml += '</ideTrabalhador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrab.xml = arquivo
            self.nisTrab.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoExclusao(XMLNFe):
    def __init__(self):
        super(InfoExclusao, self).__init__()
        self.tpEvento = TagCaracter(nome='tpEvento', tamanho=[1, 6],  raiz='//eSocial/evtExclusao/infoExclusao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrRecEvt = TagCaracter(nome='nrRecEvt', tamanho=[1, 40], raiz='//eSocial/evtExclusao/infoExclusao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideTrabalhador = []
        self.ideFolhaPagto  = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoExclusao>'
        xml += self.tpEvento.xml
        xml += self.nrRecEvt.xml
        if len(self.ideTrabalhador) > 0:
            for i in self.ideTrabalhador:
                xml += i.xml
        if len(self.ideFolhaPagto) > 0:
            for i in self.ideFolhaPagto:
                xml += i.xml
        xml += '</infoExclusao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpEvento.xml = arquivo
            self.nrRecEvt.xml = arquivo
            self.ideTrabalhador = self.le_grupo('//eSocial/evtExclusao/infoExclusao/ideTrabalhador', IdeTrabalhador, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.ideFolhaPagto = self.le_grupo('//eSocial/evtExclusao/infoExclusao/ideFolhaPagto', IdeFolhaPagto, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1, 1],  raiz='//eSocial/evtExclusao/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtExclusao/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.tpAmb   = TagCaracter(nome='tpAmb', tamanho=[1, 1],  raiz='//eSocial/evtExclusao/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='2')
        self.procEmi = TagCaracter(nome='procEmi', tamanho=[1, 1],  raiz='//eSocial/evtExclusao/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20], raiz='//eSocial/evtExclusao/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtExclusao(XMLNFe):
    def __init__(self):
        super(EvtExclusao, self).__init__()
        self.Id = TagCaracter(nome='evtExclusao', propriedade='Id', raiz='//eSocial', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.infoExclusao = InfoExclusao()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.infoExclusao.xml
        xml += '</evtExclusao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoExclusao.xml = arquivo

    xml = property(get_xml, set_xml)


class S3000(XMLNFe):
    def __init__(self):
        super(S3000, self).__init__()
        self.evtExclusao = EvtExclusao()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtExclusao.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtExclusao
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtExclusao.xml

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
            self.evtExclusao.xml = arquivo
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
        self.evtExclusao.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
