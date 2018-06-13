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

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
import os

from .eventoscte_300 import EvGTV, EvPrestDesacordo, EvCCeCTe, EvRegMultimodal, EvEPECCTe, EvCancCTe

DIRNAME = os.path.dirname(__file__)


class DetEvento(XMLNFe):
    def __init__(self):
        super(DetEvento, self).__init__()
        self.versaoEvento = TagDecimal(nome='detEvento', propriedade='versaoEvento', namespace=NAMESPACE_CTE, valor='3.00', raiz='/', namespace_obrigatorio=False)
        self.evento = None

    def get_xml(self):
        if self.evento is None:
            return ''
        xml = XMLNFe.get_xml(self)
        xml += self.versaoEvento.xml
        xml += self.evento.xml
        xml += '</detEvento>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versaoEvento.xml = arquivo
            if ('<evCancCTe>' in arquivo and '</evCancCTe>' in arquivo):
                self.evento = EvCancCTe()
                self.evento.xml = arquivo
            elif ('<evEPECCTe>' in arquivo and '</evEPECCTe>' in arquivo):
                self.evento = EvEPECCTe()
                self.evento.xml = arquivo
            elif ('<evRegMultimodal>' in arquivo and '</evRegMultimodal>' in arquivo):
                self.evento = EvRegMultimodal()
                self.evento.xml = arquivo
            elif ('<evCCeCTe>' in arquivo and '</evCCeCTe>' in arquivo):
                self.evento = EvCCeCTe()
                self.evento.xml = arquivo
            elif ('<evPrestDesacordo>' in arquivo and '</evPrestDesacordo>' in arquivo):
                self.evento = EvPrestDesacordo()
                self.evento.xml = arquivo
            elif ('<evGTV>' in arquivo and '</evGTV>' in arquivo):
                self.evento = EvGTV()
                self.evento.xml = arquivo

    xml = property(get_xml, set_xml)


class InfEvento(XMLNFe):
    def __init__(self):
        super(InfEvento, self).__init__()
        self.Id    = TagCaracter(nome='infEvento', codigo='EP04', tamanho=[54, 54]    , raiz='//eventoCTe', propriedade='Id', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cOrgao  = TagInteiro(nome='cOrgao'      , codigo='EP05', tamanho=[2, 2,2]   , raiz='//eventoCTe/infEvento', valor=91, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.tpAmb = TagInteiro(nome='tpAmb'   , codigo='EP06', tamanho=[ 1,  1, 1] , raiz='//eventoCTe/infEvento', valor=2, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.CNPJ    = TagCaracter(nome='CNPJ'   , codigo='EP07' , tamanho=[ 0, 14]   , raiz='//eventoCTe/infEvento', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.chCTe = TagCaracter(nome='chCTe'   , codigo='EP08', tamanho=[44, 44, 44], raiz='//eventoCTe/infEvento', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dhEvento = TagDataHoraUTC(nome='dhEvento', codigo='EP09' , tamanho=[ 0, 30], raiz='//eventoCTe/infEvento', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.tpEvento = TagCaracter(nome='tpEvento'   , codigo='EP10', tamanho=[6, 6, 6], raiz='//eventoCTe/infEvento',valor='110111', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nSeqEvento = TagInteiro(nome='nSeqEvento'   , codigo='EP11', tamanho=[1,2,2], raiz='//eventoCTe/infEvento', valor=1, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.detEvento = DetEvento()

    def get_xml(self):

        xml = XMLNFe.get_xml(self)

        self.Id.valor = 'ID' + self.tpEvento.valor + self.chCTe.valor +  ("%02d" % self.nSeqEvento.valor)

        xml += self.Id.xml
        xml += self.cOrgao.xml
        xml += self.tpAmb.xml
        xml += self.CNPJ.xml
        xml += self.chCTe.xml
        xml += self.dhEvento.xml
        xml += self.tpEvento.xml
        xml += self.nSeqEvento.xml
        xml += self.detEvento.xml
        xml += '</infEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.cOrgao.xml = arquivo
            self.tpAmb.xml = arquivo
            self.CNPJ.xml = arquivo
            self.chCTe.xml = arquivo
            self.dhEvento.xml = arquivo
            self.tpEvento.xml = arquivo
            self.nSeqEvento.xml = arquivo
            self.detEvento.xml = arquivo

    xml = property(get_xml, set_xml)


class EventoCTe(XMLNFe):
    def __init__(self):
        super(EventoCTe, self).__init__()
        self.versao = TagDecimal(nome='eventoCTe', propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.infEvento = InfEvento()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'eventoCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.infEvento.xml
        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.infEvento.Id.valor
        xml += self.Signature.xml
        xml += '</eventoCTe>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml        = arquivo
            self.infEvento.xml     = arquivo
            self.Signature.xml = self._le_noh('//eventoCTe/sig:Signature', ns=NAMESPACE_CTE)

    xml = property(get_xml, set_xml)


class InfEventoRet(XMLNFe):
    def __init__(self):
        super(InfEventoRet, self).__init__()
        self.Id          = TagCaracter(nome='infEvento', codigo='ER04', tamanho=[54, 54]    , raiz='//infEvento', propriedade='Id', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.tpAmb       = TagInteiro(nome='tpAmb'   , codigo='ER05', tamanho=[ 1,  1, 1] , raiz='//retEventoCTe/infEvento', valor=2, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.verAplic    = TagCaracter(nome='verAplic'      , codigo='ER06', tamanho=[1, 20]   , raiz='//retEventoCTe/infEvento', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cOrgao      = TagInteiro(nome='cOrgao'      , codigo='ER07', tamanho=[2, 2,2]   , raiz='//retEventoCTe/infEvento', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cStat       = TagCaracter(nome='cStat'   , codigo='ER08', tamanho=[3, 3, 3]   , raiz='//retEventoCTe/infEvento', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xMotivo     = TagCaracter(nome='xMotivo' , codigo='ER09', tamanho=[1, 255]    , raiz='//retEventoCTe/infEvento', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.chCTe       = TagCaracter(nome='chCTe'   , codigo='ER10', tamanho=[44, 44, 44], raiz='//retEventoCTe/infEvento', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.tpEvento    = TagCaracter(nome='tpEvento'   , codigo='ER11', tamanho=[6, 6, 6], raiz='//retEventoCTe/infEvento', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xEvento     = TagCaracter(nome='xEvento'    , codigo='ER12', tamanho=[ 4,  60], raiz='//retEventoCTe/infEvento', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nSeqEvento  = TagInteiro(nome='nSeqEvento'   , codigo='ER13', tamanho=[1,2,2], raiz='//retEventoCTe/infEvento', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dhRegEvento = TagDataHoraUTC(nome='dhRegEvento', codigo='ER14', raiz='//retEventoCTe/infEvento', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nProt       = TagCaracter(nome='nProt', codigo='ER15', tamanho=[15, 15, 15], raiz='//retEventoCTe/infEvento', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):

        xml = XMLNFe.get_xml(self)

        if self.Id.xml:
            xml += self.Id.xml
        else:
            xml += '<infEvento>'
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cOrgao.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.chCTe.xml
        xml += self.tpEvento.xml
        xml += self.xEvento.xml
        xml += self.nSeqEvento.xml
        xml += self.dhRegEvento.xml
        xml += self.nProt.xml
        xml += '</infEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml          = arquivo
            self.tpAmb.xml       = arquivo
            self.verAplic.xml    = arquivo
            self.cOrgao.xml      = arquivo
            self.cStat.xml       = arquivo
            self.xMotivo.xml     = arquivo
            self.chCTe.xml       = arquivo
            self.tpEvento.xml    = arquivo
            self.xEvento.xml     = arquivo
            self.nSeqEvento.xml  = arquivo
            self.dhRegEvento.xml = arquivo
            self.nProt.xml       = arquivo

    xml = property(get_xml, set_xml)



class RetEventoCTe(XMLNFe):
    def __init__(self):
        super(RetEventoCTe, self).__init__()
        self.versao = TagDecimal(nome='retEventoCTe', propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.infEvento = InfEventoRet()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retEventoCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infEvento.xml
        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.infEvento.Id.valor
        xml += self.Signature.xml
        xml += '</retEventoCTe>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml        = arquivo
            self.infEvento.xml     = arquivo
            self.Signature.xml = self._le_noh('//retEventoCTe/sig:Signature', ns=NAMESPACE_CTE)

    xml = property(get_xml, set_xml)



class ProcEventoCTe(XMLNFe):
    def __init__(self):
        super(ProcEventoCTe, self).__init__()
        self.versao = TagDecimal(nome='procEventoCTe', propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.ipTransmissor = TagCaracter(nome='ipTransmissor', codigo='ZR03', tamanho=[0, 15]   , raiz='/', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.eventoCTe = EventoCTe()
        self.retEventoCTe = RetEventoCTe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procEventoCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        if not (self.ipTransmissor.valor):
            xml += '<procEventoCTe versao="'+ str(self.versao.valor) +'">'
        else:
            xml += '<procEventoCTe versao="'+ str(self.versao.valor) +'" ipTransmissor="'+ self.ipTransmissor.valor +'">'
        xml += self.eventoCTe.xml
        xml += self.retEventoCTe.xml
        xml += '</procEventoCTe>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml        = arquivo
            self.ipTransmissor.xml = arquivo
            self.eventoCTe.xml     = arquivo
            self.retEventoCTe.xml  = arquivo

    xml = property(get_xml, set_xml)
