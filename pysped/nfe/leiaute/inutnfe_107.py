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

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str

from pysped.xml_sped import (ABERTURA, NAMESPACE_NFE, Signature, TagCaracter,
                             TagDataHora, TagDecimal, TagInteiro, XMLNFe)
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_1 as ESQUEMA_ATUAL
import os


DIRNAME = os.path.dirname(__file__)


class InfInutEnviado(XMLNFe):
    def __init__(self):
        super(InfInutEnviado, self).__init__()
        self.Id     = TagCaracter(nome='infInut', codigo='DP03', tamanho=[41, 41] , raiz='//inutNFe', propriedade='Id')
        self.tpAmb  = TagInteiro(nome='tpAmb'   , codigo='DP05', tamanho=[1, 1, 1], raiz='//inutNFe/infInut', valor=2)
        self.xServ  = TagCaracter(nome='xServ'  , codigo='DP06', tamanho=[10, 10] , raiz='//inutNFe/infInut', valor='INUTILIZAR')
        self.cUF    = TagInteiro(nome='cUF'     , codigo='DP07', tamanho=[2, 2, 2], raiz='//inutNFe/infInut')
        self.ano    = TagCaracter(nome='ano'    , codigo='DP08', tamanho=[2, 2]   , raiz='//inutNFe/infInut')
        self.CNPJ   = TagCaracter(nome='CNPJ'   , codigo='DP09', tamanho=[3, 14]  , raiz='//inutNFe/infInut')
        self.mod    = TagInteiro(nome='mod'     , codigo='DP10', tamanho=[2, 2, 2], raiz='//inutNFe/infInut', valor=55)
        self.serie  = TagInteiro(nome='serie'   , codigo='DP11', tamanho=[1, 3]   , raiz='//inutNFe/infInut')
        self.nNFIni = TagInteiro(nome='nNFIni'  , codigo='DP12', tamanho=[1, 9]   , raiz='//inutNFe/infInut')
        self.nNFFin = TagInteiro(nome='nNFFin'  , codigo='DP13', tamanho=[1, 9]   , raiz='//inutNFe/infInut')
        self.xJust  = TagCaracter(nome='xJust'  , codigo='DP14', tamanho=[15, 255], raiz='//inutNFe/infInut')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.cUF.xml
        xml += self.ano.xml
        xml += self.CNPJ.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNFIni.xml
        xml += self.nNFFin.xml
        xml += self.xJust.xml
        xml += '</infInut>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml     = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml  = arquivo
            self.cUF.xml    = arquivo
            self.ano.xml    = arquivo
            self.CNPJ.xml   = arquivo
            self.mod.xml    = arquivo
            self.serie.xml  = arquivo
            self.nNFIni.xml = arquivo
            self.nNFFin.xml = arquivo
            self.xJust.xml  = arquivo

    xml = property(get_xml, set_xml)


class InutNFe(XMLNFe):
    def __init__(self):
        super(InutNFe, self).__init__()
        self.versao  = TagDecimal(nome='inutNFe', codigo='DP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.07', raiz='/')
        self.infInut = InfInutEnviado()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'inutNFe_v1.07.xsd'

        self.chave = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infInut.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.infInut.Id.valor

        xml += self.Signature.xml
        xml += '</inutNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infInut.xml   = arquivo
            self.Signature.xml = self._le_noh('//inutNFe/sig:Signature')

    xml = property(get_xml, set_xml)

    def monta_chave(self):
        chave = str(self.infInut.cUF.valor).zfill(2)
        chave += self.infInut.ano.valor.zfill(2)
        chave += self.infInut.CNPJ.valor.zfill(14)
        chave += str(self.infInut.mod.valor).zfill(2)
        chave += str(self.infInut.serie.valor).zfill(3)
        chave += str(self.infInut.nNFIni.valor).zfill(9)
        chave += str(self.infInut.nNFFin.valor).zfill(9)

        self.chave = chave
        return chave

    def gera_nova_chave(self):
        chave = self.monta_chave()

        #
        # Na versão 1.07 da NF-e a chave de inutilização não tem
        # o ano
        #
        chave = chave[0:2] + chave[4:]

        #
        # Define o Id
        #
        self.infInut.Id.valor = 'ID' + chave


class InfInutRecebido(XMLNFe):
    def __init__(self):
        super(InfInutRecebido, self).__init__()
        self.Id       = TagCaracter(nome='infInut' , codigo='DR03', tamanho=[17, 17]    , raiz='//retInutNFe', propriedade='Id', obrigatorio=False)
        self.tpAmb    = TagInteiro(nome='tpAmb'    , codigo='DR05', tamanho=[1, 1, 1]   , raiz='//retInutNFe/infInut', valor=2)
        self.verAplic = TagCaracter(nome='verAplic', codigo='DR06', tamanho=[1, 20]     , raiz='//retInutNFe/infInut')
        self.cStat    = TagCaracter(nome='cStat'   , codigo='DR07', tamanho=[3, 3, 3]   , raiz='//retInutNFe/infInut')
        self.xMotivo  = TagCaracter(nome='xMotivo' , codigo='DR08', tamanho=[1, 255]    , raiz='//retInutNFe/infInut')
        self.cUF      = TagInteiro(nome='cUF'      , codigo='DR09', tamanho=[2, 2, 2]   , raiz='//retInutNFe/infInut')
        self.ano      = TagCaracter(nome='ano'     , codigo='DR10', tamanho=[2, 2]      , raiz='//retInutNFe/infInut', obrigatorio=False)
        self.CNPJ     = TagCaracter(nome='CNPJ'    , codigo='DR11', tamanho=[3, 14]     , raiz='//retInutNFe/infInut', obrigatorio=False)
        self.mod      = TagInteiro(nome='mod'      , codigo='DR12', tamanho=[2, 2, 2]   , raiz='//retInutNFe/infInut', obrigatorio=False)
        self.serie    = TagInteiro(nome='serie'    , codigo='DR13', tamanho=[1, 3]      , raiz='//retInutNFe/infInut', obrigatorio=False)
        self.nNFIni   = TagInteiro(nome='nNFIni'   , codigo='DR14', tamanho=[1, 9]      , raiz='//retInutNFe/infInut', obrigatorio=False)
        self.nNFFin   = TagInteiro(nome='nNFFin'   , codigo='DR15', tamanho=[1, 9]      , raiz='//retInutNFe/infInut', obrigatorio=False)
        self.dhRecbto = TagDataHora(nome='dhRecbto', codigo='DR16',                       raiz='//retInutNFe/infInut', obrigatorio=False)
        self.nProt    = TagInteiro(nome='nProt'    , codigo='DR17', tamanho=[15, 15, 15], raiz='//retInutNFe/infInut', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.xml:
            xml += self.Id.xml
        else:
            xml += '<infInut>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.ano.xml
        xml += self.CNPJ.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNFIni.xml
        xml += self.nNFFin.xml
        xml += self.dhRecbto.xml
        xml += self.nProt.xml
        xml += '</infInut>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml       = arquivo
            self.tpAmb.xml    = arquivo
            self.verAplic.xml = arquivo
            self.cStat.xml    = arquivo
            self.xMotivo.xml  = arquivo
            self.cUF.xml      = arquivo
            self.ano.xml      = arquivo
            self.CNPJ.xml     = arquivo
            self.mod.xml      = arquivo
            self.serie.xml    = arquivo
            self.nNFIni.xml   = arquivo
            self.nNFFin.xml   = arquivo
            self.dhRecbto.xml = arquivo
            self.nProt.xml    = arquivo

    xml = property(get_xml, set_xml)


class RetInutNFe(XMLNFe):
    def __init__(self):
        super(RetInutNFe, self).__init__()
        self.versao = TagDecimal(nome='retInutNFe', codigo='DR01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.07', raiz='/')
        self.infInut = InfInutRecebido()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retInutNFe_v1.07.xsd'

        self.chave = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infInut.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != '#'):
            xml += self.Signature.xml

        xml += '</retInutNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infInut.xml   = arquivo
            self.Signature.xml = self._le_noh('//retInutNFe/sig:Signature')

    xml = property(get_xml, set_xml)

    def monta_chave(self):
        chave = str(self.infInut.cUF.valor).zfill(2)
        chave += self.infInut.ano.valor.zfill(2)
        chave += self.infInut.CNPJ.valor.zfill(14)
        chave += str(self.infInut.mod.valor).zfill(2)
        chave += str(self.infInut.serie.valor).zfill(3)
        chave += str(self.infInut.nNFIni.valor).zfill(9)
        chave += str(self.infInut.nNFFin.valor).zfill(9)

        self.chave = chave
        return chave


class ProcInutNFe(XMLNFe):
    def __init__(self):
        super(ProcInutNFe, self).__init__()
        #
        # Atenção --- a tag ProcInutNFe tem que começar com letra maiúscula, para
        # poder validar no XSD. Os outros arquivos proc, procCancNFe, e procNFe
        # começam com minúscula mesmo
        #
        self.versao = TagDecimal(nome='ProcInutNFe', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.07', raiz='/')
        self.inutNFe = InutNFe()
        self.retInutNFe = RetInutNFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procInutNFe_v1.07.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.inutNFe.xml.replace(ABERTURA, '')
        xml += self.retInutNFe.xml.replace(ABERTURA, '')
        xml += '</ProcInutNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.inutNFe.xml    = arquivo
            self.retInutNFe.xml = arquivo

    xml = property(get_xml, set_xml)
