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
        self.CodCid           = TagInteiro(nome='CodCid'           , tamanho=[ 1, 10, 1], raiz='//nfse:ConsultaSeqRps/Cabecalho')
        self.IMPrestador      = TagCaracter(nome='IMPrestador'     , tamanho=[ 6, 11]   , raiz='//nfse:ConsultaSeqRps/Cabecalho')
        self.CPFCNPJRemetente = TagCaracter(nome='CPFCNPJRemetente', tamanho=[11, 14]   , raiz='//nfse:ConsultaSeqRps/Cabecalho')
        self.SeriePrestacao   = TagCaracter(nome='SeriePrestacao'  , tamanho=[ 2,  2]   , raiz='//nfse:ConsultaSeqRps/Cabecalho', valor='99', obrigatorio=False)
        self.Versao           = TagInteiro(nome='Versao'           , tamanho=[ 1,  3, 1], raiz='//nfse:ConsultaSeqRps/Cabecalho', valor=1)
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Cabecalho>'
        xml += self.CodCid.xml
        xml += self.IMPrestador.xml
        xml += self.CPFCNPJRemetente.xml
        xml += self.SeriePrestacao.xml
        xml += self.Versao.xml
        xml += '</Cabecalho>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CodCid.xml           = arquivo
            self.IMPrestador.xml      = arquivo
            self.CPFCNPJRemetente.xml = arquivo
            self.SeriePrestacao.xml   = arquivo
            self.Versao.xml           = arquivo

    xml = property(get_xml, set_xml)


class ConsultaSeqRPS(XMLNFe):
    def __init__(self):
        super(ConsultaSeqRPS, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'ConsultaSeqRps.xsd'
        self.Cabecalho = _Cabecalho()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<nfse:ConsultaSeqRps xmlns:nfse="http://localhost:8080/WsNFe2/lote" xmlns:tipos="http://localhost:8080/WsNFe2/tp" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://localhost:8080/WsNFe2/lote http://localhost:8080/WsNFe2/xsd/ConsultaSeqRps.xsd">'
        xml += self.Cabecalho.xml
        xml += '</nfse:ConsultaSeqRps>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Cabecalho.xml = arquivo

    xml = property(get_xml, set_xml)
