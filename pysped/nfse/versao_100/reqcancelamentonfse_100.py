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

from pysped.xml_sped import (ABERTURA, Signature, TagBoolean, TagCaracter,
                             TagInteiro, XMLNFe)
from pysped.nfse.versao_100 import ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


class NotaCancelamento(XMLNFe):
    def __init__(self):
        super(NotaCancelamento, self).__init__()
        self.Id = TagCaracter(nome='Nota', propriedade='Id', raiz='//')
        self.InscricaoMunicipalPrestador = TagCaracter(nome='InscricaoMunicipalPrestador', tamanho=[6,  11]   , raiz='//Nota')
        self.NumeroNota                  = TagInteiro(nome='NumeroNota'                  , tamanho=[1,  12, 1], raiz='//Nota')
        self.CodigoVerificacao           = TagCaracter(nome='CodigoVerificacao'          , tamanho=[1, 255]   , raiz='//Nota')
        self.MotivoCancelamento          = TagCaracter(nome='MotivoCancelamento'         , tamanho=[1,  80]   , raiz='//Nota')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.valor == '':
            self.Id.valor = 'nota:' + unicode(self.NumeroNota.valor)

        xml += self.Id.xml
        xml += self.InscricaoMunicipalPrestador.xml
        xml += self.NumeroNota.xml
        xml += self.CodigoVerificacao.xml
        xml += self.MotivoCancelamento.xml
        xml += '</Nota>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.InscricaoMunicipalPrestador.xml = arquivo
            self.NumeroNota.xml = arquivo
            self.CodigoVerificacao.xml = arquivo
            self.MotivoCancelamento.xml = arquivo

    xml = property(get_xml, set_xml)


class _Lote(XMLNFe):
    def __init__(self):
        super(_Lote, self).__init__()
        self.Id = TagCaracter(nome='Lote', propriedade=u'Id', raiz=u'//nfse:ReqCancelamentoNFSe')
        self.NotaCancelamento = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml

        if len(self.NotaCancelamento):
            for n in self.NotaCancelamento:
                xml += n.xml

        xml += '</Lote>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml        = arquivo

            notas = self._le_nohs('//nfse:ReqCancelamentoNFSe/Lote/Nota')
            self.NotaCancelamento = []
            if notas is not None:
                self.NotaCancelamento = [NotaCancelamento() for n in notas]
                for i in range(len(notas)):
                    self.NotaCancelamento[i].xml = notas[i]

    xml = property(get_xml, set_xml)


class _Cabecalho(XMLNFe):
    def __init__(self):
        super(_Cabecalho, self).__init__()
        self.CodCidade        = TagInteiro(nome='CodCidade'        , tamanho=[ 1, 10, 1], raiz='//nfse:ReqCancelamentoNFSe/Cabecalho')
        self.CPFCNPJRemetente = TagCaracter(nome='CPFCNPJRemetente', tamanho=[11, 14]   , raiz='//nfse:ReqCancelamentoNFSe/Cabecalho')
        self.transacao        = TagBoolean(nome='transacao'        ,                      raiz='//nfse:ReqCancelamentoNFSe/Cabecalho', valor=True)
        self.Versao           = TagInteiro(nome='Versao'           , tamanho=[ 1,  3, 1], raiz='//nfse:ReqCancelamentoNFSe/Cabecalho', valor=1)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Cabecalho>'
        xml += self.CodCidade.xml
        xml += self.CPFCNPJRemetente.xml
        xml += self.transacao.xml
        xml += self.Versao.xml
        xml += '</Cabecalho>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CodCidade.xml        = arquivo
            self.CPFCNPJRemetente.xml = arquivo
            self.transacao.xml        = arquivo
            self.Versao.xml           = arquivo

    xml = property(get_xml, set_xml)


class ReqCancelamentoNFSe(XMLNFe):
    def __init__(self):
        super(ReqCancelamentoNFSe, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'ReqCancelamentoNFSe.xsd'
        self.Cabecalho = _Cabecalho()
        self.Lote = _Lote()
        self.Signature = Signature()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<nfse:ReqCancelamentoNFSe xmlns:nfse="http://localhost:8080/WsNFe2/lote">'
        xml += self.Cabecalho.xml
        xml += self.Lote.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.Lote.Id.valor

        xml += self.Signature.xml

        xml += '</nfse:ReqCancelamentoNFSe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Cabecalho.xml = arquivo
            self.Lote.xml = arquivo
            self.Signature.xml = self._le_noh('//nfse:ReqCancelamentoNFSe/sig:Signature')

    xml = property(get_xml, set_xml)
