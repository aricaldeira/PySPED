# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import *
from pysped.nfse.versao_100 import ESQUEMA_ATUAL
from pysped.nfse.versao_100.evento_100 import Alerta, Erro
import os

DIRNAME = os.path.dirname(__file__)


class ConsultaNFSe(XMLNFe):
    def __init__(self):
        super(ConsultaNFSe, self).__init__()
        self.InscricaoPrestador   = TagCaracter(nome='InscricaoPrestador'  , tamanho=[6,  11]   , raiz='//ConsultaNFSe')
        self.NumeroNFe            = TagInteiro(nome='NumeroNFe'            , tamanho=[1,  12, 1], raiz='//ConsultaNFSe')
        self.CodigoVerificacao    = TagCaracter(nome='CodigoVerificacao'   , tamanho=[1, 255]   , raiz='//ConsultaNFSe')
        self.SerieRPS             = TagCaracter(nome='SerieRPS'            , tamanho=[2,   2]   , raiz='//ConsultaNFSe')
        self.NumeroRPS            = TagInteiro(nome='NumeroRPS'            , tamanho=[1,  12, 1], raiz='//ConsultaNFSe')
        self.DataEmissaoRPS       = TagDataHora(nome='DataEmissaoRPS'                           , raiz='//ConsultaNFSe')
        self.RazaoSocialPrestador = TagCaracter(nome='RazaoSocialPrestador', tamanho=[1, 120]   , raiz='//ConsultaNFSe')
        self.TipoRecolhimento     = TagCaracter(nome='TipoRecolhimento'    , tamanho=[1,   1]   , raiz='//ConsultaNFSe')
        self.ValorDeduzir         = TagDecimal(nome='ValorDeduzir'         , tamanho=[1,  15, 1], decimais=[0, 2, 0], raiz='//ConsultaNFSe', obrigatorio=False)
        self.ValorTotal           = TagDecimal(nome='ValorTotal'           , tamanho=[1,  15, 1], decimais=[0, 2, 0], raiz='//ConsultaNFSe')
        self.Aliquota             = TagDecimal(nome='Aliquota'             , tamanho=[1,   6, 1], decimais=[0, 4, 2], raiz='//ConsultaNFSe')
    
    def get_xml(self):
        if self.InscricaoPrestador.valor.strip() == '':
            return ''
            
        xml = XMLNFe.get_xml(self)
        xml += '<ConsultaNFSe>'
        xml += self.InscricaoPrestador.xml
        xml += self.NumeroNFe.xml
        xml += self.CodigoVerificacao.xml
        xml += self.SerieRPS.xml
        xml += self.NumeroRPS.xml
        xml += self.DataEmissaoRPS.xml
        xml += self.RazaoSocialPrestador.xml
        xml += self.TipoRecolhimento.xml
        xml += self.ValorDeduzir.xml
        xml += self.ValorTotal.xml
        xml += self.Aliquota.xml
        xml += '</ConsultaNFSe>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.InscricaoPrestador.xml   = arquivo
            self.NumeroNFe.xml            = arquivo
            self.CodigoVerificacao.xml    = arquivo
            self.SerieRPS.xml             = arquivo
            self.NumeroRPS.xml            = arquivo
            self.DataEmissaoRPS.xml       = arquivo
            self.RazaoSocialPrestador.xml = arquivo
            self.TipoRecolhimento.xml     = arquivo
            self.ValorDeduzir.xml         = arquivo
            self.ValorTotal.xml           = arquivo
            self.Aliquota.xml             = arquivo
        
    xml = property(get_xml, set_xml)
        

class _Cabecalho(XMLNFe):    
    def __init__(self):
        super(_Cabecalho, self).__init__()
        self.CodCidade            = TagInteiro(nome='CodCidade'            , tamanho=[ 1, 10, 1], raiz='//nfse:RetornoConsultaLote/Cabecalho')
        self.Sucesso              = TagBoolean(nome='Sucesso'                                   , raiz='//nfse:RetornoConsultaLote/Cabecalho')
        self.NumeroLote           = TagInteiro(nome='NumeroLote'           , tamanho=[ 1, 12, 1], raiz='//nfse:RetornoConsultaLote/Cabecalho')
        self.CPFCNPJRemetente     = TagCaracter(nome='CPFCNPJRemetente'    , tamanho=[11, 14]   , raiz='//nfse:RetornoConsultaLote/Cabecalho')
        self.RazaoSocialRemetente = TagCaracter(nome='RazaoSocialRemetente', tamanho=[ 1, 120]  , raiz='//nfse:RetornoConsultaLote/Cabecalho')
        self.DataEnvioLote        = TagDataHora(nome='DataEnvioLote'                            , raiz='//nfse:RetornoConsultaLote/Cabecalho')
        self.QtdNotasProcessadas  = TagInteiro(nome='QtdNotasProcessadas'  , tamanho=[ 1, 10, 1], raiz='//nfse:RetornoConsultaLote/Cabecalho')
        self.TempoProcessamento   = TagInteiro(nome='TempoProcessamento'   , tamanho=[ 1, 15, 1], raiz='//nfse:RetornoConsultaLote/Cabecalho')
        self.ValorTotalServicos   = TagDecimal(nome='ValorTotalServicos'   , tamanho=[ 1, 15, 1], decimais=[0, 2, 2], raiz='//nfse:RetornoConsultaLote/Cabecalho')
        self.ValorTotalDeducoes   = TagDecimal(nome='ValorTotalDeducoes'   , tamanho=[ 1, 15, 1], decimais=[0, 2, 2], raiz='//nfse:RetornoConsultaLote/Cabecalho')
        self.Versao               = TagInteiro(nome='Versao'               , tamanho=[ 1,  3, 1], raiz='//nfse:RetornoConsultaLote/Cabecalho', valor=1)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Cabecalho>'
        xml += self.CodCidade.xml
        xml += self.Sucesso.xml
        xml += self.NumeroLote.xml
        xml += self.CPFCNPJRemetente.xml
        xml += self.RazaoSocialRemetente.xml
        xml += self.DataEnvioLote.xml
        xml += self.QtdNotasProcessadas.xml
        xml += self.TempoProcessamento.xml
        xml += self.ValorTotalServicos.xml
        xml += self.ValorTotalDeducoes.xml
        xml += self.Versao.xml
        xml += '</Cabecalho>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CodCidade.xml            = arquivo
            self.Sucesso.xml              = arquivo
            self.NumeroLote.xml           = arquivo
            self.CPFCNPJRemetente.xml     = arquivo
            self.RazaoSocialRemetente.xml = arquivo
            self.DataEnvioLote.xml        = arquivo
            self.QtdNotasProcessadas.xml  = arquivo
            self.TempoProcessamento.xml   = arquivo
            self.ValorTotalServicos.xml   = arquivo
            self.ValorTotalDeducoes.xml   = arquivo
            self.Versao.xml               = arquivo

    xml = property(get_xml, set_xml)


class RetornoConsultaLote(XMLNFe):
    def __init__(self):
        super(RetornoConsultaLote, self).__init__()
        self.caminho_esquema  = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema  = 'RetornoConsultaLote.xsd'
        self.Cabecalho = _Cabecalho()
        self.Alertas   = []
        self.Erros     = []
        self.ListaNFSe = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<nfse:RetornoConsultaLote xmlns:nfse="http://localhost:8080/WsNFe2/lote">'
        xml += self.Cabecalho.xml
        
        if len(self.Alertas):
            xml += '<Alertas>'
            
            for a in self.Alertas:
                xml += a.xml

            xml += '</Alertas>'

        if len(self.Erros):
            xml += '<Erros>'
            
            for e in self.Erros:
                xml += e.xml

            xml += '</Erros>'
            
        if len(self.ListaNFSe):
            xml += '<ListaNFSe>'
            
            for c in self.ListaNFSe:
                xml += c.xml

            xml += '</ListaNFSe>'
            
                
        xml += '</nfse:RetornoConsultaLote>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Cabecalho.xml = arquivo

            alertas = self._le_nohs('//nfse:RetornoConsultaLote/Alertas/Alerta')
            self.Alertas = []
            if alertas is not None:
                self.Alertas = [Alerta() for a in alertas]
                for i in range(len(alertas)):
                    self.Alertas[i].xml = alertas[i]

            erros = self._le_nohs('//nfse:RetornoConsultaLote/Erros/Erro')
            self.Erros = []
            if erros is not None:
                self.Erros = [Erro() for e in erros]
                for i in range(len(erros)):
                    self.Erros[i].xml = erros[i]

            consultas = self._le_nohs('//nfse:RetornoConsultaLote/ListaNFSe/ConsultaNFSe')
            self.ListaNFSe = []
            if consultas is not None:
                self.ListaNFSe = [ConsultaNFSe() for c in consultas]
                for i in range(len(consultas)):
                    self.ListaNFSe[i].xml = consultas[i]

    xml = property(get_xml, set_xml)
