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

from pysped.xml_sped import (NAMESPACE_NFE, Signature, TagCaracter,
                             TagDataHora, TagDecimal, TagHora, TagInteiro, XMLNFe)
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL
from pysped.nfe.leiaute import nfe_110
import os

DIRNAME = os.path.dirname(__file__)


class Deduc(XMLNFe):
    def __init__(self):
        super(Deduc, self).__init__()
        self.xDed = TagCaracter(nome='xDed', codigo='ZC11', tamanho=[1, 60]                       , raiz='//deduc')
        self.vDed = TagDecimal(nome='vDed' , codigo='ZC12', tamanho=[1, 15, 1], decimais=[1, 2, 2], raiz='//deduc')

    def get_xml(self):
        if not (self.xDed.valor or self.vDed.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<deduc>'
        xml += self.xDed.xml
        xml += self.vDed.xml
        xml += '</deduc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xDed.xml = arquivo
            self.vDed.xml = arquivo

    xml = property(get_xml, set_xml)


class ForDia(XMLNFe):
    def __init__(self):
        super(ForDia, self).__init__()
        self.dia  = TagInteiro(nome='dia' , codigo='ZC05', tamanho=[1,  2, 1]                      , raiz='//forDia')
        self.qtde = TagDecimal(nome='qtde', codigo='ZC06', tamanho=[1, 11, 1], decimais=[1, 10, 10], raiz='//forDia')

    def get_xml(self):
        if not (self.dia.valor or self.qtde.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<forDia>'
        xml += self.dia.xml
        xml += self.qtde.xml
        xml += '</forDia>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dia.xml  = arquivo
            self.qtde.xml = arquivo

    xml = property(get_xml, set_xml)


class Cana(XMLNFe):
    def __init__(self):
        super(Cana, self).__init__()
        self.safra   = TagCaracter(nome='safra' , codigo='ZC02', tamanho=[4,  9]                         , raiz='//NFe/infNFe/cana')
        self.ref     = TagCaracter(nome='ref'   , codigo='ZC03', tamanho=[6,  6]                         , raiz='//NFe/infNFe/cana')
        self.forDia  = []
        self.qTotMes = TagDecimal(nome='qTotMes', codigo='ZC07', tamanho=[1, 11, 1], decimais=[1, 10, 10], raiz='//NFe/infNFe/cana')
        self.qTotAnt = TagDecimal(nome='qTotAnt', codigo='ZC08', tamanho=[1, 11, 1], decimais=[1, 10, 10], raiz='//NFe/infNFe/cana')
        self.qTotGer = TagDecimal(nome='qTotGer', codigo='ZC09', tamanho=[1, 11, 1], decimais=[1, 10, 10], raiz='//NFe/infNFe/cana')
        self.deduc   = []
        self.vFor    = TagDecimal(nome='vFor'   , codigo='ZC13', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz='//NFe/infNFe/cana')
        self.vTotDed = TagDecimal(nome='vTotDed', codigo='ZC14', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz='//NFe/infNFe/cana')
        self.vLiqFor = TagDecimal(nome='vLiqFor', codigo='ZC15', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz='//NFe/infNFe/cana')

    def get_xml(self):
        if not (self.safra.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<cana>'
        xml += self.safra.xml
        xml += self.ref.xml

        for fd in self.forDia:
            xml += fd.xml

        xml += self.qTotMes.xml
        xml += self.qTotAnt.xml
        xml += self.qTotGer.xml

        for d in self.deduc:
            xml += d.xml

        xml += self.vFor.xml
        xml += self.vTotDed.xml
        xml += self.vLiqFor.xml
        xml += '</cana>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.safra.xml   = arquivo
            self.ref.xml     = arquivo
            self.forDia      = self.le_grupo('//NFe/infNFe/cana/forDia', ForDia)
            self.qTotMes.xml = arquivo
            self.qTotAnt.xml = arquivo
            self.qTotGer.xml = arquivo
            self.deduc       = self.le_grupo('//NFe/infNFe/cana/deduc', Deduc)
            self.vFor.xml    = arquivo
            self.vTotDed.xml = arquivo
            self.vLiqFor.xml = arquivo

    xml = property(get_xml, set_xml)


class ISSQN(nfe_110.ISSQN):
    def __init__(self):
        super(ISSQN, self).__init__()
        self.cSitTrib  = TagCaracter(nome='cSitTrib', codigo='U07', tamanho=[1,  1], raiz='//det/imposto/ISSQN')

    def get_xml(self):
        if not (self.cSitTrib.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ISSQN>'
        xml += self.vBC.xml
        xml += self.vAliq.xml
        xml += self.vISSQN.xml
        xml += self.cMunFG.xml
        xml += self.cListServ.xml
        xml += self.cSitTrib.xml
        xml += '</ISSQN>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml       = arquivo
            self.vAliq.xml     = arquivo
            self.vISSQN.xml    = arquivo
            self.cMunFG.xml    = arquivo
            self.cListServ.xml = arquivo
            self.cSitTrib.xml  = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.cSitTrib.valor):
            return ''

        txt = 'U|'
        txt += self.vBC.txt + '|'
        txt += self.vAliq.txt + '|'
        txt += self.vISSQN.txt + '|'
        txt += self.cMunFG.txt + '|'
        txt += self.cListServ.txt + '|'
        txt += self.cSitTrib.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class COFINSST(nfe_110.COFINSST):
    def __init__(self):
        super(COFINSST, self).__init__()


class TagCSTCOFINS(nfe_110.TagCSTCOFINS):
    def __init__(self, *args, **kwargs):
        super(TagCSTCOFINS, self).__init__(*args, **kwargs)


class COFINS(nfe_110.COFINS):
    def __init__(self):
        super(COFINS, self).__init__()


class PISST(nfe_110.PISST):
    def __init__(self):
        super(PISST, self).__init__()


class TagCSTPIS(nfe_110.TagCSTPIS):
    def __init__(self, *args, **kwargs):
        super(TagCSTPIS, self).__init__(*args, **kwargs)


class PIS(nfe_110.PIS):
    def __init__(self):
        super(PIS, self).__init__()


class II(nfe_110.II):
    def __init__(self):
        super(II, self).__init__()


class TagCSTIPI(nfe_110.TagCSTIPI):
    def __init__(self, *args, **kwargs):
        super(TagCSTIPI, self).__init__(*args, **kwargs)


class IPI(nfe_110.IPI):
    def __init__(self):
        super(IPI, self).__init__()


class TagCSOSN(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagCSOSN, self).__init__(*args, **kwargs)
        self.nome = 'CSOSN'
        self.codigo = 'N12a'
        self.tamanho = [3, 3]
        self.raiz = ''
        self.grupo_icms = None

    def set_valor(self, novo_valor):
        super(TagCSOSN, self).set_valor(novo_valor)

        if not self.grupo_icms:
            return None

        #
        # Definimos todas as tags como não obrigatórias
        #
        self.grupo_icms.modBC.obrigatorio       = False
        self.grupo_icms.vBC.obrigatorio         = False
        self.grupo_icms.pRedBC.obrigatorio      = False
        self.grupo_icms.pICMS.obrigatorio       = False
        self.grupo_icms.vICMS.obrigatorio       = False
        self.grupo_icms.modBCST.obrigatorio     = False
        self.grupo_icms.pMVAST.obrigatorio      = False
        self.grupo_icms.pRedBCST.obrigatorio    = False
        self.grupo_icms.vBCST.obrigatorio       = False
        self.grupo_icms.pICMSST.obrigatorio     = False
        self.grupo_icms.vICMSST.obrigatorio     = False
        self.grupo_icms.vBCSTRet.obrigatorio    = False
        self.grupo_icms.vICMSSTRet.obrigatorio  = False
        self.grupo_icms.pCredSN.obrigatorio     = False
        self.grupo_icms.vCredICMSSN.obrigatorio = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo ICMS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_icms.modBC.valor       = 3
        self.grupo_icms.vBC.valor         = '0.00'
        self.grupo_icms.pRedBC.valor      = '0.00'
        self.grupo_icms.pICMS.valor       = '0.00'
        self.grupo_icms.vICMS.valor       = '0.00'
        self.grupo_icms.modBCST.valor     = 4
        self.grupo_icms.pMVAST.valor      = '0.00'
        self.grupo_icms.pRedBCST.valor    = '0.00'
        self.grupo_icms.vBCST.valor       = '0.00'
        self.grupo_icms.pICMSST.valor     = '0.00'
        self.grupo_icms.vICMSST.valor     = '0.00'
        self.grupo_icms.vBCSTRet.valor    = '0.00'
        self.grupo_icms.vICMSSTRet.valor  = '0.00'
        self.grupo_icms.pCredSN.valor     = '0.00'
        self.grupo_icms.vCredICMSSN.valor = '0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de ICMS
        #
        # Definimos também o valor da tag CST do ICMS
        # tradicional para mapear os novos valores
        # na impressão do DANFE
        #
        # Mapeamento de acordo com a Nota Técnica 2009.004
        #
        #
        # Usamos a propriedade privada, para evitar
        # o processamento do set_valor da classe TagCSTICMS
        #
        if self.valor == '101':
            self.grupo_icms.nome_tag = 'ICMSSN101'
            self.grupo_icms.nome_tag_txt = 'N10c'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMSSN101'
            self.grupo_icms.pCredSN.obrigatorio     = True
            self.grupo_icms.vCredICMSSN.obrigatorio = True
            self.grupo_icms.CST._valor_string       = '41'

        elif self.valor in ('102', '103', '300', '400'):
            self.grupo_icms.nome_tag = 'ICMSSN102'
            self.grupo_icms.nome_tag_txt = 'N10d'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMSSN102'
            self.grupo_icms.CST._valor_string       = '41'

        elif self.valor == '201':
            self.grupo_icms.nome_tag = 'ICMSSN201'
            self.grupo_icms.nome_tag_txt = 'N10e'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMSSN201'
            self.grupo_icms.modBCST.obrigatorio     = True
            self.grupo_icms.vBCST.obrigatorio       = True
            self.grupo_icms.pICMSST.obrigatorio     = True
            self.grupo_icms.vICMSST.obrigatorio     = True
            self.grupo_icms.pCredSN.obrigatorio     = True
            self.grupo_icms.vCredICMSSN.obrigatorio = True
            self.grupo_icms.CST._valor_string       = '30'

        elif self.valor in ('202', '203'):
            self.grupo_icms.nome_tag = 'ICMSSN202'
            self.grupo_icms.nome_tag_txt = 'N10f'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMSSN202'
            self.grupo_icms.modBCST.obrigatorio     = True
            self.grupo_icms.vBCST.obrigatorio       = True
            self.grupo_icms.pICMSST.obrigatorio     = True
            self.grupo_icms.vICMSST.obrigatorio     = True
            self.grupo_icms.CST._valor_string       = '30'

        elif self.valor == '500':
            self.grupo_icms.nome_tag = 'ICMSSN500'
            self.grupo_icms.nome_tag_txt = 'N10g'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMSSN500'
            self.grupo_icms.vBCSTRet.obrigatorio    = True
            self.grupo_icms.vICMSSTRet.obrigatorio  = True
            self.grupo_icms.CST._valor_string       = '60'

        elif self.valor == '900':
            self.grupo_icms.nome_tag = 'ICMSSN900'
            self.grupo_icms.nome_tag_txt = 'N10h'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMSSN900'
            self.grupo_icms.modBC.obrigatorio       = True
            self.grupo_icms.vBC.obrigatorio         = True
            self.grupo_icms.pICMS.obrigatorio       = True
            self.grupo_icms.vICMS.obrigatorio       = True
            self.grupo_icms.modBCST.obrigatorio     = True
            self.grupo_icms.vBCST.obrigatorio       = True
            self.grupo_icms.pICMSST.obrigatorio     = True
            self.grupo_icms.vICMSST.obrigatorio     = True
            self.grupo_icms.pCredSN.obrigatorio     = True
            self.grupo_icms.vCredICMSSN.obrigatorio = True
            self.grupo_icms.CST._valor_string       = '90'

        #
        # Redefine a raiz para todas as tags do grupo ICMS
        #
        self.grupo_icms.orig.raiz        = self.grupo_icms.raiz_tag
        self.grupo_icms.CSOSN.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.modBC.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.vBC.raiz         = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBC.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMS.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMS.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.modBCST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.pMVAST.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBCST.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCST.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMSST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCSTRet.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSSTRet.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.pCredSN.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.vCredICMSSN.raiz = self.grupo_icms.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class TagCSTICMS(nfe_110.TagCSTICMS):
    def __init__(self, *args, **kwargs):
        super(TagCSTICMS, self).__init__(*args, **kwargs)
        self.nome = 'CST'
        self.codigo = 'N12'
        self.tamanho = [2, 2]
        self.raiz = ''
        self.grupo_icms = None

    def set_valor(self, novo_valor):
        super(TagCSTICMS, self).set_valor(novo_valor)

        if not self.grupo_icms:
            return None

        #
        # Definimos todas as tags como não obrigatórias
        #
        self.grupo_icms.modBC.obrigatorio       = False
        self.grupo_icms.vBC.obrigatorio         = False
        self.grupo_icms.pRedBC.obrigatorio      = False
        self.grupo_icms.pICMS.obrigatorio       = False
        self.grupo_icms.vICMS.obrigatorio       = False
        self.grupo_icms.modBCST.obrigatorio     = False
        self.grupo_icms.pMVAST.obrigatorio      = False
        self.grupo_icms.pRedBCST.obrigatorio    = False
        self.grupo_icms.vBCST.obrigatorio       = False
        self.grupo_icms.pICMSST.obrigatorio     = False
        self.grupo_icms.vICMSST.obrigatorio     = False
        self.grupo_icms.motDesICMS.obrigatorio  = False
        self.grupo_icms.vBCSTRet.obrigatorio    = False
        self.grupo_icms.vICMSSTRet.obrigatorio  = False
        self.grupo_icms.vBCSTDest.obrigatorio   = False
        self.grupo_icms.vICMSSTDest.obrigatorio = False
        self.grupo_icms.UFST.obrigatorio        = False
        self.grupo_icms.pBCOp.obrigatorio       = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo ICMS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_icms.modBC.valor       = 3
        self.grupo_icms.vBC.valor         = '0.00'
        self.grupo_icms.pRedBC.valor      = '0.00'
        self.grupo_icms.pICMS.valor       = '0.00'
        self.grupo_icms.vICMS.valor       = '0.00'
        self.grupo_icms.modBCST.valor     = 4
        self.grupo_icms.pMVAST.valor      = '0.00'
        self.grupo_icms.pRedBCST.valor    = '0.00'
        self.grupo_icms.vBCST.valor       = '0.00'
        self.grupo_icms.pICMSST.valor     = '0.00'
        self.grupo_icms.vICMSST.valor     = '0.00'
        self.grupo_icms.motDesICMS.valor  = 0
        self.grupo_icms.vBCSTRet.valor    = '0.00'
        self.grupo_icms.vICMSSTRet.valor  = '0.00'
        self.grupo_icms.vBCSTDest.valor   = '0.00'
        self.grupo_icms.vICMSSTDest.valor = '0.00'
        self.grupo_icms.UFST.valor        = ''
        self.grupo_icms.pBCOp.valor       = '0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de ICMS
        #
        if self.valor == '00':
            self.grupo_icms.nome_tag = 'ICMS00'
            self.grupo_icms.nome_tag_txt = 'N02'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMS00'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True

        elif self.valor == '10':
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

            if not self.grupo_icms.partilha:
                self.grupo_icms.nome_tag = 'ICMS10'
                self.grupo_icms.nome_tag_txt = 'N03'
                self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMS10'
            else:
                self.grupo_icms.nome_tag = 'ICMSPart'
                self.grupo_icms.nome_tag_txt = 'N10a'
                self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMSPart'
                self.grupo_icms.pBCOp.obrigatorio    = True
                self.grupo_icms.UFST.obrigatorio     = True

        elif self.valor == '20':
            self.grupo_icms.nome_tag = 'ICMS20'
            self.grupo_icms.nome_tag_txt = 'N04'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMS20'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pRedBC.obrigatorio   = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True

        elif self.valor == '30':
            self.grupo_icms.nome_tag = 'ICMS30'
            self.grupo_icms.nome_tag_txt = 'N05'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMS30'
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

        elif self.valor in ('40', '41', '50'):
            if self.grupo_icms.repasse and self.valor == '41':
                self.grupo_icms.nome_tag = 'ICMSST'
                self.grupo_icms.nome_tag_txt = 'N10b'
                self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMSST'
                self.grupo_icms.vBCSTRet.obrigatorio    = True
                self.grupo_icms.vICMSSTRet.obrigatorio  = True
                self.grupo_icms.vBCSTDest.obrigatorio   = True
                self.grupo_icms.vICMSSTDest.obrigatorio = True
            else:
                self.grupo_icms.nome_tag = 'ICMS40'
                self.grupo_icms.nome_tag_txt = 'N06'
                self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMS40'

        elif self.valor == '51':
            self.grupo_icms.nome_tag = 'ICMS51'
            self.grupo_icms.nome_tag_txt = 'N07'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMS51'

        elif self.valor == '60':
            self.grupo_icms.nome_tag = 'ICMS60'
            self.grupo_icms.nome_tag_txt = 'N08'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMS60'
            self.grupo_icms.vBCSTRet.obrigatorio   = True
            self.grupo_icms.vICMSSTRet.obrigatorio = True

        elif self.valor == '70':
            self.grupo_icms.nome_tag = 'ICMS70'
            self.grupo_icms.nome_tag_txt = 'N09'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMS70'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pRedBC.obrigatorio   = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

        elif self.valor == '90':
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

            if not self.grupo_icms.partilha:
                self.grupo_icms.nome_tag = 'ICMS90'
                self.grupo_icms.nome_tag_txt = 'N10'
                self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMS90'
            else:
                self.grupo_icms.nome_tag = 'ICMSPart'
                self.grupo_icms.nome_tag_txt = 'N10a'
                self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMSPart'
                self.grupo_icms.pBCOp.obrigatorio    = True
                self.grupo_icms.UFST.obrigatorio     = True

        #
        # Redefine a raiz para todas as tags do grupo ICMS
        #
        self.grupo_icms.orig.raiz        = self.grupo_icms.raiz_tag
        self.grupo_icms.CST.raiz         = self.grupo_icms.raiz_tag
        self.grupo_icms.modBC.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.vBC.raiz         = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBC.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMS.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMS.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.modBCST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.pMVAST.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBCST.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCST.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMSST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.motDesICMS.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCSTRet.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSSTRet.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCSTDest.raiz   = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSSTDest.raiz = self.grupo_icms.raiz_tag
        self.grupo_icms.UFST.raiz        = self.grupo_icms.raiz_tag
        self.grupo_icms.pBCOp.raiz       = self.grupo_icms.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class ICMS(nfe_110.ICMS):
    def __init__(self):
        super(ICMS, self).__init__()
        self.nome_tag = 'ICMSSN102'
        self.nome_tag_txt = 'N10d'
        self.raiz_tag = '//det/imposto/ICMS/ICMSSN102'

        #
        # Valores de controle, para gerar corretamente as tags
        # com os novos campos
        #
        self.regime_tributario = 1 # Simples Nacional
        self.partilha          = False # Para o grupo ICMSPart
        self.repasse           = False # Para o grupo ICMSST

        #
        # Novos campos para o ICMS
        #
        self.UFST        = TagCaracter(nome='UFST'      , codigo='N24', tamanho=[2,  2]                       , raiz='')
        self.pBCOp       = TagDecimal(nome='pBCOp'      , codigo='N25', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vBCSTRet    = TagDecimal(nome='vBCSTRet'   , codigo='N26', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.vICMSSTRet  = TagDecimal(nome='vICMSSTRet' , codigo='N27', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.motDesICMS  = TagInteiro(nome='motDesICMS' , codigo='N28', tamanho=[1, 1]                        , raiz='')
        self.pCredSN     = TagDecimal(nome='pCredSN'    , codigo='N29', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.vCredICMSSN = TagDecimal(nome='vCredICMSSN', codigo='N30', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.vBCSTDest   = TagDecimal(nome='vBCSTDest'  , codigo='N31', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.vICMSSTDest = TagDecimal(nome='vICMSSTDest', codigo='N32', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')

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

            elif self.CST.valor == '10':
                if not self.partilha:
                    xml += self.modBC.xml
                    xml += self.vBC.xml
                    #xml += self.pRedBC.xml
                    xml += self.pICMS.xml
                    xml += self.vICMS.xml
                    xml += self.modBCST.xml

                    # Somente quando for marge de valor agregado
                    if self.modBCST.valor == 4:
                        xml += self.pMVAST.xml

                    xml += self.pRedBCST.xml
                    xml += self.vBCST.xml
                    xml += self.pICMSST.xml
                    xml += self.vICMSST.xml
                else:
                    xml += self.modBC.xml
                    xml += self.vBC.xml
                    xml += self.pRedBC.xml
                    xml += self.pICMS.xml
                    xml += self.vICMS.xml
                    xml += self.modBCST.xml

                    # Somente quando for marge de valor agregado
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

            elif self.CST.valor == '30':
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

            elif self.CST.valor in ('40', '41', '50'):
                if self.repasse and self.CST.valor == '41':
                    xml += self.vBCSTRet.xml
                    xml += self.vICMSSTRet.xml
                    xml += self.vBCSTDest.xml
                    xml += self.vICMSSTDest.xml

                elif self.motDesICMS.valor:
                    xml += self.vICMS.xml
                    xml += self.motDesICMS.xml

            elif self.CST.valor == '51':
                xml += self.modBC.xml
                xml += self.pRedBC.xml
                xml += self.vBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml

            elif self.CST.valor == '60':
                xml += self.vBCSTRet.xml
                xml += self.vICMSSTRet.xml

            elif self.CST.valor == '70':
                xml += self.modBC.xml
                xml += self.pRedBC.xml
                xml += self.vBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

            elif self.CST.valor == '90':
                xml += self.modBC.xml
                xml += self.vBC.xml
                xml += self.pRedBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

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

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml
                xml += self.pCredSN.xml
                xml += self.vCredICMSSN.xml

            elif self.CSOSN.valor in ('202', '203'):
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

            elif self.CSOSN.valor == '500':
                xml += self.vBCSTRet.xml
                xml += self.vICMSSTRet.xml

            elif self.CSOSN.valor == '900':
                xml += self.modBC.xml
                xml += self.vBC.xml
                xml += self.pRedBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml
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
            self.modBCST.xml    = arquivo
            self.pMVAST.xml     = arquivo
            self.pRedBCST.xml   = arquivo
            self.vBCST.xml      = arquivo
            self.pICMSST.xml    = arquivo
            self.vICMSST.xml    = arquivo
            self.vBCSTRet.xml   = arquivo
            self.vICMSSTRet.xml = arquivo

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

    def get_txt(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        txt = 'N|\n'
        txt += self.nome_tag_txt + '|'
        txt += self.orig.txt + '|'

        #
        # Se for regime tradicional (não Simples Nacional)
        #
        if self.regime_tributario != 1:
            txt += self.CST.txt + '|'

            if self.CST.valor == '00':
                txt += self.modBC.txt + '|'
                txt += self.vBC.txt + '|'
                txt += self.pICMS.txt + '|'
                txt += self.vICMS.txt + '|'

            elif self.CST.valor == '10':
                if not self.partilha:
                    txt += self.modBC.txt + '|'
                    txt += self.vBC.txt + '|'
                    #txt += self.pRedBC.txt + '|'
                    txt += self.pICMS.txt + '|'
                    txt += self.vICMS.txt + '|'
                    txt += self.modBCST.txt + '|'

                    # Somente quando for marge de valor agregado
                    if self.modBCST.valor == 4:
                        txt += self.pMVAST.txt + '|'
                    else:
                        txt += '|'

                    txt += self.pRedBCST.txt + '|'
                    txt += self.vBCST.txt + '|'
                    txt += self.pICMSST.txt + '|'
                    txt += self.vICMSST.txt + '|'
                else:
                    txt += self.modBC.txt + '|'
                    txt += self.vBC.txt + '|'
                    txt += self.pRedBC.txt + '|'
                    txt += self.pICMS.txt + '|'
                    txt += self.vICMS.txt + '|'
                    txt += self.modBCST.txt + '|'

                    # Somente quando for marge de valor agregado
                    if self.modBCST.valor == 4:
                        txt += self.pMVAST.txt + '|'
                    else:
                        txt += '|'

                    txt += self.pRedBCST.txt + '|'
                    txt += self.vBCST.txt + '|'
                    txt += self.pICMSST.txt + '|'
                    txt += self.vICMSST.txt + '|'
                    txt += self.pBCOp.txt + '|'
                    txt += self.UFST.txt + '|'

            elif self.CST.valor == '20':
                txt += self.modBC.txt + '|'
                txt += self.vBC.txt + '|'
                txt += self.pRedBC.txt + '|'
                txt += self.pICMS.txt + '|'
                txt += self.vICMS.txt + '|'

            elif self.CST.valor == '30':
                txt += self.modBCST.txt + '|'

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    txt += self.pMVAST.txt + '|'
                else:
                    txt += '|'

                txt += self.pRedBCST.txt + '|'
                txt += self.vBCST.txt + '|'
                txt += self.pICMSST.txt + '|'
                txt += self.vICMSST.txt + '|'

            elif self.CST.valor in ('40', '41', '50'):
                if self.repasse and self.CST.valor == '41':
                    txt += self.vBCSTRet.txt + '|'
                    txt += self.vICMSSTRet.txt + '|'
                    txt += self.vBCSTDest.txt + '|'
                    txt += self.vICMSSTDest.txt + '|'

                elif self.motDesICMS.valor:
                    txt += self.vICMS.txt + '|'
                    txt += self.motDesICMS.txt + '|'

            elif self.CST.valor == '51':
                txt += self.modBC.txt + '|'
                txt += self.pRedBC.txt + '|'
                txt += self.vBC.txt + '|'
                txt += self.pICMS.txt + '|'
                txt += self.vICMS.txt + '|'

            elif self.CST.valor == '60':
                txt += self.vBCSTRet.txt + '|'
                txt += self.vICMSSTRet.txt + '|'

            elif self.CST.valor == '70':
                txt += self.modBC.txt + '|'
                txt += self.vBC.txt + '|'
                txt += self.pRedBC.txt + '|'
                txt += self.pICMS.txt + '|'
                txt += self.vICMS.txt + '|'
                txt += self.modBCST.txt + '|'

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    txt += self.pMVAST.txt + '|'
                else:
                    txt += '|'

                txt += self.pRedBCST.txt + '|'
                txt += self.vBCST.txt + '|'
                txt += self.pICMSST.txt + '|'
                txt += self.vICMSST.txt + '|'

            elif self.CST.valor == '90':
                txt += self.modBC.txt + '|'
                txt += self.vBC.txt + '|'
                txt += self.pRedBC.txt + '|'
                txt += self.pICMS.txt + '|'
                txt += self.vICMS.txt + '|'
                txt += self.modBCST.txt + '|'

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    txt += self.pMVAST.txt + '|'
                else:
                    txt += '|'

                txt += self.pRedBCST.txt + '|'
                txt += self.vBCST.txt + '|'
                txt += self.pICMSST.txt + '|'
                txt += self.vICMSST.txt + '|'

                if self.partilha:
                    txt += self.pBCOp.txt + '|'
                    txt += self.UFST.txt + '|'

        #
        # O regime tributário é o Simples Nacional
        #
        else:
            txt += self.CSOSN.txt + '|'

            if self.CSOSN.valor == '101':
                txt += self.pCredSN.txt + '|'
                txt += self.vCredICMSSN.txt + '|'

            elif self.CSOSN.valor in ('102', '103', '300', '400'):
                pass

            elif self.CSOSN.valor == '201':
                txt += self.modBCST.txt + '|'

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    txt += self.pMVAST.txt + '|'
                else:
                    txt += '|'

                txt += self.pRedBCST.txt + '|'
                txt += self.vBCST.txt + '|'
                txt += self.pICMSST.txt + '|'
                txt += self.vICMSST.txt + '|'
                txt += self.pCredSN.txt + '|'
                txt += self.vCredICMSSN.txt + '|'

            elif self.CSOSN.valor in ('202', '203'):
                txt += self.modBCST.txt + '|'

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    txt += self.pMVAST.txt + '|'
                else:
                    txt += '|'

                txt += self.pRedBCST.txt + '|'
                txt += self.vBCST.txt + '|'
                txt += self.pICMSST.txt + '|'
                txt += self.vICMSST.txt + '|'

            elif self.CSOSN.valor == '500':
                txt += self.vBCSTRet.txt + '|'
                txt += self.vICMSSTRet.txt + '|'

            elif self.CSOSN.valor == '900':
                txt += self.modBC.txt + '|'
                txt += self.vBC.txt + '|'
                txt += self.pRedBC.txt + '|'
                txt += self.pICMS.txt + '|'
                txt += self.vICMS.txt + '|'
                txt += self.modBCST.txt + '|'

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    txt += self.pMVAST.txt + '|'
                else:
                    txt += '|'

                txt += self.pRedBCST.txt + '|'
                txt += self.vBCST.txt + '|'
                txt += self.pICMSST.txt + '|'
                txt += self.vICMSST.txt + '|'
                txt += self.pCredSN.txt + '|'
                txt += self.vCredICMSSN.txt + '|'

        txt += '\n'
        return txt


class Imposto(nfe_110.Imposto):
    def __init__(self):
        super(Imposto, self).__init__()
        self.vTotTrib = TagDecimal(nome='vTotTrib', codigo='M02', tamanho=[1, 15, 1], decimais=[0,  2,  2], raiz='//det/imposto', obrigatorio=False)
        self.ICMS     = ICMS()
        self.ISSQN    = ISSQN()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<imposto>'
        xml += self.vTotTrib.xml

        # Enviar ICMS, IPI e II somente quando não for serviço
        if not self.ISSQN.cSitTrib.valor:
            xml += self.ICMS.xml
            xml += self.IPI.xml
            xml += self.II.xml

        xml += self.PIS.xml
        xml += self.PISST.xml
        xml += self.COFINS.xml
        xml += self.COFINSST.xml

        if self.ISSQN.cSitTrib.valor:
            xml += self.ISSQN.xml

        xml += '</imposto>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vTotTrib.xml = arquivo
            self.ICMS.xml     = arquivo
            self.IPI.xml      = arquivo
            self.II.xml       = arquivo
            self.PIS.xml      = arquivo
            self.PISST.xml    = arquivo
            self.COFINS.xml   = arquivo
            self.COFINSST.xml = arquivo
            self.ISSQN.xml    = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'M|\n'

        if not self.ISSQN.cSitTrib.valor:
            txt += self.ICMS.txt
            txt += self.IPI.txt
            txt += self.II.txt

        txt += self.PIS.txt
        txt += self.PISST.txt
        txt += self.COFINS.txt
        txt += self.COFINSST.txt

        if self.ISSQN.cSitTrib.valor:
            txt += self.ISSQN.txt

        return txt

    txt = property(get_txt)


class CIDE(nfe_110.CIDE):
    def __init__(self):
        super(CIDE, self).__init__()


class Comb(nfe_110.Comb):
    def __init__(self):
        super(Comb, self).__init__()

    def get_xml(self):
        if not self.cProdANP.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<comb>'
        xml += self.cProdANP.xml
        xml += self.CODIF.xml
        xml += self.qTemp.xml
        xml += self.CIDE.xml
        xml += '</comb>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cProdANP.xml  = arquivo
            self.CODIF.xml     = arquivo
            self.qTemp.xml     = arquivo
            self.CIDE.xml      = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not self.cProdANP.valor:
            return ''

        txt = 'L1|'
        txt += self.cProdANP.txt + '|'
        txt += self.CODIF.txt + '|'
        txt += self.qTemp.txt + '|'
        txt += '\n'

        txt += self.CIDE.txt
        return txt

    txt = property(get_txt)


class Arma(nfe_110.Arma):
    def __init__(self):
        super(Arma, self).__init__()


class Med(nfe_110.Med):
    def __init__(self):
        super(Med, self).__init__()


class VeicProd(nfe_110.VeicProd):
    def __init__(self):
        super(VeicProd, self).__init__()
        self.cilin        = TagCaracter(nome='cilin'       , codigo='J07', tamanho=[ 1,  4], raiz='//det/prod/veicProd')
        self.tpComb       = TagCaracter(nome='tpComb'      , codigo='J11', tamanho=[ 2,  2], raiz='//det/prod/veicProd')
        self.CMT          = TagCaracter(nome='CMT'         , codigo='J13', tamanho=[ 1,  9], raiz='//det/prod/veicProd')
        self.cCorDENATRAN = TagCaracter(nome='cCorDENATRAN', codigo='J24', tamanho=[ 2,  2], raiz='//det/prod/veicProd')
        self.lota         = TagInteiro(nome='lota'         , codigo='J25', tamanho=[ 1,  3], raiz='//det/prod/veicProd')
        self.tpRest       = TagInteiro(nome='tpRest'       , codigo='J26', tamanho=[ 1,  3], raiz='//det/prod/veicProd')

    def get_xml(self):
        if not self.chassi.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<veicProd>'
        xml += self.tpOp.xml
        xml += self.chassi.xml
        xml += self.cCor.xml
        xml += self.xCor.xml
        xml += self.pot.xml
        xml += self.cilin.xml
        xml += self.pesoL.xml
        xml += self.pesoB.xml
        xml += self.nSerie.xml
        xml += self.tpComb.xml
        xml += self.nMotor.xml
        xml += self.CMT.xml
        xml += self.dist.xml
        xml += self.anoMod.xml
        xml += self.anoFab.xml
        xml += self.tpPint.xml
        xml += self.tpVeic.xml
        xml += self.espVeic.xml
        xml += self.VIN.xml
        xml += self.condVeic.xml
        xml += self.cMod.xml
        xml += self.cCorDENATRAN.xml
        xml += self.lota.xml
        xml += self.tpRest.xml
        xml += '</veicProd>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpOp.xml     = arquivo
            self.chassi.xml   = arquivo
            self.cCor.xml     = arquivo
            self.xCor.xml     = arquivo
            self.pot.xml      = arquivo
            self.cilin.xml      = arquivo
            self.pesoL.xml    = arquivo
            self.pesoB.xml    = arquivo
            self.nSerie.xml   = arquivo
            self.tpComb.xml   = arquivo
            self.nMotor.xml   = arquivo
            self.CMT.xml     = arquivo
            self.dist.xml     = arquivo
            self.anoMod.xml   = arquivo
            self.anoFab.xml   = arquivo
            self.tpPint.xml   = arquivo
            self.tpVeic.xml   = arquivo
            self.espVeic.xml  = arquivo
            self.VIN.xml      = arquivo
            self.condVeic.xml = arquivo
            self.cMod.xml     = arquivo
            self.cCorDENATRAN.xml = arquivo
            self.lota.xml     = arquivo
            self.tpRest.xml   = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not self.chassi.valor:
            return ''

        txt = 'J|'
        txt += self.tpOp.txt + '|'
        txt += self.chassi.txt + '|'
        txt += self.cCor.txt + '|'
        txt += self.xCor.txt + '|'
        txt += self.pot.txt + '|'
        txt += self.cilin.txt + '|'
        txt += self.pesoL.txt + '|'
        txt += self.pesoB.txt + '|'
        txt += self.nSerie.txt + '|'
        txt += self.tpComb.txt + '|'
        txt += self.nMotor.txt + '|'
        txt += self.CMT.txt + '|'
        txt += self.dist.txt + '|'
        txt += self.anoMod.txt + '|'
        txt += self.anoFab.txt + '|'
        txt += self.tpPint.txt + '|'
        txt += self.tpVeic.txt + '|'
        txt += self.espVeic.txt + '|'
        txt += self.VIN.txt + '|'
        txt += self.condVeic.txt + '|'
        txt += self.cMod.txt + '|'
        txt += self.cCorDENATRAN.txt + '|'
        txt += self.lota.txt + '|'
        txt += self.tpRest.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class Adi(nfe_110.Adi):
    def __init__(self):
        super(Adi, self).__init__()
        self.nDraw = TagInteiro(nome='nDraw', codigo='I29a', tamanho=[1,  11],                     raiz='//adi', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<adi>'
        xml += self.nAdicao.xml
        xml += self.nSeqAdic.xml
        xml += self.cFabricante.xml
        xml += self.vDescDI.xml
        xml += self.nDraw.xml
        xml += '</adi>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nAdicao.xml     = arquivo
            self.nSeqAdic.xml    = arquivo
            self.cFabricante.xml = arquivo
            self.vDescDI.xml     = arquivo
            self.nDraw.xml     = arquivo

    xml = property(get_xml, set_xml)


class DI(nfe_110.DI):
    def __init__(self):
        super(DI, self).__init__()
        self.adi = []

class Prod(nfe_110.Prod):
    def __init__(self):
        super(Prod, self).__init__()
        self.NCM      = TagCaracter(nome='NCM'     , codigo='I05' , tamanho=[2,  8]                        , raiz='//det/prod')
        self.qCom     = TagDecimal(nome='qCom'     , codigo='I10' , tamanho=[1, 15, 1], decimais=[0,  4, 4], raiz='//det/prod')
        self.vUnCom   = TagDecimal(nome='vUnCom'   , codigo='I10a', tamanho=[1, 21, 1], decimais=[0, 10, 4], raiz='//det/prod')
        self.qTrib    = TagDecimal(nome='qTrib'    , codigo='I14' , tamanho=[1, 15, 1], decimais=[0,  4, 4], raiz='//det/prod')
        self.vUnTrib  = TagDecimal(nome='vUnTrib'  , codigo='I14a', tamanho=[1, 21, 1], decimais=[0, 10, 4], raiz='//det/prod')
        self.vOutro   = TagDecimal(nome='vOutro'   , codigo='I17a', tamanho=[1, 15, 1], decimais=[0,  2, 2], raiz='//det/prod', obrigatorio=False)
        self.indTot   = TagInteiro(nome='indTot'   , codigo='I17b', tamanho=[1,  1, 1],                      raiz='//det/prod', valor=1)
        self.xPed     = TagCaracter(nome='xPed'    , codigo='I30' , tamanho=[1, 15],                         raiz='//det/prod', obrigatorio=False)
        self.nItemPed = TagCaracter(nome='nItemPed', codigo='I31' , tamanho=[1,  6],                         raiz='//det/prod', obrigatorio=False)
        self.nFCI     = TagCaracter(nome='nFCI'    , codigo='I70' , tamanho=[36, 36, 36],                    raiz='//det/prod', obrigatorio=False)
        self.veicProd = VeicProd()
        self.comb     = Comb()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<prod>'
        xml += self.cProd.xml
        xml += self.cEAN.xml
        xml += self.xProd.xml
        xml += self.NCM.xml
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

        xml += self.xPed.xml
        xml += self.nItemPed.xml
        xml += self.nFCI.xml
        xml += self.veicProd.xml

        for m in self.med:
            xml += m.xml

        for a in self.arma:
            xml += a.xml

        xml += self.comb.xml
        xml += '</prod>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cProd.xml    = arquivo
            self.cEAN.xml     = arquivo
            self.xProd.xml    = arquivo
            self.NCM.xml      = arquivo
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

            self.xPed.xml     = arquivo
            self.nItemPed.xml = arquivo
            self.nFCI.xml     = arquivo
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

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'I|'
        txt += self.cProd.txt + '|'
        txt += self.cEAN.txt + '|'
        txt += self.xProd.txt + '|'
        txt += self.NCM.txt + '|'
        txt += self.EXTIPI.txt + '|'
        #txt += self.genero.txt + '|'
        txt += self.CFOP.txt + '|'
        txt += self.uCom.txt + '|'
        txt += self.qCom.txt + '|'
        txt += self.vUnCom.txt + '|'
        txt += self.vProd.txt + '|'
        txt += self.cEANTrib.txt + '|'
        txt += self.uTrib.txt + '|'
        txt += self.qTrib.txt + '|'
        txt += self.vUnTrib.txt + '|'
        txt += self.vFrete.txt + '|'
        txt += self.vSeg.txt + '|'
        txt += self.vDesc.txt + '|'
        txt += self.vOutro.txt + '|'
        txt += self.indTot.txt + '|'
        txt += self.xPed.txt + '|'
        txt += self.nItemPed.txt + '|'
        txt += '\n'

        for d in self.DI:
            txt += d.txt

        txt += self.veicProd.txt

        for m in self.med:
            txt += m.txt

        for a in self.arma:
            txt += a.txt

        txt += self.comb.txt

        return txt

    txt = property(get_txt)


class Det(nfe_110.Det):
    def __init__(self):
        super(Det, self).__init__()
        self.prod      = Prod()
        self.imposto   = Imposto()

    def cst_formatado(self):
        formatado = unicode(self.imposto.ICMS.orig.valor).zfill(1)

        if self.imposto.ICMS.regime_tributario == 1:
            formatado += unicode(self.imposto.ICMS.CSOSN.valor).zfill(3)
        else:
            formatado += unicode(self.imposto.ICMS.CST.valor).zfill(2)

        return formatado


class Compra(nfe_110.Compra):
    def __init__(self):
        super(Compra, self).__init__()


class Exporta(nfe_110.Exporta):
    def __init__(self):
        super(Exporta, self).__init__()


class ProcRef(nfe_110.ProcRef):
    def __init__(self):
        super(ProcRef, self).__init__()


class ObsFisco(nfe_110.ObsFisco):
    def __init__(self):
        super(ObsFisco, self).__init__()


class ObsCont(nfe_110.ObsCont):
    def __init__(self):
        super(ObsCont, self).__init__()


class InfAdic(nfe_110.InfAdic):
    def __init__(self):
        super(InfAdic, self).__init__()
        self.infAdFisco = TagCaracter(nome='infAdFisco', codigo='Z02', tamanho=[1, 2000], raiz='//NFe/infNFe/infAdic', obrigatorio=False)


class Dup(nfe_110.Dup):
    def __init__(self):
        super(Dup, self).__init__()


class Fat(nfe_110.Fat):
    def __init__(self):
        super(Fat, self).__init__()


class Cobr(nfe_110.Cobr):
    def __init__(self):
        super(Cobr, self).__init__()


class Lacres(nfe_110.Lacres):
    def __init__(self):
        super(Lacres, self).__init__()


class Vol(nfe_110.Vol):
    def __init__(self, xml=None):
        super(Vol, self).__init__()


class Reboque(nfe_110.Reboque):
    def __init__(self):
        super(Reboque, self).__init__()


class VeicTransp(nfe_110.VeicTransp):
    def __init__(self):
        super(VeicTransp, self).__init__()


class RetTransp(nfe_110.RetTransp):
    def __init__(self):
        super(RetTransp, self).__init__()


class Transporta(nfe_110.Transporta):
    def __init__(self):
        super(Transporta, self).__init__()


class Transp(nfe_110.Transp):
    def __init__(self):
        super(Transp, self).__init__()
        self.vagao = TagCaracter(nome='vagao', codigo='X25a', tamanho=[1, 20], raiz='//NFe/infNFe/transp', obrigatorio=False)
        self.balsa = TagCaracter(nome='balsa', codigo='X25b', tamanho=[1, 20], raiz='//NFe/infNFe/transp', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<transp>'
        xml += self.modFrete.xml
        xml += self.transporta.xml
        xml += self.retTransp.xml

        if self.balsa.valor:
            xml += self.balsa.xml
        elif self.vagao.valor:
            xml += self.vagao.xml
        else:
            xml += self.veicTransp.xml

            for r in self.reboque:
                xml += r.xml

        for v in self.vol:
            xml += v.xml

        xml += '</transp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.modFrete.xml   = arquivo
            self.transporta.xml = arquivo
            self.retTransp.xml  = arquivo
            self.veicTransp.xml = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.reboque = self.le_grupo('//NFe/infNFe/transp/reboque', nfe_110.Reboque)

            self.vagao.xml = arquivo
            self.balsa.xml = arquivo

            self.vol = self.le_grupo('//NFe/infNFe/transp/vol', nfe_110.Vol)

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'X|'
        txt += self.modFrete.txt + '|\n'
        txt += self.transporta.txt
        txt += self.retTransp.txt
        txt += self.veicTransp.txt

        for r in self.reboque:
            txt += r.txt

        for v in self.vol:
            txt += v.txt

        return txt

    txt = property(get_txt)


class RetTrib(nfe_110.RetTrib):
    def __init__(self):
        super(RetTrib, self).__init__()


class ISSQNTot(nfe_110.ISSQNTot):
    def __init__(self):
        super(ISSQNTot, self).__init__()


class ICMSTot(nfe_110.ICMSTot):
    def __init__(self):
        super(ICMSTot, self).__init__()
        self.vTotTrib = TagDecimal(nome='vTotTrib', codigo='W16a', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz='//NFe/infNFe/total/ICMSTot', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ICMSTot>'
        xml += self.vBC.xml
        xml += self.vICMS.xml
        xml += self.vBCST.xml
        xml += self.vST.xml
        xml += self.vProd.xml
        xml += self.vFrete.xml
        xml += self.vSeg.xml
        xml += self.vDesc.xml
        xml += self.vII.xml
        xml += self.vIPI.xml
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
            self.vBCST.xml   = arquivo
            self.vST.xml     = arquivo
            self.vProd.xml   = arquivo
            self.vFrete.xml  = arquivo
            self.vSeg.xml    = arquivo
            self.vDesc.xml   = arquivo
            self.vII.xml     = arquivo
            self.vIPI.xml    = arquivo
            self.vPIS.xml    = arquivo
            self.vCOFINS.xml = arquivo
            self.vOutro.xml  = arquivo
            self.vNF.xml     = arquivo
            self.vTotTrib.xml = arquivo

    xml = property(get_xml, set_xml)


class Total(nfe_110.Total):
    def __init__(self):
        super(Total, self).__init__()
        self.ICMSTot = ICMSTot()


class Entrega(nfe_110.Entrega):
    def __init__(self):
        super(Entrega, self).__init__()
        self.CNPJ    = TagCaracter(nome='CNPJ'   , codigo='G02', tamanho=[14, 14]   , raiz='//NFe/infNFe/entrega')
        self.CPF       = TagCaracter(nome='CPF'  , codigo='G02a', tamanho=[11, 11]   , raiz='//NFe/infNFe/entrega',)
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='G03', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/entrega')
        self.nro     = TagCaracter(nome='nro'    , codigo='G04', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/entrega')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='G05', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/entrega', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='G06', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/entrega')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='G07', tamanho=[ 7,  7, 7], raiz='//NFe/infNFe/entrega')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='G08', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/entrega')
        self.UF      = TagCaracter(nome='UF'     , codigo='G09', tamanho=[ 2,  2]   , raiz='//NFe/infNFe/entrega')


    def get_xml(self):
        if not (self.CNPJ.valor or self.CPF.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<entrega>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += '</entrega>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml    = arquivo
            self.CPF.xml     = arquivo
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.UF.xml      = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not len(self.CNPJ.valor):
            return ''

        txt = 'G|'
        txt += self.CNPJ.txt + '|'
        txt += self.xLgr.txt + '|'
        txt += self.nro.txt + '|'
        txt += self.xCpl.txt + '|'
        txt += self.xBairro.txt + '|'
        txt += self.cMun.txt + '|'
        txt += self.xMun.txt + '|'
        txt += self.UF.txt + '|'
        txt += '\n'

        if self.CPF.valor:
            txt += 'G02a|' + self.CPF.txt + '|\n'
        else:
            txt += 'G02|' + self.CNPJ.txt + '|\n'

        return txt

    txt = property(get_txt)


class Retirada(nfe_110.Retirada):
    def __init__(self):
        super(Retirada, self).__init__()
        self.CNPJ    = TagCaracter(nome='CNPJ'   , codigo='F02' , tamanho=[ 0, 14]   , raiz='//NFe/infNFe/retirada')
        self.CPF     = TagCaracter(nome='CPF'    , codigo='F02a', tamanho=[11, 11]   , raiz='//NFe/infNFe/retirada')


    def get_xml(self):
        if not (self.CNPJ.valor or self.CPF.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<retirada>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += '</retirada>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml    = arquivo
            self.CPF.xml     = arquivo
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.UF.xml      = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not len(self.CNPJ.valor):
            return ''

        txt = 'F|'
        txt += self.CNPJ.txt + '|'
        txt += self.xLgr.txt + '|'
        txt += self.nro.txt + '|'
        txt += self.xCpl.txt + '|'
        txt += self.xBairro.txt + '|'
        txt += self.cMun.txt + '|'
        txt += self.xMun.txt + '|'
        txt += self.UF.txt + '|'
        txt += '\n'

        if self.CPF.valor:
            txt += 'F02a|' + self.CPF.txt + '|\n'
        else:
            txt += 'F02|' + self.CNPJ.txt + '|\n'

        return txt

    txt = property(get_txt)


class EnderDest(nfe_110.EnderDest):
    def __init__(self):
        super(EnderDest, self).__init__()
        self.fone    = TagInteiro(nome='fone'    , codigo='E16', tamanho=[ 6, 14]   , raiz='//NFe/infNFe/dest/enderDest', obrigatorio=False)


class Dest(nfe_110.Dest):
    def __init__(self):
        super(Dest, self).__init__()
        self.enderDest = EnderDest()
        self.ISUF      = TagCaracter(nome='ISUF' , codigo='E18', tamanho=[ 8,  9], raiz='//NFe/infNFe/dest', obrigatorio=False)
        self.email     = TagCaracter(nome='email', codigo='E19', tamanho=[1, 60], raiz='//NFe/infNFe/dest', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dest>'

        #
        # Força o uso da tag CNPJ quando a nota for em homologação
        #
        if self.CNPJ.valor == '99999999000191':
            xml += self.CNPJ.xml
        elif self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.xNome.xml
        xml += self.enderDest.xml
        xml += self.IE.xml
        xml += self.ISUF.xml
        xml += self.email.xml
        xml += '</dest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.xNome.xml     = arquivo
            self.enderDest.xml = arquivo
            self.IE.xml        = arquivo
            self.ISUF.xml      = arquivo
            self.email.xml     = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'E|'
        txt += self.xNome.txt + '|'
        txt += self.IE.txt + '|'
        txt += self.ISUF.txt + '|'
        txt += self.email.txt + '|'
        txt += '\n'

        if self.CPF.valor:
            txt += 'E03|' + self.CPF.txt + '|\n'
        else:
            txt += 'E02|' + self.CNPJ.txt + '|\n'

        txt += self.enderDest.txt
        return txt

    txt = property(get_txt)


class Avulsa(nfe_110.Avulsa):
    def __init__(self):
        super(Avulsa, self).__init__()
        self.fone    = TagInteiro(nome='fone'    , codigo='D05', tamanho=[ 6, 14], raiz='//NFe/infNFe/avulsa')


class EnderEmit(nfe_110.EnderEmit):
    def __init__(self):
        super(EnderEmit, self).__init__()
        self.fone    = TagInteiro(nome='fone'    , codigo='C16', tamanho=[ 6, 14]   , raiz='//NFe/infNFe/emit/enderEmit', obrigatorio=False)


class Emit(nfe_110.Emit):
    def __init__(self):
        super(Emit, self).__init__()
        self.enderEmit = EnderEmit()
        self.CRT       = TagInteiro(nome='CRT'  , codigo='C21' , tamanho=[ 1,  1], raiz='//NFe/infNFe/emit', valor=1)


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<emit>'
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.xNome.xml
        xml += self.xFant.xml
        xml += self.enderEmit.xml
        xml += self.IE.xml
        xml += self.IEST.xml
        xml += self.IM.xml
        xml += self.CNAE.xml
        xml += self.CRT.xml
        xml += '</emit>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.xNome.xml     = arquivo
            self.xFant.xml     = arquivo
            self.enderEmit.xml = arquivo
            self.IE.xml        = arquivo
            self.IEST.xml      = arquivo
            self.IM.xml        = arquivo
            self.CNAE.xml      = arquivo
            self.CRT.xml       = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'C|'
        txt += self.xNome.txt + '|'
        txt += self.xFant.txt + '|'
        txt += self.IE.txt + '|'
        txt += self.IEST.txt + '|'
        txt += self.IM.txt + '|'
        txt += self.CNAE.txt + '|'
        txt += self.CRT.txt + '|'
        txt += '\n'

        if self.CNPJ.valor:
            txt += 'C02|' + self.CNPJ.txt + '|\n'

        else:
            txt += 'C02a|' + self.CPF.txt + '|\n'

        txt += self.enderEmit.txt

        return txt

    txt = property(get_txt)


class RefECF(XMLNFe):
    def __init__(self):
        super(RefECF, self).__init__()
        self.mod   = TagCaracter(nome='mod', codigo='B20l', tamanho=[ 2,  2, 2], raiz='//NFref/refECF')
        self.nECF  = TagInteiro(nome='nECF', codigo='B20m', tamanho=[ 1,  3, 1], raiz='//NFref/refECF')
        self.nCOO  = TagInteiro(nome='nCOO', codigo='B20n', tamanho=[ 1,  6, 1], raiz='//NFref/refECF')

    def get_xml(self):
        if not (self.mod.valor or self.nECF.valor or self.nCOO.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<refECF>'
        xml += self.mod.xml
        xml += self.nECF.xml
        xml += self.nCOO.xml
        xml += '</refECF>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.mod.xml   = arquivo
            self.nECF.xml = arquivo
            self.nCOO.xml   = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.mod.valor or self.nECF.valor or self.nCOO.valor):
            return ''

        txt = 'B20g|'
        txt += self.mod.txt + '|'
        txt += self.nECF.txt + '|'
        txt += self.nCOO.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class RefNFP(XMLNFe):
    def __init__(self):
        super(RefNFP, self).__init__()
        self.cUF   = TagInteiro(nome='cUF'  , codigo='B20b', tamanho=[ 2,  2, 2], raiz='//NFref/refNFP')
        self.AAMM  = TagCaracter(nome='AAMM', codigo='B20c', tamanho=[ 4,  4, 4], raiz='//NFref/refNFP')
        self.CNPJ  = TagCaracter(nome='CNPJ', codigo='B20d', tamanho=[14, 14]   , raiz='//NFref/refNFP')
        self.CPF   = TagCaracter(nome='CPF' , codigo='B20e', tamanho=[11, 11]   , raiz='//NFref/refNFP')
        self.IE    = TagCaracter(nome='IE'  , codigo='B20f', tamanho=[ 1, 14]   , raiz='//NFref/refNFP')
        self.mod   = TagCaracter(nome='mod' , codigo='B20g', tamanho=[ 2,  2, 2], raiz='//NFref/refNFP')
        self.serie = TagInteiro(nome='serie', codigo='B20h', tamanho=[ 1,  3, 1], raiz='//NFref/refNFP')
        self.nNF   = TagInteiro(nome='nNF'  , codigo='B20i', tamanho=[ 1,  9, 1], raiz='//NFref/refNFP')

    def get_xml(self):
        if not (self.cUF.valor or self.AAMM.valor or self.CNPJ.valor or self.CPF.valor or self.IE.valor or self.mod.valor or self.serie.valor or self.nNF.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<refNFP>'
        xml += self.cUF.xml
        xml += self.AAMM.xml

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.IE.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNF.xml
        xml += '</refNFP>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml   = arquivo
            self.AAMM.xml  = arquivo
            self.CNPJ.xml  = arquivo
            self.CPF.xml   = arquivo
            self.IE.xml    = arquivo
            self.mod.xml   = arquivo
            self.serie.xml = arquivo
            self.nNF.xml   = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.cUF.valor or self.AAMM.valor or self.CNPJ.valor or self.CPF.valor or self.IE.valor or self.mod.valor or self.serie.valor or self.nNF.valor):
            return ''

        txt = 'B20a|'
        txt += self.cUF.txt + '|'
        txt += self.AAMM.txt + '|'
        txt += self.IE.txt + '|'
        txt += self.mod.txt + '|'
        txt += self.serie.txt + '|'
        txt += self.nNF.txt + '|'
        txt += '\n'

        if self.CPF.valor:
            txt += 'B20e|' + self.CPF.txt + '|\n'
        else:
            txt += 'B20d|' + self.CNPJ.txt + '|\n'

        return txt

    txt = property(get_txt)


class RefNF(nfe_110.RefNF):
    def __init__(self):
        super(RefNF, self).__init__()


class NFRef(nfe_110.NFRef):
    def __init__(self):
        super(NFRef, self).__init__()
        #self.refNFe = TagCaracter(nome='refNFe', codigo='B13', tamanho=[44, 44], raiz='//NFRef', obrigatorio=False)
        #self.refNF  = RefNF()
        self.refNFP = RefNFP()
        self.refCTe = TagCaracter(nome='refCTe', codigo='B20j', tamanho=[44, 44], raiz='//NFRef', obrigatorio=False)
        self.refECF = RefECF()

    def get_xml(self):
        if not (self.refNFe.valor or self.refNF.xml or self.refNFP.xml or self.refCTe.valor or self.refECF.xml):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<NFref>'

        if self.refNFe.valor:
            xml += self.refNFe.xml
        elif self.refNF.xml:
            xml += self.refNF.xml
        elif self.refNFP.xml:
            xml += self.refNFP.xml
        elif self.refCTe.valor:
            xml += self.refCTe.xml
        elif self.refECF.xml:
            xml += self.refECF.xml

        xml += '</NFref>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.refNFe.xml = arquivo
            self.refNF.xml  = arquivo
            self.refNFP.xml = arquivo
            self.refCTe.xml = arquivo
            self.refECF.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.refNFe.valor or self.refNF.xml):
            return ''

        if self.refNFe.xml:
            txt = 'B13|' + self.refNFe.txt + '|'
        elif self.refNF.xml:
            txt += self.refNF.txt
        elif self.refNFP.xml:
            txt += self.refNFP.txt
        elif self.refCTe.xml:
            txt = 'B20i|' + self.refCTe.txt + '|'
        elif self.refECF.xml:
            txt += self.refECF.txt

        return txt

    txt = property(get_txt)


class Ide(nfe_110.Ide):
    def __init__(self):
        super(Ide, self).__init__()
        self.cNF     = TagCaracter(nome='cNF'    , codigo='B03', tamanho=[ 8,  8, 8], raiz='//NFe/infNFe/ide')
        self.hSaiEnt = TagHora(nome='hSaiEnt'    , codigo='B10a',                     raiz='//NFe/infNFe/ide', obrigatorio=False)
        self.dhCont   = TagDataHora(nome='dhCont', codigo='B28',                      raiz='//NFe/infNFe/ide', obrigatorio=False)
        self.xJust    = TagCaracter(nome='xJust' , codigo='B29',                      raiz='//NFe/infNFe/ide', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ide>'
        xml += self.cUF.xml
        xml += self.cNF.xml
        xml += self.natOp.xml
        xml += self.indPag.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNF.xml
        xml += self.dEmi.xml
        xml += self.dSaiEnt.xml
        xml += self.hSaiEnt.xml
        xml += self.tpNF.xml
        xml += self.cMunFG.xml
        xml += self.tpImp.xml
        xml += self.tpEmis.xml
        xml += self.cDV.xml
        xml += self.tpAmb.xml
        xml += self.finNFe.xml
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
            self.dSaiEnt.xml = arquivo
            self.hSaiEnt.xml = arquivo
            self.tpNF.xml    = arquivo
            self.cMunFG.xml  = arquivo

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
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo
            self.dhCont.xml  = arquivo
            self.xJust.xml   = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'B|'
        txt += self.cUF.txt + '|'
        txt += self.cNF.txt + '|'
        txt += self.natOp.txt + '|'
        txt += self.indPag.txt + '|'
        txt += self.mod.txt + '|'
        txt += self.serie.txt + '|'
        txt += self.nNF.txt + '|'
        txt += self.dEmi.txt + '|'
        txt += self.dSaiEnt.txt + '|'
        txt += self.hSaiEnt.txt + '|'
        txt += self.tpNF.txt + '|'
        txt += self.cMunFG.txt + '|'
        txt += self.tpImp.txt + '|'
        txt += self.tpEmis.txt + '|'
        txt += self.cDV.txt + '|'
        txt += self.tpAmb.txt + '|'
        txt += self.finNFe.txt + '|'
        txt += self.procEmi.txt + '|'
        txt += self.verProc.txt + '|'
        txt += self.dhCont.txt + '|'
        txt += self.xJust.txt + '|'
        txt += '\n'

        for nr in self.NFref:
            txt += nr.txt

        return txt

    txt = property(get_txt)


class InfNFe(nfe_110.InfNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.versao   = TagDecimal(nome='infNFe' , codigo='A01', propriedade='versao', raiz='//NFe', namespace=NAMESPACE_NFE, valor='2.00')
        #self.Id       = TagCaracter(nome='infNFe', codigo='A03', propriedade='Id'    , raiz='//NFe', namespace=NAMESPACE_NFE)
        self.ide      = Ide()
        self.emit     = Emit()
        self.avulsa   = Avulsa()
        self.dest     = Dest()
        self.retirada = Retirada()
        self.entrega  = Entrega()
        self.det      = []
        self.total    = Total()
        self.transp   = Transp()
        self.cobr     = Cobr()
        self.infAdic  = InfAdic()
        self.exporta  = Exporta()
        self.compra   = Compra()
        self.cana     = Cana()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infNFe versao="' + unicode(self.versao.valor) + '" Id="' + self.Id.valor + '">'
        xml += self.ide.xml
        xml += self.emit.xml
        xml += self.avulsa.xml
        xml += self.dest.xml
        xml += self.retirada.xml
        xml += self.entrega.xml

        for d in self.det:
            #d.imposto.regime_tributario = self.emit.CRT.valor
            d.imposto.ICMS.regime_tributario = self.emit.CRT.valor
            xml += d.xml

        xml += self.total.xml
        xml += self.transp.xml
        xml += self.cobr.xml
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
            self.retirada.xml = arquivo
            self.entrega.xml  = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.det = self.le_grupo('//NFe/infNFe/det', Det)

            self.total.xml    = arquivo
            self.transp.xml   = arquivo
            self.cobr.xml     = arquivo
            self.infAdic.xml  = arquivo
            self.exporta.xml  = arquivo
            self.compra.xml   = arquivo
            self.cana.xml     = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'A|'
        txt += self.versao.txt + '|'
        txt += self.Id.txt + '|'
        txt += '\n'

        txt += self.ide.txt
        txt += self.emit.txt
        txt += self.avulsa.txt
        txt += self.dest.txt
        txt += self.retirada.txt
        txt += self.entrega.txt

        for d in self.det:
            txt += d.txt

        txt += self.total.txt
        txt += self.transp.txt
        txt += self.cobr.txt
        txt += self.infAdic.txt
        txt += self.exporta.txt
        txt += self.compra.txt
        #txt += self.cana.txt

        return txt

    txt = property(get_txt)


class NFe(nfe_110.NFe):
    def __init__(self):
        super(NFe, self).__init__()
        self.infNFe = InfNFe()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'nfe_v2.00.xsd'

    def gera_nova_chave(self):
        super(NFe, self).gera_nova_chave()

        #
        # Ajustar o campo cNF para remover o 1º dígito, que é
        # o tipo da emissão
        #
        self.infNFe.ide.cNF.valor = self.chave[35:43]

    def monta_chave(self):
        chave = unicode(self.infNFe.ide.cUF.valor).strip().rjust(2, '0')
        chave += unicode(self.infNFe.ide.dEmi.valor.strftime('%y%m')).strip().rjust(4, '0')
        chave += unicode(self.infNFe.emit.CNPJ.valor).strip().rjust(14, '0')
        chave += '55'
        chave += unicode(self.infNFe.ide.serie.valor).strip().rjust(3, '0')
        chave += unicode(self.infNFe.ide.nNF.valor).strip().rjust(9, '0')

        #
        # Inclui agora o tipo da emissão
        #
        chave += unicode(self.infNFe.ide.tpEmis.valor).strip().rjust(1, '0')

        chave += unicode(self.infNFe.ide.cNF.valor).strip().rjust(8, '0')
        chave += unicode(self.infNFe.ide.cDV.valor).strip().rjust(1, '0')
        self.chave = chave

    def cst_descricao(self):
        if self.infNFe.emit.CRT.valor == 1:
            return 'CSOSN'
        else:
            return 'CST'

    def crt_descricao(self):
        texto = 'Regime tributário: '

        if self.infNFe.emit.CRT.valor == 1:
            texto += 'SIMPLES Nacional'
        elif self.infNFe.emit.CRT.valor == 2:
            texto += 'SIMPLES Nacional - excesso de sublimite de receita bruta'
        else:
            texto += 'regime normal'

        return texto
