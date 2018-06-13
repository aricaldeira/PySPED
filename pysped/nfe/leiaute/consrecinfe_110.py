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

from pysped.xml_sped import (ABERTURA, NAMESPACE_NFE, Signature, TagCaracter,
                             TagDataHora, TagDecimal, TagInteiro, XMLNFe, TagDataHoraUTC)
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_1 as ESQUEMA_ATUAL
import os
from .nfe_110 import NFe


DIRNAME = os.path.dirname(__file__)


class ConsReciNFe(XMLNFe):
    def __init__(self):
        super(ConsReciNFe, self).__init__()
        self.versao  = TagDecimal(nome='consReciNFe', codigo='BP02', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.10', raiz='/')
        self.tpAmb   = TagInteiro(nome='tpAmb'      , codigo='BP03', tamanho=[1,   1, 1]  , raiz='//consReciNFe')
        self.nRec    = TagCaracter(nome='nRec'      , codigo='BP04', tamanho=[1, 15, 1]   , raiz='//consReciNFe')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consReciNFe_v1.10.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.nRec.xml
        xml += '</consReciNFe>'
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
        self.Id        = TagCaracter(nome='infProt' , codigo='PR04', propriedade='Id'  , raiz='/'        , obrigatorio=False)
        self.tpAmb     = TagInteiro(nome='tpAmb'    , codigo='PR05', tamanho=[1,   1, 1], raiz='//infProt')
        self.verAplic  = TagCaracter(nome='verAplic', codigo='PR06', tamanho=[1,  20]   , raiz='//infProt')
        self.chNFe     = TagCaracter(nome='chNFe'   , codigo='PR07', tamanho=[44, 44]   , raiz='//infProt')
        self.dhRecbto  = TagDataHoraUTC(nome='dhRecbto', codigo='PR08'                     , raiz='//infProt')
        self.nProt     = TagCaracter(nome='nProt'   , codigo='PR09', tamanho=[15, 15]   , raiz='//infProt', obrigatorio=False)
        self.digVal    = TagCaracter(nome='digVal'  , codigo='PR10', tamanho=[28, 28]   , raiz='//infProt', obrigatorio=False)
        self.cStat     = TagCaracter(nome='cStat'   , codigo='PR11' , tamanho=[1,   3]  , raiz='//infProt')
        self.xMotivo   = TagCaracter(nome='xMotivo' , codigo='PR12' , tamanho=[1, 255]  , raiz='//infProt')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.valor:
            xml += self.Id.xml
        else:
            xml += '<infProt>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.chNFe.xml
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
            self.chNFe.xml     = arquivo
            self.dhRecbto.xml  = arquivo
            self.nProt.xml     = arquivo
            self.digVal.xml    = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo

    xml = property(get_xml, set_xml)


class ProtNFe(XMLNFe):
    def __init__(self):
        super(ProtNFe, self).__init__()
        self.versao  = TagDecimal(nome='protNFe', codigo='PR02' , propriedade='versao', namespace=NAMESPACE_NFE, valor='1.10', raiz='/')
        self.infProt = InfProt()
        self.Signature = Signature()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.infProt.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != '#'):
            xml += self.Signature.xml

        xml += '</protNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            #
            # o grupo infProt é usado também no webservice de consulta da situação de uma NF-e
            # por isso, a raiz dele não pode ser assumida como sendo sempre o grupo
            # protNFe
            #
            self.infProt.xml = self._le_noh('//protNFe/infProt')
            self.Signature.xml = self._le_noh('//protNFe/sig:Signature')

    xml = property(get_xml, set_xml)

    @property
    def protocolo_formatado(self):
        if not self.infProt.nProt.valor:
            return ''

        formatado = self.infProt.nProt.valor
        formatado += ' - '
        formatado += self.infProt.dhRecbto.formato_danfe
        return formatado


class RetConsReciNFe(XMLNFe):
    def __init__(self):
        super(RetConsReciNFe, self).__init__()
        self.versao   = TagDecimal(nome='retConsReciNFe', codigo='BR02' , propriedade='versao', namespace=NAMESPACE_NFE, valor='1.10', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'         , codigo='BR03' , tamanho=[1,   1, 1], raiz='//retConsReciNFe')
        self.verAplic = TagCaracter(nome='verAplic'     , codigo='BR04' , tamanho=[1,  20]   , raiz='//retConsReciNFe')
        self.nRec     = TagCaracter(nome='nRec'         , codigo='BR04a', tamanho=[1, 15, 1] , raiz='//retConsReciNFe')
        self.cStat    = TagCaracter(nome='cStat'        , codigo='BR05' , tamanho=[1,   3]   , raiz='//retConsReciNFe')
        self.xMotivo  = TagCaracter(nome='xMotivo'      , codigo='BR06' , tamanho=[1, 255]   , raiz='//retConsReciNFe')
        self.cUF      = TagCaracter(nome='cUF'          , codigo='BR06a', tamanho=[2,   2, 2], raiz='//retConsReciNFe')
        self.protNFe  = []

        #
        # Dicionário dos protocolos, com a chave sendo a chave de NF-e
        #
        self.dic_protNFe = {}
        #
        # Dicionário dos processos (NF-e + protocolo), com a chave sendo a chave da NF-e
        #
        self.dic_procNFe = {}

        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsReciNFe_v1.10.xsd'


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.nRec.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml

        for pn in self.protNFe:
            xml += pn.xml

        xml += '</retConsReciNFe>'
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
            self.protNFe      = self.le_grupo('//retConsReciNFe/protNFe', ProtNFe)

            #
            # Monta o dicionário dos protocolos
            #
            for pn in self.protNFe:
                self.dic_protNFe[pn.infProt.chNFe.valor] = pn

    xml = property(get_xml, set_xml)


class ProcNFe(XMLNFe):
    def __init__(self):
        super(ProcNFe, self).__init__()
        self.versao  = TagDecimal(nome='nfeProc', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.10', raiz='/')
        self.NFe     = NFe()
        self.protNFe = ProtNFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procNFe_v1.10.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.NFe.xml.replace(ABERTURA, '')
        xml += self.protNFe.xml.replace(ABERTURA, '')
        xml += '</nfeProc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.NFe.xml     = arquivo
            self.protNFe.xml = arquivo

    xml = property(get_xml, set_xml)
