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

from os.path import abspath, dirname
from pysped.nfe import ProcessadorNFe
from pysped.nfe.webservices_flags import *
from pysped.nfe.leiaute import *


FILE_DIR = abspath(dirname(__file__))

#
#
# ATENÇÃO!
#
# Em todas as consultas que eu tentei, a RFB sempre me diz que não
# retorna as notas solicitadas, mesmo em produção.
# Se alguém conseguir um resultado positivo da RFB, me avise, porque daí
# vou poder dar a tratativa dos arquivos zipados que virão na resposta.
#
#


if __name__ == '__main__':
    p = ProcessadorNFe()
    p.versao              = '2.00'
    p.estado              = 'SP'
    #p.certificado.arquivo = 'certificado.pfx'
    #p.certificado.senha   = 'senha'

    #
    # arquivo 'certificado_caminho.txt' deve conter o caminho para o 'certificado.pfx'
    #
    p.certificado.arquivo = open(FILE_DIR+'/certificado_caminho.txt').read().strip()

    #
    # arquivo 'certificado_senha.txt' deve conter a senha para o 'certificado.pfx'
    #
    p.certificado.senha   = open(FILE_DIR+'/certificado_senha.txt').read().strip()

    p.salva_arquivos      = True
    p.contingencia_SCAN   = False
    p.caminho = ''

    #
    # O retorno de cada webservice é um objeto
    # com as seguintes propriedades
    #  .webservice - o webservice que foi consultado
    #  .envio - o objeto da classe XMLNFE enviado
    #  .envio.original - o texto do xml (envelope SOAP) enviado ao webservice
    #  .resposta - o objeto da classe XMLNFE retornado
    #  .resposta.version - version da HTTPResponse
    #  .resposta.status - status da HTTPResponse
    #  .resposta.reason - reason da HTTPResponse
    #  .resposta.msg - msg da HTTPResponse
    #  .resposta.original - o texto do xml (SOAP) recebido do webservice
    #
    processo = p.baixar_notas_destinadas(
        cnpj='34274233006488',
        lista_chaves=[
            '35120834274233006488550000005885641180809921',
            '35120834274233006488550000005885642180809921',
            ]
        )

    print(processo)
    print()
    print(processo.envio.xml)
    print()
    print(processo.envio.original)
    print()
    print(processo.resposta.xml)
    print()
    print(processo.resposta.original)
    print()
    print(processo.resposta.reason)
