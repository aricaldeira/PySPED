# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals


#
# RPS
#
from rps.rpsretrato import *
from StringIO import StringIO

class _Prestador(object):
    pass

class RPS(object):
    def __init__(self):
        self.caminho          = ''
        self.salvar_arquivo   = True

        self.dados_rps        = None
        self.rps              = None

        self.obs_impressao    = 'DANFE gerado em %(now:%d/%m/%Y, %H:%M:%S)s'
        self.nome_sistema     = ''
        self.site             = ''
        self.logo             = ''
        self.leiaute_logo_vertical = False
        
        self.prestador = _Prestador()
        self.prestador.nome = ''
        self.prestador.cnpj = ''
        self.prestador.im = ''
        self.prestador.endereco = ''
        self.prestador.cidade = ''
        self.prestador.estado = ''
        
        self.dados_prestador  = []

    def gerar_rps(self):
        if self.dados_rps is None:
            raise ValueError('Não é possível gerar um RPS sem a informação do arquivo xml')

        #
        # Prepara o queryset para impressão
        #
        #self.NFe.monta_chave()
        #self.NFe.monta_dados_contingencia_fsda()
        self.dados_rps.site = self.site
        self.dados_rps.prestador = self.prestador
        
        if self.prestador.nome == '':
            self.prestador.nome = self.dados_rps.RazaoSocialPrestador.valor
            
        if self.prestador.im == '':
            self.prestador.im = self.dados_rps.InscricaoMunicipalPrestador.valor
        
        for item in self.dados_rps.Itens:
            item.RPS = self.dados_rps

        #
        # Prepara as bandas de impressão para cada formato
        #
        self.rps = RPSRetrato()
        self.rps.queryset = self.dados_rps.Itens
        
        self.rps.band_page_header = self.rps.cabecalho
        self.rps.band_page_header.child_bands = []
        self.rps.band_page_header.child_bands.append(self.rps.prestador)
        self.rps.band_page_header.child_bands.append(self.rps.tomador)
        self.rps.band_page_header.child_bands.append(self.rps.discriminacao)
        
        self.rps.band_page_footer = self.rps.rodape
        
        self.rps.band_detail = self.rps.detalhe_item

        #
        # Observação de impressão
        #
        if self.nome_sistema:
            self.rps.ObsImpressao.expression = self.nome_sistema + u' - ' + self.obs_impressao
        else:
            self.rps.ObsImpressao.expression = self.obs_impressao

        ##
        ## Quadro do emitente
        ##
        ## Personalizado?
        #if self.dados_prestador:
            #self.rps.prestador.monta_quadro_prestador(self.dados_prestador)
        #else:
            ## Sem logotipo
            #if not self.logo:
                #self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_sem_logo())

            ## Logotipo na vertical
            #elif self.leiaute_logo_vertical:
                #self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_logo_vertical(self.logo))

            ## Logotipo na horizontal
            #else:
                #self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_logo_horizontal(self.logo))

        if self.salvar_arquivo:
            #nome_arq = self.caminho + self.NFe.chave + '.pdf'
            nome_arq = 'rps_teste.pdf'
            self.rps.generate_by(PDFGenerator, filename=nome_arq)

