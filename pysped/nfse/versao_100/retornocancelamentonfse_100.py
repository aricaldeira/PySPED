# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import *
from pysped.nfse.versao_100 import ESQUEMA_ATUAL
from pysped.nfse.versao_100.evento_100 import Alerta, Erro
from pysped.nfse.versao_100.reqcancelamentonfse_100 import NotaCancelamento
import os

DIRNAME = os.path.dirname(__file__)


class _Cabecalho(XMLNFe):    
    def __init__(self):
        super(_Cabecalho, self).__init__()
        self.CodCidade            = TagInteiro(nome='CodCidade'            , tamanho=[ 1, 10, 1], raiz='//nfse:RetornoCancelamentoNFSe/Cabecalho')
        self.Sucesso              = TagBoolean(nome='Sucesso'                                   , raiz='//nfse:RetornoCancelamentoNFSe/Cabecalho')
        self.CPFCNPJRemetente     = TagCaracter(nome='CPFCNPJRemetente'    , tamanho=[11, 14]   , raiz='//nfse:RetornoCancelamentoNFSe/Cabecalho')
        self.Versao               = TagInteiro(nome='Versao'               , tamanho=[ 1,  3, 1], raiz='//nfse:RetornoCancelamentoNFSe/Cabecalho', valor=1)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Cabecalho>'
        xml += self.CodCidade.xml
        xml += self.Sucesso.xml
        xml += self.CPFCNPJRemetente.xml
        xml += self.Versao.xml
        xml += '</Cabecalho>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CodCidade.xml            = arquivo
            self.Sucesso.xml              = arquivo
            self.CPFCNPJRemetente.xml     = arquivo
            self.Versao.xml               = arquivo

    xml = property(get_xml, set_xml)


class RetornoCancelamentoNFSe(XMLNFe):
    def __init__(self):
        super(RetornoCancelamentoNFSe, self).__init__()
        self.caminho_esquema  = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema  = 'RetornoCancelamentoNFSe.xsd'
        self.Cabecalho = _Cabecalho()
        self.NotasCanceladas = []
        self.Alertas   = []
        self.Erros     = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<nfse:RetornoCancelamentoNFSe xmlns:nfse="http://localhost:8080/WsNFe2/lote">'
        xml += self.Cabecalho.xml

        if len(self.NotasCanceladas):
            xml += '<NotasCanceladas>'
            
            for n in self.NotasCanceladas:
                xml += n.xml

            xml += '</NotasCanceladas>'
        
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
            
        xml += '</nfse:RetornoCancelamentoNFSe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Cabecalho.xml = arquivo

            alertas = self._le_nohs('//nfse:RetornoCancelamentoNFSe/Alertas/Alerta')
            self.Alertas = []
            if alertas is not None:
                self.Alertas = [Alerta() for a in alertas]
                for i in range(len(alertas)):
                    self.Alertas[i].xml = alertas[i]

            erros = self._le_nohs('//nfse:RetornoCancelamentoNFSe/Erros/Erro')
            self.Erros = []
            if erros is not None:
                self.Erros = [Erro() for e in erros]
                for i in range(len(erros)):
                    self.Erros[i].xml = erros[i]

            notas = self._le_nohs('//nfse:RetornoCancelamentoNFSe/NotasCanceladas/Nota')
            self.NotasCanceladas = []
            if notas is not None:
                self.NotasCanceladas = [NotaCancelamento() for n in notas]
                for i in range(len(notas)):
                    self.NotasCanceladas[i].xml = notas[i]

    xml = property(get_xml, set_xml)
