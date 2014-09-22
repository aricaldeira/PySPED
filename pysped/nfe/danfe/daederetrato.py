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
from pysped.nfe.danfe.danferetrato import (DANFERetrato,
    RemetenteRetrato as DANFERemetenteRetrato, DestinatarioRetrato)


class DAEDERetrato(DANFERetrato):
    def __init__(self, *args, **kargs):
        super(DAEDERetrato, self).__init__(*args, **kargs)
        self.title = 'DAEDE - Documento Auxiliar de Evento de Documento Eletrônico'

        # Bandas e observações
        self.remetente    = RemetenteRetrato()
        self.destinatario = DestinatarioRetrato()
        self.det_evento   = DetEventoRetrato()
        self.det_evento.child_bands = []
        self.det_evento.child_bands = [DetEventoTextoRetrato()]
        self.band_page_footer = RodapeFinalRetrato()

    def on_new_page(self, page, page_number, generator):
        pass

    class ObsImpressao(SystemField):
        expression = u'DAEDE gerado em %(now:%d/%m/%Y, %H:%M:%S)s'

        def __init__(self):
            self.name = 'obs_impressao'
            self.top = 0*cm
            self.left = 0.1*cm
            self.width = 19.4*cm
            self.height = 0.2*cm
            self.style = DADO_PRODUTO
            self.borders = {'bottom': 0.1}


class RemetenteRetrato(DANFERemetenteRetrato):
    def __init__(self):
        super(RemetenteRetrato, self).__init__()
        self.elements = []

        # Quadro do emitente
        self.inclui_texto(nome='quadro_emitente', titulo='', texto='', top=0*cm, left=0*cm, width=8*cm, height=4*cm)

        #
        # Área central - Dados do DANFE
        #
        lbl, txt = self.inclui_texto(nome='danfe', titulo='', texto=u'DAEDE', top=0*cm, left=8*cm, width=3.4*cm, height=4*cm)
        txt.style = DESCRITIVO_DANFE

        txt = self.inclui_texto_sem_borda(nome='danfe_ext', texto=u'DOCUMENTO AUXILIAR DOS EVENTOS DA NOTA FISCAL ELETRÔNICA', top=0.6*cm, left=8*cm, width=3.4*cm, height=4*cm)
        txt.style = DESCRITIVO_DANFE_GERAL

        txt = self.inclui_texto_sem_borda(nome='danfe_ext', texto=u'versão', top=2.1*cm, left=8.8*cm, width=1.4*cm, height=0.6*cm)
        txt.style = DESCRITIVO_DANFE_GERAL

        fld = self.inclui_campo_sem_borda(nome='danfe_entrada_saida', conteudo=u'NFe.infNFe.versao.valor', top=2.1*cm, left=9.8*cm, width=0.8*cm, height=0.6*cm)
        fld.style = DESCRITIVO_DANFE_GERAL

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

        lbl, lbl = self.inclui_campo(nome='remetente_var2', titulo=u'PROTOCOLO DE AUTORIZAÇÃO DE USO', conteudo=u'protNFe.protocolo_formatado', top=2.325*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        lbl.style = DADO_VARIAVEL

        self.inclui_campo(nome='remetente_ie', titulo=u'INSCRIÇÃO ESTADUAL', conteudo=u'NFe.infNFe.emit.IE.valor', top=4*cm, left=0*cm, width=6.4*cm)
        self.inclui_campo(nome='remetente_iest', titulo=u'INSCRIÇÃO ESTADUAL DO SUBSTITUTO TRIBUTÁRIO', conteudo=u'NFe.infNFe.emit.IEST.valor', top=4*cm, left=6.4*cm, width=6.6*cm)
        self.inclui_campo(nome='remetente_cnpj', titulo=u'CNPJ', conteudo=u'NFe.cnpj_emitente_formatado', top=4*cm, left=13*cm, width=6.4*cm, margem_direita=True)

        self.height = 4.7*cm


class DetEventoRetrato(BandaDANFE):
    def __init__(self):
        super(DetEventoRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='remetente', titulo=u'EVENTO', top=0*cm, left=0*cm, width=19.4*cm)

        lbl, fld = self.inclui_campo(nome='seq_evento', titulo=u'SEQUÊNCIA', conteudo=u'evento.infEvento.nSeqEvento.valor', top=0.42*cm, left=0*cm, width=1.2*cm)
        lbl, fld = self.inclui_campo(nome='cod_evento', titulo=u'CÓD. EVENTO', conteudo=u'evento.infEvento.tpEvento.valor', top=0.42*cm, left=1.2*cm, width=1.3*cm)
        lbl, fld = self.inclui_campo(nome='nome_evento', titulo=u'EVENTO', conteudo=u'evento.infEvento.detEvento.descEvento.valor', top=0.42*cm, left=2.5*cm, width=8.9*cm)
        #fld.style = DADO_CAMPO_NEGRITO
        lbl, lbl = self.inclui_campo(nome='remetente_var2', titulo=u'PROTOCOLO DE REGISTRO DO EVENTO', conteudo=u'retEvento.protocolo_formatado', top=0.42*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        lbl.style = DADO_VARIAVEL

        lbl, fld = self.inclui_campo(nome='motivo', titulo=u'SIT.', conteudo=u'retEvento.infEvento.cStat.valor', top=1.12*cm, left=0*cm, width=1.2*cm)
        lbl, fld = self.inclui_campo(nome='motivo', titulo=u'MOTIVO', conteudo=u'retEvento.infEvento.xMotivo.valor', top=1.12*cm, left=1.2*cm, width=18.2*cm, margem_direita=True)

        self.height = 1.82*cm


class DetEventoTextoRetrato(BandaDANFE):
    def __init__(self):
        super(DetEventoTextoRetrato, self).__init__()
        self.elements = []
        lbl, txt = self.inclui_campo(nome='', titulo='DESCRIÇÃO DO EVENTO', conteudo='evento.infEvento.detEvento.texto_formatado', top=0*cm, left=0*cm, width=19.4*cm, height=4*cm, margem_direita=True)
        #txt.style = DADO_COMPLEMENTAR
        lbl.borders = {'right': False, 'left': False, 'top': False, 'bottom': False}
        txt.borders = {'right': False, 'left': False, 'top': False, 'bottom': 0.1}

        #self.height = 9*cm
        self.auto_expand_height = True


class RodapeFinalRetrato(BandaDANFE):
    def __init__(self):
        super(RodapeFinalRetrato, self).__init__()
        self.elements = []
        self.height = 0.1*cm

        # Obs de impressão
        fld = DAEDERetrato.ObsImpressao()
        fld.top = 0.1*cm
        self.elements.append(fld)