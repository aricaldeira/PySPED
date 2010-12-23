# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import *
from pysped.nfse.versao_100 import ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


class ChaveNFe(XMLNFe):
    def __init__(self):
        super(ChaveNFe, self).__init__()
        self.InscricaoPrestador   = TagCaracter(nome='InscricaoPrestador'  , tamanho=[ 6,  11]   , raiz='//*/ChaveNFe')
        self.NumeroNFe            = TagInteiro(nome='NumeroNFe'            , tamanho=[ 1,  12, 1], raiz='//*/ChaveNFe')
        self.CodigoVerificacao    = TagCaracter(nome='CodigoVerificacao'   , tamanho=[ 1, 255]   , raiz='//*/ChaveNFe')
        self.RazaoSocialPrestador = TagCaracter(nome='RazaoSocialPrestador', tamanho=[ 1, 120]   , raiz='//*/ChaveNFe')
        
    def get_xml(self):
        if self.InscricaoPrestador.valor.strip() == '':
            return ''
        
        xml = XMLNFe.get_xml(self)
        xml += '<ChaveNFe>'
        xml += self.InscricaoPrestador.xml
        xml += self.NumeroNFe.xml
        xml += self.CodigoVerificacao.xml
        xml += self.RazaoSocialPrestador.xml
        xml += '</ChaveNFe>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.InscricaoPrestador.xml   = arquivo
            self.NumeroNFe.xml            = arquivo
            self.CodigoVerificacao.xml       = arquivo
            self.RazaoSocialPrestador.xml = arquivo
        
    xml = property(get_xml, set_xml)


class ChaveRPS(XMLNFe):
    def __init__(self):
        super(ChaveRPS, self).__init__()
        self.InscricaoPrestador   = TagCaracter(nome='InscricaoPrestador'  , tamanho=[ 6,  11]   , raiz='//*/ChaveRPS')
        self.SerieRPS             = TagCaracter(nome='SerieRPS'            , tamanho=[ 2,   2]   , raiz='//*/ChaveRPS', valor='NF')
        self.NumeroRPS            = TagInteiro(nome='NumeroRPS'            , tamanho=[ 1,  12, 1], raiz='//*/ChaveRPS')
        self.DataEmissaoRPS       = TagDataHora(nome='DataEmissaoRPS'                            , raiz='//*/ChaveRPS')
        self.RazaoSocialPrestador = TagCaracter(nome='RazaoSocialPrestador', tamanho=[ 1, 120]   , raiz='//*/ChaveRPS')
        
    def get_xml(self):
        if self.InscricaoPrestador.valor.strip() == '':
            return ''
            
        xml = XMLNFe.get_xml(self)
        xml += '<ChaveRPS>'
        xml += self.InscricaoPrestador.xml
        xml += self.SerieRPS.xml
        xml += self.NumeroRPS.xml
        xml += self.DataEmissaoRPS.xml
        xml += self.RazaoSocialPrestador.xml
        xml += '</ChaveRPS>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.InscricaoPrestador.xml   = arquivo
            self.SerieRPS.xml             = arquivo
            self.NumeroRPS.xml            = arquivo
            self.DataEmissaoRPS.xml       = arquivo
            self.RazaoSocialPrestador.xml = arquivo
        
    xml = property(get_xml, set_xml)


class Alerta(XMLNFe):
    def __init__(self):
        super(Alerta, self).__init__()
        self.Codigo    = TagInteiro(nome='Codigo'    , tamanho=[3, 4, 3], raiz='//Alerta')
        self.Descricao = TagCaracter(nome='Descricao', tamanho=[0, 300] , raiz='//Alerta')
        self.ChaveRPS = ChaveRPS()
        self.ChaveNFe = ChaveNFe()
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Alerta>'
        xml += self.Codigo.xml
        xml += self.Descricao.xml
        xml += self.ChaveRPS.xml
        xml += self.ChaveNFe.xml
        xml += '</Alerta>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Codigo.xml    = arquivo
            self.Descricao.xml = arquivo
            self.ChaveRPS.xml  = arquivo
            self.ChaveNFe.xml  = arquivo
        
    xml = property(get_xml, set_xml)
    
    
class Erro(XMLNFe):
    def __init__(self):
        super(Erro, self).__init__()
        self.Codigo    = TagInteiro(nome='Codigo'    , tamanho=[3, 4, 3], raiz='//Erro')
        self.Descricao = TagCaracter(nome='Descricao', tamanho=[0, 300] , raiz='//Erro')
        self.ChaveRPS = ChaveRPS()
        self.ChaveNFe = ChaveNFe()
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Erro>'
        xml += self.Codigo.xml
        xml += self.Descricao.xml
        xml += self.ChaveRPS.xml
        xml += self.ChaveNFe.xml
        xml += '</Erro>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Codigo.xml    = arquivo
            self.Descricao.xml = arquivo
            self.ChaveRPS.xml  = arquivo
            self.ChaveNFe.xml  = arquivo
        
    xml = property(get_xml, set_xml)
