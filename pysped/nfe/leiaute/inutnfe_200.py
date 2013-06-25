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

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import *
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL
from pysped.nfe.leiaute import inutnfe_107
import os


DIRNAME = os.path.dirname(__file__)


class InfInutEnviado(inutnfe_107.InfInutEnviado):
    def __init__(self):
        super(InfInutEnviado, self).__init__()
        self.Id     = TagCaracter(nome='infInut', codigo='DP03', tamanho=[43, 43] , raiz='//inutNFe', propriedade='Id')


class InutNFe(inutnfe_107.InutNFe):
    def __init__(self):
        super(InutNFe, self).__init__()
        self.versao  = TagDecimal(nome='inutNFe', codigo='DP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='2.00', raiz='/')
        self.infInut = InfInutEnviado()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'inutNFe_v2.00.xsd'

        self.chave = ''

    def gera_nova_chave(self):
        chave = self.monta_chave()

        #
        # Na versão 1.07 da NF-e a chave de inutilização não tem
        # o ano
        #
        # Mas na versão 2.00 tem
        #
        #chave = chave[0:2] + chave[4:]

        #
        # Define o Id
        #
        self.infInut.Id.valor = 'ID' + chave


class InfInutRecebido(inutnfe_107.InfInutRecebido):
    def __init__(self):
        super(InfInutRecebido, self).__init__()


class RetInutNFe(inutnfe_107.RetInutNFe):
    def __init__(self):
        super(RetInutNFe, self).__init__()
        self.versao = TagDecimal(nome='retInutNFe', codigo='DR01', propriedade='versao', namespace=NAMESPACE_NFE, valor='2.00', raiz='/')
        self.infInut = InfInutRecebido()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retInutNFe_v2.00.xsd'


class ProcInutNFe(inutnfe_107.ProcInutNFe):
    def __init__(self):
        super(ProcInutNFe, self).__init__()
        #
        # Atenção --- a tag ProcInutNFe tem que começar com letra maiúscula, para
        # poder validar no XSD. Os outros arquivos proc, procCancNFe, e procNFe
        # começam com minúscula mesmo
        #
        self.versao = TagDecimal(nome='ProcInutNFe', propriedade='versao', namespace=NAMESPACE_NFE, valor='2.00', raiz='/')
        self.inutNFe = InutNFe()
        self.retInutNFe = RetInutNFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procInutNFe_v2.00.xsd'
