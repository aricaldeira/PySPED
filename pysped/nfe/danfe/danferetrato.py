# -*- coding: utf-8 -*-


from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor

from geraldo import Report, ReportBand
from geraldo import ObjectValue, SystemField, Label, Line
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
    def __init__(self):
        super(CanhotoRetrato, self).__init__()
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


class RemetenteRetrato(BandaDANFE):
    def __init__(self):
        super(RemetenteRetrato, self).__init__()
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
        

class DestinatarioRetrato(BandaDANFE):
    def __init__(self):
        super(DestinatarioRetrato, self).__init__()
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
        
        
class LocalRetiradaRetrato(BandaDANFE):
    def __init__(self):
        super(LocalRetiradaRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='locret', titulo=u'LOCAL DE RETIRADA', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        self.inclui_texto(nome='locret_cnpj', titulo=u'CNPJ/CPF', texto=u'02.544.208/0001-05', top=0.42*cm, left=0*cm, width=3.2*cm)
        self.inclui_texto(nome='locret_endereco', titulo=u'ENDEREÇO', texto=u'', top=0.42*cm, left=3.2*cm, width=16.2*cm, margem_direita=True)
        
        self.height = 1.12*cm

class LocalEntregaRetrato(BandaDANFE):
    def __init__(self):
        super(LocalEntregaRetrato, self).__init__()
        self.elements = []
        self.inclui_descritivo(nome='locent', titulo=u'LOCAL DE ENTREGA', top=0*cm, left=0*cm, width=19.4*cm)

        # 1ª linha
        self.inclui_texto(nome='locent_cnpj', titulo=u'CNPJ/CPF', texto=u'02.544.208/0001-05', top=0.42*cm, left=0*cm, width=3.2*cm)
        self.inclui_texto(nome='locent_endereco', titulo=u'ENDEREÇO', texto=u'', top=0.42*cm, left=3.2*cm, width=16.2*cm, margem_direita=True)

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
        self.inclui_texto_numerico(nome='clc_bip', titulo=u'BASE DE CÁLCULO DO ICMS', texto=u'9.999.999.999,99', top=0.42*cm, left=0*cm, width=3.88*cm)
        self.inclui_texto_numerico(nome='clc_vip', titulo=u'VALOR DO ICMS', texto=u'9.999.999.999,99', top=0.42*cm, left=3.88*cm, width=3.88*cm)
        self.inclui_texto_numerico(nome='clc_bis', titulo=u'BASE DE CÁLCULO DO ICMS ST', texto=u'9.999.999.999,99', top=0.42*cm, left=7.76*cm, width=3.88*cm)
        self.inclui_texto_numerico(nome='clc_vis', titulo=u'VALOR DO ICMS ST', texto=u'9.999.999.999,99', top=0.42*cm, left=11.64*cm, width=3.88*cm)
        self.inclui_texto_numerico(nome='clc_vpn', titulo=u'VALOR TOTAL DOS PRODUTOS', texto=u'9.999.999.999,99', top=0.42*cm, left=15.52*cm, width=3.88*cm, margem_direita=True)

        # 2ª linha
        self.inclui_texto_numerico(nome='clc_vfrete', titulo=u'VALOR DO FRETE', texto=u'9.999.999.999,99', top=1.12*cm, left=0*cm, width=3.104*cm)
        self.inclui_texto_numerico(nome='clc_vseguro', titulo=u'VALOR DO SEGURO', texto=u'9.999.999.999,99', top=1.12*cm, left=3.104*cm, width=3.104*cm)
        self.inclui_texto_numerico(nome='clc_vdesconto', titulo=u'DESCONTO', texto=u'9.999.999.999,99', top=1.12*cm, left=6.208*cm, width=3.104*cm)
        self.inclui_texto_numerico(nome='clc_voutras', titulo=u'OUTRAS DESPESAS ACESSÓRIAS', texto=u'9.999.999.999,99', top=1.12*cm, left=9.312*cm, width=3.104*cm)
        self.inclui_texto_numerico(nome='clc_vipi', titulo=u'VALOR TOTAL DO IPI', texto=u'9.999.999.999,99', top=1.12*cm, left=12.416*cm, width=3.104*cm)
        self.inclui_texto_numerico(nome='clc_vnf', titulo=u'VALOR TOTAL DA NOTA', texto=u'9.999.999.999,99', top=1.12*cm, left=15.52*cm, width=3.88*cm, margem_direita=True)
        
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


class CabProdutoRetrato(BandaDANFE):
    def __init__(self):
        super(CabProdutoRetrato, self).__init__()
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
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR UNITÁRIO', top=0.42*cm, left=12.04*cm, width=1.4*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR TOTAL', top=0.42*cm, left=13.44*cm, width=1.2*cm)
        lbl.margin_top = 0.2*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='BASE CÁLC. DO ICMS', top=0.42*cm, left=14.64*cm, width=1.2*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR DO ICMS', top=0.42*cm, left=15.84*cm, width=1.2*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='VALOR DO IPI', top=0.42*cm, left=17.04*cm, width=1.2*cm)
        lbl.margin_top = 0.2*cm
        lbl = self.inclui_descritivo_produto(nome='', titulo='ALÍQUOTAS', top=0.42*cm, left=18.24*cm, width=1.16*cm, height=0.26*cm, margem_direita=True)
        lbl = self.inclui_descritivo_produto(nome='', titulo='ICMS', top=0.68*cm, left=18.24*cm, width=0.58*cm, height=0.26*cm)
        lbl = self.inclui_descritivo_produto(nome='', titulo='IPI', top=0.68*cm, left=18.82*cm, width=0.58*cm, height=0.26*cm, margem_direita=True)
        
        self.height = 0.94*cm


class DetProdutoRetrato(BandaDANFE):
    def __init__(self):
        super(DetProdutoRetrato, self).__init__()
        self.elements = []

        txt = self.inclui_texto_produto(nome='', texto='MMMMMMMMMMMMMM', top=0*cm, left=0*cm, width=2.6*cm)
        txt = self.inclui_texto_centralizado_produto(nome='', texto='999999999', top=0*cm, left=2.6*cm, width=1*cm)
        txt = self.inclui_texto_produto(nome='', texto='ISTO É UM TESTE<br />ÁÉÍÓÚ ÂÊÔ ÃÕÑ À Ü Ç<br />3<br />4<br />abcçdefghijklmnopqrstuvwxyz 0123456879,.;/?!@$%&ªº', top=0*cm, left=3.6*cm, width=6.31*cm)
        txt = self.inclui_texto_centralizado_produto(nome='', texto='999', top=0*cm, left=9.91*cm, width=0.44*cm)
        txt = self.inclui_texto_centralizado_produto(nome='', texto='9999', top=0*cm, left=10.35*cm, width=0.54*cm)
        txt = self.inclui_texto_centralizado_produto(nome='', texto='MMMMMM', top=0*cm, left=10.89*cm, width=1.15*cm)
        txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,9999', top=0*cm, left=12.04*cm, width=1.4*cm)
        txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=13.44*cm, width=1.2*cm)
        txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=14.64*cm, width=1.2*cm)
        txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=15.84*cm, width=1.2*cm)
        txt = self.inclui_texto_numerico_produto(nome='', texto='9.999.999,99', top=0*cm, left=17.04*cm, width=1.2*cm)
        txt = self.inclui_texto_numerico_produto(nome='', texto='99,99', top=0*cm, left=18.24*cm, width=0.58*cm)
        txt = self.inclui_texto_numerico_produto(nome='', texto='99,99', top=0*cm, left=18.82*cm, width=0.58*cm, margem_direita=True)

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
