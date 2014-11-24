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

from pysped.xml_sped import (ABERTURA, NAMESPACE_NFE, TagCaracter, TagDecimal,
                             TagDataHora, TagInteiro, XMLNFe)
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL
import os
from lxml import etree

DIRNAME = os.path.dirname(__file__)


class TagChNFe(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagChNFe, self).__init__(*args, **kwargs)
        self.nome = 'chNFe'
        self.codigo = 'JP06',
        self.tamanho = [44, 44]
        self.raiz = '//downloadNFe'


class DownloadNFe(XMLNFe):
    def __init__(self):
        super(DownloadNFe, self).__init__()
        self.versao    = TagDecimal(nome='downloadNFe', codigo='JP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.00', raiz='/')
        self.tpAmb = TagInteiro(nome='tpAmb'   , codigo='JP03', tamanho=[ 1,  1, 1] , raiz='//downloadNFe', valor=2)
        self.xServ = TagCaracter(nome='xServ'  , codigo='JP04', tamanho=[12, 12]    , raiz='//downloadNFe', valor='DOWNLOAD NFE')
        self.CNPJ  = TagCaracter(nome='CNPJ'  , codigo='JP05', tamanho=[14, 14], raiz='//downloadNFe')
        self.chNFe = []
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'downloadNFe_v1.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.CNPJ.xml

        for c in self.chNFe:
            xml += c.xml

        xml += '</downloadNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml = arquivo
            self.xServ.xml = arquivo
            self.CNPJ.xml = arquivo
            self.chNFe = self.le_grupo('//downloadNFe/chNFe', TagChNFe)

    xml = property(get_xml, set_xml)


class ProcNFeGrupoZip(XMLNFe):
    def __init__(self):
        super(ProcNFeGrupoZip, self).__init__()
        self.NFeZip = TagCaracter(nome='NFeZip', codigo='JR13', raiz='//retNFe/procNFeGrupoZip')
        self.protNFeZip = TagCaracter(nome='protNFeZip', codigo='JR14', raiz='//retNFe/procNFeGrupoZip')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.NFeZip.valor and self.protNFeZip.valor:
            xml += '<procNFeGrupoZip>'
            xml += self.NFeZip.xml
            xml += self.protNFeZip.xml
            xml += '</procNFeGrupoZip>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.NFeZip.xml     = arquivo
            self.protNFeZip.xml = arquivo

    xml = property(get_xml, set_xml)


class RetNFe(XMLNFe):
    def __init__(self):
        super(RetNFe, self).__init__()
        self.chNFe    = TagCaracter(nome='chNFe'    , codigo='CR09' , tamanho=[44, 44, 44], raiz='//retNFe', obrigatorio=False)
        self.cStat    = TagCaracter(nome='cStat'    , codigo='CR07' , tamanho=[3, 3, 3]   , raiz='//retNFe')
        self.xMotivo  = TagCaracter(nome='xMotivo' , codigo='CR08' , tamanho=[1, 255]    , raiz='//retNFe')
        self.schema  = TagCaracter(nome='procNFe', propriedade='schema', raiz='//retNFe', obrigatorio=False)
        self.procNFe  = TagCaracter(nome='procNFe', codigo='JR12', raiz='//retNFe', obrigatorio=False)
        self.procNFeZip = TagCaracter(nome='procNFeZip', codigo='JR13', raiz='//retNFe', obrigatorio=False)
        self.procNFeGrupoZip = ProcNFeGrupoZip()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<retNFe>'
        xml += self.chNFe.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml

        if self.procNFe.valor:
            xml += self.schema.xml
            xml += self.procNFe.valor
            xml += '</procNFe>'

        xml += self.procNFeZip.xml
        xml += self.procNFeGrupoZip.xml
        xml += '</retNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chNFe.xml    = arquivo
            self.cStat.xml    = arquivo
            self.xMotivo.xml  = arquivo
            self.schema.xml = arquivo

            procNFe = self._le_noh('//retNFe/procNFe')
            if procNFe is not None and len(procNFe):
                procNFe = etree.tostring(procNFe, encoding='unicode')
                procNFe = procNFe.split('<')
                procNFe = '<' + '<'.join(procNFe[2:-1])
                self.procNFe.valor = procNFe
            else:
                self.procNFe.valor = ''

            self.procNFeZip.xml = arquivo
            self.procNFeGrupoZip.xml = arquivo

    xml = property(get_xml, set_xml)


class RetDownloadNFe(XMLNFe):
    def __init__(self):
        super(RetDownloadNFe, self).__init__()
        self.versao = TagDecimal(nome='retDownloadNFe', codigo='IR01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.00', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'         , codigo='IR03', tamanho=[1,   1, 1], raiz='//retDownloadNFe')
        self.verAplic = TagCaracter(nome='verAplic'     , codigo='IR04', tamanho=[1,  20]   , raiz='//retDownloadNFe')
        self.cStat    = TagCaracter(nome='cStat'        , codigo='IR05', tamanho=[1,   3]   , raiz='//retDownloadNFe')
        self.xMotivo  = TagCaracter(nome='xMotivo'      , codigo='IR06', tamanho=[1, 255]   , raiz='//retDownloadNFe')
        self.dhResp   = TagDataHora(nome='dhResp'       , codigo='IR07',                      raiz='//retDownloadNFe')
        self.retNFe   = []
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retDownloadNFe_v1.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.dhResp.xml

        for r in self.retNFe:
            xml += r.xml

        xml += '</retDownloadNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.tpAmb.xml   = arquivo
            self.verAplic.xml   = arquivo
            self.cStat.xml   = arquivo
            self.xMotivo.xml   = arquivo
            self.dhResp.xml   = arquivo
            self.retNFe = self.le_grupo('//retDownloadNFe/retNFe', RetNFe)

    xml = property(get_xml, set_xml)
