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

from pysped.xml_sped import NAMESPACE_NFE, TagDecimal, TagInteiro, XMLNFe
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL
from pysped.nfe.leiaute import conscad_101
import os


DIRNAME = os.path.dirname(__file__)


class ConsCad(conscad_101.ConsCad):
    def __init__(self):
        super(ConsCad, self).__init__()
        self.versao = TagDecimal(nome='ConsCad', codigo='GP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='2.00', raiz='/')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consCad_v2.00.xsd'


class InfCadRecebido(conscad_101.InfCadRecebido):
    def __init__(self):
        super(InfCadRecebido, self).__init__()
        self.indCredNFe = TagInteiro(nome='indCredNFe', codigo='GR12a' , tamanho=[1, 1, 1], raiz='//infCad')
        self.indCredCTe = TagInteiro(nome='indCredCTe', codigo='GR12b' , tamanho=[1, 1, 1], raiz='//infCad')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCad>'
        xml += self.IE.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.UF.xml
        xml += self.cSit.xml
        xml += self.indCredNFe.xml
        xml += self.indCredCTe.xml
        xml += self.xNome.xml
        xml += self.xFant.xml
        xml += self.xRegApur.xml
        xml += self.CNAE.xml
        xml += self.dIniAtiv.xml
        xml += self.dUltSit.xml
        xml += self.dBaixa.xml
        xml += self.IEUnica.xml
        xml += self.IEAtual.xml
        xml += self.ender.xml
        xml += '</infCad>'
        return xml

    def set_xml(self, arquivo):
        super(InfCadRecebido, self).set_xml(arquivo)

        if self._le_xml(arquivo):
            self.indCredNFe.xml = arquivo
            self.indCredCTe.xml = arquivo

    xml = property(get_xml, set_xml)


class InfConsRecebido(conscad_101.InfConsRecebido):
    def __init__(self):
        super(InfConsRecebido, self).__init__()

    def get_xml(self):
        return super(InfConsRecebido, self).get_xml()

    def set_xml(self, arquivo):
        super(InfConsRecebido, self).set_xml(arquivo)

        if self._le_xml(arquivo):
            if self._le_nohs('//retConsCad/infCons/infCad') is not None:
                self.infCad = self.le_grupo('//retConsCad/infCons/infCad', InfCadRecebido)

    xml = property(get_xml, set_xml)


class RetConsCad(conscad_101.RetConsCad):
    def __init__(self):
        super(RetConsCad, self).__init__()
        self.versao    = TagDecimal(nome='retConsCad', codigo='GR01', propriedade='versao', namespace=NAMESPACE_NFE, valor='2.00', raiz='/')
        self.infCons = InfConsRecebido()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retConsCad_v2.00.xsd'
