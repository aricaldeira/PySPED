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

NAMESPACE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evtTotal/v1_03_02'


class RRecEspetDesp(XMLNFe):
    def __init__(self):
        super(RRecEspetDesp, self).__init__()
        self.CRRecEspetDesp = TagCaracter(nome='CRRecEspetDesp', tamanho=[1, 6], raiz='//Reinf/evtTotal/infoTotal/RRecEspetDesp', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrReceitaTotal = TagDecimal(nome='vlrReceitaTotal', raiz='//Reinf/evtTotal/infoTotal/RRecEspetDesp', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrCRRecEspetDesp = TagDecimal(nome='vlrCRRecEspetDesp', raiz='//Reinf/evtTotal/infoTotal/RRecEspetDesp', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrCRRecEspetDespSusp = TagDecimal(nome='vlrCRRecEspetDespSusp', raiz='//Reinf/evtTotal/infoTotal/RCPRB', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RRecEspetDesp>'
        xml += self.CRRecEspetDesp.xml
        xml += self.vlrReceitaTotal.xml
        xml += self.vlrCRRecEspetDesp.xml
        xml += self.vlrCRRecEspetDespSusp.xml
        xml += '</RRecEspetDesp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CRRecEspetDesp.xml = arquivo
            self.vlrReceitaTotal.xml = arquivo
            self.vlrCRRecEspetDesp.xml = arquivo
            self.vlrCRRecEspetDespSusp.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class RCPRB(XMLNFe):
    def __init__(self):
        super(RCPRB, self).__init__()
        self.CRCPRB = TagCaracter(nome='CRCPRB', tamanho=[1, 6], raiz='//Reinf/evtTotal/infoTotal/RCPRB', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrCRCPRB = TagDecimal(nome='vlrCRCPRB', raiz='//Reinf/evtTotal/infoTotal/RCPRB', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrCRCPRBSusp = TagDecimal(nome='vlrCRCPRBSusp', raiz='//Reinf/evtTotal/infoTotal/RCPRB', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RCPRB>'
        xml += self.CRCPRB.xml
        xml += self.vlrCRCPRB.xml
        xml += self.vlrCRCPRBSusp.xml
        xml += '</RCPRB>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CRCPRB.xml = arquivo
            self.vlrCRCPRB.xml = arquivo
            self.vlrCRCPRBSusp.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class RComl(XMLNFe):
    def __init__(self):
        super(RComl, self).__init__()
        self.CRComl = TagCaracter(nome='CRComl', tamanho=[1, 6], raiz='//Reinf/evtTotal/infoTotal/RComl', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrCRComl = TagDecimal(nome='vlrCRComl', raiz='//Reinf/evtTotal/infoTotal/RComl', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrCRComlSusp = TagDecimal(nome='vlrCRComlSusp', raiz='//Reinf/evtTotal/infoTotal/RComl', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RComl>'
        xml += self.CRComl.xml
        xml += self.vlrCRComl.xml
        xml += self.vlrCRComlSusp.xml
        xml += '</RComl>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CRComl.xml = arquivo
            self.vlrCRComl.xml = arquivo
            self.vlrCRComlSusp.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class RRecRepAD(XMLNFe):
    def __init__(self):
        super(RRecRepAD, self).__init__()
        self.cnpjAssocDesp = TagCaracter(nome='cnpjAssocDesp', tamanho=[1, 14], raiz='//Reinf/evtTotal/infoTotal/RRecRepAD', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrTotalRep = TagDecimal(nome='vlrTotalRep', raiz='//Reinf/evtTotal/infoTotal/RRecRepAD', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.CRRecRepAD = TagCaracter(nome='CRRecRepAD', tamanho=[1, 6], raiz='//Reinf/evtTotal/infoTotal/RRecRepAD', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrCRRecRepAD = TagDecimal(nome='vlrCRRecRepAD', raiz='//Reinf/evtTotal/infoTotal/RRecRepAD', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrCRRecRepADSusp = TagDecimal(nome='vlrCRRecRepADSusp', raiz='//Reinf/evtTotal/infoTotal/RRecRepAD', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RRecRepAD>'
        xml += self.cnpjAssocDesp.xml
        xml += self.vlrTotalRep.xml
        xml += self.CRRecRepAD.xml
        xml += self.vlrCRRecRepAD.xml
        xml += self.vlrCRRecRepADSusp.xml
        xml += '</RRecRepAD>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjAssocDesp.xml = arquivo
            self.vlrTotalRep.xml = arquivo
            self.CRRecRepAD.xml = arquivo
            self.vlrCRRecRepAD.xml = arquivo
            self.vlrCRRecRepADSusp.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class RPrest(XMLNFe):
    def __init__(self):
        super(RPrest, self).__init__()
        self.tpInscTomador = TagInteiro(nome='tpInscTomador', tamanho=[1, 1, 1], raiz='//Reinf/evtTotal/infoTotal/RPrest', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInscTomador = TagCaracter(nome='nrInscTomador', tamanho=[1, 14], raiz='//Reinf/evtTotal/infoTotal/RPrest', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrTotalBaseRet = TagDecimal(nome='vlrTotalBaseRet', raiz='//Reinf/evtTotal/infoTotal/RPrest', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrTotalRetPrinc = TagDecimal(nome='vlrTotalRetPrinc', raiz='//Reinf/evtTotal/infoTotal/RPrest', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrTotalRetAdic = TagDecimal(nome='vlrTotalRetAdic', raiz='//Reinf/evtTotal/infoTotal/RPrest', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrTotalNRetPrinc = TagDecimal(nome='vlrTotalNRetPrinc', raiz='//Reinf/evtTotal/infoTotal/RPrest', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrTotalNRetAdic = TagDecimal(nome='vlrTotalNRetAdic', raiz='//Reinf/evtTotal/infoTotal/RPrest', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RPrest>'
        xml += self.tpInscTomador.xml
        xml += self.nrInscTomador.xml
        xml += self.vlrTotalBaseRet.xml
        xml += self.vlrTotalRetPrinc.xml
        xml += self.vlrTotalRetAdic.xml
        xml += self.vlrTotalNRetPrinc.xml
        xml += self.vlrTotalNRetAdic.xml
        xml += '</RPrest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInscTomador.xml = arquivo
            self.nrInscTomador.xml = arquivo
            self.vlrTotalBaseRet.xml = arquivo
            self.vlrTotalRetPrinc.xml = arquivo
            self.vlrTotalRetAdic.xml = arquivo
            self.vlrTotalNRetPrinc.xml = arquivo
            self.vlrTotalNRetAdic.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class InfoCRTom(XMLNFe):
    def __init__(self):
        super(InfoCRTom, self).__init__()
        self.CRTom = TagCaracter(nome='CRTom', tamanho=[1, 6], raiz='//Reinf/evtTotal/infoTotal/RTom/infoCRTom', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrCRTom = TagDecimal(nome='vlrCRTom', raiz='//Reinf/evtTotal/infoTotal/RTom/infoCRTom', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrCRTomSusp = TagDecimal(nome='vlrCRTomSusp', raiz='//Reinf/evtTotal/infoTotal/RTom/infoCRTom', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCRTom>'
        xml += self.CRTom.xml
        xml += self.vlrCRTom.xml
        xml += self.vlrCRTomSusp.xml
        xml += '</infoCRTom>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CRTom.xml = arquivo
            self.vlrCRTom.xml = arquivo
            self.vlrCRTomSusp.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class RTom(XMLNFe):
    def __init__(self):
        super(RTom, self).__init__()
        self.cnpjPrestador = TagCaracter(nome='cnpjPrestado', tamanho=[1, 14], raiz='//Reinf/evtTotal/infoTotal/RTom', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrTotalBaseRet = TagDecimal(nome='vlrTotalBaseRet', raiz='//Reinf/evtTotal/infoTotal/RTom', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.infoCRTom = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RTom>'
        xml += self.cnpjPrestador.xml
        xml += self.vlrTotalBaseRet.xml
        if len(self.infoCRTom) >= 1:
            for r in self.infoCRTom:
                xml += r.xml
        xml += '</RTom>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjPrestador.xml = arquivo
            self.vlrTotalBaseRet.xml = arquivo
            self.infoCRTom = self.le_grupo('//Reinf/evtTotal/infoTotal/RTom/infoCRTom', InfoCRTom, namespace=NAMESPACE_EFDREINF, sigla_ns='res')
        return True

    xml = property(get_xml, set_xml)


class InfoTotal(XMLNFe):
    def __init__(self):
        super(InfoTotal, self).__init__()
        self.nrRecArqBase = TagCaracter(nome='nrRecArqBase', raiz='//Reinf/evtTotal/infoTotal', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.RTom = RTom()
        self.RPrest = RPrest()
        self.RRecRepAD = []
        self.RComl = []
        self.RCPRB = []
        self.RRecEspetDesp = RRecEspetDesp()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoTotal>'
        xml += self.nrRecArqBase.xml
        xml += self.RTom.xml
        xml += self.RPrest.xml
        if len(self.RRecRepAD) >= 1:
            for r in self.RRecRepAD:
                xml += r.xml
        if len(self.RComl) >= 1:
            for r in self.RComl:
                xml += r.xml
        if len(self.RCPRB) >= 1:
            for r in self.RCPRB:
                xml += r.xml
        xml += self.RRecEspetDesp.xml
        xml += '</infoTotal>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRecArqBase.xml = arquivo
            self.RTom.xml = arquivo
            self.RPrest.xml = arquivo
            self.RRecRepAD = self.le_grupo('//Reinf/evtTotal/infoTotal/RRecRepAD', RRecRepAD, namespace=NAMESPACE_EFDREINF, sigla_ns='res')
            self.RComl = self.le_grupo('//Reinf/evtTotal/infoTotal/RComl', RComl, namespace=NAMESPACE_EFDREINF, sigla_ns='res')
            self.RCPRB = self.le_grupo('//Reinf/evtTotal/infoTotal/RCPRB', RCPRB, namespace=NAMESPACE_EFDREINF, sigla_ns='res')
            self.RRecEspetDesp.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class InfoRecEv(XMLNFe):
    def __init__(self):
        super(InfoRecEv, self).__init__()
        self.nrProtEntr = TagCaracter(nome='nrProtEntr', tamanho=[0, 49], raiz='//Reinf/evtTotal/infoRecEv', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.dhProcess  = TagDataHora(nome='dhProcess', raiz='//Reinf/evtTotal/infoRecEv', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.tpEv       = TagCaracter(nome='tpEv', tamanho=[1, 6], raiz='//Reinf/evtTotal/infoRecEv', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.idEv       = TagCaracter(nome='idEv', tamanho=[1, 36], raiz='//Reinf/evtTotal/infoRecEv', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.hash       = TagCaracter(nome='hash', tamanho=[1, 60], raiz='//Reinf/evtTotal/infoRecEv', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoRecEv>'
        xml += self.nrProtEntr.xml
        xml += self.dhProcess.xml
        xml += self.tpEv.xml
        xml += self.idEv.xml
        xml += self.hash.xml
        xml += '</infoRecEv>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrProtEntr.xml = arquivo
            self.dhProcess.xml = arquivo
            self.tpEv.xml = arquivo
            self.idEv.xml = arquivo
            self.hash.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class Ocorrencias(XMLNFe):
    def __init__(self):
        super(Ocorrencias, self).__init__()
        self.tpOcorr         = TagCaracter(nome='tpOcorr'       , raiz='//regOcorrs', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.localErroAviso  = TagCaracter(nome='localErroAviso', raiz='//regOcorrs', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.codResp         = TagCaracter(nome='codResp'       , raiz='//regOcorrs', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.dscResp         = TagCaracter(nome='dscResp'       , raiz='//regOcorrs', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<regOcorrs>'
        xml += self.tpOcorr.xml
        xml += self.localErroAviso.xml
        xml += self.codResp.xml
        xml += self.dscResp.xml
        xml += '</regOcorrs>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpOcorr.xml = arquivo
            self.localErroAviso.xml = arquivo
            self.codResp.xml = arquivo
            self.dscResp.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class IdeStatus(XMLNFe):
    def __init__(self):
        super(IdeStatus, self).__init__()
        self.cdRetorno   = TagCaracter(nome='cdRetorno', tamanho=[1, 6], raiz='//Reinf/evtTotal/ideRecRetorno/ideStatus', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.descRetorno = TagCaracter(nome='descRetorno', tamanho=[1, 255], raiz='//Reinf/evtTotal/ideRecRetorno/ideStatus', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.regOcorrs = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideRecRetorno>'
        xml += self.cdRetorno.xml
        xml += self.descRetorno.xml
        if len(self.regOcorrs) >= 1:
            xml += '<regOcorrs>'
            for o in self.regOcorrs:
                xml += o.xml
            xml += '</regOcorrs>'

        xml += '</ideRecRetorno>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cdRetorno.xml = arquivo
            self.descRetorno.xml = arquivo
            self.regOcorrs = self.le_grupo('//Reinf/evtTotal/ideRecRetorno/ideStatus/regOcorrs', Ocorrencias, namespace=NAMESPACE_EFDREINF, sigla_ns='res')
        return True

    xml = property(get_xml, set_xml)


class IdeRecRetorno(XMLNFe):
    def __init__(self):
        super(IdeRecRetorno, self).__init__()
        self.ideStatus = IdeStatus()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideRecRetorno>'
        xml += self.ideStatus.xml
        xml += '</ideRecRetorno>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideStatus.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class IdeContri(XMLNFe):
    def __init__(self):
        super(IdeContri, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', valor='1', raiz='//Reinf/evtTotal/ideContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[8, 14], raiz='//Reinf/evtTotal/ideContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideContri>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideContri>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class IdeEvento(XMLNFe):
    def __init__(self):
        super(IdeEvento, self).__init__()
        self.perApur = TagCaracter(nome='perApur', tamanho=[7, 7], raiz='//Reinf/evtTotal/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.perApur.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.perApur.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class EvtTotal(XMLNFe):
    def __init__(self):
        super(EvtTotal, self).__init__()
        self.Id = TagCaracter(nome='evtTotal', propriedade='id', raiz='//Reinf', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideContri = IdeContri()
        self.ideRecRetorno = IdeRecRetorno()
        self.infoRecEv = InfoRecEv()
        self.infoTotal = InfoTotal()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideContri.xml
        xml += self.ideRecRetorno.xml
        xml += self.infoRecEv.xml
        xml += self.infoTotal.xml
        xml += '</evtTotal>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideContri.xml = arquivo
            self.ideRecRetorno.xml = arquivo
            self.infoRecEv.xml = arquivo
            self.infoTotal.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class RetornoTotalizadorEvento(XMLNFe):
    def __init__(self):
        super(RetornoTotalizadorEvento, self).__init__()
        self.evtTotal = EvtTotal()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retornoTotalizadorEvento.xsd'
        self.id_evento = ''
        self.Signature = Signature()
        self.evento = self.evtTotal

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<Reinf xmlns="' + NAMESPACE_EFDREINF + '">'
        xml += self.evtTotal.xml
        
        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtTotal.Id.valor
        xml += self.Signature.xml               
        xml += '</Reinf>'

        # Define o método de assinatura
        self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtTotal.xml = arquivo
            self.Signature.xml = self._le_noh('//Reinf/evtTotal/sig:Signature')
        return True

    # def gera_id_evento(self, data_hora):
    #
    #     #A identificação única do evento (Id) é composta por 36 caracteres, conforme o que segue: IDTNNNNNNNNNNNNNNAAAAMMDDHHMMSSQQQQQ
    #     #ID - Texto Fixo "ID";
    #     #T - Tipo de Inscrição do Empregador (1 - CNPJ; 2 - CPF);
    #     #NNNNNNNNNNNNNN - Número do CNPJ ou CPF do empregador - Completar com
    #     #zeros à direita. No caso de pessoas jurídicas, o CNPJ informado deve conter 8 ou 14
    #     #posições de acordo com o enquadramento do contribuinte para preenchimento do campo
    #     #{ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se
    #     #necessário.
    #     #AAAAMMDD - Ano, mês e dia da geração do evento;
    #     #HHMMSS - Hora, minuto e segundo da geração do evento;
    #     #QQQQQ - Número sequencial da chave. Incrementar somente quando ocorrer geração de
    #     #eventos na mesma data/hora, completando com zeros à esquerda.
    #     #OBS.: No caso de pessoas jurídicas, o CNPJ informado deverá conter 8 ou 14 posições de
    #     #acordo com o enquadramento do contribuinte para preenchimento do campo {ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se necessário.
    #
    #     id_evento = 'ID'
    #     id_evento += self.evtInfoContri.ideContri.tpInsc.valor
    #     id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor)[0:8] + '000000'
    #     # id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor).zfill(14)
    #     id_evento += data_hora
    #     id_evento += str(1).zfill(5)
    #
    #     # Define o Id
    #     #
    #     self.evtTotal.Id.valor = id_evento
    #     self.id_evento = id_evento

    xml = property(get_xml, set_xml)
