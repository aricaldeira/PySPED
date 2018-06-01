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

NAMESPACE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evtInfoContribuinte/v1_03_02'


class Contato(XMLNFe):
    def __init__(self):
        super(Contato, self).__init__()
        self.nmCtt = TagCaracter(nome='nmCtt', tamanho=[1, 70], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro/contato', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.cpfCtt = TagCaracter(nome='cpfCtt', tamanho=[1, 11], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro/contato', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.foneFixo = TagCaracter(nome='foneFixo', tamanho=[1, 11], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro/contato', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.email = TagCaracter(nome='email', tamanho=[1, 11], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro/contato', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<contato>'
        xml += self.nmCtt.xml
        xml += self.cpfCtt.xml
        xml += self.foneFixo.xml
        xml += self.email.xml
        xml += '</contato>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nmCtt.xml = arquivo
            self.cpfCtt.xml = arquivo
            self.foneFixo.xml = arquivo
            self.email.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class SoftHouse(XMLNFe):
    def __init(self):
        super(SoftHouse, self).__init()
        self.cnpjSoftHouse = TagCaracter(nome='cnpjSoftHouse', tamanho=[1, 14], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro/softHouse', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.nmRazao = TagCaracter(nome='nmRazao', tamanho=[1, 115], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro/softHouse', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.nmCont = TagCaracter(nome='nmRazao', tamanho=[1, 70], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro/softHouse', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.telefone = TagCaracter(nome='telefone', tamanho=[10, 13], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro/softHouse', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.email = TagCaracter(nome='email', tamanho=[1, 60], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro/softHouse', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<softHouse>'
        xml += self.cnpjSoftHouse.xml
        xml += self.nmRazao.xml
        xml += self.nmCont.xml
        xml += self.telefone.xml
        xml += self.email.xml
        xml += '</softHouse>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.cnpjSoftHouse.xml = arquivo
            self.nmRazao.xml = arquivo
            self.nmCont.xml = arquivo
            self.telefone.xml = arquivo
            self.email.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class InfoEFR(XMLNFe):
    def __init(self):
        super(InfoEFR, self).__init()
        self.ideEFR = TagCaracter(nome='ideEFR', tamanho=[1, 1], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro/infoEFR', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.cnpjEFR = TagCaracter(nome='cnpjEFR', tamanho=[1, 14], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro/infoEFR', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoEFR>'
        xml += self.ideEFR.xml
        xml += self.cnpjEFR.xml
        xml += '</infoEFR>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.ideEFR.xml = arquivo
            self.cnpjEFR.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class InfoCadastro(XMLNFe):
    def __init__(self):
        super(InfoCadastro, self).__init__()
        self.contato = Contato()
        self.classTrib = TagCaracter(nome='classTrib', tamanho=[1, 2], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indEscrituracao = TagCaracter(nome='indEscrituracao', tamanho=[1, 1], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indDesoneracao = TagCaracter(nome='indDesoneracao', tamanho=[1, 1], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indAcordoIsenMulta = TagCaracter(nome='indAcordoIsenMulta', tamanho=[1, 1], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indSitPJ = TagCaracter(nome='indSitPJ', tamanho=[1, 1], raiz='//Reinf/evtInfoContri/infoContri/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCadastro>'
        xml += self.classTrib.xml
        xml += self.indEscrituracao.xml
        xml += self.indDesoneracao.xml
        xml += self.indAcordoIsenMulta.xml
        xml += self.indSitPJ.xml
        xml += self.contato.xml
        xml += '</infoCadastro>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.classTrib.xml = arquivo
            self.indEscrituracao.xml = arquivo
            self.indDesoneracao.xml = arquivo
            self.indAcordoIsenMulta.xml = arquivo
            self.indSitPJ.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class IdePeriodo(XMLNFe):
    def __init__(self):
        super(IdePeriodo, self).__init__()
        self.iniValid  = TagCaracter(nome='iniValid', raiz='//Reinf/evtInfoContri/infoContri/idePeriodo', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.fimValid  = TagCaracter(nome='fimValid', raiz='//Reinf/evtInfoContri/infoContri/idePeriodo', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePeriodo>'
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</idePeriodo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class InfoContri(XMLNFe):
    def __init__(self):
        super(InfoContri, self).__init__()
        self.idePeriodo = IdePeriodo()
        self.infoCadastro = InfoCadastro()
        self.novaValidade = IdePeriodo()
        self.operacao = 'I'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoContri>'
        if self.operacao == 'I':
            xml += '<inclusao>'
            xml += self.idePeriodo.xml
            xml += self.infoCadastro.xml
            xml += '</inclusao>'
        elif self.operacao == 'A':
            xml += '<alteracao>'
            xml += self.idePeriodo.xml
            xml += self.infoCadastro.xml
            xml += self.novaValidade.xml
            xml += '</alteracao>'

        elif self.operacao == 'E':
            xml += '<exclusao>'
            xml += self.idePeriodo.xml
            xml += '</exclusao>'

        xml += '</infoContri>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.novaValidade.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class IdeContri(XMLNFe):
    def __init__(self):
        super(IdeContri, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', valor='1', raiz='//Reinf/evtInfoContri/ideContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[8, 14], raiz='//Reinf/evtInfoContri/ideContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

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
        self.tpAmb = TagInteiro(nome='tpAmb', tamanho=[1, 1, 1], raiz='//Reinf/evtInfoContri/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', tamanho=[1, 1, 1], raiz='//Reinf/evtInfoContri/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20], raiz='//Reinf/evtInfoContri/ideEvento', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class EvtInfoContri(XMLNFe):
    def __init__(self):
        super(EvtInfoContri, self).__init__()
        self.Id = TagCaracter(nome='evtInfoContri', propriedade='id', raiz='//Reinf/evtInfoContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideContri = IdeContri()
        self.infoContri = InfoContri()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideContri.xml
        xml += self.infoContri.xml
        xml += '</evtInfoContri>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class R1000(XMLNFe):
    def __init__(self):
        super(R1000, self).__init__()
        self.evtInfoContri = EvtInfoContri()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtInfoContribuinte.xsd'
        self.id_evento = ''
        self.Signature = Signature()
        self.evento = self.evtInfoContri

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<Reinf xmlns="' + NAMESPACE_EFDREINF + '">'
        xml += self.evtInfoContri.xml
        
        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtInfoContri.Id.valor
        xml += self.Signature.xml               
        xml += '</Reinf>'

        # Define o método de assinatura
        self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtInfoContri.xml = arquivo
            self.Signature.xml = self._le_noh('//Reinf/evtInfoContri/sig:Signature')
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
        id_evento += self.evtInfoContri.ideContri.tpInsc.valor
        id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor)[0:8] + '000000'
        # id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor).zfill(14)
        id_evento += data_hora        
        id_evento += str(1).zfill(5)
   
        # Define o Id
        #
        self.evtInfoContri.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
