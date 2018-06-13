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
from pysped.nfe.leiaute import envinfe_200
import os
from .nfe_310 import NFe


DIRNAME = os.path.dirname(__file__)


class EnviNFe(envinfe_200.EnviNFe):
    def __init__(self):
        super(EnviNFe, self).__init__()
        self.indSinc = TagCaracter(nome='indSinc', tamanho=[1, 1, 1], raiz='//enviNFe', valor='0')
        self.versao  = TagDecimal(nome='enviNFe', codigo='AP02', propriedade='versao', namespace=NAMESPACE_NFE, valor='3.10', raiz='/')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'enviNFe_v3.10.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.idLote.xml
        xml += self.indSinc.xml

        for n in self.NFe:
            xml += tira_abertura(n.xml)

        xml += '</enviNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.idLote.xml    = arquivo
            self.indSinc.xml    = arquivo
            self.NFe = self.le_grupo('//NFe', NFe)

        return self.xml

    xml = property(get_xml, set_xml)


class InfRec(envinfe_200.InfRec):
    def __init__(self):
        super(InfRec, self).__init__()


class RetEnviNFe(envinfe_200.RetEnviNFe):
    def __init__(self):
        super(RetEnviNFe, self).__init__()
        self.versao   = TagDecimal(nome='retEnviNFe', codigo='AR02' , propriedade='versao', namespace=NAMESPACE_NFE, valor='3.10', raiz='/')
        self.dhRecbto = TagDataHoraUTC(nome='dhRecbto' , codigo='AR09', raiz='//retEnviNFe')
        self.infRec   = InfRec()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retEnviNFe_v3.10.xsd'
