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


class IPIDevol(nfe_310.IPÎDevol):
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


class Imposto(nfe_310.Imposto):
    def __init__(self):
        super(Imposto, self).__init__()


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


class Prod(nfe_310.Prod):
    def __init__(self):
        super(Prod, self).__init__()


class Det(nfe_310.Det):
    def __init__(self):
        super(Det, self).__init__()


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


class Pag(nfe_310.Pag):
    def __init__(self):
        super(Pag, self).__init__()


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


class Total(nfe_310.Total):
    def __init__(self):
        super(Total, self).__init__()


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


class InfNFe(nfe_310.InfNFe):
    def __init__(self):
        super(InfNFe, self).__init__()


class NFe(nfe_310.NFe):
    def __init__(self):
        super(NFe, self).__init__()
