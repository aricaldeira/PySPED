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
from pysped.esocial.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

PYBRASIL = False
#try:
from pybrasil.inscricao import formata_ie
from pybrasil.telefone import formata_fone
PYBRASIL = True
#except:
    #pass

DIRNAME = os.path.dirname(__file__)

NAMESPACE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evtInfoEmpregador/v1_03_02'


class EvtInfoContri(XMLNFe):
    def __init__(self):
        super(EvtInfoContri, self).__init__()
        self.Id = TagCaracter(nome='Id', tamanho=[1, 36], raiz='//Reinf', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=True)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evtInfoContri>'
        xml += self.Id.xml
        xml += '</evtInfoContri>'
        return xml


class IdeEvento(XMLNFe):
    def __init__(self):
        super(IdeEvento, self).__init__()
        self.tpAmb = TagInteiro(nome='tpAmb', tamanho=[1, 1, 1], raiz='//Reinf/evtInfoContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', tamanho=[1, 1, 1], raiz='//Reinf/evtInfoContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20], raiz='//Reinf/evtInfoContri', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

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

    xml = property(get_xml, set_xml)


class IdeContri(XMLNFe):
    def __init__(self):
        super(IdeContri, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', valor='1', raiz='//Reinf/evtInfoContri', namespace=NAMESPACE_REINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[14, 14], raiz='//Reinf//evtInfoContri', namespace=NAMESPACE_REINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEmpregador>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideEmpregador>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

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
        xml += '<infoEmpregador>'
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
                         
        xml += '</infoEmpregador>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.idePeriodo.xml = arquivo  
            self.infoCadastro.xml = arquivo  
            self.novaValidade.xml = arquivo  
    xml = property(get_xml, set_xml)       
    

class Inclusao(XMLNfe):
    def __init(self):
        super(Inclusao, self).__init()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<inclusao>'
        xml += '</inclusao>'
        return xml


class InclusaoIdePeriodo(XMLNFe):
    def __init__(self):
        super(InclusaoIdePeriodo, self).__init__()
        self.iniValid = TagCaracter(nome='iniValid', raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePeriodo>'
        xml += self.iniValid.xml        
        xml += self.fimValid.xml        
        xml += '</idePeriodo>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo
                        
    xml = property(get_xml, set_xml) 


class InclusaoInfoCadastro(XMLNFe):
    def __init__(self):
        super(InclusaoInfoCadastro, self).__init__()
        self.contato = Contato()        
        self.nmRazao  = TagCaracter(nome='nmRazao', tamanho=[ 1, 100], raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.classTrib  = TagCaracter(nome='classTrib', tamanho=[ 1, 2], raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.natJurid  = TagCaracter(nome='natJurid', tamanho=[ 1, 4], raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indCoop  = TagCaracter(nome='indCoop', tamanho=[ 1, 1], raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indConstr  = TagCaracter(nome='indConstr', tamanho=[ 1, 1], raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indDesFolha  = TagCaracter(nome='indDesFolha', tamanho=[ 1, 1], raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indOptRegEletron  = TagCaracter(nome='indOptRegEletron', tamanho=[ 1, 1], raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indEntEd  = TagCaracter(nome='indEntEd', raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indEtt  = TagCaracter(nome='indEtt', raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrRegEtt  = TagCaracter(nome='nrRegEtt', tamanho=[ 1, 30], raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indSitPJ = TagCaracter(nome='indSitPJ', tamanho=[ 1, 1], raiz='//Reinf/evtInfoContri/infoContri/inclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCadastro>'
        xml += self.nmRazao.xml        
        xml += self.classTrib.xml        
        xml += self.natJurid.xml        
        xml += self.indCoop.xml        
        xml += self.indConstr.xml        
        xml += self.indDesFolha.xml        
        xml += self.indOptRegEletron.xml        
        xml += self.indEntEd.xml        
        xml += self.indEtt.xml        
        xml += self.nrRegEtt.xml        
        xml += self.contato.xml
        xml += '<infoComplementares>'
        xml += '<situacaoPJ>'
        xml += self.indSitPJ.xml
        xml += '</situacaoPJ>'        
        xml += '</infoComplementares>'
        xml += '</infoCadastro>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.nmRazao.xml = arquivo
            self.classTrib.xml = arquivo
            self.natJurid.xml = arquivo
            self.indCoop.xml = arquivo
            self.indConstr.xml = arquivo
            self.indDesFolha.xml = arquivo
            self.indOptRegEletron.xml = arquivo
            self.indEntEd.xml = arquivo
            self.indEtt.xml = arquivo
            self.nrRegEtt.xml = arquivo
            self.contato.xml = arquivo
            self.infoComplementares.xml = arquivo
                        
    xml = property(get_xml, set_xml)        


class InclusaoContato(XMLNFe):
    def __init__(self):
        super(InclusaoContato, self).__init__()
        self.nmCtt = TagCaracter(nome='nmCtt', tamanho=[1, 70], raiz='//Reinf/evtInfoContri/infoContri/inclusao/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.cpfCtt = TagCaracter(nome='cpfCtt', tamanho=[1, 11], raiz='//Reinf/evtInfoContri/infoContri/inclusao/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.foneFixo = TagCaracter(nome='foneFixo', tamanho=[1, 11], raiz='//Reinf/evtInfoContri/infoContri/inclusao/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.email = TagCaracter(nome='email', tamanho=[1, 11], raiz='//Reinf/evtInfoContri/infoContri/inclusao/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<contato>'
        xml += self.nmCtt.xml
        xml += self.cpfCtt.xml
        xml += self.foneFixo.xml
        xml += self.email.xml
        xml += '</contato>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.nmCtt.xml = arquivo
            self.cpfCtt.xml = arquivo
            self.foneFixo.xml = arquivo
            self.email.xml = arquivo

    xml = property(get_xml, set_xml)       


class InclusaoSoftHouse(XMLNfe):
    def __init(self):
        super(InclusaoSoftHouse, self).__init()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<softHouse>'
        xml += '</softHouse>'
        return xml


class InclusaoInfoEFR(XMLNfe):
    def __init(self):
        super(InclusaoInfoEFR, self).__init()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoEFR>'
        xml += '</infoEFR>'
        return xml


class Alteracao(XMLNfe):
    def __init(self):
        super(Alteracao, self).__init()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<alteracao>'
        xml += '</alteracao>'
        return xml


class AlteracaoIdePeriodo(XMLNFe):
    def __init__(self):
        super(AlteracaoIdePeriodo, self).__init__()
        self.iniValid = TagCaracter(nome='iniValid', raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePeriodo>'
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</idePeriodo>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo

    xml = property(get_xml, set_xml)


class AlteracaoInfoCadastro(XMLNFe):
    def __init__(self):
        super(AlteracaoInfoCadastro, self).__init__()
        self.contato = Contato()
        self.nmRazao = TagCaracter(nome='nmRazao', tamanho=[1, 100], raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.classTrib = TagCaracter(nome='classTrib', tamanho=[1, 2], raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.natJurid = TagCaracter(nome='natJurid', tamanho=[1, 4], raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indCoop = TagCaracter(nome='indCoop', tamanho=[1, 1], raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indConstr = TagCaracter(nome='indConstr', tamanho=[1, 1], raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indDesFolha = TagCaracter(nome='indDesFolha', tamanho=[1, 1], raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indOptRegEletron = TagCaracter(nome='indOptRegEletron', tamanho=[1, 1], raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indEntEd = TagCaracter(nome='indEntEd', raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indEtt = TagCaracter(nome='indEtt', raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrRegEtt = TagCaracter(nome='nrRegEtt', tamanho=[1, 30], raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indSitPJ = TagCaracter(nome='indSitPJ', tamanho=[1, 1], raiz='//Reinf/evtInfoContri/infoContri/alteracao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCadastro>'
        xml += self.nmRazao.xml
        xml += self.classTrib.xml
        xml += self.natJurid.xml
        xml += self.indCoop.xml
        xml += self.indConstr.xml
        xml += self.indDesFolha.xml
        xml += self.indOptRegEletron.xml
        xml += self.indEntEd.xml
        xml += self.indEtt.xml
        xml += self.nrRegEtt.xml
        xml += self.contato.xml
        xml += '<infoComplementares>'
        xml += '<situacaoPJ>'
        xml += self.indSitPJ.xml
        xml += '</situacaoPJ>'
        xml += '</infoComplementares>'
        xml += '</infoCadastro>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.nmRazao.xml = arquivo
            self.classTrib.xml = arquivo
            self.natJurid.xml = arquivo
            self.indCoop.xml = arquivo
            self.indConstr.xml = arquivo
            self.indDesFolha.xml = arquivo
            self.indOptRegEletron.xml = arquivo
            self.indEntEd.xml = arquivo
            self.indEtt.xml = arquivo
            self.nrRegEtt.xml = arquivo
            self.contato.xml = arquivo
            self.infoComplementares.xml = arquivo

    xml = property(get_xml, set_xml)


class AlteracaoContato(XMLNFe):
    def __init__(self):
        super(AlteracaoContato, self).__init__()
        self.nmCtt = TagCaracter(nome='nmCtt', tamanho=[1, 70], raiz='//Reinf/evtInfoContri/infoContri/alteracao/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.cpfCtt = TagCaracter(nome='cpfCtt', tamanho=[1, 11], raiz='//Reinf/evtInfoContri/infoContri/alteracao/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.foneFixo = TagCaracter(nome='foneFixo', tamanho=[1, 11], raiz='//Reinf/evtInfoContri/infoContri/alteracao/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.email = TagCaracter(nome='email', tamanho=[1, 11], raiz='//Reinf/evtInfoContri/infoContri/alteracao/infoCadastro', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<contato>'
        xml += self.nmCtt.xml
        xml += self.cpfCtt.xml
        xml += self.foneFixo.xml
        xml += self.email.xml
        xml += '</contato>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.nmCtt.xml = arquivo
            self.cpfCtt.xml = arquivo
            self.foneFixo.xml = arquivo
            self.email.xml = arquivo

    xml = property(get_xml, set_xml)


class AlteracaoSoftHouse(XMLNfe):
    def __init(self):
        super(AlteracaoSoftHouse, self).__init()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<softHouse>'
        xml += '</softHouse>'
        return xml


class AlteracaoInfoEFR(XMLNfe):
    def __init(self):
        super(AlteracaoInfoEFR, self).__init()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoEFR>'
        xml += '</infoEFR>'
        return xml


class AlteracaoNovaValidade(XMLNfe):
    def __init(self):
        super(AlteracaoNovaValidade, self).__init()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<novaValidade>'
        xml += '</novaValidade>'
        return xml


class Exclusao(XMLNfe):
    def __init(self):
        super(Exclusao, self).__init()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<exclusao>'
        xml += '</exclusao>'
        return xml


class ExclusaoIdePeriodo(XMLNFe):
    def __init__(self):
        super(ExclusaoIdePeriodo, self).__init__()
        self.iniValid = TagCaracter(nome='iniValid', raiz='//Reinf/evtInfoContri/infoContri/exclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//Reinf/evtInfoContri/infoContri/exclusao', namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePeriodo>'
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</idePeriodo>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo

    xml = property(get_xml, set_xml)


class R1000(XMLNFe):
    def __init__(self):
        super(R1000, self).__init__()
        self.evtInfoEmpregador = EvtInfoContribuinte()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtInfoContribuinte.xsd'
        self.id_evento = ''
        self.Signature = Signature()

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
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtInfoContri.xml = arquivo
            self.Signature.xml = self._le_noh('//Reinf/evtInfoContri/sig:Signature')
                        
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
        id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor).zfill(14)
        id_evento += data_hora        
        id_evento += str(1).zfill(5)
   
        # Define o Id
        #
        self.evtInfoContri.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
