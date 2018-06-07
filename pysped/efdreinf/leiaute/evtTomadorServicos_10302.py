# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Wagner Pereira <wagner.pereira at tauga.com.br>
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

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str
import os
import base64
from reportlab.graphics.barcode import createBarcodeDrawing
from genshi.core import Markup
from pysped.xml_sped import *
from pysped.efdreinf.leiaute import ESQUEMA_ATUAL_VERSAO_1 as ESQUEMA_ATUAL

PYBRASIL = False
#try:
from pybrasil.inscricao import formata_ie
from pybrasil.telefone import formata_fone
PYBRASIL = True
#except:
    #pass

DIRNAME = os.path.dirname(__file__)

NAMESPACE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evtServTom/v1_03_02'


class InfoProcRetAd(XMLNFe):
    def __init__(self):
        super(InfoProcRetAd, self).__init__()
        self.tpProcRetAdic = TagInteiro(nome='tpProcRetAdic', tamanho=[1, 1, 1], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/infoProcRetAd', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrProcRetAdic = TagCaracter(nome='nrProcRetAdic', tamanho=[1, 21], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/infoProcRetAd', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.codSuspAdic = TagInteiro(nome='codSuspAdic', tamanho=[0, 14], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/infoProcRetAd', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.valorAdic = TagDecimal(nome='valorAdic', tamanho=[1, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/infoProcRetAd', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoProcRetAd>'
        xml += self.tpProcRetAdic.xml
        xml += self.nrProcRetAdic.xml
        xml += self.codSuspAdic.xml
        xml += self.valorAdic.xml
        xml += '</infoProcRetAd>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.tpProcRetAdic.xml = arquivo
            self.nrProcRetAdic.xml = arquivo
            self.codSuspAdic.xml = arquivo
            self.valorAdic.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class InfoProcRetPr(XMLNFe):
    def __init__(self):
        super(InfoProcRetPr, self).__init__()
        self.tpProcRetPrinc = TagInteiro(nome='tpProcRetPrinc', tamanho=[1, 1, 1], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/infoProcRetPr', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrProcRetPrinc = TagCaracter(nome='nrProcRetPrint', tamanho=[1, 21], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/infoProcRetPr', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.codSuspPrinc = TagInteiro(nome='codSuspPrinc', tamanho=[0, 14], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/infoProcRetPr', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.valorPrinc = TagDecimal(nome='valorPrinc', tamanho=[1, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/infoProcRetPr', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoProcRetPr>'
        xml += self.tpProcRetPrinc.xml
        xml += self.nrProcRetPrinc.xml
        xml += self.codSuspPrinc.xml
        xml += self.valorPrinc.xml
        xml += '</infoProcRetPr>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.tpProcRetPrinc.xml = arquivo
            self.nrProcRetPrinc.xml = arquivo
            self.codSuspPrinc.xml = arquivo
            self.valorPrinc.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class InfoTpServ(XMLNFe):
    def __init__(self):
        super(InfoTpServ, self).__init__()
        self.tpServico = TagInteiro(nome='tpServico', tamanho=[1, 9], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs/infoTpServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrBaseRet = TagDecimal(nome='vlrBaseRet', tamanho=[1, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs/infoTpServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrRetencao = TagDecimal(nome='vlrRetencao', tamanho=[1, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs/infoTpServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrRetSub = TagDecimal(nome='vlrRetSub', tamanho=[0, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs/infoTpServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrNRetPrinc = TagDecimal(nome='vlrNRetPrinc', tamanho=[0, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs/infoTpServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrServicos15 = TagDecimal(nome='vlrServicos15', tamanho=[0, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs/infoTpServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrServicos20 = TagDecimal(nome='vlrServicos20', tamanho=[0, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs/infoTpServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrServicos25 = TagDecimal(nome='vlrServicos25', tamanho=[0, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs/infoTpServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrAdicional = TagDecimal(nome='vlrAdicional', tamanho=[0, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs/infoTpServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrNRetAdic = TagDecimal(nome='vlrNRetAdic', tamanho=[0, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs/infoTpServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoTpServ>'
        xml += self.tpServico.xml
        xml += self.vlrBaseRet.xml
        xml += self.vlrRetencao.xml
        xml += self.vlrRetSub.xml
        xml += self.vlrNRetPrinc.xml
        xml += self.vlrServicos15.xml
        xml += self.vlrServicos20.xml
        xml += self.vlrServicos25.xml
        xml += self.vlrAdicional.xml
        xml += self.vlrNRetAdic.xml
        xml += '</infoTpServ>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.tpServico.xml = arquivo
            self.vlrBaseRet.xml = arquivo
            self.vlrRetencao.xml = arquivo
            self.vlrRetSub.xml = arquivo
            self.vlrNRetPrinc.xml = arquivo
            self.vlrServicos15.xml = arquivo
            self.vlrServicos20.xml = arquivo
            self.vlrServicos25.xml = arquivo
            self.vlrAdicional.xml = arquivo
            self.vlrNRetAdic.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class NFS(XMLNFe):
    def __init__(self):
        super(NFS, self).__init__()
        self.serie = TagCaracter(nome='serie', tamanho=[1, 5], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.numDocto = TagCaracter(nome='numDocto', tamanho=[1, 15], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.dtEmissaoNF = TagData(nome='dtEmissaoNF', tamanho=[1, 1], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrBruto = TagDecimal(nome='vlrBruto', tamanho=[1, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.obs = TagCaracter(nome='obs', tamanho=[0, 250], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.infoTpServ = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<nfs>'
        xml += self.serie.xml
        xml += self.numDocto.xml
        xml += self.dtEmissaoNF.xml
        xml += self.vlrBruto.xml
        xml += self.obs.xml
        if len(self.infoTpServ) >= 1:
            for tpserv in self.infoTpServ:
                xml += tpserv.xml
        xml += '</nfs>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.serie.xml = arquivo
            self.numDocto.xml = arquivo
            self.dtEmissaoNF.xml = arquivo
            self.vlrBruto.xml = arquivo
            self.obs.xml = arquivo
            self.infoTpServ = self.le_grupo('//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs/infoTpServ', InfoTpServ, namespace=NAMESPACE_EFDREINF)
        return True

    xml = property(get_xml, set_xml)


class IdePrestServ(XMLNFe):
    def __init__(self):
        super(IdePrestServ, self).__init__()
        self.cnpjPrestador = TagCaracter(nome='cnpjPrestador', raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrTotalBruto = TagDecimal(nome='vlrTotalBruto', tamanho=[1, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrTotalBaseRet = TagDecimal(nome='vlrTotalBaseRet', tamanho=[1, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrTotalRetPrinc = TagDecimal(nome='vlrTotalRetPrinc', tamanho=[1, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrTotalRetAdic = TagDecimal(nome='vlrTotalRetAdic', tamanho=[1, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrTotalNRetPrinc = TagDecimal(nome='vlrTotalNRetPrinc', tamanho=[0, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrTotalNRetAdic = TagDecimal(nome='vlrTotalNRetAdic', tamanho=[0, 14, 2], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indCPRB = TagInteiro(nome='indCPRB', tamanho=[1, 1, 1], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nfs = []
        self.infoProcRetPr = []
        self.infoProcRetAd = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePrestServ>'
        xml += self.cnpjPrestador.xml
        xml += self.vlrTotalBruto.xml
        xml += self.vlrTotalBaseRet.xml
        xml += self.vlrTotalRetPrinc.xml
        xml += self.vlrTotalRetAdic.xml
        xml += self.vlrTotalNRetPrinc.xml
        xml += self.vlrTotalNRetAdic.xml
        xml += self.indCPRB.xml

        # Adiciona as NFs
        if len(self.nfs) >= 1:
            for nfs in self.nfs:
                xml += nfs.xml

        # Adiciona as InfoProcRetPr
        if len(self.infoProcRetPr) >= 1:
            for infoProcRetPr in self.infoProcRetPr:
                xml += infoProcRetPr.xml

        # Adiciona as InfoProcRetAd
        if len(self.infoProcRetAd) >= 1:
            for infoProcRetAd in self.infoProcRetAd:
                xml += infoProcRetAd.xml

        xml += '</idePrestServ>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjPrestador.xml = arquivo
            self.vlrTotalBruto.xml = arquivo
            self.vlrTotalBaseRet.xml = arquivo
            self.vlrTotalRetPrinc.xml = arquivo
            self.vlrTotalRetAdic.xml = arquivo
            self.vlrTotalNRetPrinc.xml = arquivo
            self.vlrTotalNRetAdic.xml = arquivo
            self.indCPRB.xml = arquivo
            self.nfs = self.le_grupo('//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/nfs', NFS, namespace=NAMESPACE_EFDREINF)
            self.infoProcRetPr = self.le_grupo('//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/infoProcRetPr', InfoProcRetPr, namespace=NAMESPACE_EFDREINF)
            self.infoProcRetAd = self.le_grupo('//Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/infoProcRetAd', InfoProcRetAd, namespace=NAMESPACE_EFDREINF)
        return True

    xml = property(get_xml, set_xml)


class IdeEstabObra(XMLNFe):
    def __init__(self):
        super(IdeEstabObra, self).__init__()
        self.tpInscEstab = TagInteiro(nome='tpInscEstab', tamanho=[1, 1, 1], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=1)
        self.nrInscEstab = TagCaracter(nome='nrInsc', tamanho=[8, 14], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indObra = TagInteiro(nome='indObra', tamanho=[1, 1, 1], raiz='//Reinf/evtServTom/infoServTom/ideEstabObra', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=0)
        self.idePrestServ = IdePrestServ()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstabObra>'
        xml += self.tpInscEstab.xml
        xml += self.nrInscEstab.xml
        xml += self.indObra.xml
        xml += self.idePrestServ.xml
        xml += '</ideEstabObra>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.tpInscEstab.xml = arquivo
            self.nrInscEstab.xml = arquivo
            self.indObra.xml = arquivo
            self.idePrestServ.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class InfoServTom(XMLNFe):
    def __init__(self):
        super(InfoServTom, self).__init__()
        self.ideEstabObra = IdeEstabObra()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoServTom>'
        xml += self.ideEstabObra.xml
        xml += '</infoServTom>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideEstabObra.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class IdeContri(XMLNFe):
    def __init__(self):
        super(IdeContri, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', valor='1', raiz='//Reinf/evtServTom/ideContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[8, 14], raiz='//Reinf/evtServTom/ideContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideContri>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideContri>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class IdeEvento(XMLNFe):
    def __init__(self):
        super(IdeEvento, self).__init__()
        self.indRetif = TagInteiro(nome='indRetif', tamanho=[1, 1, 1], raiz='//Reinf/evtServTom/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', tamanho=[0, 52], raiz='//Reinf/evtServTom/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.perApur = TagCaracter(nome='perApur', tamanho=[1, 10], raiz='//Reinf/evtServTom/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.tpAmb = TagInteiro(nome='tpAmb', tamanho=[1, 1, 1], raiz='//Reinf/evtServTom/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', tamanho=[1, 1, 1], raiz='//Reinf/evtServTom/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20], raiz='//Reinf/evtServTom/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.indRetif.xml
        xml += self.nrRecibo.xml
        xml += self.perApur.xml
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.indRetif.xml = arquivo
            self.nrRecibo.xml = arquivo
            self.perApur.xml = arquivo
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class EvtServTom(XMLNFe):
    def __init__(self):
        super(EvtServTom, self).__init__()
        self.Id = TagCaracter(nome='evtServTom', propriedade='id', raiz='//Reinf/evtServTom', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideContri = IdeContri()
        self.infoServTom = InfoServTom()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideContri.xml
        xml += self.infoServTom.xml
        xml += '</evtInfoContri>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideContri.xml = arquivo
            self.infoServTom.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class R2010(XMLNFe):
    def __init__(self):
        super(R2010, self).__init__()
        self.evtServTom = EvtServTom()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtTomadorServicos.xsd'
        self.id_evento = ''
        self.Signature = Signature()
        self.evento = self.evtServTom

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<Reinf xmlns="' + NAMESPACE_EFDREINF + '">'
        xml += self.evtServTom.xml
        
        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtServTom.Id.valor
        xml += self.Signature.xml               
        xml += '</Reinf>'

        # Define o método de assinatura
        self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtServTom.xml = arquivo
            self.Signature.xml = self._le_noh('//Reinf/evtServTom/sig:Signature')
        return True

    def gera_id_evento(self, data_hora):
        
        #A identificação única do evento (Id) é composta por 36 caracteres, conforme o que segue: IDTNNNNNNNNNNNNNNAAAAMMDDHHMMSSQQQQQ
        #ID - Texto Fixo "ID";
        #T - Tipo de Inscrição do Empregador (1 - CNPJ; 2 - CPF);
        #NNNNNNNNNNNNNN - Número do CNPJ ou CPF do empregador - Completar com
        #zeros à direita. No caso de pessoas jurídicas, o CNPJ informado deve conter 8 ou 14
        #posições de acordo com o enquadramento do contribuinte para preenchimento do campo
        #{ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se
        #necessário.
        #AAAAMMDD - Ano, mês e dia da geração do evento;
        #HHMMSS - Hora, minuto e segundo da geração do evento;
        #QQQQQ - Número sequencial da chave. Incrementar somente quando ocorrer geração de
        #eventos na mesma data/hora, completando com zeros à esquerda.
        #OBS.: No caso de pessoas jurídicas, o CNPJ informado deverá conter 8 ou 14 posições de
        #acordo com o enquadramento do contribuinte para preenchimento do campo {ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se necessário.        
                
        id_evento = 'ID'
        id_evento += self.evtServTom.ideContri.tpInsc.valor
        id_evento += str(self.evtServTom.ideContri.nrInsc.valor)[0:8] + '000000'
        # id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor).zfill(14)
        id_evento += data_hora        
        id_evento += str(1).zfill(5)
   
        # Define o Id
        #
        self.evtServTom.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
