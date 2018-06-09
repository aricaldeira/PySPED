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

NAMESPACE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evtFechamento/v1_03_02'


class InfoFech(XMLNFe):
    def __init__(self):
        super(InfoFech, self).__init__()
        self.evtServTm = TagCaracter(nome='evtServTm', tamanho=[1, 1], raiz='//Reinf/evtFechaEvPer/infoFech', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.evtServPr = TagCaracter(nome='evtServPr', tamanho=[1, 1], raiz='//Reinf/evtFechaEvPer/infoFech', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.evtAssDespRec = TagCaracter(nome='evtAssDespRec', tamanho=[1, 1], raiz='//Reinf/evtFechaEvPer/infoFech', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.evtAssDespRep = TagCaracter(nome='evtAssDespRep', tamanho=[1, 1], raiz='//Reinf/evtFechaEvPer/infoFech', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.evtComProd = TagCaracter(nome='evtComProd', tamanho=[1, 1], raiz='//Reinf/evtFechaEvPer/infoFech', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.evtCPRB = TagCaracter(nome='evtCPRB', tamanho=[1, 1], raiz='//Reinf/evtFechaEvPer/infoFech', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.evtPgtos = TagCaracter(nome='evtPgtos', tamanho=[1, 1], raiz='//Reinf/evtFechaEvPer/infoFech', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.compSemMovto = TagCaracter(nome='compSemMovto', tamanho=[0, 7], raiz='//Reinf/evtFechaEvPer/infoFech', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoFech>'
        xml += self.evtServTm.xml
        xml += self.evtServPr.xml
        xml += self.evtAssDespRec.xml
        xml += self.evtAssDespRep.xml
        xml += self.evtComProd.xml
        xml += self.evtCPRB.xml
        xml += self.evtPgtos.xml
        if self.compSemMovto.valor:
            xml += self.compSemMovto.xml
        xml += '</infoFech>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtServTm.xml = arquivo
            self.evtServPr.xml = arquivo
            self.evtAssDespRec.xml = arquivo
            self.evtAssDespRep.xml = arquivo
            self.evtComProd.xml = arquivo
            self.evtCPRB.xml = arquivo
            self.evtPgtos.xml = arquivo
            self.compSemMovto.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class IdeRespInf(XMLNFe):
    def __init__(self):
        super(IdeRespInf, self).__init__()
        self.nmResp = TagCaracter(nome='nmResp', tamanho=[1, 70], raiz='//Reinf/evtFechaEvPer/ideRespInf', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.cpfResp = TagCaracter(nome='cpfResp', tamanho=[1, 11], raiz='//Reinf/evtFechaEvPer/ideRespInf', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.telefone = TagCaracter(nome='telefone', tamanho=[0, 13], raiz='//Reinf/evtFechaEvPer/ideRespInf', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.email = TagCaracter(nome='email', tamanho=[0, 60], raiz='//Reinf/evtFechaEvPer/ideRespInf', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideRespInf>'
        xml += self.nmResp.xml
        xml += self.cpfResp.xml
        if self.telefone.valor:
            xml += self.telefone.xml
        if self.email.valor:
            xml += self.email.xml
        xml += '</ideRespInf>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nmResp.xml = arquivo
            self.cpfResp.xml = arquivo
            self.telefone.xml = arquivo
            self.email.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class IdeContri(XMLNFe):
    def __init__(self):
        super(IdeContri, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', valor='1', raiz='//Reinf/evtFechaEvPer/ideContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[8, 14], raiz='//Reinf/evtFechaEvPer/ideContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

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
        self.perApur = TagCaracter(nome='perApur', tamanho=[1, 10], raiz='//Reinf/evtFechaEvPer/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.tpAmb = TagInteiro(nome='tpAmb', tamanho=[1, 1, 1], raiz='//Reinf/evtFechaEvPer/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', tamanho=[1, 1, 1], raiz='//Reinf/evtFechaEvPer/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20], raiz='//Reinf/evtFechaEvPer/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.perApur.xml
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.perApur.xml = arquivo
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class EvtFechaEvPer(XMLNFe):
    def __init__(self):
        super(EvtFechaEvPer, self).__init__()
        self.Id = TagCaracter(nome='evtFechaEvPer', propriedade='id', raiz='//Reinf/evtFechaEvPer', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideContri = IdeContri()
        self.ideRespInf = IdeRespInf()
        self.infoFech = InfoFech()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideContri.xml
        xml += self.ideRespInf.xml
        xml += self.infoFech.xml
        xml += '</evtFechaEvPer>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideContri.xml = arquivo
            self.ideRespInf.xml = arquivo
            self.infoFech.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class R2099(XMLNFe):
    def __init__(self):
        super(R2099, self).__init__()
        self.evtFechaEvPer = EvtFechaEvPer()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtFechamento.xsd'
        self.id_evento = ''
        self.Signature = Signature()
        self.evento = self.evtFechaEvPer

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<Reinf xmlns="' + NAMESPACE_EFDREINF + '">'
        xml += self.evtFechaEvPer.xml
        
        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtFechaEvPer.Id.valor
        xml += self.Signature.xml               
        xml += '</Reinf>'

        # Define o método de assinatura
        self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtFechaEvPer.xml = arquivo
            self.Signature.xml = self._le_noh('//Reinf/evtFechaEvPer/sig:Signature')
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
        id_evento += self.evtFechaEvPer.ideContri.tpInsc.valor
        id_evento += str(self.evtFechaEvPer.ideContri.nrInsc.valor)[0:8] + '000000'
        # id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor).zfill(14)
        id_evento += data_hora        
        id_evento += str(1).zfill(5)
   
        # Define o Id
        #
        self.evtFechaEvPer.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
