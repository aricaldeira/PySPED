# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Affero General Public License,
# publicada pela Free Software Foundation, em sua versão 3 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Affero General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Affero General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import *
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_1 as ESQUEMA_ATUAL
import os


DIRNAME = os.path.dirname(__file__)


class ConsSitNFe(XMLNFe):
    def __init__(self):
        super(ConsSitNFe, self).__init__()
        self.versao = TagDecimal(nome='consSitNFe', codigo='EP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.07', raiz='/')
        self.tpAmb  = TagInteiro(nome='tpAmb'     , codigo='EP03', tamanho=[ 1,  1, 1], raiz='//consSitNFe', valor=2)
        self.xServ  = TagCaracter(nome='xServ'    , codigo='EP04', tamanho=[ 9,  9]   , raiz='//consSitNFe', valor='CONSULTAR')
        self.chNFe  = TagCaracter(nome='chNFe'    , codigo='EP05', tamanho=[44, 44]   , raiz='//consSitNFe')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consSitNFe_v1.07.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.chNFe.xml
        xml += '</consSitNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml  = arquivo
            self.chNFe.xml  = arquivo

    xml = property(get_xml, set_xml)


class InfProt(XMLNFe):
    '''Atenção!!!

    Este grupo infProt é DIFERENTE do infProt do retorno do recibo do lote

    Colocar esse infProt dentro do arquivo procNFe vai fazer com que o procNFe gerado
    seja INVALIDADO pelo XSD!!!

    Para transportar os valores desta infProt para a infProt do procNFe, é preciso usar

    procNFe.protNFe.infProt.xml = este_infProt.xml

    '''
    def __init__(self):
        super(InfProt, self).__init__()
        self.Id        = TagCaracter(nome='infProt' , codigo='ER04' , propriedade='Id'  , raiz='/'        , obrigatorio=False)
        self.tpAmb     = TagInteiro(nome='tpAmb'    , codigo='ER05' , tamanho=[1,   1, 1], raiz='//infProt')
        self.verAplic  = TagCaracter(nome='verAplic', codigo='ER06' , tamanho=[1,  20]   , raiz='//infProt')
        self.cStat     = TagCaracter(nome='cStat'   , codigo='ER07' , tamanho=[1,   3]   , raiz='//infProt')
        self.xMotivo   = TagCaracter(nome='xMotivo' , codigo='ER08' , tamanho=[1, 2000]  , raiz='//infProt')
        self.cUF       = TagInteiro(nome='cUF'      , codigo='ER08a', tamanho=[2,   2, 2], raiz='//infProt')
        self.chNFe     = TagCaracter(nome='chNFe'   , codigo='ER09' , tamanho=[44, 44]   , raiz='//infProt', obrigatorio=False)
        self.dhRecbto  = TagDataHora(nome='dhRecbto', codigo='ER10'                      , raiz='//infProt', obrigatorio=False)
        self.nProt     = TagCaracter(nome='nProt'   , codigo='ER11' , tamanho=[15, 15]   , raiz='//infProt', obrigatorio=False)
        self.digVal    = TagCaracter(nome='digVal'  , codigo='ER12' , tamanho=[28, 28]   , raiz='//infProt', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.valor:
            xml += self.Id.xml
        else:
            xml += '<infProt>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.chNFe.xml
        xml += self.dhRecbto.xml
        xml += self.nProt.xml
        xml += self.digVal.xml
        xml += '</infProt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml        = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.cUF.xml       = arquivo
            self.chNFe.xml     = arquivo
            self.dhRecbto.xml  = arquivo
            self.nProt.xml     = arquivo
            self.digVal.xml    = arquivo

    xml = property(get_xml, set_xml)


class RetConsSitNFe(XMLNFe):
    def __init__(self):
        super(RetConsSitNFe, self).__init__()
        self.versao    = TagDecimal(nome='retConsSitNFe', codigo='ER01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.07', raiz='/')
        self.infProt   = InfProt()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsSitNFe_v1.07.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infProt.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != '#'):
            xml += self.Signature.xml

        xml += '</retConsSitNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            #
            # o grupo infProt é usado também no webservice de consulta do recibo de lote de NF-e
            # por isso, a raiz dele não pode ser assumida como sendo sempre o grupo
            # retConsSitNFe
            #
            self.infProt.xml   = self._le_noh('//retConsSitNFe/infProt')
            self.Signature.xml = self._le_noh('//retConsSitNFe/sig:Signature')

    xml = property(get_xml, set_xml)
