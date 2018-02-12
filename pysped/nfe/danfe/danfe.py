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
from io import BytesIO
from uuid import uuid4
from pysped.nfe.leiaute import ProtNFe_400, RetCancNFe_200, ProcCancNFe_200
from pysped.nfe.leiaute import ProcEventoCancNFe_100, ProcEventoCCe_100
from py3o.template import Template
import sh


DIRNAME = os.path.dirname(__file__)


class DANFE(object):
    def __init__(self):
        self.imprime_canhoto        = True
        self.imprime_local_retirada = True
        self.imprime_local_entrega  = True
        self.imprime_fatura         = True
        self.imprime_duplicatas     = True
        self.imprime_issqn          = True

        self.caminho            = ''
        self.caminho_temporario = ''
        self.salvar_arquivo     = True

        self.NFe               = None
        self.protNFe           = None
        self.procEventoCancNFe = None
        self.procEventoCCe     = None
        self.reset()

        self.nome_sistema     = ''
        self.site             = ''
        self.logo             = ''
        self.cabecalho        = ''
        self.template         = ''

    def reset(self):
        self.protNFe     = ProtNFe_400()
        self.procEventoCancNFe = ProcEventoCancNFe_100()
        self.procEventoCCe = ProcEventoCCe_100()
        self.conteudo_pdf = None

    def _gera_pdf(self, template):
        self.caminho_temporario = self.caminho_temporario or '/tmp/'

        nome_arq_template = self.caminho_temporario + uuid4().hex
        open(nome_arq_template, 'wb').write(template.read())
        template.close()

        nome_arq_temp = uuid4().hex
        nome_arq_odt = self.caminho_temporario + nome_arq_temp + '.odt'
        nome_arq_pdf = self.caminho_temporario + nome_arq_temp + '.pdf'

        t = Template(nome_arq_template, nome_arq_odt)
        t.render({'danfe': self})

        lo = sh.libreoffice('--headless', '--invisible', '--convert-to', 'pdf', '--outdir', '/tmp', nome_arq_odt, _bg=True)
        lo.wait()

        self.conteudo_pdf = open(nome_arq_pdf, 'rb').read()

        os.remove(nome_arq_template)
        os.remove(nome_arq_odt)
        os.remove(nome_arq_pdf)

    def gerar_danfe(self):
        if self.NFe is None:
            raise ValueError('Não é possível gerar um DANFE sem a informação de uma NF-e')

        if self.protNFe is None:
            self.reset()

        #
        # Prepara o queryset para impressão
        #
        self.NFe.monta_chave()
        self.NFe.site = self.site

        if self.template:
            if isinstance(self.template, str):
                template = open(self.template, 'rb')
            else:
                template = self.template

        else:
            template = open(os.path.join(DIRNAME, 'danfe_a4_retrato.odt'), 'rb')

        self._gera_pdf(template)

        if self.salvar_arquivo:
            nome_arq = self.caminho + self.NFe.chave + '.pdf'
            open(nome_arq, 'wb').write(self.conteudo_pdf)

    def gerar_dacce(self):
        if self.NFe is None:
            raise ValueError('Não é possível gerar um DACCE sem a informação de uma NF-e')

        if self.protNFe is None:
            self.reset()

        if not self.procEventoCCe.retEvento.infEvento.cStat.valor:
            raise ValueError('Não é possível gerar um DACCE sem a informação de uma CC-e')

        #
        # Prepara o queryset para impressão
        #
        self.NFe.monta_chave()
        self.NFe.site = self.site

        if self.template:
            if isinstance(self.template, (file, BytesIO)):
                template = self.template
            else:
                template = open(self.template, 'rb')

        else:
            template = open(os.path.join(DIRNAME, 'dacce_a4_retrato.odt'), 'rb')

        self._gera_pdf(template)

        if self.salvar_arquivo:
            nome_arq = self.caminho + 'cce-'
            nome_arq += str(self.procEventoCCe.evento.infEvento.nSeqEvento.valor).zfill(2)
            nome_arq += '-' + self.NFe.chave + '.pdf'
            open(nome_arq, 'wb').write(self.conteudo_pdf)

    def gerar_duplicata(self):
        if self.NFe is None:
            raise ValueError('Não é possível gerar uma duplicata sem a informação de uma NF-e')

        if self.protNFe is None:
            self.reset()

        #
        # Prepara o queryset para impressão
        #
        self.NFe.monta_chave()
        self.NFe.site = self.site

        if self.template:
            if isinstance(self.template, (file, BytesIO)):
                template = self.template
            else:
                template = open(self.template, 'rb')

        else:
            template = open(os.path.join(DIRNAME, 'duplicata_a4_retrato.odt'), 'rb')

        self._gera_pdf(template)

        if self.salvar_arquivo:
            nome_arq = self.caminho + 'duplicatas-' + self.NFe.chave + '.pdf'
            open(nome_arq, 'wb').write(self.conteudo_pdf)

    @property
    def fatura_a_prazo(self):
        if not (self.NFe.infNFe.cobr.fat.nFat.valor or
                self.NFe.infNFe.cobr.fat.vOrig.valor or
                self.NFe.infNFe.cobr.fat.vDesc.valor or
                self.NFe.infNFe.cobr.fat.vLiq.valor):
            return False

        if (self.NFe.infNFe.ide.indPag.valor == 1) or \
            (len(self.NFe.infNFe.cobr.dup) > 1) or \
            ((len(self.NFe.infNFe.cobr.dup) == 1) and \
            (self.NFe.infNFe.cobr.dup[0].dVenc.valor.toordinal() > self.NFe.infNFe.ide.dEmi.valor.toordinal())):
            return True

        return False

    @property
    def fatura_a_vista(self):
        if not (self.NFe.infNFe.cobr.fat.nFat.valor or
                self.NFe.infNFe.cobr.fat.vOrig.valor or
                self.NFe.infNFe.cobr.fat.vDesc.valor or
                self.NFe.infNFe.cobr.fat.vLiq.valor):
            return False

        return not self.fatura_a_prazo
