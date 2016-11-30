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
from pysped.nfe.leiaute import nfe_200
import os

DIRNAME = os.path.dirname(__file__)


class Exporta(XMLNFe):
    def __init__(self):
        super(Exporta, self).__init__()
        self.UFSaidaPais   = TagCaracter(nome='UFSaidaPais', codigo='ZA02', tamanho=[2,  2], raiz='//NFe/infNFe/exporta', obrigatorio=False)
        self.xLocExporta = TagCaracter(nome='xLocExporta', codigo='ZA03', tamanho=[1, 60], raiz='//NFe/infNFe/exporta', obrigatorio=False)
        self.xLocDespacho = TagCaracter(nome='xLocDespacho', codigo='ZA04', tamanho=[1, 60], raiz='//NFe/infNFe/exporta', obrigatorio=False)

    def get_xml(self):
        if not (self.UFSaidaPais.valor or self.xLocExporta.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<exporta>'
        xml += self.UFSaidaPais.xml
        xml += self.xLocExporta.xml
        xml += self.xLocDespacho.xml
        xml += '</exporta>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.UFSaidaPais.xml = arquivo
            self.xLocExporta.xml = arquivo
            self.xLocDespacho.xml = arquivo

    xml = property(get_xml, set_xml)

    def get_txt(self):
        if not (self.UFSaidaPais.valor or self.xLocExporta.valor):
            return ''

        txt = 'ZA|'
        txt += self.UFSaidaPais.txt + '|'
        txt += self.xLocExporta.txt + '|'
        txt += self.xLocDespacho.txt + '|'
        txt += '\n'
        return txt

    txt = property(get_txt)


class InfNFe(nfe_200.InfNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.exporta = Exporta()


class Deduc(nfe_200.Deduc):
    def __init__(self):
        super(Deduc, self).__init__()


class ForDia(nfe_200.ForDia):
    def __init__(self):
        super(ForDia, self).__init__()


class Cana(nfe_200.Cana):
    def __init__(self):
        super(Cana, self).__init__()


class IPIDevol(XMLNFe):
    def __init__(self):
        super(IPIDevol, self).__init__()
        self.vIPIDevol = TagDecimal(nome='vIPIDevol', codigo='I50', tamanho=[1,  15, 1], decimais=[0, 2, 2], raiz='//det/impostoDevol/IPI')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.vIPIDevol.valor:
            xml += '<IPI>'
            xml += self.vIPIDevol.xml
            xml += '</IPI>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vIPIDevol.xml = arquivo

    xml = property(get_xml, set_xml)


class ImpostoDevol(XMLNFe):
    def __init__(self):
        super(ImpostoDevol, self).__init__()
        self.pDevol = TagDecimal(nome='pDevol', codigo='I50', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz='//det/impostoDevol')
        self.IPI    = IPIDevol()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.pDevol.valor:
            xml += '<impostoDevol>'
            xml += self.pDevol.xml
            xml += self.IPI.xml
            xml += '</impostoDevol>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.pDevol.xml = arquivo

    xml = property(get_xml, set_xml)


class ISSQN(nfe_200.ISSQN):
    def __init__(self):
        super(ISSQN, self).__init__()
        self.vAliq     = TagDecimal(nome='vAliq'    , codigo='U03', tamanho=[1,  5, 1], decimais=[0, 4, 4], raiz='//det/imposto/ISSQN')
        self.cListServ = TagCaracter(nome='cListServ', codigo='U06', tamanho=[5,  5],                     raiz='//det/imposto/ISSQN')
        #
        # Campos novos da versão 3.10
        #
        self.vDeducao = TagDecimal(nome='vDeducao', codigo='U07', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/ISSQN', obrigatorio=False)
        self.vOutro = TagDecimal(nome='vOutro', codigo='U08', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/ISSQN', obrigatorio=False)
        self.vDescIncond = TagDecimal(nome='vDescIncond', codigo='U09', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/ISSQN', obrigatorio=False)
        self.vDescCond = TagDecimal(nome='vDescCond', codigo='U10', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/ISSQN', obrigatorio=False)
        self.vISSRet = TagDecimal(nome='vISSRet', codigo='U11', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//det/imposto/ISSQN', obrigatorio=False)
        self.indISS  = TagCaracter(nome='indISS', codigo='U12', tamanho=[1,  2], raiz='//det/imposto/ISSQN')
        self.cServico = TagCaracter(nome='cServico', codigo='U13', tamanho=[1, 20], raiz='//det/imposto/ISSQN', obrigatorio=False)
        self.cMun     = TagInteiro(nome='cMun'   , codigo='U14', tamanho=[7, 7, 7], raiz='//det/imposto/ISSQN', obrigatorio=False)
        self.cPais    = TagInteiro(nome='cPais'  , codigo='U15', tamanho=[4, 4, 4], raiz='//det/imposto/ISSQN', obrigatorio=False)
        self.nProcesso = TagCaracter(nome='nProcesso', codigo='U16', tamanho=[1, 30], raiz='//det/imposto/ISSQN', obrigatorio=False)
        self.indIncentivo = TagCaracter(nome='indIncentivo', codigo='U17', tamanho=[1, 1], raiz='//det/imposto/ISSQN', valor='2')

    def get_xml(self):
        if not (self.indISS.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ISSQN>'
        xml += self.vBC.xml
        xml += self.vAliq.xml
        xml += self.vISSQN.xml
        xml += self.cMunFG.xml
        xml += self.cListServ.xml
        xml += self.vDeducao.xml
        xml += self.vOutro.xml
        xml += self.vDescIncond.xml
        xml += self.vDescCond.xml
        xml += self.vISSRet.xml
        xml += self.indISS.xml
        xml += self.cServico.xml
        xml += self.cMun.xml
        xml += self.cPais.xml
        xml += self.nProcesso.xml
        xml += self.indIncentivo.xml
        xml += '</ISSQN>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml       = arquivo
            self.vAliq.xml     = arquivo
            self.vISSQN.xml    = arquivo
            self.cMunFG.xml    = arquivo
            self.cListServ.xml = arquivo
            self.vDeducao.xml  = arquivo
            self.vOutro.xml  = arquivo
            self.vDescIncond.xml  = arquivo
            self.vDescCond.xml  = arquivo
            self.vISSRet.xml  = arquivo
            self.indISS.xml  = arquivo
            self.cServico.xml  = arquivo
            self.cMun.xml  = arquivo
            self.cPais.xml  = arquivo
            self.nProcesso.xml  = arquivo
            self.indIncentivo.xml  = arquivo

    xml = property(get_xml, set_xml)


class COFINSST(nfe_200.COFINSST):
    def __init__(self):
        super(COFINSST, self).__init__()


class TagCSTCOFINS(nfe_200.TagCSTCOFINS):
    def __init__(self, *args, **kwargs):
        super(TagCSTCOFINS, self).__init__(*args, **kwargs)


class COFINS(nfe_200.COFINS):
    def __init__(self):
        super(COFINS, self).__init__()
        self.pCOFINS   = TagDecimal(nome='pCOFINS'  , codigo='S08', tamanho=[1,  5, 1], decimais=[0, 4, 4], raiz='')

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


class PISST(nfe_200.PISST):
    def __init__(self):
        super(PISST, self).__init__()


class TagCSTPIS(nfe_200.TagCSTPIS):
    def __init__(self, *args, **kwargs):
        super(TagCSTPIS, self).__init__(*args, **kwargs)


class PIS(nfe_200.PIS):
    def __init__(self):
        super(PIS, self).__init__()
        self.pPIS      = TagDecimal(nome='pPIS'     , codigo='Q08', tamanho=[1,  5, 1], decimais=[0, 4, 4], raiz='')

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


class II(nfe_200.II):
    def __init__(self):
        super(II, self).__init__()


class TagCSTIPI(nfe_200.TagCSTIPI):
    def __init__(self, *args, **kwargs):
        super(TagCSTIPI, self).__init__(*args, **kwargs)


class IPI(nfe_200.IPI):
    def __init__(self):
        super(IPI, self).__init__()
        self.pIPI = TagDecimal(nome='pIPI', codigo='O13', tamanho=[1,  5, 1], decimais=[0, 4, 4], raiz='')

    def get_xml(self):
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


class TagCSOSN(nfe_200.TagCSOSN):
    def __init__(self, *args, **kwargs):
        super(TagCSOSN, self).__init__(*args, **kwargs)


class TagCSTICMS(nfe_200.TagCSTICMS):
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
        self.grupo_icms.vICMSDeson.obrigatorio = False
        self.grupo_icms.vICMSOp.obrigatorio = False
        self.grupo_icms.pDif.obrigatorio = False
        self.grupo_icms.vICMSDif.obrigatorio = False


        #
        # Por segurança, zeramos os valores das tags do
        # grupo ICMS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_icms.vICMSDeson.valor = '0.00'
        self.grupo_icms.vICMSOp.valor = '0.00'
        self.grupo_icms.pDif.valor = '0.00'
        self.grupo_icms.vICMSDif.valor = '0.00'

        #
        # Redefine a raiz para todas as tags do grupo ICMS
        #
        self.grupo_icms.vICMSDeson.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSOp.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.pDif.raiz        = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSDif.raiz    = self.grupo_icms.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class ICMS(nfe_200.ICMS):
    def __init__(self):
        super(ICMS, self).__init__()
        self.pRedBC   = TagDecimal(nome='pRedBC'  , codigo='N14', tamanho=[1,  5, 1], decimais=[0, 4, 4], raiz='')
        self.pICMS    = TagDecimal(nome='pICMS'   , codigo='N16', tamanho=[1,  5, 1], decimais=[0, 4, 4], raiz='')
        self.pMVAST   = TagDecimal(nome='pMVAST'  , codigo='N19', tamanho=[1,  5, 1], decimais=[0, 4, 4], raiz='')
        self.pRedBCST = TagDecimal(nome='pRedBCST', codigo='N20', tamanho=[1,  5, 1], decimais=[0, 4, 4], raiz='')
        self.pICMSST  = TagDecimal(nome='pICMSST' , codigo='N22', tamanho=[1,  5, 1], decimais=[0, 4, 4], raiz='')
        self.pCredSN  = TagDecimal(nome='pCredSN' , codigo='N29', tamanho=[1, 15, 1], decimais=[0, 4, 4], raiz='')
        #
        # Novos campos para o ICMS desonerado
        #
        self.vICMSDeson = TagDecimal(nome='vICMSDeson', codigo='N27a', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='')
        self.vICMSOp = TagDecimal(nome='vICMSOp', codigo='P16a', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='', obrigatorio=False)
        self.pDif = TagDecimal(nome='pDif', codigo='P16b', tamanho=[1, 7, 1], decimais=[0, 2, 4], raiz='', obrigatorio=False)
        self.vICMSDif = TagDecimal(nome='vICMSDif', codigo='P16b', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='', obrigatorio=False)

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
                xml += self.vICMSDeson.xml
                xml += self.motDesICMS.xml

            elif self.CST.valor == '30':
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml
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

            elif self.CST.valor == '60':
                xml += self.vBCSTRet.xml
                xml += self.vICMSSTRet.xml

            elif self.CST.valor == '70':
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
                xml += self.vICMSDeson.xml
                xml += self.motDesICMS.xml

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

class ICMSUFDest(XMLNFe):
    def __init__(self):
        super(ICMSUFDest, self).__init__()
        self.vBCUFDest = TagDecimal(nome='vBCUFDest', codigo='AI01', tamanho=[1,  13, 1], decimais=[2, 4, 2], raiz='//det/imposto/ICMSUFDest')
        self.pFCPUFDest = TagDecimal(nome='pFCPUFDest', codigo='AI02', tamanho=[1,  3, 1], decimais=[2, 4, 2], raiz='//det/imposto/ICMSUFDest')
        self.pICMSUFDest = TagDecimal(nome='pICMSUFDest', codigo='AI03', tamanho=[1,  3, 1], decimais=[2, 4, 2], raiz='//det/imposto/ICMSUFDest')
        self.pICMSInter= TagDecimal(nome='pICMSInter', codigo='AI04', tamanho=[1,  3, 1], decimais=[2, 4, 2], raiz='//det/imposto/ICMSUFDest')
        self.pICMSInterPart = TagDecimal(nome='pICMSInterPart', codigo='AI05', tamanho=[1,  3, 1], decimais=[2, 4, 2], raiz='//det/imposto/ICMSUFDest')
        self.vFCPUFDest = TagDecimal(nome='vFCPUFDest', codigo='AI06', tamanho=[1,  13, 1], decimais=[0, 2, 2], raiz='//det/imposto/ICMSUFDest')
        self.vICMSUFDest = TagDecimal(nome='vICMSUFDest', codigo='AI07', tamanho=[1,  13, 1], decimais=[0, 2, 2], raiz='//det/imposto/ICMSUFDest')
        self.vICMSUFRemet = TagDecimal(nome='vICMSUFRemet', codigo='AI08', tamanho=[1,  13, 1], decimais=[0, 2, 2], raiz='//det/imposto/ICMSUFDest')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if not self.pICMSInter.valor:
            return ''

        xml += '<ICMSUFDest>'
        xml += self.vBCUFDest.xml
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
            self.pFCPUFDest.xml     = arquivo
            self.pICMSUFDest.xml    = arquivo
            self.pICMSInter.xml     = arquivo
            self.pICMSInterPart.xml = arquivo
            self.vFCPUFDest.xml     = arquivo
            self.vICMSUFDest.xml    = arquivo
            self.vICMSUFRemet.xml   = arquivo

    xml = property(get_xml, set_xml)

class Imposto(nfe_200.Imposto):
    def __init__(self):
        super(Imposto, self).__init__()
        self.ICMS     = ICMS()
        self.IPI      = IPI()
        self.PIS      = PIS()
        self.COFINS   = COFINS()
        self.ISSQN    = ISSQN()
        self.ICMSUFDest = ICMSUFDest()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<imposto>'
        xml += self.vTotTrib.xml

        # Enviar ICMS, IPI e II somente quando não for serviço
        if not self.ISSQN.vAliq.valor:
            xml += self.ICMS.xml
            xml += self.IPI.xml
            xml += self.II.xml
        else:
            xml += self.ISSQN.xml

        xml += self.PIS.xml
        xml += self.PISST.xml
        xml += self.COFINS.xml
        xml += self.COFINSST.xml
        xml += self.ICMSUFDest.xml

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
            self.ICMSUFDest.xml    = arquivo

    xml = property(get_xml, set_xml)


class CIDE(nfe_200.CIDE):
    def __init__(self):
        super(CIDE, self).__init__()


class Comb(nfe_200.Comb):
    def __init__(self):
        super(Comb, self).__init__()
        self.pMixGN = TagDecimal(nome='pMixGN', codigo='LA03', tamanho=[1, 2, 1], decimais=[0, 4, 4], raiz='//det/prod/comb', obrigatorio=False)

    def get_xml(self):
        if not self.cProdANP.valor:
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<comb>'
        xml += self.cProdANP.xml
        xml += self.pMixGN.xml
        xml += self.CODIF.xml
        xml += self.qTemp.xml
        xml += self.CIDE.xml
        xml += '</comb>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cProdANP.xml  = arquivo
            self.pMixGN.xml  = arquivo
            self.CODIF.xml     = arquivo
            self.qTemp.xml     = arquivo
            self.CIDE.xml      = arquivo

    xml = property(get_xml, set_xml)


class Arma(nfe_200.Arma):
    def __init__(self):
        super(Arma, self).__init__()


class Med(nfe_200.Med):
    def __init__(self):
        super(Med, self).__init__()


class VeicProd(nfe_200.VeicProd):
    def __init__(self):
        super(VeicProd, self).__init__()


class ExportInd(XMLNFe):
    def __init__(self):
        super(ExportInd, self).__init__()
        self.nRE = TagInteiro(nome='nRE', codigo='I53', tamanho=[1, 12], raiz='//detExport/exportInd', obrigatorio=False)
        self.chNFe = TagCaracter(nome='chNFe', codigo='I54', tamanho=[44, 44], raiz='//detExport/exportInd', obrigatorio=False)
        self.qExport = TagDecimal(nome='qExport', codigo='I55', tamanho=[1, 12, 1], decimais=[0, 2, 4], raiz='//detExport/exportInd', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.nRE.valor or self.chNFe.valor or self.qExport.valor:
            xml += '<exportInd>'
            xml += self.nRE.xml
            xml += self.chNFe.xml
            xml += self.qExport.xml
            xml += '</exportInd>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nRE.xml     = arquivo
            self.chNFe.xml    = arquivo
            self.qExport.xml = arquivo

    xml = property(get_xml, set_xml)


class DetExport(XMLNFe):
    def __init__(self):
        super(DetExport, self).__init__()
        self.nDraw = TagInteiro(nome='nDraw', codigo='I50', tamanho=[1,  11], raiz='//detExport', obrigatorio=False)
        self.exportInd = ExportInd()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.nDraw.valor or self.exportInd.xml:
            xml += '<detExport>'
            xml += self.nDraw.xml
            xml += self.exportInd.xml
            xml += '</detExport>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nDraw.xml     = arquivo
            self.exportInd.xml    = arquivo

    xml = property(get_xml, set_xml)


class Adi(nfe_200.Adi):
    def __init__(self):
        super(Adi, self).__init__()


class DI(nfe_200.DI):
    def __init__(self):
        super(DI, self).__init__()
        self.tpViaTransp = TagCaracter(nome='tpViaTransp', codigo='I23a', tamanho=[1,  1], raiz='//DI')
        self.vAFRMM      = TagDecimal(nome='vAFRMM'      , codigo='I23b', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//DI', obrigatorio=False)
        self.tpIntermedio = TagCaracter(nome='tpIntermedio', codigo='I23c', tamanho=[1,  1], raiz='//DI')
        self.CNPJ = TagCaracter(nome='CNPJ'  , codigo='I23d', tamanho=[14, 14], raiz='//DI', obrigatorio=False)
        self.UFTerceiro = TagCaracter(nome='UFTerceiro', codigo='I23e', tamanho=[2, 2], raiz='//DI', obrigatorio=False)

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
        xml += self.tpViaTransp.xml
        xml += self.vAFRMM.xml
        xml += self.tpIntermedio.xml
        xml += self.CNPJ.xml
        xml += self.UFTerceiro.xml
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
            self.tpViaTransp.xml = arquivo
            self.vAFRMM.xml = arquivo
            self.tpIntermedio.xml = arquivo
            self.CNPJ.xml = arquivo
            self.UFTerceiro.xml = arquivo
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


class Prod(nfe_200.Prod):
    def __init__(self):
        super(Prod, self).__init__()
        #self.NCM      = TagCaracter(nome='NCM'     , codigo='I05' , tamanho=[2,  8]                        , raiz='//det/prod')
        #self.qCom     = TagDecimal(nome='qCom'     , codigo='I10' , tamanho=[1, 15, 1], decimais=[0,  4, 4], raiz='//det/prod')
        #self.vUnCom   = TagDecimal(nome='vUnCom'   , codigo='I10a', tamanho=[1, 21, 1], decimais=[0, 10, 4], raiz='//det/prod')
        #self.qTrib    = TagDecimal(nome='qTrib'    , codigo='I14' , tamanho=[1, 15, 1], decimais=[0,  4, 4], raiz='//det/prod')
        #self.vUnTrib  = TagDecimal(nome='vUnTrib'  , codigo='I14a', tamanho=[1, 21, 1], decimais=[0, 10, 4], raiz='//det/prod')
        #self.vOutro   = TagDecimal(nome='vOutro'   , codigo='I17a', tamanho=[1, 15, 1], decimais=[0,  2, 2], raiz='//det/prod', obrigatorio=False)
        #self.indTot   = TagInteiro(nome='indTot'   , codigo='I17b', tamanho=[1,  1, 1],                      raiz='//det/prod', valor=1)
        #self.xPed     = TagCaracter(nome='xPed'    , codigo='I30' , tamanho=[1, 15],                         raiz='//det/prod', obrigatorio=False)
        #self.nItemPed = TagCaracter(nome='nItemPed', codigo='I31' , tamanho=[1,  6],                         raiz='//det/prod', obrigatorio=False)
        #self.nFCI     = TagCaracter(nome='nFCI'    , codigo='I70' , tamanho=[36, 36, 36],                    raiz='//det/prod', obrigatorio=False)
        self.NVE = TagCaracter(nome='NVE', codigo='I05', tamanho=[0, 8], raiz='//det/prod', obrigatorio=False)
        self.CEST = TagCaracter(nome='CEST', codigo='I05c', tamanho=[0, 7], raiz='//det/prod', obrigatorio=False)
        self.detExport = DetExport()
        self.veicProd = VeicProd()
        self.comb     = Comb()
        self.nRECOPI  = TagCaracter(nome='nRECOPI', codigo='LB01', tamanho=[20, 20, 20], raiz='//det/prod', obrigatorio=False)


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


class Det(nfe_200.Det):
    def __init__(self):
        super(Det, self).__init__()
        self.prod      = Prod()
        self.imposto   = Imposto()
        self.impostoDevol = ImpostoDevol()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.nItem.xml
        xml += self.prod.xml
        xml += self.imposto.xml
        xml += self.impostoDevol.xml
        xml += self.infAdProd.xml
        xml += '</det>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nItem.xml     = arquivo
            self.prod.xml      = arquivo
            self.imposto.xml   = arquivo
            self.impostoDevol.xml = arquivo
            self.infAdProd.xml = arquivo

    xml = property(get_xml, set_xml)


class Compra(nfe_200.Compra):
    def __init__(self):
        super(Compra, self).__init__()


class ProcRef(nfe_200.ProcRef):
    def __init__(self):
        super(ProcRef, self).__init__()


class ObsFisco(nfe_200.ObsFisco):
    def __init__(self):
        super(ObsFisco, self).__init__()


class ObsCont(nfe_200.ObsCont):
    def __init__(self):
        super(ObsCont, self).__init__()


class InfAdic(nfe_200.InfAdic):
    def __init__(self):
        super(InfAdic, self).__init__()


class Card(XMLNFe):
    def __init__(self):
        super(Card, self).__init__()
        self.CNPJ  = TagCaracter(nome='CNPJ' , codigo='XA05', tamanho=[14, 14], raiz='//pag/card')
        self.tBand = TagCaracter(nome='tBand', codigo='YA01', tamanho=[ 2,  2], raiz='//pag/card')
        self.cAut  = TagCaracter(nome='cAut' , codigo='YA01', tamanho=[20, 20], raiz='//pag/card')

    def get_xml(self):
        if not (self.CNPJ.valor or self.tBand.valor or self.cAut.valor):
            return ''

        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += '<card>'
        xml += self.CNPJ.xml
        xml += self.tBand.xml
        xml += self.cAut.xml
        xml += '</card>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.tBand.xml = arquivo
            self.cAut.xml      = arquivo

    xml = property(get_xml, set_xml)


class Pag(XMLNFe):
    def __init__(self):
        super(Pag, self).__init__()
        self.tPag = TagCaracter(nome='tPag', codigo='YA01', tamanho=[2, 2, 2], raiz='//pag')
        self.vPag = TagDecimal(nome='vPag' , codigo='YA02', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//pag')
        self.card = Card()

    def get_xml(self):
        if not (self.tPag.valor or self.vPag.valor or self.card.xml):
            return ''

        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += '<pag>'
        xml += self.tPag.xml
        xml += self.vPag.xml
        xml += self.card.xml
        xml += '</pag>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tPag.xml = arquivo
            self.vPag.xml = arquivo
            self.cad.xml  = arquivo

    xml = property(get_xml, set_xml)


class Dup(nfe_200.Dup):
    def __init__(self):
        super(Dup, self).__init__()


class Fat(nfe_200.Fat):
    def __init__(self):
        super(Fat, self).__init__()


class Cobr(nfe_200.Cobr):
    def __init__(self):
        super(Cobr, self).__init__()


class Lacres(nfe_200.Lacres):
    def __init__(self):
        super(Lacres, self).__init__()


class Vol(nfe_200.Vol):
    def __init__(self, xml=None):
        super(Vol, self).__init__()


class Reboque(nfe_200.Reboque):
    def __init__(self):
        super(Reboque, self).__init__()


class VeicTransp(nfe_200.VeicTransp):
    def __init__(self):
        super(VeicTransp, self).__init__()


class RetTransp(nfe_200.RetTransp):
    def __init__(self):
        super(RetTransp, self).__init__()
        self.pICMSRet = TagDecimal(nome='vICMSRet', codigo='X14', tamanho=[1, 15, 1], decimais=[0, 4, 4], raiz='//NFe/infNFe/transp/retTransp')

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


class Transporta(nfe_200.Transporta):
    def __init__(self):
        super(Transporta, self).__init__()


class Transp(nfe_200.Transp):
    def __init__(self):
        super(Transp, self).__init__()
        self.retTransp  = RetTransp()

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


class RetTrib(nfe_200.RetTrib):
    def __init__(self):
        super(RetTrib, self).__init__()


class ISSQNTot(nfe_200.ISSQNTot):
    def __init__(self):
        super(ISSQNTot, self).__init__()
        self.dCompet     = TagData(nome='dCompet'       , codigo='W22a'                                        , raiz='//NFe/infNFe/total/ISSQNtot')
        self.vDeducao    = TagDecimal(nome='vDeducao'   , codigo='W22b', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vOutro      = TagDecimal(nome='vOutro'     , codigo='W22c', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vDescIncond = TagDecimal(nome='vDescIncond', codigo='W22d', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vDescCond   = TagDecimal(nome='vDescCond'  , codigo='W22e', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vISSRet     = TagDecimal(nome='vISSRet'    , codigo='W22f', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz='//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.cRegTrib    = TagCaracter(nome='cRegTrib'  , codigo='W22g', tamanho=[0, 1, 1]                     , raiz='//NFe/infNFe/total/ISSQNtot', obrigatorio=False)

    def get_xml(self):
        if not (self.vServ.valor or self.vBC.valor or self.vISS.valor or self.vPIS.valor or self.vCOFINS.valor or
                self.dCompet.valor or self.vDeducao.valor or self.vOutro.valor or self.vDescIncond.valor or self.vDescCond.valor
                or self.vISSRet.valor or self.cRegTrib.valor):
            return ''

        xml = XMLNFe.get_xml(self)
        xml += '<ISSQNtot>'
        xml += self.vServ.xml
        xml += self.vBC.xml
        xml += self.vISS.xml
        xml += self.vPIS.xml
        xml += self.vCOFINS.xml
        xml += self.dCompet.xml
        xml += self.vDeducao.xml
        xml += self.vOutro.xml
        xml += self.vDescIncond.xml
        xml += self.vDescCond.xml
        xml += self.vISSRet.xml
        xml += self.cRegTrib.xml
        xml += '</ISSQNtot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vServ.xml   = arquivo
            self.vBC.xml     = arquivo
            self.vISS.xml    = arquivo
            self.vPIS.xml    = arquivo
            self.vCOFINS.xml = arquivo
            self.dCompet.xml = arquivo
            self.vDeducao.xml = arquivo
            self.vOutro.xml = arquivo
            self.vDescIncond.xml = arquivo
            self.vDescCond.xml = arquivo
            self.vISSRet.xml = arquivo
            self.cRegTrib.xml = arquivo

    xml = property(get_xml, set_xml)


class ICMSTot(nfe_200.ICMSTot):
    def __init__(self):
        super(ICMSTot, self).__init__()
        self.vICMSDeson = TagDecimal(nome='vICMSDeson', codigo='W04a', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vFCPUFDest = TagDecimal(nome='vFCPUFDest', codigo='W04b', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vICMSUFDest = TagDecimal(nome='vICMSUFDest', codigo='W04c', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz='//NFe/infNFe/total/ICMSTot')
        self.vICMSUFRemet = TagDecimal(nome='vICMSUFRemet', codigo='W04d', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz='//NFe/infNFe/total/ICMSTot')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ICMSTot>'
        xml += self.vBC.xml
        xml += self.vICMS.xml
        xml += self.vICMSDeson.xml
        xml += self.vFCPUFDest.xml
        xml += self.vICMSUFDest.xml
        xml += self.vICMSUFRemet.xml
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
            self.vICMSDeson.xml = arquivo
            self.vFCPUFDest.xml   = arquivo
            self.vICMSUFDest.xml  = arquivo
            self.vICMSUFRemet.xml = arquivo
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


class Total(nfe_200.Total):
    def __init__(self):
        super(Total, self).__init__()
        self.ICMSTot = ICMSTot()
        self.ISSQNTot = ISSQNTot()
        #self.retTrib  = RetTrib()


class AutXML(XMLNFe):
    def __init__(self):
        super(AutXML, self).__init__()
        self.CNPJ = TagCaracter(nome='CNPJ'  , codigo='GA02', tamanho=[14, 14],  raiz='/', obrigatorio=False)
        self.CPF  = TagCaracter(nome='CPF'   , codigo='GA03', tamanho=[11, 11], raiz='/', obrigatorio=False)

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


class Entrega(nfe_200.Entrega):
    def __init__(self):
        super(Entrega, self).__init__()


class Retirada(nfe_200.Retirada):
    def __init__(self):
        super(Retirada, self).__init__()


class EnderDest(nfe_200.EnderDest):
    def __init__(self):
        super(EnderDest, self).__init__()


class Dest(nfe_200.Dest):
    def __init__(self):
        super(Dest, self).__init__()
        self.modelo = '55'
        self.enderDest = EnderDest()
        self.idEstrangeiro = TagCaracter(nome='idEstrangeiro' , codigo='E03a', tamanho=[0 , 20]   , raiz='//NFe/infNFe/dest', obrigatorio=False)
        self.indIEDest = TagCaracter(nome='indIEDest', codigo='E16a', tamanho=[1 , 1], raiz='//NFe/infNFe/dest', obrigatorio=True)
        self.IE        = TagCaracter(nome='IE'   , codigo='E17', tamanho=[ 2, 14]   , raiz='//NFe/infNFe/dest', obrigatorio=False)
        self.IM        = TagCaracter(nome='IM', codigo='E18a', tamanho=[ 1, 15]   , raiz='//NFe/infNFe/dest', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.modelo == '65' and (not self.CNPJ.valor) and (not self.CPF.valor) and (not self.idEstrangeiro.valor):
            return xml

        xml += '<dest>'

        #
        # Força o uso da tag CNPJ quando a nota for em homologação
        #
        if self.CNPJ.valor == '99999999000191':
            xml += self.CNPJ.xml
        elif self.CPF.valor:
            xml += self.CPF.xml
        elif self.CNPJ.valor:
            xml += self.CNPJ.xml
        elif self.idEstrangeiro.valor:
            xml += self.idEstrangeiro.xml

        if self.xNome.valor:
            xml += self.xNome.xml

        xml += self.enderDest.xml
        xml += self.indIEDest.xml

        if (not self.idEstrangeiro.valor) or (self.indIEDest.valor != '2' and self.IE.valor):
            xml += self.IE.xml

        xml += self.ISUF.xml
        xml += self.IM.xml
        xml += self.email.xml
        xml += '</dest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.idEstrangeiro.xml = arquivo
            self.xNome.xml     = arquivo
            self.enderDest.xml = arquivo
            self.indIEDest.xml = arquivo
            self.IE.xml        = arquivo
            self.ISUF.xml      = arquivo
            self.IM.xml     = arquivo
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


class Avulsa(nfe_200.Avulsa):
    def __init__(self):
        super(Avulsa, self).__init__()


class EnderEmit(nfe_200.EnderEmit):
    def __init__(self):
        super(EnderEmit, self).__init__()


class Emit(nfe_200.Emit):
    def __init__(self):
        super(Emit, self).__init__()
        self.enderEmit = EnderEmit()


class RefECF(nfe_200.RefECF):
    def __init__(self):
        super(RefECF, self).__init__()


class RefNFP(nfe_200.RefNFP):
    def __init__(self):
        super(RefNFP, self).__init__()


class RefNF(nfe_200.RefNF):
    def __init__(self):
        super(RefNF, self).__init__()


class NFRef(nfe_200.NFRef):
    def __init__(self):
        super(NFRef, self).__init__()


class Ide(nfe_200.Ide):
    def __init__(self):
        super(Ide, self).__init__()
        self.dhEmi    = TagDataHoraUTC(nome='dhEmi'   , codigo='B09' ,                      raiz='//NFe/infNFe/ide')
        self.dhSaiEnt = TagDataHoraUTC(nome='dhSaiEnt', codigo='B10' ,                      raiz='//NFe/infNFe/ide', obrigatorio=False)
        self.dhCont   = TagDataHoraUTC(nome='dhCont'  , codigo='B28',                       raiz='//NFe/infNFe/ide', obrigatorio=False)
        self.idDest   = TagCaracter(nome='idDest'      , codigo='B11a', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide', valor='1')
        self.indFinal = TagCaracter(nome='indFinal'   , codigo='B25a', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide', valor='0')
        self.indPres  = TagCaracter(nome='indPres'    , codigo='B25b', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide', valor='9')

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
        xml += self.dhEmi.xml

        self.dEmi.valor = self.dhEmi.valor

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


class InfNFe(nfe_200.InfNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.versao   = TagDecimal(nome='infNFe' , codigo='A01', propriedade='versao', raiz='//NFe', namespace=NAMESPACE_NFE, valor='3.10')
        self.ide      = Ide()
        self.emit     = Emit()
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
        self.pag = []
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

        for a in self.autXML:
            xml += a.xml

        for d in self.det:
            d.imposto.ICMS.regime_tributario = self.emit.CRT.valor
            xml += d.xml

        xml += self.total.xml
        xml += self.transp.xml
        xml += self.cobr.xml

        if self.ide.mod.valor == '65':
            for p in self.pag:
                xml += p.xml

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

            self.total.xml    = arquivo
            self.transp.xml   = arquivo
            self.cobr.xml     = arquivo

            self.pag = self.le_grupo('//NFe/infNFe/pag', Pag)

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


class NFe(nfe_200.NFe):
    def __init__(self):
        super(NFe, self).__init__()
        self.infNFe = InfNFe()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'nfe_v3.10.xsd'

    def monta_chave(self):
        chave = unicode(self.infNFe.ide.cUF.valor).strip().rjust(2, '0')
        chave += unicode(self.infNFe.ide.dhEmi.valor.strftime('%y%m')).strip().rjust(4, '0')
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

        dados += self.infNFe.ide.dhEmi.valor.strftime('%d').zfill(2)

        digito = self._calcula_dv(dados)
        dados += unicode(digito)
        self.dados_contingencia_fsda = dados

    def crt_desconto(self):
        return (
            self.infNFe.total.ICMSTot.vDesc.valor +
            self.infNFe.total.ICMSTot.vICMSDeson.valor
        )