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
#from soap_100 import SOAPEnvio, SOAPRetorno, conectar_servico
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os


DIRNAME = os.path.dirname(__file__)


class _InfConsEnviado(XMLNFe):
    xServ = TagCaracter(nome='xServ', codigo='GP04', tamanho=[8, 8]  , raiz='//ConsCad', valor='CONS-CAD')
    UF    = TagCaracter(nome='UF'   , codigo='GP05', tamanho=[2, 2]  , raiz='//ConsCad')
    IE    = TagCaracter(nome='IE'   , codigo='GP06', tamanho=[2, 14] , raiz='//ConsCad', obrigatorio=False)
    CNPJ  = TagCaracter(nome='CNPJ'  , codigo='GP07', tamanho=[3, 14], raiz='//ConsCad', obrigatorio=False)
    CPF   = TagCaracter(nome='CPF'   , codigo='GP08', tamanho=[3, 11], raiz='//ConsCad', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCons>'
        xml += self.xServ.xml
        xml += self.UF.xml
        xml += self.IE.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += '</infCons>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xServ.xml = arquivo
            self.UF.xml    = arquivo
            self.IE.xml    = arquivo
            self.CNPJ.xml  = arquivo
            self.CPF.xml   = arquivo

    xml = property(get_xml, set_xml)
    

class ConsCad(XMLNFe):
    versao = TagDecimal(nome='ConsCad', codigo='GP01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.01', raiz='/')
    infCons = _InfConsEnviado()
    caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL)
    arquivo_esquema = 'consCad_v1.01.xsd'
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infCons.xml
        xml += '</ConsCad>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.infCons.xml = arquivo

    xml = property(get_xml, set_xml)


class _Ender(XMLNFe):
    xLgr    = TagCaracter(nome='xLgr'   , codigo='GR23', tamanho=[1, 255] , raiz='//retConsCad/infCons/infCad/ender', obrigatorio=False)
    nro     = TagCaracter(nome='nro'    , codigo='GR24', tamanho=[1, 60]  , raiz='//retConsCad/infCons/infCad/ender', obrigatorio=False)
    xCpl    = TagCaracter(nome='xCpl'   , codigo='GR25', tamanho=[1, 60]  , raiz='//retConsCad/infCons/infCad/ender', obrigatorio=False)
    xBairro = TagCaracter(nome='xBairro', codigo='GR26', tamanho=[1, 60]  , raiz='//retConsCad/infCons/infCad/ender', obrigatorio=False)
    cMun    = TagInteiro(nome='cMun'    , codigo='GR27', tamanho=[7, 7]   , raiz='//retConsCad/infCons/infCad/ender', obrigatorio=False)
    xMun    = TagCaracter(nome='xMun'   , codigo='GR28', tamanho=[1, 60]  , raiz='//retConsCad/infCons/infCad/ender', obrigatorio=False)
    CEP     = TagInteiro(nome='CEP'     , codigo='GR29', tamanho=[7, 8]   , raiz='//retConsCad/infCons/infCad/ender', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        if self.xLgr.valor or self.nro.valor or self.xCpl.valor or self.xBairro.valor or self.cMun.valor or self.xMun.valor or self.CEP.valor:
            xml += '<ender>'
            xml += self.xLgr.xml
            xml += self.nro.xml
            xml += self.xCpl.xml
            xml += self.xBairro.xml
            xml += self.cMun.xml
            xml += self.xMun.xml
            xml += self.CEP.xml
            xml += '</ender>'
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

    xml = property(get_xml, set_xml)


class _InfCadRecebido(XMLNFe):
    IE       = TagCaracter(nome='IE'      , codigo='GR08' , tamanho=[2, 14], raiz='//retConsCad/infCons/infCad')
    CNPJ     = TagCaracter(nome='CNPJ'    , codigo='GR09' , tamanho=[3, 14], raiz='//retConsCad/infCons/infCad')
    CPF      = TagCaracter(nome='CPF'     , codigo='GR10' , tamanho=[3, 11], raiz='//retConsCad/infCons/infCad')
    UF       = TagCaracter(nome='UF'      , codigo='GR11' , tamanho=[2, 2] , raiz='//retConsCad/infCons/infCad')
    cSit     = TagInteiro(nome='cSit'     , codigo='GR12' , tamanho=[1, 1] , raiz='//retConsCad/infCons/infCad')
    xNome    = TagCaracter(nome='xNome'   , codigo='GR13' , tamanho=[1, 60], raiz='//retConsCad/infCons/infCad', obrigatorio=False)
    xFant    = TagCaracter(nome='xFant'   , codigo='GR13a', tamanho=[1, 60], raiz='//retConsCad/infCons/infCad', obrigatorio=False)
    xRegApur = TagCaracter(nome='xRegApur', codigo='GR14' , tamanho=[1, 60], raiz='//retConsCad/infCons/infCad', obrigatorio=False)
    CNAE     = TagInteiro(nome='CNAE'     , codigo='GR15' , tamanho=[6, 7] , raiz='//retConsCad/infCons/infCad', obrigatorio=False)
    dIniAtiv = TagData(nome='dIniAtiv'    , codigo='GR16' ,                  raiz='//retConsCad/infCons/infCad', obrigatorio=False)
    dUltSit  = TagData(nome='dUltSit'     , codigo='GR17' ,                  raiz='//retConsCad/infCons/infCad', obrigatorio=False)
    dBaixa   = TagData(nome='dBaixa'      , codigo='GR18' ,                  raiz='//retConsCad/infCons/infCad', obrigatorio=False)
    IEUnica  = TagCaracter(nome='IEUnica' , codigo='GR20' , tamanho=[2, 14], raiz='//retConsCad/infCons/infCad', obrigatorio=False)
    IEAtual  = TagCaracter(nome='IEAtual' , codigo='GR21' , tamanho=[2, 14], raiz='//retConsCad/infCons/infCad', obrigatorio=False)
    ender    = _Ender()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCad>'
        xml += self.IE.xml      
        xml += self.CNPJ.xml    
        xml += self.CPF.xml     
        xml += self.UF.xml      
        xml += self.cSit.xml    
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
        if self._le_xml(arquivo):
            self.IE.xml       = arquivo
            self.CNPJ.xml     = arquivo
            self.CPF.xml      = arquivo
            self.UF.xml       = arquivo
            self.cSit.xml     = arquivo
            self.xNome.xml    = arquivo
            self.xFant.xml    = arquivo
            self.xRegApur.xml = arquivo
            self.CNAE.xml     = arquivo
            self.dIniAtiv.xml = arquivo
            self.dUltSit.xml  = arquivo
            self.dBaixa.xml   = arquivo
            self.IEUnica.xml  = arquivo
            self.IEAtual.xml  = arquivo
            self.ender.xml    = arquivo

    xml = property(get_xml, set_xml)


class _InfConsRecebido(XMLNFe):
    verAplic = TagCaracter(nome='verAplic', codigo='GR04' , tamanho=[1, 20]  , raiz='//retConsCad/infCons')
    cStat    = TagInteiro(nome='cStat'    , codigo='GR05' , tamanho=[3, 3, 3], raiz='//retConsCad/infCons')
    xMotivo  = TagCaracter(nome='xMotivo' , codigo='GR06' , tamanho=[1, 255] , raiz='//retConsCad/infCons')
    UF       = TagCaracter(nome='UF'      , codigo='GR06a', tamanho=[2, 2]   , raiz='//retConsCad/infCons')
    IE       = TagCaracter(nome='IE'      , codigo='GR06b', tamanho=[2, 14]  , raiz='//retConsCad/infCons', obrigatorio=False)
    CNPJ     = TagCaracter(nome='CNPJ'    , codigo='GR06c', tamanho=[3, 14]  , raiz='//retConsCad/infCons', obrigatorio=False)
    CPF      = TagCaracter(nome='CPF'     , codigo='GR06d', tamanho=[3, 11]  , raiz='//retConsCad/infCons', obrigatorio=False)
    dhCons   = TagDataHora(nome='dhCons'  , codigo='GR06e',                    raiz='//retConsCad/infCons')
    cUF      = TagInteiro(nome='cUF'      , codigo='GR06f', tamanho=[2, 2, 2], raiz='//retConsCad/infCons')
    infCad   = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCons>'
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.UF.xml
        xml += self.IE.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.dhCons.xml
        xml += self.cUF.xml
        
        if len(self.infCad) > 0:
            for ic in self.infCad:
                xml += ic.xml
                
        xml += '</infCons>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.UF.xml        = arquivo
            self.IE.xml        = arquivo
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.dhCons.xml    = arquivo
            self.cUF.xml       = arquivo
            
            self.infCad = []
            cadastros = self._le_nohs('//retConsCad/infCons/infCad')
            
            if len(cadastros) > 0:
                for c in cadastros:
                    nc = _InfCadRecebido()
                    nc.xml = c
                    self.infCad.append(nc)

    xml = property(get_xml, set_xml)


class RetConsCad(XMLNFe):
    versao = TagDecimal(nome='retConsCad', codigo='GR01', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.01', raiz='/')
    infCons = _InfConsRecebido()
    caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL)
    arquivo_esquema = 'retConsCad_v1.01.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infCons.xml
        xml += '</retConsCad>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            self.infCons.xml = arquivo

    xml = property(get_xml, set_xml)
