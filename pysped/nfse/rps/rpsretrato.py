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

from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor

from geraldo import Report, ReportBand, SubReport
from geraldo import ObjectValue, SystemField, Label, Line, Rect, Image
from geraldo.barcodes import BarCode
from geraldo.generators import PDFGenerator

from pysped.relato_sped.base_rps import *


class RPSRetrato(Report):
    def __init__(self, *args, **kargs):
        super(RPSRetrato, self).__init__(*args, **kargs)
        self.title = 'RPS - Recibo Provisório de Serviços'
        self.print_if_empty = True
        self.additional_fonts = FONTES_ADICIONAIS

        self.page_size = RETRATO
        self.margin_top = MARGEM_SUPERIOR
        self.margin_bottom = MARGEM_INFERIOR
        self.margin_left = MARGEM_ESQUERDA
        self.margin_right = MARGEM_DIREITA

        # Bandas e observações
        self.cabecalho         = CabecalhoRetrato()
        self.prestador         = PrestadorRetrato()
        self.tomador           = TomadorRetrato()
        self.discriminacao     = DiscriminacaoRetrato()
        self.detalhe_item      = DetItemRetrato()
        self.rodape            = RodapeRetrato()

    #def on_new_page(self, page, page_number, generator):
        #if generator._current_page_number <> 1:
            #self.band_page_footer = self.rodape_final

            #self.band_page_header = self.remetente
            #self.band_page_header.child_bands = []
            #self.band_page_header.child_bands.append(self.cab_item)

    def format_date(self, data, formato):
        return  data.strftime(formato.encode('utf-8')).decode('utf-8')

    class ObsImpressao(SystemField):
        name = 'obs_impressao'
        expression = 'RPS gerado em %(now:%d/%m/%Y, %H:%M:%S)s'
        top = 0*cm
        left = 0.1*cm
        width = 19.4*cm
        height = 0.2*cm
        style = DADO_PRODUTO
        borders = {'bottom': 0.1}


class CabecalhoRetrato(BandaRPS):
    def __init__(self):
        super(CabecalhoRetrato, self).__init__()
        self.elements = []

        # Quadro do emitente
        self.inclui_texto(nome='quadro_emitente', titulo='', texto='', top=0*cm, left=0*cm, width=15.4*cm, height=2.3*cm)

        #
        # Área central - Dados do DANFE
        #
        txt = self.inclui_texto_sem_borda(nome='prefeitura', texto='Prefeitura de Sorocaba', top=0*cm, left=3*cm, width=12.4*cm, height=0.5*cm)
        txt.style = DESCRITIVO_DANFE

        txt = self.inclui_texto_sem_borda(nome='secretaria', texto='Secretaria de Finanças', top=0.75*cm, left=3*cm, width=12.4*cm, height=0.5*cm)
        txt.style = DESCRITIVO_DANFE

        txt = self.inclui_texto_sem_borda(nome='rps', texto='RECIBO PROVISÓRIO DE SERVIÇOS - RPS', top=1.5*cm, left=3*cm, width=12.4*cm, height=0.5*cm)
        txt.style = DESCRITIVO_DANFE

        lbl, fld = self.inclui_campo_numerico(nome='numero_rps', titulo='Número do RPS', conteudo='RPS.numero_formatado', top=0*cm, left=15.4*cm, width=4*cm, height=(2.3/2)*cm, margem_direita=True)

        lbl, fld = self.inclui_campo(nome='data_rps', titulo='Data de Emissão do RPS', conteudo='RPS.DataEmissaoRPS.valor', top=(2.3/2)*cm, left=15.4*cm, width=4*cm, height=(2.3/2)*cm, margem_direita=True)

        #
        # Dados do remetente
        #
        img = Image()
        img.top = 5
        img.left = 9
        #
        # Tamanhos equilaventes, em centímetros, a 3,0 x 2,2, em 128 dpi
        # estranhamente, colocar os tamanhos em centímetros encolhe a imagem
        #
        img.width = 133
        img.height = 98
        img.filename = 'logotipo_prefeitura/sp-sorocaba.jpeg'
        self.elements.append(img)


        #txt = self.inclui_texto_sem_borda(nome='danfe_ext', texto=u'DOCUMENTO AUXILIAR DA NOTA FISCAL ELETRÔNICA', top=0.6*cm, left=8*cm, width=3.4*cm, *cm)height=4*cm)
        #txt.style = DESCRITIVO_DANFE_GERAL

        #txt = self.inclui_texto_sem_borda(nome='danfe_entrada', texto=u'0 - ENTRADA', top=1.45*cm, left=8.3*cm, width=3.4*cm, height=4*cm)
        #txt.style = DESCRITIVO_DANFE_ES

        #txt = self.inclui_texto_sem_borda(nome='danfe_saida', texto=u'1 - SAÍDA', top=1.85*cm, left=8.3*cm, width=3.4*cm, height=4*cm)
        #txt.style = DESCRITIVO_DANFE_ES

        #fld = self.inclui_campo_sem_borda(nome='danfe_entrada_saida', conteudo=u'NFe.infNFe.ide.tpNF.valor', top=1.6*cm, left=10.4*cm, width=0.6*cm, height=0.6*cm)
        #fld.style = DESCRITIVO_NUMERO
        #fld.borders = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': 0.1}
        #fld.padding_bottom = 0.2*cm

        #fld = self.inclui_campo_sem_borda(nome='danfe_numero', conteudo=u'NFe.numero_formatado', top=2.4*cm, left=8*cm, width=3.4*cm, height=0.5*cm)
        #fld.style = DESCRITIVO_NUMERO

        #fld = self.inclui_campo_sem_borda(nome='danfe_serie', conteudo=u'NFe.serie_formatada', top=2.85*cm, left=8*cm, width=3.4*cm, height=0.5*cm)
        #fld.style = DESCRITIVO_NUMERO

        #fld = SystemField(name='fld_danfe_folha', expression=u'FOLHA %(page_number)02d/%(page_count)02d', top=3.3*cm, left=8*cm, width=3.4*cm, height=0.5*cm)
        #fld.padding_top = 0.1*cm
        #fld.style = DESCRITIVO_NUMERO
        #self.elements.append(fld)

        ##
        ## No caso dos códigos de barra, altura (height) e largura (width) se referem às barras, não à imagem
        ##
        #self.elements.append(Line(top=0*cm, bottom=0*cm, left=11.4*cm, right=19.4*cm, stroke_width=0.1))
        #self.elements.append(BarCode(type=u'Code128', attribute_name=u'NFe.chave_para_codigo_barras', top=((1.625-0.8)/2.0)*cm, left=11.3*cm, width=0.025*cm, height=0.8*cm))

        #lbl, fld = self.inclui_campo(nome='remetente_chave', titulo=u'CHAVE DE ACESSO', conteudo=u'NFe.chave_formatada', top=1.625*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        #fld.style = DADO_CHAVE

        #self.inclui_campo(nome='remetente_natureza', titulo=u'NATUREZA DA OPERAÇÃO', conteudo=u'NFe.infNFe.ide.natOp.valor', top=4*cm, left=0*cm, width=11.4*cm)

        #self.inclui_campo(nome='remetente_ie', titulo=u'INSCRIÇÃO ESTADUAL', conteudo=u'NFe.infNFe.emit.IE.valor', top=4.70*cm, left=0*cm, width=6.4*cm)
        #self.inclui_campo(nome='remetente_iest', titulo=u'INSCRIÇÃO ESTADUAL DO SUBSTITUTO TRIBUTÁRIO', conteudo=u'NFe.infNFe.emit.IEST.valor', top=4.70*cm, left=6.4*cm, width=6.6*cm)
        #self.inclui_campo(nome='remetente_cnpj', titulo=u'CNPJ', conteudo=u'NFe.cnpj_emitente_formatado', top=4.70*cm, left=13*cm, width=6.4*cm, margem_direita=True)

        self.height = 2.3*cm

class PrestadorRetrato(BandaRPS):
    def __init__(self):
        super(PrestadorRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='titulo_prestador', titulo='PRESTADOR DE SERVIÇOS', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        lbl = Titulo(text='Razão Social/Nome:', top=0.42*cm, left=0*cm, width=2.8*cm)
        self.elements.append(lbl)
        fld = Campo(attribute_name='RPS.prestador.nome', top=0.42*cm, left=2.6*cm, width=16.8*cm)
        self.elements.append(fld)

        # 2ª linha
        lbl = Titulo(text='CNPJ/CPF:', top=0.84*cm, left=0*cm, width=1.4*cm)
        self.elements.append(lbl)
        fld = Campo(attribute_name='RPS.prestador.cnpj', top=0.84*cm, left=1.4*cm, width=18*cm)
        self.elements.append(fld)

        lbl = Titulo(text='Inscrição mobiliária:', top=0.84*cm, left=8*cm, width=3.4*cm)
        self.elements.append(lbl)
        fld = Campo(attribute_name='RPS.prestador.im', top=0.84*cm, left=10.7*cm, width=18*cm)
        self.elements.append(fld)

        # 3ª linha
        lbl = Titulo(text='Endereço:', top=1.26*cm, left=0*cm, width=1.4*cm)
        self.elements.append(lbl)
        fld = Campo(attribute_name='RPS.prestador.endereco', top=1.26*cm, left=1.4*cm, width=18*cm)
        self.elements.append(fld)

        # 4ª linha
        lbl = Titulo(text='Município:', top=1.68*cm, left=0*cm, width=1.4*cm)
        self.elements.append(lbl)
        fld = Campo(attribute_name='RPS.prestador.cidade', top=1.68*cm, left=1.4*cm, width=18*cm)
        self.elements.append(fld)

        self.elements.append(Line(top=2.1*cm, bottom=2.1*cm, left=0*cm, right=19.4*cm, stroke_width=0.1))

        self.height = 2.1*cm


class TomadorRetrato(BandaRPS):
    def __init__(self):
        super(TomadorRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='titulo_tomador', titulo='TOMADOR DE SERVIÇOS', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        lbl = Titulo(text='Razão Social/Nome:', top=0.42*cm, left=0*cm, width=2.8*cm)
        self.elements.append(lbl)
        fld = Campo(attribute_name='RPS.RazaoSocialTomador.valor', top=0.42*cm, left=2.6*cm, width=16.8*cm)
        self.elements.append(fld)

        # 2ª linha
        lbl = Titulo(text='CNPJ/CPF:', top=0.84*cm, left=0*cm, width=1.4*cm)
        self.elements.append(lbl)
        fld = Campo(attribute_name='RPS.cnpj_tomador_formatado', top=0.84*cm, left=1.4*cm, width=18*cm)
        self.elements.append(fld)

        # 3ª linha
        lbl = Titulo(text='Endereço:', top=1.26*cm, left=0*cm, width=1.4*cm)
        self.elements.append(lbl)
        fld = Campo(attribute_name='RPS.endereco_tomador_formatado', top=1.26*cm, left=1.4*cm, width=18*cm)
        self.elements.append(fld)

        # 4ª linha
        lbl = Titulo(text='Município:', top=1.68*cm, left=0*cm, width=1.4*cm)
        self.elements.append(lbl)
        fld = Campo(attribute_name='RPS.CidadeTomadorDescricao.valor', top=1.68*cm, left=1.4*cm, width=18*cm)
        self.elements.append(fld)

        self.elements.append(Line(top=2.1*cm, bottom=2.1*cm, left=0*cm, right=19.4*cm, stroke_width=0.1))

        self.height = 2.1*cm


class DiscriminacaoRetrato(BandaRPS):
    def __init__(self):
        super(DiscriminacaoRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='titulo_discriminacao', titulo='DISCRIMINAÇÃO DOS SERVIÇOS', top=0*cm, left=0*cm, width=19.4*cm)

        fld = Campo(attribute_name='RPS.descricao_formatada', top=0.42*cm, left=0*cm, width=19.4*cm)
        fld.style = DADO_CAMPO_NORMAL
        fld.height = 3.98*cm
        self.elements.append(fld)

        #self.elements.append(Line(top=4.4*cm, bottom=4.4*cm, left=0*cm, right=19.4*cm, stroke_width=0.1))

        lbl = self.inclui_descritivo_item(nome='', titulo='TRIBUTÁVEL', top=4.4*cm, left=0*cm, width=1.2*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_item(nome='', titulo='ITEM', top=4.4*cm, left=1.2*cm, width=11.3*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_item(nome='', titulo='QUANTIDADE', top=4.4*cm, left=12.5*cm, width=2.3*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_item(nome='', titulo='VALOR UNITÁRIO', top=4.4*cm, left=14.8*cm, width=2.3*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_item(nome='', titulo='VALOR TOTAL', top=4.4*cm, left=17.1*cm, width=2.3*cm, margem_direita=True)
        lbl.padding_top = 0.15*cm

        self.height = 4.82*cm


class DetItemRetrato(BandaRPS):
    def __init__(self):
        super(DetItemRetrato, self).__init__()
        self.elements = []
        txt = self.inclui_campo_item(nome='item', conteudo='tributavel_formatado', top=0*cm, left=0*cm, width=1.2*cm)
        txt.style = DADO_PRODUTO_CENTRALIZADO
        txt = self.inclui_campo_item(nome='item', conteudo='DiscriminacaoServico.valor', top=0*cm, left=1.2*cm, width=11.3*cm)
        txt = self.inclui_campo_numerico_item(nome='quantidade', conteudo='Quantidade.formato_danfe', top=0*cm, left=12.5*cm, width=2.3*cm)
        txt = self.inclui_campo_numerico_item(nome='vr_unitario', conteudo='ValorUnitario.formato_danfe', top=0*cm, left=14.8*cm, width=2.3*cm)
        txt = self.inclui_campo_numerico_item(nome='vr_total', conteudo='ValorTotal.formato_danfe', top=0*cm, left=17.1*cm, width=2.3*cm, margem_direita=True)

        #self.height = 0.28*cm
        self.auto_expand_height = True


class RodapeRetrato(BandaRPS):
    def __init__(self):
        super(RodapeRetrato, self).__init__()
        self.elements = []

        # 1ª linha
        lbl, fld = self.inclui_campo_imposto(nome='clc_bip', titulo='RPS.aliquota_pis_formatada', conteudo='RPS.ValorPIS.formato_danfe', top=0*cm, left=0*cm, width=3.88*cm)
        lbl, fld = self.inclui_campo_imposto(nome='clc_vip', titulo='RPS.aliquota_cofins_formatada', conteudo='RPS.ValorCOFINS.formato_danfe', top=0*cm, left=3.88*cm, width=3.88*cm)
        lbl, fld = self.inclui_campo_imposto(nome='clc_bis', titulo='RPS.aliquota_inss_formatada', conteudo='RPS.ValorINSS.formato_danfe', top=0*cm, left=7.76*cm, width=3.88*cm)
        lbl, fld = self.inclui_campo_imposto(nome='clc_vis', titulo='RPS.aliquota_ir_formatada', conteudo='RPS.ValorIR.formato_danfe', top=0*cm, left=11.64*cm, width=3.88*cm)
        lbl, fld = self.inclui_campo_imposto(nome='clc_vpn', titulo='RPS.aliquota_csll_formatada', conteudo='RPS.ValorCSLL.formato_danfe', top=0*cm, left=15.52*cm, width=3.88*cm, margem_direita=True)

        lbl = self._inclui_texto(nome='titulo_discriminacao', texto='VALOR TOTAL DO RPS =', top=0.85*cm, left=0*cm, width=19.4*cm)
        lbl.style = DESCRICAO_VALOR_TOTAL
        self.elements.append(lbl)

        fld = self._inclui_campo(nome='total', conteudo='RPS.ValorTotalRPS.formato_danfe', top=0.85*cm, left=14.4*cm, width=5*cm)
        fld.style = VALOR_TOTAL
        self.elements.append(fld)

        lbl, fld = self.inclui_campo_numerico(nome='iss_im', titulo='VALOR TOTAL DAS DEDUÇÕES', conteudo='RPS.ValorDeducoes.formato_danfe'    , top=1.5*cm, left=0*cm, width=4.85*cm)
        lbl, fld = self.inclui_campo_numerico(nome='iss_vr', titulo='BASE DE CÁLCULO DO ISS'  , conteudo='RPS.BaseCalculo.formato_danfe'      , top=1.5*cm, left=4.85*cm, width=4.85*cm)
        lbl, fld = self.inclui_campo_numerico(nome='iss_bc', titulo='ALÍQUOTA'                , conteudo='RPS.AliquotaAtividade.formato_danfe', top=1.5*cm, left=9.7*cm, width=4.85*cm)
        lbl, fld = self.inclui_campo_numerico(nome='iss_vr', titulo='VALOR DO ISS'            , conteudo='RPS.ValorISS.formato_danfe'         , top=1.5*cm, left=14.55*cm, width=4.85*cm, margem_direita=True)

        self.inclui_descritivo(nome='titulo_discriminacao', titulo='INFORMAÇÕES IMPORTANTES', top=2.2*cm, left=0*cm, width=19.4*cm)

        fld = Campo(attribute_name='RPS.informacoes_formatadas', top=2.62*cm, left=0*cm, width=19.4*cm)
        fld.style = DADO_CAMPO_NORMAL
        fld.height = 3.98*cm
        self.elements.append(fld)

        self.elements.append(Line(top=6.6*cm, bottom=6.6*cm, left=0*cm, right=19.4*cm, stroke_width=0.1))

        fld = RPSRetrato.ObsImpressao()
        fld.top = 6.6*cm
        self.elements.append(fld)

        self.height = 6.6*cm
