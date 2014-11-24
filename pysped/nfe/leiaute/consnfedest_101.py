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

from pysped.xml_sped import (ABERTURA, NAMESPACE_NFE, TagCaracter,
                             TagDataHora, TagDecimal, TagInteiro, XMLNFe,
                             TagData, TagDataHoraUTC)
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


CONS_NFE_TODAS = '0'
CONS_NFE_SEM_CONFIRMACAO_OPERACAO = '1'
CONS_NFE_SEM_CIENCIA_OPERACAO = '2'

CONS_NFE_EMISSAO_TODOS_EMITENTES = '0'
CONS_NFE_EMISSAO_SOMENTE_TERCEIROS = '1'


class ConsNFeDest(XMLNFe):
    def __init__(self):
        super(ConsNFeDest, self).__init__()
        self.versao    = TagDecimal(nome='consNFeDest', codigo='IP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.01', raiz='/')
        self.tpAmb = TagInteiro(nome='tpAmb'   , codigo='IP03', tamanho=[ 1,  1, 1] , raiz='//consNFeDest', valor=2)
        self.xServ = TagCaracter(nome='xServ'  , codigo='IP04', tamanho=[18, 18]    , raiz='//consNFeDest', valor='CONSULTAR NFE DEST')
        self.CNPJ  = TagCaracter(nome='CNPJ'  , codigo='IP05', tamanho=[14, 14], raiz='//consNFeDest')
        self.indNFe = TagInteiro(nome='indNFe'   , codigo='IP06', tamanho=[ 1,  1, 1] , raiz='//consNFeDest', valor=CONS_NFE_TODAS)
        self.indEmi = TagInteiro(nome='indEmi'   , codigo='IP07', tamanho=[ 1,  1, 1] , raiz='//consNFeDest', valor=CONS_NFE_EMISSAO_TODOS_EMITENTES)
        self.ultNSU = TagCaracter(nome='ultNSU'   , codigo='IP08', tamanho=[1, 15], raiz='//consNFeDest', valor='0')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consNFeDest_v1.01.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.CNPJ.xml
        xml += self.indNFe.xml
        xml += self.indEmi.xml
        xml += self.ultNSU.xml
        xml += '</consNFeDest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml = arquivo
            self.xServ.xml = arquivo
            self.CNPJ.xml = arquivo
            self.indNFe.xml = arquivo
            self.indEmi.xml = arquivo
            self.ultNSU.xml = arquivo

    xml = property(get_xml, set_xml)



class ResNFe(XMLNFe):
    def __init__(self):
        super(ResNFe, self).__init__()
        self.NSU      = TagCaracter(nome='resNFe', propriedade='NSU', raiz='/')
        self.chNFe    = TagCaracter(nome='chNFe' , tamanho=[44, 44], raiz='//resNFe')
        self.CNPJ     = TagCaracter(nome='CNPJ'  , tamanho=[14, 14], raiz='//resNFe', obrigatorio=False)
        self.CPF      = TagCaracter(nome='CPF'   , tamanho=[11, 11], raiz='//resNFe', obrigatorio=False)
        self.xNome    = TagCaracter(nome='xNome' , tamanho=[ 1, 60], raiz='//resNFe')
        self.IE       = TagCaracter(nome='IE'    , tamanho=[ 2, 14], raiz='//resNFe', obrigatorio=False)
        self.dEmi     = TagData(nome='dEmi'      ,                   raiz='//resNFe', obrigatorio=False)
        self.tpNF     = TagCaracter(nome='tpNF'  , tamanho=[ 1,  1], raiz='//resNFe')
        self.vNF      = TagDecimal(nome='vNF'    , tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//resNFe')
        self.digVal   = TagCaracter(nome='digVal', tamanho=[28, 28], raiz='//resNFe')
        self.dhRecbto = TagDataHoraUTC(nome='dhRecbto', raiz='//resNFe')
        self.cSitNFe  = TagCaracter(nome='cSitNFe', tamanho=[ 1,  1], raiz='//resNFe')
        self.cSitConf = TagCaracter(nome='cSitConf', tamanho=[ 1,  1], raiz='//resNFe')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ret>'
        xml += self.NSU.xml
        xml += self.chNFe.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.xNome.xml
        xml += self.IE.xml
        xml += self.dEmi.xml
        xml += self.tpNF.xml
        xml += self.vNF.xml
        xml += self.digVal.xml
        xml += self.dhRecbto.xml
        xml += self.cSitNFe.xml
        xml += self.cSitConf.xml
        xml += '</resNFe>'
        xml += '</ret>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.NSU.xml   = arquivo
            self.chNFe.xml   = arquivo
            self.CNPJ.xml   = arquivo
            self.CPF.xml   = arquivo
            self.xNome.xml   = arquivo
            self.IE.xml   = arquivo
            self.dEmi.xml   = arquivo
            self.tpNF.xml   = arquivo
            self.vNF.xml   = arquivo
            self.digVal.xml   = arquivo
            self.dhRecbto.xml   = arquivo
            self.cSitNFe.xml   = arquivo
            self.cSitConf.xml   = arquivo

    xml = property(get_xml, set_xml)


class ResCanc(XMLNFe):
    def __init__(self):
        super(ResCanc, self).__init__()
        self.NSU      = TagCaracter(nome='resCanc', propriedade='NSU', raiz='/')
        self.chNFe    = TagCaracter(nome='chNFe' , tamanho=[44, 44], raiz='//resCanc')
        self.CNPJ     = TagCaracter(nome='CNPJ'  , tamanho=[14, 14], raiz='//resCanc', obrigatorio=False)
        self.CPF      = TagCaracter(nome='CPF'   , tamanho=[11, 11], raiz='//resCanc', obrigatorio=False)
        self.xNome    = TagCaracter(nome='xNome' , tamanho=[ 1, 60], raiz='//resCanc')
        self.IE       = TagCaracter(nome='IE'    , tamanho=[ 2, 14], raiz='//resCanc', obrigatorio=False)
        self.dEmi     = TagData(nome='dEmi'      ,                   raiz='//resCanc', obrigatorio=False)
        self.tpNF     = TagCaracter(nome='tpNF'  , tamanho=[ 1,  1], raiz='//resCanc')
        self.vNF      = TagDecimal(nome='vNF'    , tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//resCanc')
        self.digVal   = TagCaracter(nome='digVal', tamanho=[28, 28], raiz='//resCanc')
        self.dhRecbto = TagDataHoraUTC(nome='dhRecbto', raiz='//resCanc')
        self.cSitNFe  = TagCaracter(nome='cSitNFe', tamanho=[ 1,  1], raiz='//resCanc')
        self.cSitConf = TagCaracter(nome='cSitConf', tamanho=[ 1,  1], raiz='//resCanc')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ret>'
        xml += self.NSU.xml
        xml += self.chNFe.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.xNome.xml
        xml += self.IE.xml
        xml += self.dEmi.xml
        xml += self.tpNF.xml
        xml += self.vNF.xml
        xml += self.digVal.xml
        xml += self.dhRecbto.xml
        xml += self.cSitNFe.xml
        xml += self.cSitConf.xml
        xml += '</resCanc>'
        xml += '</ret>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.NSU.xml   = arquivo
            self.chNFe.xml   = arquivo
            self.CNPJ.xml   = arquivo
            self.CPF.xml   = arquivo
            self.xNome.xml   = arquivo
            self.IE.xml   = arquivo
            self.dEmi.xml   = arquivo
            self.tpNF.xml   = arquivo
            self.vNF.xml   = arquivo
            self.digVal.xml   = arquivo
            self.dhRecbto.xml   = arquivo
            self.cSitNFe.xml   = arquivo
            self.cSitConf.xml   = arquivo

    xml = property(get_xml, set_xml)


class RetConsNFeDest(XMLNFe):
    def __init__(self):
        super(RetConsNFeDest, self).__init__()
        self.versao   = TagDecimal(nome='retConsNFeDest', codigo='IR01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.01', raiz='/')
        self.tpAmb    = TagInteiro(nome='tpAmb'         , codigo='IR03', tamanho=[1,   1, 1], raiz='//retConsNFeDest')
        self.verAplic = TagCaracter(nome='verAplic'     , codigo='IR04', tamanho=[1,  20]   , raiz='//retConsNFeDest')
        self.cStat    = TagCaracter(nome='cStat'        , codigo='IR05', tamanho=[1,   3]   , raiz='//retConsNFeDest')
        self.xMotivo  = TagCaracter(nome='xMotivo'      , codigo='IR06', tamanho=[1, 255]   , raiz='//retConsNFeDest')
        self.dhResp   = TagDataHora(nome='dhResp'       , codigo='IR07',                      raiz='//retConsNFeDest')
        self.indCont  = TagCaracter(nome='indCont'      , codigo='IR08', tamanho=[1,   1, 1], raiz='//retConsNFeDest', obrigatorio=False)
        self.ultNSU   = TagCaracter(nome='ultNSU'       , codigo='IP09', tamanho=[1, 15]    , raiz='//retConsNFeDest', obrigatorio=False)
        self.resNFe   = []
        self.resCanc  = []
        self.resCCe   = []

        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retconsNFeDest_v1.01.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.dhResp.xml
        xml += self.indCont.xml
        xml += self.ultNSU.xml

        for n in self.resNFe:
            xml += n.xml

        for n in self.resCanc:
            xml += n.xml

        for n in self.resCCe:
            xml += n.xml

        xml += '</retConsNFeDest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.tpAmb.xml   = arquivo
            self.verAplic.xml   = arquivo
            self.cStat.xml   = arquivo
            self.xMotivo.xml   = arquivo
            self.dhResp.xml   = arquivo
            self.indCont.xml   = arquivo
            self.ultNSU.xml   = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.resNFe = self.le_grupo('//ret/resNFe', ResNFe)
            self.resCanc = self.le_grupo('//ret/resCanc', ResCanc)
            #self.resCCe = self.le_grupo('//ret/resCCe', ResCCe)

    xml = property(get_xml, set_xml)
