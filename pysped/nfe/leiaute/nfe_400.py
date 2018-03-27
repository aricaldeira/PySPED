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

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str

from pysped.xml_sped import *
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_4 as ESQUEMA_ATUAL
from pysped.nfe.leiaute import nfe_310
import os

DIRNAME = os.path.dirname(__file__)


class Deduc(nfe_310.Deduc):
    def __init__(self):
        super(Deduc, self).__init__()


class ForDia(nfe_310.ForDia):
    def __init__(self):
        super(ForDia, self).__init__()


class Cana(nfe_310.Cana):
    def __init__(self):
        super(Cana, self).__init__()


class IPIDevol(nfe_310.IPIDevol):
    def __init__(self):
        super(IPIDevol, self).__init__()


class ImpostoDevol(nfe_310.ImpostoDevol):
    def __init__(self):
        super(ImpostoDevol, self).__init__()


class ISSQN(nfe_310.ISSQN):
    def __init__(self):
        super(ISSQN, self).__init__()


class ICMSUFDest(nfe_310.ICMSUFDest):
    def __init__(self):
        super(ICMSUFDest, self).__init__()
        self.vBCFCPUFDest = TagDecimal(nome='vBCFCPUFDest', codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//det/imposto/ICMSUFDest')

    def get_xml(self):
        if not (self.vBCUFDest.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ICMSUFDest>'
        xml += self.vBCUFDest.xml
        xml += self.vBCFCPUFDest.xml
        xml += self.pFCPUFDest.xml
        xml += self.pICMSUFDest.xml
        xml += self.pICMSInter.xml
        xml += self.pICMSInterPart.xml
        xml += self.vFCPUFDest.xml
        xml += self.vICMSUFDest.xml
        xml += self.vICMSUFRemet.xml
        xml += '</ICMSUFDest>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBCUFDest.xml      = arquivo
            self.vBCFCPUFDest.xml   = arquivo
            self.pFCPUFDest.xml     = arquivo
            self.pICMSUFDest.xml    = arquivo
            self.pICMSInter.xml     = arquivo
            self.pICMSInterPart.xml = arquivo
            self.vFCPUFDest.xml     = arquivo
            self.vICMSUFDest.xml    = arquivo
            self.vICMSUFRemet.xml   = arquivo

    xml = property(get_xml, set_xml)


class COFINSST(nfe_310.COFINSST):
    def __init__(self):
        super(COFINSST, self).__init__()


class TagCSTCOFINS(nfe_310.TagCSTCOFINS):
    def __init__(self, *args, **kwargs):
        super(TagCSTCOFINS, self).__init__(*args, **kwargs)


class COFINS(nfe_310.COFINS):
    def __init__(self):
        super(COFINS, self).__init__()


class PISST(nfe_310.PISST):
    def __init__(self):
        super(PISST, self).__init__()


class TagCSTPIS(nfe_310.TagCSTPIS):
    def __init__(self, *args, **kwargs):
        super(TagCSTPIS, self).__init__(*args, **kwargs)


class PIS(nfe_310.PIS):
    def __init__(self):
        super(PIS, self).__init__()
        self.pPIS      = TagDecimal(nome='pPIS'     , codigo='Q08', tamanho=[1,  5, 1], decimais=[0, 4, 4], raiz='')


class II(nfe_310.II):
    def __init__(self):
        super(II, self).__init__()


class TagCSTIPI(nfe_310.TagCSTIPI):
    def __init__(self, *args, **kwargs):
        super(TagCSTIPI, self).__init__(*args, **kwargs)


class IPI(nfe_310.IPI):
    def __init__(self):
        super(IPI, self).__init__()


class TagCSOSN(nfe_310.TagCSOSN):
    def __init__(self, *args, **kwargs):
        super(TagCSOSN, self).__init__(*args, **kwargs)


class TagCSTICMS(nfe_310.TagCSTICMS):
    def __init__(self, *args, **kwargs):
        super(TagCSTICMS, self).__init__(*args, **kwargs)


class ICMS(nfe_310.ICMS):
    def __init__(self):
        super(ICMS, self).__init__()
        self.pST  = TagDecimal(nome='pST'               , codigo='', tamanho=[1,  3, 1], decimais=[0, 2, 4], raiz='')
        self.vBCFCP = TagDecimal(nome='vBCFCP'          , codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.pFCP = TagDecimal(nome='pFCP'              , codigo='', tamanho=[1,  3, 1], decimais=[0, 2, 4], raiz='')
        self.vFCP = TagDecimal(nome='vFCP'              , codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.vBCFCPST = TagDecimal(nome='vBCFCPST'      , codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.pFCPST = TagDecimal(nome='pFCPST'          , codigo='', tamanho=[1,  3, 1], decimais=[0, 2, 4], raiz='')
        self.vFCPST = TagDecimal(nome='vFCPST'          , codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.vBCFCPSTRet = TagDecimal(nome='vBCFCPSTRet', codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.pFCPSTRet = TagDecimal(nome='pFCPSTRet'    , codigo='', tamanho=[1,  3, 1], decimais=[0, 2, 4], raiz='')
        self.vFCPSTRet = TagDecimal(nome='vFCPSTRet'    , codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.orig = TagCaracter(nome='orig', codigo='', raiz='')

        #
        # Situação tributária do Simples Nacional
        #
        self.CSOSN = TagCSOSN()
        self.CSOSN.grupo_icms = self
        self.CSOSN.valor = '400'

        #
        # Situação tributária tradicional
        #
        self.CST = TagCSTICMS()
        self.CST.grupo_icms = self
        self.CST.valor = '41'

    def get_xml(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += '<ICMS><' + self.nome_tag + '>'
        xml += self.orig.xml

        #
        # Se for regime tradicional (não Simples Nacional)
        #
        if self.regime_tributario != 1:
            xml += self.CST.xml

            if self.CST.valor == '00':
                xml += self.modBC.xml
                xml += self.vBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml

                #xml += self.vBCFCP.xml
                if self.vFCP.valor:
                    xml += self.pFCP.xml
                    xml += self.vFCP.xml

            elif self.CST.valor == '10':
                if not self.partilha:
                    xml += self.modBC.xml
                    xml += self.vBC.xml
                    #xml += self.pRedBC.xml
                    xml += self.pICMS.xml
                    xml += self.vICMS.xml
                    xml += self.modBCST.xml

                    # Somente quando for margem de valor agregado
                    if self.modBCST.valor == 4:
                        xml += self.pMVAST.xml

                    xml += self.pRedBCST.xml
                    xml += self.vBCST.xml
                    xml += self.pICMSST.xml
                    xml += self.vICMSST.xml

                    xml += self.vBCFCPST.xml
                    xml += self.pFCPST.xml
                    xml += self.vFCPST.xml

                else:
                    xml += self.modBC.xml
                    xml += self.vBC.xml
                    xml += self.pRedBC.xml
                    xml += self.pICMS.xml
                    xml += self.vICMS.xml
                    xml += self.modBCST.xml

                    # Somente quando for margem de valor agregado
                    if self.modBCST.valor == 4:
                        xml += self.pMVAST.xml

                    xml += self.pRedBCST.xml
                    xml += self.vBCST.xml
                    xml += self.pICMSST.xml
                    xml += self.vICMSST.xml
                    xml += self.pBCOp.xml
                    xml += self.UFST.xml

            elif self.CST.valor == '20':
                xml += self.modBC.xml
                xml += self.pRedBC.xml
                xml += self.vBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml

                if self.vFCP.valor:
                    xml += self.vBCFCP.xml
                    xml += self.pFCP.xml
                    xml += self.vFCP.xml

                xml += self.vICMSDeson.xml
                xml += self.motDesICMS.xml

            elif self.CST.valor == '30':
                xml += self.modBCST.xml

                # Somente quando for margem de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

                xml += self.vBCFCPST.xml
                xml += self.pFCPST.xml
                xml += self.vFCPST.xml

                xml += self.vICMSDeson.xml
                xml += self.motDesICMS.xml

            elif self.CST.valor in ('40', '41', '50'):
                xml += self.vICMSDeson.xml
                xml += self.motDesICMS.xml

            elif self.CST.valor == '51':
                xml += self.modBC.xml
                xml += self.pRedBC.xml
                xml += self.vBC.xml
                xml += self.pICMS.xml
                xml += self.vICMSOp.xml
                xml += self.pDif.xml
                xml += self.vICMSDif.xml
                xml += self.vICMS.xml
                if self.vFCP.valor:
                    xml += self.vBCFCP.xml
                    xml += self.pFCP.xml
                    xml += self.vFCP.xml

            elif self.CST.valor == '60':
                if (self.vBCSTRet.valor or self.pST.valor or self.vICMSSTRet.valor):
                    xml += self.vBCSTRet.xml
                    xml += self.pST.xml
                    xml += self.vICMSSTRet.xml

                if (self.vBCFCPSTRet.valor or self.pFCPSTRet.valor or self.vFCPSTRet.valor):
                    xml += self.vBCFCPSTRet.xml
                    xml += self.pFCPSTRet.xml
                    xml += self.vFCPSTRet.xml

            elif self.CST.valor == '70':
                xml += self.modBC.xml
                xml += self.vBC.xml
                xml += self.pRedBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml
                xml += self.modBCST.xml

                # Somente quando for margem de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

                xml += self.vBCFCPST.xml
                xml += self.pFCPST.xml
                xml += self.vFCPST.xml

                xml += self.vICMSDeson.xml
                xml += self.motDesICMS.xml

            elif self.CST.valor == '90':
                xml += self.modBC.xml
                xml += self.vBC.xml
                xml += self.pRedBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml

                if self.vFCP.valor:
                    xml += self.vBCFCP.xml
                    xml += self.pFCP.xml
                    xml += self.vFCP.xml

                xml += self.modBCST.xml

                # Somente quando for margem de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

                xml += self.vBCFCPST.xml
                xml += self.pFCPST.xml
                xml += self.vFCPST.xml

                xml += self.vICMSDeson.xml
                xml += self.motDesICMS.xml

                if self.partilha:
                    xml += self.pBCOp.xml
                    xml += self.UFST.xml

        #
        # O regime tributário é o Simples Nacional
        #
        else:
            xml += self.CSOSN.xml

            if self.CSOSN.valor == '101':
                xml += self.pCredSN.xml
                xml += self.vCredICMSSN.xml

            elif self.CSOSN.valor in ('102', '103', '300', '400'):
                pass

            elif self.CSOSN.valor == '201':
                xml += self.modBCST.xml

                # Somente quando for margem de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

                xml += self.vBCFCPST.xml
                xml += self.pFCPST.xml
                xml += self.vFCPST.xml

                xml += self.pCredSN.xml
                xml += self.vCredICMSSN.xml

            elif self.CSOSN.valor in ('202', '203'):
                xml += self.modBCST.xml

                # Somente quando for margem de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

                xml += self.vBCFCPST.xml
                xml += self.pFCPST.xml
                xml += self.vFCPST.xml

            elif self.CSOSN.valor == '500':
                xml += self.vBCSTRet.xml
                xml += self.vICMSSTRet.xml

                xml += self.pST.xml
                xml += self.vBCFCPSTRet.xml
                xml += self.pFCPSTRet.xml
                xml += self.vFCPSTRet.xml

            elif self.CSOSN.valor == '900':
                xml += self.modBC.xml
                xml += self.vBC.xml
                xml += self.pRedBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml
                xml += self.modBCST.xml

                # Somente quando for margem de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

                xml += self.vBCFCPST.xml
                xml += self.pFCPST.xml
                xml += self.vFCPST.xml

                xml += self.pCredSN.xml
                xml += self.vCredICMSSN.xml

        xml += '</' + self.nome_tag + '></ICMS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o ICMS, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            self.partilha = False
            self.repasse  = False

            if self._le_noh('//det/imposto/ICMS/ICMS00') is not None:
                self.regime_tributario = 3
                self.CST.valor = '00'
            elif self._le_noh('//det/imposto/ICMS/ICMS10') is not None:
                self.regime_tributario = 3
                self.CST.valor = '10'
            elif self._le_noh('//det/imposto/ICMS/ICMS20') is not None:
                self.regime_tributario = 3
                self.CST.valor = '20'
            elif self._le_noh('//det/imposto/ICMS/ICMS30') is not None:
                self.regime_tributario = 3
                self.CST.valor = '30'
            elif self._le_noh('//det/imposto/ICMS/ICMS40') is not None:
                self.regime_tributario = 3
                self.CST.valor = '40'
            elif self._le_noh('//det/imposto/ICMS/ICMS51') is not None:
                self.regime_tributario = 3
                self.CST.valor = '51'
            elif self._le_noh('//det/imposto/ICMS/ICMS60') is not None:
                self.regime_tributario = 3
                self.CST.valor = '60'
            elif self._le_noh('//det/imposto/ICMS/ICMS70') is not None:
                self.regime_tributario = 3
                self.CST.valor = '70'
            elif self._le_noh('//det/imposto/ICMS/ICMS90') is not None:
                self.regime_tributario = 3
                self.CST.valor = '90'
            elif self._le_noh('//det/imposto/ICMS/ICMSPart') is not None:
                self.regime_tributario = 3
                self.partilha = True
                self.CST.valor = '10'
            elif self._le_noh('//det/imposto/ICMS/ICMSST') is not None:
                self.regime_tributario = 3
                self.repasse = True
                self.CST.valor = '41'
            elif self._le_noh('//det/imposto/ICMS/ICMSSN101') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = '101'
            elif self._le_noh('//det/imposto/ICMS/ICMSSN102') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = '102'
            elif self._le_noh('//det/imposto/ICMS/ICMSSN201') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = '201'
            elif self._le_noh('//det/imposto/ICMS/ICMSSN202') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = '202'
            elif self._le_noh('//det/imposto/ICMS/ICMSSN500') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = '500'
            elif self._le_noh('//det/imposto/ICMS/ICMSSN900') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = '900'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            self.orig.xml       = arquivo

            if self.regime_tributario == 1:
                self.CSOSN.xml       = arquivo
            else:
                self.CST.xml        = arquivo

            self.modBC.xml      = arquivo
            self.vBC.xml        = arquivo
            self.pRedBC.xml     = arquivo
            self.pICMS.xml      = arquivo
            self.vICMS.xml      = arquivo
            self.vBCFCP.xml     = arquivo
            self.pFCP.xml       = arquivo
            self.vFCP.xml       = arquivo
            self.modBCST.xml    = arquivo
            self.pMVAST.xml     = arquivo
            self.pRedBCST.xml   = arquivo
            self.vBCST.xml      = arquivo
            self.pICMSST.xml    = arquivo
            self.vICMSST.xml    = arquivo
            self.vBCFCPST.xml   = arquivo
            self.pFCPST.xml     = arquivo
            self.vFCPST.xml     = arquivo
            self.vBCSTRet.xml   = arquivo
            self.vICMSSTRet.xml = arquivo
            self.pST.xml        = arquivo
            self.vBCFCPSTRet.xml = arquivo
            self.pFCPSTRet.xml  = arquivo
            self.vFCPSTRet.xml  = arquivo
            self.vICMSDeson.xml = arquivo
            self.vICMSOp.xml    = arquivo
            self.pDif.xml       = arquivo
            self.vICMSDif.xml   = arquivo

            if self.regime_tributario == 1:
                self.pCredSN.xml     = arquivo
                self.vCredICMSSN.xml = arquivo
            else:
                self.UFST.xml        = arquivo
                self.pBCOp.xml       = arquivo
                self.motDesICMS.xml  = arquivo
                self.vBCSTDest.xml   = arquivo
                self.vICMSSTDest.xml = arquivo

    xml = property(get_xml, set_xml)


class Imposto(nfe_310.Imposto):
    def __init__(self):
        super(Imposto, self).__init__()
        self.ICMS = ICMS()
        self.vTotTrib = TagDecimal(nome='vTotTrib', codigo='M02', tamanho=[1, 15, 1], decimais=[0,  2,  2], raiz='//det/imposto', obrigatorio=True)


class CIDE(nfe_310.CIDE):
    def __init__(self):
        super(CIDE, self).__init__()


class Comb(nfe_310.Comb):
    def __init__(self):
        super(Comb, self).__init__()


class Arma(nfe_310.Arma):
    def __init__(self):
        super(Arma, self).__init__()


class Med(nfe_310.Med):
    def __init__(self):
        super(Med, self).__init__()
        self.cProdANVISA = TagCaracter(nome='cProdANVISA', codigo='', tamanho=[1, 13], raiz='//med', obrigatorio=True)

    def get_xml(self):
        if not self.cProdANVISA.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<med>'
        xml += self.cProdANVISA.xml
        xml += self.vPMC.xml
        xml += '</med>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cProdANVISA.xml = arquivo
            self.vPMC.xml  = arquivo

    xml = property(get_xml, set_xml)


class VeicProd(nfe_310.VeicProd):
    def __init__(self):
        super(VeicProd, self).__init__()


class ExportInd(nfe_310.ExportInd):
    def __init__(self):
        super(ExportInd, self).__init__()


class DetExport(nfe_310.DetExport):
    def __init__(self):
        super(DetExport, self).__init__()


class Adi(nfe_310.Adi):
    def __init__(self):
        super(Adi, self).__init__()


class DI(nfe_310.DI):
    def __init__(self):
        super(DI, self).__init__()


class Rastro(XMLNFe):
    def __init__(self):
        super(Rastro, self).__init__()
        self.nLote = TagCaracter(nome='nLote', codigo='', tamanho=[1, 20]                    , raiz='//rastro', obrigatorio=True)
        self.qLote = TagDecimal(nome='qLote' , codigo='', tamanho=[1,  8], decimais=[0, 3, 3], raiz='//rastro', obrigatorio=True)
        self.dFab  = TagData(nome='dFab'     , codigo=''                                     , raiz='//rastro', obrigatorio=True)
        self.dVal  = TagData(nome='dVal'     , codigo=''                                     , raiz='//rastro', obrigatorio=True)

    def get_xml(self):
        if not self.nLote.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<rastro>'
        xml += self.nLote.xml
        xml += self.qLote.xml
        xml += self.dFab.xml
        xml += self.dVal.xml
        xml += '</rastro>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nLote.xml = arquivo
            self.qLote.xml = arquivo
            self.dFab.xml  = arquivo
            self.dVal.xml  = arquivo

    xml = property(get_xml, set_xml)


class Prod(nfe_310.Prod):
    def __init__(self):
        super(Prod, self).__init__()
        self.rastro = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<prod>'
        xml += self.cProd.xml
        xml += self.cEAN.xml
        xml += self.xProd.xml
        xml += self.NCM.xml
        xml += self.NVE.xml
        xml += self.CEST.xml
        xml += self.EXTIPI.xml
        #xml += self.genero.xml
        xml += self.CFOP.xml
        xml += self.uCom.xml
        xml += self.qCom.xml
        xml += self.vUnCom.xml
        xml += self.vProd.xml
        xml += self.cEANTrib.xml
        xml += self.uTrib.xml
        xml += self.qTrib.xml
        xml += self.vUnTrib.xml
        xml += self.vFrete.xml
        xml += self.vSeg.xml
        xml += self.vDesc.xml
        xml += self.vOutro.xml
        xml += self.indTot.xml

        for d in self.DI:
            xml += d.xml

        xml += self.detExport.xml
        xml += self.xPed.xml
        xml += self.nItemPed.xml
        xml += self.nFCI.xml

        for r in self.rastro:
            xml += r.xml

        xml += self.veicProd.xml

        for m in self.med:
            xml += m.xml

        for a in self.arma:
            xml += a.xml

        xml += self.comb.xml
        xml += self.nRECOPI.xml
        xml += '</prod>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cProd.xml    = arquivo
            self.cEAN.xml     = arquivo
            self.xProd.xml    = arquivo
            self.NCM.xml      = arquivo
            self.NVE.xml      = arquivo
            self.CEST.xml      = arquivo
            self.EXTIPI.xml   = arquivo
            #self.genero.xml   = arquivo
            self.CFOP.xml     = arquivo
            self.uCom.xml     = arquivo
            self.qCom.xml     = arquivo
            self.vUnCom.xml   = arquivo
            self.vProd.xml    = arquivo
            self.cEANTrib.xml = arquivo
            self.uTrib.xml    = arquivo
            self.qTrib.xml    = arquivo
            self.vUnTrib.xml  = arquivo
            self.vFrete.xml   = arquivo
            self.vSeg.xml     = arquivo
            self.vDesc.xml    = arquivo
            self.vOutro.xml   = arquivo
            self.indTot.xml   = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.DI = self.le_grupo('//det/prod/DI', DI)

            self.detExport.xml     = arquivo
            self.xPed.xml     = arquivo
            self.nItemPed.xml = arquivo
            self.nFCI.xml     = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.rastro = self.le_grupo('//det/prod/rastro', Rastro)

            self.veicProd.xml = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.med = self.le_grupo('//det/prod/med', Med)
            self.arma = self.le_grupo('//det/prod/arma', Arma)

            self.comb.xml = arquivo
            self.nRECOPI.xml = arquivo

    xml = property(get_xml, set_xml)


class Det(nfe_310.Det):
    def __init__(self):
        super(Det, self).__init__()
        self.prod      = Prod()
        self.imposto   = Imposto()


class Compra(nfe_310.Compra):
    def __init__(self):
        super(Compra, self).__init__()


class Exporta(nfe_310.Exporta):
    def __init__(self):
        super(Exporta, self).__init__()


class ProcRef(nfe_310.ProcRef):
    def __init__(self):
        super(ProcRef, self).__init__()


class ObsFisco(nfe_310.ObsFisco):
    def __init__(self):
        super(ObsFisco, self).__init__()


class ObsCont(nfe_310.ObsCont):
    def __init__(self):
        super(ObsCont, self).__init__()


class InfAdic(nfe_310.InfAdic):
    def __init__(self):
        super(InfAdic, self).__init__()


class Card(nfe_310.Card):
    def __init__(self):
        super(Card, self).__init__()
        self.tpIntegra = TagCaracter(nome='tpIntegra', codigo='', tamanho=[ 1,  1], raiz='//detPag/card')
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='XA05', tamanho=[14, 14], raiz='//detPag/card', obrigatorio=False)
        self.tBand     = TagCaracter(nome='tBand', codigo='YA01', tamanho=[ 2,  2], raiz='//detPag/card', obrigatorio=False)
        self.cAut      = TagCaracter(nome='cAut' , codigo='YA07', tamanho=[20, 20], raiz='//detPag/card', obrigatorio=False)

    def get_xml(self):
        if not (self.tpIntegra.valor or self.CNPJ.valor or self.tBand.valor or self.cAut.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<card>'
        xml += self.tpIntegra.xml
        xml += self.CNPJ.xml
        xml += self.tBand.xml
        xml += self.cAut.xml
        xml += '</card>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpIntegra.xml = arquivo
            self.CNPJ.xml      = arquivo
            self.tBand.xml     = arquivo
            self.cAut.xml      = arquivo

    xml = property(get_xml, set_xml)


class DetPag(nfe_310.Pag):
    def __init__(self):
        super(DetPag, self).__init__()
        self.tPag = TagCaracter(nome='tPag', codigo='YA01', tamanho=[2, 2, 2], raiz='//detPag')
        self.vPag = TagDecimal(nome='vPag' , codigo='YA02', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//detPag')
        self.card = Card()

    def get_xml(self):
        if not (self.tPag.valor or self.vPag.valor or self.card.xml):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<detPag>'
        xml += self.tPag.xml
        xml += self.vPag.xml
        xml += self.card.xml
        xml += '</detPag>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tPag.xml = arquivo
            self.vPag.xml = arquivo
            self.card.xml  = arquivo

    xml = property(get_xml, set_xml)

    @property
    def pagamento_formatado(self):
        TIPOS = {
            '01': 'Dinheiro',
            '02': 'Cheque',
            '03': 'Cartão de crédito',
            '04': 'Cartão de débito',
            '05': 'Crédito loja',
            '10': 'Vale alimentação',
            '11': 'Vale refeição',
            '12': 'Vale presente',
            '13': 'Vale combustível',
            '14': 'Duplicata mercantil',
            '15': 'Boleto bancário',
            '90': 'Sem pagamento',
            '99': 'Outros',
        }

        if self.tPag.valor not in TIPOS:
            return ''

        return TIPOS[self.tPag.valor]


class Pag(XMLNFe):
    def __init__(self):
        super(Pag, self).__init__()
        self.detPag = []
        self.vTroco = TagDecimal(nome='vTroco' , codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//pag')

    def get_xml(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += '<pag>'

        for d in self.detPag:
            xml += d.xml

        xml += self.vTroco.xml
        xml += '</pag>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.detPag = self.le_grupo('//NFe/infNFe/pag/detPag', DetPag)

            self.vTroco.xml  = arquivo

    xml = property(get_xml, set_xml)


class Dup(nfe_310.Dup):
    def __init__(self):
        super(Dup, self).__init__()


class Fat(nfe_310.Fat):
    def __init__(self):
        super(Fat, self).__init__()


class Cobr(nfe_310.Cobr):
    def __init__(self):
        super(Cobr, self).__init__()


class Lacres(nfe_310.Lacres):
    def __init__(self):
        super(Lacres, self).__init__()


class Vol(nfe_310.Vol):
    def __init__(self, xml=None):
        super(Vol, self).__init__()


class Reboque(nfe_310.Reboque):
    def __init__(self):
        super(Reboque, self).__init__()


class VeicTransp(nfe_310.VeicTransp):
    def __init__(self):
        super(VeicTransp, self).__init__()


class RetTransp(nfe_310.RetTransp):
    def __init__(self):
        super(RetTransp, self).__init__()


class Transporta(nfe_310.Transporta):
    def __init__(self):
        super(Transporta, self).__init__()


class Transp(nfe_310.Transp):
    def __init__(self):
        super(Transp, self).__init__()


class RetTrib(nfe_310.RetTrib):
    def __init__(self):
        super(RetTrib, self).__init__()


class ISSQNTot(nfe_310.ISSQNTot):
    def __init__(self):
        super(ISSQNTot, self).__init__()


class ICMSTot(nfe_310.ICMSTot):
    def __init__(self):
        super(ICMSTot, self).__init__()
        self.vFCP = TagDecimal(nome='vFCP', codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot', obrigatorio=True)
        self.vFCPST = TagDecimal(nome='vFCPST', codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot', obrigatorio=True)
        self.vFCPSTRet = TagDecimal(nome='vFCPSTRet', codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot', obrigatorio=True)
        self.vIPIDevol = TagDecimal(nome='vIPIDevol', codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot', obrigatorio=True)
        self.vICMSUFDest = TagDecimal(nome='vICMSUFDest', codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot', obrigatorio=True)
        self.vFCPUFDest = TagDecimal(nome='vFCPUFDest', codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot', obrigatorio=True)
        self.vICMSUFRemet = TagDecimal(nome='vICMSUFRemet', codigo='', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot', obrigatorio=True)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ICMSTot>'
        xml += self.vBC.xml
        xml += self.vICMS.xml
        xml += self.vICMSDeson.xml
        xml += self.vFCP.xml
        xml += self.vBCST.xml
        xml += self.vST.xml
        xml += self.vFCPST.xml
        xml += self.vFCPSTRet.xml
        if self.vICMSUFDest.valor:
            xml += self.vICMSUFDest.xml
        if self.vICMSUFRemet.valor:
            xml += self.vICMSUFRemet.xml
        if self.vFCPUFDest.valor:
            xml += self.vFCPUFDest.xml
        xml += self.vProd.xml
        xml += self.vFrete.xml
        xml += self.vSeg.xml
        xml += self.vDesc.xml
        xml += self.vII.xml
        xml += self.vIPI.xml
        xml += self.vIPIDevol.xml
        xml += self.vPIS.xml
        xml += self.vCOFINS.xml
        xml += self.vOutro.xml
        xml += self.vNF.xml
        xml += self.vTotTrib.xml
        xml += '</ICMSTot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml     = arquivo
            self.vICMS.xml   = arquivo
            self.vICMSDeson.xml = arquivo
            self.vFCPUFDest.xml = arquivo
            self.vICMSUFDest.xml = arquivo
            self.vICMSUFRemet.xml = arquivo
            self.vFCP.xml    = arquivo
            self.vBCST.xml   = arquivo
            self.vST.xml     = arquivo
            self.vFCPST.xml  = arquivo
            self.vFCPSTRet.xml = arquivo
            self.vProd.xml   = arquivo
            self.vFrete.xml  = arquivo
            self.vSeg.xml    = arquivo
            self.vDesc.xml   = arquivo
            self.vII.xml     = arquivo
            self.vIPI.xml    = arquivo
            self.vIPIDevol.xml = arquivo
            self.vPIS.xml    = arquivo
            self.vCOFINS.xml = arquivo
            self.vOutro.xml  = arquivo
            self.vNF.xml     = arquivo
            self.vTotTrib.xml = arquivo

    xml = property(get_xml, set_xml)


class Total(nfe_310.Total):
    def __init__(self):
        super(Total, self).__init__()
        self.ICMSTot = ICMSTot()


class AutXML(nfe_310.AutXML):
    def __init__(self):
        super(AutXML, self).__init__()


class Entrega(nfe_310.Entrega):
    def __init__(self):
        super(Entrega, self).__init__()


class Retirada(nfe_310.Retirada):
    def __init__(self):
        super(Retirada, self).__init__()


class EnderDest(nfe_310.EnderDest):
    def __init__(self):
        super(EnderDest, self).__init__()


class Dest(nfe_310.Dest):
    def __init__(self):
        super(Dest, self).__init__()


class Avulsa(nfe_310.Avulsa):
    def __init__(self):
        super(Avulsa, self).__init__()


class EnderEmit(nfe_310.EnderEmit):
    def __init__(self):
        super(EnderEmit, self).__init__()


class Emit(nfe_310.Emit):
    def __init__(self):
        super(Emit, self).__init__()


class RefECF(nfe_310.RefECF):
    def __init__(self):
        super(RefECF, self).__init__()


class RefNFP(nfe_310.RefNFP):
    def __init__(self):
        super(RefNFP, self).__init__()


class RefNF(nfe_310.RefNF):
    def __init__(self):
        super(RefNF, self).__init__()


class NFRef(nfe_310.NFRef):
    def __init__(self):
        super(NFRef, self).__init__()


class Ide(nfe_310.Ide):
    def __init__(self):
        super(Ide, self).__init__()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ide>'
        xml += self.cUF.xml
        xml += self.cNF.xml
        xml += self.natOp.xml
        #xml += self.indPag.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNF.xml
        xml += self.dhEmi.xml

        self.dEmi.valor = self.dhEmi.valor

        if self.mod.valor == '55':
            xml += self.dhSaiEnt.xml

        self.dSaiEnt.valor = self.dhSaiEnt.valor
        self.hSaiEnt.valor = self.hSaiEnt.valor

        xml += self.tpNF.xml
        xml += self.idDest.xml

        xml += self.cMunFG.xml
        xml += self.tpImp.xml
        xml += self.tpEmis.xml
        xml += self.cDV.xml
        xml += self.tpAmb.xml
        xml += self.finNFe.xml

        xml += self.indFinal.xml
        xml += self.indPres.xml

        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += self.dhCont.xml
        xml += self.xJust.xml

        for nr in self.NFref:
            xml += nr.xml

        xml += '</ide>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml     = arquivo
            self.cNF.xml     = arquivo
            self.natOp.xml   = arquivo
            self.indPag.xml  = arquivo
            self.mod.xml     = arquivo
            self.serie.xml   = arquivo
            self.nNF.xml     = arquivo
            self.dEmi.xml    = arquivo
            self.dhEmi.xml   = arquivo
            self.dSaiEnt.xml = arquivo
            self.dhSaiEnt.xml = arquivo
            self.hSaiEnt.xml = arquivo
            self.tpNF.xml    = arquivo
            self.idDest.xml  = arquivo
            self.cMunFG.xml  = arquivo

            self.dEmi.valor = self.dhEmi.valor
            self.dSaiEnt.valor = self.dhSaiEnt.valor
            self.hSaiEnt.valor = self.hSaiEnt.valor

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.NFref = self.le_grupo('//NFe/infNFe/ide/NFref', NFRef)

            self.tpImp.xml   = arquivo
            self.tpEmis.xml  = arquivo
            self.cDV.xml     = arquivo
            self.tpAmb.xml   = arquivo
            self.finNFe.xml  = arquivo
            self.indFinal.xml = arquivo
            self.indPres.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo
            self.dhCont.xml  = arquivo
            self.xJust.xml   = arquivo

    xml = property(get_xml, set_xml)


class CSC(nfe_310.CSC):
    def __init__(self):
        super(CSC, self).__init__()


class InfNFe(nfe_310.InfNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.versao   = TagDecimal(nome='infNFe' , codigo='A01', propriedade='versao', raiz='//NFe', namespace=NAMESPACE_NFE, valor='4.00')
        self.ide      = Ide()
        self.emit     = Emit()
        self.emit.csc = CSC()
        self.avulsa   = Avulsa()
        self.dest     = Dest()
        self.dest.modelo = self.ide.mod.valor
        self.retirada = Retirada()
        self.entrega  = Entrega()
        self.autXML   = []
        self.det      = []
        self.total    = Total()
        self.transp   = Transp()
        self.cobr     = Cobr()
        self.pag      = Pag()
        self.exporta  = Exporta()
        self.compra   = Compra()
        self.cana     = Cana()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infNFe versao="' + str(self.versao.valor) + '" Id="' + self.Id.valor + '">'
        xml += self.ide.xml
        xml += self.emit.xml
        xml += self.avulsa.xml
        xml += self.dest.xml
        xml += self.retirada.xml
        xml += self.entrega.xml

        for a in self.autXML:
            xml += a.xml

        for d in self.det:
            d.imposto.ICMS.regime_tributario = self.emit.CRT.valor
            d.imposto.ISSQN.regime_tributario = self.emit.CRT.valor
            xml += d.xml

        xml += self.total.xml
        xml += self.transp.xml

        if self.ide.mod.valor == '55':
            xml += self.cobr.xml

        xml += self.pag.xml

        xml += self.infAdic.xml
        xml += self.exporta.xml
        xml += self.compra.xml
        xml += self.cana.xml
        xml += '</infNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.Id.xml       = arquivo
            self.ide.xml      = arquivo
            self.emit.xml     = arquivo
            self.avulsa.xml   = arquivo
            self.dest.xml     = arquivo

            self.dest.modelo = self.ide.mod.valor

            self.retirada.xml = arquivo
            self.entrega.xml  = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.autXML = self.le_grupo('//NFe/infNFe/autXML', AutXML)
            self.det = self.le_grupo('//NFe/infNFe/det', Det)
            for i in range(len(self.det)):
                d = self.det[i]
                d.imposto.ICMS.regime_tributario = self.emit.CRT.valor
                d.imposto.ISSQN.regime_tributario = self.emit.CRT.valor
                self.det[i] = d

            self.total.xml    = arquivo
            self.transp.xml   = arquivo
            self.cobr.xml     = arquivo

            self.pag = self.le_grupo('//NFe/infNFe/pag', Pag)

            self.infAdic.xml  = arquivo
            self.exporta.xml  = arquivo
            self.compra.xml   = arquivo
            self.cana.xml     = arquivo

    xml = property(get_xml, set_xml)


class InfNFeSupl(nfe_310.InfNFeSupl):
    def __init__(self):
        super(InfNFeSupl, self).__init__()


class NFe(nfe_310.NFe):
    def __init__(self):
        super(NFe, self).__init__()
        self.infNFe = InfNFe()
        self.infNFeSupl = InfNFeSupl()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'nfe_v4.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<NFe xmlns="http://www.portalfiscal.inf.br/nfe">'
        xml += self.infNFe.xml

        if str(self.infNFe.ide.mod.valor) == '65':
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


class NFCe(NFe):
    def __init__(self):
        super(NFCe, self).__init__()
        self.infNFe.ide.mod.valor = '65'  #  NFC-e
        self.infNFe.ide.tpImp.valor = '4'  #  DANFE NFC-e em papel
        self.infNFe.ide.indPres.valor = '1'  #  Operação presencial
        self.infNFe.ide.indFinal.valor = '1'  #  Consumidor final
        self.infNFe.transp.modFrete.valor = 9  #  Sem frete
        self.infNFe.dest.modelo = '65'


class NFSe(NFe):
    def __init__(self):
        super(NFSe, self).__init__()
        self.infNFe.ide.mod.valor = '99'  #  NFS-e
        self.infNFe.ide.tpImp.valor = '4'  #  DANFE NFS-e em papel
        self.infNFe.ide.indFinal.valor = '1'  #  Consumidor final
        self.infNFe.transp.modFrete.valor = 9  #  Sem frete
        self.infNFe.dest.modelo = '99'
