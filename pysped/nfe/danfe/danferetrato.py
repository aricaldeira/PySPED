# -*- coding: utf-8 -*-


from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor

from geraldo import Report, ReportBand
from geraldo import ObjectValue, SystemField, Label, Line, BarCode
from geraldo.generators import PDFGenerator

from pysped.relato_sped import *


class DANFERetrato(Report):
    title = 'DANFE - Documento Auxiliar da Nota Fiscal Eletrônica'
    author = 'TaŭgaRS Haveno'
    print_if_empty = True
    additional_fonts = FONTES_ADICIONAIS
    
    page_size = RETRATO
    margin_top = MARGEM_SUPERIOR
    margin_bottom = MARGEM_INFERIOR
    margin_left = MARGEM_ESQUERDA
    margin_right = MARGEM_DIREITA
    
    def __init__(self, *args, **kargs):
        super(DANFERetrato, self).__init__(*args, **kargs)

    def on_new_page(self, page, page_number, generator):
        if generator._current_page_number <> 1:
            self.band_page_footer = None
            
            self.band_page_header = RemetenteRetrato()
            self.band_page_header.campo_variavel_normal()
            
            self.band_page_header.child_bands = []
            self.band_page_header.child_bands.append(CabProdutoRetrato())
        

class CanhotoRetrato(BandaDANFE):
    def __init__(self, nfe=None, *args, **kwargs):
        super(CanhotoRetrato, self).__init__(*args, **kwargs)
        self.elements = []
        self.inclui_campo(nome='canhoto_recebemos', titulo=u'RECEBEMOS OS PRODUTOS E/OU SERVIÇOS CONSTANTES DA NOTA FISCAL ELETRÔNICA INDICADA AO LADO DE', conteudo=u'NFe.infNFe.emit.xNome.valor', top=0*cm, left=0*cm, width=16*cm)
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

        txt = self.inclui_texto_sem_borda(nome='obs_contingencia', texto='DANFE EM CONTINGÊNCIA<br /><br />IMPRESSO EM DECORRÊNCIA DE PROBLEMAS TÉCNICOS', top=4*cm, left=0*cm, width=19.4*cm)
        txt.padding_top = 0.1*cm
        txt.style = OBS_CONTINGENCIA
        
        self.inclui_texto(nome='remetente_nome', titulo='', texto='', top=0*cm, left=0*cm, width=8*cm, height=4*cm)
        
        #
        # Área central - Dados do DANFE
        #
        lbl, txt = self.inclui_texto(nome='danfe', titulo='', texto=u'DANFE', top=0*cm, left=8*cm, width=3.4*cm, height=4*cm)
        txt.style = DESCRITIVO_DANFE
        
        txt = self.inclui_texto_sem_borda(nome='danfe_ext', texto=u'DOCUMENTO AUXILIAR DA NOTA FISCAL ELETRÔNICA', top=0.6*cm, left=8*cm, width=3.4*cm, height=4*cm)
        txt.style = DESCRITIVO_DANFE_GERAL

        txt = self.inclui_texto_sem_borda(nome='danfe_entrada', texto=u'0 - ENTRADA', top=1.45*cm, left=8.3*cm, width=3.4*cm, height=4*cm)
        txt.style = DESCRITIVO_DANFE_ES

        txt = self.inclui_texto_sem_borda(nome='danfe_saida', texto=u'1 - SAÍDA', top=1.85*cm, left=8.3*cm, width=3.4*cm, height=4*cm)
        txt.style = DESCRITIVO_DANFE_ES
        
        fld = self.inclui_campo_sem_borda(nome='danfe_entrada_saida', conteudo=u'NFe.infNFe.ide.tpNF.valor', top=1.6*cm, left=10.4*cm, width=0.6*cm, height=0.6*cm)
        fld.style = DESCRITIVO_NUMERO
        fld.borders = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': 0.1}
        fld.padding_bottom = 0.2*cm
        
        fld = self.inclui_campo_sem_borda(nome='danfe_numero', conteudo=u'NFe.numero_formatado', top=2.4*cm, left=8*cm, width=3.4*cm, height=0.5*cm)
        fld.style = DESCRITIVO_NUMERO

        fld = self.inclui_campo_sem_borda(nome='danfe_serie', conteudo=u'NFe.serie_formatada', top=2.85*cm, left=8*cm, width=3.4*cm, height=0.5*cm)
        fld.style = DESCRITIVO_NUMERO
        
        txt = self.inclui_texto_sem_borda(nome='danfe_folha', texto=u'FOLHA 99/99', top=3.3*cm, left=8*cm, width=3.4*cm, height=0.5*cm)
        txt.style = DESCRITIVO_NUMERO
        
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
        
    def campo_variavel_normal(self):
        txt = self.inclui_texto_sem_borda(nome='remetente_var1', texto=u'Consulta de autenticidade no portal nacional da NF-e<br /><a href="http://www.nfe.fazenda.gov.br/portal"><u>www.nfe.fazenda.gov.br/portal</u></a><br /> ou no site da SEFAZ autorizadora', top=2.375*cm, left=11.4*cm, width=8*cm, height=1.625*cm)
        txt.padding_top = 0.2*cm
        txt.style = DADO_VARIAVEL
        
        lbl, txt = self.inclui_texto(nome='remetente_var2', titulo=u'PROTOCOLO DE AUTORIZAÇÃO DE USO', texto=u'123456789012345 99/99/9999 99:99:99', top=4*cm, left=11.4*cm, width=8*cm, margem_direita=True)
        txt.style = DADO_VARIAVEL
    
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
        

class DestinatarioRetrato(BandaDANFE):
    def __init__(self):
        super(DestinatarioRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='remetente', titulo=u'DESTINATÁRIO/REMETENTE', top=0*cm, left=0*cm, width=19.4*cm)
        
        # 1ª linha
        self.inclui_campo(nome='remetente_nome', titulo=u'NOME/RAZÃO SOCIAL', conteudo=u'NFe.infNFe.dest.xNome.valor', top=0.42*cm, left=0*cm, width=14*cm)
        self.inclui_campo(nome='remetente_cnpj', titulo=u'CNPJ/CPF', conteudo=u'NFe.cnpj_destinatario_formatado', top=0.42*cm, left=14*cm, width=3.2*cm)
        self.inclui_campo(nome='remetente_data_emissao', titulo=u'DATA DA EMISSÃO', conteudo=u'NFe.infNFe.ide.dEmi.formato_danfe', top=0.42*cm, left=17.2*cm, width=2.2*cm, margem_direita=True)

        # 2ª linha
        self.inclui_campo(nome='remetente_nome', titulo=u'ENDEREÇO', conteudo=u'NFe.endereco_destinatario_formatado', top=1.12*cm, left=0*cm, width=10.9*cm)
        self.inclui_campo(nome='remetente_bairro', titulo=u'BAIRRO/DISTRITO', conteudo=u'NFe.infNFe.dest.enderDest.xBairro.valor', top=1.12*cm, left=10.9*cm, width=4.5*cm)
        self.inclui_campo(nome='remetente_cep', titulo=u'CEP', conteudo=u'NFe.cep_destinatario_formatado', top=1.12*cm, left=15.4*cm, width=1.8*cm)
        self.inclui_campo(nome='remetente_data_entradasaida', titulo=u'DATA DA ENTRADA/SAÍDA', conteudo=u'NFe.infNFe.ide.dSaiEnt.formato_danfe', top=1.12*cm, left=17.2*cm, width=2.2*cm, margem_direita=True)

        ## 3ª linha
        self.inclui_campo(nome='remetente_municipio', titulo=u'MUNICÍPIO', conteudo=u'NFe.infNFe.dest.enderDest.xMun.valor', top=1.82*cm, left=0*cm, width=10.4*cm)
        self.inclui_campo(nome='remetente_fone', titulo=u'FONE', conteudo=u'NFe.fone_destinatario_formatado', top=1.82*cm, left=10.4*cm, width=2.8*cm)
        self.inclui_campo(nome='remetente_uf', titulo=u'UF', conteudo='NFe.infNFe.dest.enderDest.UF.valor', top=1.82*cm, left=13.2*cm, width=0.8*cm)
        self.inclui_campo(nome='remetente_ie', titulo=u'INSCRIÇÃO ESTADUAL', conteudo=u'NFe.infNFe.dest.IE.valor', top=1.82*cm, left=14*cm, width=3.2*cm)
        self.inclui_texto(nome='remetente_hora_entradasaida', titulo=u'HORA DA ENTRADA/SAÍDA', texto=u'', top=1.82*cm, left=17.2*cm, width=2.2*cm, margem_direita=True)
        
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

        self.height = 1.12*cm


class CalculoImpostoRetrato(BandaDANFE):
    def __init__(self):
        super(CalculoImpostoRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='clc', titulo=u'CÁLCULO DO IMPOSTO', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        self.inclui_campo_numerico(nome='clc_bip', titulo=u'BASE DE CÁLCULO DO ICMS', conteudo=u'NFe.infNFe.total.ICMSTot.vBC.formato_danfe', top=0.42*cm, left=0*cm, width=3.88*cm)
        self.inclui_campo_numerico(nome='clc_vip', titulo=u'VALOR DO ICMS', conteudo=u'NFe.infNFe.total.ICMSTot.vICMS.formato_danfe', top=0.42*cm, left=3.88*cm, width=3.88*cm)
        self.inclui_campo_numerico(nome='clc_bis', titulo=u'BASE DE CÁLCULO DO ICMS ST', conteudo=u'NFe.infNFe.total.ICMSTot.vBCST.formato_danfe', top=0.42*cm, left=7.76*cm, width=3.88*cm)
        self.inclui_campo_numerico(nome='clc_vis', titulo=u'VALOR DO ICMS ST', conteudo=u'NFe.infNFe.total.ICMSTot.vST.formato_danfe', top=0.42*cm, left=11.64*cm, width=3.88*cm)
        self.inclui_campo_numerico(nome='clc_vpn', titulo=u'VALOR TOTAL DOS PRODUTOS', conteudo=u'NFe.infNFe.total.ICMSTot.vProd.formato_danfe', top=0.42*cm, left=15.52*cm, width=3.88*cm, margem_direita=True)

        # 2ª linha
        self.inclui_campo_numerico(nome='clc_vfrete', titulo=u'VALOR DO FRETE', conteudo=u'NFe.infNFe.total.ICMSTot.vFrete.formato_danfe', top=1.12*cm, left=0*cm, width=3.104*cm)
        self.inclui_campo_numerico(nome='clc_vseguro', titulo=u'VALOR DO SEGURO', conteudo=u'NFe.infNFe.total.ICMSTot.vSeg.formato_danfe', top=1.12*cm, left=3.104*cm, width=3.104*cm)
        self.inclui_campo_numerico(nome='clc_vdesconto', titulo=u'DESCONTO', conteudo=u'NFe.infNFe.total.ICMSTot.vDesc.formato_danfe', top=1.12*cm, left=6.208*cm, width=3.104*cm)
        self.inclui_campo_numerico(nome='clc_voutras', titulo=u'OUTRAS DESPESAS ACESSÓRIAS', conteudo=u'NFe.infNFe.total.ICMSTot.vOutro.formato_danfe', top=1.12*cm, left=9.312*cm, width=3.104*cm)
        self.inclui_campo_numerico(nome='clc_vipi', titulo=u'VALOR TOTAL DO IPI', conteudo=u'NFe.infNFe.total.ICMSTot.vIPI.formato_danfe', top=1.12*cm, left=12.416*cm, width=3.104*cm)
        self.inclui_campo_numerico(nome='clc_vnf', titulo=u'VALOR TOTAL DA NOTA', conteudo=u'NFe.infNFe.total.ICMSTot.vNF.formato_danfe', top=1.12*cm, left=15.52*cm, width=3.88*cm, margem_direita=True)
        
        self.height = 1.82*cm


class TransporteRetrato(BandaDANFE):
    def __init__(self):
        super(TransporteRetrato, self).__init__()
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
        txt.padding_top = 0*cm
        txt.padding_left = 0.05*cm
        txt.padding_bottom = 0*cm
        txt.padding_right = 0*cm
        #txt.borders_stroke_width = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': 0.1}
        txt.borders = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': 0.1}
        
        
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
        self.inclui_texto_numerico(nome='trn_qtd', titulo=u'QUANTIDADE', texto='9.999.999.999', top=1.82*cm, left=0*cm, width=3.2*cm)
        self.inclui_texto(nome='trn_esp', titulo=u'ESPÉCIE', texto='', top=1.82*cm, left=3.2*cm, width=3.2*cm)
        self.inclui_texto(nome='trn_esp', titulo=u'MARCA', texto='', top=1.82*cm, left=6.4*cm, width=3.4*cm)
        self.inclui_texto(nome='trn_esp', titulo=u'NÚMERO', texto='', top=1.82*cm, left=9.8*cm, width=3.2*cm)
        self.inclui_texto_numerico(nome='trn_qtd', titulo=u'PESO BRUTO', texto='9.999.999.999,999', top=1.82*cm, left=13*cm, width=3.2*cm)
        self.inclui_texto_numerico(nome='trn_qtd', titulo=u'PESO LÍQUIDO', texto='9.999.999.999,999', top=1.82*cm, left=16.2*cm, width=3.2*cm, margem_direita=True)
        
        self.height = 2.52*cm


class CabProdutoRetrato(BandaDANFE):
    def __init__(self):
        super(CabProdutoRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='cabprod', titulo=u'DADOS DOS PRODUTOS/SERVIÇOS', top=0*cm, left=0*cm, width=19.4*cm)

        txt = self.inclui_texto_sem_borda(nome='obs_homologacao', texto='SEM VALOR FISCAL', top=1*cm, left=0*cm, width=19.4*cm)
        txt.padding_top = 0.1*cm
        txt.style = OBS_HOMOLOGACAO

        lbl = self.inclui_descritivo_produto(nome='', titulo='CÓDIGO DO PRODUTO', top=0.42*cm, left=0*cm, width=2.6*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='NCM/SH', top=0.42*cm, left=2.6*cm, width=1*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='DESCRIÇÃO DO PRODUTO/SERVIÇO', top=0.42*cm, left=3.6*cm, width=5.26*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='CST', top=0.42*cm, left=8.86*cm, width=0.44*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='CFOP', top=0.42*cm, left=9.3*cm, width=0.54*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='UNIDADE', top=0.42*cm, left=9.84*cm, width=1.1*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='QUANTIDADE', top=0.42*cm, left=10.94*cm, width=1.4*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR UNITÁRIO', top=0.42*cm, left=12.34*cm, width=1.4*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR TOTAL', top=0.42*cm, left=13.74*cm, width=1.2*cm)
        lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='BASE CÁLC. DO ICMS', top=0.42*cm, left=14.94*cm, width=1.2*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR DO ICMS', top=0.42*cm, left=16.14*cm, width=1.05*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR DO IPI', top=0.42*cm, left=17.19*cm, width=1.05*cm)
        #lbl.padding_top = 0.15*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='ALÍQUOTAS', top=0.42*cm, left=18.24*cm, width=1.16*cm, height=0.26*cm, margem_direita=True)
        lbl = self.inclui_descritivo_produto(nome='', titulo='ICMS', top=0.68*cm, left=18.24*cm, width=0.58*cm, height=0.26*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='IPI', top=0.68*cm, left=18.82*cm, width=0.58*cm, height=0.26*cm, margem_direita=True)
        
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
        #txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,9999', top=0*cm, left=12.34*cm, width=1.4*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=13.74*cm, width=1.2*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=14.94*cm, width=1.2*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='999.999,99', top=0*cm, left=16.14*cm, width=1.05*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='999.999,99', top=0*cm, left=17.19*cm, width=1.05*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='99,99', top=0*cm, left=18.24*cm, width=0.58*cm)
        #txt = self.inclui_texto_numerico_produto(nome='', texto='99,99', top=0*cm, left=18.82*cm, width=0.58*cm, margem_direita=True)

        txt = self.inclui_campo_produto(nome=u'prod_codigo', conteudo=u'prod.cProd.valor', top=0*cm, left=0*cm, width=2.6*cm)
        txt = self.inclui_campo_centralizado_produto(nome=u'prod_ncm', conteudo=u'prod.NCM.valor', top=0*cm, left=2.6*cm, width=1*cm)
        txt = self.inclui_campo_produto(nome=u'prod_descricaco', conteudo=u'descricao_produto_formatada', top=0*cm, left=3.6*cm, width=5.26*cm)
        txt = self.inclui_campo_centralizado_produto(nome='prod_cst', conteudo='cst_formatado', top=0*cm, left=8.86*cm, width=0.44*cm)
        txt = self.inclui_campo_centralizado_produto(nome=u'prod_cfop', conteudo=u'prod.CFOP.valor', top=0*cm, left=9.3*cm, width=0.54*cm)
        txt = self.inclui_campo_centralizado_produto(nome=u'prod_unidade', conteudo=u'prod.uCom.valor', top=0*cm, left=9.84*cm, width=1.1*cm)
        txt = self.inclui_campo_numerico_produto(nome='prod_quantidade', conteudo=u'prod.qCom.formato_danfe', top=0*cm, left=10.94*cm, width=1.4*cm)
        txt = self.inclui_campo_numerico_produto(nome='vr_unitario', conteudo=u'prod.vUnCom.formato_danfe', top=0*cm, left=12.34*cm, width=1.4*cm)
        txt = self.inclui_campo_numerico_produto(nome='', conteudo='prod.vProd.formato_danfe', top=0*cm, left=13.74*cm, width=1.2*cm)
        txt = self.inclui_campo_numerico_produto(nome='', conteudo='imposto.ICMS.vBC.formato_danfe', top=0*cm, left=14.94*cm, width=1.2*cm)
        txt = self.inclui_campo_numerico_produto(nome='', conteudo='imposto.ICMS.vICMS.formato_danfe', top=0*cm, left=16.14*cm, width=1.05*cm)
        txt = self.inclui_campo_numerico_produto(nome='', conteudo='imposto.IPI.vIPI.formato_danfe', top=0*cm, left=17.19*cm, width=1.05*cm)
        txt = self.inclui_campo_numerico_produto(nome='', conteudo='imposto.ICMS.pICMS.formato_danfe', top=0*cm, left=18.24*cm, width=0.58*cm)
        txt = self.inclui_campo_numerico_produto(nome='', conteudo='imposto.IPI.pIPI.formato_danfe', top=0*cm, left=18.82*cm, width=0.58*cm, margem_direita=True)

        #self.height = 0.28*cm
        self.auto_expand_height = True


class ISSRetrato(BandaDANFE):
    def __init__(self):
        super(ISSRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='iss', titulo=u'CÁLCULO DO ISSQN', top=0*cm, left=0*cm, width=19.4*cm)
        
        self.inclui_texto(nome='iss', titulo=u'INSCRIÇÃO MUNICIPAL', texto='', top=0.42*cm, left=0*cm, width=4.85*cm)
        self.inclui_texto_numerico(nome='iss', titulo=u'VALOR TOTAL DOS SERVIÇOS', texto='9.999.999.999,99', top=0.42*cm, left=4.85*cm, width=4.85*cm)
        self.inclui_texto_numerico(nome='iss', titulo=u'BASE DE CÁLCULO DO ISSQN', texto='9.999.999.999,99', top=0.42*cm, left=9.7*cm, width=4.85*cm)
        self.inclui_texto_numerico(nome='iss', titulo=u'VALOR DO ISSQN', texto='9.999.999.999,99', top=0.42*cm, left=14.55*cm, width=4.85*cm)
        
        self.height = 1.12*cm
        

class DadosAdicionaisRetrato(BandaDANFE):
    def __init__(self):
        super(DadosAdicionaisRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='clc', titulo=u'DADOS ADICIONAIS', top=0*cm, left=0*cm, width=19.4*cm)
        
        lbl, txt = self.inclui_texto(nome='', titulo='INFORMAÇÕES COMPLEMENTARES', texto='MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MMMMMMMMMM1234567890MM<br />', top=0.42*cm, left=0*cm, width=11.7*cm, height=4*cm)
        txt.style = DADO_COMPLEMENTAR
        self.inclui_texto(nome='', titulo='RESERVADO AO FISCO', texto='', top=0.42*cm, left=11.7*cm, width=7.7*cm, height=4*cm, margem_direita=True)
        self.inclui_texto_sem_borda(nome='', texto='Impresso no dia ', top=4.1*cm, left=0.1*cm, width=5*cm, height=0.2*cm)
        
        #self.height = 4.42*cm
        self.height = 4.62*cm


class RodapeImpressao(BandaDANFE):
    def __init__(self):
        super(RodapeImpressao, self).__init__()
        self.elements = []
        lbl, txt = self.inclui_texto(nome='', titulo='DATA DA IMPRESSÃO', texto='', top=0.1*cm, left=0*cm, width=11.7*cm, height=0.5*cm)
        
        self.height = 0.6*cm
       

if __name__ == '__main__':
    #registra_fontes()
    
    registros = [{'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1}, {'id': 1},]

    d = DANFERetrato()
    d.queryset = registros
    
    d.band_page_header = CanhotoRetrato()
    
    d.band_page_header.child_bands = []
    d.band_page_header.child_bands.append(RemetenteRetrato())
    d.band_page_header.child_bands[0].campo_variavel_normal()
    
    d.band_page_header.child_bands.append(DestinatarioRetrato())
    d.band_page_header.child_bands.append(LocalRetiradaRetrato())
    d.band_page_header.child_bands.append(LocalEntregaRetrato())
    d.band_page_header.child_bands.append(FaturaAVistaRetrato())
    d.band_page_header.child_bands.append(CalculoImpostoRetrato())
    d.band_page_header.child_bands.append(TransporteRetrato())
    d.band_page_header.child_bands.append(CabProdutoRetrato())

    d.band_detail = DetProdutoRetrato()

    d.band_page_footer = DadosAdicionaisRetrato()
    #d.band_page_footer.child_bands.append()
    
    d.generate_by(PDFGenerator, filename='danfe.pdf')
