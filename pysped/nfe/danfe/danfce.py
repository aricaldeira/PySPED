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
from uuid import uuid4
from pysped.nfe.leiaute import ProtNFe_310
from pysped.nfe.leiaute import ProcEventoCancNFe_100
from py3o.template import Template
import sh


DIRNAME = os.path.dirname(__file__)


class DANFCE(object):
    def __init__(self):
        self.imprime_detalhe    = True
        self.caminho            = ''
        self.caminho_temporario = ''
        self.salvar_arquivo     = True

        self.NFe         = None
        self.protNFe     = None
        self.procEventoCancNFe = None
        self.conteudo_pdf = None

        self.obs_impressao    = 'DANFCE gerado em {agora}'
        self.nome_sistema     = ''
        self.site             = ''
        self.logo             = ''
        self.template         = ''

    def gerar_danfce(self):
        if self.NFe is None:
            raise ValueError('Não é possível gerar um DANFCE sem a informação de uma NFC-e')

        if self.protNFe is None:
            self.protNFe = ProtNFe_310()

        if self.procEventoCancNFe is None:
            self.procEventoCancNFe = ProcEventoCancNFe_100()

        #
        # Prepara o queryset para impressão
        #
        self.NFe.monta_chave()
        self.NFe.monta_qrcode()
        self.NFe.site = self.site

        # Emissão para simples conferência / sem protocolo de autorização
        self.mensagem_protocolo = ''
        self.mensagem_sem_valor = ''
        if (not self.protNFe.infProt.nProt.valor) or self.NFe.infNFe.ide.tpAmb.valor == 2:
            self.mensagem_sem_valor = 'Sem valor fiscal'

        # NF-e denegada
        if self.protNFe.infProt.cStat.valor in ('110', '301', '302'):
            self.mensagem_protocolo = 'Protocolo de Denegação '
            self.mensagem_protocolo += self.protNFe.protocolo_formatado

        # Emissão normal
        elif self.protNFe.infProt.nProt.valor:
            self.mensagem_protocolo = 'Protocolo de Autorização '
            self.mensagem_protocolo += self.protNFe.protocolo_formatado

        # A NF-e foi cancelada por um evento de cancelamento, , no DANFCE imprimir o "carimbo" de cancelamento
        self.mensagem_cancelamento = ''
        self.motivo_cancelamento = ''
        if self.procEventoCancNFe.retEvento.infEvento.nProt.valor:
            self.mensagem_cancelamento = self.procEventoCancNFe.retEvento.protocolo_formatado
            self.motivo_cancelamento = self.procEventoCancNFe.evento.infEvento.detEvento.xJust.valor

        ##
        ## Observação de impressão
        ##
        #if self.nome_sistema:
            #self.obs_impressao = self.nome_sistema + ' - ' + self.obs_impressao
        #else:
            #self.obs_impressao = self.obs_impressao


        if self.template:
            if isinstance(self.template, file):
                template = self.template
            else:
                template = open(self.template)

        else:
            template = open(os.path.join(DIRNAME, 'danfce_a4.odt'))

        self.caminho_temporario = self.caminho_temporario or '/tmp/'


        nome_arq_template = self.caminho_temporario + uuid4().hex
        open(nome_arq_template, 'w').write(template.read())
        template.close()

        nome_arq_temp = uuid4().hex
        nome_arq_odt = self.caminho_temporario + nome_arq_temp + '.odt'
        nome_arq_pdf = self.caminho_temporario + nome_arq_temp + '.pdf'

        t = Template(nome_arq_template, nome_arq_odt)
        t.render({'danfce': self})

        lo = sh.libreoffice('--headless', '--invisible', '--convert-to', 'pdf', '--outdir', '/tmp', nome_arq_odt, _bg=True)
        lo.wait()

        self.conteudo_pdf = open(nome_arq_pdf, 'r').read()

        os.remove(nome_arq_template)
        os.remove(nome_arq_odt)
        os.remove(nome_arq_pdf)

        if self.salvar_arquivo:
            nome_arq = self.caminho + self.NFe.chave + '.pdf'
            open(nome_arq, 'w').write(self.conteudo_pdf)
