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
from pysped.nfe.danfe.danferetrato import DANFERetrato
from pysped.nfe.leiaute import ProtNFe_310, RetCancNFe_200, ProcCancNFe_200
from pysped.nfe.leiaute import ProcEventoCancNFe_100


class DANFE(object):
    def __init__(self):
        self.imprime_canhoto        = True
        self.imprime_local_retirada = True
        self.imprime_local_entrega  = True
        self.imprime_fatura         = True
        self.imprime_duplicatas     = True
        self.imprime_issqn          = True

        self.caminho           = ''
        self.salvar_arquivo    = True

        self.NFe         = None
        self.protNFe     = None
        self.procCancNFe = None
        self.retCancNFe  = None
        self.procEventoCancNFe = None
        self.danfe       = None
        self.conteudo_pdf = None

        self.obs_impressao    = 'DANFE gerado em %(now:%d/%m/%Y, %H:%M:%S)s'
        self.nome_sistema     = ''
        self.site             = ''
        self.logo             = ''
        self.leiaute_logo_vertical = False
        self.dados_emitente   = []

    def gerar_danfe(self):
        if self.NFe is None:
            raise ValueError('Não é possível gerar um DANFE sem a informação de uma NF-e')

        if self.protNFe is None:
            self.protNFe = ProtNFe_310()

        if self.retCancNFe is None:
            self.retCancNFe = RetCancNFe_200()

        if self.procCancNFe is None:
            self.procCancNFe = ProcCancNFe_200()

        if self.procEventoCancNFe is None:
            self.procEventoCancNFe = ProcEventoCancNFe_100()

        #
        # Prepara o queryset para impressão
        #
        self.NFe.monta_chave()
        self.NFe.monta_dados_contingencia_fsda()
        self.NFe.site = self.site

        for detalhe in self.NFe.infNFe.det:
            detalhe.NFe = self.NFe
            detalhe.protNFe = self.protNFe
            detalhe.retCancNFe = self.retCancNFe
            detalhe.procCancNFe = self.procCancNFe
            detalhe.procEventoCancNFe = self.procEventoCancNFe

        #
        # Prepara as bandas de impressão para cada formato
        #
        if self.NFe.infNFe.ide.tpImp.valor == 2:
            raise ValueError('DANFE em formato paisagem ainda não implementado')
        else:
            self.danfe = DANFERetrato()
            self.danfe.queryset = self.NFe.infNFe.det

        if self.imprime_canhoto:
            self.danfe.band_page_header = self.danfe.canhoto
            self.danfe.band_page_header.child_bands = []
            self.danfe.band_page_header.child_bands.append(self.danfe.remetente)
        else:
            self.danfe.band_page_header = self.danfe.remetente
            self.danfe.band_page_header.child_bands = []

        # Emissão para simples conferência / sem protocolo de autorização
        if not self.protNFe.infProt.nProt.valor:
            self.danfe.remetente.campo_variavel_conferencia()

        # NF-e denegada
        elif self.protNFe.infProt.cStat.valor in ('110', '301', '302'):
            #self.danfe.remetente.campo_variavel_denegacao()
            self.danfe.remetente.campo_variavel_normal()
            self.danfe.remetente.obs_denegacao()

            #
            # Adiciona a observação de quem é a irregularidade fiscal
            #
            #if self.protNFe.infProt.cStat.valor == '301':
                #self.danfe.remetente.find_by_name('txt_remetente_var1').text = b'A circulação da mercadoria foi <font color="red"><b>PROIBIDA</b></font> pela SEFAZ<br />autorizadora, devido a irregularidades fiscais do emitente.'
            #elif self.protNFe.infProt.cStat.valor == '302':
                #self.danfe.remetente.find_by_name('txt_remetente_var1').text = b'A circulação da mercadoria foi <font color="red"><b>PROIBIDA</b></font> pela SEFAZ<br />autorizadora, devido a irregularidades fiscais do destinatário.'

        # Emissão em contingência com FS ou FSDA
        elif self.NFe.infNFe.ide.tpEmis.valor in (2, 5,):
            self.danfe.remetente.campo_variavel_contingencia_fsda()
            self.danfe.remetente.obs_contingencia_normal_scan()

        # Emissão em contingência com DPEC
        elif self.NFe.infNFe.ide.tpEmis.valor == 4:
            self.danfe.remetente.campo_variavel_contingencia_dpec()
            self.danfe.remetente.obs_contingencia_dpec()

        # Emissão normal ou contingência SCAN
        else:
            self.danfe.remetente.campo_variavel_normal()
            # Contingência SCAN
            if self.NFe.infNFe.ide.tpEmis.valor == 3:
                self.danfe.remetente.obs_contingencia_normal_scan()

        # A NF-e foi cancelada, no DANFE imprimir o "carimbo" de cancelamento
        if self.retCancNFe.infCanc.nProt.valor or self.procCancNFe.retCancNFe.infCanc.nProt.valor:
            if self.procCancNFe.cancNFe.infCanc.xJust.valor:
                self.danfe.remetente.obs_cancelamento_com_motivo()
            else:
                self.danfe.remetente.obs_cancelamento()

        # A NF-e foi cancelada por um evento de cancelamento, , no DANFE imprimir o "carimbo" de cancelamento
        if self.procEventoCancNFe.retEvento.infEvento.nProt.valor:
            if self.procEventoCancNFe.evento.infEvento.detEvento.xJust.valor:
              self.danfe.remetente.obs_cancelamento_com_motivo_evento()
            else:
              self.danfe.remetente.obs_cancelamento_evento()

        # Observação de ausência de valor fiscal
        # se não houver protocolo ou se o ambiente for de homologação
        if (not self.protNFe.infProt.nProt.valor) or self.NFe.infNFe.ide.tpAmb.valor == 2:
            self.danfe.remetente.obs_sem_valor_fiscal()

        self.danfe.band_page_header.child_bands.append(self.danfe.destinatario)

        if self.imprime_local_retirada and len(self.NFe.infNFe.retirada.xml):
            self.danfe.band_page_header.child_bands.append(self.danfe.local_retirada)

        if self.imprime_local_entrega and len(self.NFe.infNFe.entrega.xml):
            self.danfe.band_page_header.child_bands.append(self.danfe.local_entrega)

        if self.imprime_fatura:
            # Pagamento a prazo
            if (self.NFe.infNFe.ide.indPag.valor == 1) or \
                (len(self.NFe.infNFe.cobr.dup) > 1) or \
                ((len(self.NFe.infNFe.cobr.dup) == 1) and \
                (self.NFe.infNFe.cobr.dup[0].dVenc.valor.toordinal() > self.NFe.infNFe.ide.dEmi.valor.toordinal())):

                if self.imprime_duplicatas:
                    self.danfe.fatura_a_prazo.elements.append(self.danfe.duplicatas)

                self.danfe.band_page_header.child_bands.append(self.danfe.fatura_a_prazo)

            # Pagamento a vista
            elif (self.NFe.infNFe.ide.indPag.valor != 2):
                self.danfe.band_page_header.child_bands.append(self.danfe.fatura_a_vista)

                if self.imprime_duplicatas:
                    self.danfe.fatura_a_vista.elements.append(self.danfe.duplicatas)

        self.danfe.band_page_header.child_bands.append(self.danfe.calculo_imposto)
        self.danfe.band_page_header.child_bands.append(self.danfe.transporte)
        self.danfe.band_page_header.child_bands.append(self.danfe.cab_produto)

        if self.imprime_issqn and len(self.NFe.infNFe.total.ISSQNTot.xml):
            self.danfe.band_page_footer = self.danfe.iss
        else:
            self.danfe.band_page_footer = self.danfe.dados_adicionais

        self.danfe.band_detail = self.danfe.det_produto

        #
        # Observação de impressão
        #
        if self.nome_sistema:
            self.danfe.ObsImpressao.expression = self.nome_sistema + ' - ' + self.obs_impressao
        else:
            self.danfe.ObsImpressao.expression = self.obs_impressao

        #
        # Quadro do emitente
        #
        # Personalizado?
        if self.dados_emitente:
            self.danfe.remetente.monta_quadro_emitente(self.dados_emitente)
        else:
            # Sem logotipo
            if not self.logo:
                self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_sem_logo())

            # Logotipo na vertical
            elif self.leiaute_logo_vertical:
                self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_logo_vertical(self.logo))

            # Logotipo na horizontal
            else:
                self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_logo_horizontal(self.logo))

        danfe_pdf = StringIO()
        self.danfe.generate_by(PDFGenerator, filename=danfe_pdf)
        self.conteudo_pdf = danfe_pdf.getvalue()
        danfe_pdf.close()

        if self.salvar_arquivo:
            nome_arq = self.caminho + self.NFe.chave + '.pdf'
            self.danfe.generate_by(PDFGenerator, filename=nome_arq)
