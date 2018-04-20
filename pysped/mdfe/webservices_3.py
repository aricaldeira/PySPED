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

from .webservices_flags import *


METODO_WS = {
    WS_MDFE_AUTORIZACAO: {
        'webservice': 'MDFeRecepcao',
        'metodo'    : 'MDFeRecepcao',
    },
    WS_MDFE_CONSULTA_AUTORIZACAO: {
        'webservice': 'MDFeRetRecepcao',
        'metodo'    : 'MDFeRetRecepcao',
    },
    WS_MDFE_RECEPCAO_EVENTO: {
        'webservice': 'MDFeRecepcaoEvento',
        'metodo'    : 'MDFeRecepcaoEvento',
    },
    WS_MDFE_CONSULTA: {
        'webservice': 'MDFeConsulta',
        'metodo'    : 'MDFeConsulta',
    },
    WS_MDFE_SITUACAO: {
        'webservice': 'MDFeStatusServico',
        'metodo'    : 'MDFeStatusServico',
    },
    WS_MDFE_CONSULTA_NAO_ENCERRADO: {
        'webservice': 'MDFeConsNaoEnc',
        'metodo'    : 'MDFeConsNaoEnc',
    },
}


SVRS = {
    # o servidor da consulta de cadastro é diferente dos demais...
    MDFE_AMBIENTE_PRODUCAO: {
        'servidor'                    : 'mdfe.svrs.rs.gov.br',
        WS_MDFE_AUTORIZACAO           : 'ws/MDFerecepcao/MDFeRecepcao.asmx',
        WS_MDFE_CONSULTA_AUTORIZACAO  : 'ws/MDFeRetRecepcao/MDFeRetRecepcao.asmx',
        WS_MDFE_RECEPCAO_EVENTO       : 'ws/MDFeRecepcaoEvento/MDFeRecepcaoEvento.asmx',
        WS_MDFE_CONSULTA              : 'ws/MDFeConsulta/MDFeConsulta.asmx',
        WS_MDFE_SITUACAO              : 'ws/MDFeStatusServico/MDFeStatusServico.asmx',
        WS_MDFE_CONSULTA_NAO_ENCERRADO: 'ws/MDFeConsNaoEnc/MDFeConsNaoEnc.asmx',
    },
    MDFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                    : 'mdfe-homologacao.svrs.rs.gov.br',
        WS_MDFE_AUTORIZACAO           : 'ws/MDFerecepcao/MDFeRecepcao.asmx',
        WS_MDFE_CONSULTA_AUTORIZACAO  : 'ws/MDFeRetRecepcao/MDFeRetRecepcao.asmx',
        WS_MDFE_RECEPCAO_EVENTO       : 'ws/MDFeRecepcaoEvento/MDFeRecepcaoEvento.asmx',
        WS_MDFE_CONSULTA              : 'ws/MDFeConsulta/MDFeConsulta.asmx',
        WS_MDFE_SITUACAO              : 'ws/MDFeStatusServico/MDFeStatusServico.asmx',
        WS_MDFE_CONSULTA_NAO_ENCERRADO: 'ws/MDFeConsNaoEnc/MDFeConsNaoEnc.asmx',
    }
}
