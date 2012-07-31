# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import *
from pysped.nfse.versao_100 import ESQUEMA_ATUAL
import os
from lxml.etree import tounicode

DIRNAME = os.path.dirname(__file__)


class _Cabecalho(XMLNFe):
    def __init__(self):
        super(_Cabecalho, self).__init__()
        self.CodCidade        = TagInteiro(nome='CodCidade'        , tamanho=[ 1, 10, 1], raiz='//nfse:ReqConsultaNotas/Cabecalho')
        self.CPFCNPJRemetente = TagCaracter(nome='CPFCNPJRemetente', tamanho=[11, 14]   , raiz='//nfse:ReqConsultaNotas/Cabecalho')
        self.InscricaoMunicipalPrestador  = TagCaracter(nome='InscricaoMunicipalPrestador'     , tamanho=[ 6, 11]   , raiz='//nfse:ReqConsultaNotas/Cabecalho')
        self.dtInicio         = TagData(nome='dtInicio', raiz='//nfse:ReqConsultaNotas/Cabecalho')
        self.dtFim            = TagData(nome='dtFim', raiz='//nfse:ReqConsultaNotas/Cabecalho')
        self.NotaInicial      = TagInteiro(nome='NotaInicial'      , tamanho=[ 1, 12, 1], raiz='//nfse:ReqConsultaNotas/Cabecalho', obrigatorio=False)
        self.Versao           = TagInteiro(nome='Versao'           , tamanho=[ 1,  3, 1], raiz='//nfse:ReqConsultaNotas/Cabecalho', valor=1)
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Cabecalho>'
        xml += self.CodCidade.xml
        xml += self.CPFCNPJRemetente.xml
        xml += self.InscricaoMunicipalPrestador.xml
        xml += self.dtInicio.xml
        xml += self.dtFim.xml
        xml += self.NotaInicial.xml
        xml += self.Versao.xml
        xml += '</Cabecalho>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CodCidade.xml        = arquivo
            self.CPFCNPJRemetente.xml = arquivo
            self.InscricaoMunicipalPrestador.xml = arquivo
            self.dtInicio.xml         = arquivo
            self.dtFim.xml            = arquivo
            self.NotaInicial.xml      = arquivo
            self.Versao.xml           = arquivo

    xml = property(get_xml, set_xml)


class ReqConsultaNotas(XMLNFe):
    def __init__(self):
        super(ReqConsultaNotas, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'ReqConsultaNotas.xsd'
        self.Cabecalho = _Cabecalho()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<nfse:ReqConsultaNotas xmlns:nfse="http://localhost:8080/WsNFe2/lote" xmlns:tipos="http://localhost:8080/WsNFe2/tp" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://localhost:8080/WsNFe2/lote http://localhost:8080/WsNFe2/xsd/ReqConsultaNotas.xsd">'
        xml += self.Cabecalho.xml
        xml += '</nfse:ReqConsultaNotas>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Cabecalho.xml = arquivo

    xml = property(get_xml, set_xml)
