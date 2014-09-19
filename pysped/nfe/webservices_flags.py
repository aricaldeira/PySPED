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


WS_NFE_ENVIO_LOTE = 0
WS_NFE_CONSULTA_RECIBO = 1

#
# Novos webservices na versão 3.10, para as mesmas
# funções dos antigos
#
WS_NFE_AUTORIZACAO = WS_NFE_ENVIO_LOTE
WS_NFE_CONSULTA_AUTORIZACAO = WS_NFE_CONSULTA_RECIBO

WS_NFE_CANCELAMENTO = 2
WS_NFE_INUTILIZACAO = 3
WS_NFE_CONSULTA = 4
WS_NFE_SITUACAO = 5
WS_NFE_CONSULTA_CADASTRO = 6

WS_DPEC_RECEPCAO = 7
WS_DPEC_CONSULTA = 8

WS_NFE_RECEPCAO_EVENTO = 9
WS_NFE_DOWNLOAD = 10
WS_NFE_CONSULTA_DESTINADAS = 11

NFE_AMBIENTE_PRODUCAO = 1
NFE_AMBIENTE_HOMOLOGACAO = 2

UF_CODIGO = {
    'AC': 12,
    'AL': 27,
    'AM': 13,
    'AP': 16,
    'BA': 29,
    'CE': 23,
    'DF': 53,
    'ES': 32,
    'GO': 52,
    'MA': 21,
    'MG': 31,
    'MS': 50,
    'MT': 51,
    'PA': 15,
    'PB': 25,
    'PE': 26,
    'PI': 22,
    'PR': 41,
    'RJ': 33,
    'RN': 24,
    'RO': 11,
    'RR': 14,
    'RS': 43,
    'SC': 42,
    'SE': 28,
    'SP': 35,
    'TO': 17,
    'SUFRAMA': 90, # Código especial para eventos
    'RFB': 91, # Código especial para eventos
}

CODIGO_UF = {
    12: 'AC',
    27: 'AL',
    13: 'AM',
    16: 'AP',
    29: 'BA',
    23: 'CE',
    53: 'DF',
    32: 'ES',
    52: 'GO',
    21: 'MA',
    31: 'MG',
    50: 'MS',
    51: 'MT',
    15: 'PA',
    25: 'PB',
    26: 'PE',
    22: 'PI',
    41: 'PR',
    33: 'RJ',
    24: 'RN',
    11: 'RO',
    14: 'RR',
    43: 'RS',
    42: 'SC',
    28: 'SE',
    35: 'SP',
    17: 'TO',
    90: 'SUFRAMA', # Código especial para eventos
    91: 'RFB', # Código especial para eventos
}

