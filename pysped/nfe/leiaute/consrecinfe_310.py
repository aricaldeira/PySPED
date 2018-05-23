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
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_3 as ESQUEMA_ATUAL
from pysped.nfe.leiaute import consrecinfe_200
import os
from .nfe_310 import NFe, NFCe


DIRNAME = os.path.dirname(__file__)


class ConsReciNFe(consrecinfe_200.ConsReciNFe):
    def __init__(self):
        super(ConsReciNFe, self).__init__()
        self.versao  = TagDecimal(nome='consReciNFe', codigo='BP02', propriedade='versao', namespace=NAMESPACE_NFE, valor='3.10', raiz='/')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consReciNFe_v3.10.xsd'


class InfProt(consrecinfe_200.InfProt):
    def __init__(self):
        super(InfProt, self).__init__()
        self.dhRecbto = TagDataHoraUTC(nome='dhRecbto', codigo='PR08', raiz='//infProt')

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


class ProtNFe(consrecinfe_200.ProtNFe):
    def __init__(self):
        super(ProtNFe, self).__init__()
        self.versao  = TagDecimal(nome='protNFe', codigo='PR02' , propriedade='versao', namespace=NAMESPACE_NFE, valor='3.10', raiz='/')
        self.infProt = InfProt()


class RetConsReciNFe(consrecinfe_200.RetConsReciNFe):
    def __init__(self):
        super(RetConsReciNFe, self).__init__()
        self.versao   = TagDecimal(nome='retConsReciNFe', codigo='BR02' , propriedade='versao', namespace=NAMESPACE_NFE, valor='3.10', raiz='/')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsReciNFe_v3.10.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.nRec.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.cMsg.xml
        xml += self.xMsg.xml

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
            self.cMsg.xml     = arquivo
            self.xMsg.xml     = arquivo
            self.protNFe      = self.le_grupo('//retConsReciNFe/protNFe', ProtNFe)

            #
            # Monta o dicionário dos protocolos
            #
            for pn in self.protNFe:
                self.dic_protNFe[pn.infProt.chNFe.valor] = pn

    xml = property(get_xml, set_xml)


class ProcNFe(consrecinfe_200.ProcNFe):
    def __init__(self):
        super(ProcNFe, self).__init__()
        self.versao  = TagDecimal(nome='nfeProc', propriedade='versao', namespace=NAMESPACE_NFE, valor='3.10', raiz='/')
        self.NFe     = NFe()
        self.protNFe = ProtNFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procNFe_v3.10.xsd'

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

            if self.NFe.infNFe.ide.mod.valor == 65:
                self.NFe = NFCe()
                self.NFe.xml = arquivo

            self.protNFe.xml = arquivo

    xml = property(get_xml, set_xml)
