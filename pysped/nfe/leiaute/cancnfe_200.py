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
from pysped.nfe.leiaute import cancnfe_107
import os


DIRNAME = os.path.dirname(__file__)


class InfCancEnviado(cancnfe_107.InfCancEnviado):
    def __init__(self):
        super(InfCancEnviado, self).__init__()


class CancNFe(cancnfe_107.CancNFe):
    def __init__(self):
        super(CancNFe, self).__init__()
        self.versao    = TagDecimal(nome='cancNFe', codigo='CP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='2.00', raiz='/')
        self.infCanc   = InfCancEnviado()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'cancNFe_v2.00.xsd'


class InfCancRecebido(cancnfe_107.InfCancRecebido):
    def __init__(self):
        super(InfCancRecebido, self).__init__()


class RetCancNFe(cancnfe_107.RetCancNFe):
    def __init__(self):
        super(RetCancNFe, self).__init__()
        self.versao = TagDecimal(nome='retCancNFe', codigo='CR01', propriedade='versao', namespace=NAMESPACE_NFE, valor='2.00', raiz='/')
        self.infCanc = InfCancRecebido()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retCancNFe_v2.00.xsd'


class ProcCancNFe(cancnfe_107.ProcCancNFe):
    def __init__(self):
        super(ProcCancNFe, self).__init__()
        #
        # Atenção --- a tag procCancNFe tem que começar com letra minúscula, para
        # poder validar no XSD.
        #
        self.versao = TagDecimal(nome='procCancNFe', propriedade='versao', namespace=NAMESPACE_NFE, valor='2.00', raiz='/')
        self.cancNFe = CancNFe()
        self.retCancNFe = RetCancNFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procCancNFe_v2.00.xsd'
