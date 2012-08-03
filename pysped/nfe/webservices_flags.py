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


WS_NFE_ENVIO_LOTE = 0
WS_NFE_CONSULTA_RECIBO = 1
WS_NFE_CANCELAMENTO = 2
WS_NFE_INUTILIZACAO = 3
WS_NFE_CONSULTA = 4
WS_NFE_SITUACAO = 5
WS_NFE_CONSULTA_CADASTRO = 6

WS_DPEC_RECEPCAO = 7
WS_DPEC_CONSULTA = 8

NFE_AMBIENTE_PRODUCAO = 1
NFE_AMBIENTE_HOMOLOGACAO = 2

PROC_ENVIO_NFE = 101
PROC_CANCELAMENTO_NFE = 102
PROC_INUTILIZACAO_NFE = 103

UF_CODIGO = {
    u'AC': 12,
    u'AL': 27,
    u'AM': 13,
    u'AP': 16,
    u'BA': 29,
    u'CE': 23,
    u'DF': 53,
    u'ES': 32,
    u'GO': 52,
    u'MA': 21,
    u'MG': 31,
    u'MS': 50,
    u'MT': 51,
    u'PA': 15,
    u'PB': 25,
    u'PE': 26,
    u'PI': 22,
    u'PR': 41,
    u'RJ': 33,
    u'RN': 24,
    u'RO': 11,
    u'RR': 14,
    u'RS': 43,
    u'SC': 42,
    u'SE': 28,
    u'SP': 35,
    u'TO': 17
}

CODIGO_UF = {
    12: u'AC',
    27: u'AL',
    13: u'AM',
    16: u'AP',
    29: u'BA',
    23: u'CE',
    53: u'DF',
    32: u'ES',
    52: u'GO',
    21: u'MA',
    31: u'MG',
    50: u'MS',
    51: u'MT',
    15: u'PA',
    25: u'PB',
    26: u'PE',
    22: u'PI',
    41: u'PR',
    33: u'RJ',
    24: u'RN',
    11: u'RO',
    14: u'RR',
    43: u'RS',
    42: u'SC',
    28: u'SE',
    35: u'SP',
    17: u'TO'
}

