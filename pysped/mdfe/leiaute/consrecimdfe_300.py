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

from pysped.xml_sped import (ABERTURA, NAMESPACE_MDFE, Signature, TagCaracter,
                             TagDataHora, TagDecimal, TagInteiro, XMLNFe, TagDataHoraUTC)
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_3 as ESQUEMA_ATUAL
import os
from .mdfe_300 import MDFe


DIRNAME = os.path.dirname(__file__)


class ConsReciMDFe(XMLNFe):
    def __init__(self):
        super(ConsReciMDFe, self).__init__()
        self.versao  = TagDecimal(nome='consReciMDFe', propriedade='versao', namespace=NAMESPACE_MDFE, valor='3.00', raiz='/')
        self.tpAmb   = TagInteiro(nome='tpAmb'       , tamanho=[1,   1, 1] , raiz='//consReciMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.nRec    = TagCaracter(nome='nRec'       , tamanho=[1, 15, 1]  , raiz='//consReciMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consReciMDFe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.nRec.xml
        xml += '</consReciMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.nRec.xml   = arquivo

        return self.xml

    xml = property(get_xml, set_xml)


class InfProt(XMLNFe):
    def __init__(self):
        super(InfProt, self).__init__()
        self.Id        = TagCaracter(nome='infProt' , propriedade='Id'   , raiz='/'        , obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.tpAmb     = TagInteiro(nome='tpAmb'    , tamanho=[1,   1, 1], raiz='//infProt', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.verAplic  = TagCaracter(nome='verAplic', tamanho=[1,  20]   , raiz='//infProt', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.chMDFe    = TagCaracter(nome='chMDFe'  , tamanho=[44, 44]   , raiz='//infProt', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.dhRecbto  = TagDataHoraUTC(nome='dhRecbto'                  , raiz='//infProt', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.nProt     = TagCaracter(nome='nProt'   , tamanho=[15, 15]   , raiz='//infProt', obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.digVal    = TagCaracter(nome='digVal'  , tamanho=[28, 28]   , raiz='//infProt', obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cStat     = TagCaracter(nome='cStat'   , tamanho=[1,   3]   , raiz='//infProt', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.xMotivo   = TagCaracter(nome='xMotivo' , tamanho=[1, 255]   , raiz='//infProt', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.valor:
            xml += self.Id.xml
        else:
            xml += '<infProt>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.chMDFe.xml
        xml += self.dhRecbto.xml
        xml += self.nProt.xml
        xml += self.digVal.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += '</infProt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml        = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.chMDFe.xml     = arquivo
            self.dhRecbto.xml  = arquivo
            self.nProt.xml     = arquivo
            self.digVal.xml    = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo

    xml = property(get_xml, set_xml)


class ProtMDFe(XMLNFe):
    def __init__(self):
        super(ProtMDFe, self).__init__()
        self.versao  = TagDecimal(nome='protMDFe', propriedade='versao', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, valor='3.00', raiz='/')
        self.infProt = InfProt()
        self.Signature = Signature()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.infProt.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != '#'):
            xml += self.Signature.xml

        xml += '</protMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            #
            # o grupo infProt é usado também no webservice de consulta da situação de uma NF-e
            # por isso, a raiz dele não pode ser assumida como sendo sempre o grupo
            # protMDFe
            #
            self.infProt.xml = self._le_noh('//protMDFe/infProt', ns=NAMESPACE_MDFE)
            self.Signature.xml = self._le_noh('//protMDFe/sig:Signature')

    xml = property(get_xml, set_xml)

    @property
    def protocolo_formatado(self):
        if not self.infProt.nProt.valor:
            return ''

        formatado = self.infProt.nProt.valor
        formatado += ' - '
        formatado += self.infProt.dhRecbto.formato_danfe
        return formatado


class RetConsReciMDFe(XMLNFe):
    def __init__(self):
        super(RetConsReciMDFe, self).__init__()
        self.versao   = TagDecimal(nome='retConsReciMDFe', propriedade='versao', namespace=NAMESPACE_MDFE, valor='3.00', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'          , tamanho=[1,   1, 1], raiz='//retConsReciMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.verAplic = TagCaracter(nome='verAplic'      , tamanho=[1,  20]   , raiz='//retConsReciMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.nRec     = TagCaracter(nome='nRec'          , tamanho=[1, 15, 1] , raiz='//retConsReciMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cStat    = TagCaracter(nome='cStat'         , tamanho=[1,   3]   , raiz='//retConsReciMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.xMotivo  = TagCaracter(nome='xMotivo'       , tamanho=[1, 255]   , raiz='//retConsReciMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cUF      = TagCaracter(nome='cUF'           , tamanho=[2,   2, 2], raiz='//retConsReciMDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.protMDFe  = []

        #
        # Dicionário dos protocolos, com a chave sendo a chave de NF-e
        #
        self.dic_protMDFe = {}
        #
        # Dicionário dos processos (NF-e + protocolo), com a chave sendo a chave da NF-e
        #
        self.dic_procMDFe = {}

        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsReciMDFe_v3.00.xsd'


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.nRec.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml

        for pn in self.protMDFe:
            xml += pn.xml

        xml += '</retConsReciMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.tpAmb.xml    = arquivo
            self.verAplic.xml = arquivo
            self.nRec.xml     = arquivo
            self.cStat.xml    = arquivo
            self.xMotivo.xml  = arquivo
            self.cUF.xml      = arquivo
            self.protMDFe      = self.le_grupo('//retConsReciMDFe/protMDFe', ProtMDFe, sigla_ns='mdfe')

            #
            # Monta o dicionário dos protocolos
            #
            for pn in self.protMDFe:
                self.dic_protMDFe[pn.infProt.chMDFe.valor] = pn

    xml = property(get_xml, set_xml)


class ProcMDFe(XMLNFe):
    def __init__(self):
        super(ProcMDFe, self).__init__()
        self.versao  = TagDecimal(nome='nfeProc', propriedade='versao', namespace=NAMESPACE_MDFE, valor='3.00', raiz='/')
        self.MDFe     = MDFe()
        self.protMDFe = ProtMDFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procMDFe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.MDFe.xml.replace(ABERTURA, '')
        xml += self.protMDFe.xml.replace(ABERTURA, '')
        xml += '</nfeProc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.MDFe.xml     = arquivo
            self.protMDFe.xml = arquivo

    xml = property(get_xml, set_xml)
