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
from pysped.mdfe.leiaute import ESQUEMA_ATUAL_VERSAO_3 as ESQUEMA_ATUAL
from pysped.mdfe.leiaute.modal_rodoviario_300 import InfModalRodoviario

PYBRASIL = False
#try:
from pybrasil.inscricao import formata_ie
from pybrasil.telefone import formata_fone
from pybrasil.valor import numero_por_extenso_unidade
from pybrasil.codigo_barras import code128_png_base64, code128_svg_base64
PYBRASIL = True
#except:
    #pass

DIRNAME = os.path.dirname(__file__)


class InfAdic(XMLNFe):
    def __init__(self):
        super(InfAdic, self).__init__()
        self.infAdFisco = TagCaracter(nome='infAdFisco', tamanho=[1,  256], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infAdic', obrigatorio=False)
        self.infCpl     = TagCaracter(nome='infCpl'    , tamanho=[1, 5000], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/infAdic', obrigatorio=False)

    def get_xml(self):
        if not (self.infAdFisco.valor or self.infCpl.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infAdic>'
        xml += self.infAdFisco.xml
        xml += self.infCpl.xml
        xml += '</infAdic>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infAdFisco.xml = arquivo
            self.infCpl.xml     = arquivo

    xml = property(get_xml, set_xml)


class Lacres(XMLNFe):
    def __init__(self):
        super(Lacres, self).__init__()
        self.nLacre = TagCaracter(nome='nLacre', tamanho=[1, 60], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//lacres')

    def get_xml(self):
        if not self.nLacre.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<lacres>'
        xml += self.nLacre.xml
        xml += '</lacres>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nLacre.xml = arquivo

    xml = property(get_xml, set_xml)


class AutXML(XMLNFe):
    def __init__(self):
        super(AutXML, self).__init__()
        self.CNPJ = TagCaracter(nome='CNPJ', tamanho=[14, 14], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='/', obrigatorio=False)
        self.CPF  = TagCaracter(nome='CPF' , tamanho=[11, 11], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='/', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.CNPJ.valor or self.CPF.valor:
            xml += '<autXML>'

            if self.CNPJ.valor:
                xml += self.CNPJ.xml
            else:
                xml += self.CPF.xml

            xml += '</autXML>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml     = arquivo
            self.CPF.xml      = arquivo

    xml = property(get_xml, set_xml)


class Tot(XMLNFe):
    def __init__(self):
        super(Tot, self).__init__()
        self.qCTe   = TagInteiro(nome='qCTe'  , tamanho=[1,  6]                       , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/tot', obrigatorio=False)
        self.qNFe   = TagInteiro(nome='qNFe'  , tamanho=[1,  6]                       , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/tot', obrigatorio=False)
        self.qMDFe  = TagInteiro(nome='qMDFe' , tamanho=[1,  6]                       , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/tot', obrigatorio=False)
        self.vCarga = TagDecimal(nome='vCarga', tamanho=[1, 15, 1], decimais=[0, 2, 2], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/tot')
        self.cUnid  = TagCaracter(nome='cUnid', tamanho=[2,  2]                       , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/tot', valor='01')
        self.qCarga = TagDecimal(nome='qCarga', tamanho=[1, 15, 1], decimais=[0, 4, 2], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/tot')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<tot>'
        xml += self.qCTe.xml
        xml += self.qNFe.xml
        xml += self.qMDFe.xml
        xml += self.vCarga.xml
        xml += self.cUnid.xml
        xml += self.qCarga.xml
        xml += '</tot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.qCTe.xml    = arquivo
            self.qNFe.xml    = arquivo
            self.qMDFe.xml   = arquivo
            self.vCarga.xml  = arquivo
            self.cUnid.xml   = arquivo
            self.qCarga.xml  = arquivo

    xml = property(get_xml, set_xml)


class InfNFe(XMLNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.chNFe = TagCaracter(nome='chNFe', tamanho=[44, 44], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//infNFe')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infNFe>'
        xml += self.chNFe.xml
        xml += '</infNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chNFe.xml = arquivo

    xml = property(get_xml, set_xml)


class InfMunDescarga(XMLNFe):
    def __init__(self):
        super(InfMunDescarga, self).__init__()
        self.cMunDescarga = TagInteiro(nome='cMunDescarga' , tamanho=[ 7,  7, 7], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//infMunDescarga')
        self.xMunDescarga = TagCaracter(nome='xMunDescarga', tamanho=[ 2, 60]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//infMunDescarga')
        self.infCTe = []
        self.infNFe = []
        self.infMDFeTransp = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infMunDescarga>'
        xml += self.cMunDescarga.xml
        xml += self.xMunDescarga.xml

        for icte in self.infCTe:
            xml += icte.xml

        for infe in self.infNFe:
            xml += infe.xml

        for imdfe in self.infMDFeTransp:
            xml += imdfe.xml

        xml += '</infMunDescarga>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cMunDescarga.xml = arquivo
            self.xMunDescarga.xml = arquivo

            #self.infCTe = self.le_grupo('//infMunDescarga/infCTe', InfCTe, sigla_ns='mdfe')
            self.infNFe = self.le_grupo('//infMunDescarga/infNFe', InfNFe, sigla_ns='mdfe')
            #self.infMDFeTransp = self.le_grupo('//infMunDescarga/infMDFeTransp', infMDFeTransp, sigla_ns='mdfe')

    xml = property(get_xml, set_xml)

    @property
    def lista_nfes_libreoffice(self):
        texto = ''

        for infe in self.infNFe:
            texto += infe.chNFe.valor + '; '

        return texto


class InfDoc(XMLNFe):
    def __init__(self):
        super(InfDoc, self).__init__()
        self.infMunDescarga = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infDoc>'

        for imd in self.infMunDescarga:
            xml += imd.xml

        xml += '</infDoc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infMunDescarga = self.le_grupo('//MDFe/infMDFe/infDoc/infMunDescarga', InfMunDescarga, sigla_ns='mdfe')

    xml = property(get_xml, set_xml)


class EnderEmit(XMLNFe):
    def __init__(self):
        super(EnderEmit, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , tamanho=[ 2, 60]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit/enderEmit')
        self.nro     = TagCaracter(nome='nro'    , tamanho=[ 1, 60]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit/enderEmit')
        self.xCpl    = TagCaracter(nome='xCpl'   , tamanho=[ 1, 60]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit/enderEmit', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', tamanho=[ 2, 60]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit/enderEmit')
        self.cMun    = TagInteiro(nome='cMun'    , tamanho=[ 7,  7, 7], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit/enderEmit')
        self.xMun    = TagCaracter(nome='xMun'   , tamanho=[ 2, 60]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit/enderEmit')
        self.CEP     = TagCaracter(nome='CEP'    , tamanho=[ 8,  8, 8], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit/enderEmit', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , tamanho=[ 2,  2]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit/enderEmit')
        self.fone    = TagInteiro(nome='fone'    , tamanho=[ 1, 10]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit/enderEmit', obrigatorio=False)
        self.celular = TagInteiro(nome='celular' , tamanho=[ 1, 10]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit/enderEmit', obrigatorio=False)
        self.email   = TagCaracter(nome='email'  , tamanho=[ 1, 60]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit/enderEmit', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderEmit>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += self.fone.xml
        xml += self.email.xml
        xml += '</enderEmit>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.CEP.xml     = arquivo
            self.UF.xml      = arquivo
            self.fone.xml    = arquivo
            self.email.xml   = arquivo

    xml = property(get_xml, set_xml)


class Emit(XMLNFe):
    def __init__(self):
        super(Emit, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , tamanho=[14, 14], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit')
        self.IE        = TagCaracter(nome='IE'   , tamanho=[ 2, 14], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit')
        self.xNome     = TagCaracter(nome='xNome', tamanho=[ 2, 60], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit')
        self.xFant     = TagCaracter(nome='xFant', tamanho=[ 1, 60], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/emit', obrigatorio=False)
        self.enderEmit = EnderEmit()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<emit>'
        xml += self.CNPJ.xml
        xml += self.IE.xml
        xml += self.xNome.xml
        xml += self.xFant.xml
        xml += self.enderEmit.xml
        xml += '</emit>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.xFant.xml     = arquivo
            self.enderEmit.xml = arquivo

    xml = property(get_xml, set_xml)


class InfPercurso(XMLNFe):
    def __init__(self):
        super(InfPercurso, self).__init__()
        self.UFPer = TagCaracter(nome='UFPer', tamanho=[2,  2], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//infPercurso')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infPercurso>'
        xml += self.UFPer.xml
        xml += '</infPercurso>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.UFPer.xml = arquivo

    xml = property(get_xml, set_xml)


class InfMunCarrega(XMLNFe):
    def __init__(self):
        super(InfMunCarrega, self).__init__()
        self.cMunCarrega = TagInteiro(nome='cMunCarrega' , tamanho=[ 7,  7, 7], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//infMunCarrega')
        self.xMunCarrega = TagCaracter(nome='xMunCarrega', tamanho=[ 2, 60]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//infMunCarrega')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infMunCarrega>'
        xml += self.cMunCarrega.xml
        xml += self.xMunCarrega.xml
        xml += '</infMunCarrega>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cMunCarrega.xml = arquivo
            self.xMunCarrega.xml = arquivo

    xml = property(get_xml, set_xml)


class Ide(XMLNFe):
    def __init__(self):
        super(Ide, self).__init__()
        self.cUF      = TagInteiro(nome='cUF'     , tamanho=[ 2,  2, 2], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide')
        self.tpAmb    = TagInteiro(nome='tpAmb'   , tamanho=[ 1,  1, 1], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide', valor=2)
        self.tpEmit   = TagInteiro(nome='tpEmit'  , tamanho=[ 1,  1, 1], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide', valor=2)
        self.tpTransp = TagInteiro(nome='tpTransp', tamanho=[ 1,  1, 1], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide', obrigatorio=False)
        self.mod      = TagCaracter(nome='mod'    , tamanho=[ 2,  2, 2], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide', valor=58)
        self.serie    = TagInteiro(nome='serie'   , tamanho=[ 1,  3, 1], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide')
        self.nMDF     = TagInteiro(nome='nMDF'    , tamanho=[ 1,  9, 1], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide')
        self.cMDF     = TagCaracter(nome='cMDF'   , tamanho=[ 8,  8, 8], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide')
        self.cDV      = TagInteiro(nome='cDV'     , tamanho=[ 1,  1, 1], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide')
        self.modal    = TagInteiro(nome='modal'   , tamanho=[ 1,  1, 1], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide', valor=1)
        self.dhEmi    = TagDataHoraUTC(nome='dhEmi'                    , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide')
        self.tpEmis   = TagInteiro(nome='tpEmis'  , tamanho=[ 1,  1, 1], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide', valor=1)
        self.procEmi  = TagInteiro(nome='procEmi' , tamanho=[ 1,  1, 1], namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide')
        self.verProc  = TagCaracter(nome='verProc', tamanho=[ 1, 20]   , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide')
        self.UFIni    = TagCaracter(nome='UFIni'  , tamanho=[2,  2]    , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide')
        self.UFFim    = TagCaracter(nome='UFFim'  , tamanho=[2,  2]    , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide')
        self.infMunCarrega = []
        self.infPercurso = []
        self.dhIniViagem = TagDataHoraUTC(nome='dhIniViagem'           , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide', obrigatorio=False)
        self.indCanalVerde = TagInteiro(nome='indCanalVerde'           , namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, raiz='//MDFe/infMDFe/ide', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ide>'
        xml += self.cUF.xml
        xml += self.tpAmb.xml
        xml += self.tpEmit.xml
        xml += self.tpTransp.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nMDF.xml
        xml += self.cMDF.xml
        xml += self.cDV.xml
        xml += self.modal.xml
        xml += self.dhEmi.xml
        xml += self.tpEmis.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += self.UFIni.xml
        xml += self.UFFim.xml

        for imc in self.infMunCarrega:
            xml += imc.xml

        for ip in self.infPercurso:
            xml += ip.xml

        xml += self.dhIniViagem.xml
        xml += self.indCanalVerde.xml

        xml += '</ide>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml      = arquivo
            self.tpAmb.xml    = arquivo
            self.tpEmit.xml   = arquivo
            self.tpTransp.xml = arquivo
            self.mod.xml      = arquivo
            self.serie.xml    = arquivo
            self.nMDF.xml     = arquivo
            self.cMDF.xml     = arquivo
            self.cDV.xml      = arquivo
            self.modal.xml    = arquivo
            self.dhEmi.xml    = arquivo
            self.tpEmis.xml   = arquivo
            self.procEmi.xml  = arquivo
            self.verProc.xml  = arquivo
            self.UFIni.xml    = arquivo
            self.UFFim.xml    = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.infMunCarrega = self.le_grupo('//MDFe/infMDFe/ide/infMunCarrega', InfMunCarrega, sigla_ns='mdfe')
            self.infPercurso = self.le_grupo('//MDFe/infMDFe/ide/infPercurso', InfPercurso, sigla_ns='mdfe')

            self.dhIniViagem.xml   = arquivo
            self.indCanalVerde.xml = arquivo


    xml = property(get_xml, set_xml)


class InfMDFe(XMLNFe):
    def __init__(self):
        super(InfMDFe, self).__init__()
        self.versao   = TagDecimal(nome='infMDFe' , propriedade='versao', raiz='//MDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False, valor='3.00')
        self.Id       = TagCaracter(nome='infMDFe', propriedade='Id'    , raiz='//MDFe', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.ide      = Ide()
        self.emit     = Emit()
        self.infModal = InfModalRodoviario()
        self.infDoc   = InfDoc()
        self.tot      = Tot()
        self.lacres   = []
        self.autXML   = []
        self.infAdic  = InfAdic()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infMDFe versao="' + str(self.versao.valor) + '" Id="' + self.Id.valor + '">'
        xml += self.ide.xml
        xml += self.emit.xml
        xml += self.infModal.xml
        xml += self.infDoc.xml
        xml += self.tot.xml
        xml += self.infAdic.xml
        xml += '</infMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.Id.xml       = arquivo
            self.ide.xml      = arquivo
            self.emit.xml     = arquivo
            self.infModal.xml = arquivo
            self.infDoc.xml   = arquivo
            self.tot.xml      = arquivo
            self.infAdic.xml  = arquivo

    xml = property(get_xml, set_xml)


class MDFe(XMLNFe):
    def __init__(self):
        super(MDFe, self).__init__()
        self.infMDFe = InfMDFe()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'mdfe_v3.00.xsd'
        self.chave = ''
        self.dados_contingencia_fsda = ''
        self.site = ''
        self.email = ''
        self.cancelado = False

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<MDFe xmlns="http://www.portalfiscal.inf.br/mdfe">'
        xml += self.infMDFe.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.infMDFe.Id.valor

        xml += self.Signature.xml
        xml += '</MDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infMDFe.xml    = arquivo
            self.Signature.xml = self._le_noh('//MDFe/sig:Signature')

    xml = property(get_xml, set_xml)

    def _calcula_dv(self, valor):
        soma = 0
        m = 2
        for i in range(len(valor)-1, -1, -1):
            c = valor[i]
            soma += int(c) * m
            m += 1
            if m > 9:
                m = 2

        digito = 11 - (soma % 11)
        if digito > 9:
            digito = 0

        return digito

    def gera_nova_chave(self):
        chave = str(self.infMDFe.ide.cUF.valor).zfill(2)
        chave += str(self.infMDFe.ide.dhEmi.valor.strftime('%y%m')).zfill(4)
        chave += str(self.infMDFe.emit.CNPJ.valor).zfill(14)
        chave += str(self.infMDFe.ide.mod.valor).zfill(2)
        chave += str(self.infMDFe.ide.serie.valor).zfill(3)
        chave += str(self.infMDFe.ide.nMDF.valor).zfill(9)
        chave += str(self.infMDFe.ide.tpEmis.valor).zfill(1)

        #
        # O código numério é um número aleatório
        #
        #chave += str(random.randint(0, 99999999)).strip().rjust(8, '0')

        #
        # Mas, por segurança, é preferível que esse número não seja aleatório de todo
        #
        soma = 0
        for c in chave:
            soma += int(c) ** 3 ** 2

        codigo = str(soma)
        if len(codigo) > 8:
            codigo = codigo[-8:]
        else:
            codigo = codigo.rjust(8, '0')

        chave += codigo

        #
        # Define na estrutura do XML o campo cMDF
        #
        self.infMDFe.ide.cMDF.valor = codigo

        #
        # Gera o dígito verificador
        #
        digito = self._calcula_dv(chave)

        #
        # Define na estrutura do XML o campo cDV
        #
        self.infMDFe.ide.cDV.valor = digito

        chave += str(digito)
        self.chave = chave

        #
        # Define o Id
        #
        self.infMDFe.Id.valor = 'MDFe' + chave

    def monta_chave(self):
        chave = str(self.infMDFe.ide.cUF.valor).zfill(2)
        chave += str(self.infMDFe.ide.dhEmi.valor.strftime('%y%m')).zfill(4)
        chave += str(self.infMDFe.emit.CNPJ.valor).zfill(14)
        chave += str(self.infMDFe.ide.mod.valor).zfill(2)
        chave += str(self.infMDFe.ide.serie.valor).zfill(3)
        chave += str(self.infMDFe.ide.nMDF.valor).zfill(9)
        chave += str(self.infMDFe.ide.tpEmis.valor).zfill(1)
        chave += str(self.infMDFe.ide.cMDF.valor).zfill(8)
        chave += str(self.infMDFe.ide.cDV.valor).zfill(1)
        self.chave = chave

    @property
    def chave_imagem(self):
        self.monta_chave()

        if PYBRASIL:
            return code128_png_base64(self.chave)

        #
        # Para converter centímetros para o tamanho do reportlab, use a
        # seguinte fórmula:
        # cm × 128 ÷ 2,75
        #
        # Assim: 0,8 cm = 0,8 × 128 ÷ 2,75 = 37,2 = 37
        # Assim: 0,02 cm = 0,02 × 128 ÷ 2,75 = 0,9 = 1
        #
        imagem = createBarcodeDrawing('Code128', value=self.chave, barHeight=37, barWidth=1)
        return base64.b64encode(imagem.asString('png')).decode('utf-8')

    @property
    def chave_svg(self):
        self.monta_chave()

        if not PYBRASIL:
            return ''

        return code128_svg_base64(self.chave)

    #
    # Funções para formatar campos para o DANFE
    #
    @property
    def chave_formatada(self):
        chave = self.chave
        chave_formatada = ' '.join((chave[0:4], chave[4:8], chave[8:12], chave[12:16], chave[16:20], chave[20:24], chave[24:28], chave[28:32], chave[32:36], chave[36:40], chave[40:44]))
        return chave_formatada

    @property
    def numero_formatado(self):
        num = str(self.infMDFe.ide.nMDF.valor).zfill(9)
        num_formatado = '.'.join((num[0:3], num[3:6], num[6:9]))
        return num_formatado

    @property
    def serie_formatada(self):
        return str(self.infMDFe.ide.serie.valor).zfill(3)

    def _formata_cpf(self, cpf):
        if not len(cpf.strip()):
            return ''

        formatado = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
        return formatado

    def _formata_cnpj(self, cnpj):
        if not len(cnpj.strip()):
            return ''

        formatado = cnpj[0:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[12:14]
        return formatado

    @property
    def cnpj_emitente_formatado(self):
        return self._formata_cnpj(str(self.infMDFe.emit.CNPJ.valor))

    @property
    def ie_emitente_formatada(self):
        if not PYBRASIL:
            return self.infMDFe.emit.IE.valor

        return formata_ie(self.infMDFe.emit.IE.valor, self.infMDFe.emit.enderEmit.UF.valor)

    @property
    def endereco_emitente_formatado(self):
        formatado = self.infMDFe.emit.enderEmit.xLgr.valor
        formatado += ', ' + self.infMDFe.emit.enderEmit.nro.valor

        if len(self.infMDFe.emit.enderEmit.xCpl.valor.strip()):
            formatado += ' - ' + self.infMDFe.emit.enderEmit.xCpl.valor

        return formatado

    def _formata_cep(self, cep):
        if not len(cep.strip()):
            return ''

        return cep[0:5] + '-' + cep[5:8]

    @property
    def cep_emitente_formatado(self):
        return self._formata_cep(self.infMDFe.emit.enderEmit.CEP.valor)

    def _formata_fone(self, fone):
        if not len(fone.strip()):
            return ''

        if fone.strip() == '0':
            return ''

        if PYBRASIL:
            return formata_fone(fone)

        if len(fone) <= 8:
            formatado = fone[:-4] + '-' + fone[-4:]
        elif len(fone) <= 10:
            ddd = fone[0:2]
            fone = fone[2:]
            formatado = '(' + ddd + ') ' + fone[:-4] + '-' + fone[-4:]

        elif len(fone) <= 11:
            ddd = fone[0:3]
            fone = fone[3:]
            formatado = '(' + ddd + ') ' + fone[-9:-6] + '-' + fone[-6:-4] + '-' + fone[-4:]

        #
        # Assume 8 dígitos para o número, 2 para o DD, e o restante é o DDI
        #
        else:
            numero = fone[len(fone)-8:]
            ddd = fone[len(fone)-10:len(fone)-8]
            ddi = fone[:len(fone)-10]
            formatado = '+' + ddi + ' (' + ddd + ') ' + numero[:-4] + '-' + numero[-4:]

        return formatado

    @property
    def fone_emitente_formatado(self):
        return self._formata_fone(str(self.infMDFe.emit.enderEmit.fone.valor))

    @property
    def celular_emitente_formatado(self):
        return self._formata_fone(str(self.infMDFe.emit.enderEmit.celular.valor))

    @property
    def placa_veiculo_formatada(self):
        if not self.infMDFe.infModal.veicTracao.placa.valor:
            return ''

        placa = self.infMDFe.infModal.veicTracao.placa.valor
        placa = placa[:-4] + '-' + placa[-4:]
        return placa

    @property
    def dados_adicionais(self):
        da = ''

        if self.infMDFe.infAdic.infAdFisco.valor:
            da = self.infMDFe.infAdic.infAdFisco.valor.replace('|', '<br />')

        if self.infMDFe.infAdic.infCpl.valor:
            if len(da) > 0:
                da += '<br />'

            da += self.infMDFe.infAdic.infCpl.valor.replace('|', '<br />')

        return da

    @property
    def dados_adicionais_libreoffice(self):
        da = ''

        if self.infMDFe.infAdic.infAdFisco.valor:
            da = self.infMDFe.infAdic.infAdFisco.valor.replace('| ', '<text:line-break/>')

        if self.infMDFe.infAdic.infCpl.valor:
            if len(da) > 0:
                da += '<text:line-break/>'

            da += self.infMDFe.infAdic.infCpl.valor.replace('| ', '<text:line-break/>')

        return Markup(da)
