# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Affero General Public License,
# publicada pela Free Software Foundation, em sua versão 3 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Affero General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Affero General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import *
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_4 as ESQUEMA_ATUAL
from pysped.nfe.leiaute import inutnfe_310
import os


DIRNAME = os.path.dirname(__file__)


class InfInutEnviado(inutnfe_310.InfInutEnviado):
    def __init__(self):
        super(InfInutEnviado, self).__init__()


class InutNFe(inutnfe_310.InutNFe):
    def __init__(self):
        super(InutNFe, self).__init__()
        self.versao  = TagDecimal(nome='inutNFe', codigo='DP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='4.00', raiz='/')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'inutNFe_v4.00.xsd'


class InfInutRecebido(inutnfe_310.InfInutRecebido):
    def __init__(self):
        super(InfInutRecebido, self).__init__()


class RetInutNFe(inutnfe_310.RetInutNFe):
    def __init__(self):
        super(RetInutNFe, self).__init__()
        self.versao = TagDecimal(nome='retInutNFe', codigo='DR01', propriedade='versao', namespace=NAMESPACE_NFE, valor='4.00', raiz='/')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retInutNFe_v4.00.xsd'


class ProcInutNFe(inutnfe_310.ProcInutNFe):
    def __init__(self):
        super(ProcInutNFe, self).__init__()
        #
        # Atenção --- a tag ProcInutNFe tem que começar com letra maiúscula, para
        # poder validar no XSD. Os outros arquivos proc, procCancNFe, e procNFe
        # começam com minúscula mesmo
        #
        self.versao = TagDecimal(nome='ProcInutNFe', propriedade='versao', namespace=NAMESPACE_NFE, valor='4.00', raiz='/')
        self.inutNFe = InutNFe()
        self.retInutNFe = RetInutNFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procInutNFe_v4.00.xsd'
