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
                             TagData, TagDecimal, TagHora, TagInteiro, XMLNFe)
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_1 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


class ISSQN(XMLNFe):
    def __init__(self):
        super(ISSQN, self).__init__()
        self.vBC       = TagDecimal(nome='vBC'      , codigo='U02', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/ISSQN')
        self.vAliq     = TagDecimal(nome='vAliq'    , codigo='U03', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='//det/imposto/ISSQN')
        self.vISSQN    = TagDecimal(nome='vISSQN'   , codigo='U04', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/ISSQN')
        self.cMunFG    = TagInteiro(nome='cMunFG'   , codigo='U05', tamanho=[7,  7, 7],                     raiz='//det/imposto/ISSQN')
        self.cListServ = TagInteiro(nome='cListServ', codigo='U06', tamanho=[3,  4]   ,                     raiz='//det/imposto/ISSQN')

    def get_xml(self):
        if not (self.vBC.valor or self.vAliq.valor or self.vISSQN.valor or self.cMunFG.valor or self.cListServ.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ISSQN>'
        xml += self.vBC.xml
        xml += self.vAliq.xml
        xml += self.vISSQN.xml
        xml += self.cMunFG.xml
        xml += self.cListServ.xml
        xml += '</ISSQN>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml       = arquivo
            self.vAliq.xml     = arquivo
            self.vISSQN.xml    = arquivo
            self.cMunFG.xml    = arquivo
            self.cListServ.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.vBC.valor or self.vAliq.valor or self.vISSQN.valor or self.cMunFG.valor or self.cListServ.valor):
            return ''

        txt = 'U|'
        txt += self.vBC.txt + '|'
        txt += self.vAliq.txt + '|'
        txt += self.vISSQN.txt + '|'
        txt += self.cMunFG.txt + '|'
        txt += self.cListServ.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class COFINSST(XMLNFe):
    def __init__(self):
        super(COFINSST, self).__init__()
        self.vBC       = TagDecimal(nome='vBC'      , codigo='T02', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/COFINS/COFINSST')
        self.pCOFINS   = TagDecimal(nome='pCOFINS'  , codigo='T03', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='//det/imposto/COFINS/COFINSST')
        self.qBCProd   = TagDecimal(nome='qBCProd'  , codigo='T04', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz='//det/imposto/COFINS/COFINSST')
        self.vAliqProd = TagDecimal(nome='vAliqProd', codigo='T05', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz='//det/imposto/COFINS/COFINSST')
        self.vCOFINS   = TagDecimal(nome='vCOFINS'  , codigo='T06', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/COFINS/COFINSST')

    def get_xml(self):
        if not (self.vBC.valor or self.pCOFINS.valor or self.qBCProd.valor or self.vAliqProd.valor or self.vCOFINS.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<COFINSST>'

        if self.qBCProd.valor or self.vAliqProd.valor:
            xml += self.qBCProd.xml
            xml += self.vAliqProd.xml
        else:
            xml += self.vBC.xml
            xml += self.pCOFINS.xml

        xml += self.vCOFINS.xml
        xml += '</COFINSST>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml       = arquivo
            self.pCOFINS.xml   = arquivo
            self.qBCProd.xml   = arquivo
            self.vAliqProd.xml = arquivo
            self.vCOFINS.xml   = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.vBC.valor or self.pCOFINS.valor or self.qBCProd.valor or self.vAliqProd.valor or self.vCOFINS.valor):
            return ''

        txt = 'T|'
        txt += self.pCOFINS.txt + '|'
        txt += '\n'

        if self.qBCProd.valor or self.vAliqProd.valor:
            txt += 'T02|'
            txt += self.qBCProd.txt + '|'
            txt += self.vAliqProd.txt + '|'
        else:
            txt += 'T04|'
            txt += self.vBC.txt + '|'
            txt += self.pCOFINS.txt + '|'

        txt += '\n'

        return txt

    txt = property(get_txt)



class TagCSTCOFINS(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagCSTCOFINS, self).__init__(*args, **kwargs)
        self.nome = 'CST'
        self.codigo = 'S06'
        self.tamanho = [2, 2]
        self.raiz = ''
        self.grupo_cofins = None

    def set_valor(self, novo_valor):
        super(TagCSTCOFINS, self).set_valor(novo_valor)

        if not self.grupo_cofins:
            return None

        #
        # Definimos todas as tags como não obrigatórias
        #
        self.grupo_cofins.vBC.obrigatorio       = False
        self.grupo_cofins.pCOFINS.obrigatorio   = False
        self.grupo_cofins.vCOFINS.obrigatorio   = False
        self.grupo_cofins.qBCProd.obrigatorio   = False
        self.grupo_cofins.vAliqProd.obrigatorio = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo COFINS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_cofins.vBC.valor       = '0.00'
        self.grupo_cofins.pCOFINS.valor   = '0.00'
        self.grupo_cofins.vCOFINS.valor   = '0.00'
        self.grupo_cofins.qBCProd.valor   = '0.00'
        self.grupo_cofins.vAliqProd.valor = '0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de COFINS
        #
        if self.valor in ('01', '02'):
            self.grupo_cofins.nome_tag = 'COFINSAliq'
            self.grupo_cofins.nome_tag_txt = 'S02'
            self.grupo_cofins.raiz_tag = '//det/imposto/COFINS/COFINSAliq'
            self.grupo_cofins.vBC.obrigatorio       = True
            self.grupo_cofins.pCOFINS.obrigatorio   = True
            self.grupo_cofins.vCOFINS.obrigatorio   = True
            #self.grupo_cofins.qBCProd.obrigatorio   = True
            #self.grupo_cofins.vAliqProd.obrigatorio = True

        elif self.valor == '03':
            self.grupo_cofins.nome_tag = 'COFINSQtde'
            self.grupo_cofins.nome_tag_txt = 'S03'
            self.grupo_cofins.raiz_tag = '//det/imposto/COFINS/COFINSQtde'
            #self.grupo_cofins.vBC.obrigatorio       = True
            #self.grupo_cofins.pCOFINS.obrigatorio   = True
            self.grupo_cofins.vCOFINS.obrigatorio   = True
            self.grupo_cofins.qBCProd.obrigatorio   = True
            self.grupo_cofins.vAliqProd.obrigatorio = True

        elif self.valor in ('04', '06', '07', '08', '09'):
            self.grupo_cofins.nome_tag = 'COFINSNT'
            self.grupo_cofins.nome_tag_txt = 'S04'
            self.grupo_cofins.raiz_tag = '//det/imposto/COFINS/COFINSNT'
            #self.grupo_cofins.vBC.obrigatorio       = True
            #self.grupo_cofins.pCOFINS.obrigatorio   = True
            #self.grupo_cofins.vCOFINS.obrigatorio   = True
            #self.grupo_cofins.qBCProd.obrigatorio   = True
            #self.grupo_cofins.vAliqProd.obrigatorio = True

        else:
            self.grupo_cofins.nome_tag = 'COFINSOutr'
            self.grupo_cofins.nome_tag_txt = 'S05'
            self.grupo_cofins.raiz_tag = '//det/imposto/COFINS/COFINSOutr'
            self.grupo_cofins.vBC.obrigatorio       = True
            self.grupo_cofins.pCOFINS.obrigatorio   = True
            self.grupo_cofins.vCOFINS.obrigatorio   = True
            self.grupo_cofins.qBCProd.obrigatorio   = True
            self.grupo_cofins.vAliqProd.obrigatorio = True


        #
        # Redefine a raiz para todas as tags do grupo COFINS
        #
        self.grupo_cofins.CST.raiz       = self.grupo_cofins.raiz_tag
        self.grupo_cofins.vBC.raiz       = self.grupo_cofins.raiz_tag
        self.grupo_cofins.pCOFINS.raiz   = self.grupo_cofins.raiz_tag
        self.grupo_cofins.vCOFINS.raiz   = self.grupo_cofins.raiz_tag
        self.grupo_cofins.qBCProd.raiz   = self.grupo_cofins.raiz_tag
        self.grupo_cofins.vAliqProd.raiz = self.grupo_cofins.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class COFINS(XMLNFe):
    def __init__(self):
        super(COFINS, self).__init__()
        self.vBC       = TagDecimal(nome='vBC'      , codigo='S07', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.pCOFINS   = TagDecimal(nome='pCOFINS'  , codigo='S08', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vCOFINS   = TagDecimal(nome='vCOFINS'  , codigo='S11', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.qBCProd   = TagDecimal(nome='qBCProd'  , codigo='S09', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz='')
        self.vAliqProd = TagDecimal(nome='vAliqProd', codigo='S10', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz='')

        self.CST      = TagCSTCOFINS()
        self.CST.grupo_cofins = self
        self.CST.valor = '07'
        self.nome_tag = 'COFINSNT'
        self.nome_tag_txt = 'S04'
        self.raiz_tag = '//det/imposto/COFINS/COFINSNT'

    def get_xml(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += '<COFINS>'
        xml += '<' + self.nome_tag + '>'
        xml += self.CST.xml

        if self.CST.valor in ('01', '02'):
            xml += self.vBC.xml
            xml += self.pCOFINS.xml
            xml += self.vCOFINS.xml

        elif self.CST.valor == '03':
            xml += self.qBCProd.xml
            xml += self.vAliqProd.xml
            xml += self.vCOFINS.xml

        elif self.CST.valor in ('04', '06', '07', '08', '09'):
            pass

        else:
            if self.qBCProd.valor or self.vAliqProd.valor:
                xml += self.qBCProd.xml
                xml += self.vAliqProd.xml
            else:
                xml += self.vBC.xml
                xml += self.pCOFINS.xml
            xml += self.vCOFINS.xml

        xml += '</' + self.nome_tag + '></COFINS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o COFINS, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            if self._le_noh('//det/imposto/COFINS/COFINSAliq') is not None:
                self.CST.valor = '01'
            elif self._le_noh('//det/imposto/COFINS/COFINSQtde') is not None:
                self.CST.valor = '03'
            elif self._le_noh('//det/imposto/COFINS/COFINSNT') is not None:
                self.CST.valor = '04'
            else:
                self.CST.valor = '99'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            self.CST.xml       = arquivo
            self.vBC.xml       = arquivo
            self.pCOFINS.xml   = arquivo
            self.vCOFINS.xml   = arquivo
            self.qBCProd.xml   = arquivo
            self.vAliqProd.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'S|\n'

        #
        # Define as tags baseado no código da situação tributária
        #
        txt += self.nome_tag_txt + '|'
        txt += self.CST.txt + '|'

        if self.CST.valor in ('01', '02'):
            txt += self.vBC.txt + '|'
            txt += self.pCOFINS.txt + '|'
            txt += self.vCOFINS.txt + '|'
            txt += '\n'

        elif self.CST.valor == '03':
            txt += self.qBCProd.txt + '|'
            txt += self.vAliqProd.txt + '|'
            txt += self.vCOFINS.txt + '|'
            txt += '\n'

        elif self.CST.valor in ('04', '06', '07', '08', '09'):
            txt += '\n'

        else:
            txt += self.vCOFINS.txt + '|'
            txt += '\n'

            if self.qBCProd.valor or self.vAliqProd.valor:
                txt += 'S09|'
                txt += self.qBCProd.txt + '|'
                txt += self.vAliqProd.txt + '|'
            else:
                txt += 'S07|'
                txt += self.vBC.txt + '|'
                txt += self.pCOFINS.txt + '|'

            txt += '\n'

        return txt

    txt = property(get_txt)


class PISST(XMLNFe):
    def __init__(self):
        super(PISST, self).__init__()
        self.vBC       = TagDecimal(nome='vBC'      , codigo='R02', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/PIS/PISST')
        self.pPIS      = TagDecimal(nome='pPIS'     , codigo='R03', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='//det/imposto/PIS/PISST')
        self.qBCProd   = TagDecimal(nome='qBCProd'  , codigo='R04', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz='//det/imposto/PIS/PISST')
        self.vAliqProd = TagDecimal(nome='vAliqProd', codigo='R05', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz='//det/imposto/PIS/PISST')
        self.vPIS      = TagDecimal(nome='vPIS'     , codigo='R06', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/PIS/PISST')

    def get_xml(self):
        if not (self.vBC.valor or self.pPIS.valor or self.qBCProd.valor or self.vAliqProd.valor or self.vPIS.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<PISST>'

        if self.qBCProd.valor or self.vAliqProd.valor:
            xml += self.qBCProd.xml
            xml += self.vAliqProd.xml
        else:
            xml += self.vBC.xml
            xml += self.pPIS.xml

        xml += self.vPIS.xml
        xml += '</PISST>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml       = arquivo
            self.pPIS.xml      = arquivo
            self.qBCProd.xml   = arquivo
            self.vAliqProd.xml = arquivo
            self.vPIS.xml      = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.vBC.valor or self.pPIS.valor or self.qBCProd.valor or self.vAliqProd.valor or self.vPIS.valor):
            return ''

        txt = 'R|'
        txt += self.pPIS.txt + '|'
        txt += '\n'

        if self.qBCProd.valor or self.vAliqProd.valor:
            txt += 'R02|'
            txt += self.qBCProd.txt + '|'
            txt += self.vAliqProd.txt + '|'
        else:
            txt += 'R04|'
            txt += self.vBC.txt + '|'
            txt += self.pPIS.txt + '|'

        txt += '\n'

        return txt

    txt = property(get_txt)


class TagCSTPIS(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagCSTPIS, self).__init__(*args, **kwargs)
        self.nome = 'CST'
        self.codigo = 'Q06'
        self.tamanho = [2, 2]
        self.raiz = ''
        self.grupo_pis = None

    def set_valor(self, novo_valor):
        super(TagCSTPIS, self).set_valor(novo_valor)

        if not self.grupo_pis:
            return None

        #
        # Definimos todas as tags como não obrigatórias
        #
        self.grupo_pis.vBC.obrigatorio       = False
        self.grupo_pis.pPIS.obrigatorio      = False
        self.grupo_pis.vPIS.obrigatorio      = False
        self.grupo_pis.qBCProd.obrigatorio   = False
        self.grupo_pis.vAliqProd.obrigatorio = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo PIS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_pis.vBC.valor       = '0.00'
        self.grupo_pis.pPIS.valor      = '0.00'
        self.grupo_pis.vPIS.valor      = '0.00'
        self.grupo_pis.qBCProd.valor   = '0.00'
        self.grupo_pis.vAliqProd.valor = '0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de PIS
        #
        if self.valor in ('01', '02'):
            self.grupo_pis.nome_tag = 'PISAliq'
            self.grupo_pis.nome_tag_txt = 'Q02'
            self.grupo_pis.raiz_tag = '//det/imposto/PIS/PISAliq'
            self.grupo_pis.vBC.obrigatorio       = True
            self.grupo_pis.pPIS.obrigatorio      = True
            self.grupo_pis.vPIS.obrigatorio      = True
            #self.grupo_pis.qBCProd.obrigatorio   = True
            #self.grupo_pis.vAliqProd.obrigatorio = True

        elif self.valor == '03':
            self.grupo_pis.nome_tag = 'PISQtde'
            self.grupo_pis.nome_tag_txt = 'Q03'
            self.grupo_pis.raiz_tag = '//det/imposto/PIS/PISQtde'
            #self.grupo_pis.vBC.obrigatorio       = True
            #self.grupo_pis.pPIS.obrigatorio      = True
            self.grupo_pis.vPIS.obrigatorio      = True
            self.grupo_pis.qBCProd.obrigatorio   = True
            self.grupo_pis.vAliqProd.obrigatorio = True

        elif self.valor in ('04', '06', '07', '08', '09'):
            self.grupo_pis.nome_tag = 'PISNT'
            self.grupo_pis.nome_tag_txt = 'Q04'
            self.grupo_pis.raiz_tag = '//det/imposto/PIS/PISNT'
            #self.grupo_pis.vBC.obrigatorio       = True
            #self.grupo_pis.pPIS.obrigatorio      = True
            #self.grupo_pis.vPIS.obrigatorio      = True
            #self.grupo_pis.qBCProd.obrigatorio   = True
            #self.grupo_pis.vAliqProd.obrigatorio = True

        else:
            self.grupo_pis.nome_tag = 'PISOutr'
            self.grupo_pis.nome_tag_txt = 'Q05'
            self.grupo_pis.raiz_tag = '//det/imposto/PIS/PISOutr'
            self.grupo_pis.vBC.obrigatorio       = True
            self.grupo_pis.pPIS.obrigatorio      = True
            self.grupo_pis.vPIS.obrigatorio      = True
            self.grupo_pis.qBCProd.obrigatorio   = True
            self.grupo_pis.vAliqProd.obrigatorio = True


        #
        # Redefine a raiz para todas as tags do grupo PIS
        #
        self.grupo_pis.CST.raiz       = self.grupo_pis.raiz_tag
        self.grupo_pis.vBC.raiz       = self.grupo_pis.raiz_tag
        self.grupo_pis.pPIS.raiz      = self.grupo_pis.raiz_tag
        self.grupo_pis.vPIS.raiz      = self.grupo_pis.raiz_tag
        self.grupo_pis.qBCProd.raiz   = self.grupo_pis.raiz_tag
        self.grupo_pis.vAliqProd.raiz = self.grupo_pis.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class PIS(XMLNFe):
    def __init__(self):
        super(PIS, self).__init__()
        self.vBC       = TagDecimal(nome='vBC'      , codigo='Q07', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.pPIS      = TagDecimal(nome='pPIS'     , codigo='Q08', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vPIS      = TagDecimal(nome='vPIS'     , codigo='Q09', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.qBCProd   = TagDecimal(nome='qBCProd'  , codigo='Q10', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz='')
        self.vAliqProd = TagDecimal(nome='vAliqProd', codigo='Q11', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz='')

        self.CST      = TagCSTPIS()
        self.CST.grupo_pis = self
        self.CST.valor = '07'
        self.nome_tag = 'PISNT'
        self.nome_tag_txt = 'Q04'
        self.raiz_tag = '//det/imposto/PIS/PISNT'

    def get_xml(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += '<PIS>'
        xml += '<' + self.nome_tag + '>'
        xml += self.CST.xml

        if self.CST.valor in ('01', '02'):
            xml += self.vBC.xml
            xml += self.pPIS.xml
            xml += self.vPIS.xml

        elif self.CST.valor == '03':
            xml += self.qBCProd.xml
            xml += self.vAliqProd.xml
            xml += self.vPIS.xml

        elif self.CST.valor in ('04', '06', '07', '08', '09'):
            pass

        else:
            if self.qBCProd.valor or self.vAliqProd.valor:
                xml += self.qBCProd.xml
                xml += self.vAliqProd.xml
            else:
                xml += self.vBC.xml
                xml += self.pPIS.xml
            xml += self.vPIS.xml

        xml += '</' + self.nome_tag + '></PIS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o PIS, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            if self._le_noh('//det/imposto/PIS/PISAliq') is not None:
                self.CST.valor = '01'
            elif self._le_noh('//det/imposto/PIS/PISQtde') is not None:
                self.CST.valor = '03'
            elif self._le_noh('//det/imposto/PIS/PISNT') is not None:
                self.CST.valor = '04'
            else:
                self.CST.valor = '99'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            self.CST.xml       = arquivo
            self.vBC.xml       = arquivo
            self.pPIS.xml      = arquivo
            self.vPIS.xml      = arquivo
            self.qBCProd.xml   = arquivo
            self.vAliqProd.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'Q|\n'

        #
        # Define as tags baseado no código da situação tributária
        #
        txt += self.nome_tag_txt + '|'
        txt += self.CST.txt + '|'

        if self.CST.valor in ('01', '02'):
            txt += self.vBC.txt + '|'
            txt += self.pPIS.txt + '|'
            txt += self.vPIS.txt + '|'
            txt += '\n'

        elif self.CST.valor == '03':
            txt += self.qBCProd.txt + '|'
            txt += self.vAliqProd.txt + '|'
            txt += self.vPIS.txt + '|'
            txt += '\n'

        elif self.CST.valor in ('04', '06', '07', '08', '09'):
            txt += '\n'

        else:
            txt += self.vPIS.txt + '|'
            txt += '\n'

            if self.qBCProd.valor or self.vAliqProd.valor:
                txt += 'Q10|'
                txt += self.qBCProd.txt + '|'
                txt += self.vAliqProd.txt + '|'
            else:
                txt += 'Q07|'
                txt += self.vBC.txt + '|'
                txt += self.pPIS.txt + '|'

            txt += '\n'

        return txt

    txt = property(get_txt)


class II(XMLNFe):
    def __init__(self):
        super(II, self).__init__()
        self.vBC      = TagDecimal(nome='vBC'     , codigo='P02', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/II')
        self.vDespAdu = TagDecimal(nome='vDespAdu', codigo='P03', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/II')
        self.vII      = TagDecimal(nome='vII'     , codigo='P04', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/II')
        self.vIOF     = TagDecimal(nome='vIOF'    , codigo='P05', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/II')

    def get_xml(self):
        if not (self.vBC.valor or self.vDespAdu.valor or self.vII.valor or self.vIOF.valor):
            return ''

        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += '<II>'
        xml += self.vBC.xml
        xml += self.vDespAdu.xml
        xml += self.vII.xml
        xml += self.vIOF.xml
        xml += '</II>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml      = arquivo
            self.vDespAdu.xml = arquivo
            self.vII.xml      = arquivo
            self.vIOF.xml     = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.vBC.valor or self.vDespAdu.valor or self.vII.valor or self.vIOF.valor):
            return ''

        txt = 'P|'
        txt += self.vBC.txt + '|'
        txt += self.vDespAdu.txt + '|'
        txt += self.vII.txt + '|'
        txt += self.vIOF.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class TagCSTIPI(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagCSTIPI, self).__init__(*args, **kwargs)
        self.nome = 'CST'
        self.codigo = 'O09'
        self.tamanho = [2, 2]
        self.raiz = ''
        self.grupo_ipi = None

    def set_valor(self, novo_valor):
        super(TagCSTIPI, self).set_valor(novo_valor)

        if not self.grupo_ipi:
            return None

        #
        # Definimos todas as tags como não obrigatórias
        #
        self.grupo_ipi.vBC.obrigatorio   = False
        self.grupo_ipi.qUnid.obrigatorio = False
        self.grupo_ipi.vUnid.obrigatorio = False
        self.grupo_ipi.pIPI.obrigatorio  = False
        self.grupo_ipi.vIPI.obrigatorio  = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo IPI ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_ipi.vBC.valor   = '0.00'
        self.grupo_ipi.qUnid.valor = '0.00'
        self.grupo_ipi.vUnid.valor = '0.00'
        self.grupo_ipi.pIPI.valor  = '0.00'
        self.grupo_ipi.vIPI.valor  = '0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de IPI
        #
        if self.valor in ('00', '49', '50', '99'):
            self.grupo_ipi.nome_tag = 'IPITrib'
            self.grupo_ipi.nome_tag_txt = 'O07'
            self.grupo_ipi.raiz_tag = '//det/imposto/IPI/IPITrib'
            self.grupo_ipi.vBC.obrigatorio   = True
            self.grupo_ipi.qUnid.obrigatorio = True
            self.grupo_ipi.vUnid.obrigatorio = True
            self.grupo_ipi.pIPI.obrigatorio  = True
            self.grupo_ipi.vIPI.obrigatorio  = True

        else:
            self.grupo_ipi.nome_tag = 'IPINT'
            self.grupo_ipi.nome_tag_txt = 'O08'
            self.grupo_ipi.raiz_tag = '//det/imposto/IPI/IPINT'

        #
        # Redefine a raiz para todas as tags do grupo IPI
        #
        self.grupo_ipi.CST.raiz   = self.grupo_ipi.raiz_tag
        self.grupo_ipi.vBC.raiz   = self.grupo_ipi.raiz_tag
        self.grupo_ipi.qUnid.raiz = self.grupo_ipi.raiz_tag
        self.grupo_ipi.vUnid.raiz = self.grupo_ipi.raiz_tag
        self.grupo_ipi.pIPI.raiz  = self.grupo_ipi.raiz_tag
        self.grupo_ipi.vIPI.raiz  = self.grupo_ipi.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class IPI(XMLNFe):
    def __init__(self):
        super(IPI, self).__init__()
        self.clEnq    = TagCaracter(nome='clEnq'   , codigo='O02', tamanho=[ 5,  5], raiz='//det/imposto/IPI', obrigatorio=False)
        self.CNPJProd = TagCaracter(nome='CNPJProd', codigo='O03', tamanho=[14, 14], raiz='//det/imposto/IPI', obrigatorio=False)
        self.cSelo    = TagCaracter(nome='cSelo'   , codigo='O04', tamanho=[ 1, 60], raiz='//det/imposto/IPI', obrigatorio=False)
        self.qSelo    = TagInteiro(nome='qSelo'    , codigo='O05', tamanho=[ 1, 12], raiz='//det/imposto/IPI', obrigatorio=False)
        self.cEnq     = TagCaracter(nome='cEnq'    , codigo='O06', tamanho=[ 3,  3], raiz='//det/imposto/IPI', valor='999')

        self.vBC      = TagDecimal(nome='vBC'      , codigo='O10', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.qUnid    = TagDecimal(nome='qUnid'    , codigo='O11', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz='')
        self.vUnid    = TagDecimal(nome='vUnid'    , codigo='O12', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz='')
        self.pIPI     = TagDecimal(nome='pIPI'     , codigo='O13', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vIPI     = TagDecimal(nome='vIPI'     , codigo='O13', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')

        self.CST      = TagCSTIPI()
        self.CST.grupo_ipi = self
        self.CST.valor = '52'
        self.nome_tag = 'IPINT'
        self.nome_tag_txt = 'O08'
        self.raiz_tag = '//det/imposto/IPI/IPINT'


    def get_xml(self):
        if not self.CST.valor.strip():
            return ''

        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += '<IPI>'
        xml += self.clEnq.xml
        xml += self.CNPJProd.xml
        xml += self.cSelo.xml
        xml += self.qSelo.xml
        xml += self.cEnq.xml

        xml += '<' + self.nome_tag + '>'
        xml += self.CST.xml

        if self.CST.valor in ('00', '49', '50', '99'):
            if self.qUnid.valor or self.vUnid.valor:
                xml += self.qUnid.xml
                xml += self.vUnid.xml
            else:
                xml += self.vBC.xml
                xml += self.pIPI.xml
            xml += self.vIPI.xml

        xml += '</' + self.nome_tag + '></IPI>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o IPI, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            if self._le_noh('//det/imposto/IPI/IPINT') is not None:
                self.CST.valor = '01'
            else:
                self.CST.valor = '00'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            self.CST.xml      = arquivo
            self.clEnq.xml    = arquivo
            self.CNPJProd.xml = arquivo
            self.cSelo.xml    = arquivo
            self.qSelo.xml    = arquivo
            self.cEnq.xml     = arquivo
            self.vBC.xml      = arquivo
            self.qUnid.xml    = arquivo
            self.vUnid.xml    = arquivo
            self.pIPI.xml     = arquivo
            self.vIPI.xml     = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not ((self.CST.valor in ('00', '49', '50', '99')) or
           (self.qUnid.valor or self.vUnid.valor or self.vBC.valor or self.pIPI.valor or self.vIPI.valor)):
            return ''

        #
        # Define as tags baseado no código da situação tributária
        #
        txt = 'O|\n'
        txt += self.clEnq.txt + '|'
        txt += self.CNPJProd.txt + '|'
        txt += self.cSelo.txt + '|'
        txt += self.qSelo.txt + '|'
        txt += self.cEnq.txt + '|'
        txt += '\n'

        #
        # Define as tags baseado no código da situação tributária
        #
        txt += self.nome_tag_txt + '|'
        txt += self.CST.txt + '|'

        if self.CST.valor not in ('00', '49', '50', '99'):
            txt += '\n'
        else:
            txt += self.vIPI.txt + '|'
            txt += '\n'

            if self.qUnid.valor or self.vUnid.valor:
                txt += 'O10|'
                txt += self.qUnid.txt + '|'
                txt += self.vUnid.txt + '|'

            else:
                txt += 'O11|'
                txt += self.vBC.txt + '|'
                txt += self.pIPI.txt + '|'

            txt += '\n'

        return txt

    txt = property(get_txt)


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
        self.grupo_icms.modBC.obrigatorio    = False
        self.grupo_icms.vBC.obrigatorio      = False
        self.grupo_icms.pRedBC.obrigatorio   = False
        self.grupo_icms.pICMS.obrigatorio    = False
        self.grupo_icms.vICMS.obrigatorio    = False
        self.grupo_icms.modBCST.obrigatorio  = False
        self.grupo_icms.pMVAST.obrigatorio   = False
        self.grupo_icms.pRedBCST.obrigatorio = False
        self.grupo_icms.vBCST.obrigatorio    = False
        self.grupo_icms.pICMSST.obrigatorio  = False
        self.grupo_icms.vICMSST.obrigatorio  = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo ICMS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_icms.modBC.valor    = 3
        self.grupo_icms.vBC.valor      = '0.00'
        self.grupo_icms.pRedBC.valor   = '0.00'
        self.grupo_icms.pICMS.valor    = '0.00'
        self.grupo_icms.vICMS.valor    = '0.00'
        self.grupo_icms.modBCST.valor  = 4
        self.grupo_icms.pMVAST.valor   = '0.00'
        self.grupo_icms.pRedBCST.valor = '0.00'
        self.grupo_icms.vBCST.valor    = '0.00'
        self.grupo_icms.pICMSST.valor  = '0.00'
        self.grupo_icms.vICMSST.valor  = '0.00'

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
            self.grupo_icms.nome_tag = 'ICMS10'
            self.grupo_icms.nome_tag_txt = 'N03'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMS10'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

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
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.vICMSST.obrigatorio  = True

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
            self.grupo_icms.nome_tag = 'ICMS90'
            self.grupo_icms.nome_tag_txt = 'N10'
            self.grupo_icms.raiz_tag = '//det/imposto/ICMS/ICMS90'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

        #
        # Redefine a raiz para todas as tags do grupo ICMS
        #
        self.grupo_icms.orig.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.CST.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.modBC.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vBC.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBC.raiz   = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMS.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMS.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.modBCST.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.pMVAST.raiz   = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBCST.raiz = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCST.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMSST.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSST.raiz  = self.grupo_icms.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class ICMS(XMLNFe):
    def __init__(self):
        super(ICMS, self).__init__()
        self.orig     = TagInteiro(nome='orig'    , codigo='N11', tamanho=[1,  1, 1],                     raiz='')
        #                                            codigo='N12' é o campo CST
        self.modBC    = TagInteiro(nome='modBC'   , codigo='N13', tamanho=[1,  1, 1],                     raiz='')
        self.pRedBC   = TagDecimal(nome='pRedBC'  , codigo='N14', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vBC      = TagDecimal(nome='vBC'     , codigo='N15', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.pICMS    = TagDecimal(nome='pICMS'   , codigo='N16', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vICMS    = TagDecimal(nome='vICMS'   , codigo='N17', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.modBCST  = TagInteiro(nome='modBCST' , codigo='N18', tamanho=[1,  1, 1],                     raiz='')
        self.pMVAST   = TagDecimal(nome='pMVAST'  , codigo='N19', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.pRedBCST = TagDecimal(nome='pRedBCST', codigo='N20', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vBCST    = TagDecimal(nome='vBCST'   , codigo='N21', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.pICMSST  = TagDecimal(nome='pICMSST' , codigo='N22', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='')
        self.vICMSST  = TagDecimal(nome='vICMSST' , codigo='N23', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')

        self.CST      = TagCSTICMS()
        self.CST.grupo_icms = self
        self.CST.valor = '40'
        self.nome_tag = 'ICMS40'
        self.raiz_tag = '//det/imposto/ICMS/ICMS40'
        self.nome_tag_txt = 'N06'

    def get_xml(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += '<ICMS><' + self.nome_tag + '>'
        xml += self.orig.xml
        xml += self.CST.xml

        if self.CST.valor == '00':
            xml += self.modBC.xml
            xml += self.vBC.xml
            xml += self.pICMS.xml
            xml += self.vICMS.xml

        elif self.CST.valor == '10':
            xml += self.modBC.xml
            xml += self.vBC.xml
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

        elif self.CST.valor == '20':
            xml += self.modBC.xml
            xml += self.vBC.xml
            xml += self.pRedBC.xml
            xml += self.pICMS.xml
            xml += self.vICMS.xml

        elif self.CST.valor == '30':
            xml += self.modBCST.xml

            # Somente quando for margem de valor agregado
            if self.modBCST.valor == 4:
                xml += self.pMVAST.xml

            xml += self.pRedBCST.xml
            xml += self.vBCST.xml
            xml += self.pICMSST.xml
            xml += self.vICMSST.xml

        elif self.CST.valor in ('40', '41', '50'):
            pass

        elif self.CST.valor == '51':
            xml += self.modBC.xml
            xml += self.pRedBC.xml
            xml += self.vBC.xml
            xml += self.pICMS.xml
            xml += self.vICMS.xml

        elif self.CST.valor == '60':
            xml += self.vBCST.xml
            xml += self.vICMSST.xml

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

        elif self.CST.valor == '90':
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

        xml += '</' + self.nome_tag + '></ICMS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o ICMS, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            if self._le_noh('//det/imposto/ICMS/ICMS00') is not None:
                self.CST.valor = '00'
            elif self._le_noh('//det/imposto/ICMS/ICMS10') is not None:
                self.CST.valor = '10'
            elif self._le_noh('//det/imposto/ICMS/ICMS20') is not None:
                self.CST.valor = '20'
            elif self._le_noh('//det/imposto/ICMS/ICMS30') is not None:
                self.CST.valor = '30'
            elif self._le_noh('//det/imposto/ICMS/ICMS40') is not None:
                self.CST.valor = '40'
            elif self._le_noh('//det/imposto/ICMS/ICMS51') is not None:
                self.CST.valor = '51'
            elif self._le_noh('//det/imposto/ICMS/ICMS60') is not None:
                self.CST.valor = '60'
            elif self._le_noh('//det/imposto/ICMS/ICMS70') is not None:
                self.CST.valor = '70'
            elif self._le_noh('//det/imposto/ICMS/ICMS90') is not None:
                self.CST.valor = '90'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            self.orig.xml     = arquivo
            self.CST.xml      = arquivo
            self.modBC.xml    = arquivo
            self.vBC.xml      = arquivo
            self.pRedBC.xml   = arquivo
            self.pICMS.xml    = arquivo
            self.vICMS.xml    = arquivo
            self.modBCST.xml  = arquivo
            self.pMVAST.xml   = arquivo
            self.pRedBCST.xml = arquivo
            self.vBCST.xml    = arquivo
            self.pICMSST.xml  = arquivo
            self.vICMSST.xml  = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        txt = 'N|\n'
        txt += self.nome_tag_txt + '|'
        txt += self.orig.txt + '|'
        txt += self.CST.txt + '|'

        if self.CST.valor == '00':
            txt += self.modBC.txt + '|'
            txt += self.vBC.txt + '|'
            txt += self.pICMS.txt + '|'
            txt += self.vICMS.txt + '|'

        elif self.CST.valor == '10':
            txt += self.modBC.txt + '|'
            txt += self.vBC.txt + '|'
            txt += self.pICMS.txt + '|'
            txt += self.vICMS.txt + '|'
            txt += self.modBCST.txt + '|'

            # Somente quando for margem de valor agregado
            if self.modBCST.valor == 4:
                txt += self.pMVAST.txt + '|'
            else:
                txt += '|'

            txt += self.pRedBCST.txt + '|'
            txt += self.vBCST.txt + '|'
            txt += self.pICMSST.txt + '|'
            txt += self.vICMSST.txt + '|'

        elif self.CST.valor == '20':
            txt += self.modBC.txt + '|'
            txt += self.vBC.txt + '|'
            txt += self.pRedBC.txt + '|'
            txt += self.pICMS.txt + '|'
            txt += self.vICMS.txt + '|'

        elif self.CST.valor == '30':
            txt += self.modBCST.txt + '|'

            # Somente quando for margem de valor agregado
            if self.modBCST.valor == 4:
                txt += self.pMVAST.txt + '|'
            else:
                txt += '|'

            txt += self.pRedBCST.txt + '|'
            txt += self.vBCST.txt + '|'
            txt += self.pICMSST.txt + '|'
            txt += self.vICMSST.txt + '|'

        elif self.CST.valor in ('40', '41', '50'):
            pass

        elif self.CST.valor == '51':
            txt += self.modBC.txt + '|'
            txt += self.pRedBC.txt + '|'
            txt += self.vBC.txt + '|'
            txt += self.pICMS.txt + '|'
            txt += self.vICMS.txt + '|'

        elif self.CST.valor == '60':
            txt += self.vBCST.txt + '|'
            txt += self.vICMSST.txt + '|'

        elif self.CST.valor == '70':
            txt += self.modBC.txt + '|'
            txt += self.vBC.txt + '|'
            txt += self.pRedBC.txt + '|'
            txt += self.pICMS.txt + '|'
            txt += self.vICMS.txt + '|'
            txt += self.modBCST.txt + '|'

            # Somente quando for margem de valor agregado
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

            # Somente quando for margem de valor agregado
            if self.modBCST.valor == 4:
                txt += self.pMVAST.txt + '|'
            else:
                txt += '|'

            txt += self.pRedBCST.txt + '|'
            txt += self.vBCST.txt + '|'
            txt += self.pICMSST.txt + '|'
            txt += self.vICMSST.txt + '|'

        txt += '\n'
        return txt

    txt = property(get_txt)


class Imposto(XMLNFe):
    def __init__(self):
        super(Imposto, self).__init__()
        self.ICMS     = ICMS()
        self.IPI      = IPI()
        self.II       = II()
        self.PIS      = PIS()
        self.PISST    = PISST()
        self.COFINS   = COFINS()
        self.COFINSST = COFINSST()
        self.ISSQN    = ISSQN()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<imposto>'
        xml += self.ICMS.xml
        xml += self.IPI.xml
        xml += self.II.xml
        xml += self.PIS.xml
        xml += self.PISST.xml
        xml += self.COFINS.xml
        xml += self.COFINSST.xml
        xml += self.ISSQN.xml
        xml += '</imposto>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
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
        txt += self.ICMS.txt
        txt += self.IPI.txt
        txt += self.II.txt
        txt += self.PIS.txt
        txt += self.PISST.txt
        txt += self.COFINS.txt
        txt += self.COFINSST.txt
        txt += self.ISSQN.txt
        return txt

    txt = property(get_txt)


class ICMSCons(XMLNFe):
    def __init__(self):
        super(ICMSCons, self).__init__()
        self.vBCICMSSTCons = TagDecimal(nome='vBCICMSSTCons', codigo='L118', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/prod/comb/ICMSCons')
        self.vICMSSTCons   = TagDecimal(nome='vICMSSTCons'  , codigo='L119', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/prod/comb/ICMSCons')
        self.UFcons        = TagCaracter(nome='UFcons'      , codigo='L120', tamanho=[2,  2],                        raiz='//det/prod/comb/ICMSCons')

    def get_xml(self):
        if not (self.vBCICMSSTCons.valor or self.vICMSSTCons.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ICMSCons>'
        xml += self.vBCICMSSTCons.xml
        xml += self.vICMSSTCons.xml
        xml += self.UFcons.xml
        xml += '</ICMSCons>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBCICMSSTCons.xml = arquivo
            self.vICMSSTCons.xml   = arquivo
            self.UFcons.xml        = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.vBCICMSSTCons.valor or self.vICMSSTCons.valor):
            return ''

        txt = 'L117|'
        txt += self.vBCICMSSTCons.txt + '|'
        txt += self.vICMSSTCons.txt + '|'
        txt += self.UFCons.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class ICMSInter(XMLNFe):
    def __init__(self):
        super(ICMSInter, self).__init__()
        self.vBCICMSSTDest = TagDecimal(nome='vBCICMSSTDest', codigo='L115', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/prod/comb/ICMSInter')
        self.vICMSSTDest   = TagDecimal(nome='vICMSSTDest'  , codigo='L116', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/prod/comb/ICMSInter')

    def get_xml(self):
        if not (self.vBCICMSSTDest.valor or self.vICMSSTDest.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ICMSInter>'
        xml += self.vBCICMSSTDest.xml
        xml += self.vICMSSTDest.xml
        xml += '</ICMSInter>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBCICMSSTDest.xml = arquivo
            self.vICMSSTDest.xml   = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.vBCICMSSTDest.valor or self.vICMSSTDest.valor):
            return ''

        txt = 'L114|'
        txt += self.vBCICMSSTDest.txt + '|'
        txt += self.vICMSSTDest.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class ICMSComb(XMLNFe):
    def __init__(self):
        super(ICMSComb, self).__init__()
        self.vBCICMS   = TagDecimal(nome='vBCICMS'  , codigo='L110', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/prod/comb/ICMSComb')
        self.vICMS     = TagDecimal(nome='vICMS'    , codigo='L111', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/prod/comb/ICMSComb')
        self.vBCICMSST = TagDecimal(nome='vBCICMSST', codigo='L112', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/prod/comb/ICMSComb')
        self.vICMSST   = TagDecimal(nome='vICMSST'  , codigo='L113', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/prod/comb/ICMSComb')

    def get_xml(self):
        if not (self.vBCICMS.valor or self.vICMS.valor or self.vBCICMSST.valor or self.vICMSST.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ICMSComb>'
        xml += self.vBCICMS.xml
        xml += self.vICMS.xml
        xml += self.vBCICMSST.xml
        xml += self.vICMSST.xml
        xml += '</ICMSComb>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBCICMS.xml   = arquivo
            self.vICMS.xml     = arquivo
            self.vBCICMSST.xml = arquivo
            self.vICMSST.xml   = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.vBCICMS.valor or self.vICMS.valor or self.vBCICMSST.valor or self.vICMSST.valor):
            return ''

        txt = 'L109|'
        txt += self.vBCICMS.txt + '|'
        txt += self.vICMS.txt + '|'
        txt += self.vBCICMSST.txt + '|'
        txt += self.vICMSST.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class CIDE(XMLNFe):
    def __init__(self):
        super(CIDE, self).__init__()
        self.qBCProd   = TagDecimal(nome='qBCProd'  , codigo='L106', tamanho=[1, 16]  , decimais=[0, 4, 4], raiz='//det/prod/comb/CIDE')
        self.vAliqProd = TagDecimal(nome='vAliqProd', codigo='L107', tamanho=[1, 15]  , decimais=[0, 4, 4], raiz='//det/prod/comb/CIDE')
        self.vCIDE     = TagDecimal(nome='vCIDE'    , codigo='L108', tamanho=[1, 15]  , decimais=[0, 2, 2], raiz='//det/prod/comb/CIDE')

    def get_xml(self):
        if not (self.qBCProd.valor or self.vAliqProd.valor or self.vCIDE.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<CIDE>'
        xml += self.qBCProd.xml
        xml += self.vAliqProd.xml
        xml += self.vCIDE.xml
        xml += '</CIDE>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.qBCProd.xml   = arquivo
            self.vAliqProd.xml = arquivo
            self.vCIDE.xml     = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.qBCProd.valor or self.vAliqProd.valor or self.vCIDE.valor):
            return ''

        txt = 'L105|'
        txt += self.qBCProd.txt + '|'
        txt += self.vAliqProd.txt + '|'
        txt += self.vCIDE.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class Comb(XMLNFe):
    def __init__(self):
        super(Comb, self).__init__()
        self.cProdANP  = TagInteiro(nome='cProdANP', codigo='L102', tamanho=[9,  9, 9],                     raiz='//det/prod/comb')
        self.CODIF     = TagInteiro(nome='CODIF'   , codigo='L103', tamanho=[0, 21]   ,                     raiz='//det/prod/comb', obrigatorio=False)
        self.qTemp     = TagDecimal(nome='qTemp'   , codigo='L104', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz='//det/prod/comb', obrigatorio=False)
        self.CIDE      = CIDE()
        self.ICMSComb  = ICMSComb()
        self.ICMSInter = ICMSInter()
        self.ICMSCons  = ICMSCons()

    def get_xml(self):
        if not self.cProdANP.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<comb>'
        xml += self.cProdANP.xml
        xml += self.CODIF.xml
        xml += self.qTemp.xml
        xml += self.CIDE.xml
        xml += self.ICMSComb.xml
        xml += self.ICMSInter.xml
        xml += self.ICMSCons.xml
        xml += '</comb>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cProdANP.xml  = arquivo
            self.CODIF.xml     = arquivo
            self.qTemp.xml     = arquivo
            self.CIDE.xml      = arquivo
            self.ICMSComb.xml  = arquivo
            self.ICMSInter.xml = arquivo
            self.ICMSCons.xml  = arquivo

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
        txt += self.ICMSComb.txt
        txt += self.ICMSInter.txt
        txt += self.ICMSCons.txt

        return txt

    txt = property(get_txt)


class Arma(XMLNFe):
    def __init__(self):
        super(Arma, self).__init__()
        self.tpArma = TagInteiro(nome='tpArma', codigo='L02', tamanho=[1,   1], raiz='//arma')
        self.nSerie = TagInteiro(nome='nSerie', codigo='L03', tamanho=[1,   9], raiz='//arma')
        self.nCano  = TagInteiro(nome='nCano',  codigo='L04', tamanho=[1,   9], raiz='//arma')
        self.descr  = TagCaracter(nome='descr', codigo='L05', tamanho=[1, 256], raiz='//arma')

    def get_xml(self):
        if not self.nSerie:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<arma>'
        xml += self.tpArma.xml
        xml += self.nSerie.xml
        xml += self.nCano.xml
        xml += self.descr.xml
        xml += '</arma>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpArma.xml = arquivo
            self.nSerie.xml = arquivo
            self.nCano.xml  = arquivo
            self.descr.xml  = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not self.nLote.valor:
            return ''

        txt = 'L|'
        txt += self.tpArma.txt + '|'
        txt += self.nSerie.txt + '|'
        txt += self.nCano.txt + '|'
        txt += self.descr.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class Med(XMLNFe):
    def __init__(self):
        super(Med, self).__init__()
        self.nLote = TagCaracter(nome='nLote', codigo='K02', tamanho=[1, 20]                    , raiz='//med')
        self.qLote = TagDecimal(nome='qLote' , codigo='K03', tamanho=[1, 11], decimais=[0, 3, 3], raiz='//med')
        self.dFab  = TagData(nome='dFab'     , codigo='K04'                                     , raiz='//med')
        self.dVal  = TagData(nome='dVal'     , codigo='K05'                                     , raiz='//med')
        self.vPMC  = TagDecimal(nome='vPMC'  , codigo='K06', tamanho=[1, 15], decimais=[0, 2, 2], raiz='//med')

    def get_xml(self):
        if not self.nLote.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<med>'
        xml += self.nLote.xml
        xml += self.qLote.xml
        xml += self.dFab.xml
        xml += self.dVal.xml
        xml += self.vPMC.xml
        xml += '</med>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nLote.xml = arquivo
            self.qLote.xml = arquivo
            self.dFab.xml  = arquivo
            self.dVal.xml  = arquivo
            self.vPMC.xml  = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not self.nLote.valor:
            return ''

        txt = 'K|'
        txt += self.nLote.txt + '|'
        txt += self.qLote.txt + '|'
        txt += self.dFab.txt + '|'
        txt += self.dVal.txt + '|'
        txt += self.vPMC.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class VeicProd(XMLNFe):
    def __init__(self):
        super(VeicProd, self).__init__()
        self.tpOp     = TagInteiro(nome='tpOp'    , codigo='J02', tamanho=[ 1,  1, 1], raiz='//det/prod/veicProd')
        self.chassi   = TagCaracter(nome='chassi' , codigo='J03', tamanho=[ 1, 17]   , raiz='//det/prod/veicProd')
        self.cCor     = TagCaracter(nome='cCor'   , codigo='J04', tamanho=[ 1,  4]   , raiz='//det/prod/veicProd')
        self.xCor     = TagCaracter(nome='xCor'   , codigo='J05', tamanho=[ 1, 40]   , raiz='//det/prod/veicProd')
        self.pot      = TagCaracter(nome='pot'    , codigo='J06', tamanho=[ 1,  4]   , raiz='//det/prod/veicProd')
        self.CM3      = TagCaracter(nome='CM3'    , codigo='J07', tamanho=[ 1,  4]   , raiz='//det/prod/veicProd')
        self.pesoL    = TagCaracter(nome='pesoL'  , codigo='J08', tamanho=[ 1,  9]   , raiz='//det/prod/veicProd')
        self.pesoB    = TagCaracter(nome='pesoB'  , codigo='J09', tamanho=[ 1,  9]   , raiz='//det/prod/veicProd')
        self.nSerie   = TagCaracter(nome='nSerie' , codigo='J10', tamanho=[ 1,  9]   , raiz='//det/prod/veicProd')
        self.tpComb   = TagCaracter(nome='tpComb' , codigo='J11', tamanho=[ 1,  8]   , raiz='//det/prod/veicProd')
        self.nMotor   = TagCaracter(nome='nMotor' , codigo='J12', tamanho=[ 1, 21]   , raiz='//det/prod/veicProd')
        self.CMKG     = TagCaracter(nome='CMKG'   , codigo='J13', tamanho=[ 1,  9]   , raiz='//det/prod/veicProd')
        self.dist     = TagCaracter(nome='dist'   , codigo='J14', tamanho=[ 1,  4]   , raiz='//det/prod/veicProd')
        self.RENAVAM  = TagCaracter(nome='RENAVAM', codigo='J15', tamanho=[ 1,  9]   , raiz='//det/prod/veicProd', obrigatorio=False)
        self.anoMod   = TagInteiro(nome='anoMod'  , codigo='J16', tamanho=[ 4,  4, 4], raiz='//det/prod/veicProd')
        self.anoFab   = TagInteiro(nome='anoFab'  , codigo='J17', tamanho=[ 4,  4, 4], raiz='//det/prod/veicProd')
        self.tpPint   = TagCaracter(nome='tpPint' , codigo='J18', tamanho=[ 1,  1]   , raiz='//det/prod/veicProd')
        self.tpVeic   = TagInteiro(nome='tpVeic'  , codigo='J19', tamanho=[ 2,  2, 2], raiz='//det/prod/veicProd')
        self.espVeic  = TagInteiro(nome='espVeic' , codigo='J20', tamanho=[ 1,  1]   , raiz='//det/prod/veicProd')
        self.VIN      = TagCaracter(nome='VIN'    , codigo='J21', tamanho=[ 1,  1]   , raiz='//det/prod/veicProd')
        self.condVeic = TagInteiro(nome='condVeic', codigo='J22', tamanho=[ 1,  1]   , raiz='//det/prod/veicProd')
        self.cMod     = TagInteiro(nome='cMod'    , codigo='J23', tamanho=[ 6,  6, 6], raiz='//det/prod/veicProd')

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
        xml += self.CM3.xml
        xml += self.pesoL.xml
        xml += self.pesoB.xml
        xml += self.nSerie.xml
        xml += self.tpComb.xml
        xml += self.nMotor.xml
        xml += self.CMKG.xml
        xml += self.dist.xml
        xml += self.RENAVAM.xml
        xml += self.anoMod.xml
        xml += self.anoFab.xml
        xml += self.tpPint.xml
        xml += self.tpVeic.xml
        xml += self.espVeic.xml
        xml += self.VIN.xml
        xml += self.condVeic.xml
        xml += self.cMod.xml
        xml += '</veicProd>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpOp.xml     = arquivo
            self.chassi.xml   = arquivo
            self.cCor.xml     = arquivo
            self.xCor.xml     = arquivo
            self.pot.xml      = arquivo
            self.CM3.xml      = arquivo
            self.pesoL.xml    = arquivo
            self.pesoB.xml    = arquivo
            self.nSerie.xml   = arquivo
            self.tpComb.xml   = arquivo
            self.nMotor.xml   = arquivo
            self.CMKG.xml     = arquivo
            self.dist.xml     = arquivo
            self.RENAVAM.xml  = arquivo
            self.anoMod.xml   = arquivo
            self.anoFab.xml   = arquivo
            self.tpPint.xml   = arquivo
            self.tpVeic.xml   = arquivo
            self.espVeic.xml  = arquivo
            self.VIN.xml      = arquivo
            self.condVeic.xml = arquivo
            self.cMod.xml     = arquivo

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
        txt += self.CM3.txt + '|'
        txt += self.pesoL.txt + '|'
        txt += self.pesoB.txt + '|'
        txt += self.nSerie.txt + '|'
        txt += self.tpComb.txt + '|'
        txt += self.nMotor.txt + '|'
        txt += self.CMKG.txt + '|'
        txt += self.dist.txt + '|'
        txt += self.RENAVAM.txt + '|'
        txt += self.anoMod.txt + '|'
        txt += self.anoFab.txt + '|'
        txt += self.tpPint.txt + '|'
        txt += self.tpVeic.txt + '|'
        txt += self.espVeic.txt + '|'
        txt += self.VIN.txt + '|'
        txt += self.condVeic.txt + '|'
        txt += self.cMod.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class Adi(XMLNFe):
    def __init__(self):
        super(Adi, self).__init__()
        self.nAdicao     = TagInteiro(nome='nAdicao'     , codigo='I26', tamanho=[1,  3],                     raiz='//adi')
        self.nSeqAdic    = TagInteiro(nome='nSeqAdic'    , codigo='I27', tamanho=[1,  3],                     raiz='//adi')
        self.cFabricante = TagCaracter(nome='cFabricante', codigo='I28', tamanho=[1, 60],                     raiz='//adi')
        self.vDescDI     = TagDecimal(nome='vDescDI'     , codigo='I29', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//adi', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<adi>'
        xml += self.nAdicao.xml
        xml += self.nSeqAdic.xml
        xml += self.cFabricante.xml
        xml += self.vDescDI.xml
        xml += '</adi>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nAdicao.xml     = arquivo
            self.nSeqAdic.xml    = arquivo
            self.cFabricante.xml = arquivo
            self.vDescDI.xml     = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'I25|'
        txt += self.nAdicao.txt + '|'
        txt += self.nSeqAdic.txt + '|'
        txt += self.cFabricante.txt + '|'
        txt += self.vDescDI.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class DI(XMLNFe):
    def __init__(self):
        super(DI, self).__init__()
        self.nDI         = TagCaracter(nome='nDI'        , codigo='I19', tamanho=[1, 10], raiz='//DI')
        self.dDI         = TagData(nome='dDI'            , codigo='I20',                  raiz='//DI')
        self.xLocDesemb  = TagCaracter(nome='xLocDesemb' , codigo='I21', tamanho=[1, 60], raiz='//DI')
        self.UFDesemb    = TagCaracter(nome='UFDesemb'   , codigo='I22', tamanho=[2,  2], raiz='//DI')
        self.dDesemb     = TagData(nome='dDesemb'        , codigo='I23',                  raiz='//DI')
        self.cExportador = TagCaracter(nome='cExportador', codigo='I24', tamanho=[1, 60], raiz='//DI')
        self.adi         = [Adi()]

    def get_xml(self):
        if not self.nDI:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<DI>'
        xml += self.nDI.xml
        xml += self.dDI.xml
        xml += self.xLocDesemb.xml
        xml += self.UFDesemb.xml
        xml += self.dDesemb.xml
        xml += self.cExportador.xml

        for a in self.adi:
            xml += a.xml

        xml += '</DI>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nDI.xml         = arquivo
            self.dDI.xml         = arquivo
            self.xLocDesemb.xml  = arquivo
            self.UFDesemb.xml    = arquivo
            self.dDesemb.xml     = arquivo
            self.cExportador.xml = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            adis = self._le_nohs('//DI/adi')
            self.adi = []
            if adis is not None:
                self.adi = [Adi() for a in adis]
                for i in range(len(adis)):
                    self.adi[i].xml = adis[i]

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not self.nDI:
            return ''

        txt = 'I18|'
        txt += self.nDI.txt + '|'
        txt += self.dDI.txt + '|'
        txt += self.xLocDesemb.txt + '|'
        txt += self.UFDesemb.txt + '|'
        txt += self.dDesemb.txt + '|'
        txt += self.cExportador.txt + '|'
        txt += '\n'

        for a in self.adi:
            txt += a.txt

        return txt

    txt = property(get_txt)


class Prod(XMLNFe):
    def __init__(self):
        super(Prod, self).__init__()
        self.cProd    = TagCaracter(nome='cProd'   , codigo='I02' , tamanho=[1,  60]                       , raiz='//det/prod')
        self.cEAN     = TagCaracter(nome='cEAN'    , codigo='I03' , tamanho=[0,  14]                       , raiz='//det/prod')
        self.xProd    = TagCaracter(nome='xProd'   , codigo='I04' , tamanho=[1, 120]                       , raiz='//det/prod')
        self.NCM      = TagCaracter(nome='NCM'     , codigo='I05' , tamanho=[2,   8]                       , raiz='//det/prod', obrigatorio=False)
        self.EXTIPI   = TagCaracter(nome='EXTIPI'  , codigo='I06' , tamanho=[2,   3]                       , raiz='//det/prod', obrigatorio=False)
        self.genero   = TagCaracter(nome='genero'  , codigo='I07' , tamanho=[2,   2, 2]                    , raiz='//det/prod', obrigatorio=False)
        self.CFOP     = TagInteiro(nome='CFOP'     , codigo='I08' , tamanho=[4,   4, 4]                    , raiz='//det/prod')
        self.uCom     = TagCaracter(nome='uCom'    , codigo='I09' , tamanho=[1,   6]                       , raiz='//det/prod')
        self.qCom     = TagDecimal(nome='qCom'     , codigo='I10' , tamanho=[1,  12, 1], decimais=[0, 4, 4], raiz='//det/prod')
        self.vUnCom   = TagDecimal(nome='vUnCom'   , codigo='I10a', tamanho=[1,  16, 1], decimais=[0, 4, 4], raiz='//det/prod')
        self.vProd    = TagDecimal(nome='vProd'    , codigo='I11' , tamanho=[1,  15, 1], decimais=[0, 2, 2], raiz='//det/prod')
        self.cEANTrib = TagCaracter(nome='cEANTrib', codigo='I12' , tamanho=[0,  14]                       , raiz='//det/prod')
        self.uTrib    = TagCaracter(nome='uTrib'   , codigo='I13' , tamanho=[1,   6]                       , raiz='//det/prod')
        self.qTrib    = TagDecimal(nome='qTrib'    , codigo='I14' , tamanho=[1,  12, 1], decimais=[0, 4, 4], raiz='//det/prod')
        self.vUnTrib  = TagDecimal(nome='vUnTrib'  , codigo='I14a', tamanho=[1,  16, 1], decimais=[0, 4, 4], raiz='//det/prod')
        self.vTrib    = TagDecimal(nome='vTrib'    , codigo=''    , tamanho=[1,  15, 1], decimais=[0, 2, 2], raiz='//det/prod', obrigatorio=False)
        self.vFrete   = TagDecimal(nome='vFrete'   , codigo='I15' , tamanho=[1,  15, 1], decimais=[0, 2, 2], raiz='//det/prod', obrigatorio=False)
        self.vSeg     = TagDecimal(nome='vSeg'     , codigo='I16' , tamanho=[1,  15, 1], decimais=[0, 2, 2], raiz='//det/prod', obrigatorio=False)
        self.vDesc    = TagDecimal(nome='vDesc'    , codigo='I17' , tamanho=[1,  15, 1], decimais=[0, 2, 2], raiz='//det/prod', obrigatorio=False)
        self.DI       = []
        self.veicProd = VeicProd()
        self.med      = []
        self.arma     = []
        self.comb     = Comb()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<prod>'
        xml += self.cProd.xml
        xml += self.cEAN.xml
        xml += self.xProd.xml
        xml += self.NCM.xml
        xml += self.EXTIPI.xml
        xml += self.genero.xml
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

        for d in self.DI:
            xml += d.xml

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
            self.genero.xml   = arquivo
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

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.DI = self.le_grupo('//det/prod/DI', DI)

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
        txt += self.genero.txt + '|'
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


class Det(XMLNFe):
    def __init__(self):
        super(Det, self).__init__()
        self.nItem     = TagInteiro(nome='det'       , codigo='H01', tamanho=[1,   3], propriedade='nItem', raiz='/') #, namespace=NAMESPACE_NFE)
        self.prod      = Prod()
        self.imposto   = Imposto()
        self.infAdProd = TagCaracter(nome='infAdProd', codigo='V01', tamanho=[1, 500], raiz='//det', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.nItem.xml
        xml += self.prod.xml
        xml += self.imposto.xml
        xml += self.infAdProd.xml
        xml += '</det>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nItem.xml     = arquivo
            self.prod.xml      = arquivo
            self.imposto.xml   = arquivo
            self.infAdProd.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'H|'
        txt += self.nItem.txt + '|'
        txt += self.infAdProd.txt + '|'
        txt += '\n'

        txt += self.prod.txt
        txt += self.imposto.txt
        return txt

    txt = property(get_txt)


    def descricao_produto_formatada(self):
        formatado = self.prod.xProd.valor.replace('|', '<br />')

        if len(self.infAdProd.valor):
            formatado += '<br />'
            formatado += self.infAdProd.valor.replace('|', '<br />')

        return formatado

    def cst_formatado(self):
        formatado = unicode(self.imposto.ICMS.orig.valor).zfill(1)
        formatado += unicode(self.imposto.ICMS.CST.valor).zfill(2)
        return formatado


class Compra(XMLNFe):
    def __init__(self):
        super(Compra, self).__init__()
        self.xNEmp = TagCaracter(nome='xNEmp', codigo='ZB02', tamanho=[1, 17], raiz='//NFe/infNFe/compra', obrigatorio=False)
        self.xPed  = TagCaracter(nome='xPed' , codigo='ZB03', tamanho=[1, 60], raiz='//NFe/infNFe/compra', obrigatorio=False)
        self.xCont = TagCaracter(nome='xCont', codigo='ZB04', tamanho=[1, 60], raiz='//NFe/infNFe/compra', obrigatorio=False)

    def get_xml(self):
        if not (self.xNEmp.valor or self.xPed.valor or self.xCont.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<compra>'
        xml += self.xNEmp.xml
        xml += self.xPed.xml
        xml += self.xCont.xml
        xml += '</compra>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xNEmp.xml = arquivo
            self.xPed.xml  = arquivo
            self.xCont.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.xNEmp.valor or self.xPed.valor or self.xCont.valor):
            return ''

        txt = 'ZB|'
        txt += self.xNEmp.txt + '|'
        txt += self.xPed.txt + '|'
        txt += self.xCont.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class Exporta(XMLNFe):
    def __init__(self):
        super(Exporta, self).__init__()
        self.UFEmbarq   = TagCaracter(nome='UFEmbarq'  , codigo='ZA02', tamanho=[2,  2], raiz='//NFe/infNFe/exporta', obrigatorio=False)
        self.xLocEmbarq = TagCaracter(nome='xLocEmbarq', codigo='ZA03', tamanho=[1, 60], raiz='//NFe/infNFe/exporta', obrigatorio=False)

    def get_xml(self):
        if not (self.UFEmbarq.valor or self.xLocEmbarq.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<exporta>'
        xml += self.UFEmbarq.xml
        xml += self.xLocEmbarq.xml
        xml += '</exporta>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.UFEmbarq.xml   = arquivo
            self.xLocEmbarq.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.UFEmbarq.valor or self.xLocEmbarq.valor):
            return ''

        txt = 'ZA|'
        txt += self.UFEmbarq.txt + '|'
        txt += self.xLocEmbarq.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class ProcRef(XMLNFe):
    def __init__(self):
        super(ProcRef, self).__init__()
        self.nProc   = TagCaracter(nome='nProc' , codigo='Z11', tamanho=[1, 60], raiz='//procRef')
        self.indProc = TagInteiro(nome='indProc', codigo='Z12', tamanho=[1,  1], raiz='//procRef')

    def get_xml(self):
        if not (self.nProc.valor or self.indProc.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<procRef>'
        xml += self.nProc.xml
        xml += self.indProc.xml
        xml += '</procRef>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nProc.xml = arquivo
            self.indProc.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.nProc.valor or self.indProc.valor):
            return ''

        txt = 'Z10|'
        txt += self.nProc.txt + '|'
        txt += self.indProc.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class ObsFisco(XMLNFe):
    def __init__(self):
        super(ObsFisco, self).__init__()
        self.xCampo = TagCaracter(nome='obsFisco', codigo='Z08', propriedade='xCampo', tamanho=[1, 20], raiz='/')
        self.xTexto = TagCaracter(nome='xTexto', codigo='Z09', tamanho=[1, 60], raiz='//obsFisco')

    def get_xml(self):
        if not (self.xCampo.valor or self.xTexto.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += self.xCampo.xml
        xml += self.xTexto.xml
        xml += '</obsFisco>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xCampo.xml = arquivo
            self.xTexto.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.xCampo.valor or self.xTexto.valor):
            return ''

        txt = 'Z07|'
        txt += self.xCampo.txt + '|'
        txt += self.xTexto.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class ObsCont(XMLNFe):
    def __init__(self):
        super(ObsCont, self).__init__()
        self.xCampo = TagCaracter(nome='obsCont', codigo='Z05', propriedade='xCampo', tamanho=[1, 20], raiz='/')
        self.xTexto = TagCaracter(nome='xTexto', codigo='Z06', tamanho=[1, 60], raiz='//obsCont')

    def get_xml(self):
        if not (self.xCampo.valor or self.xTexto.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += self.xCampo.xml
        xml += self.xTexto.xml
        xml += '</obsCont>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xCampo.xml = arquivo
            self.xTexto.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.xCampo.valor or self.xTexto.valor):
            return ''

        txt = 'Z04|'
        txt += self.xCampo.txt + '|'
        txt += self.xTexto.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class InfAdic(XMLNFe):
    def __init__(self):
        super(InfAdic, self).__init__()
        self.infAdFisco = TagCaracter(nome='infAdFisco', codigo='Z02', tamanho=[1,  256], raiz='//NFe/infNFe/infAdic', obrigatorio=False)
        self.infCpl     = TagCaracter(nome='infCpl'    , codigo='Z03', tamanho=[1, 5000], raiz='//NFe/infNFe/infAdic', obrigatorio=False)
        self.obsCont    = []
        self.obsFisco   = []
        self.procRef    = []

    def get_xml(self):
        if not (self.infAdFisco.valor or self.infCpl.valor or len(self.obsCont) or len(self.obsFisco) or len(self.procRef)):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<infAdic>'
        xml += self.infAdFisco.xml
        xml += self.infCpl.xml

        for o in self.obsCont:
            xml += o.xml

        for o in self.obsFisco:
            xml += o.xml

        for p in self.procRef:
            xml += p.xml

        xml += '</infAdic>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infAdFisco.xml = arquivo
            self.infCpl.xml     = arquivo
            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.obsCont = self.le_grupo('//NFe/infNFe/infAdic/obsCont', ObsCont)
            self.obsFisco = self.le_grupo('//NFe/infNFe/infAdic/obsFisco', ObsFisco)
            self.procRef = self.le_grupo('//NFe/infNFe/infAdic/procRef', ProcRef)

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.infAdFisco.valor or self.infCpl.valor or len(self.obsCont) or len(self.obsFisco) or len(self.procRef)):
            return ''

        txt = 'Z|'
        txt += self.infAdFisco.txt + '|'
        txt += self.infCpl.txt + '|'
        txt += '\n'

        for o in self.obsCont:
            txt += o.txt

        for o in self.obsFisco:
            txt += o.txt

        for p in self.procRef:
            txt += p.txt

        return txt

    txt = property(get_txt)


class Dup(XMLNFe):
    def __init__(self):
        super(Dup, self).__init__()
        self.nDup  = TagCaracter(nome='nDup', codigo='Y08', tamanho=[1, 60],                        raiz='//dup', obrigatorio=False)
        self.dVenc = TagData(nome='dVenc'   , codigo='Y09',                                         raiz='//dup', obrigatorio=False)
        self.vDup  = TagDecimal(nome='vDup' , codigo='Y10', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//dup', obrigatorio=False)

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

    def get_txt(self):
        if not (self.nDup.valor or self.dVenc.valor or self.vDup.valor):
            return ''

        txt = 'Y07|'
        txt += self.nDup.txt + '|'
        txt += self.dVenc.txt + '|'
        txt += self.vDup.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class Fat(XMLNFe):
    def __init__(self):
        super(Fat, self).__init__()
        self.nFat  = TagCaracter(nome='nFat', codigo='Y03', tamanho=[1, 60],                        raiz='//NFe/infNFe/cobr/fat', obrigatorio=False)
        self.vOrig = TagDecimal(nome='vOrig', codigo='Y04', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/cobr/fat', obrigatorio=False)
        self.vDesc = TagDecimal(nome='vDesc', codigo='Y05', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/cobr/fat', obrigatorio=False)
        self.vLiq  = TagDecimal(nome='vLiq' , codigo='Y06', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/cobr/fat', obrigatorio=False)

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

    def get_txt(self):
        if not (self.nFat.valor or self.vOrig.valor or self.vDesc.valor or self.vLiq.valor):
            return ''

        txt = 'Y02|'
        txt += self.nFat.txt + '|'
        txt += self.vOrig.txt + '|'
        txt += self.vDesc.txt + '|'
        txt += self.vLiq.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


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
            self.dup = self.le_grupo('//NFe/infNFe/cobr/dup', Dup)

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.fat.xml or len(self.dup)):
            return ''

        txt = 'Y|\n'
        txt += self.fat.txt

        for d in self.dup:
            txt += d.txt

        return txt

    txt = property(get_txt)


class Lacres(XMLNFe):
    def __init__(self):
        super(Lacres, self).__init__()
        self.nLacre = TagCaracter(nome='nLacre', codigo='X34', tamanho=[1, 60], raiz='//lacres')

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

    def get_txt(self):
        if not self.nLacre.valor:
            return ''

        txt = 'X33|'
        txt += self.nLacre.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class Vol(XMLNFe):
    #
    # No caso dos volumes, se o valor da quantidade, peso bruto ou líquido for zero ou inexistente
    # não imprime os valores no DANFE
    #
    class TagInteiroVolume(TagInteiro):
        def formato_danfe(self):
            if not self._valor_inteiro:
                return ''
            else:
                return super(Vol.TagInteiroVolume, self).formato_danfe()

    class TagDecimalVolume(TagDecimal):
        def formato_danfe(self):
            if not self._valor_decimal:
                return ''
            else:
                return super(Vol.TagDecimalVolume, self).formato_danfe()

    def __init__(self, xml=None):
        super(Vol, self).__init__()
        self.qVol   = TagInteiro(nome='qVol'  , codigo='X27', tamanho=[1, 15], raiz='//vol', obrigatorio=False)
        #self.qVol   = self.TagInteiroVolume(nome='qVol'  , codigo='X27', tamanho=[1, 15], raiz='//vol', obrigatorio=False)
        self.esp    = TagCaracter(nome='esp'  , codigo='X28', tamanho=[1, 60], raiz='//vol', obrigatorio=False)
        self.marca  = TagCaracter(nome='marca', codigo='X29', tamanho=[1, 60], raiz='//vol', obrigatorio=False)
        self.nVol   = TagCaracter(nome='nVol' , codigo='X30', tamanho=[1, 60], raiz='//vol', obrigatorio=False)
        self.pesoL  = TagDecimal(nome='pesoL' , codiog='X31', tamanho=[1, 15, 1], decimais=[0, 3, 3], raiz='//vol', obrigatorio=False)
        self.pesoB  = TagDecimal(nome='pesoB' , codiog='X32', tamanho=[1, 15, 1], decimais=[0, 3, 3], raiz='//vol', obrigatorio=False)
        #self.pesoL  = self.TagDecimalVolume(nome='pesoL' , codiog='X31', tamanho=[1, 15, 1], decimais=[0, 3, 3], raiz='//vol', obrigatorio=False)
        #self.pesoB  = self.TagDecimalVolume(nome='pesoB' , codiog='X32', tamanho=[1, 15, 1], decimais=[0, 3, 3], raiz='//vol', obrigatorio=False)
        self.lacres = []

    def get_xml(self):
        if not (self.qVol.valor or self.esp.valor or self.marca.valor or self.nVol.valor or self.pesoL.valor or self.pesoB.valor or len(self.lacres)):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<vol>'
        xml += self.qVol.xml
        xml += self.esp.xml
        xml += self.marca.xml
        xml += self.nVol.xml
        xml += self.pesoL.xml
        xml += self.pesoB.xml

        for l in self.lacres:
            xml += l.xml

        xml += '</vol>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.qVol.xml = arquivo
            self.esp.xml = arquivo
            self.marca.xml = arquivo
            self.nVol.xml = arquivo
            self.pesoL.xml = arquivo
            self.pesoB.xml = arquivo
            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.lacres = self.le_grupo('//vol/lacres', Lacres)

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.qVol.valor or self.esp.valor or self.marca.valor or self.nVol.valor or self.pesoL.valor or self.pesoB.valor or len(self.lacres)):
            return ''

        txt = 'X26|'
        txt += self.qVol.txt + '|'
        txt += self.esp.txt + '|'
        txt += self.marca.txt + '|'
        txt += self.nVol.txt + '|'
        txt += self.pesoL.txt + '|'
        txt += self.pesoB.txt + '|'
        txt += '\n'

        for l in self.lacres:
            txt += l.txt

        return txt

    txt = property(get_txt)


class Reboque(XMLNFe):
    def __init__(self):
        super(Reboque, self).__init__()
        self.placa = TagCaracter(nome='placa', codigo='X23', tamanho=[1,  8], raiz='//reboque')
        self.UF    = TagCaracter(nome='UF'   , codigo='X24', tamanho=[2,  2], raiz='//reboque')
        self.RNTC  = TagCaracter(nome='RNTC' , codigo='X25', tamanho=[1, 20], raiz='//reboque', obrigatorio=False)

    def get_xml(self):
        if not (self.placa.valor or self.UF.valor or self.RNTC.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<reboque>'
        xml += self.placa.xml
        xml += self.UF.xml
        xml += self.RNTC.xml
        xml += '</reboque>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.placa.xml = arquivo
            self.UF.xml    = arquivo
            self.RNTC.xml  = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.placa.valor or self.UF.valor or self.RNTC.valor):
            return ''

        txt = 'X22|'
        txt += self.placa.txt + '|'
        txt += self.UF.txt + '|'
        txt += self.RNTC.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class VeicTransp(XMLNFe):
    def __init__(self):
        super(VeicTransp, self).__init__()
        self.placa = TagCaracter(nome='placa', codigo='X19', tamanho=[1,  8], raiz='//NFe/infNFe/transp/veicTransp')
        self.UF    = TagCaracter(nome='UF'   , codigo='X20', tamanho=[2,  2], raiz='//NFe/infNFe/transp/veicTransp')
        self.RNTC  = TagCaracter(nome='RNTC' , codigo='X21', tamanho=[1, 20], raiz='//NFe/infNFe/transp/veicTransp', obrigatorio=False)

    def get_xml(self):
        if not (self.placa.valor or self.UF.valor or self.RNTC.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<veicTransp>'
        xml += self.placa.xml
        xml += self.UF.xml
        xml += self.RNTC.xml
        xml += '</veicTransp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.placa.xml = arquivo
            self.UF.xml    = arquivo
            self.RNTC.xml  = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.placa.valor or self.UF.valor or self.RNTC.valor):
            return ''

        txt = 'X18|'
        txt += self.placa.txt + '|'
        txt += self.UF.txt + '|'
        txt += self.RNTC.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class RetTransp(XMLNFe):
    def __init__(self):
        super(RetTransp, self).__init__()
        self.vServ    = TagDecimal(nome='vServ'   , codigo='X12', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/transp/retTransp')
        self.vBCRet   = TagDecimal(nome='vBCRet'  , codigo='X13', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/transp/retTransp')
        self.pICMSRet = TagDecimal(nome='vICMSRet', codigo='X14', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/transp/retTransp')
        self.vICMSRet = TagDecimal(nome='vICMSRet', codigo='X15', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/transp/retTransp')
        self.CFOP     = TagInteiro(nome='CFOP'    , codigo='X16', tamanho=[4,  4, 4],                     raiz='//NFe/infNFe/transp/retTransp')
        self.cMunFG   = TagInteiro(nome='cMunFG'  , codigo='X17', tamanho=[7,  7, 7],                     raiz='//NFe/infNFe/transp/retTransp')

    def get_xml(self):
        if not (self.vServ.valor or self.vBCRet.valor or self.pICMSRet.valor or self.vICMSRet.valor or self.CFOP.valor or self.cMunFG.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<retTransp>'
        xml += self.vServ.xml
        xml += self.vBCRet.xml
        xml += self.pICMSRet.xml
        xml += self.vICMSRet.xml
        xml += self.CFOP.xml
        xml += self.cMunFG.xml
        xml += '</retTransp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vServ.xml    = arquivo
            self.vBCRet.xml   = arquivo
            self.pICMSRet.xml = arquivo
            self.vICMSRet.xml = arquivo
            self.CFOP.xml     = arquivo
            self.cMunFG.xml   = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.vServ.valor or self.vBCRet.valor or self.pICMSRet.valor or self.vICMSRet.valor or self.CFOP.valor or self.cMunFG.valor):
            return ''

        txt = 'X11|'
        txt += self.vServ.txt + '|'
        txt += self.vBCRet.txt + '|'
        txt += self.pICMSRet.txt + '|'
        txt += self.vICMSRet.txt + '|'
        txt += self.CFOP.txt + '|'
        txt += self.cMunFG.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class Transporta(XMLNFe):
    def __init__(self):
        super(Transporta, self).__init__()
        self.CNPJ   = TagCaracter(nome='CNPJ'  , codigo='X04', tamanho=[14, 14], raiz='//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.CPF    = TagCaracter(nome='CPF'   , codigo='X05', tamanho=[11, 11], raiz='//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.xNome  = TagCaracter(nome='xNome' , codigo='X06', tamanho=[ 1, 60], raiz='//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.IE     = TagCaracter(nome='IE'    , codigo='X07', tamanho=[ 2, 14], raiz='//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.xEnder = TagCaracter(nome='xEnder', codigo='X08', tamanho=[ 1, 60], raiz='//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.xMun   = TagCaracter(nome='xMun'  , codigo='X09', tamanho=[ 1, 60], raiz='//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.UF     = TagCaracter(nome='UF'    , codigo='X10', tamanho=[ 2,  2], raiz='//NFe/infNFe/transp/transporta', obrigatorio=False)

    def get_xml(self):
        if not (self.CNPJ.valor or self.CPF.valor or self.xNome.valor or self.IE.valor or self.xEnder.valor or self.xMun.valor or self.UF.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<transporta>'
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.xNome.xml
        xml += self.IE.xml
        xml += self.xEnder.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += '</transporta>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml   = arquivo
            self.CPF.xml    = arquivo
            self.xNome.xml  = arquivo
            self.IE.xml     = arquivo
            self.xEnder.xml = arquivo
            self.xMun.xml   = arquivo
            self.UF.xml     = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.CNPJ.valor or self.CPF.valor or self.xNome.valor or self.IE.valor or self.xEnder.valor or self.xMun.valor or self.UF.valor):
            return ''

        txt = 'X03|'
        txt += self.xNome.txt + '|'
        txt += self.IE.txt + '|'
        txt += self.xEnder.txt + '|'
        txt += self.xMun.txt + '|'
        txt += self.UF.txt + '|'
        txt += '\n'

        if self.CPF.valor:
            txt += 'X05|' + self.CPF.txt + '|\n'
        else:
            txt += 'X04|' + self.CNPJ.txt + '|\n'

        return txt

    txt = property(get_txt)


class Transp(XMLNFe):
    def __init__(self):
        super(Transp, self).__init__()
        self.modFrete   = TagInteiro(nome='modFrete', codigo='X02', tamanho=[ 1, 1, 1], raiz='//NFe/infNFe/transp')
        self.transporta = Transporta()
        self.retTransp  = RetTransp()
        self.veicTransp = VeicTransp()
        self.reboque    = []
        self.vol        = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<transp>'
        xml += self.modFrete.xml
        xml += self.transporta.xml
        xml += self.retTransp.xml
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
            self.reboque = self.le_grupo('//NFe/infNFe/transp/reboque', Reboque)
            self.vol = self.le_grupo('//NFe/infNFe/transp/vol', Vol)

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


class RetTrib(XMLNFe):
    def __init__(self):
        super(RetTrib, self).__init__()
        self.vRetPIS    = TagDecimal(nome='vRetPIS'   , codigo='W24', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vRetCOFINS = TagDecimal(nome='vRetCOFINS', codigo='W25', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vRetCSLL   = TagDecimal(nome='vRetCSLL'  , codigo='W26', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vBCIRRF    = TagDecimal(nome='vBCIRRF'   , codigo='W27', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vIRRF      = TagDecimal(nome='vIRRF'     , codigo='W28', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vBCRetPrev = TagDecimal(nome='vBCRetPrev', codigo='W29', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vRetPrev   = TagDecimal(nome='vRetPrev'  , codigo='W30', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/retTrib', obrigatorio=False)

    def get_xml(self):
        if not (self.vRetPIS.valor or self.vRetCOFINS.valor or self.vRetCSLL.valor or self.vBCIRRF.valor or self.vIRRF.valor or self.vBCRetPrev.valor or self.vRetPrev.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<retTrib>'
        xml += self.vRetPIS.xml
        xml += self.vRetCOFINS.xml
        xml += self.vRetCSLL.xml
        xml += self.vBCIRRF.xml
        xml += self.vIRRF.xml
        xml += self.vBCRetPrev.xml
        xml += self.vRetPrev.xml
        xml += '</retTrib>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vRetPIS.xml    = arquivo
            self.vRetCOFINS.xml = arquivo
            self.vRetCSLL.xml   = arquivo
            self.vBCIRRF.xml    = arquivo
            self.vIRRF.xml      = arquivo
            self.vBCRetPrev.xml = arquivo
            self.vRetPrev.xml   = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.vRetPIS.valor or self.vRetCOFINS.valor or self.vRetCSLL.valor or self.vBCIRRF.valor or self.vIRRF.valor or self.vBCRetPrev.valor or self.vRetPrev.valor):
            return ''

        txt = 'W23|'
        txt += self.vRetPIS.txt + '|'
        txt += self.vRetCOFINS.txt + '|'
        txt += self.vRetCSLL.txt + '|'
        txt += self.vBCIRRF.txt + '|'
        txt += self.vIRRF.txt + '|'
        txt += self.vBCRetPrev.txt + '|'
        txt += self.vRetPrev.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class ISSQNTot(XMLNFe):
    def __init__(self):
        super(ISSQNTot, self).__init__()
        self.vServ   = TagDecimal(nome='vServ'  , codigo='W18', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vBC     = TagDecimal(nome='vBC'    , codigo='W19', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vISS    = TagDecimal(nome='vISS'   , codigo='W20', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vPIS    = TagDecimal(nome='vPIS'   , codigo='W21', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vCOFINS = TagDecimal(nome='vCOFINS', codigo='W22', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ISSQNtot', obrigatorio=False)

    def get_xml(self):
        if not (self.vServ.valor or self.vBC.valor or self.vISS.valor or self.vPIS.valor or self.vCOFINS.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ISSQNtot>'
        xml += self.vServ.xml
        xml += self.vBC.xml
        xml += self.vISS.xml
        xml += self.vPIS.xml
        xml += self.vCOFINS.xml
        xml += '</ISSQNtot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vServ.xml   = arquivo
            self.vBC.xml     = arquivo
            self.vISS.xml    = arquivo
            self.vPIS.xml    = arquivo
            self.vCOFINS.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.vServ.valor or self.vBC.valor or self.vISS.valor or self.vPIS.valor or self.vCOFINS.valor):
            return ''

        txt = 'W17|'
        txt += self.vServ.txt + '|'
        txt += self.vBC.txt + '|'
        txt += self.vISS.txt + '|'
        txt += self.vPIS.txt + '|'
        txt += self.vCOFINS.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class ICMSTot(XMLNFe):
    def __init__(self):
        super(ICMSTot, self).__init__()
        self.vBC     = TagDecimal(nome='vBC'    , codigo='W03', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vICMS   = TagDecimal(nome='vICMS'  , codigo='W04', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vBCST   = TagDecimal(nome='vBCST'  , codigo='W05', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vST     = TagDecimal(nome='vST'    , codigo='W06', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vProd   = TagDecimal(nome='vProd'  , codigo='W07', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vFrete  = TagDecimal(nome='vFrete' , codigo='W08', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vSeg    = TagDecimal(nome='vSeg'   , codigo='W09', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vDesc   = TagDecimal(nome='vDesc'  , codigo='W10', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vII     = TagDecimal(nome='vII'    , codigo='W11', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vIPI    = TagDecimal(nome='vIPI'   , codigo='W12', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vPIS    = TagDecimal(nome='vPIS'   , codigo='W13', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vCOFINS = TagDecimal(nome='vCOFINS', codigo='W14', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vOutro  = TagDecimal(nome='vOutro' , codigo='W15', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vNF     = TagDecimal(nome='vNF'    , codigo='W16', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ICMSTot')

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

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'W02|'
        txt += self.vBC.txt + '|'
        txt += self.vICMS.txt + '|'
        txt += self.vBCST.txt + '|'
        txt += self.vST.txt + '|'
        txt += self.vProd.txt + '|'
        txt += self.vFrete.txt + '|'
        txt += self.vSeg.txt + '|'
        txt += self.vDesc.txt + '|'
        txt += self.vII.txt + '|'
        txt += self.vIPI.txt + '|'
        txt += self.vPIS.txt + '|'
        txt += self.vCOFINS.txt + '|'
        txt += self.vOutro.txt + '|'
        txt += self.vNF.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class Total(XMLNFe):
    def __init__(self):
        super(Total, self).__init__()
        self.ICMSTot = ICMSTot()
        self.ISSQNTot = ISSQNTot()
        self.retTrib  = RetTrib()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<total>'
        xml += self.ICMSTot.xml
        xml += self.ISSQNTot.xml
        xml += self.retTrib.xml
        xml += '</total>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ICMSTot.xml  = arquivo
            self.ISSQNTot.xml = arquivo
            self.retTrib.xml  = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'W|\n'
        txt += self.ICMSTot.txt
        txt += self.ISSQNTot.txt
        txt += self.retTrib.txt
        return txt

    txt = property(get_txt)


class Entrega(XMLNFe):
    def __init__(self):
        super(Entrega, self).__init__()
        self.CNPJ    = TagCaracter(nome='CNPJ'   , codigo='G02', tamanho=[14, 14]   , raiz='//NFe/infNFe/entrega')
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='G03', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/entrega')
        self.nro     = TagCaracter(nome='nro'    , codigo='G04', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/entrega')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='G05', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/entrega', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='G06', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/entrega')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='G07', tamanho=[ 7,  7, 7], raiz='//NFe/infNFe/entrega')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='G08', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/entrega')
        self.UF      = TagCaracter(nome='UF'     , codigo='G09', tamanho=[ 2,  2]   , raiz='//NFe/infNFe/entrega')


    def get_xml(self):
        if not len(self.CNPJ.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<entrega>'
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
            self.CNPJ.xml = arquivo
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
        return txt

    txt = property(get_txt)


class Retirada(XMLNFe):
    def __init__(self):
        super(Retirada, self).__init__()
        self.CNPJ    = TagCaracter(nome='CNPJ'   , codigo='F01', tamanho=[14, 14]   , raiz='//NFe/infNFe/retirada')
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='F02', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/retirada')
        self.nro     = TagCaracter(nome='nro'    , codigo='F03', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/retirada')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='F04', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/retirada', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='F05', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/retirada')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='F06', tamanho=[ 7,  7, 7], raiz='//NFe/infNFe/retirada')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='F07', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/retirada')
        self.UF      = TagCaracter(nome='UF'     , codigo='F08', tamanho=[ 2,  2]   , raiz='//NFe/infNFe/retirada')


    def get_xml(self):
        if not len(self.CNPJ.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<retirada>'
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
            self.CNPJ.xml = arquivo
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
        return txt

    txt = property(get_txt)


class EnderDest(XMLNFe):
    def __init__(self):
        super(EnderDest, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='E06', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/dest/enderDest')
        self.nro     = TagCaracter(nome='nro'    , codigo='E07', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/dest/enderDest')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='E08', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='E09', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/dest/enderDest')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='E10', tamanho=[ 7,  7, 7], raiz='//NFe/infNFe/dest/enderDest')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='E11', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/dest/enderDest')
        self.UF      = TagCaracter(nome='UF'     , codigo='E12', tamanho=[ 2,  2]   , raiz='//NFe/infNFe/dest/enderDest')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='E13', tamanho=[ 8,  8, 8], raiz='//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.cPais   = TagCaracter(nome='cPais'  , codigo='E14', tamanho=[ 4,  4, 4], raiz='//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , codigo='E15', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.fone    = TagInteiro(nome='fone'    , codigo='E16', tamanho=[ 1, 10]   , raiz='//NFe/infNFe/dest/enderDest', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderDest>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += self.CEP.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += self.fone.xml
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
            self.UF.xml      = arquivo
            self.CEP.xml     = arquivo
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo
            self.fone.xml    = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'E05|'
        txt += self.xLgr.txt + '|'
        txt += self.nro.txt + '|'
        txt += self.xCpl.txt + '|'
        txt += self.xBairro.txt + '|'
        txt += self.cMun.txt + '|'
        txt += self.xMun.txt + '|'
        txt += self.UF.txt + '|'
        txt += self.CEP.txt + '|'
        txt += self.cPais.txt + '|'
        txt += self.xPais.txt + '|'
        txt += self.fone.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class Dest(XMLNFe):
    def __init__(self):
        super(Dest, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='E02', tamanho=[0 , 14]   , raiz='//NFe/infNFe/dest', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , codigo='E03', tamanho=[11, 11]   , raiz='//NFe/infNFe/dest', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='E04', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/dest')
        self.enderDest = EnderDest()
        self.IE        = TagCaracter(nome='IE'   , codigo='E17', tamanho=[ 2, 14]   , raiz='//NFe/infNFe/dest')
        self.ISUF      = TagCaracter(nome='ISUF' , codigo='E18', tamanho=[ 9,  9]   , raiz='//NFe/infNFe/dest', obrigatorio=False)

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

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'E|'
        txt += self.xNome.txt + '|'
        txt += self.IE.txt + '|'
        txt += self.ISUF.txt + '|'
        txt += '\n'

        if self.CPF.valor:
            txt += 'E03|' + self.CPF.txt + '|\n'
        else:
            txt += 'E02|' + self.CNPJ.txt + '|\n'

        txt += self.enderDest.txt
        return txt

    txt = property(get_txt)


class Avulsa(XMLNFe):
    def __init__(self):
        super(Avulsa, self).__init__()
        self.CNPJ    = TagCaracter(nome='CNPJ'   , codigo='D02', tamanho=[14, 14], raiz='//NFe/infNFe/avulsa')
        self.xOrgao  = TagCaracter(nome='xOrgao' , codigo='D03', tamanho=[ 1, 60], raiz='//NFe/infNFe/avulsa')
        self.matr    = TagCaracter(nome='matr'   , codigo='D04', tamanho=[ 1, 60], raiz='//NFe/infNFe/avulsa')
        self.xAgente = TagCaracter(nome='xAgente', codigo='D05', tamanho=[ 1, 60], raiz='//NFe/infNFe/avulsa')
        self.fone    = TagInteiro(nome='fone'    , codigo='D06', tamanho=[ 1, 10], raiz='//NFe/infNFe/avulsa')
        self.UF      = TagCaracter(nome='UF'     , codigo='D07', tamanho=[ 2,  2], raiz='//NFe/infNFe/avulsa')
        self.nDAR    = TagCaracter(nome='nDAR'   , codigo='D08', tamanho=[ 1, 60], raiz='//NFe/infNFe/avulsa')
        self.dEmi    = TagData(nome='dEmi'       , codigo='D09',                   raiz='//NFe/infNFe/avulsa')
        self.vDAR    = TagDecimal(nome='vDAR'    , codigo='D10', tamanho=[ 1, 15], decimais=[0, 2, 2], raiz='//NFe/infNFe/avulsa')
        self.repEmi  = TagCaracter(nome='repEmi' , codigo='D11', tamanho=[ 1, 60], raiz='//NFe/infNFe/avulsa')
        self.dPag    = TagData(nome='dPag'       , codigo='D12',                   raiz='//NFe/infNFe/avulsa', obrigatorio=False)

    def get_xml(self):
        if not len(self.CNPJ.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<avulsa>'
        xml += self.CNPJ.xml
        xml += self.xOrgao.xml
        xml += self.matr.xml
        xml += self.xAgente.xml
        xml += self.fone.xml
        xml += self.UF.xml
        xml += self.nDAR.xml
        xml += self.dEmi.xml
        xml += self.vDAR.xml
        xml += self.repEmi.xml
        xml += self.dPag.xml
        xml += '</avulsa>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml    = arquivo
            self.xOrgao.xml  = arquivo
            self.matr.xml    = arquivo
            self.xAgente.xml = arquivo
            self.fone.xml    = arquivo
            self.UF.xml      = arquivo
            self.nDAR.xml    = arquivo
            self.dEmi.xml    = arquivo
            self.vDAR.xml    = arquivo
            self.repEmi.xml  = arquivo
            self.dPag.xml    = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not len(self.CNPJ.valor):
            return ''

        txt = 'D|'
        txt += self.CNPJ.txt + '|'
        txt += self.xOrgao.txt + '|'
        txt += self.matr.txt + '|'
        txt += self.xAgente.txt + '|'
        txt += self.fone.txt + '|'
        txt += self.UF.txt + '|'
        txt += self.nDAR.txt + '|'
        txt += self.dEmi.txt + '|'
        txt += self.vDAR.txt + '|'
        txt += self.repEmi.txt + '|'
        txt += self.dPag.txt + '|'
        txt += '\n'

        return txt

    txt = property(get_txt)


class EnderEmit(XMLNFe):
    def __init__(self):
        super(EnderEmit, self).__init__()
        self.xLgr    = TagCaracter(nome='xLgr'   , codigo='C06', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/emit/enderEmit')
        self.nro     = TagCaracter(nome='nro'    , codigo='C07', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/emit/enderEmit')
        self.xCpl    = TagCaracter(nome='xCpl'   , codigo='C08', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/emit/enderEmit', obrigatorio=False)
        self.xBairro = TagCaracter(nome='xBairro', codigo='C09', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/emit/enderEmit')
        self.cMun    = TagInteiro(nome='cMun'    , codigo='C10', tamanho=[ 7,  7, 7], raiz='//NFe/infNFe/emit/enderEmit')
        self.xMun    = TagCaracter(nome='xMun'   , codigo='C11', tamanho=[ 2, 60]   , raiz='//NFe/infNFe/emit/enderEmit')
        self.UF      = TagCaracter(nome='UF'     , codigo='C12', tamanho=[ 2,  2]   , raiz='//NFe/infNFe/emit/enderEmit')
        self.CEP     = TagCaracter(nome='CEP'    , codigo='C13', tamanho=[ 8,  8, 8], raiz='//NFe/infNFe/emit/enderEmit', obrigatorio=False)
        self.cPais   = TagCaracter(nome='cPais'  , codigo='C14', tamanho=[ 4,  4, 4], raiz='//NFe/infNFe/emit/enderEmit', obrigatorio=False)
        self.xPais   = TagCaracter(nome='xPais'  , codigo='C15', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/emit/enderEmit', obrigatorio=False)
        self.fone    = TagInteiro(nome='fone'    , codigo='C16', tamanho=[ 1, 10]   , raiz='//NFe/infNFe/emit/enderEmit', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<enderEmit>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += self.CEP.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
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
            self.UF.xml      = arquivo
            self.CEP.xml     = arquivo
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo
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
        txt += self.UF.txt + '|'
        txt += self.CEP.txt + '|'
        txt += self.cPais.txt + '|'
        txt += self.xPais.txt + '|'
        txt += self.fone.txt + '|'
        txt += '\n'

        return txt

    txt = property(get_txt)


class Emit(XMLNFe):
    def __init__(self):
        super(Emit, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , codigo='C02' , tamanho=[14, 14], raiz='//NFe/infNFe/emit', obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , codigo='C02a', tamanho=[11, 11], raiz='//NFe/infNFe/emit', obrigatorio=False)
        self.xNome     = TagCaracter(nome='xNome', codigo='C03' , tamanho=[ 2, 60], raiz='//NFe/infNFe/emit')
        self.xFant     = TagCaracter(nome='xFant', codigo='C04' , tamanho=[ 1, 60], raiz='//NFe/infNFe/emit', obrigatorio=False)
        self.enderEmit = EnderEmit()
        self.IE        = TagCaracter(nome='IE'   , codigo='C17' , tamanho=[ 2, 14], raiz='//NFe/infNFe/emit', obrigatorio=False)
        self.IEST      = TagCaracter(nome='IEST' , codigo='C18' , tamanho=[ 2, 14], raiz='//NFe/infNFe/emit', obrigatorio=False)
        self.IM        = TagCaracter(nome='IM'   , codigo='C19' , tamanho=[ 1, 15], raiz='//NFe/infNFe/emit', obrigatorio=False)
        self.CNAE      = TagCaracter(nome='CNAE' , codigo='C20' , tamanho=[ 7,  7], raiz='//NFe/infNFe/emit', obrigatorio=False)


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

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = 'C|'
        txt += self.xNome.txt + '|'
        txt += self.xFant.txt + '|'
        txt += self.IE.txt + '|'
        txt += self.IEST.txt + '|'
        txt += self.IM.txt + '|'
        txt += self.CNAE.txt + '|'
        txt += '\n'

        if self.CNPJ.valor:
            txt += 'C02|' + self.CNPJ.txt + '|\n'

        else:
            txt += 'C02a|' + self.CPF.txt + '|\n'

        txt += self.enderEmit.txt

        return txt

    txt = property(get_txt)


class RefNF(XMLNFe):
    def __init__(self):
        super(RefNF, self).__init__()
        self.cUF   = TagInteiro(nome='cUF'  , codigo='B15', tamanho=[ 2,  2, 2], raiz='//NFref/refNF')
        self.AAMM  = TagCaracter(nome='AAMM', codigo='B16', tamanho=[ 4,  4, 4], raiz='//NFref/refNF')
        self.CNPJ  = TagCaracter(nome='CNPJ', codigo='B17', tamanho=[14, 14]   , raiz='//NFref/refNF')
        self.mod   = TagCaracter(nome='mod' , codigo='B18', tamanho=[ 2,  2, 2], raiz='//NFref/refNF')
        self.serie = TagInteiro(nome='serie', codigo='B19', tamanho=[ 1,  3, 1], raiz='//NFref/refNF')
        self.nNF   = TagInteiro(nome='nNF'  , codigo='B20', tamanho=[ 1,  9, 1], raiz='//NFref/refNF')

    def get_xml(self):
        if not (self.cUF.valor or self.AAMM.valor or self.CNPJ.valor or self.mod.valor or self.serie.valor or self.nNF.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<refNF>'
        xml += self.cUF.xml
        xml += self.AAMM.xml
        xml += self.CNPJ.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNF.xml
        xml += '</refNF>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml   = arquivo
            self.AAMM.xml  = arquivo
            self.CNPJ.xml  = arquivo
            self.mod.xml   = arquivo
            self.serie.xml = arquivo
            self.nNF.xml   = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.cUF.valor or self.AAMM.valor or self.CNPJ.valor or self.mod.valor or self.serie.valor or self.nNF.valor):
            return ''

        txt = 'B14|'
        txt += self.cUF.txt + '|'
        txt += self.AAMM.txt + '|'
        txt += self.CNPJ.txt + '|'
        txt += self.mod.txt + '|'
        txt += self.serie.txt + '|'
        txt += self.nNF.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)

class NFRef(XMLNFe):
    def __init__(self):
        super(NFRef, self).__init__()
        self.refNFe = TagCaracter(nome='refNFe', codigo='B13', tamanho=[44, 44], raiz='//NFref', obrigatorio=False)
        self.refNF  = RefNF()

    def get_xml(self):
        if not (self.refNFe.valor or self.refNF.xml):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<NFref>'
        xml += self.refNFe.xml
        xml += self.refNF.xml
        xml += '</NFref>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.refNFe.xml = arquivo
            self.refNF.xml  = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.refNFe.valor or self.refNF.xml):
            return ''

        if self.refNFe.valor:
            txt = 'B13|' + self.refNFe.txt + '|\n'
        else:
            txt = self.refNF.txt

        return txt

    txt = property(get_txt)


class Ide(XMLNFe):
    def __init__(self):
        super(Ide, self).__init__()
        self.cUF     = TagInteiro(nome='cUF'     , codigo='B02', tamanho=[ 2,  2, 2], raiz='//NFe/infNFe/ide')
        self.cNF     = TagCaracter(nome='cNF'    , codigo='B03', tamanho=[ 9,  9, 9], raiz='//NFe/infNFe/ide')
        self.natOp   = TagCaracter(nome='natOp'  , codigo='B04', tamanho=[ 1, 60]   , raiz='//NFe/infNFe/ide')
        self.indPag  = TagInteiro(nome='indPag'  , codigo='B05', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide')
        self.mod     = TagCaracter(nome='mod'     , codigo='B06', tamanho=[ 2,  2, 2], raiz='//NFe/infNFe/ide', valor=55)
        self.serie   = TagInteiro(nome='serie'   , codigo='B07', tamanho=[ 1,  3, 1], raiz='//NFe/infNFe/ide')
        self.nNF     = TagInteiro(nome='nNF'     , codigo='B08', tamanho=[ 1,  9, 1], raiz='//NFe/infNFe/ide')
        self.dEmi    = TagData(nome='dEmi'       , codigo='B09',                      raiz='//NFe/infNFe/ide')
        self.dSaiEnt = TagData(nome='dSaiEnt'    , codigo='B10',                      raiz='//NFe/infNFe/ide', obrigatorio=False)
        self.tpNF    = TagInteiro(nome='tpNF'    , codigo='B11', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide', valor=1)
        self.cMunFG  = TagInteiro(nome='cMunFG'  , codigo='B12', tamanho=[ 7,  7, 7], raiz='//NFe/infNFe/ide')
        self.NFref   = []
        self.tpImp   = TagInteiro(nome='tpImp'   , codigo='B21', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide', valor=1)
        self.tpEmis  = TagInteiro(nome='tpEmis'  , codigo='B22', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide', valor=1)
        self.cDV     = TagInteiro(nome='cDV'     , codigo='B23', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide')
        self.tpAmb   = TagInteiro(nome='tpAmb'   , codigo='B24', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide', valor=2)
        self.finNFe  = TagInteiro(nome='finNFe'  , codigo='B25', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide', valor=1)
        self.procEmi = TagInteiro(nome='procEmi' , codigo='B26', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide')
        self.verProc = TagCaracter(nome='verProc', codigo='B27', tamanho=[ 1, 20]   , raiz='//NFe/infNFe/ide')
        self.hSaiEnt = TagHora(nome='hSaiEnt'    , codigo=''   ,                      raiz='//NFe/infNFe/ide', obrigatorio=False)

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
        xml += self.tpNF.xml
        xml += self.cMunFG.xml

        for nr in self.NFref:
            xml += nr.xml

        xml += self.tpImp.xml
        xml += self.tpEmis.xml
        xml += self.cDV.xml
        xml += self.tpAmb.xml
        xml += self.finNFe.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
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
        txt += self.tpNF.txt + '|'
        txt += self.cMunFG.txt + '|'
        txt += self.tpImp.txt + '|'
        txt += self.tpEmis.txt + '|'
        txt += self.cDV.txt + '|'
        txt += self.tpAmb.txt + '|'
        txt += self.finNFe.txt + '|'
        txt += self.procEmi.txt + '|'
        txt += self.verProc.txt + '|'
        txt += '\n'

        for nr in self.NFref:
            txt += nr.txt

        return txt

    txt = property(get_txt)


class InfNFe(XMLNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.versao   = TagDecimal(nome='infNFe' , codigo='A01', propriedade='versao', raiz='//NFe', namespace=NAMESPACE_NFE, valor='1.10')
        self.Id       = TagCaracter(nome='infNFe', codigo='A03', propriedade='Id'    , raiz='//NFe', namespace=NAMESPACE_NFE)
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
            xml += d.xml

        xml += self.total.xml
        xml += self.transp.xml
        xml += self.cobr.xml
        xml += self.infAdic.xml
        xml += self.exporta.xml
        xml += self.compra.xml
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

        return txt

    txt = property(get_txt)


class NFe(XMLNFe):
    def __init__(self):
        super(NFe, self).__init__()
        self.infNFe = InfNFe()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'nfe_v1.10.xsd'
        self.chave = ''
        self.dados_contingencia_fsda = ''
        self.site = ''
        self.email = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<NFe xmlns="http://www.portalfiscal.inf.br/nfe">'
        xml += self.infNFe.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.infNFe.Id.valor

        xml += self.Signature.xml
        xml += '</NFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infNFe.xml    = arquivo
            self.Signature.xml = self._le_noh('//NFe/sig:Signature')

    xml = property(get_xml, set_xml)

    def get_txt(self):
        txt = self.infNFe.txt
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
        chave = unicode(self.infNFe.ide.cUF.valor).zfill(2)

        if str(self.infNFe.versao.valor) == '3.10':
            chave += unicode(self.infNFe.ide.dhEmi.valor.strftime('%y%m')).zfill(4)

        else:
            chave += unicode(self.infNFe.ide.dEmi.valor.strftime('%y%m')).zfill(4)

        chave += unicode(self.infNFe.emit.CNPJ.valor).zfill(14)
        chave += unicode(self.infNFe.ide.mod.valor).zfill(2)
        chave += unicode(self.infNFe.ide.serie.valor).zfill(3)
        chave += unicode(self.infNFe.ide.nNF.valor).zfill(9)

        #
        # A inclusão do tipo de emissão na chave já torna a chave válida também
        # para a versão 2.00 da NF-e
        #
        chave += unicode(self.infNFe.ide.tpEmis.valor).zfill(1)

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
        # Define na estrutura do XML o campo cNF
        #
        self.infNFe.ide.cNF.valor = unicode(self.infNFe.ide.tpEmis.valor).zfill(1) + codigo

        #
        # Gera o dígito verificador
        #
        digito = self._calcula_dv(chave)

        #
        # Define na estrutura do XML o campo cDV
        #
        self.infNFe.ide.cDV.valor = digito

        chave += unicode(digito)
        self.chave = chave

        #
        # Define o Id
        #
        self.infNFe.Id.valor = 'NFe' + chave

    def monta_chave(self):
        chave = unicode(self.infNFe.ide.cUF.valor).zfill(2)
        chave += unicode(self.infNFe.ide.dEmi.valor.strftime('%y%m')).zfill(4)
        chave += unicode(self.infNFe.emit.CNPJ.valor).zfill(14)
        chave += unicode(self.infNFe.ide.mod.valor).zfill(2)
        chave += unicode(self.infNFe.ide.serie.valor).zfill(3)
        chave += unicode(self.infNFe.ide.nNF.valor).zfill(9)
        chave += unicode(self.infNFe.ide.cNF.valor).zfill(9)
        chave += unicode(self.infNFe.ide.cDV.valor).zfill(1)
        self.chave = chave

    def chave_para_codigo_barras(self):
        #
        # As funções do reportlabs para geração de códigos de barras não estão
        # aceitando strings unicode
        #
        return self.chave.encode('utf-8')

    def monta_dados_contingencia_fsda(self):
        dados = unicode(self.infNFe.ide.cUF.valor).zfill(2)
        dados += unicode(self.infNFe.ide.tpEmis.valor).zfill(1)
        dados += unicode(self.infNFe.emit.CNPJ.valor).zfill(14)
        dados += unicode(int(self.infNFe.total.ICMSTot.vNF.valor * 100)).zfill(14)

        #
        # Há ICMS próprio?
        #
        if self.infNFe.total.ICMSTot.vICMS.valor:
            dados += '1'
        else:
            dados += '2'

        #
        # Há ICMS ST?
        #
        if self.infNFe.total.ICMSTot.vST.valor:
            dados += '1'
        else:
            dados += '2'

        dados += self.infNFe.ide.dEmi.valor.strftime('%d').zfill(2)

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
    @property
    def chave_formatada(self):
        chave = self.chave
        chave_formatada = ' '.join((chave[0:4], chave[4:8], chave[8:12], chave[12:16], chave[16:20], chave[20:24], chave[24:28], chave[28:32], chave[32:36], chave[36:40], chave[40:44]))
        return chave_formatada

    @property
    def dados_contingencia_fsda_formatados(self):
        self.monta_dados_contingencia_fsda()
        dados = self.dados_contingencia_fsda
        dados_formatados = ' '.join((dados[0:4], dados[4:8], dados[8:12], dados[12:16], dados[16:20], dados[20:24], dados[24:28], dados[28:32], dados[32:36]))
        return dados_formatados

    @property
    def numero_formatado(self):
        num = unicode(self.infNFe.ide.nNF.valor).zfill(9)
        num_formatado = '.'.join((num[0:3], num[3:6], num[6:9]))
        return 'Nº ' + num_formatado

    @property
    def serie_formatada(self):
        return 'SÉRIE ' + unicode(self.infNFe.ide.serie.valor).zfill(3)


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
        if len(self.infNFe.emit.CPF.valor):
            return self._formata_cpf(unicode(self.infNFe.emit.CPF.valor))
        else:
            return self._formata_cnpj(unicode(self.infNFe.emit.CNPJ.valor))

    @property
    def endereco_emitente_formatado(self):
        formatado = self.infNFe.emit.enderEmit.xLgr.valor
        formatado += ', ' + self.infNFe.emit.enderEmit.nro.valor

        if len(self.infNFe.emit.enderEmit.xCpl.valor.strip()):
            formatado += ' - ' + self.infNFe.emit.enderEmit.xCpl.valor

        return formatado

    def _formata_cep(self, cep):
        if not len(cep.strip()):
            return ''

        return cep[0:5] + '-' + cep[5:8]

    @property
    def cep_emitente_formatado(self):
        return self._formata_cep(self.infNFe.emit.enderEmit.CEP.valor)

    @property
    def endereco_emitente_formatado_linha_1(self):
        formatado = self.endereco_emitente_formatado
        formatado += ' - ' + self.infNFe.emit.enderEmit.xBairro.valor
        return formatado

    @property
    def endereco_emitente_formatado_linha_2(self):
        formatado = self.infNFe.emit.enderEmit.xMun.valor
        formatado += ' - ' + self.infNFe.emit.enderEmit.UF.valor
        formatado += ' - ' + self.cep_emitente_formatado
        return formatado

    @property
    def endereco_emitente_formatado_linha_3(self):
        if self.fone_emitente_formatado.strip() != '':
            formatado = 'Fone: ' + self.fone_emitente_formatado
        else:
            formatado = ''
        return formatado

    @property
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
        return self._formata_fone(unicode(self.infNFe.emit.enderEmit.fone.valor))

    @property
    def cnpj_destinatario_formatado(self):
        if self.infNFe.dest.CPF.valor and len(self.infNFe.dest.CPF.valor):
            return self._formata_cpf(unicode(self.infNFe.dest.CPF.valor))
        elif self.infNFe.dest.CNPJ.valor and len(self.infNFe.dest.CNPJ.valor):
            return self._formata_cnpj(unicode(self.infNFe.dest.CNPJ.valor))
        elif self.infNFe.dest.idEstrangeiro.valor and len(self.infNFe.dest.idEstrangeiro.valor):
            return self.infNFe.dest.idEstrangeiro.valor
        else:
            return ''

    @property
    def endereco_destinatario_formatado(self):
        formatado = self.infNFe.dest.enderDest.xLgr.valor
        formatado += ', ' + self.infNFe.dest.enderDest.nro.valor

        if len(self.infNFe.dest.enderDest.xCpl.valor.strip()):
            formatado += ' - ' + self.infNFe.dest.enderDest.xCpl.valor

        return formatado

    @property
    def cep_destinatario_formatado(self):
        return self._formata_cep(self.infNFe.dest.enderDest.CEP.valor)

    @property
    def fone_destinatario_formatado(self):
        return self._formata_fone(unicode(self.infNFe.dest.enderDest.fone.valor))

    @property
    def cnpj_retirada_formatado(self):
        return self._formata_cnpj(self.infNFe.retirada.CNPJ.valor)

    @property
    def endereco_retirada_formatado(self):
        formatado = self.infNFe.retirada.xLgr.valor
        formatado += ', ' + self.infNFe.retirada.nro.valor

        if len(self.infNFe.retirada.xCpl.valor.strip()):
            formatado += ' - ' + self.infNFe.retirada.xCpl.valor

        formatado += ' - ' + self.infNFe.retirada.xBairro.valor
        formatado += ' - ' + self.infNFe.retirada.xMun.valor
        formatado += '-' + self.infNFe.retirada.UF.valor
        return formatado

    @property
    def cnpj_entrega_formatado(self):
        return self._formata_cnpj(self.infNFe.entrega.CNPJ.valor)

    @property
    def endereco_entrega_formatado(self):
        formatado = self.infNFe.entrega.xLgr.valor
        formatado += ', ' + self.infNFe.entrega.nro.valor

        if len(self.infNFe.entrega.xCpl.valor.strip()):
            formatado += ' - ' + self.infNFe.entrega.xCpl.valor

        formatado += ' - ' + self.infNFe.entrega.xBairro.valor
        formatado += ' - ' + self.infNFe.entrega.xMun.valor
        formatado += '-' + self.infNFe.entrega.UF.valor
        return formatado

    @property
    def cnpj_transportadora_formatado(self):
        if self.infNFe.transp.transporta.CPF.valor:
            return self._formata_cpf(self.infNFe.transp.transporta.CPF.valor)
        else:
            return self._formata_cnpj(self.infNFe.transp.transporta.CNPJ.valor)

    @property
    def placa_veiculo_formatada(self):
        if not self.infNFe.transp.veicTransp.placa.valor:
            return ''

        placa = self.infNFe.transp.veicTransp.placa.valor
        placa = placa[:-4] + '-' + placa[-4:]
        return placa

    @property
    def dados_adicionais(self):
        da = ''

        if self.infNFe.infAdic.infAdFisco.valor:
            da = self.infNFe.infAdic.infAdFisco.valor.replace('|', '<br />')

        if self.infNFe.infAdic.infCpl.valor:
            if len(da) > 0:
                da += '<br />'

            da += self.infNFe.infAdic.infCpl.valor.replace('|', '<br />')

        return da

    @property
    def canhoto_formatado(self):
        formatado = 'RECEBEMOS DE <b>'
        formatado += self.infNFe.emit.xNome.valor.upper()
        formatado += '</b> OS PRODUTOS E/OU SERVIÇOS CONSTANTES DA <b>NOTA FISCAL ELETRÔNICA</b> INDICADA AO LADO'
        return formatado

    @property
    def frete_formatado(self):
        if self.infNFe.transp.modFrete.valor == 0:
            formatado = '0-EMITENTE'

        elif self.infNFe.transp.modFrete.valor == 1:
            if self.infNFe.ide.tpNF.valor == 0:
                formatado = '1-REMETENTE'
            else:
                formatado = '1-DESTINATÁRIO'

        elif self.infNFe.transp.modFrete.valor == 2:
            formatado = '2-DE TERCEIROS'

        elif self.infNFe.transp.modFrete.valor == 9:
            formatado = '9-SEM FRETE'

        else:
            formatado = ''

        return formatado

    @property
    def cst_descricao(self):
        return 'CST'

    @property
    def crt_descricao(self):
        return ''
