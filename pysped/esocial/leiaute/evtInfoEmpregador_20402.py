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
import os
import base64
from reportlab.graphics.barcode import createBarcodeDrawing
from genshi.core import Markup
from pysped.xml_sped import *
from pysped.esocial.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

PYBRASIL = False
#try:
from pybrasil.inscricao import formata_ie
from pybrasil.telefone import formata_fone
PYBRASIL = True
#except:
    #pass

DIRNAME = os.path.dirname(__file__)


NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v02_04_02'


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', valor='2', raiz='//ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEmpregador>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideEmpregador>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEvento(XMLNFe):
    def __init__(self):
        super(IdeEvento, self).__init__()
        self.tpAmb   = TagInteiro(nome='tpAmb'   , tamanho=[ 1,  1, 1], raiz='//eSocial/evtInfoEmpregador/ideEvento', valor=2, namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.procEmi = TagInteiro(nome='procEmi' , tamanho=[ 1,  1, 1], raiz='//eSocial/evtInfoEmpregador/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', tamanho=[ 1, 20]   , raiz='//eSocial/evtInfoEmpregador/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtInfoEmpregador(XMLNFe):
    def __init__(self):
        super(EvtInfoEmpregador, self).__init__()
        self.Id = TagCaracter(nome='evtInfoEmpregador', propriedade='Id', raiz='//evtInfoEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.Signature = Signature()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml

        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml

        xml += '</evtInfoEmpregador>'

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.Id.valor

        xml += self.Signature.xml
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.Signature.xml = self._le_noh('//eSocial/evtInfoEmpregador/sig:Signature')

    xml = property(get_xml, set_xml)


class S1000(XMLNFe):
    def __init__(self):
        super(S1000, self).__init__()
        self.evtInfoEmpregador = EvtInfoEmpregador()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtInfoEmpregador.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtInfoEmpregador.xml
        xml += '</eSocial>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtInfoEmpregador.xml = arquivo

    xml = property(get_xml, set_xml)
