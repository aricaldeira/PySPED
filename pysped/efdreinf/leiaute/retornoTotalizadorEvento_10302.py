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


class InfoTotal(XMLNFe):
    def __init__(self):
        super(InfoTotal, self).__init__()
        self.nrRecArqBase = TagCaracter(nome='nrRecArqBase', raiz='//Reinf/evtTotal/infoTotal', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoTotal>'
        xml += self.nrRecArqBase.xml
        xml += '</infoTotal>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRecArqBase.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class InfoRecEv(XMLNFe):
    def __init__(self):
        super(InfoRecEv, self).__init__()
        self.dhProcess = TagCaracter(nome='dhProcess', raiz='//Reinf/evtTotal/infoRecEv', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.tpEv      = TagCaracter(nome='tpEv', raiz='//Reinf/evtTotal/infoRecEv', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.idEv      = TagCaracter(nome='idEv', raiz='//Reinf/evtTotal/infoRecEv', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.hash      = TagCaracter(nome='hash', raiz='//Reinf/evtTotal/infoRecEv', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoRecEv>'
        xml += self.dhProcess.xml
        xml += self.tpEv.xml
        xml += self.idEv.xml
        xml += self.hash.xml
        xml += '</infoRecEv>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
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
        self.cdRetorno   = TagInteiro(nome='cdRetorno', tamanho=[1, 1, 1], raiz='//Reinf/evtTotal/ideRecRetorno/ideStatus', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
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
        self.perApur = TagCaracter(nome='perApur', tamanho=[7, 10], raiz='//Reinf/evtTotal/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=2)

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
