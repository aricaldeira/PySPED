# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import *
from pysped.nfse.versao_100 import ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


class _Cabecalho(XMLNFe):
    def __init__(self):
        super(_Cabecalho, self).__init__()
        self.CodCidade        = TagInteiro(nome='CodCidade'        , tamanho=[ 1, 10, 1], raiz='//nfse:ReqConsultaLote/Cabecalho')
        self.CPFCNPJRemetente = TagCaracter(nome='CPFCNPJRemetente', tamanho=[11, 14]   , raiz='//nfse:ReqConsultaLote/Cabecalho')
        self.Versao           = TagInteiro(nome='Versao'           , tamanho=[ 1,  3, 1], raiz='//nfse:ReqConsultaLote/Cabecalho', valor=1)
        self.NumeroLote       = TagInteiro(nome='NumeroLote'       , tamanho=[ 1, 12, 1], raiz='//nfse:ReqConsultaLote/Cabecalho')
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Cabecalho>'
        xml += self.CodCidade.xml
        xml += self.CPFCNPJRemetente.xml
        xml += self.Versao.xml
        xml += self.NumeroLote.xml
        xml += '</Cabecalho>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CodCidade.xml        = arquivo
            self.CPFCNPJRemetente.xml = arquivo
            self.Versao.xml           = arquivo
            self.NumeroLote.xml       = arquivo

    xml = property(get_xml, set_xml)


class ReqConsultaLote(XMLNFe):
    def __init__(self):
        super(ReqConsultaLote, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'ReqConsultaLote.xsd'
        self.Cabecalho = _Cabecalho()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<nfse:ReqConsultaLote xmlns:nfse="http://localhost:8080/WsNFe2/lote">'
        xml += self.Cabecalho.xml
        xml += '</nfse:ReqConsultaLote>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Cabecalho.xml = arquivo

    xml = property(get_xml, set_xml)
