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

from StringIO import StringIO
from geraldo.generators import PDFGenerator
from pysped.nfe.danfe.daederetrato import DAEDERetrato


class DAEDE(object):
    def __init__(self):
        self.caminho           = ''
        self.salvar_arquivo    = True

        self.NFe          = None
        self.protNFe      = None
        self.procEventos  = []
        self.daede        = None
        self.conteudo_pdf = None

        self.obs_impressao    = 'DAEDE gerado em %(now:%d/%m/%Y, %H:%M:%S)s'
        self.nome_sistema     = ''
        self.site             = ''
        self.logo             = ''
        self.leiaute_logo_vertical = False
        self.dados_emitente   = []

    def gerar_daede(self):
        if self.NFe is None:
            raise ValueError('Não é possível gerar um DAEDE sem a informação de uma NF-e')

        if self.protNFe is None:
            self.protNFe = ProtNFe_310()

        #
        # Prepara o queryset para impressão
        #
        self.NFe.monta_chave()
        self.NFe.site = self.site

        #
        # Prepara as bandas de impressão
        #
        self.daede = DAEDERetrato()
        self.daede.queryset = self.procEventos
        for pe in self.daede.queryset:
            pe.NFe = self.NFe
            pe.protNFe = self.protNFe

        self.daede.band_page_header = self.daede.remetente
        self.daede.band_page_header.child_bands = []
        self.daede.band_page_header.child_bands.append(self.daede.destinatario)

        self.daede.band_detail = self.daede.det_evento

        #
        # Observação de impressão
        #
        if self.nome_sistema:
            self.daede.ObsImpressao.expression = self.nome_sistema + ' - ' + self.obs_impressao
        else:
            self.daede.ObsImpressao.expression = self.obs_impressao

        #
        # Quadro do emitente
        #
        # Personalizado?
        if self.dados_emitente:
            self.daede.remetente.monta_quadro_emitente(self.dados_emitente)
        else:
            # Sem logotipo
            if not self.logo:
                self.daede.remetente.monta_quadro_emitente(self.daede.remetente.dados_emitente_sem_logo())

            # Logotipo na vertical
            elif self.leiaute_logo_vertical:
                self.daede.remetente.monta_quadro_emitente(self.daede.remetente.dados_emitente_logo_vertical(self.logo))

            # Logotipo na horizontal
            else:
                self.daede.remetente.monta_quadro_emitente(self.daede.remetente.dados_emitente_logo_horizontal(self.logo))

        daede_pdf = StringIO()
        self.daede.generate_by(PDFGenerator, filename=daede_pdf)
        self.conteudo_pdf = daede_pdf.getvalue()
        daede_pdf.close()

        if self.salvar_arquivo:
            nome_arq = self.caminho + 'eventos-' + self.NFe.chave + '.pdf'
            self.daede.generate_by(PDFGenerator, filename=nome_arq)
