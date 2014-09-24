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

from pysped.xml_sped import (ABERTURA, NAMESPACE_CTE, Signature, TagCaracter,
                             TagData, TagDataHora, TagDecimal, TagHora,
                             TagInteiro, XMLNFe)
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_104 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)



class Dup(XMLNFe):
    def __init__(self):
        super(Dup, self).__init__()
        self.nDup  = TagCaracter(nome='nDup', codigo='Y08', tamanho=[1, 60],                        raiz='//dup', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dVenc = TagData(nome='dVenc'   , codigo='Y09',                                         raiz='//dup', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vDup  = TagDecimal(nome='vDup' , codigo='Y10', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//dup', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.nDup.valor or self.dVenc.valor or self.vDup.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<dup>'
        xml += self.nDup.xml
        xml += self.dVenc.xml
        xml += self.vDup.xml
        xml += '</dup>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nDup.xml  = arquivo
            self.dVenc.xml = arquivo
            self.vDup.xml  = arquivo

    xml = property(get_xml, set_xml)


class Fat(XMLNFe):
    def __init__(self):
        super(Fat, self).__init__()
        self.nFat  = TagCaracter(nome='nFat', codigo='Y03', tamanho=[1, 60],                        raiz='//CTe/infCte/infCTeNorm/cobr/fat', obrigatorio=False)
        self.vOrig = TagDecimal(nome='vOrig', codigo='Y04', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/infCTeNorm/cobr/fat', obrigatorio=False)
        self.vDesc = TagDecimal(nome='vDesc', codigo='Y05', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/infCTeNorm/cobr/fat', obrigatorio=False)
        self.vLiq  = TagDecimal(nome='vLiq' , codigo='Y06', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/infCTeNorm/cobr/fat', obrigatorio=False)

    def get_xml(self):
        if not (self.nFat.valor or self.vOrig.valor or self.vDesc.valor or self.vLiq.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<fat>'
        xml += self.nFat.xml
        xml += self.vOrig.xml
        xml += self.vDesc.xml
        xml += self.vLiq.xml
        xml += '</fat>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nFat.xml  = arquivo
            self.vOrig.xml = arquivo
            self.vDesc.xml = arquivo
            self.vLiq.xml  = arquivo

    xml = property(get_xml, set_xml)


class Cobr(XMLNFe):
    def __init__(self):
        super(Cobr, self).__init__()
        self.fat = Fat()
        self.dup = []

    def get_xml(self):
        if not (self.fat.xml or len(self.dup)):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<cobr>'
        xml += self.fat.xml

        for d in self.dup:
            xml += d.xml

        xml += '</cobr>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.fat.xml  = arquivo
            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.dup = self.le_grupo('//CTe/infCte/infCTeNorm/cobr/dup', Dup, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class InfQ(XMLNFe):
    def __init__(self):
        super(InfQ, self).__init__()
        self.cUnid  = TagCaracter(nome='cUnid', tamanho=[2, 2, 2] ,                     raiz='//infQ', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.tpMed  = TagCaracter(nome='tpMed', tamanho=[1, 20]   ,                     raiz='//infQ', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.qCarga = TagDecimal(nome='qCarga', tamanho=[1, 11, 1], decimais=[0, 4, 4], raiz='//infQ', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infQ>'
        xml += self.cUnid.xml
        xml += self.tpMed.xml
        xml += self.qCarga.xml
        xml += '</infQ>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUnid.xml  = arquivo
            self.tpMed.xml = arquivo
            self.qCarga.xml = arquivo

    xml = property(get_xml, set_xml)


class InfCarga(XMLNFe):
    def __init__(self):
        super(InfCarga, self).__init__()
        self.vCarga  = TagDecimal(nome='vCarga'  , tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/infCTeNorm/infCarga', obrigatorio=False)
        self.proPred = TagCaracter(nome='proPred', tamanho=[1, 60]   ,                     raiz='//CTe/infCte/infCTeNorm/infCarga')
        self.xOutCat = TagCaracter(nome='xOutCat', tamanho=[1, 30]   ,                     raiz='//CTe/infCte/infCTeNorm/infCarga', obrigatorio=False)
        self.infQ    = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCarga>'
        xml += self.vCarga.xml
        xml += self.proPred.xml
        xml += self.xOutCat.xml

        for i in self.infQ:
            xml += i.xml

        xml += '</infCarga>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vCarga.xml  = arquivo
            self.proPred.xml = arquivo
            self.xOutCat.xml = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.infQ = self.le_grupo('//CTe/infCte/infCTeNorm/infCarga/infQ', InfQ, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class InfCTeNorm(XMLNFe):
    def __init__(self):
        super(InfCTeNorm, self).__init__()
        self.infCarga = InfCarga()
        self.contQt = []
        #self.docAnt = DocAnt()
        self.seg = []
        #self.infModal = InfModal()
        self.peri = []
        self.veicNovos = []
        self.cobr = Cobr()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCTeNorm>'
        xml += self.infCarga.xml

        for q in self.contQt:
            xml += q.xml

        #xml += self.docAnt.xml

        for s in self.seg:
            xml += s.xml

        #xml += self.infModal.xml

        for p in self.peri:
            xml += p.xml

        for v in self.veicNovos:
            xml += v.xml

        xml += self.cobr.xml
        xml += '</infCTeNorm>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infCarga.xml = arquivo
            self.cobr.xml     = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            #self.contQt    = self.le_grupo('//CTe/infCte/infCTeNorm/contQt'   , ContQt   , sigla_ns='cte')
            #self.seg       = self.le_grupo('//CTe/infCte/infCTeNorm/seg'      , Seg      , sigla_ns='cte')
            #self.peri      = self.le_grupo('//CTe/infCte/infCTeNorm/peri'     , Peri     , sigla_ns='cte')
            #self.veicNovos = self.le_grupo('//CTe/infCte/infCTeNorm/veicNovos', VeicNovos, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class TagCSTICMS(TagCaracter):
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
        #self.grupo_icms.modBC.obrigatorio    = False
        self.grupo_icms.pRedBC.obrigatorio   = False
        self.grupo_icms.vBC.obrigatorio      = False
        self.grupo_icms.pICMS.obrigatorio    = False
        self.grupo_icms.vICMS.obrigatorio    = False
        #self.grupo_icms.modBCST.obrigatorio  = False
        #self.grupo_icms.pMVAST.obrigatorio   = False
        #self.grupo_icms.pRedBCST.obrigatorio = False
        self.grupo_icms.vBCSTRet.obrigatorio    = False
        self.grupo_icms.pICMSSTRet.obrigatorio  = False
        self.grupo_icms.vICMSSTRet.obrigatorio  = False
        self.grupo_icms.vCred.obrigatorio  = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo ICMS ao redefinirmos o código da situação
        # tributária
        #
        #self.grupo_icms.modBC.valor    = 3
        self.grupo_icms.pRedBC.valor   = '0.00'
        self.grupo_icms.vBC.valor      = '0.00'
        self.grupo_icms.pICMS.valor    = '0.00'
        self.grupo_icms.vICMS.valor    = '0.00'
        #self.grupo_icms.modBCST.valor  = 4
        #self.grupo_icms.pMVAST.valor   = '0.00'
        #self.grupo_icms.pRedBCST.valor = '0.00'
        self.grupo_icms.vBCSTRet.valor    = '0.00'
        self.grupo_icms.pICMSSTRet.valor  = '0.00'
        self.grupo_icms.vICMSSTRet.valor  = '0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de ICMS
        #
        if self.valor == '00':
            self.grupo_icms.nome_tag = 'ICMS00'
            self.grupo_icms.nome_tag_txt = 'N02'
            self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS00'
            #self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True

        elif self.valor == '20':
            self.grupo_icms.nome_tag = 'ICMS20'
            self.grupo_icms.nome_tag_txt = 'N04'
            self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS20'
            #self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.pRedBC.obrigatorio   = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True

        elif self.valor in ('40', '41', '51'):
            self.grupo_icms.nome_tag = 'ICMS45'
            self.grupo_icms.nome_tag_txt = 'N06'
            self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS45'

        elif self.valor == '60':
            self.grupo_icms.nome_tag = 'ICMS60'
            self.grupo_icms.nome_tag_txt = 'N08'
            self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS60'
            self.grupo_icms.vBCSTRet.obrigatorio   = True
            self.grupo_icms.pICMSSTRet.obrigatorio   = True
            self.grupo_icms.vICMSSTRet.obrigatorio = True

        elif self.valor == '90':
            self.grupo_icms.nome_tag = 'ICMS90'
            self.grupo_icms.nome_tag_txt = 'N10'
            self.grupo_icms.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS90'
            #self.grupo_icms.pRedBC.obrigatorio   = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True

        #
        # Redefine a raiz para todas as tags do grupo ICMS
        #
        #self.grupo_icms.orig.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.CST.raiz      = self.grupo_icms.raiz_tag
        #self.grupo_icms.modBC.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBC.raiz   = self.grupo_icms.raiz_tag
        self.grupo_icms.vBC.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMS.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMS.raiz    = self.grupo_icms.raiz_tag
        #self.grupo_icms.modBCST.raiz  = self.grupo_icms.raiz_tag
        #self.grupo_icms.pMVAST.raiz   = self.grupo_icms.raiz_tag
        #self.grupo_icms.pRedBCST.raiz = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCSTRet.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMSSTRet.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSSTRet.raiz  = self.grupo_icms.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class ICMS(XMLNFe):
    def __init__(self):
        super(ICMS, self).__init__()
        #self.orig     = TagInteiro(nome='orig'     , tamanho=[1,  1, 1],                     raiz='')
        #self.modBC    = TagInteiro(nome='modBC'    , tamanho=[1,  1, 1],                     raiz='')
        self.pRedBC   = TagDecimal(nome='pRedBC'    , tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vBC      = TagDecimal(nome='vBC'       , tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.pICMS    = TagDecimal(nome='pICMS'     , tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vICMS    = TagDecimal(nome='vICMS'     , tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        #self.modBCST  = TagInteiro(nome='modBCST'  , tamanho=[1,  1, 1],                     raiz='')
        #self.pMVAST   = TagDecimal(nome='pMVAST'   , tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        #self.pRedBCST = TagDecimal(nome='pRedBCST' , tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vBCSTRet   = TagDecimal(nome='vBCSTRet'  , tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.pICMSSTRet = TagDecimal(nome='pICMSSTRet', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vICMSSTRet = TagDecimal(nome='vICMSSTRet', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')
        self.vCred      = TagDecimal(nome='vCred'     , tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='')

        self.CST      = TagCSTICMS()
        self.CST.grupo_icms = self
        self.CST.valor = '40'
        self.nome_tag = 'ICMS45'
        self.raiz_tag = '//CTe/infCte/imp/ICMS/ICMS45'
        self.nome_tag_txt = 'N06'

    def get_xml(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += '<ICMS><' + self.nome_tag + '>'
        #xml += self.orig.xml
        xml += self.CST.xml

        if self.CST.valor == '00':
            #xml += self.modBC.xml
            xml += self.vBC.xml
            xml += self.pICMS.xml
            xml += self.vICMS.xml

        elif self.CST.valor == '20':
            #xml += self.modBC.xml
            xml += self.pRedBC.xml
            xml += self.vBC.xml
            xml += self.pICMS.xml
            xml += self.vICMS.xml

        elif self.CST.valor in ('40', '41', '51'):
            pass

        elif self.CST.valor == '60':
            xml += self.vBCSTRet.xml
            xml += self.pICMSSTRet.xml
            xml += self.vICMSSTRet.xml

        elif self.CST.valor == '90':
            #xml += self.modBC.xml
            xml += self.pRedBC.xml
            xml += self.vBC.xml
            xml += self.pICMS.xml
            xml += self.vICMS.xml
            xml += self.vCred.xml

        xml += '</' + self.nome_tag + '></ICMS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o ICMS, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            if self._le_noh('//CTe/infCte/imp/ICMS/ICMS00') is not None:
                self.CST.valor = '00'
            elif self._le_noh('//CTe/infCte/imp/ICMS/ICMS20') is not None:
                self.CST.valor = '20'
            elif self._le_noh('//CTe/infCte/imp/ICMS/ICMS45') is not None:
                self.CST.valor = '40'
            elif self._le_noh('//CTe/infCte/imp/ICMS/ICMS60') is not None:
                self.CST.valor = '60'
            elif self._le_noh('//CTe/infCte/imp/ICMS/ICMS90') is not None:
                self.CST.valor = '90'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            #self.orig.xml     = arquivo
            self.CST.xml      = arquivo
            #self.modBC.xml    = arquivo
            self.pRedBC.xml   = arquivo
            self.vBC.xml      = arquivo
            self.pICMS.xml    = arquivo
            self.vICMS.xml    = arquivo
            #self.modBCST.xml  = arquivo
            #self.pMVAST.xml   = arquivo
            #self.pRedBCST.xml = arquivo
            self.vBCSTRet.xml    = arquivo
            self.pICMSSTRet.xml  = arquivo
            self.vICMSSTRet.xml  = arquivo
            self.vCred.xml       = arquivo

    xml = property(get_xml, set_xml)


class Imp(XMLNFe):
    def __init__(self):
        super(Imp, self).__init__()
        self.ICMS     = ICMS()
        self.infAdFisco = TagCaracter(nome='infAdFisco', tamanho=[1, 2000], raiz='//CTe/infCte/imp', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<imp>'
        xml += self.ICMS.xml
        xml += self.infAdFisco.xml
        xml += '</imp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ICMS.xml       = arquivo
            self.infAdFisco.xml = arquivo

    xml = property(get_xml, set_xml)


class VPrest(XMLNFe):
    def __init__(self):
        super(VPrest, self).__init__()
        self.vTPrest = TagDecimal(nome='vTPrest', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/vPrest')
        self.vRec = TagDecimal(nome='vRec', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//CTe/infCte/vPrest')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<vPrest>'
        xml += self.vTPrest.xml
        xml += self.vRec.xml
        xml += '</vPrest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vTPrest.xml  = arquivo
            self.vRec.xml = arquivo

    xml = property(get_xml, set_xml)


class LocEnt(XMLNFe):
    def __init__(self):
        super(LocEnt, self).__init__()
        self.CNPJ    = TagCaracter(nome='CNPJ'   , codigo='E02', tamanho=[ 0, 14]   , raiz='//CTe/infCte/dest/locEnt', obrigatorio=False)
        self.CPF     = TagCaracter(nome='CPF'    , codigo='E03', tamanho=[11, 11]   , raiz='//CTe/infCte/dest/locEnt', obrigatorio=False)
        self.xNome   = TagCaracter(nome='xNome'  , codigo='E04', tamanho=[ 2, 60]   , raiz='//CTe/infCte/dest/locEnt')
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='G02', tamanho=[ 2, 60]   , raiz='//CTe/infCte/dest/locEnt')
        self.nro     = TagCaracter(nome='nro'    , codigo='G03', tamanho=[ 1, 60]   , raiz='//CTe/infCte/dest/locEnt')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='G04', tamanho=[ 1, 60]   , raiz='//CTe/infCte/dest/locEnt', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='G05', tamanho=[ 2, 60]   , raiz='//CTe/infCte/dest/locEnt')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='G06', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/dest/locEnt')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='G07', tamanho=[ 2, 60]   , raiz='//CTe/infCte/dest/locEnt')
        self.UF      = TagCaracter(nome='UF'     , codigo='G08', tamanho=[ 2,  2]   , raiz='//CTe/infCte/dest/locEnt')

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<locEnt>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.xNome.xml
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += '</locEnt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml = arquivo
            self.CPF.xml = arquivo
            self.xNome.xml    = arquivo
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.UF.xml      = arquivo

    xml = property(get_xml, set_xml)


class EnderDest(XMLNFe):
    def __init__(self):
        super(EnderDest, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='E06', tamanho=[ 1, 255]  , raiz='//CTe/infCte/dest/enderDest')
        self.nro     = TagCaracter(nome='nro'    , codigo='E07', tamanho=[ 1, 60]   , raiz='//CTe/infCte/dest/enderDest')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='E08', tamanho=[ 1, 60]   , raiz='//CTe/infCte/dest/enderDest', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='E09', tamanho=[ 2, 60]   , raiz='//CTe/infCte/dest/enderDest')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='E10', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/dest/enderDest')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='E11', tamanho=[ 2, 60]   , raiz='//CTe/infCte/dest/enderDest')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='E13', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/dest/enderDest', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='E12', tamanho=[ 2,  2]   , raiz='//CTe/infCte/dest/enderDest')
        self.cPais   = TagInteiro(nome='cPais'   , codigo='E14', tamanho=[ 4,  4, 4], raiz='//CTe/infCte/dest/enderDest', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , codigo='E15', tamanho=[ 1, 60]   , raiz='//CTe/infCte/dest/enderDest', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderDest>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += '</enderDest>'
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
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo

    xml = property(get_xml, set_xml)


class Dest(XMLNFe):
    def __init__(self):
        super(Dest, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='E02', tamanho=[ 0, 14], raiz='//CTe/infCte/dest', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , codigo='E03', tamanho=[11, 11], raiz='//CTe/infCte/dest', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , codigo='E17', tamanho=[ 2, 14], raiz='//CTe/infCte/dest', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='E04', tamanho=[ 2, 60], raiz='//CTe/infCte/dest')
        self.fone      = TagInteiro(nome='fone'  , codigo='E16', tamanho=[ 7, 12], raiz='//CTe/infCte/dest', obrigatorio=False)
        self.ISUF      = TagCaracter(nome='ISUF' , codigo='E18', tamanho=[ 9,  9], raiz='//CTe/infCte/dest', obrigatorio=False)
        self.enderDest = EnderDest()
        self.email     = TagCaracter(nome='email', codigo='E19', tamanho=[ 1, 60], raiz='//CTe/infCte/dest', obrigatorio=False)
        self.locEnt    = LocEnt()

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<dest>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.IE.xml
        xml += self.xNome.xml
        xml += self.fone.xml
        xml += self.ISUF.xml
        xml += self.enderDest.xml
        xml += self.email.xml
        xml += self.locEnt.xml
        xml += '</dest>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.fone.xml      = arquivo
            self.ISUF.xml      = arquivo
            self.enderDest.xml = arquivo
            self.email.xml     = arquivo
            self.locEnt.xml    = arquivo

    xml = property(get_xml, set_xml)


class EnderReceb(XMLNFe):
    def __init__(self):
        super(EnderReceb, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='E06', tamanho=[ 1, 255]  , raiz='//CTe/infCte/receb/enderReceb')
        self.nro     = TagCaracter(nome='nro'    , codigo='E07', tamanho=[ 1, 60]   , raiz='//CTe/infCte/receb/enderReceb')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='E08', tamanho=[ 1, 60]   , raiz='//CTe/infCte/receb/enderReceb', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='E09', tamanho=[ 2, 60]   , raiz='//CTe/infCte/receb/enderReceb')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='E10', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/receb/enderReceb')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='E11', tamanho=[ 2, 60]   , raiz='//CTe/infCte/receb/enderReceb')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='E13', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/receb/enderReceb', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='E12', tamanho=[ 2,  2]   , raiz='//CTe/infCte/receb/enderReceb')
        self.cPais   = TagInteiro(nome='cPais'   , codigo='E14', tamanho=[ 4,  4, 4], raiz='//CTe/infCte/receb/enderReceb', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , codigo='E15', tamanho=[ 1, 60]   , raiz='//CTe/infCte/receb/enderReceb', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderReceb>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += '</enderReceb>'
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
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo

    xml = property(get_xml, set_xml)


class Receb(XMLNFe):
    def __init__(self):
        super(Receb, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='E02', tamanho=[ 0, 14], raiz='//CTe/infCte/receb', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , codigo='E03', tamanho=[11, 11], raiz='//CTe/infCte/receb', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , codigo='E17', tamanho=[ 2, 14], raiz='//CTe/infCte/receb', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='E04', tamanho=[ 2, 60], raiz='//CTe/infCte/receb')
        self.fone      = TagInteiro(nome='fone'  , codigo='E16', tamanho=[ 7, 12], raiz='//CTe/infCte/receb', obrigatorio=False)
        self.enderReceb = EnderReceb()
        self.email     = TagCaracter(nome='email', codigo='E19', tamanho=[ 1, 60], raiz='//CTe/infCte/receb', obrigatorio=False)

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<receb>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.IE.xml
        xml += self.xNome.xml
        xml += self.fone.xml
        xml += self.enderReceb.xml
        xml += self.email.xml
        xml += '</receb>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.fone.xml      = arquivo
            self.enderReceb.xml = arquivo
            self.email.xml     = arquivo

    xml = property(get_xml, set_xml)


class EnderExped(XMLNFe):
    def __init__(self):
        super(EnderExped, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='E06', tamanho=[ 1, 255]  , raiz='//CTe/infCte/exped/enderExped')
        self.nro     = TagCaracter(nome='nro'    , codigo='E07', tamanho=[ 1, 60]   , raiz='//CTe/infCte/exped/enderExped')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='E08', tamanho=[ 1, 60]   , raiz='//CTe/infCte/exped/enderExped', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='E09', tamanho=[ 2, 60]   , raiz='//CTe/infCte/exped/enderExped')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='E10', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/exped/enderExped')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='E11', tamanho=[ 2, 60]   , raiz='//CTe/infCte/exped/enderExped')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='E13', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/exped/enderExped', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='E12', tamanho=[ 2,  2]   , raiz='//CTe/infCte/exped/enderExped')
        self.cPais   = TagInteiro(nome='cPais'   , codigo='E14', tamanho=[ 4,  4, 4], raiz='//CTe/infCte/exped/enderExped', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , codigo='E15', tamanho=[ 1, 60]   , raiz='//CTe/infCte/exped/enderExped', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderExped>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += '</enderExped>'
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
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo

    xml = property(get_xml, set_xml)


class Exped(XMLNFe):
    def __init__(self):
        super(Exped, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='E02', tamanho=[ 0, 14], raiz='//CTe/infCte/exped', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , codigo='E03', tamanho=[11, 11], raiz='//CTe/infCte/exped', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , codigo='E17', tamanho=[ 2, 14], raiz='//CTe/infCte/exped', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='E04', tamanho=[ 2, 60], raiz='//CTe/infCte/exped')
        self.fone      = TagInteiro(nome='fone'  , codigo='E16', tamanho=[ 7, 12], raiz='//CTe/infCte/exped', obrigatorio=False)
        self.enderExped = EnderExped()
        self.email     = TagCaracter(nome='email', codigo='E19', tamanho=[ 1, 60], raiz='//CTe/infCte/exped', obrigatorio=False)

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<exped>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.IE.xml
        xml += self.xNome.xml
        xml += self.fone.xml
        xml += self.enderExped.xml
        xml += self.email.xml
        xml += '</exped>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.fone.xml      = arquivo
            self.enderExped.xml = arquivo
            self.email.xml     = arquivo

    xml = property(get_xml, set_xml)


class InfOutros(XMLNFe):
    def __init__(self):
        super(InfOutros, self).__init__()
        self.tpDoc  = TagCaracter(nome='tpDoc', codigo='B16', tamanho=[ 2,  2]   , raiz='//infOutros', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, valor='99')
        self.descOutros = TagCaracter(nome='descOutros', codigo='B16', tamanho=[ 1, 100], raiz='//infOutros', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.nDoc   = TagInteiro(nome='nDoc'  , codigo='B20', tamanho=[ 1, 20]   , raiz='//infOutros', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dEmi   = TagData(nome='dEmi'     , codigo='B09',                      raiz='//infOutros', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vDocFisc = TagDecimal(nome='vDocFisc', codigo='W16', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infOutros', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.tpDoc.valor or self.descOutros.valor or self.nDoc.valor or self.dEmi.valor or self.vDocFisc.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infOutros>'
        xml += self.tpDoc.xml
        xml += self.descOutros.xml
        xml += self.nDoc.xml
        xml += self.dEmi.xml
        xml += self.vDocFisc.xml
        xml += '</infOutros>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpDoc.xml   = arquivo
            self.descOutros.xml    = arquivo
            self.nDoc.xml    = arquivo
            self.dEmi.xml    = arquivo
            self.vDocFisc.xml     = arquivo

    xml = property(get_xml, set_xml)


class InfNFe(XMLNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.chave  = TagCaracter(nome='chave', codigo='B16', tamanho=[44, 44]   , raiz='//infNFe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.PIN    = TagInteiro(nome='PIN'   , codigo='B20', tamanho=[ 2, 9]    , raiz='//infNFe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        if not self.chave.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infNFe>'
        xml += self.chave.xml
        xml += self.PIN.xml
        xml += '</infNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chave.xml   = arquivo
            self.PIN.xml     = arquivo

    xml = property(get_xml, set_xml)


class LocRet(XMLNFe):
    def __init__(self):
        super(LocRet, self).__init__()
        self.CNPJ    = TagCaracter(nome='CNPJ'   , codigo='E02', tamanho=[ 0, 14]   , raiz='//infNF/locRet', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.CPF     = TagCaracter(nome='CPF'    , codigo='E03', tamanho=[11, 11]   , raiz='//infNF/locRet', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.xNome   = TagCaracter(nome='xNome'  , codigo='E04', tamanho=[ 2, 60]   , raiz='//infNF/locRet', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='E04', tamanho=[ 1, 255]  , raiz='//infNF/locRet', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nro     = TagCaracter(nome='nro'    , codigo='F03', tamanho=[ 1, 60]   , raiz='//infNF/locRet', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='F04', tamanho=[ 1, 60]   , raiz='//infNF/locRet', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='F05', tamanho=[ 2, 60]   , raiz='//infNF/locRet', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cMun    = TagInteiro(nome='cMun'    , codigo='F06', tamanho=[ 7,  7, 7], raiz='//infNF/locRet', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xMun    = TagCaracter(nome='xMun'   , codigo='F07', tamanho=[ 2, 60]   , raiz='//infNF/locRet', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='F08', tamanho=[ 2,  2]   , raiz='//infNF/locRet', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<locRet>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.xNome.xml
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += '</locRet>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml = arquivo
            self.CPF.xml = arquivo
            self.xNome.xml   = arquivo
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.UF.xml      = arquivo

    xml = property(get_xml, set_xml)


class InfNF(XMLNFe):
    def __init__(self):
        super(InfNF, self).__init__()
        self.nRoma  = TagCaracter(nome='nRoma', codigo='B16', tamanho=[ 1, 20]   , raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.nPed   = TagCaracter(nome='nPed' , codigo='B16', tamanho=[ 1, 20]   , raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.mod    = TagCaracter(nome='mod'  , codigo='B18', tamanho=[ 2,  2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.serie  = TagCaracter(nome='serie' , codigo='B19', tamanho=[ 1,  3, 1], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nDoc   = TagInteiro(nome='nDoc'  , codigo='B20', tamanho=[ 1, 20]   , raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dEmi   = TagData(nome='dEmi'     , codigo='B09',                      raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vBC    = TagDecimal(nome='vBC'   , codigo='W03', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vICMS  = TagDecimal(nome='vICMS' , codigo='W04', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vBCST  = TagDecimal(nome='vBCST' , codigo='W05', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vST    = TagDecimal(nome='vST'   , codigo='W06', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vProd  = TagDecimal(nome='vProd' , codigo='W07', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vNF    = TagDecimal(nome='vNF'   , codigo='W16', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nCFOP  = TagInteiro(nome='nCFOP' , codigo='I08', tamanho=[4,  4, 4]                    , raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nPeso  = TagDecimal(nome='nPeso' , codigo='W16', tamanho=[1, 12, 1], decimais=[0, 3, 3], raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.PIN    = TagInteiro(nome='PIN'   , codigo='B20', tamanho=[ 2, 9]    , raiz='//infNF', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.locRet = LocRet()

    def get_xml(self):
        if not self.mod.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infNF>'
        xml += self.nRoma.xml
        xml += self.nPed.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nDoc.xml
        xml += self.dEmi.xml
        xml += self.vBC.xml
        xml += self.vICMS.xml
        xml += self.vBCST.xml
        xml += self.vST.xml
        xml += self.vProd.xml
        xml += self.vNF.xml
        xml += self.nCFOP.xml
        xml += self.nPeso.xml
        xml += self.PIN.xml
        xml += self.locRet.xml
        xml += '</infNF>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nRoma.xml   = arquivo
            self.nPed.xml    = arquivo
            self.mod.xml     = arquivo
            self.serie.xml   = arquivo
            self.nDoc.xml    = arquivo
            self.dEmi.xml    = arquivo
            self.vBC.xml     = arquivo
            self.vICMS.xml   = arquivo
            self.vBCST.xml   = arquivo
            self.vST.xml     = arquivo
            self.vProd.xml   = arquivo
            self.vNF.xml     = arquivo
            self.nCFOP.xml   = arquivo
            self.nPeso.xml   = arquivo
            self.PIN.xml     = arquivo
            self.locRet.xml  = arquivo

    xml = property(get_xml, set_xml)


class EnderReme(XMLNFe):
    def __init__(self):
        super(EnderReme, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='E06', tamanho=[ 1, 255]  , raiz='//CTe/infCte/rem/enderReme')
        self.nro     = TagCaracter(nome='nro'    , codigo='E07', tamanho=[ 1, 60]   , raiz='//CTe/infCte/rem/enderReme')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='E08', tamanho=[ 1, 60]   , raiz='//CTe/infCte/rem/enderReme', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='E09', tamanho=[ 2, 60]   , raiz='//CTe/infCte/rem/enderReme')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='E10', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/rem/enderReme')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='E11', tamanho=[ 2, 60]   , raiz='//CTe/infCte/rem/enderReme')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='E13', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/rem/enderReme', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='E12', tamanho=[ 2,  2]   , raiz='//CTe/infCte/rem/enderReme')
        self.cPais   = TagInteiro(nome='cPais'   , codigo='E14', tamanho=[ 4,  4, 4], raiz='//CTe/infCte/rem/enderReme', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , codigo='E15', tamanho=[ 1, 60]   , raiz='//CTe/infCte/rem/enderReme', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderReme>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += '</enderReme>'
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
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo

    xml = property(get_xml, set_xml)


class Rem(XMLNFe):
    def __init__(self):
        super(Rem, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='E02', tamanho=[ 0, 14], raiz='//CTe/infCte/rem', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , codigo='E03', tamanho=[11, 11], raiz='//CTe/infCte/rem', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , codigo='E17', tamanho=[ 2, 14], raiz='//CTe/infCte/rem', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='E04', tamanho=[ 2, 60], raiz='//CTe/infCte/rem')
        self.xFant     = TagCaracter(nome='xFant', codigo='E04', tamanho=[ 1, 60], raiz='//CTe/infCte/rem', obrigatorio=False)
        self.fone      = TagInteiro(nome='fone'  , codigo='E16', tamanho=[ 7, 12], raiz='//CTe/infCte/rem', obrigatorio=False)
        self.enderReme = EnderReme()
        self.email     = TagCaracter(nome='email', codigo='E19', tamanho=[ 1, 60], raiz='//CTe/infCte/rem', obrigatorio=False)
        self.infNF     = []
        self.infNFe    = []
        self.infOutros = []

    def get_xml(self):
        if self.CNPJ.valor == '' and self.CPF.valor == '':
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<rem>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.IE.xml
        xml += self.xNome.xml
        xml += self.xFant.xml
        xml += self.fone.xml
        xml += self.enderReme.xml
        xml += self.email.xml

        for inf in self.infNF:
            xml += inf.xml

        for infe in self.infNFe:
            xml += infe.xml

        for iou in self.infOutros:
            xml += iou.xml

        xml += '</rem>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.xFant.xml     = arquivo
            self.fone.xml      = arquivo
            self.enderReme.xml = arquivo
            self.email.xml     = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.infNF  = self.le_grupo('//CTe/infCte/rem/infNF', InfNF, sigla_ns='cte')
            self.infNFe = self.le_grupo('//CTe/infCte/rem/infNFe', InfNFe, sigla_ns='cte')
            self.infOutros = self.le_grupo('//CTe/infCte/rem/infOutros', InfOutros, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class EnderEmit(XMLNFe):
    def __init__(self):
        super(EnderEmit, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='C06', tamanho=[ 2, 60]   , raiz='//CTe/infCte/emit/enderEmit')
        self.nro     = TagCaracter(nome='nro'    , codigo='C07', tamanho=[ 1, 60]   , raiz='//CTe/infCte/emit/enderEmit')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='C08', tamanho=[ 1, 60]   , raiz='//CTe/infCte/emit/enderEmit', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='C09', tamanho=[ 2, 60]   , raiz='//CTe/infCte/emit/enderEmit')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='C10', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/emit/enderEmit')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='C11', tamanho=[ 2, 60]   , raiz='//CTe/infCte/emit/enderEmit')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='C13', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/emit/enderEmit', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='C12', tamanho=[ 2,  2]   , raiz='//CTe/infCte/emit/enderEmit')
        #self.cPais   = TagInteiro(nome='cPais'   , codigo='C14', tamanho=[ 4,  4, 4], raiz='//CTe/infCte/emit/enderEmit', obrigatorio=False)
        #self.xPais   = TagCaracter(nome='xPais'  , codigo='C15', tamanho=[ 1, 60]   , raiz='//CTe/infCte/emit/enderEmit', obrigatorio=False)
        self.fone    = TagInteiro(nome='fone'    , codigo='C16', tamanho=[ 1, 12]   , raiz='//CTe/infCte/emit/enderEmit', obrigatorio=False)

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
        #xml += self.cPais.xml
        #xml += self.xPais.xml
        xml += self.fone.xml
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
            #self.cPais.xml   = arquivo
            #self.xPais.xml   = arquivo
            self.fone.xml    = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'C05|'
        txt += self.xLgr.txt + '|'
        txt += self.nro.txt + '|'
        txt += self.xCpl.txt + '|'
        txt += self.xBairro.txt + '|'
        txt += self.cMun.txt + '|'
        txt += self.xMun.txt + '|'
        txt += self.CEP.txt + '|'
        txt += self.UF.txt + '|'
        #txt += self.cPais.txt + '|'
        #txt += self.xPais.txt + '|'
        txt += self.fone.txt + '|'
        txt += '\n'

        return txt

    txt = property(get_txt)


class Emit(XMLNFe):
    def __init__(self):
        super(Emit, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='C02' , tamanho=[14, 14], raiz='//CTe/infCte/emit', obrigatorio=False)
        #self.CPF       = TagCaracter(nome='CPF'  , codigo='C02a', tamanho=[11, 11], raiz='//CTe/infCte/emit', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , codigo='C17' , tamanho=[ 2, 14], raiz='//CTe/infCte/emit', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='C03' , tamanho=[ 2, 60], raiz='//CTe/infCte/emit')
        self.xFant     = TagCaracter(nome='xFant', codigo='C04' , tamanho=[ 1, 60], raiz='//CTe/infCte/emit', obrigatorio=False)
        self.enderEmit = EnderEmit()
        #self.IEST      = TagCaracter(nome='IEST' , codigo='C18' , tamanho=[ 2, 14], raiz='//CTe/infCte/emit', obrigatorio=False)
        #self.IM        = TagCaracter(nome='IM'   , codigo='C19' , tamanho=[ 1, 15], raiz='//CTe/infCte/emit', obrigatorio=False)
        #self.CNAE      = TagCaracter(nome='CNAE' , codigo='C20' , tamanho=[ 7,  7], raiz='//CTe/infCte/emit', obrigatorio=False)


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<emit>'
        xml += self.CNPJ.xml
        #xml += self.CPF.xml
        xml += self.IE.xml
        xml += self.xNome.xml
        xml += self.xFant.xml
        xml += self.enderEmit.xml
        #xml += self.IEST.xml
        #xml += self.IM.xml
        #xml += self.CNAE.xml
        xml += '</emit>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            #self.CPF.xml       = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.xFant.xml     = arquivo
            self.enderEmit.xml = arquivo
            #self.IEST.xml      = arquivo
            #self.IM.xml        = arquivo
            #self.CNAE.xml      = arquivo

    xml = property(get_xml, set_xml)


class ObsFisco(XMLNFe):
    def __init__(self):
        super(ObsFisco, self).__init__()
        self.xCampo = TagCaracter(nome='ObsFisco', codigo='Z08', propriedade='xCampo', tamanho=[1, 20], raiz='/', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xTexto = TagCaracter(nome='xTexto', codigo='Z09', tamanho=[1, 160], raiz='//ObsFisco', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.xCampo.valor or self.xTexto.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ObsFisco xCampo="' + self.xCampo.valor + '">'
        xml += self.xTexto.xml
        xml += '</ObsFisco>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xCampo.xml = arquivo
            self.xTexto.xml = arquivo

    xml = property(get_xml, set_xml)


class ObsCont(XMLNFe):
    def __init__(self):
        super(ObsCont, self).__init__()
        self.xCampo = TagCaracter(nome='ObsCont', propriedade='xCampo', tamanho=[1,  20], raiz='/', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xTexto = TagCaracter(nome='xTexto', codigo='Z06', tamanho=[1, 160], raiz='//ObsCont', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not (self.xCampo.valor or self.xTexto.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ObsCont xCampo="' + self.xCampo.valor + '">'
        xml += self.xTexto.xml
        xml += '</ObsCont>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xCampo.xml = arquivo
            self.xTexto.xml = arquivo

    xml = property(get_xml, set_xml)


class Entrega(XMLNFe):
    def __init__(self):
        super(Entrega, self).__init__()
        #
        # Data da entrega
        #
        self.tpPer = TagCaracter(nome='tpPer', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/semData')
        self.tpPerSemData = TagCaracter(nome='tpPer', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/semData', obrigatorio=False)
        self.tpPerComData = TagCaracter(nome='tpPer', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/comData', obrigatorio=False)
        self.dProg = TagData(nome='dProg', raiz='//CTe/infCte/compl/Entrega/comData')
        self.tpPerNoPeriodo = TagCaracter(nome='tpPer', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/noPeriodo', obrigatorio=False)
        self.dIni = TagData(nome='dIni', raiz='//CTe/infCte/compl/Entrega/noPeriodo')
        self.dFim = TagData(nome='dFim', raiz='//CTe/infCte/compl/Entrega/noPeriodo')

        #
        # Hora da entrega
        #
        self.tpHor = TagCaracter(nome='tpHor', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/semHora')
        self.tpHorSemHora = TagCaracter(nome='tpHor', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/semHora', obrigatorio=False)
        self.tpHorComHora = TagCaracter(nome='tpHor', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/comHora', obrigatorio=False)
        self.hProg = TagHora(nome='hProg', raiz='//CTe/infCte/compl/Entrega/comHora')
        self.tpHorNoInter = TagCaracter(nome='tpHor', tamanho=[1, 1, 1], raiz='//CTe/infCte/compl/Entrega/noInter', obrigatorio=False)
        self.hIni = TagHora(nome='hIni', raiz='//CTe/infCte/compl/Entrega/noInter')
        self.hFim = TagHora(nome='hFim', raiz='//CTe/infCte/compl/Entrega/noInter')


    def get_xml(self):
        if not (self.tpPer.valor and self.tpHor.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<Entrega>'

        if self.tpPer.valor == '0':
            xml += '<semData>'
            xml += self.tpPer.xml
            xml += '</semData>'

        elif self.tpPer.valor <= '3':
            xml += '<comData>'
            xml += self.tpPer.xml
            xml += self.dProg.xml
            xml += '</comData>'

        else:
            xml += '<noPeriodo>'
            xml += self.tpPer.xml
            xml += self.dIni.xml
            xml += self.dFim.xml
            xml += '</noPeriodo>'

        if self.tpHor.valor == '0':
            xml += '<semHora>'
            xml += self.tpHor.xml
            xml += '</semHora>'

        elif self.tpHor.valor <= '3':
            xml += '<comHora>'
            xml += self.tpHor.xml
            xml += self.hProg.xml
            xml += '</comHora>'

        else:
            xml += '<noInter>'
            xml += self.tpHor.xml
            xml += self.hIni.xml
            xml += self.hFim.xml
            xml += '</noInter>'

        xml += '</Entrega>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):

            if self._le_noh('//CTe/infCte/compl/Entrega/semData') is not None:
                self.tpPerSemData.xml = arquivo
                self.tpPer.valor = self.tpPerSemData.valor
            elif self._le_noh('//CTe/infCte/compl/Entrega/comData') is not None:
                self.tpPerComData.xml = arquivo
                self.tpPer.valor = self.tpPerComData.valor
            else:
                self.tpPerNoPeriodo.xml = arquivo
                self.tpPer.valor = self.tpPerNoPeriodo.valor

            self.dProg.xml = arquivo
            self.dIni.xml = arquivo
            self.dFim.xml = arquivo

            if self._le_noh('//CTe/infCte/compl/Entrega/semHora') is not None:
                self.tpHorSemHora.xml = arquivo
                self.tpHor.valor = self.tpHorSemHora.valor
            elif self._le_noh('//CTe/infCte/compl/Entrega/comHora') is not None:
                self.tpHorComHora.xml = arquivo
                self.tpHor.valor = self.tpHorComHora.valor
            else:
                self.tpHorNoInter.xml = arquivo
                self.tpHor.valor = self.tpHorNoInter.valor

            self.hProg.xml = arquivo
            self.hIni.xml = arquivo
            self.hFim.xml = arquivo

    xml = property(get_xml, set_xml)


class Pass(XMLNFe):
    def __init__(self):
        super(Pass, self).__init__()
        self.xPass = TagCaracter(nome='xPass', tamanho=[1,  15], raiz='//pass', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)

    def get_xml(self):
        if not self.xPass.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<pass>'
        xml += self.xPass.xml
        xml += '</pass>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xPass.xml = arquivo

    xml = property(get_xml, set_xml)


class Fluxo(XMLNFe):
    def __init__(self):
        super(Fluxo, self).__init__()
        self.xOrig = TagCaracter(nome='xOrig', tamanho=[1,  15], raiz='//CTe/infCte/compl/fluxo', obrigatorio=False)
        self.passagem = []
        self.xDest = TagCaracter(nome='xDest', tamanho=[1,  15], raiz='//CTe/infCte/compl/fluxo', obrigatorio=False)
        self.xRota = TagCaracter(nome='xRota', tamanho=[1,  15], raiz='//CTe/infCte/compl/fluxo', obrigatorio=False)

    def get_xml(self):
        if not (self.xOrig.valor or self.xDest.valor or self.xRota.valor or len(self.passagem)):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<fluxo>'
        xml += self.xOrig.xml

        if len(self.passagem):
            for p in self.passagem:
                xml += p.xml

        xml += self.xDest.xml
        xml += self.xRota.xml
        xml += '</fluxo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xOrig.xml = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.passagem = self.le_grupo('//CTe/infCte/compl/fluxo/pass', Pass, sigla_ns='cte')

            self.xDest.xml = arquivo
            self.xRota.xml = arquivo

    xml = property(get_xml, set_xml)


class Compl(XMLNFe):
    def __init__(self):
        super(Compl, self).__init__()
        self.xCaracAd = TagCaracter(nome='xCaracAd', tamanho=[ 1, 15], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.xCaracSer = TagCaracter(nome='xCaracSer', tamanho=[ 1, 30], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.xEmi = TagCaracter(nome='xEmi', tamanho=[ 1, 20], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.fluxo = Fluxo()
        self.Entrega = Entrega()
        self.origCalc = TagCaracter(nome='origCalc', tamanho=[ 1, 40], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.destCalc = TagCaracter(nome='destCalc', tamanho=[ 1, 40], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.xObs = TagCaracter(nome='xObs', tamanho=[ 1, 2000], raiz='//CTe/infCte/compl', obrigatorio=False)
        self.ObsCont = []
        self.ObsFisco = []

    def get_xml(self):
        if not (self.xCaracAd.valor or self.xCaracSer.valor or self.xEmi.valor or self.origCalc.valor or self.destCalc.valor or
            self.xObs.valor or len(self.ObsCont) or len(self.ObsFisco) or self.fluxo is not None or self.Entrega is not None):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<compl>'
        xml += self.xCaracAd.xml
        xml += self.xCaracSer.xml
        xml += self.xEmi.xml
        xml += self.fluxo.xml
        xml += self.Entrega.xml
        xml += self.origCalc.xml
        xml += self.destCalc.xml
        xml += self.xObs.xml

        for o in self.ObsCont:
            xml += o.xml

        for o in self.ObsFisco:
            xml += o.xml

        xml += '</compl>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xCaracAd.xml = arquivo
            self.xCaracSer.xml = arquivo
            self.xEmi.xml = arquivo
            self.fluxo.xml = arquivo
            self.Entrega.xml = arquivo
            self.origCalc.xml = arquivo
            self.destCalc.xml = arquivo
            self.xObs.xml = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.ObsCont = self.le_grupo('//CTe/infCte/compl/ObsCont', ObsCont, sigla_ns='cte')
            self.ObsFisco = self.le_grupo('//CTe/infCte/compl/ObsFisco', ObsFisco, sigla_ns='cte')

    xml = property(get_xml, set_xml)


class EnderToma(XMLNFe):
    def __init__(self):
        super(EnderToma, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='E06', tamanho=[ 1, 255]  , raiz='//CTe/infCte/ide/toma4/enderToma')
        self.nro     = TagCaracter(nome='nro'    , codigo='E07', tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide/toma4/enderToma')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='E08', tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide/toma4/enderToma', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='E09', tamanho=[ 2, 60]   , raiz='//CTe/infCte/ide/toma4/enderToma')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='E10', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/ide/toma4/enderToma')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='E11', tamanho=[ 2, 60]   , raiz='//CTe/infCte/ide/toma4/enderToma')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='E13', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/ide/toma4/enderToma', obrigatorio=False)
        self.UF      = TagCaracter(nome='UF'     , codigo='E12', tamanho=[ 2,  2]   , raiz='//CTe/infCte/ide/toma4/enderToma')
        self.cPais   = TagInteiro(nome='cPais'   , codigo='E14', tamanho=[ 4,  4, 4], raiz='//CTe/infCte/ide/toma4/enderToma', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , codigo='E15', tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide/toma4/enderToma', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderToma>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.CEP.xml
        xml += self.UF.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += '</enderToma>'
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
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo

    xml = property(get_xml, set_xml)


class Tomador(XMLNFe):
    def __init__(self):
        super(Tomador, self).__init__()
        self.toma      = TagInteiro(nome='toma'  , tamanho=[1, 1, 1], raiz='//CTe/infCte/ide/toma03', valor=0)
        self.toma03    = TagInteiro(nome='toma'  , tamanho=[1, 1, 1], raiz='//CTe/infCte/ide/toma03', valor=0)
        self.toma4     = TagInteiro(nome='toma'  , tamanho=[1, 1, 1], raiz='//CTe/infCte/ide/toma4', valor=4)
        self.CNPJ      = TagCaracter(nome='CNPJ' , tamanho=[ 0, 14], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , tamanho=[11, 11], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , tamanho=[ 2, 14], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', tamanho=[ 2, 60], raiz='//CTe/infCte/ide/toma4')
        self.xFant     = TagCaracter(nome='xFant', tamanho=[ 1, 60], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)
        self.fone      = TagInteiro(nome='fone'  , tamanho=[ 7, 12], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)
        self.enderToma = EnderToma()
        self.email     = TagCaracter(nome='email', tamanho=[ 1, 60], raiz='//CTe/infCte/ide/toma4', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.toma.valor < 4:
            xml += '<toma03>'
            xml += self.toma.xml
            xml += '</toma03>'

        else:
            xml += '<toma4>'
            xml += self.toma.xml

            if self.CPF.valor:
                xml += self.CPF.xml
            else:
                xml += self.CNPJ.xml

            xml += self.IE.xml
            xml += self.xNome.xml
            xml += self.xFant.xml
            xml += self.fone.xml
            xml += self.enderToma.xml
            xml += self.email.xml
            xml += '</toma4>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.IE.xml        = arquivo
            self.xNome.xml     = arquivo
            self.xFant.xml     = arquivo
            self.fone.xml      = arquivo
            self.enderToma.xml = arquivo
            self.email.xml     = arquivo

            if self._le_noh('//CTe/infCte/ide/toma03/toma') is not None:
                self.toma03.xml = arquivo
                self.toma.valor = self.toma03.valor
            else:
                self.toma4.xml = arquivo
                self.toma.valor = self.toma4.valor

    xml = property(get_xml, set_xml)


class Ide(XMLNFe):
    def __init__(self):
        super(Ide, self).__init__()
        self.cUF     = TagInteiro(nome='cUF'     , codigo='B02', tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide')
        self.cCT     = TagCaracter(nome='cCT'    , codigo='B03', tamanho=[ 8,  8, 8], raiz='//CTe/infCte/ide')
        self.CFOP    = TagInteiro(nome='CFOP'    , codigo='I08', tamanho=[4,   4, 4], raiz='//CTe/infCte/ide')
        self.natOp   = TagCaracter(nome='natOp'  , codigo='B04', tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide')
        self.forPag  = TagInteiro(nome='forPag'  , codigo='B05', tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=1)
        self.mod     = TagInteiro(nome='mod'     , codigo='B06', tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide', valor=57)
        self.serie   = TagInteiro(nome='serie'   , codigo='B07', tamanho=[ 1,  3, 1], raiz='//CTe/infCte/ide')
        self.nCT     = TagInteiro(nome='nCT'     , codigo='B08', tamanho=[ 1,  9, 1], raiz='//CTe/infCte/ide')
        self.dhEmi   = TagDataHora(nome='dhEmi'  , codigo='B09',                      raiz='//CTe/infCte/ide')
        self.tpImp   = TagInteiro(nome='tpImp'   , codigo='B21', tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=1)
        self.tpEmis  = TagInteiro(nome='tpEmis'  , codigo='B22', tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=1)
        self.cDV     = TagInteiro(nome='cDV'     , codigo='B23', tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide')
        self.tpAmb   = TagInteiro(nome='tpAmb'   , codigo='B24', tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=2)
        self.tpCTe   = TagInteiro(nome='tpCTe'   , codigo='B11', tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=1)
        self.procEmi = TagInteiro(nome='procEmi' , codigo='B26', tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide')
        self.verProc = TagCaracter(nome='verProc', codigo='B27', tamanho=[ 1, 20]   , raiz='//CTe/infCte/ide')
        self.refCTE  = TagCaracter(nome='refCTE' , codigo='B13', tamanho=[44, 44]   , raiz='//CTe/infCte/ide', obrigatorio=False)
        self.cMunEnv = TagInteiro(nome='cMunEnv' , codigo='B12', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/ide')
        self.xMunEnv = TagCaracter(nome='xMunEnv', codigo='B12', tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide')
        self.UFEnv   = TagCaracter(nome='UFEnv'  , codigo='B12', tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide')
        self.modal   = TagCaracter(nome='modal'  , codigo='B12', tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide', default='01')
        self.tpServ  = TagInteiro(nome='tpServ'  , codigo='B11', tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=0)
        self.cMunIni = TagInteiro(nome='cMunIni' , codigo='B12', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/ide')
        self.xMunIni = TagCaracter(nome='xMunIni', codigo='B12', tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide')
        self.UFIni   = TagCaracter(nome='UFIni'  , codigo='B12', tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide')
        self.cMunFim = TagInteiro(nome='cMunFim' , codigo='B12', tamanho=[ 7,  7, 7], raiz='//CTe/infCte/ide')
        self.xMunFim = TagCaracter(nome='xMunFim', codigo='B12', tamanho=[ 1, 60]   , raiz='//CTe/infCte/ide')
        self.UFFim   = TagCaracter(nome='UFFim'  , codigo='B12', tamanho=[ 2,  2, 2], raiz='//CTe/infCte/ide')
        self.retira  = TagInteiro(nome='retira'  , codigo='B11', tamanho=[ 1,  1, 1], raiz='//CTe/infCte/ide', valor=0)
        self.xDetRetira  = TagCaracter(nome='xDetRetira', codigo='B11', tamanho=[ 1, 160], raiz='//CTe/infCte/ide', obrigatorio=False)
        self.tomador  = Tomador()
        self.dhCont   = TagDataHora(nome='dhCont', codigo='B28',                      raiz='//CTe/infCte/ide', obrigatorio=False)
        self.xJust    = TagCaracter(nome='xJust' , codigo='B29',                      raiz='//CTe/infCte/ide', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ide>'
        xml += self.cUF.xml
        xml += self.cCT.xml
        xml += self.CFOP.xml
        xml += self.natOp.xml
        xml += self.forPag.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nCT.xml
        xml += self.dhEmi.xml
        xml += self.tpImp.xml
        xml += self.tpEmis.xml
        xml += self.cDV.xml
        xml += self.tpAmb.xml
        xml += self.tpCTe.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += self.refCTE.xml
        xml += self.cMunEnv.xml
        xml += self.xMunEnv.xml
        xml += self.UFEnv.xml
        xml += self.modal.xml
        xml += self.tpServ.xml
        xml += self.cMunIni.xml
        xml += self.xMunIni.xml
        xml += self.UFIni.xml
        xml += self.cMunFim.xml
        xml += self.xMunFim.xml
        xml += self.UFFim.xml
        xml += self.retira.xml
        xml += self.xDetRetira.xml
        xml += self.tomador.xml
        xml += self.dhCont.xml
        xml += self.xJust.xml

        xml += '</ide>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml     = arquivo
            self.cCT.xml     = arquivo
            self.CFOP.xml     = arquivo
            self.natOp.xml   = arquivo
            self.forPag.xml  = arquivo
            self.mod.xml     = arquivo
            self.serie.xml   = arquivo
            self.nCT.xml     = arquivo
            self.dhEmi.xml    = arquivo
            self.tpImp.xml   = arquivo
            self.tpEmis.xml  = arquivo
            self.cDV.xml     = arquivo
            self.tpAmb.xml   = arquivo
            self.tpCTe.xml   = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo
            self.refCTE.xml  = arquivo
            self.cMunEnv.xml = arquivo
            self.xMunEnv.xml = arquivo
            self.UFEnv.xml   = arquivo
            self.modal.xml   = arquivo
            self.tpServ.xml  = arquivo
            self.cMunIni.xml = arquivo
            self.xMunIni.xml = arquivo
            self.UFIni.xml   = arquivo
            self.cMunFim.xml = arquivo
            self.xMunFim.xml = arquivo
            self.UFFim.xml   = arquivo
            self.retira.xml  = arquivo
            self.xDetRetira.xml = arquivo
            self.tomador.xml   = arquivo
            self.dhCont.xml  = arquivo
            self.xJust.xml   = arquivo

    xml = property(get_xml, set_xml)


class InfCTe(XMLNFe):
    def __init__(self):
        super(InfCTe, self).__init__()
        self.versao   = TagDecimal(nome='infCte' , codigo='A01', propriedade='versao', raiz='//CTe', namespace=NAMESPACE_CTE, valor='1.04')
        self.Id       = TagCaracter(nome='infCte', codigo='A03', propriedade='Id'    , raiz='//CTe', namespace=NAMESPACE_CTE)
        self.ide      = Ide()
        self.compl    = Compl()
        self.emit     = Emit()
        self.rem      = Rem()
        self.exped    = Exped()
        self.receb    = Receb()
        self.dest     = Dest()
        self.vPrest   = VPrest()
        self.imp      = Imp()
        self.infCTeNorm = InfCTeNorm()
        #self.det      = []
        #self.total    = Total()
        #self.transp   = Transp()
        #self.cobr     = Cobr()
        #self.infAdic  = InfAdic()
        #self.exporta  = Exporta()
        #self.compra   = Compra()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCte versao="' + unicode(self.versao.valor) + '" Id="' + self.Id.valor + '">'
        xml += self.ide.xml
        xml += self.compl.xml
        xml += self.emit.xml
        xml += self.rem.xml
        xml += self.exped.xml
        xml += self.receb.xml
        xml += self.dest.xml
        xml += self.vPrest.xml
        xml += self.imp.xml
        xml += self.infCTeNorm.xml

        #for d in self.det:
            #xml += d.xml

        #xml += self.total.xml
        #xml += self.transp.xml
        #xml += self.cobr.xml
        #xml += self.infAdic.xml
        #xml += self.exporta.xml
        #xml += self.compra.xml
        xml += '</infCte>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.Id.xml       = arquivo
            self.ide.xml      = arquivo
            self.compl.xml    = arquivo
            self.emit.xml     = arquivo
            self.rem.xml      = arquivo
            self.exped.xml    = arquivo
            self.receb.xml    = arquivo
            self.dest.xml     = arquivo
            self.vPrest.xml   = arquivo
            self.imp.xml      = arquivo
            self.infCTeNorm.xml = arquivo

            if self.ide.tomador.toma.valor != 4:
                if self.ide.tomador.toma.valor == 0:
                    tomador = self.rem
                    endertoma = self.rem.enderReme
                elif self.ide.tomador.toma.valor == 1:
                    tomador = self.exped
                    endertoma = self.exped.enderExped
                elif self.ide.tomador.toma.valor == 2:
                    tomador = self.receb
                    endertoma = self.receb.enderReceb
                elif self.ide.tomador.toma.valor == 3:
                    tomador = self.dest
                    endertoma = self.dest.enderDest

                self.ide.tomador.CNPJ.valor = tomador.CNPJ.valor
                self.ide.tomador.CPF.valor = tomador.CPF.valor
                self.ide.tomador.IE.valor = tomador.IE.valor
                self.ide.tomador.xNome.valor = tomador.xNome.valor

                try:
                    self.ide.tomador.xFant.valor = tomador.xFant.valor4
                except:
                    pass

                self.ide.tomador.fone.valor = tomador.fone.valor
                self.ide.tomador.email.valor = tomador.email.valor
                self.ide.tomador.enderToma.xLgr.valor = endertoma.xLgr.valor
                self.ide.tomador.enderToma.nro.valor = endertoma.nro.valor
                self.ide.tomador.enderToma.xCpl.valor = endertoma.xCpl.valor
                self.ide.tomador.enderToma.xBairro.valor = endertoma.xBairro.valor
                self.ide.tomador.enderToma.cMun.valor = endertoma.cMun.valor
                self.ide.tomador.enderToma.xMun.valor = endertoma.xMun.valor
                self.ide.tomador.enderToma.CEP.valor = endertoma.CEP.valor
                self.ide.tomador.enderToma.UF.valor = endertoma.UF.valor
                self.ide.tomador.enderToma.cPais.valor = endertoma.cPais.valor
                self.ide.tomador.enderToma.xPais.valor = endertoma.xPais.valor

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            #self.det = self.le_grupo('//CTe/infCte/det', Det)

            #self.total.xml    = arquivo
            #self.transp.xml   = arquivo
            #self.cobr.xml     = arquivo
            #self.infAdic.xml  = arquivo
            #self.exporta.xml  = arquivo
            #self.compra.xml   = arquivo

    xml = property(get_xml, set_xml)


class CTe(XMLNFe):
    def __init__(self):
        super(CTe, self).__init__()
        self.infCte = InfCTe()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'cte_v1.04.xsd'
        self.chave = ''
        self.dados_contingencia_fsda = ''
        self.site = ''
        self.email = ''
        self.infCTe = self.infCte

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<CTe xmlns="http://www.portalfiscal.inf.br/cte">'
        xml += self.infCte.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.infCte.Id.valor

        xml += self.Signature.xml
        xml += '</CTe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infCte.xml    = arquivo
            self.Signature.xml = self._le_noh('//CTe/sig:Signature')

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = self.infCte.txt
        return txt

    txt = property(get_txt)

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
        chave = unicode(self.infCte.ide.cUF.valor).zfill(2)
        chave += unicode(self.infCte.ide.dhEmi.valor.strftime('%y%m')).zfill(4)
        chave += unicode(self.infCte.emit.CNPJ.valor).zfill(14)
        chave += unicode(self.infCte.ide.mod.valor).zfill(2)
        chave += unicode(self.infCte.ide.serie.valor).zfill(3)
        chave += unicode(self.infCte.ide.nCT.valor).zfill(9)
        chave += unicode(self.infCte.ide.tpEmis.valor).zfill(1)

        #
        # O código numério é um número aleatório
        #
        #chave += unicode(random.randint(0, 99999999)).strip().rjust(8, '0')

        #
        # Mas, por segurança, é preferível que esse número não seja aleatório de todo
        #
        soma = 0
        for c in chave:
            soma += int(c) ** 3 ** 2

        codigo = unicode(soma)
        if len(codigo) > 8:
            codigo = codigo[-8:]
        else:
            codigo = codigo.rjust(8, '0')

        chave += codigo

        #
        # Define na estrutura do XML o campo cCT
        #
        #self.infCte.ide.cCT.valor = unicode(self.infCte.ide.tpEmis.valor).zfill(1) + codigo
        self.infCte.ide.cCT.valor = chave[-8:]

        #
        # Gera o dígito verificador
        #
        digito = self._calcula_dv(chave)

        #
        # Define na estrutura do XML o campo cDV
        #
        self.infCte.ide.cDV.valor = digito

        chave += unicode(digito)
        self.chave = chave

        #
        # Define o Id
        #
        self.infCte.Id.valor = 'CTe' + chave

    def monta_chave(self):
        chave = unicode(self.infCte.ide.cUF.valor).zfill(2)
        chave += unicode(self.infCte.ide.dEmi.valor.strftime('%y%m')).zfill(4)
        chave += unicode(self.infCte.emit.CNPJ.valor).zfill(14)
        chave += unicode(self.infCte.ide.mod.valor).zfill(2)
        chave += unicode(self.infCte.ide.serie.valor).zfill(3)
        chave += unicode(self.infCte.ide.nCT.valor).zfill(9)
        chave += unicode(self.infCte.ide.cCT.valor).zfill(9)
        chave += unicode(self.infCte.ide.cDV.valor).zfill(1)
        self.chave = chave

    def chave_para_codigo_barras(self):
        #
        # As funções do reportlabs para geração de códigos de barras não estão
        # aceitando strings unicode
        #
        return self.chave.encode('utf-8')

    def monta_dados_contingencia_fsda(self):
        dados = unicode(self.infCte.ide.cUF.valor).zfill(2)
        dados += unicode(self.infCte.ide.tpEmis.valor).zfill(1)
        dados += unicode(self.infCte.emit.CNPJ.valor).zfill(14)
        dados += unicode(int(self.infCte.total.ICMSTot.vNF.valor * 100)).zfill(14)

        #
        # Há ICMS próprio?
        #
        if self.infCte.total.ICMSTot.vICMS.valor:
            dados += '1'
        else:
            dados += '2'

        #
        # Há ICMS ST?
        #
        if self.infCte.total.ICMSTot.vST.valor:
            dados += '1'
        else:
            dados += '2'

        dados += self.infCte.ide.dEmi.valor.strftime('%d').zfill(2)

        digito = self._calcula_dv(dados)
        dados += unicode(digito)
        self.dados_contingencia_fsda = dados

    def dados_contingencia_fsda_para_codigo_barras(self):
        #
        # As funções do reportlabs para geração de códigos de barras não estão
        # aceitando strings unicode
        #
        self.monta_dados_contingencia_fsda()
        return self.dados_contingencia_fsda.encode('utf-8')

    #
    # Funções para formatar campos para o DANFE
    #

    def chave_formatada(self):
        chave = self.chave
        chave_formatada = ' '.join((chave[0:4], chave[4:8], chave[8:12], chave[12:16], chave[16:20], chave[20:24], chave[24:28], chave[28:32], chave[32:36], chave[36:40], chave[40:44]))
        return chave_formatada

    def dados_contingencia_fsda_formatados(self):
        self.monta_dados_contingencia_fsda()
        dados = self.dados_contingencia_fsda
        dados_formatados = ' '.join((dados[0:4], dados[4:8], dados[8:12], dados[12:16], dados[16:20], dados[20:24], dados[24:28], dados[28:32], dados[32:36]))
        return dados_formatados

    def numero_formatado(self):
        num = unicode(self.infCte.ide.nCT.valor).zfill(9)
        num_formatado = '.'.join((num[0:3], num[3:6], num[6:9]))
        return 'Nº ' + num_formatado

    def serie_formatada(self):
        return 'SÉRIE ' + unicode(self.infCte.ide.serie.valor).zfill(3)


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

    def cnpj_emitente_formatado(self):
        if len(self.infCte.emit.CPF.valor):
            return self._formata_cpf(unicode(self.infCte.emit.CPF.valor))
        else:
            return self._formata_cnpj(unicode(self.infCte.emit.CNPJ.valor))

    def endereco_emitente_formatado(self):
        formatado = self.infCte.emit.enderEmit.xLgr.valor
        formatado += ', ' + self.infCte.emit.enderEmit.nro.valor

        if len(self.infCte.emit.enderEmit.xCpl.valor.strip()):
            formatado += ' - ' + self.infCte.emit.enderEmit.xCpl.valor

        return formatado

    def _formata_cep(self, cep):
        if not len(cep.strip()):
            return ''

        return cep[0:5] + '-' + cep[5:8]

    def cep_emitente_formatado(self):
        return self._formata_cep(self.infCte.emit.enderEmit.CEP.valor)

    def endereco_emitente_formatado_linha_1(self):
        formatado = self.endereco_emitente_formatado()
        formatado += ' - ' + self.infCte.emit.enderEmit.xBairro.valor
        return formatado

    def endereco_emitente_formatado_linha_2(self):
        formatado = self.infCte.emit.enderEmit.xMun.valor
        formatado += ' - ' + self.infCte.emit.enderEmit.UF.valor
        formatado += ' - ' + self.cep_emitente_formatado()
        return formatado

    def endereco_emitente_formatado_linha_3(self):
        if self.fone_emitente_formatado().strip() != '':
            formatado = 'Fone: ' + self.fone_emitente_formatado()
        else:
            formatado = ''
        return formatado

    def endereco_emitente_formatado_linha_4(self):
        return self.site

    def _formata_fone(self, fone):
        if not len(fone.strip()):
            return ''

        if fone.strip() == '0':
            return ''

        if len(fone) <= 8:
            formatado = fone[:-4] + '-' + fone[-4:]
        elif len(fone) <= 10:
            ddd = fone[0:2]
            fone = fone[2:]
            formatado = '(' + ddd + ') ' + fone[:-4] + '-' + fone[-4:]

        #
        # Celulares de SP agora têm 9 dígitos...
        #
        elif len(fone) <= 11:
            ddd = fone[0:3]
            fone = fone[3:]
            formatado = '(' + ddd + ') ' + fone[:-4] + '-' + fone[-4:]

        #
        # Assume 8 dígitos para o número, 2 para o DD, e o restante é o DDI
        #
        else:
            numero = fone[len(fone)-8:]
            ddd = fone[len(fone)-10:len(fone)-8]
            ddi = fone[:len(fone)-10]
            formatado = '+' + ddi + ' (' + ddd + ') ' + numero[:-4] + '-' + numero[-4:]

        return formatado

    def fone_emitente_formatado(self):
        return self._formata_fone(unicode(self.infCte.emit.enderEmit.fone.valor))

    def cnpj_destinatario_formatado(self):
        if self.infCte.dest.CPF.valor and len(self.infCte.dest.CPF.valor):
            return self._formata_cpf(unicode(self.infCte.dest.CPF.valor))
        elif self.infCte.dest.CNPJ.valor and len(self.infCte.dest.CNPJ.valor):
            return self._formata_cnpj(unicode(self.infCte.dest.CNPJ.valor))
        else:
            return ''

    def endereco_destinatario_formatado(self):
        formatado = self.infCte.dest.enderDest.xLgr.valor
        formatado += ', ' + self.infCte.dest.enderDest.nro.valor

        if len(self.infCte.dest.enderDest.xCpl.valor.strip()):
            formatado += ' - ' + self.infCte.dest.enderDest.xCpl.valor

        return formatado

    def cep_destinatario_formatado(self):
        return self._formata_cep(self.infCte.dest.enderDest.CEP.valor)

    def fone_destinatario_formatado(self):
        return self._formata_fone(unicode(self.infCte.dest.enderDest.fone.valor))

    def cnpj_retirada_formatado(self):
        return self._formata_cnpj(self.infCte.retirada.CNPJ.valor)

    def endereco_retirada_formatado(self):
        formatado = self.infCte.retirada.xLgr.valor
        formatado += ', ' + self.infCte.retirada.nro.valor

        if len(self.infCte.retirada.xCpl.valor.strip()):
            formatado += ' - ' + self.infCte.retirada.xCpl.valor

        formatado += ' - ' + self.infCte.retirada.xBairro.valor
        formatado += ' - ' + self.infCte.retirada.xMun.valor
        formatado += '-' + self.infCte.retirada.UF.valor
        return formatado

    def cnpj_entrega_formatado(self):
        return self._formata_cnpj(self.infCte.entrega.CNPJ.valor)

    def endereco_entrega_formatado(self):
        formatado = self.infCte.entrega.xLgr.valor
        formatado += ', ' + self.infCte.entrega.nro.valor

        if len(self.infCte.entrega.xCpl.valor.strip()):
            formatado += ' - ' + self.infCte.entrega.xCpl.valor

        formatado += ' - ' + self.infCte.entrega.xBairro.valor
        formatado += ' - ' + self.infCte.entrega.xMun.valor
        formatado += '-' + self.infCte.entrega.UF.valor
        return formatado

    def cnpj_transportadora_formatado(self):
        if self.infCte.transp.transporta.CPF.valor:
            return self._formata_cpf(self.infCte.transp.transporta.CPF.valor)
        else:
            return self._formata_cnpj(self.infCte.transp.transporta.CNPJ.valor)

    def placa_veiculo_formatada(self):
        if not self.infCte.transp.veicTransp.placa.valor:
            return ''

        placa = self.infCte.transp.veicTransp.placa.valor
        placa = placa[:-4] + '-' + placa[-4:]
        return placa

    def dados_adicionais(self):
        da = ''

        if self.infCte.infAdic.infAdFisco.valor:
            da = self.infCte.infAdic.infAdFisco.valor.replace('|', '<br />')

        if self.infCte.infAdic.infCpl.valor:
            if len(da) > 0:
                da += '<br />'

            da += self.infCte.infAdic.infCpl.valor.replace('|', '<br />')

        return da

    def canhoto_formatado(self):
        formatado = 'RECEBEMOS DE <b>'
        formatado += self.infCte.emit.xNome.valor.upper()
        formatado += '</b> OS PRODUTOS E/OU SERVIÇOS CONSTANTES DA <b>NOTA FISCAL ELETRÔNICA</b> INDICADA AO LADO'
        return formatado

    def frete_formatado(self):
        if self.infCte.transp.modFrete.valor == 0:
            formatado = '0-EMITENTE'

        elif self.infCte.transp.modFrete.valor == 1:
            if self.infCte.ide.tpCT.valor == 0:
                formatado = '1-REMETENTE'
            else:
                formatado = '1-DESTINATÁRIO'

        elif self.infCte.transp.modFrete.valor == 2:
            formatado = '2-DE TERCEIROS'

        elif self.infCte.transp.modFrete.valor == 9:
            formatado = '9-SEM FRETE'

        else:
            formatado = ''

        return formatado

    def cst_descricao(self):
        return 'CST'

    def crt_descricao(self):
        return ''
