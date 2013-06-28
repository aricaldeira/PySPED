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

from pysped.xml_sped import XMLNFe
import os


DIRNAME = os.path.dirname(__file__)


class Signature(XMLNFe):
    def __init__(self):
        super(Signature, self).__init__()
        self.URI = u''
        self.DigestValue = u''
        self.SignatureValue = u''
        self.X509Certificate = u''
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/')
        self.arquivo_esquema = u'xmldsig-core-schema_v1.01.xsd'

    def get_xml(self):
        if not len(self.URI):
            self.URI = u'#'

        if self.URI[0] != u'#':
            self.URI = u'#' + self.URI

        xml  = u'<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">'
        xml +=     u'<SignedInfo>'
        xml +=         u'<CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />'
        xml +=         u'<SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" />'
        xml +=         u'<Reference URI="' + self.URI + u'">'
        xml +=             u'<Transforms>'
        xml +=                 u'<Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />'
        xml +=                 u'<Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />'
        xml +=             u'</Transforms>'
        xml +=             u'<DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" />'
        xml +=             u'<DigestValue>' + self.DigestValue + u'</DigestValue>'
        xml +=         u'</Reference>'
        xml +=     u'</SignedInfo>'
        xml +=     u'<SignatureValue>' + self.SignatureValue + u'</SignatureValue>'
        xml +=     u'<KeyInfo>'
        xml +=         u'<X509Data>'
        xml +=             u'<X509Certificate>' + self.X509Certificate + u'</X509Certificate>'
        xml +=         u'</X509Data>'
        xml +=     u'</KeyInfo>'
        xml += u'</Signature>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.URI = self._le_tag(u'//sig:Signature/sig:SignedInfo/sig:Reference', u'URI') or u''
            self.DigestValue = self._le_tag(u'//sig:Signature/sig:SignedInfo/sig:Reference/sig:DigestValue') or u''
            self.SignatureValue = self._le_tag(u'//sig:Signature/sig:SignatureValue') or u''
            self.X509Certificate = self._le_tag(u'//sig:Signature/sig:KeyInfo/sig:X509Data/sig:X509Certificate') or u''
        return self.xml

    xml = property(get_xml, set_xml)
