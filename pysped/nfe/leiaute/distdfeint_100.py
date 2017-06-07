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

from pysped.xml_sped import (ABERTURA, NAMESPACE_NFE, Signature, TagCaracter,
                             TagDataHora, TagDecimal, TagInteiro, XMLNFe,
                             TagDataHoraUTC)
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_3 as ESQUEMA_ATUAL
from pysped.nfe.leiaute.soap_200 import NFeDadosMsg
from pysped.nfe.leiaute import ProcNFe_310
import unicodedata
import os
import gzip
from StringIO import StringIO


DIRNAME = os.path.dirname(__file__)


class DistNSU(XMLNFe):
    def __init__(self):
        super(DistNSU, self).__init__()
        self.ultNSU = TagCaracter(nome='ultNSU', tamanho=[1, 15], raiz='//distDFeInt/distNSU', valor='0000000000000000')

    def get_xml(self):
        if not self.ultNSU.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<distNSU>'
        xml += self.ultNSU.xml
        xml += '</distNSU>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ultNSU.xml = arquivo

    xml = property(get_xml, set_xml)


class ConsNSU(XMLNFe):
    def __init__(self):
        super(ConsNSU, self).__init__()
        self.NSU = TagCaracter(nome='NSU', tamanho=[1, 15], raiz='//distDFeInt/consNSU', valor='')

    def get_xml(self):
        if not self.NSU.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<consNSU>'
        xml += self.NSU.xml
        xml += '</consNSU>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.NSU.xml = arquivo

    xml = property(get_xml, set_xml)


class ConsChNFe(XMLNFe):
    def __init__(self):
        super(ConsChNFe, self).__init__()
        self.chNFe = TagCaracter(nome='chNFe', tamanho=[44, 44], raiz='//distDFeInt/consChNFe', valor='')

    def get_xml(self):
        if not self.chNFe.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<consChNFe>'
        xml += self.chNFe.xml
        xml += '</consChNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chNFe.xml = arquivo

    xml = property(get_xml, set_xml)


class DistDFeInt(XMLNFe):
    def __init__(self):
        super(DistDFeInt, self).__init__()
        self.versao   = TagDecimal(nome='distDFeInt', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.01', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'     , tamanho=[1, 1, 1], raiz='//distDFeInt', valor=2)
        self.cUFAutor = TagInteiro(nome='cUFAutor'  , tamanho=[2, 2, 2], raiz='//distDFeInt')
        self.CNPJ     = TagCaracter(nome='CNPJ'     , tamanho=[14, 14] , raiz='//distDFeInt', obrigatorio=False)
        self.CPF      = TagCaracter(nome='CPF'      , tamanho=[11, 11] , raiz='//distDFeInt', obrigatorio=False)
        self.distNSU  = DistNSU()
        self.consNSU  = ConsNSU()
        self.consChNFe  = ConsChNFe()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'distDFeInt_v1.01.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.cUFAutor.xml

        if self.CNPJ.valor:
            xml += self.CNPJ.xml
        else:
            xml += self.CPF.xml

        if self.consChNFe.chNFe.valor is not None and self.consChNFe.chNFe.valor != '':
            xml += self.consChNFe.xml
        elif self.consNSU.NSU.valor is not None and self.consNSU.NSU.valor != '':
            xml += self.consNSU.xml
        else:
            xml += self.distNSU.xml

        xml += '</distDFeInt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml     = arquivo
            self.tpAmb.xml  = arquivo
            self.cUFAutor.xml    = arquivo
            self.CNPJ.xml   = arquivo
            self.CPF.xml   = arquivo
            self.distNSU.xml    = arquivo
            self.consNSU.xml    = arquivo
            self.consChNFe.xml  = arquivo

    xml = property(get_xml, set_xml)


class ResNFe(XMLNFe):
    def __init__(self):
        super(ResNFe, self).__init__()
        self.chNFe    = TagCaracter(nome='chNFe' , tamanho=[44, 44], raiz='//resNFe')
        self.CNPJ     = TagCaracter(nome='CNPJ'  , tamanho=[14, 14], raiz='//resNFe', obrigatorio=False)
        self.CPF      = TagCaracter(nome='CPF'   , tamanho=[11, 11], raiz='//resNFe', obrigatorio=False)
        self.xNome    = TagCaracter(nome='xNome' , tamanho=[ 1, 60], raiz='//resNFe')
        self.IE       = TagCaracter(nome='IE'    , tamanho=[ 2, 14], raiz='//resNFe', obrigatorio=False)
        self.dhEmi    = TagDataHoraUTC(nome='dhEmi',                   raiz='//resNFe', obrigatorio=False)
        self.tpNF     = TagCaracter(nome='tpNF'  , tamanho=[ 1,  1], raiz='//resNFe')
        self.vNF      = TagDecimal(nome='vNF'    , tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//resNFe')
        self.digVal   = TagCaracter(nome='digVal', tamanho=[28, 28], raiz='//resNFe')
        self.dhRecbto = TagDataHoraUTC(nome='dhRecbto', raiz='//resNFe')
        self.cSitNFe  = TagCaracter(nome='cSitNFe', tamanho=[ 1,  1], raiz='//resNFe')
        self.cSitConf = TagCaracter(nome='cSitConf', tamanho=[ 1,  1], raiz='//resNFe', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.chNFe.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.xNome.xml
        xml += self.IE.xml
        xml += self.dhEmi.xml
        xml += self.tpNF.xml
        xml += self.vNF.xml
        xml += self.digVal.xml
        xml += self.dhRecbto.xml
        xml += self.cSitNFe.xml
        xml += self.cSitConf.xml
        xml += '</resNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chNFe.xml   = arquivo
            self.CNPJ.xml   = arquivo
            self.CPF.xml   = arquivo
            self.xNome.xml   = arquivo
            self.IE.xml   = arquivo
            self.dhEmi.xml   = arquivo
            self.tpNF.xml   = arquivo
            self.vNF.xml   = arquivo
            self.digVal.xml   = arquivo
            self.dhRecbto.xml   = arquivo
            self.cSitNFe.xml   = arquivo
            self.cSitConf.xml   = arquivo

    xml = property(get_xml, set_xml)


class DocZip(XMLNFe):
    def __init__(self):
        super(DocZip, self).__init__()
        self.NSU    = TagCaracter(nome='docZip', propriedade='NSU'   , namespace=NAMESPACE_NFE, raiz='/')
        self.schema = TagCaracter(nome='docZip', propriedade='schema', namespace=NAMESPACE_NFE, raiz='/')
        self.docZip = TagCaracter(nome='docZip', namespace=NAMESPACE_NFE, raiz='/')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        xml += '<docZip NSU="'
        xml += self.NSU.valor
        xml += '" schema="'
        xml += self.schema.valor
        xml += '">'
        xml += self.docZip.valor
        xml += '</docZip>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.NSU.xml    = arquivo
            self.schema.xml = arquivo
            self.docZip.xml = arquivo

            if self.docZip.valor:
                arq = StringIO()
                arq.write(self.docZip.valor.decode('base64'))
                arq.seek(0)
                zip = gzip.GzipFile(fileobj=arq)
                texto = zip.read()
                arq.close()
                zip.close()
                self.texto = texto.decode('utf-8')
                self.resposta = None

                if self.schema.valor == 'resNFe_v1.00.xsd':
                    self.resposta = ResNFe()
                    texto = unicodedata.normalize(b'NFKD', self.texto).encode('ascii', 'ignore')
                    self.resposta.xml = texto
                elif self.schema.valor == 'procNFe_v3.10.xsd':
                    self.resposta = ProcNFe_310()
                    self.resposta.xml = self.texto

    xml = property(get_xml, set_xml)


class LoteDistDFeInt(XMLNFe):
    def __init__(self):
        super(LoteDistDFeInt, self).__init__()
        self.docZip = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if len(self.docZip) == 0:
            return xml

        xml += '<loteDistDFeInt>'

        for d in self.docZip:
            xml += d.xml

        xml += '</loteDistDFeInt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.docZip = self.le_grupo('//loteDistDFeInt/docZip', DocZip)

    xml = property(get_xml, set_xml)


class RetDistDFeInt(XMLNFe):
    def __init__(self):
        super(RetDistDFeInt, self).__init__()
        self.versao   = TagDecimal(nome='retDistDFeInt', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.00', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'        , tamanho=[1, 1, 1], raiz='//retDistDFeInt', valor=2)
        self.verAplic = TagCaracter(nome='verAplic'    , tamanho=[1, 20]  , raiz='//retDistDFeInt')
        self.cStat    = TagCaracter(nome='cStat'       , tamanho=[3, 3, 3], raiz='//retDistDFeInt')
        self.xMotivo  = TagCaracter(nome='xMotivo'     , tamanho=[1, 255] , raiz='//retDistDFeInt')
        self.dhResp   = TagDataHoraUTC(nome='dhResp'                      , raiz='//retDistDFeInt')
        self.ultNSU   = TagCaracter(nome='ultNSU'      , tamanho=[1, 15]  , raiz='//retDistDFeInt', obrigatorio=False)
        self.maxNSU   = TagCaracter(nome='maxNSU'      , tamanho=[1, 15]  , raiz='//retDistDFeInt', obrigatorio=False)
        self.loteDistDFeInt = LoteDistDFeInt()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retDistDFeInt_v1.00.xsd'

        self.chave = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.dhResp.xml
        xml += self.ultNSU.xml
        xml += self.maxNSU.xml
        xml += self.loteDistDFeInt.xml
        xml += '</retDistDFeInt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpAmb.xml    = arquivo
            self.verAplic.xml = arquivo
            self.cStat.xml    = arquivo
            self.xMotivo.xml  = arquivo
            self.dhResp.xml  = arquivo
            self.ultNSU.xml  = arquivo
            self.maxNSU.xml  = arquivo
            self.loteDistDFeInt.xml = arquivo

    xml = property(get_xml, set_xml)


class SOAPEnvio(XMLNFe):
    def __init__(self):
        super(SOAPEnvio, self).__init__()
        self.webservice = ''
        self.metodo = ''
        self.cUF    = None
        self.envio  = None
        self.nfeDadosMsg = NFeDadosMsg()
        self._header = {b'content-type': b'application/soap+xml; charset=utf-8'}
        self.soap_action_webservice_e_metodo = False

    def get_xml(self):
        self.nfeDadosMsg.webservice = self.webservice
        self.nfeDadosMsg.dados = self.envio

        self._header[b'content-type'] = b'application/soap+xml; charset=utf-8;'  #  ' action="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice.encode('utf-8') + b'/' + self.metodo.encode('utf-8') + b'"'

        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     '<soap12:Body>'
        xml +=       '<nfeDistDFeInteresse xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe">'
        xml +=             self.nfeDadosMsg.xml
        xml +=       '</nfeDistDFeInteresse>'
        xml +=     '</soap12:Body>'
        xml += '</soap12:Envelope>'
        return xml

    def set_xml(self):
        pass

    xml = property(get_xml, set_xml)

    def get_header(self):
        header = self._header
        return header

    header = property(get_header)


class SOAPRetorno(XMLNFe):
    def __init__(self):
        super(SOAPRetorno, self).__init__()
        self.webservice = ''
        self.metodo = ''
        self.resposta = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        xml +=     '<soap:Header>'
        xml +=         '<nfeCabecMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/' + self.webservice + '">'
        xml +=             self.nfeCabecMsg.xml
        xml +=         '</nfeCabecMsg>'
        xml +=     '</soap:Header>'
        xml +=     '<soap:Body>'
        xml +=         '<nfeDistDFeInteresseResponse xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe">'
        xml +=             '<' + self.metodo + 'Result>'
        xml +=                 self.resposta.xml
        xml +=             '</' + self.metodo + 'Result>'
        xml +=     '</soap:Body>'
        xml += '</soap:Envelope>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.resposta.xml = arquivo

    xml = property(get_xml, set_xml)
