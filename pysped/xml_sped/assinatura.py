# -*- coding: utf-8 -*-

from pysped.xml_sped import XMLNFe, NAMESPACE_SIG, ABERTURA, tira_abertura
import libxml2
import xmlsec
import os
from datetime import datetime
from time import mktime


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
