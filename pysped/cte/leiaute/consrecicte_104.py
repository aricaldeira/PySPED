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

from pysped.xml_sped import (ABERTURA, NAMESPACE_CTE, Signature, TagCaracter,
                             TagDataHora, TagDecimal, TagInteiro, XMLNFe)
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_104 as ESQUEMA_ATUAL
import os
from .cte_104 import CTe


DIRNAME = os.path.dirname(__file__)


class ConsReciCTe(XMLNFe):
    def __init__(self):
        super(ConsReciCTe, self).__init__()
        self.versao  = TagDecimal(nome='consReciCTe', codigo='BP02', propriedade='versao', namespace=NAMESPACE_CTE, valor='1.04', raiz='/')
        self.tpAmb   = TagInteiro(nome='tpAmb'      , codigo='BP03', tamanho=[1,   1, 1]  , raiz='//consReciCTe')
        self.nRec    = TagCaracter(nome='nRec'      , codigo='BP04', tamanho=[1, 15, 1]   , raiz='//consReciCTe')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consReciCte_v1.04.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.nRec.xml
        xml += '</consReciCTe>'
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
        self.Id        = TagCaracter(nome='infProt' , codigo='PR04', propriedade='Id'  , raiz='/'        , obrigatorio=False, namespace=NAMESPACE_CTE)
        self.tpAmb     = TagInteiro(nome='tpAmb'    , codigo='PR05', tamanho=[1,   1, 1], raiz='//infProt', namespace=NAMESPACE_CTE)
        self.verAplic  = TagCaracter(nome='verAplic', codigo='PR06', tamanho=[1,  20]   , raiz='//infProt', namespace=NAMESPACE_CTE)
        self.chCTe     = TagCaracter(nome='chCTe'   , codigo='PR07', tamanho=[44, 44]   , raiz='//infProt', namespace=NAMESPACE_CTE)
        self.dhRecbto  = TagDataHora(nome='dhRecbto', codigo='PR08'                     , raiz='//infProt', namespace=NAMESPACE_CTE)
        self.nProt     = TagCaracter(nome='nProt'   , codigo='PR09', tamanho=[15, 15]   , raiz='//infProt', obrigatorio=False, namespace=NAMESPACE_CTE)
        self.digVal    = TagCaracter(nome='digVal'  , codigo='PR10', tamanho=[28, 28]   , raiz='//infProt', obrigatorio=False, namespace=NAMESPACE_CTE)
        self.cStat     = TagCaracter(nome='cStat'   , codigo='PR11' , tamanho=[1,   3]  , raiz='//infProt', namespace=NAMESPACE_CTE)
        self.xMotivo   = TagCaracter(nome='xMotivo' , codigo='PR12' , tamanho=[1, 255]  , raiz='//infProt', namespace=NAMESPACE_CTE)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.valor:
            xml += self.Id.xml
        else:
            xml += '<infProt>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.chCTe.xml
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
            self.chCTe.xml     = arquivo
            self.dhRecbto.xml  = arquivo
            self.nProt.xml     = arquivo
            self.digVal.xml    = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo

    xml = property(get_xml, set_xml)


class ProtCTe(XMLNFe):
    def __init__(self):
        super(ProtCTe, self).__init__()
        self.versao  = TagDecimal(nome='protCTe', codigo='PR02' , propriedade='versao', namespace=NAMESPACE_CTE, valor='1.04', raiz='/')
        self.infProt = InfProt()
        self.Signature = Signature()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.infProt.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != '#'):
            xml += self.Signature.xml

        xml += '</protCTe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            #
            # o grupo infProt é usado também no webservice de consulta da situação de uma NF-e
            # por isso, a raiz dele não pode ser assumida como sendo sempre o grupo
            # protCTe
            #
            self.infProt.xml = self._le_noh('//protCTe/infProt', ns=NAMESPACE_CTE)
            self.Signature.xml = self._le_noh('//protCTe/sig:Signature')

    xml = property(get_xml, set_xml)

    def protocolo_formatado(self):
        if not self.infProt.nProt.valor:
            return ''

        formatado = self.infProt.nProt.valor
        formatado += ' - '
        formatado += self.infProt.dhRecbto.formato_danfe()
        return formatado


class RetConsReciCTe(XMLNFe):
    def __init__(self):
        super(RetConsReciCTe, self).__init__()
        self.versao   = TagDecimal(nome='retConsReciCTe', codigo='BR02' , propriedade='versao', namespace=NAMESPACE_CTE, valor='1.04', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'         , codigo='BR03' , tamanho=[1,   1, 1], raiz='//retConsReciCTe')
        self.verAplic = TagCaracter(nome='verAplic'     , codigo='BR04' , tamanho=[1,  20]   , raiz='//retConsReciCTe')
        self.nRec     = TagCaracter(nome='nRec'         , codigo='BR04a', tamanho=[1, 15, 1] , raiz='//retConsReciCTe')
        self.cStat    = TagCaracter(nome='cStat'        , codigo='BR05' , tamanho=[1,   3]   , raiz='//retConsReciCTe')
        self.xMotivo  = TagCaracter(nome='xMotivo'      , codigo='BR06' , tamanho=[1, 255]   , raiz='//retConsReciCTe')
        self.cUF      = TagCaracter(nome='cUF'          , codigo='BR06a', tamanho=[2,   2, 2], raiz='//retConsReciCTe')
        self.protCTe  = []

        #
        # Dicionário dos protocolos, com a chave sendo a chave de NF-e
        #
        self.dic_protCTe = {}
        #
        # Dicionário dos processos (NF-e + protocolo), com a chave sendo a chave da NF-e
        #
        self.dic_procCTe = {}

        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsReciCte_v1.04.xsd'


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.nRec.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml

        for pn in self.protCTe:
            xml += pn.xml

        xml += '</retConsReciCTe>'
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
            self.protCTe      = self.le_grupo('//retConsReciCTe/protCTe', ProtCTe)

            #
            # Monta o dicionário dos protocolos
            #
            for pn in self.protCTe:
                self.dic_protCTe[pn.infProt.chCTe.valor] = pn

    xml = property(get_xml, set_xml)


class ProcCTe(XMLNFe):
    def __init__(self):
        super(ProcCTe, self).__init__()
        self.versao  = TagDecimal(nome='cteProc', propriedade='versao', namespace=NAMESPACE_CTE, valor='1.04', raiz='/')
        self.CTe     = CTe()
        self.protCTe = ProtCTe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procCTe_v1.04.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.CTe.xml.replace(ABERTURA, '')
        xml += self.protCTe.xml.replace(ABERTURA, '')
        xml += '</cteProc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CTe.xml     = arquivo
            self.protCTe.xml = self._le_noh('//cteProc/protCTe', ns=NAMESPACE_CTE)

    xml = property(get_xml, set_xml)
