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
from pysped.nfe.leiaute import nfe_310
from pysped.nfe.webservices_flags import CODIGO_UF
from pysped.nfe.webservices_nfce_3 import ESTADO_QRCODE, ESTADO_CONSULTA_NFCE
import os
import binascii
import hashlib
import qrcode
from StringIO import StringIO


DIRNAME = os.path.dirname(__file__)

class CSC(object):
    def __init__(self):
        self.id = '1'
        self.codigo = ''


class InfNFe(nfe_310.InfNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.ide.mod.valor = '65'  #  NFC-e
        self.ide.tpImp.valor = '4'  #  DANFE NFC-e em papel
        self.ide.indPres.valor = '1'  #  Operação presencial
        self.ide.indFinal.valor = '1'  #  Consumidor final
        self.transp.modFrete.valor = 9  #  Sem frete
        self.dest.modelo = '65'
        self.emit.csc = CSC()


class InfNFeSupl(XMLNFe):
    def __init__(self):
        super(InfNFeSupl, self).__init__()
        self.qrCode = TagCaracter(nome='qrCode', codigo='', tamanho=[1,  600], raiz='//NFe/infNFeSupl', cdata=True)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infNFeSupl>'
        xml += self.qrCode.xml
        xml += '</infNFeSupl>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.qrCode.xml = arquivo

    xml = property(get_xml, set_xml)


class NFCe(nfe_310.NFe):
    def __init__(self):
        super(NFCe, self).__init__()
        self.infNFe = InfNFe()
        self.qrcode = ''
        self.infNFeSupl = InfNFeSupl()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'nfe_v3.10.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<NFe xmlns="http://www.portalfiscal.inf.br/nfe">'
        xml += self.infNFe.xml
        xml += self.infNFeSupl.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.infNFe.Id.valor

        xml += self.Signature.xml
        xml += '</NFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infNFe.xml     = arquivo
            self.infNFeSupl.xml = arquivo
            self.Signature.xml  = self._le_noh('//NFe/sig:Signature')

    xml = property(get_xml, set_xml)

    def monta_chave(self):
        chave = unicode(self.infNFe.ide.cUF.valor).strip().rjust(2, '0')
        chave += unicode(self.infNFe.ide.dhEmi.valor.strftime('%y%m')).strip().rjust(4, '0')
        chave += unicode(self.infNFe.emit.CNPJ.valor).strip().rjust(14, '0')
        chave += '65'
        chave += unicode(self.infNFe.ide.serie.valor).strip().rjust(3, '0')
        chave += unicode(self.infNFe.ide.nNF.valor).strip().rjust(9, '0')

        #
        # Inclui agora o tipo da emissão
        #
        chave += unicode(self.infNFe.ide.tpEmis.valor).strip().rjust(1, '0')

        chave += unicode(self.infNFe.ide.cNF.valor).strip().rjust(8, '0')
        chave += unicode(self.infNFe.ide.cDV.valor).strip().rjust(1, '0')
        self.chave = chave

    def monta_qrcode(self):
        self.monta_chave()

        qrcode = 'chNFe=' + self.chave
        qrcode += '&nVersao=100'
        qrcode += '&tpAmb=' + self.infNFe.ide.tpAmb._valor_string

        if self.infNFe.dest.CNPJ.valor:
            qrcode += '&cDest=' + self.infNFe.dest.CNPJ._valor_string

        elif self.infNFe.dest.CPF.valor:
            qrcode += '&cDest=' + self.infNFe.dest.CPF._valor_string

        elif self.infNFe.dest.idEstrangeiro.valor:
            qrcode += '&cDest=' + self.infNFe.dest.idEstrangeiro._valor_string

        #
        # SP, PR e MS
        #
        if self.infNFe.ide.cUF.valor not in (35, 41, 50):
            qrcode += '&dhEmi=' + binascii.hexlify(self.infNFe.ide.dhEmi._valor_string)
        else:
            qrcode += '&dhEmi=' + binascii.hexlify(self.infNFe.ide.dhEmi._valor_string).upper()

        qrcode += '&vNF=' + self.infNFe.total.ICMSTot.vNF._valor_string
        qrcode += '&vICMS=' + self.infNFe.total.ICMSTot.vICMS._valor_string

        if self.infNFe.ide.cUF.valor not in (35, 41, 50):
            qrcode += '&digVal=' + binascii.hexlify(self.Signature.DigestValue)
        else:
            qrcode += '&digVal=' + binascii.hexlify(self.Signature.DigestValue).upper()

        qrcode += '&cIdToken=' + str(self.infNFe.emit.csc.id).zfill(6)

        pre_qrcode = qrcode + self.infNFe.emit.csc.codigo.ljust(36).upper()

        qrcode += '&cHashQRCode=' + hashlib.sha1(pre_qrcode).hexdigest().upper()

        self.qrcode = qrcode

        qrcode = ESTADO_QRCODE[CODIGO_UF[self.infNFe.ide.cUF.valor]][self.infNFe.ide.tpAmb.valor] + '?' + qrcode

        self.infNFeSupl.qrCode.valor = qrcode

    @property
    def qrcode_imagem(self):
        #
        # box_size=2 dá um tamanho de 4 x 4 cm
        #
        codigo = qrcode.QRCode(box_size=2)
        codigo.add_data(self.infNFeSupl.qrCode.valor)

        arq = StringIO()
        codigo.make_image().save(arq)
        arq.pos = 0
        imagem = arq.read().encode('base64')
        arq.close()

        return imagem

    @property
    def numero_formatado(self):
        num = unicode(self.infNFe.ide.nNF.valor).zfill(9)
        num_formatado = '.'.join((num[0:3], num[3:6], num[6:9]))
        return 'nº ' + num_formatado

    @property
    def serie_formatada(self):
        return 'Série ' + unicode(self.infNFe.ide.serie.valor).zfill(3)

    @property
    def url_consulta(self):
        return ESTADO_CONSULTA_NFCE[CODIGO_UF[self.infNFe.ide.cUF.valor]][self.infNFe.ide.tpAmb.valor]

    @property
    def cnpj_destinatario_formatado(self):
        if self.infNFe.dest.CPF.valor and len(self.infNFe.dest.CPF.valor):
            return 'CNPJ ' + self._formata_cpf(unicode(self.infNFe.dest.CPF.valor))
        elif self.infNFe.dest.CNPJ.valor and len(self.infNFe.dest.CNPJ.valor):
            return 'CPF ' + self._formata_cnpj(unicode(self.infNFe.dest.CNPJ.valor))
        elif self.infNFe.dest.idEstrangeiro.valor and len(self.infNFe.dest.idEstrangeiro.valor):
            return 'Id. estrangeiro ' + self.infNFe.dest.idEstrangeiro.valor
        else:
            return ''

    @property
    def quantidade_itens(self):
        return str(int(len(self.infNFe.det)))
