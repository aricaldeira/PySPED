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

import os
import base64
from io import BytesIO
from py3o.template import Template
import sh

from .danfe import DANFE

DIRNAME = os.path.dirname(__file__)

CACHE_LOGO = {}


class DANFSE(DANFE):
    def __init__(self):
        super(DANFSE, self).__init__()
        self.imprime_descricao_servico = True
        self.imprime_item_servico      = True
        self.imprime_codigo_cnae       = True
        self.imprime_codigo_servico    = True
        self.imprime_construcao_civil  = False

    def reset(self):
        super(DANFSE, self).reset()

    def gerar_danfse(self):
        if self.NFe is None:
            raise ValueError('Não é possível gerar um DANFSE sem a informação de uma NFS-e')

        if self.protNFe is None:
            self.reset()

        #
        # Prepara o queryset para impressão
        #
        self.NFe.site = self.site

        if self.template:
            if isinstance(self.template, (file, BytesIO)):
                template = self.template
            else:
                template = open(self.template, 'rb')

        else:
            template = open(os.path.join(DIRNAME, 'danfse_a4.odt'), 'rb')

        self._gera_pdf(template)

        if self.salvar_arquivo:
            #nome_arq = self.caminho + self.NFe.chave + '.pdf'
            nome_arq = self.caminho + 'nfse.pdf'
            open(nome_arq, 'wb').write(self.conteudo_pdf)

    def gerar_danfe(self):
        self.gerar_danfse()

    @property
    def logo_prefeitura(self):
        if self.NFe is None:
            return ''

        if not self.NFe.nome_cidade:
            return ''

        if self.NFe.nome_cidade in CACHE_LOGO:
            return CACHE_LOGO[self.NFe.nome_cidade]

        caminho_logo = os.path.join(DIRNAME, '../../nfse/logo_prefeitura/', self.NFe.nome_cidade + '.jpeg')

        if not os.path.exists(caminho_logo):
            return ''

        logo = open(caminho_logo, 'rb').read()

        CACHE_LOGO[self.NFe.nome_cidade] = base64.encodebytes(logo)

        return CACHE_LOGO[self.NFe.nome_cidade]
