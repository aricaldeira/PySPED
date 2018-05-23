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

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str
import os
from pysped.xml_sped import *
from pysped.esocial.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

DIRNAME = os.path.dirname(__file__)

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v02_04_02'


class Contato(XMLNFe):
    def __init__(self):
        super(Contato, self).__init__()
        self.nmCtt = TagCaracter(nome='nmCtt', tamanho=[ 1, 70]   , raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro/contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cpfCtt = TagCaracter(nome='cpfCtt', tamanho=[ 1, 11]   , raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro/contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.foneFixo = TagCaracter(nome='foneFixo', tamanho=[ 1, 11]   , raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro/contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.email = TagCaracter(nome='email', tamanho=[ 1, 11]   , raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro/contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

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

    xml = property(get_xml, set_xml)


class InfoCadastro(XMLNFe):
    def __init__(self):
        super(InfoCadastro, self).__init__()
        self.contato = Contato()
        self.nmRazao     = TagCaracter(nome='nmRazao'  , tamanho=[ 1, 100], raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.classTrib   = TagCaracter(nome='classTrib', tamanho=[ 1, 2]  , raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.natJurid    = TagCaracter(nome='natJurid' , tamanho=[ 1, 4]  , raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indCoop     = TagCaracter(nome='indCoop'  , tamanho=[ 1, 1]  , raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indConstr   = TagCaracter(nome='indConstr', tamanho=[ 1, 1]  , raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indDesFolha = TagCaracter(nome='indDesFolha', tamanho=[ 1, 1], raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='0')
        self.indOptRegEletron = TagCaracter(nome='indOptRegEletron', tamanho=[ 1, 1], raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='0')
        self.indEntEd    = TagCaracter(nome='indEntEd',                     raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indEtt      = TagCaracter(nome='indEtt'  ,                     raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='N')
        self.nrRegEtt    = TagCaracter(nome='nrRegEtt', tamanho=[ 1, 30]  , raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indSitPJ    = TagCaracter(nome='indSitPJ', tamanho=[ 1, 1]   , raiz='//eSocial/evtInfoEmpregador/infoEmpregador/infoCadastro/infoComplementares/situacaoPJ', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        xml += '<infoComplementares />'
        #xml += '<situacaoPJ>'
        #xml += self.indSitPJ.xml
        #xml += '</situacaoPJ>'
        #xml += '</infoComplementares>'
        xml += '</infoCadastro>'
        return xml

    def set_xml(self, arquivo):
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
            self.indSitPJ.xml = arquivo

    xml = property(get_xml, set_xml)


class IdePeriodo(XMLNFe):
    def __init__(self):
        super(IdePeriodo, self).__init__()
        self.iniValid  = TagCaracter(nome='iniValid', raiz='//eSocial/evtInfoEmpregador/infoEmpregador/idePeriodo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fimValid  = TagCaracter(nome='fimValid', raiz='//eSocial/evtInfoEmpregador/infoEmpregador/idePeriodo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

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

    xml = property(get_xml, set_xml)


class InfoEmpregador(XMLNFe):
    def __init__(self):
        super(InfoEmpregador, self).__init__()
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

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.idePeriodo.xml = arquivo
            self.infoCadastro.xml = arquivo
            self.novaValidade.xml = arquivo
    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtInfoEmpregador/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtInfoEmpregador/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEmpregador>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideEmpregador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEvento(XMLNFe):
    def __init__(self):
        super(IdeEvento, self).__init__()
        self.tpAmb   = TagInteiro(nome='tpAmb'   , raiz='//eSocial/evtInfoEmpregador/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi' , raiz='//eSocial/evtInfoEmpregador/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc = TagCaracter(nome='verProc', raiz='//eSocial/evtInfoEmpregador/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtInfoEmpregador(XMLNFe):
    def __init__(self):
        super(EvtInfoEmpregador, self).__init__()
        self.Id = TagCaracter(nome='evtInfoEmpregador', propriedade='Id', raiz='//eSocial/evtInfoEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.infoEmpregador = InfoEmpregador()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.infoEmpregador.xml
        xml += '</evtInfoEmpregador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoEmpregador.xml = arquivo

    xml = property(get_xml, set_xml)


class S1000(XMLNFe):
    def __init__(self):
        super(S1000, self).__init__()
        self.evtInfoEmpregador = EvtInfoEmpregador()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtInfoEmpregador.xsd'
        self.id_evento = ''
        self.Signature = Signature()
        self.evento = self.evtInfoEmpregador

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtInfoEmpregador.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtInfoEmpregador.Id.valor
        xml += self.Signature.xml
        xml += '</eSocial>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtInfoEmpregador.xml = arquivo
            self.Signature.xml = self._le_noh('//eSocial/sig:Signature')

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
        id_evento += self.evtInfoEmpregador.ideEmpregador.tpInsc.valor
        id_evento += str(self.evtInfoEmpregador.ideEmpregador.nrInsc.valor).zfill(14)
        id_evento += data_hora
        id_evento += str(1).zfill(5)

        # Define o Id
        #
        self.evtInfoEmpregador.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
