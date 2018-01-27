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

from geraldo import Report
from geraldo import Line
from geraldo.generators import PDFGenerator

import os
#cur_dir = os.path.dirname(os.path.abspath(__file__))
cur_dir = '/home/ari/django/danfe/'

from registrafontes import registra_fontes

from base import (BandaDANFE,
                  DADO_CHAVE,
                  DADO_VARIAVEL,
                  DESCRITIVO_CAMPO,
                  DESCRITIVO_NUMERO,
                  OBS_CONTINGENCIA,
                  OBS_HOMOLOGACAO,
                  MARGEM_DIREITA,
                  MARGEM_ESQUERDA,
                  MARGEM_INFERIOR,
                  MARGEM_SUPERIOR,
                  PAISAGEM)


class DANFEPaisagem(Report):
    title = 'DANFE - Documento Auxiliar da Nota Fiscal Eletrônica'
    author = 'Taŭga Haveno'
    print_if_empty = True

    page_size = PAISAGEM
    margin_top = MARGEM_SUPERIOR
    margin_bottom = MARGEM_INFERIOR
    margin_left = MARGEM_ESQUERDA
    margin_right = MARGEM_DIREITA

    def __init__(self, *args, **kargs):
        super(DANFEPaisagem, self).__init__(*args, **kargs)

    def on_new_page(self, generator):
        if generator._current_page_number <> 1:
            self.band_page_footer = None

            self.band_page_header = RemetentePaisagem()
            self.band_page_header.campo_variavel_normal()

            self.band_page_header.child_bands = []
            self.band_page_header.child_bands.append(CabProdutoPaisagem())


class CanhotoPaisagem(BandaDANFE):
    def __init__(self):
        super(CanhotoPaisagem, self).__init__()
        self.elements = []
        self.inclui_texto(nome='canhoto_recebemos', titulo=u'RECEBEMOS OS PRODUTOS E/OU SERVIÇOS CONSTANTES DA NOTA FISCAL ELETRÔNICA INDICADA AO LADO DE', texto='', top=0*cm, left=0*cm, width=16*cm)
        self.inclui_texto(nome='canhoto_data', titulo=u'DATA DE RECEBIMENTO', texto='', top=0.7*cm, left=0*cm, width=2.7*cm)
        self.inclui_texto(nome='canhoto_assinatura', titulo=u'IDENTIFICAÇÃO E ASSINATURA DO RECEBEDOR', texto='', top=0.7*cm, left=2.7*cm, width=13.3*cm)

        lbl, txt = self.inclui_texto(nome='canhoto_nfe', titulo=u'NF-e', texto='', top=0*cm, left=16*cm, width=3.4*cm, height=1.4*cm, margem_direita=True)
        lbl.style = DESCRITIVO_NUMERO
        txt = self.inclui_texto_sem_borda(nome='canhoto_numero', texto=u'Nº 000.000.000', top=0.4*cm, left=16*cm, width=3.4*cm, height=0.5*cm)
        txt.style = DESCRITIVO_NUMERO
        txt = self.inclui_texto_sem_borda(nome='canhoto_numero', texto=u'SÉRIE 000', top=0.8*cm, left=16*cm, width=3.4*cm, height=0.5*cm)
        txt.style = DESCRITIVO_NUMERO

        self.elements.append(Line(top=1.65*cm, bottom=1.65*cm, left=0*cm, right=19.4*cm, stroke_width=0.1))
        self.height = 1.9*cm


class RemetentePaisagem(BandaDANFE):
    def __init__(self):
        super(RemetentePaisagem, self).__init__()
        self.elements = []

        txt = self.inclui_texto_sem_borda(nome='obs_contingencia', texto='DANFE EM CONTINGÊNCIA<br /><br />IMPRESSO EM DECORRÊNCIA DE PROBLEMAS TÉCNICOS', top=4*cm, left=0*cm, width=19.4*cm)
        txt.margin_top = 0.1*cm
        txt.style = OBS_CONTINGENCIA

        self.inclui_texto(nome='remetente_nome', titulo='', texto='', top=0*cm, left=0*cm, width=8*cm, height=4*cm)
        self.inclui_texto(nome='retemente_danfe', titulo='', texto='', top=0*cm, left=8*cm, width=3.4*cm, height=4*cm)

        self.inclui_texto(nome='remetente_codigobarras', titulo='', texto='', top=0*cm, left=11.4*cm, width=8*cm, height=1.625*cm, margem_direita=True)
        lbl, fld = self.inclui_texto(nome='remetente_chave', titulo=u'CHAVE DE ACESSO', texto=u'1234 5678 9012 3456 7890 1234 5678 9012 3456 7890 1234', top=1.625*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        fld.style = DADO_CHAVE


        self.inclui_texto(nome='remetente_natureza', titulo=u'NATUREZA DA OPERAÇÃO', texto=u'VENDA PARA CONSUMIDOR FINAL', top=4*cm, left=0*cm, width=11.4*cm)

        self.inclui_texto(nome='remetente_ie', titulo=u'INSCRIÇÃO ESTADUAL', texto=u'', top=4.70*cm, left=0*cm, width=6.4*cm)
        self.inclui_texto(nome='remetente_iest', titulo=u'INSCRIÇÃO ESTADUAL DO SUBSTITUTO TRIBUTÁRIO', texto=u'', top=4.70*cm, left=6.4*cm, width=6.6*cm)
        self.inclui_texto(nome='remetente_cnpj', titulo=u'CNPJ', texto=u'', top=4.70*cm, left=13*cm, width=6.4*cm, margem_direita=True)

        self.height = 5.4*cm

    def campo_variavel_normal(self):
        txt = self.inclui_texto_sem_borda(nome='remetente_var1', texto=u'Consulta de autenticidade no portal nacional da NF-e<br /><a href="http://www.nfe.fazenda.gov.br/portal"><u>www.nfe.fazenda.gov.br/portal</u></a><br /> ou no site da SEFAZ autorizadora', top=2.375*cm, left=11.4*cm, width=8*cm, height=1.625*cm)
        txt.margin_top = 0.1*cm
        txt.style = DADO_VARIAVEL

        lbl, txt = self.inclui_texto(nome='remetente_var2', titulo=u'PROTOCOLO DE AUTORIZAÇÃO DE USO', texto=u'123456789012345 99/99/9999 99:99:99', top=4*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        txt.style = DADO_VARIAVEL

    def campo_variavel_fsda(self):
        pass

    def campo_variavel_dpec(self):
        txt = self.inclui_texto_sem_borda(nome='remetente_var1', texto=u'Consulta de autenticidade no portal nacional da NF-e<br /><a href="http://www.nfe.fazenda.gov.br/portal"><u>www.nfe.fazenda.gov.br/portal</u></a>', top=2.375*cm, left=11.4*cm, width=8*cm, height=1.625*cm)
        txt.margin_top = 0.4*cm
        txt.style = DADO_VARIAVEL

        lbl, txt = self.inclui_texto(nome='remetente_var2', titulo=u'NÚMERO DE REGISTRO DPEC', texto=u'123456789012345 99/99/9999 99:99:99', top=4*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        txt.style = DADO_VARIAVEL


class DestinatarioPaisagem(BandaDANFE):
    def __init__(self):
        super(DestinatarioPaisagem, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='remetente', titulo=u'DESTINATÁRIO/REMETENTE', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        self.inclui_texto(nome='remetente_nome', titulo=u'NOME/RAZÃO SOCIAL', texto=u'TAUGA RS TECNOLOGIA LTDA.', top=0.42*cm, left=0*cm, width=14*cm)
        self.inclui_texto(nome='remetente_cnpj', titulo=u'CNPJ/CPF', texto=u'02.544.208/0001-05', top=0.42*cm, left=14*cm, width=3.2*cm)
        self.inclui_texto(nome='remetente_data_emissao', titulo=u'DATA DA EMISSÃO', texto=u'99/99/9999', top=0.42*cm, left=17.2*cm, width=2.2*cm, margem_direita=True)

        # 2ª linha
        self.inclui_texto(nome='remetente_nome', titulo=u'ENDEREÇO', texto=u'R. IBIUNA, 729 - SALA 2', top=1.12*cm, left=0*cm, width=10.9*cm)
        self.inclui_texto(nome='remetente_bairro', titulo=u'BAIRRO/DISTRITO', texto=u'JD. MORUMBI', top=1.12*cm, left=10.9*cm, width=4.5*cm)
        self.inclui_texto(nome='remetente_cep', titulo=u'CEP', texto=u'99.999-999', top=1.12*cm, left=15.4*cm, width=1.8*cm)
        self.inclui_texto(nome='remetente_data_entradasaida', titulo=u'DATA DA ENTRADA/SAÍDA', texto=u'99/99/9999', top=1.12*cm, left=17.2*cm, width=2.2*cm, margem_direita=True)

        # 3ª linha
        self.inclui_texto(nome='remetente_municipio', titulo=u'MUNICÍPIO', texto=u'SOROCABA', top=1.82*cm, left=0*cm, width=10.4*cm)
        self.inclui_texto(nome='remetente_fone', titulo=u'FONE', texto=u'(15) 3411-0602', top=1.82*cm, left=10.4*cm, width=2.8*cm)
        self.inclui_texto(nome='remetente_uf', titulo=u'UF', texto='MM', top=1.82*cm, left=13.2*cm, width=0.8*cm)
        self.inclui_texto(nome='remetente_ie', titulo=u'INSCRIÇÃO ESTADUAL', texto=u'MM999999999999', top=1.82*cm, left=14*cm, width=3.2*cm)
        self.inclui_texto(nome='remetente_hora_entradasaida', titulo=u'HORA DA ENTRADA/SAÍDA', texto=u'99h99', top=1.82*cm, left=17.2*cm, width=2.2*cm, margem_direita=True)

        self.height = 2.52*cm


class LocalRetiradaPaisagem(BandaDANFE):
    def __init__(self):
        super(LocalRetiradaPaisagem, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='locret', titulo=u'LOCAL DE RETIRADA', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        self.inclui_texto(nome='locret_cnpj', titulo=u'CNPJ/CPF', texto=u'02.544.208/0001-05', top=0.42*cm, left=0*cm, width=3.2*cm)
        self.inclui_texto(nome='locret_endereco', titulo=u'ENDEREÇO', texto=u'', top=0.42*cm, left=3.2*cm, width=16.2*cm, margem_direita=True)

        self.height = 1.12*cm

class LocalEntregaPaisagem(BandaDANFE):
    def __init__(self):
        super(LocalEntregaPaisagem, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='locent', titulo=u'LOCAL DE ENTREGA', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        self.inclui_texto(nome='locent_cnpj', titulo=u'CNPJ/CPF', texto=u'02.544.208/0001-05', top=0.42*cm, left=0*cm, width=3.2*cm)
        self.inclui_texto(nome='locent_endereco', titulo=u'ENDEREÇO', texto=u'', top=0.42*cm, left=3.2*cm, width=16.2*cm, margem_direita=True)

        self.height = 1.12*cm


class FaturaAVistaPaisagem(BandaDANFE):
    def __init__(self):
        super(FaturaAVistaPaisagem, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='fat', titulo=u'FATURA', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        lbl, txt = self.inclui_texto(nome='fat_texto', titulo='', texto=u'PAGAMENTO À VISTA', top=0.42*cm, left=0*cm, width=19.4*cm)
        lbl.borders['right'] = False

        self.height = 1.12*cm


class CalculoImpostoPaisagem(BandaDANFE):
    def __init__(self):
        super(CalculoImpostoPaisagem, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='clc', titulo=u'CÁLCULO DO IMPOSTO', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        lbl, txt = self.inclui_texto_numerico(nome='clc_bip', titulo=u'BASE DE CÁLCULO DO ICMS', texto=u'9.999.999.999,99', top=0.42*cm, left=0*cm, width=3.88*cm)
        lbl, txt = self.inclui_texto_numerico(nome='clc_vip', titulo=u'VALOR DO ICMS', texto=u'9.999.999.999,99', top=0.42*cm, left=3.88*cm, width=3.88*cm)
        lbl, txt = self.inclui_texto_numerico(nome='clc_bis', titulo=u'BASE DE CÁLCULO DO ICMS ST', texto=u'9.999.999.999,99', top=0.42*cm, left=7.76*cm, width=3.88*cm)
        lbl, txt = self.inclui_texto_numerico(nome='clc_vis', titulo=u'VALOR DO ICMS ST', texto=u'9.999.999.999,99', top=0.42*cm, left=11.64*cm, width=3.88*cm)
        lbl, txt = self.inclui_texto_numerico(nome='clc_vpn', titulo=u'VALOR TOTAL DOS PRODUTOS', texto=u'9.999.999.999,99', top=0.42*cm, left=15.52*cm, width=3.88*cm, margem_direita=True)

        # 2ª linha
        lbl, txt = self.inclui_texto_numerico(nome='clc_vfrete', titulo=u'VALOR DO FRETE', texto=u'9.999.999.999,99', top=1.12*cm, left=0*cm, width=3.104*cm)
        lbl, txt = self.inclui_texto_numerico(nome='clc_vseguro', titulo=u'VALOR DO SEGURO', texto=u'9.999.999.999,99', top=1.12*cm, left=3.104*cm, width=3.104*cm)
        lbl, txt = self.inclui_texto_numerico(nome='clc_vdesconto', titulo=u'DESCONTO', texto=u'9.999.999.999,99', top=1.12*cm, left=6.208*cm, width=3.104*cm)
        lbl, txt = self.inclui_texto_numerico(nome='clc_voutras', titulo=u'OUTRAS DESPESAS ACESSÓRIAS', texto=u'9.999.999.999,99', top=1.12*cm, left=9.312*cm, width=3.104*cm)
        lbl, txt = self.inclui_texto_numerico(nome='clc_vipi', titulo=u'VALOR TOTAL DO IPI', texto=u'9.999.999.999,99', top=1.12*cm, left=12.416*cm, width=3.104*cm)
        lbl, txt = self.inclui_texto_numerico(nome='clc_vnf', titulo=u'VALOR TOTAL DA NOTA', texto=u'9.999.999.999,99', top=1.12*cm, left=15.52*cm, width=3.88*cm, margem_direita=True)

        self.height = 1.82*cm


class TransportePaisagem(BandaDANFE):
    def __init__(self):
        super(TransportePaisagem, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='clc', titulo=u'TRANSPORTADOR/VOLUMES TRANSPORTADOS', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        self.inclui_texto_numerico(nome='trn_bip', titulo=u'NOME/RAZÃO SOCIAL', texto='', top=0.42*cm, left=0*cm, width=9.7*cm)

        self.inclui_texto(nome='trn_placa', titulo=u'FRETE POR CONTA', texto='', top=0.42*cm, left=9.7*cm, width=1.9*cm)
        txt = self.inclui_texto_sem_borda(nome='', texto='0 - EMITENTE', top=0.62*cm, left=9.7*cm, width=1.9*cm)
        txt.style = DESCRITIVO_CAMPO

        txt = self.inclui_texto_sem_borda(nome='', texto='1 - DESTINATÁRIO', top=0.82*cm, left=9.7*cm, width=1.9*cm)
        txt.style = DESCRITIVO_CAMPO

        txt = self.inclui_texto_sem_borda(nome='', texto='9', top=0.62*cm, left=11.25*cm, width=0.25*cm)
        txt.height = 0.35*cm
        txt.margin_top = 0*cm
        txt.margin_left = 0.05*cm
        txt.margin_bottom = 0*cm
        txt.margin_right = 0*cm
        txt.borders_stroke_width = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': 0.1}
        txt.borders = {'top': True, 'right': True, 'bottom': True, 'left': True}


        self.inclui_texto(nome='trn_placa', titulo=u'CÓDIGO ANTT', texto='', top=0.42*cm, left=11.6*cm, width=1.9*cm)
        self.inclui_texto(nome='trn_placa', titulo=u'PLACA DO VEÍCULO', texto=u'MMM-9999', top=0.42*cm, left=13.5*cm, width=1.9*cm)
        self.inclui_texto(nome='trn_vei_uf', titulo=u'UF', texto='MM', top=0.42*cm, left=15.4*cm, width=0.8*cm)
        self.inclui_texto(nome='trn_cnpj', titulo=u'CNPJ/CPF', texto=u'02.544.208/0001-05', top=0.42*cm, left=16.2*cm, width=3.2*cm, margem_direita=True)

        # 2ª linha
        self.inclui_texto_numerico(nome='trn_end', titulo=u'ENDEREÇO', texto='', top=1.12*cm, left=0*cm, width=9.7*cm)
        self.inclui_texto_numerico(nome='trn_mun', titulo=u'MUNICÍPIO', texto='', top=1.12*cm, left=9.7*cm, width=5.7*cm)
        self.inclui_texto(nome='trn_uf', titulo=u'UF', texto='MM', top=1.12*cm, left=15.4*cm, width=0.8*cm)
        self.inclui_texto(nome='trn_ie', titulo=u'INSCRIÇÃO ESTADUAL', texto=u'MM999999999999', top=1.12*cm, left=16.2*cm, width=3.2*cm, margem_direita=True)

        # 3ª linha
        self.inclui_texto_numerico(nome='trn_qtd', titulo=u'QUANTIDADE', texto='9.999.999.999,999999', top=1.82*cm, left=0*cm, width=3.2*cm)
        self.inclui_texto(nome='trn_esp', titulo=u'ESPÉCIE', texto='', top=1.82*cm, left=3.2*cm, width=3.2*cm)
        self.inclui_texto(nome='trn_esp', titulo=u'MARCA', texto='', top=1.82*cm, left=6.4*cm, width=3.4*cm)
        self.inclui_texto(nome='trn_esp', titulo=u'NÚMERO', texto='', top=1.82*cm, left=9.8*cm, width=3.2*cm)
        self.inclui_texto_numerico(nome='trn_qtd', titulo=u'PESO BRUTO', texto='9.999.999.999,999999', top=1.82*cm, left=13*cm, width=3.2*cm)
        self.inclui_texto_numerico(nome='trn_qtd', titulo=u'PESO LÍQUIDO', texto='9.999.999.999,999999', top=1.82*cm, left=16.2*cm, width=3.2*cm, margem_direita=True)

        self.height = 2.52*cm


class CabProdutoPaisagem(BandaDANFE):
    def __init__(self):
        super(CabProdutoPaisagem, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='cabprod', titulo=u'DADOS DOS PRODUTOS/SERVIÇOS', top=0*cm, left=0*cm, width=19.4*cm)

        txt = self.inclui_texto_sem_borda(nome='obs_homologacao', texto='SEM VALOR FISCAL', top=1*cm, left=0*cm, width=19.4*cm)
        txt.margin_top = 0.1*cm
        txt.style = OBS_HOMOLOGACAO

        lbl = self.inclui_descritivo_produto(nome='', titulo='CÓDIGO DO PRODUTO', top=0.42*cm, left=0*cm, width=2.6*cm)
        lbl.margin_top = 0.2*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='NCM/SH', top=0.42*cm, left=2.6*cm, width=1*cm)
        lbl.margin_top = 0.2*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='DESCRIÇÃO DO PRODUTO/SERVIÇO', top=0.42*cm, left=3.6*cm, width=6.31*cm)
        lbl.margin_top = 0.2*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='CST', top=0.42*cm, left=9.91*cm, width=0.44*cm)
        lbl.margin_top = 0.2*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='CFOP', top=0.42*cm, left=10.35*cm, width=0.54*cm)
        lbl.margin_top = 0.2*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='UNIDADE', top=0.42*cm, left=10.89*cm, width=1.15*cm)
        lbl.margin_top = 0.2*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR', top=0.42*cm, left=12.04*cm, width=1.4*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='UNITÁRIO', top=0.62*cm, left=12.04*cm, width=1.4*cm)
        lbl.borders = {'top': False, 'right': False, 'bottom': False, 'left': False}
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR TOTAL', top=0.42*cm, left=13.44*cm, width=1.2*cm)
        lbl.margin_top = 0.2*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='BASE CÁLC.', top=0.42*cm, left=14.64*cm, width=1.2*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='DO ICMS', top=0.62*cm, left=14.64*cm, width=1.2*cm)
        lbl.borders = {'top': False, 'right': False, 'bottom': False, 'left': False}
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR DO', top=0.42*cm, left=15.84*cm, width=1.2*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='ICMS', top=0.62*cm, left=15.84*cm, width=1.2*cm)
        lbl.borders = {'top': False, 'right': False, 'bottom': False, 'left': False}
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR DO IPI', top=0.42*cm, left=17.04*cm, width=1.2*cm)
        lbl.margin_top = 0.2*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='ALÍQUOTAS', top=0.42*cm, left=18.24*cm, width=1.16*cm, height=0.26*cm, margem_direita=True)
        lbl = self.inclui_descritivo_produto(nome='', titulo='ICMS', top=0.68*cm, left=18.24*cm, width=0.58*cm, height=0.26*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='IPI', top=0.68*cm, left=18.82*cm, width=0.58*cm, height=0.26*cm, margem_direita=True)

        self.height = 0.94*cm


class DetProdutoPaisagem(BandaDANFE):
    def __init__(self):
        super(DetProdutoPaisagem, self).__init__()
        self.elements = []

        self.inclui_texto_produto(nome='', texto='MMMMMMMMMMMMMM', top=0*cm, left=0*cm, width=2.6*cm)
        self.inclui_texto_centralizado_produto(nome='', texto='999999999', top=0*cm, left=2.6*cm, width=1*cm)
        self.inclui_texto_produto(nome='', texto='1<br />2<br />3<br />4<br />5', top=0*cm, left=3.6*cm, width=6.31*cm)
        self.inclui_texto_centralizado_produto(nome='', texto='999', top=0*cm, left=9.91*cm, width=0.44*cm)
        self.inclui_texto_centralizado_produto(nome='', texto='9999', top=0*cm, left=10.35*cm, width=0.54*cm)
        self.inclui_texto_centralizado_produto(nome='', texto='MMMMMM', top=0*cm, left=10.89*cm, width=1.15*cm)
        self.inclui_texto_numerico_produto(nome='', texto='9.999.999,9999', top=0*cm, left=12.04*cm, width=1.4*cm)
        self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=13.44*cm, width=1.2*cm)
        self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=14.64*cm, width=1.2*cm)
        self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=15.84*cm, width=1.2*cm)
        self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=17.04*cm, width=1.2*cm)
        self.inclui_texto_numerico_produto(nome='', texto='99,99', top=0*cm, left=18.24*cm, width=0.58*cm)
        self.inclui_texto_numerico_produto(nome='', texto='99,99', top=0*cm, left=18.82*cm, width=0.58*cm, margem_direita=True)

        #self.height = 0.28*cm
        self.auto_expand_height = True


class ISSPaisagem(BandaDANFE):
    def __init__(self):
        super(ISSPaisagem, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='iss', titulo=u'CÁLCULO DO ISSQN', top=0*cm, left=0*cm, width=19.4*cm)

        self.inclui_texto(nome='iss', titulo=u'INSCRIÇÃO MUNICIPAL', texto='', top=0.42*cm, left=0*cm, width=4.85*cm)
        self.inclui_texto_numerico(nome='iss', titulo=u'VALOR TOTAL DOS SERVIÇOS', texto='9.999.999.999,99', top=0.42*cm, left=4.85*cm, width=4.85*cm)
        self.inclui_texto_numerico(nome='iss', titulo=u'BASE DE CÁLCULO DO ISSQN', texto='9.999.999.999,99', top=0.42*cm, left=9.7*cm, width=4.85*cm)
        self.inclui_texto_numerico(nome='iss', titulo=u'VALOR DO ISSQN', texto='9.999.999.999,99', top=0.42*cm, left=14.55*cm, width=4.85*cm)

        self.height = 1.12*cm


class DadosAdicionaisPaisagem(BandaDANFE):
    def __init__(self):
        super(DadosAdicionaisPaisagem, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='clc', titulo=u'DADOS ADICIONAIS', top=0*cm, left=0*cm, width=19.4*cm)

        self.inclui_texto(nome='', titulo='INFORMAÇÕES COMPLEMENTARES', texto='', top=0.42*cm, left=0*cm, width=11.7*cm, height=4*cm)
        self.inclui_texto(nome='', titulo='RESERVADO AO FISCO', texto='', top=0.42*cm, left=11.7*cm, width=7.7*cm, height=4*cm, margem_direita=True)

        self.height = 4.42*cm


if __name__ == '__main__':
    registra_fontes()

    registros = [{'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1},]

    d = DANFEPaisagem()
    #d.on_new_page = OnNewPage

    d.queryset = registros
    d.band_page_header = CanhotoPaisagem()
    d.band_page_header.child_bands = []

    d.band_page_header.child_bands.append(RemetentePaisagem())
    d.band_page_header.child_bands[0].campo_variavel_normal()

    d.band_page_header.child_bands.append(DestinatarioPaisagem())
    #d.band_page_header.child_bands.append(LocalRetiradaPaisagem())
    #d.band_page_header.child_bands.append(LocalEntregaPaisagem())
    #d.band_page_header.child_bands.append(FaturaAVistaPaisagem())
    #d.band_page_header.child_bands.append(CalculoImpostoPaisagem())
    #d.band_page_header.child_bands.append(TransportePaisagem())
    #d.band_page_header.child_bands.append(CabProdutoPaisagem())

    d.band_detail = DetProdutoPaisagem()

    d.band_page_footer = DadosAdicionaisPaisagem()

    d.generate_by(PDFGenerator, filename=os.path.join(cur_dir, 'teste.pdf'))
