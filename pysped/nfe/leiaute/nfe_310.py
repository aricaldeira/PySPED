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


class Deduc(nfe_200.Deduc):
    def __init__(self):
        super(Deduc, self).__init__()


class ForDia(nfe_200.ForDia):
    def __init__(self):
        super(ForDia, self).__init__()


class Cana(nfe_200.Cana):
    def __init__(self):
        super(Cana, self).__init__()


class ISSQN(nfe_200.ISSQN):
    def __init__(self):
        super(ISSQN, self).__init__()


class COFINSST(nfe_200.COFINSST):
    def __init__(self):
        super(COFINSST, self).__init__()


class TagCSTCOFINS(nfe_200.TagCSTCOFINS):
    def __init__(self, *args, **kwargs):
        super(TagCSTCOFINS, self).__init__(*args, **kwargs)


class COFINS(nfe_200.COFINS):
    def __init__(self):
        super(COFINS, self).__init__()


class PISST(nfe_200.PISST):
    def __init__(self):
        super(PISST, self).__init__()


class TagCSTPIS(nfe_200.TagCSTPIS):
    def __init__(self, *args, **kwargs):
        super(TagCSTPIS, self).__init__(*args, **kwargs)


class PIS(nfe_200.PIS):
    def __init__(self):
        super(PIS, self).__init__()


class II(nfe_200.II):
    def __init__(self):
        super(II, self).__init__()


class TagCSTIPI(nfe_200.TagCSTIPI):
    def __init__(self, *args, **kwargs):
        super(TagCSTIPI, self).__init__(*args, **kwargs)


class IPI(nfe_200.IPI):
    def __init__(self):
        super(IPI, self).__init__()


class TagCSOSN(nfe_200.TagCSOSN):
    def __init__(self, *args, **kwargs):
        super(TagCSOSN, self).__init__(*args, **kwargs)


class TagCSTICMS(nfe_200.TagCSTICMS):
    def __init__(self, *args, **kwargs):
        super(TagCSTICMS, self).__init__(*args, **kwargs)


class ICMS(nfe_200.ICMS):
    def __init__(self):
        super(ICMS, self).__init__()


class Imposto(nfe_200.Imposto):
    def __init__(self):
        super(Imposto, self).__init__()
        self.ICMS     = ICMS()
        self.ISSQN    = ISSQN()


class CIDE(nfe_200.CIDE):
    def __init__(self):
        super(CIDE, self).__init__()


class Comb(nfe_200.Comb):
    def __init__(self):
        super(Comb, self).__init__()


class Arma(nfe_200.Arma):
    def __init__(self):
        super(Arma, self).__init__()


class Med(nfe_200.Med):
    def __init__(self):
        super(Med, self).__init__()


class VeicProd(nfe_200.VeicProd):
    def __init__(self):
        super(VeicProd, self).__init__()


class Adi(nfe_200.Adi):
    def __init__(self):
        super(Adi, self).__init__()


class DI(nfe_200.DI):
    def __init__(self):
        super(DI, self).__init__()


class Prod(nfe_200.Prod):
    def __init__(self):
        super(Prod, self).__init__()
        self.veicProd = VeicProd()
        self.comb     = Comb()


class Det(nfe_200.Det):
    def __init__(self):
        super(Det, self).__init__()
        self.prod      = Prod()
        self.imposto   = Imposto()


class Compra(nfe_200.Compra):
    def __init__(self):
        super(Compra, self).__init__()


class Exporta(nfe_200.Exporta):
    def __init__(self):
        super(Exporta, self).__init__()


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


class Transporta(nfe_200.Transporta):
    def __init__(self):
        super(Transporta, self).__init__()


class Transp(nfe_200.Transp):
    def __init__(self):
        super(Transp, self).__init__()


class RetTrib(nfe_200.RetTrib):
    def __init__(self):
        super(RetTrib, self).__init__()


class ISSQNTot(nfe_200.ISSQNTot):
    def __init__(self):
        super(ISSQNTot, self).__init__()


class ICMSTot(nfe_200.ICMSTot):
    def __init__(self):
        super(ICMSTot, self).__init__()


class Total(nfe_200.Total):
    def __init__(self):
        super(Total, self).__init__()


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
        self.enderDest = EnderDest()


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
        self.idDest   = TagInteiro(nome='idDest'      , codigo='B11a', tamanho=[ 1,  1, 1], raiz='//NFe/infNFe/ide', valor=1)
        self.indFinal = TagCaracter(nome='indFinal'   , codigo='B25a',                      raiz='//NFe/infNFe/ide', valor='0')
        self.indPres  = TagCaracter(nome='indPres'    , codigo='B25b',                      raiz='//NFe/infNFe/ide', valor='9')

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
        xml += self.dhSaiEnt.xml
        xml += self.tpNF.xml
        xml += self.idDest.xml

        xml += self.cMunFG.xml

        for nr in self.NFref:
            xml += nr.xml

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

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.NFRef = self.le_grupo('//NFe/infNFe/ide/NFref', NFRef)

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


class NFe(nfe_200.NFe):
    def __init__(self):
        super(NFe, self).__init__()
        self.infNFe = InfNFe()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'nfe_v3.10.xsd'
