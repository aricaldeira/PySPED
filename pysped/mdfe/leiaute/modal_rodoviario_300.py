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

from __future__ import (division, print_function, unicode_literals, absolute_import)

from builtins import str
import os
from genshi.core import Markup
from pysped.xml_sped import *
from pysped.mdfe.leiaute import ESQUEMA_ATUAL_VERSAO_3 as ESQUEMA_ATUAL

PYBRASIL = False
try:
    from pybrasil.inscricao import formata_cnpj, formata_cpf

    PYBRASIL = True
except:
    pass

DIRNAME = os.path.dirname(__file__)


class LacRodo(XMLNFe):
    def __init__(self):
        super(LacRodo, self).__init__()
        self.nLacre = TagCaracter(nome='nLacre', tamanho=[1, 20], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//lacRodo')

    def get_xml(self):
        if not self.nLacre.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<lacRodo>'
        xml += self.nLacre.xml
        xml += '</lacRodo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nLacre.xml = arquivo

    xml = property(get_xml, set_xml)


class Condutor(XMLNFe):
    def __init__(self):
        super(Condutor, self).__init__()
        self.xNome = TagCaracter(nome='xNome', tamanho=[ 2, 60], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//condutor')
        self.CPF   = TagCaracter(nome='CPF'  , tamanho=[11, 11], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//condutor')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<condutor>'
        xml += self.xNome.xml
        xml += self.CPF.xml
        xml += '</condutor>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xNome.xml    = arquivo
            self.CPF.xml   = arquivo

    xml = property(get_xml, set_xml)

    @property
    def cpf_formatado(self):
        if not self.CPF.valor:
            return ''

        if not PYBRASIL:
            return self.CPF.valor

        return formata_cpf(self.CPF.valor)


class VeicTracao(XMLNFe):
    def __init__(self):
        super(VeicTracao, self).__init__()
        self.cInt     = TagCaracter(nome='cInt'   , tamanho=[ 1, 10], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infModal/rodo/veicTracao', obrigatorio=False)
        self.placa    = TagCaracter(nome='placa'  , tamanho=[ 1,  8], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infModal/rodo/veicTracao')
        self.RENAVAM  = TagCaracter(nome='RENAVAM', tamanho=[ 9, 11], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infModal/rodo/veicTracao', obrigatorio=False)
        self.tara     = TagInteiro(nome='tara'    , tamanho=[ 1,  5], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infModal/rodo/veicTracao')
        self.capKG    = TagInteiro(nome='capKG'   , tamanho=[ 1,  5], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infModal/rodo/veicTracao', obrigatorio=False)
        self.capM3    = TagInteiro(nome='capM3'   , tamanho=[ 1,  3], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infModal/rodo/veicTracao', obrigatorio=False)
        #self.prop     = Prop()
        self.condutor = []
        self.tpRod    = TagCaracter(nome='tpRod'  , tamanho=[ 2,  2], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infModal/rodo/veicTracao', obrigatorio=False, valor='06')
        self.tpCar    = TagCaracter(nome='tpCar'  , tamanho=[ 2,  2], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infModal/rodo/veicTracao', obrigatorio=False, valor='00')
        self.UF       = TagCaracter(nome='UF'     , tamanho=[ 2,  2], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infModal/rodo/veicTracao')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<veicTracao>'
        xml += self.cInt.xml
        xml += self.placa.xml
        xml += self.RENAVAM.xml
        xml += self.tara.xml
        xml += self.capKG.xml
        xml += self.capM3.xml
        #xml += self.prop.xml

        for cond in self.condutor:
            xml += cond.xml

        xml += self.tpRod.xml
        xml += self.tpCar.xml
        xml += self.UF.xml
        xml += '</veicTracao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cInt.xml    = arquivo
            self.placa.xml   = arquivo
            self.RENAVAM.xml = arquivo
            self.tara.xml    = arquivo
            self.capKG.xml   = arquivo
            self.capM3.xml   = arquivo
            #self.prop.xml    = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.condutor = self.le_grupo('//MDFe/infMDFe/infModal/rodo/veicTracao/condutor', Condutor, sigla_ns='mdfe')

            self.tpRod.xml   = arquivo
            self.tpCar.xml   = arquivo
            self.UF.xml      = arquivo

    xml = property(get_xml, set_xml)


class InfModalRodoviario(XMLNFe):
    def __init__(self):
        super(InfModalRodoviario, self).__init__()
        self.versaoModal = TagDecimal(nome='infModal' , propriedade='versaoModal', raiz='//MDFe/infMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, valor='3.00')
        #self.infANTT = InfANTT()
        self.veicTracao = VeicTracao()
        self.veicReboque = []
        self.codAgPorto = TagCaracter(nome='codAgPorto', tamanho=[ 1, 16], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infModal', obrigatorio=False)
        self.lacRodo = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infModal versaoModal="' + str(self.versaoModal.valor) + '">'
        xml += '<rodo>'
        #xml += self.infANTT.xml
        xml += self.veicTracao.xml

        for vr in self.veicReboque:
            xml += vr.xml

        xml += self.codAgPorto.xml

        for lr in self.lacRodo:
            xml += lr.xml

        xml += '</rodo>'
        xml += '</infModal>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versaoModal.xml = arquivo
            #self.infANTT.xml     = arquivo
            self.veicTracao.xml  = arquivo
            self.codAgPorto.xml  = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            #self.veicReboque = self.le_grupo('//MDFe/infMDFe/infModal/rodo/veicReboque', VeicReboque, sigla_ns='mdfe')
            self.lacRodo = self.le_grupo('//MDFe/infMDFe/infModal/rodo/lacRodo', LacRodo, sigla_ns='mdfe')

    xml = property(get_xml, set_xml)
