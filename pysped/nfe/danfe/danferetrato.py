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


from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor

from geraldo import Report, SubReport
from geraldo import SystemField, Line, Rect, Image
from geraldo.barcodes import BarCode

from pysped.relato_sped.base import (BandaDANFE,
                                     Campo,
                                     DADO_CAMPO_NEGRITO,
                                     DADO_CAMPO_NUMERICO_NEGRITO,
                                     DADO_CHAVE,
                                     DADO_COMPLEMENTAR,
                                     DADO_PRODUTO,
                                     DADO_PRODUTO_CENTRALIZADO,
                                     DADO_VARIAVEL_CANCELAMENTO,
                                     DADO_VARIAVEL,
                                     DESCRITIVO_CAMPO,
                                     DESCRITIVO_CAMPO_CANCELAMENTO,
                                     DESCRITIVO_CAMPO_NEGRITO,
                                     DESCRITIVO_DANFE,
                                     DESCRITIVO_DANFE_ES,
                                     DESCRITIVO_DANFE_GERAL,
                                     DESCRITIVO_NUMERO,
                                     DESCRITIVO_PRODUTO,
                                     EMIT_DADOS,
                                     EMIT_NOME,
                                     FONTES_ADICIONAIS,
                                     LabelMargemEsquerda,
                                     OBS_CANCELAMENTO,
                                     OBS_DENEGACAO,
                                     OBS_HOMOLOGACAO,
                                     OBS_CONTINGENCIA,
                                     MARGEM_DIREITA,
                                     MARGEM_ESQUERDA,
                                     MARGEM_INFERIOR,
                                     MARGEM_SUPERIOR,
                                     RETRATO,
                                     Texto)
from pysped.nfe.manual_401 import Vol_200


class DANFERetrato(Report):
    def __init__(self, *args, **kargs):
        super(DANFERetrato, self).__init__(*args, **kargs)
        self.title = 'DANFE - Documento Auxiliar da Nota Fiscal Eletrônica'
        self.print_if_empty = True
        self.additional_fonts = FONTES_ADICIONAIS

        self.page_size = RETRATO
        self.margin_top = MARGEM_SUPERIOR
        self.margin_bottom = MARGEM_INFERIOR
        self.margin_left = MARGEM_ESQUERDA
        self.margin_right = MARGEM_DIREITA

        # Bandas e observações
        self.canhoto          = CanhotoRetrato()
        self.remetente        = RemetenteRetrato()
        self.destinatario     = DestinatarioRetrato()
        self.local_retirada   = LocalRetiradaRetrato()
        self.local_entrega    = LocalEntregaRetrato()
        self.fatura_a_vista   = FaturaAVistaRetrato()
        self.fatura_a_prazo   = FaturaAPrazoRetrato()
        self.duplicatas       = DuplicatasRetrato()
        self.calculo_imposto  = CalculoImpostoRetrato()
        self.transporte       = TransporteRetrato()
        self.cab_produto      = CabProdutoRetrato()
        self.det_produto      = DetProdutoRetrato()
        self.iss              = ISSRetrato()
        self.dados_adicionais = DadosAdicionaisRetrato()
        self.rodape_final     = RodapeFinalRetrato()

        #
        # Guarda a definição do cabeçalho e rodapé da 1ª página
        #
        self.cabecalho_primeira_pagina = None
        self.cabecalho_primeira_pagina_filhos = None
        self.remetente_filhos = None
        self.rodape_primeira_pagina = None

    def on_new_page(self, page, page_number, generator):
        if page_number == 1:
            if self.cabecalho_primeira_pagina is None:
                self.cabecalho_primeira_pagina = self.band_page_header
                self.cabecalho_primeira_pagina_filhos = list(self.band_page_header.child_bands)
                self.remetente_filhos = list(self.remetente.child_bands)
                self.rodape_primeira_pagina = self.band_page_footer

            else:
                self.band_page_header = self.cabecalho_primeira_pagina
                #self.band_page_header.child_bands = []
                self.band_page_header.child_bands = self.cabecalho_primeira_pagina_filhos
                #self.remetente.child_bands = []
                self.remetente.child_bands = self.remetente_filhos
                self.band_page_footer = self.rodape_primeira_pagina

        else:
            self.band_page_footer = self.rodape_final

            self.band_page_header = self.remetente
            self.band_page_header.child_bands = [self.cab_produto]

    def format_date(self, data, formato):
        return  data.strftime(formato.encode('utf-8')).decode('utf-8')


    class ObsImpressao(SystemField):
        expression = u'DANFE gerado em %(now:%d/%m/%Y, %H:%M:%S)s'

        def __init__(self):
            self.name = 'obs_impressao'
            self.top = 0*cm
            self.left = 0.1*cm
            self.width = 19.4*cm
            self.height = 0.2*cm
            self.style = DADO_PRODUTO
            self.borders = {'bottom': 0.1}


class CanhotoRetrato(BandaDANFE):
    def __init__(self):
        super(CanhotoRetrato, self).__init__()
        self.elements = []
        lbl, txt = self.inclui_texto(nome='', titulo='', texto=u'', top=0*cm, left=0*cm, width=16*cm)
        fld = self.inclui_campo_sem_borda(nome='canhoto_recebemos', conteudo=u'NFe.canhoto_formatado', top=0*cm, left=0*cm, width=16*cm)
        fld.borders = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': False}
        fld.padding_top = 0.08*cm
        fld.padding_left = 0.08*cm
        fld.padding_bottom = 0.08*cm
        fld.padding_right = 0.08*cm
        fld.style = DESCRITIVO_CAMPO
        fld.height = 0.70*cm

        self.inclui_texto(nome='canhoto_data', titulo=u'DATA DE RECEBIMENTO', texto='', top=0.7*cm, left=0*cm, width=2.7*cm)
        self.inclui_texto(nome='canhoto_assinatura', titulo=u'IDENTIFICAÇÃO E ASSINATURA DO RECEBEDOR', texto='', top=0.7*cm, left=2.7*cm, width=13.3*cm)

        lbl, txt = self.inclui_texto(nome='canhoto_nfe', titulo=u'NF-e', texto='', top=0*cm, left=16*cm, width=3.4*cm, height=1.4*cm, margem_direita=True)
        lbl.style = DESCRITIVO_NUMERO
        fld = self.inclui_campo_sem_borda(nome='canhoto_numero', conteudo=u'NFe.numero_formatado', top=0.35*cm, left=16*cm, width=3.4*cm, height=0.5*cm)
        fld.style = DESCRITIVO_NUMERO
        fld = self.inclui_campo_sem_borda(nome='canhoto_serie', conteudo=u'NFe.serie_formatada', top=0.8*cm, left=16*cm, width=3.4*cm, height=0.5*cm)
        fld.style = DESCRITIVO_NUMERO

        self.elements.append(Line(top=1.65*cm, bottom=1.65*cm, left=0*cm, right=19.4*cm, stroke_width=0.1))
        self.height = 1.9*cm


class RemetenteRetrato(BandaDANFE):
    def __init__(self):
        super(RemetenteRetrato, self).__init__()
        self.elements = []

        # Quadro do emitente
        self.inclui_texto(nome='quadro_emitente', titulo='', texto='', top=0*cm, left=0*cm, width=8*cm, height=4*cm)

        #
        # Área central - Dados do DANFE
        #
        lbl, txt = self.inclui_texto(nome='danfe', titulo='', texto=u'DANFE', top=0*cm, left=8*cm, width=3.4*cm, height=4*cm)
        txt.style = DESCRITIVO_DANFE

        txt = self.inclui_texto_sem_borda(nome='danfe_ext', texto=u'DOCUMENTO AUXILIAR DA NOTA FISCAL ELETRÔNICA', top=0.6*cm, left=8*cm, width=3.4*cm, height=4*cm)
        txt.style = DESCRITIVO_DANFE_GERAL

        txt = self.inclui_texto_sem_borda(nome='danfe_ext', texto=u'versão', top=1.1*cm, left=8.8*cm, width=1.4*cm, height=0.6*cm)
        txt.style = DESCRITIVO_DANFE_GERAL

        fld = self.inclui_campo_sem_borda(nome='danfe_entrada_saida', conteudo=u'NFe.infNFe.versao.valor', top=1.1*cm, left=9.8*cm, width=0.8*cm, height=0.6*cm)
        fld.style = DESCRITIVO_DANFE_GERAL

        txt = self.inclui_texto_sem_borda(nome='danfe_entrada', texto=u'0 - ENTRADA', top=1.5*cm, left=8.3*cm, width=3.4*cm, height=4*cm)
        txt.style = DESCRITIVO_DANFE_ES

        txt = self.inclui_texto_sem_borda(nome='danfe_saida', texto=u'1 - SAÍDA', top=1.9*cm, left=8.3*cm, width=3.4*cm, height=4*cm)
        txt.style = DESCRITIVO_DANFE_ES

        fld = self.inclui_campo_sem_borda(nome='danfe_entrada_saida', conteudo=u'NFe.infNFe.ide.tpNF.valor', top=1.65*cm, left=10.4*cm, width=0.6*cm, height=0.6*cm)
        fld.style = DESCRITIVO_NUMERO
        fld.borders = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': 0.1}
        fld.padding_bottom = 0.2*cm

        fld = self.inclui_campo_sem_borda(nome='danfe_numero', conteudo=u'NFe.numero_formatado', top=2.4*cm, left=8*cm, width=3.4*cm, height=0.5*cm)
        fld.style = DESCRITIVO_NUMERO

        fld = self.inclui_campo_sem_borda(nome='danfe_serie', conteudo=u'NFe.serie_formatada', top=2.85*cm, left=8*cm, width=3.4*cm, height=0.5*cm)
        fld.style = DESCRITIVO_NUMERO

        fld = SystemField(name='fld_danfe_folha', expression=u'FOLHA %(page_number)02d/%(page_count)02d', top=3.3*cm, left=8*cm, width=3.4*cm, height=0.5*cm)
        fld.padding_top = 0.1*cm
        fld.style = DESCRITIVO_NUMERO
        self.elements.append(fld)

        #
        # No caso dos códigos de barra, altura (height) e largura (width) se referem às barras, não à imagem
        #
        self.elements.append(Line(top=0*cm, bottom=0*cm, left=11.4*cm, right=19.4*cm, stroke_width=0.1))
        self.elements.append(BarCode(type=u'Code128', attribute_name=u'NFe.chave_para_codigo_barras', top=((1.625-0.8)/2.0)*cm, left=11.3*cm, width=0.025*cm, height=0.8*cm))

        lbl, fld = self.inclui_campo(nome='remetente_chave', titulo=u'CHAVE DE ACESSO', conteudo=u'NFe.chave_formatada', top=1.625*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        fld.style = DADO_CHAVE

        self.inclui_campo(nome='remetente_natureza', titulo=u'NATUREZA DA OPERAÇÃO', conteudo=u'NFe.infNFe.ide.natOp.valor', top=4*cm, left=0*cm, width=11.4*cm)

        self.inclui_campo(nome='remetente_ie', titulo=u'INSCRIÇÃO ESTADUAL', conteudo=u'NFe.infNFe.emit.IE.valor', top=4.70*cm, left=0*cm, width=6.4*cm)
        self.inclui_campo(nome='remetente_iest', titulo=u'INSCRIÇÃO ESTADUAL DO SUBSTITUTO TRIBUTÁRIO', conteudo=u'NFe.infNFe.emit.IEST.valor', top=4.70*cm, left=6.4*cm, width=6.6*cm)
        self.inclui_campo(nome='remetente_cnpj', titulo=u'CNPJ', conteudo=u'NFe.cnpj_emitente_formatado', top=4.70*cm, left=13*cm, width=6.4*cm, margem_direita=True)

        self.height = 5.4*cm

    def campo_variavel_conferencia(self):
        txt = self.inclui_texto_sem_borda(nome='remetente_var1', texto=u'<font color="red"><b>Impresso para simples conferência<br />Informações ainda não transmitidas a nenhuma SEFAZ autorizadora, nem ao SCAN<br />Sem valor fiscal</b></font>', top=2.375*cm, left=11.4*cm, width=8*cm, height=1.625*cm)
        txt.padding_top = 0*cm
        txt.style = DADO_VARIAVEL

        lbl, lbl = self.inclui_campo(nome='remetente_var2', titulo=u'PROTOCOLO DE AUTORIZAÇÃO DE USO', conteudo=u'protNFe.protocolo_formatado', top=4*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        lbl.style = DADO_VARIAVEL

    def campo_variavel_normal(self):
        txt = self.inclui_texto_sem_borda(nome='remetente_var1', texto=u'Consulta de autenticidade no portal nacional da NF-e<br /><a href="http://www.nfe.fazenda.gov.br/portal"><u>www.nfe.fazenda.gov.br</u></a><br /> ou no site da SEFAZ autorizadora', top=2.375*cm, left=11.4*cm, width=8*cm, height=1.625*cm)
        txt.padding_top = 0.2*cm
        txt.style = DADO_VARIAVEL

        #fld = self.inclui_campo_sem_borda(nome='remetente_var1', conteudo=u'NFe.consulta_autenticidade', top=2.375*cm, left=11.4*cm, width=8*cm, height=1.625*cm)
        #fld.padding_top = 0.2*cm
        #fld.style = DADO_VARIAVEL

        lbl, lbl = self.inclui_campo(nome='remetente_var2', titulo=u'PROTOCOLO DE AUTORIZAÇÃO DE USO', conteudo=u'protNFe.protocolo_formatado', top=4*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        lbl.style = DADO_VARIAVEL

    def campo_variavel_denegacao(self):
        txt = self.inclui_texto_sem_borda(nome='remetente_var1', texto=u'A circulação da mercadoria foi <font color="red"><b>PROIBIDA</b></font> pela SEFAZ<br />autorizadora, devido a irregularidades fiscais.', top=2.375*cm, left=11.4*cm, width=8*cm, height=1.625*cm)
        txt.padding_top = 0.2*cm
        txt.style = DADO_VARIAVEL

        lbl, lbl = self.inclui_campo(nome='remetente_var2', titulo=u'PROTOCOLO DE DENEGAÇÃO DE USO', conteudo=u'protNFe.protocolo_formatado', top=4*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        lbl.style = DADO_VARIAVEL

    def campo_variavel_contingencia_fsda(self):
        #
        # No caso dos códigos de barra, altura (height) e largura (width) se referem às barras, não à imagem
        #
        self.elements.append(Line(top=0*cm, bottom=0*cm, left=11.4*cm, right=19.4*cm, stroke_width=0.1))
        self.elements.append(BarCode(type=u'Code128', attribute_name=u'NFe.dados_contingencia_fsda_para_codigo_barras', top=(2.375 + ((1.625 - 0.8) / 2.0))*cm, left=11.9*cm, width=0.025*cm, height=0.8*cm))

        lbl, fld = self.inclui_campo(nome='remetente_var2', titulo=u'DADOS DA NF-e', conteudo=u'NFe.dados_contingencia_fsda_formatados', top=4*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        fld.style = DADO_CHAVE

    def campo_variavel_contingencia_dpec(self):
        txt = self.inclui_texto_sem_borda(nome='remetente_var1', texto=u'Consulta de autenticidade no portal nacional da NF-e<br /><a href="http://www.nfe.fazenda.gov.br/portal"><u>www.nfe.fazenda.gov.br/portal</u></a>', top=2.375*cm, left=11.4*cm, width=8*cm, height=1.625*cm)
        txt.padding_top = 0.4*cm
        txt.style = DADO_VARIAVEL

        lbl, txt = self.inclui_texto(nome='remetente_var2', titulo=u'NÚMERO DE REGISTRO DPEC', texto=u'123456789012345 99/99/9999 99:99:99', top=4*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        txt.style = DADO_VARIAVEL

    def obs_cancelamento(self):
        txt = Texto()
        txt.name   = 'txt_obs_cancelamento'
        txt.text   = u'cancelada'
        #txt.top    = -0.1*cm
        txt.top    = 3.5*cm
        txt.left   = 4.7*cm
        txt.width  = 10*cm
        txt.height = 1.5*cm
        txt.padding_top = 0.1*cm
        txt.style  = OBS_CANCELAMENTO
        self.elements.insert(0, txt)

        lbl = LabelMargemEsquerda()
        lbl.borders = None
        lbl.name = 'lbl_prot_cancelamento'
        lbl.text = u'PROTOCOLO<br />DE CANCELAMENTO'
        lbl.top = 5.35*cm
        lbl.left = 6.15*cm
        lbl.width = 1.75*cm
        lbl.style = DESCRITIVO_CAMPO_CANCELAMENTO
        self.elements.insert(2, lbl)

        fld = Campo()
        fld.name = 'fld_prot_cancelamento'
        fld.attribute_name = u'retCancNFe.protocolo_formatado'
        fld.top  = 5.15*cm
        fld.left = 7.5*cm
        fld.width = 6.3*cm
        fld.padding_top = 0.25*cm
        fld.style = DADO_VARIAVEL_CANCELAMENTO
        self.elements.insert(3, fld)

    def obs_cancelamento_evento(self):
        txt = Texto()
        txt.name   = 'txt_obs_cancelamento'
        txt.text   = u'cancelada'
        #txt.top    = -0.1*cm
        txt.top    = 3.5*cm
        txt.left   = 4.7*cm
        txt.width  = 10*cm
        txt.height = 1.5*cm
        txt.padding_top = 0.1*cm
        txt.style  = OBS_CANCELAMENTO
        self.elements.insert(0, txt)

        lbl = LabelMargemEsquerda()
        lbl.borders = None
        lbl.name = 'lbl_prot_cancelamento'
        lbl.text = u'PROTOCOLO<br />DE CANCELAMENTO'
        lbl.top = 5.35*cm
        lbl.left = 5.2*cm
        lbl.width = 1.75*cm
        lbl.style = DESCRITIVO_CAMPO_CANCELAMENTO
        self.elements.insert(2, lbl)

        fld = Campo()
        fld.name = 'fld_prot_cancelamento'
        fld.attribute_name = u'procEventoCancNFe.retEvento.protocolo_formatado'
        fld.top  = 5.15*cm
        fld.left = 6.85*cm
        fld.width = 6.3*cm
        fld.padding_top = 0.25*cm
        fld.style = DADO_VARIAVEL_CANCELAMENTO
        self.elements.insert(3, fld)

    def obs_cancelamento_com_motivo(self):
        txt = Texto()
        txt.name   = 'txt_obs_cancelamento'
        txt.text   = u'cancelada'
        txt.top    = 3.5*cm
        txt.left   = 4.7*cm
        txt.width  = 10*cm
        txt.height = 1.5*cm
        txt.padding_top = 0.1*cm
        txt.style  = OBS_DENEGACAO
        self.elements.insert(0, txt)

        fld = Campo()
        fld.name = 'fld_motivo_cancelamento'
        fld.attribute_name = u'procCancNFe.cancNFe.infCanc.xJust'
        fld.top  = 5.15*cm
        fld.left = 4.7*cm
        fld.width = 10*cm
        fld.padding_top = 0.25*cm
        fld.style = DADO_VARIAVEL_CANCELAMENTO
        self.elements.insert(1, fld)

        lbl = LabelMargemEsquerda()
        lbl.borders = None
        lbl.name = 'lbl_prot_cancelamento'
        lbl.text = u'PROTOCOLO<br />DE CANCELAMENTO'
        lbl.top = 5.72*cm
        lbl.left = 6.15*cm
        lbl.width = 1.75*cm
        lbl.style = DESCRITIVO_CAMPO_CANCELAMENTO
        self.elements.insert(2, lbl)

        fld = Campo()
        fld.name = 'fld_prot_cancelamento'
        fld.attribute_name = u'retCancNFe.protocolo_formatado'
        fld.top  = 5.52*cm
        fld.left = 7.5*cm
        fld.width = 6.3*cm
        fld.padding_top = 0.25*cm
        fld.style = DADO_VARIAVEL_CANCELAMENTO
        self.elements.insert(3, fld)

    def obs_cancelamento_com_motivo_evento(self):
        txt = Texto()
        txt.name   = 'txt_obs_cancelamento'
        txt.text   = u'cancelada'
        txt.top    = 3.5*cm
        txt.left   = 4.7*cm
        txt.width  = 10*cm
        txt.height = 1.5*cm
        txt.padding_top = 0.1*cm
        txt.style  = OBS_DENEGACAO
        self.elements.insert(0, txt)

        fld = Campo()
        fld.name = 'fld_motivo_cancelamento'
        fld.attribute_name = u'procEventoCancNFe.evento.infEvento.detEvento.xJust'
        fld.top  = 5.15*cm
        fld.left = 4.7*cm
        fld.width = 10*cm
        fld.padding_top = 0.25*cm
        fld.style = DADO_VARIAVEL_CANCELAMENTO
        self.elements.insert(1, fld)

        lbl = LabelMargemEsquerda()
        lbl.borders = None
        lbl.name = 'lbl_prot_cancelamento'
        lbl.text = u'PROTOCOLO<br />DE CANCELAMENTO'
        lbl.top = 5.72*cm
        lbl.left = 5.2*cm
        lbl.width = 1.75*cm
        lbl.style = DESCRITIVO_CAMPO_CANCELAMENTO
        self.elements.insert(2, lbl)

        fld = Campo()
        fld.name = 'fld_prot_cancelamento'
        fld.attribute_name = u'procEventoCancNFe.retEvento.protocolo_formatado'
        fld.top  = 5.52*cm
        fld.left = 6.85*cm
        fld.width = 7.5*cm
        fld.padding_top = 0.25*cm
        fld.style = DADO_VARIAVEL_CANCELAMENTO
        self.elements.insert(3, fld)

    def obs_denegacao(self):
        txt = Texto()
        txt.name   = 'txt_obs_denegacao'
        txt.text   = u'denegada'
        #txt.top    = -0.1*cm
        txt.top    = 3.5*cm
        txt.left   = 4.7*cm
        txt.width  = 10*cm
        txt.height = 1.5*cm
        txt.padding_top = 0.1*cm
        txt.style  = OBS_DENEGACAO
        self.elements.insert(0, txt)

        fld = Campo()
        fld.name = 'fld_motivo_denegacao'
        fld.attribute_name = u'protNFe.infProt.xMotivo'
        fld.top  = 5.15*cm
        fld.left = 4.7*cm
        fld.width = 10*cm
        fld.padding_top = 0.25*cm
        fld.style = DADO_VARIAVEL_CANCELAMENTO
        self.elements.insert(1, fld)

        lbl = LabelMargemEsquerda()
        lbl.borders = None
        lbl.name = 'lbl_prot_denegacao'
        lbl.text = u'PROTOCOLO<br />DE DENEGAÇÃO'
        lbl.top = 5.72*cm
        lbl.left = 6.15*cm
        lbl.width = 1.75*cm
        lbl.style = DESCRITIVO_CAMPO_CANCELAMENTO
        self.elements.insert(2, lbl)

        fld = Campo()
        fld.name = 'fld_prot_denegacao'
        fld.attribute_name = u'protNFe.protocolo_formatado'
        fld.top  = 5.52*cm
        fld.left = 7.5*cm
        fld.width = 6.3*cm
        fld.padding_top = 0.25*cm
        fld.style = DADO_VARIAVEL_CANCELAMENTO
        self.elements.insert(3, fld)

    def obs_contingencia_normal_scan(self):
        lbl = Texto()
        lbl.name  = 'txt_obs_contingencia'
        lbl.text  = u'DANFE em contingência<br /><br />impresso em decorrência de problemas técnicos'
        lbl.top   = 6.6*cm
        lbl.left  = 0*cm
        lbl.width = 19.4*cm
        lbl.padding_top = 0.1*cm
        lbl.style = OBS_CONTINGENCIA
        self.elements.insert(0, lbl)

    def obs_contingencia_dpec(self):
        lbl = Texto()
        lbl.name  = 'txt_obs_contingencia'
        lbl.text  = u'DANFE em contingência<br /><br />DPEC regularmente recebida pela Receita Federal do Brasil'
        lbl.top   = 6.6*cm
        lbl.left  = 0*cm
        lbl.width = 19.4*cm
        lbl.padding_top = 0.1*cm
        lbl.style = OBS_CONTINGENCIA
        self.elements.insert(0, lbl)

    def obs_sem_valor_fiscal(self):
        lbl = Texto()
        lbl.name  = 'txt_obs_homologacao'
        lbl.text  = u'sem valor fiscal'
        lbl.top   = 9*cm
        lbl.left  = 0*cm
        lbl.width = 19.4*cm
        lbl.padding_top = 0.1*cm
        lbl.style = OBS_HOMOLOGACAO
        self.elements.append(lbl)

    def monta_quadro_emitente(self, dados_emitente=[]):
        for de in dados_emitente:
            self.elements.append(de)

    def dados_emitente_sem_logo(self):
        elements = []

        #
        # Dados do remetente
        #
        fld = Campo()
        fld.nome  = 'fld_rem_nome'
        fld.attribute_name = u'NFe.infNFe.emit.xNome.valor'
        fld.top   = 0.2*cm
        fld.width = 8*cm
        fld.height = 1.5*cm
        fld.style = EMIT_NOME
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_rem_endereco_1'
        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_1'
        fld.top   = 1.4*cm
        fld.width = 8*cm
        fld.height = 0.7*cm
        fld.style = EMIT_DADOS
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_rem_endereco_2'
        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_2'
        fld.top   = 2.2*cm
        fld.width = 8*cm
        fld.height = 0.7*cm
        fld.style = EMIT_DADOS
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_rem_endereco_3'
        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_3'
        fld.top   = 3*cm
        fld.width = 8*cm
        fld.height = 0.45*cm
        fld.style = EMIT_DADOS
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_rem_endereco_4'
        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_4'
        fld.top   = 3.4*cm
        fld.width = 8*cm
        fld.height = 0.45*cm
        fld.style = EMIT_DADOS
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_regime_tributario'
        fld.attribute_name = 'NFe.crt_descricao'
        fld.top   = 3.6*cm
        fld.width = 8*cm
        fld.height = 0.4*cm
        fld.style = DADO_PRODUTO_CENTRALIZADO
        elements.append(fld)

        return elements

    def dados_emitente_logo_vertical(self, arquivo_imagem):
        elements = []

        #
        # Dados do remetente
        #
        img = Image()
        img.top = 0.1*cm
        img.left = 0.1*cm
        #
        # Tamanhos equilaventes, em centímetros, a 2,5 x 3,8, em 128 dpi
        # estranhamente, colocar os tamanhos em centímetros encolhe a imagem
        #
        img.width = 116
        img.height = 191
        img.filename = arquivo_imagem
        elements.append(img)

        fld = Campo()
        fld.nome  = 'fld_rem_nome'
        fld.attribute_name = u'NFe.infNFe.emit.xNome.valor'
        fld.top   = 0.2*cm
        fld.left  = 2.5*cm
        fld.width = 5.5*cm
        fld.height = 1.5*cm
        fld.style = EMIT_NOME
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_rem_endereco_1'
        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_1'
        fld.top   = 1.4*cm
        fld.left  = 2.5*cm
        fld.width = 5.5*cm
        fld.height = 0.7*cm
        fld.style = EMIT_DADOS
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_rem_endereco_2'
        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_2'
        fld.top   = 2.2*cm
        fld.left  = 2.5*cm
        fld.width = 5.5*cm
        fld.height = 0.7*cm
        fld.style = EMIT_DADOS
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_rem_endereco_3'
        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_3'
        fld.top   = 3*cm
        fld.left  = 2.5*cm
        fld.width = 5.5*cm
        fld.height = 0.45*cm
        fld.style = EMIT_DADOS
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_rem_endereco_4'
        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_4'
        fld.top   = 3.4*cm
        fld.left  = 2.5*cm
        fld.width = 5.5*cm
        fld.height = 0.45*cm
        fld.style = EMIT_DADOS
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_regime_tributario'
        fld.attribute_name = 'NFe.crt_descricao'
        fld.top   = 3.6*cm
        fld.left  = 2.5*cm
        fld.width = 5.5*cm
        fld.height = 0.4*cm
        fld.style = DADO_PRODUTO_CENTRALIZADO
        elements.append(fld)

        return elements

    def dados_emitente_logo_horizontal(self, arquivo_imagem):
        elements = []

        #
        # Dados do remetente
        #
        img = Image()
        img.top = 0.1*cm
        img.left = 0.1*cm
        #
        # Tamanhos equilaventes, em centímetros, a 3,8 x 2,5, em 128 dpi
        # estranhamente, colocar os tamanhos em centímetros encolhe a imagem
        #
        img.width = 191
        img.height = 116
        img.filename = arquivo_imagem
        elements.append(img)

        fld = Campo()
        fld.nome  = 'fld_rem_nome'
        fld.attribute_name = u'NFe.infNFe.emit.xNome.valor'
        fld.top   = 0.2*cm
        fld.left  = 4*cm
        fld.width = 4*cm
        fld.height = 1.4*cm
        fld.style = EMIT_NOME
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_rem_endereco_3'
        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_3'
        fld.top   = 2.05*cm
        fld.left  = 4*cm
        fld.width = 4*cm
        fld.height = 0.45*cm
        fld.style = EMIT_DADOS
        elements.append(fld)

#        fld = Campo()
#        fld.nome  = 'fld_rem_endereco_4'
#        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_4'
#        fld.top   = 2.05*cm
#        fld.left  = 4*cm
#        fld.width = 4*cm
#        fld.height = 0.45*cm
#        fld.style = EMIT_DADOS
#        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_rem_endereco_1'
        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_1'
        fld.top   = 2.5*cm
        fld.left  = 0*cm
        fld.width = 8*cm
        fld.height = 0.7*cm
        fld.style = EMIT_DADOS
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_rem_endereco_2'
        fld.attribute_name = u'NFe.endereco_emitente_formatado_linha_2'
        fld.top   = 3.2*cm
        fld.left  = 0*cm
        fld.width = 8*cm
        fld.height = 0.7*cm
        fld.style = EMIT_DADOS
        elements.append(fld)

        fld = Campo()
        fld.nome  = 'fld_regime_tributario'
        fld.attribute_name = 'NFe.crt_descricao'
        fld.top   = 3.6*cm
        fld.left  = 0*cm
        fld.width = 8*cm
        fld.height = 0.4*cm
        fld.style = DADO_PRODUTO_CENTRALIZADO
        elements.append(fld)

        return elements


class DestinatarioRetrato(BandaDANFE):
    def __init__(self):
        super(DestinatarioRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='remetente', titulo=u'DESTINATÁRIO/REMETENTE', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        lbl, fld = self.inclui_campo(nome='remetente_nome', titulo=u'NOME/RAZÃO SOCIAL', conteudo=u'NFe.infNFe.dest.xNome.valor', top=0.42*cm, left=0*cm, width=13.95*cm)
        lbl, fld = self.inclui_campo(nome='remetente_cnpj', titulo=u'CNPJ/CPF', conteudo=u'NFe.cnpj_destinatario_formatado', top=0.42*cm, left=13.95*cm, width=3.26*cm, margem_direita=True)
        fld.style = DADO_CAMPO_NEGRITO
        lbl, fld = self.inclui_campo(nome='remetente_data_emissao', titulo=u'DATA DA EMISSÃO', conteudo=u'NFe.infNFe.ide.dEmi.formato_danfe', top=0.42*cm, left=17.2*cm, width=2.2*cm, margem_direita=True)
        fld.style = DADO_CAMPO_NEGRITO

        # 2ª linha
        lbl, fld = self.inclui_campo(nome='remetente_nome', titulo=u'ENDEREÇO', conteudo=u'NFe.endereco_destinatario_formatado', top=1.12*cm, left=0*cm, width=10.9*cm)
        lbl, fld = self.inclui_campo(nome='remetente_bairro', titulo=u'BAIRRO/DISTRITO', conteudo=u'NFe.infNFe.dest.enderDest.xBairro.valor', top=1.12*cm, left=10.9*cm, width=4.5*cm)
        lbl, fld = self.inclui_campo(nome='remetente_cep', titulo=u'CEP', conteudo=u'NFe.cep_destinatario_formatado', top=1.12*cm, left=15.4*cm, width=1.8*cm)
        lbl, fld = self.inclui_campo(nome='remetente_data_entradasaida', titulo=u'DATA DA ENTRADA/SAÍDA', conteudo=u'NFe.infNFe.ide.dSaiEnt.formato_danfe', top=1.12*cm, left=17.2*cm, width=2.2*cm, margem_direita=True)
        fld.style = DADO_CAMPO_NEGRITO

        ## 3ª linha
        lbl, fld = self.inclui_campo(nome='remetente_municipio', titulo=u'MUNICÍPIO', conteudo=u'NFe.infNFe.dest.enderDest.xMun.valor', top=1.82*cm, left=0*cm, width=9.9*cm)
        lbl, fld = self.inclui_campo(nome='remetente_fone', titulo=u'FONE', conteudo=u'NFe.fone_destinatario_formatado', top=1.82*cm, left=9.9*cm, width=3.3*cm)
        lbl, fld = self.inclui_campo(nome='remetente_uf', titulo=u'UF', conteudo='NFe.infNFe.dest.enderDest.UF.valor', top=1.82*cm, left=13.2*cm, width=0.75*cm)
        lbl, fld = self.inclui_campo(nome='remetente_ie', titulo=u'INSCRIÇÃO ESTADUAL', conteudo=u'NFe.infNFe.dest.IE.valor', top=1.82*cm, left=13.95*cm, width=3.25*cm)
        lbl, fld = self.inclui_campo(nome='remetente_hora_entradasaida', titulo=u'HORA DA ENTRADA/SAÍDA', conteudo=u'NFe.infNFe.ide.hSaiEnt.formato_danfe', top=1.82*cm, left=17.2*cm, width=2.2*cm, margem_direita=True)
        fld.style = DADO_CAMPO_NEGRITO

        self.height = 2.52*cm


class LocalRetiradaRetrato(BandaDANFE):
    def __init__(self):
        super(LocalRetiradaRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='locret', titulo=u'LOCAL DE RETIRADA', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        self.inclui_campo(nome='locret_cnpj', titulo=u'CNPJ/CPF', conteudo=u'NFe.cnpj_retirada_formatado', top=0.42*cm, left=0*cm, width=3.2*cm)
        self.inclui_campo(nome='locret_endereco', titulo=u'ENDEREÇO', conteudo=u'NFe.endereco_retirada_formatado', top=0.42*cm, left=3.2*cm, width=16.2*cm, margem_direita=True)

        self.height = 1.12*cm


class LocalEntregaRetrato(BandaDANFE):
    def __init__(self):
        super(LocalEntregaRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='locent', titulo=u'LOCAL DE ENTREGA', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        self.inclui_campo(nome='locent_cnpj', titulo=u'CNPJ/CPF', conteudo=u'NFe.cnpj_entrega_formatado', top=0.42*cm, left=0*cm, width=3.2*cm)
        self.inclui_campo(nome='locent_endereco', titulo=u'ENDEREÇO', conteudo=u'NFe.endereco_entrega_formatado', top=0.42*cm, left=3.2*cm, width=16.2*cm, margem_direita=True)

        self.height = 1.12*cm


class FaturaAVistaRetrato(BandaDANFE):
    def __init__(self):
        super(FaturaAVistaRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='fat', titulo=u'FATURA', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        lbl, txt = self.inclui_texto(nome='fat_texto', titulo='', texto=u'PAGAMENTO À VISTA', top=0.42*cm, left=0*cm, width=19.4*cm)
        lbl.borders['right'] = False

        lbl, fld = self.inclui_campo(nome='fat_numero', titulo=u'NÚMERO DA FATURA', conteudo=u'NFe.infNFe.cobr.fat.nFat.valor', top=0.42*cm, left=3.7*cm, width=9.7*cm)
        lbl, fld = self.inclui_campo_numerico(nome='fat_vorig', titulo=u'VALOR ORIGINAL', conteudo=u'NFe.infNFe.cobr.fat.vOrig.formato_danfe', top=0.42*cm, left=13.4*cm, width=2*cm)
        lbl, fld = self.inclui_campo_numerico(nome='fat_vorig', titulo=u'DESCONTO', conteudo=u'NFe.infNFe.cobr.fat.vDesc.formato_danfe', top=0.42*cm, left=15.4*cm, width=2*cm)
        lbl, fld = self.inclui_campo_numerico(nome='fat_vorig', titulo=u'VALOR LÍQUIDO', conteudo=u'NFe.infNFe.cobr.fat.vLiq.formato_danfe', top=0.42*cm, left=17.4*cm, width=2*cm, margem_direita=True)

        self.height = 1.12*cm

class FaturaAPrazoRetrato(BandaDANFE):
    def __init__(self):
        super(FaturaAPrazoRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='fat', titulo=u'FATURA', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        lbl, txt = self.inclui_texto(nome='fat_texto', titulo='', texto=u'PAGAMENTO A PRAZO', top=0.42*cm, left=0*cm, width=19.4*cm)
        lbl.borders['right'] = False

        lbl, fld = self.inclui_campo(nome='fat_numero', titulo=u'NÚMERO DA FATURA', conteudo=u'NFe.infNFe.cobr.fat.nFat.valor', top=0.42*cm, left=3.7*cm, width=9.7*cm)
        lbl, fld = self.inclui_campo_numerico(nome='fat_vorig', titulo=u'VALOR ORIGINAL', conteudo=u'NFe.infNFe.cobr.fat.vOrig.formato_danfe', top=0.42*cm, left=13.4*cm, width=2*cm)
        lbl, fld = self.inclui_campo_numerico(nome='fat_vorig', titulo=u'DESCONTO', conteudo=u'NFe.infNFe.cobr.fat.vDesc.formato_danfe', top=0.42*cm, left=15.4*cm, width=2*cm)
        lbl, fld = self.inclui_campo_numerico(nome='fat_vorig', titulo=u'VALOR LÍQUIDO', conteudo=u'NFe.infNFe.cobr.fat.vLiq.formato_danfe', top=0.42*cm, left=17.4*cm, width=2*cm, margem_direita=True)

        self.height = 1.12*cm


class DuplicatasRetrato(SubReport):
    def __init__(self):
        super(DuplicatasRetrato, self).__init__()
        self.get_queryset = lambda self, parent_object: parent_object.NFe.infNFe.cobr.dup or []

    class band_header(BandaDANFE):
        def __init__(self):
            super(DuplicatasRetrato.band_header, self).__init__()
            self.elements = []
            self.inclui_descritivo(nome='dup', titulo=u'DUPLICATAS', top=1.12*cm, left=0*cm, width=19.4*cm)
            self.height = 0.42*cm

    class band_detail(BandaDANFE):
        def __init__(self):
            super(DuplicatasRetrato.band_detail, self).__init__()
            self.width = 6.4*cm
            self.display_inline = True
            self.margin_right = 0.08*cm

            self.elements = []
            lbl, fld = self.inclui_campo(nome='dup_numero', titulo=u'NÚMERO', conteudo=u'nDup.valor', top=1.12*cm, left=0*cm, width=2.8*cm)
            lbl, fld = self.inclui_campo(nome='dup_venc'  , titulo=u'VENCIMENTO', conteudo=u'dVenc.formato_danfe', top=1.12*cm, left=2.8*cm, width=1.9*cm)
            lbl, fld = self.inclui_campo_numerico(nome='dup_valor', titulo=u'VALOR', conteudo=u'vDup.formato_danfe', top=1.12*cm, left=4.7*cm, width=1.7*cm, margem_direita=True)

            self.height = fld.height


class CalculoImpostoRetrato(BandaDANFE):
    def __init__(self):
        super(CalculoImpostoRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='clc', titulo=u'CÁLCULO DO IMPOSTO', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        lbl, fld = self.inclui_campo_numerico(nome='clc_bip', titulo=u'BASE DE CÁLCULO DO ICMS', conteudo=u'NFe.infNFe.total.ICMSTot.vBC.formato_danfe', top=0.42*cm, left=0*cm, width=3.88*cm)
        lbl, fld = self.inclui_campo_numerico(nome='clc_vip', titulo=u'VALOR DO ICMS', conteudo=u'NFe.infNFe.total.ICMSTot.vICMS.formato_danfe', top=0.42*cm, left=3.88*cm, width=3.88*cm)
        lbl, fld = self.inclui_campo_numerico(nome='clc_bis', titulo=u'BASE DE CÁLCULO DO ICMS ST', conteudo=u'NFe.infNFe.total.ICMSTot.vBCST.formato_danfe', top=0.42*cm, left=7.76*cm, width=3.88*cm)
        lbl, fld = self.inclui_campo_numerico(nome='clc_vis', titulo=u'VALOR DO ICMS ST', conteudo=u'NFe.infNFe.total.ICMSTot.vST.formato_danfe', top=0.42*cm, left=11.64*cm, width=3.88*cm)
        lbl, fld = self.inclui_campo_numerico(nome='clc_vpn', titulo=u'VALOR TOTAL DOS PRODUTOS', conteudo=u'NFe.infNFe.total.ICMSTot.vProd.formato_danfe', top=0.42*cm, left=15.52*cm, width=3.88*cm, margem_direita=True)
        #fld.style = DADO_CAMPO_NUMERICO_NEGRITO

        # 2ª linha
        lbl, fld = self.inclui_campo_numerico(nome='clc_vfrete', titulo=u'VALOR DO FRETE', conteudo=u'NFe.infNFe.total.ICMSTot.vFrete.formato_danfe', top=1.12*cm, left=0*cm, width=3.104*cm)
        lbl, fld = self.inclui_campo_numerico(nome='clc_vseguro', titulo=u'VALOR DO SEGURO', conteudo=u'NFe.infNFe.total.ICMSTot.vSeg.formato_danfe', top=1.12*cm, left=3.104*cm, width=3.104*cm)
        lbl, fld = self.inclui_campo_numerico(nome='clc_vdesconto', titulo=u'DESCONTO', conteudo=u'NFe.infNFe.total.ICMSTot.vDesc.formato_danfe', top=1.12*cm, left=6.208*cm, width=3.104*cm)
        lbl, fld = self.inclui_campo_numerico(nome='clc_voutras', titulo=u'OUTRAS DESPESAS ACESSÓRIAS', conteudo=u'NFe.infNFe.total.ICMSTot.vOutro.formato_danfe', top=1.12*cm, left=9.312*cm, width=3.104*cm)
        lbl, fld = self.inclui_campo_numerico(nome='clc_vipi', titulo=u'VALOR TOTAL DO IPI', conteudo=u'NFe.infNFe.total.ICMSTot.vIPI.formato_danfe', top=1.12*cm, left=12.416*cm, width=3.104*cm)

        # Fundo destacado do total da NF
        self.elements.append(Rect(top=1.12*cm, left=15.52*cm, height=0.7*cm, width=3.88*cm, stroke=False, stroke_width=0, fill=True, fill_color=HexColor(0xd0d0d0)))
        lbl, fld = self.inclui_campo_numerico(nome='clc_vnf', titulo=u'VALOR TOTAL DA NOTA', conteudo=u'NFe.infNFe.total.ICMSTot.vNF.formato_danfe', top=1.12*cm, left=15.52*cm, width=3.88*cm, margem_direita=True)
        lbl.style = DESCRITIVO_CAMPO_NEGRITO
        fld.style = DADO_CAMPO_NUMERICO_NEGRITO

        self.height = 1.82*cm


class TransporteRetrato(BandaDANFE):
    def __init__(self):
        super(TransporteRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='clc', titulo=u'TRANSPORTADOR/VOLUMES TRANSPORTADOS', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        lbl, fld = self.inclui_campo(nome='trn_nome', titulo=u'NOME/RAZÃO SOCIAL', conteudo='NFe.infNFe.transp.transporta.xNome.valor', top=0.42*cm, left=0*cm, width=9.55*cm)
        lbl, fld = self.inclui_campo(nome='trn_frete', titulo=u'FRETE POR CONTA', conteudo='NFe.frete_formatado', top=0.42*cm, left=9.55*cm, width=2.8*cm)
        lbl, fld = self.inclui_campo(nome='trn_antt', titulo=u'CÓDIGO ANTT', conteudo='NFe.infNFe.transp.veicTransp.RNTC.valor', top=0.42*cm, left=12.35*cm, width=1.4*cm)
        lbl, fld = self.inclui_campo(nome='trn_placa', titulo=u'PLACA DO VEÍCULO', conteudo=u'NFe.placa_veiculo_formatada', top=0.42*cm, left=13.75*cm, width=1.85*cm)
        lbl, fld = self.inclui_campo(nome='trn_vei_uf', titulo=u'UF', conteudo='NFe.infNFe.transp.veicTransp.UF.valor', top=0.42*cm, left=15.6*cm, width=0.6*cm)
        lbl, fld = self.inclui_campo(nome='trn_cnpj', titulo=u'CNPJ/CPF', conteudo=u'NFe.cnpj_transportadora_formatado', top=0.42*cm, left=16.2*cm, width=3.1*cm, margem_direita=True)

        # 2ª linha
        lbl, fld = self.inclui_campo(nome='trn_end', titulo=u'ENDEREÇO', conteudo='NFe.infNFe.transp.transporta.xEnder.valor', top=1.12*cm, left=0*cm, width=9.75*cm)
        lbl, fld = self.inclui_campo(nome='trn_mun', titulo=u'MUNICÍPIO', conteudo='NFe.infNFe.transp.transporta.xMun.valor', top=1.12*cm, left=9.75*cm, width=5.85*cm)
        lbl, fld = self.inclui_campo(nome='trn_uf', titulo=u'UF', conteudo='NFe.infNFe.transp.transporta.UF.valor', top=1.12*cm, left=15.6*cm, width=0.6*cm)
        lbl, fld = self.inclui_campo(nome='trn_ie', titulo=u'INSCRIÇÃO ESTADUAL', conteudo=u'NFe.infNFe.transp.transporta.IE.valor', top=1.12*cm, left=16.2*cm, width=3.1*cm, margem_direita=True)

        # 3ª linha
        self.elements.append(VolumesRetrato())

        #self.height = (2.52*cm) - fld.height
        self.height = 1.82*cm


class VolumesRetrato(SubReport):
    def __init__(self):
        super(VolumesRetrato, self).__init__()
        self.get_queryset = lambda self, parent_object: parent_object.NFe.infNFe.transp.vol or [Vol_200()]

    class band_detail(BandaDANFE):
        def __init__(self):
            super(VolumesRetrato.band_detail, self).__init__()
            self.elements = []
            lbl, fld = self.inclui_campo_numerico(nome='vol_qtd', titulo=u'QUANTIDADE', conteudo=u'qVol.formato_danfe', top=1.82*cm, left=0*cm, width=3.2*cm)
            lbl, fld = self.inclui_campo(nome='vol_esp', titulo=u'ESPÉCIE', conteudo=u'esp.valor', top=1.82*cm, left=3.2*cm, width=3.2*cm)
            lbl, fld = self.inclui_campo(nome='vol_marca', titulo=u'MARCA', conteudo=u'marca.valor', top=1.82*cm, left=6.4*cm, width=3.4*cm)
            lbl, fld = self.inclui_campo(nome='vol_numero', titulo=u'NÚMERO', conteudo=u'nVol.valor', top=1.82*cm, left=9.8*cm, width=3.2*cm)
            lbl, fld = self.inclui_campo_numerico(nome='vol_peso_bruto', titulo=u'PESO BRUTO', conteudo=u'pesoB.formato_danfe', top=1.82*cm, left=13*cm, width=3.2*cm)
            lbl, fld = self.inclui_campo_numerico(nome='vol_peso_liquido', titulo=u'PESO LÍQUIDO', conteudo=u'pesoL.formato_danfe', top=1.82*cm, left=16.2*cm, width=3.2*cm, margem_direita=True)

            self.height = fld.height


class CabProdutoRetrato(BandaDANFE):
    def __init__(self):
        super(CabProdutoRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='cabprod', titulo=u'DADOS DOS PRODUTOS/SERVIÇOS', top=0*cm, left=0*cm, width=19.4*cm)

        lbl = self.inclui_descritivo_produto(nome='', titulo='CÓDIGO DO PRODUTO', top=0.42*cm, left=0*cm, width=1.8*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='DESCRIÇÃO DO PRODUTO/SERVIÇO', top=0.42*cm, left=1.8*cm, width=5.1*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='NCM/SH', top=0.42*cm, left=6.9*cm, width=1*cm)
        lbl.padding_top = 0.15*cm

        #lbl = self.inclui_descritivo_produto(nome='', titulo='CST', top=0.42*cm, left=8.75*cm, width=0.55*cm)
        #lbl.padding_top = 0.15*cm

        fld = self.inclui_campo_sem_borda(nome='cst_descricao', conteudo=u'NFe.cst_descricao', top=0.42*cm, left=7.9*cm, width=0.6*cm)
        fld.style = DESCRITIVO_PRODUTO
        fld.padding_top = 0.15*cm
        fld.padding_left = 0.05*cm
        fld.padding_bottom = 0.05*cm
        fld.padding_right = 0.05*cm
        fld.borders = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': False}
        fld.height = 0.52*cm

        lbl = self.inclui_descritivo_produto(nome='', titulo='CFOP', top=0.42*cm, left=8.5*cm, width=0.54*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='UNIDADE', top=0.42*cm, left=9.04*cm, width=0.9*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='QUANTIDADE', top=0.42*cm, left=9.94*cm, width=1.4*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR UNITÁRIO', top=0.42*cm, left=11.34*cm, width=2*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR TOTAL', top=0.42*cm, left=13.34*cm, width=1.2*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='BASE CÁLC. DO ICMS', top=0.42*cm, left=14.54*cm, width=1.2*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR DO ICMS', top=0.42*cm, left=15.74*cm, width=1.05*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR DO IPI', top=0.42*cm, left=16.79*cm, width=1.05*cm)
        #lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='ALÍQUOTAS', top=0.42*cm, left=17.84*cm, width=1.36*cm, height=0.26*cm, margem_direita=True)
        lbl = self.inclui_descritivo_produto(nome='', titulo='ICMS', top=0.68*cm, left=17.84*cm, width=0.78*cm, height=0.26*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='IPI', top=0.68*cm, left=18.62*cm, width=0.78*cm, height=0.26*cm, margem_direita=True)

        self.height = 0.94*cm


class DetProdutoRetrato(BandaDANFE):
    def __init__(self):
        super(DetProdutoRetrato, self).__init__()
        self.elements = []

        #
        # Modelagem do tamanho dos campos
        #
        #txt = self.inclui_texto_produto(nome='', texto='MMMMMMMMMMMMMM', top=0*cm, left=0*cm, width=2.6*cm)
        #txt = self.inclui_texto_centralizado_produto(nome='', texto='999999999', top=0*cm, left=2.6*cm, width=1*cm)
        #txt = self.inclui_texto_produto(nome='', texto='ISTO É UM TESTE', top=0*cm, left=3.6*cm, width=5.26*cm)
        #txt = self.inclui_texto_centralizado_produto(nome='', texto='999', top=0*cm, left=8.86*cm, width=0.44*cm)
        #txt = self.inclui_texto_centralizado_produto(nome='', texto='9999', top=0*cm, left=9.3*cm, width=0.54*cm)
        #txt = self.inclui_texto_centralizado_produto(nome='', texto='MMMMMM', top=0*cm, left=9.84*cm, width=1.1*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,9999', top=0*cm, left=10.94*cm, width=1.4*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,9999999999', top=0*cm, left=12.34*cm, width=2*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=13.74*cm, width=1.2*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=14.94*cm, width=1.2*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='999.999,99', top=0*cm, left=16.14*cm, width=1.05*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='999.999,99', top=0*cm, left=17.19*cm, width=1.05*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='99,99', top=0*cm, left=18.24*cm, width=0.58*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='99,99', top=0*cm, left=18.82*cm, width=0.58*cm, margem_direita=True)

        self.inclui_campo_produto(nome=u'prod_codigo', conteudo=u'prod.cProd.valor', top=0*cm, left=0*cm, width=1.8*cm)
        self.inclui_campo_produto(nome=u'prod_descricaco', conteudo=u'descricao_produto_formatada', top=0*cm, left=1.8*cm, width=5.1*cm)
        self.inclui_campo_centralizado_produto(nome=u'prod_ncm', conteudo=u'prod.NCM.valor', top=0*cm, left=6.9*cm, width=1*cm)
        self.inclui_campo_centralizado_produto(nome='prod_cst', conteudo='cst_formatado', top=0*cm, left=7.9*cm, width=0.6*cm)
        self.inclui_campo_centralizado_produto(nome=u'prod_cfop', conteudo=u'prod.CFOP.valor', top=0*cm, left=8.5*cm, width=0.54*cm)
        self.inclui_campo_centralizado_produto(nome=u'prod_unidade', conteudo=u'prod.uCom.valor', top=0*cm, left=9.04*cm, width=0.9*cm)
        self.inclui_campo_numerico_produto(nome='prod_quantidade', conteudo=u'prod.qCom.formato_danfe', top=0*cm, left=9.94*cm, width=1.4*cm)
        self.inclui_campo_numerico_produto(nome='vr_unitario', conteudo=u'prod.vUnCom.formato_danfe', top=0*cm, left=11.34*cm, width=2*cm)
        self.inclui_campo_numerico_produto(nome='', conteudo='prod.vProd.formato_danfe', top=0*cm, left=13.34*cm, width=1.2*cm)
        self.inclui_campo_numerico_produto(nome='', conteudo='imposto.ICMS.vBC.formato_danfe', top=0*cm, left=14.54*cm, width=1.2*cm)
        self.inclui_campo_numerico_produto(nome='', conteudo='imposto.ICMS.vICMS.formato_danfe', top=0*cm, left=15.74*cm, width=1.05*cm)
        self.inclui_campo_numerico_produto(nome='', conteudo='imposto.IPI.vIPI.formato_danfe', top=0*cm, left=16.79*cm, width=1.05*cm)
        self.inclui_campo_numerico_produto(nome='', conteudo='imposto.ICMS.pICMS.formato_danfe', top=0*cm, left=17.84*cm, width=0.78*cm)
        self.inclui_campo_numerico_produto(nome='', conteudo='imposto.IPI.pIPI.formato_danfe', top=0*cm, left=18.62*cm, width=0.78*cm, margem_direita=True)

        #self.height = 0.28*cm
        self.auto_expand_height = True


class ISSRetrato(BandaDANFE):
    def __init__(self):
        super(ISSRetrato, self).__init__()
        self.elements = []

        # Cálculo do ISS
        self.inclui_descritivo(nome='iss', titulo=u'CÁLCULO DO ISSQN', top=0*cm, left=0*cm, width=19.4*cm)
        lbl, fld = self.inclui_campo(nome='iss_im', titulo=u'INSCRIÇÃO MUNICIPAL', conteudo=u'NFe.infNFe.emit.IM.valor', top=0.42*cm, left=0*cm, width=4.85*cm)
        lbl, fld = self.inclui_campo_numerico(nome='iss_vr_servico', titulo=u'VALOR TOTAL DOS SERVIÇOS', conteudo=u'NFe.infNFe.total.ISSQNTot.vServ.formato_danfe', top=0.42*cm, left=4.85*cm, width=4.85*cm)
        lbl, fld = self.inclui_campo_numerico(nome='iss_bc', titulo=u'BASE DE CÁLCULO DO ISSQN', conteudo=u'NFe.infNFe.total.ISSQNTot.vBC.formato_danfe', top=0.42*cm, left=9.7*cm, width=4.85*cm)
        lbl, fld = self.inclui_campo_numerico(nome='iss_vr_iss', titulo=u'VALOR DO ISSQN', conteudo=u'NFe.infNFe.total.ISSQNTot.vISS.formato_danfe', top=0.42*cm, left=14.55*cm, width=4.85*cm, margem_direita=True)

        # Dados adicionais
        self.inclui_descritivo(nome='clc', titulo=u'DADOS ADICIONAIS', top=1.12*cm, left=0*cm, width=19.4*cm)
        lbl, txt = self.inclui_campo(nome='', titulo='INFORMAÇÕES COMPLEMENTARES', conteudo='NFe.dados_adicionais', top=1.54*cm, left=0*cm, width=11.7*cm, height=4*cm)
        txt.style = DADO_COMPLEMENTAR
        self.inclui_texto(nome='', titulo='RESERVADO AO FISCO', texto='', top=1.54*cm, left=11.7*cm, width=7.7*cm, height=4*cm, margem_direita=True)

        fld = DANFERetrato.ObsImpressao()
        fld.top = 5.54*cm
        self.elements.append(fld)

        self.height = 5.54*cm


class DadosAdicionaisRetrato(BandaDANFE):
    def __init__(self):
        super(DadosAdicionaisRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='clc', titulo=u'DADOS ADICIONAIS', top=0*cm, left=0*cm, width=19.4*cm)

        lbl, txt = self.inclui_campo(nome='', titulo='INFORMAÇÕES COMPLEMENTARES', conteudo='NFe.dados_adicionais', top=0.42*cm, left=0*cm, width=11.7*cm, height=4*cm)
        txt.style = DADO_COMPLEMENTAR
        self.inclui_texto(nome='', titulo='RESERVADO AO FISCO', texto='', top=0.42*cm, left=11.7*cm, width=7.7*cm, height=4*cm, margem_direita=True)

        fld = DANFERetrato.ObsImpressao()
        fld.top = 4.42*cm
        self.elements.append(fld)

        self.height = 4.42*cm
        #self.height = 4.62*cm


class RodapeFinalRetrato(BandaDANFE):
    def __init__(self):
        super(RodapeFinalRetrato, self).__init__()
        self.elements = []
        self.height = 0.1*cm

        # Obs de impressão
        fld = DANFERetrato.ObsImpressao()
        fld.top = 0.1*cm
        self.elements.append(fld)
