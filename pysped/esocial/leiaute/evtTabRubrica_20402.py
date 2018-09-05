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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtTabRubrica/v02_04_02'


class NovaValidade(XMLNFe):
    def __init__(self):
        super(NovaValidade, self).__init__()
        self.iniValid = TagCaracter(nome='iniValid', raiz='//eSocial/evtTabRubrica/infoRubrica/novaValidade', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//eSocial/evtTabRubrica/infoRubrica/novaValidade', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<novaValidade>'
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</novaValidade>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeProcessoSIND(XMLNFe):
    def __init__(self):
        super(IdeProcessoSIND, self).__init__()
        self.nrProc = TagCaracter(nome='nrProc', tamanho=[1, 21], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoFGTS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideProcessoSIND>'
        xml += self.nrProc.xml
        xml += '</ideProcessoSIND>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrProc.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeProcessoFGTS(XMLNFe):
    def __init__(self):
        super(IdeProcessoFGTS, self).__init__()
        self.nrProc = TagCaracter(nome='nrProc', tamanho=[1, 21], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoFGTS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideProcessoFGTS>'
        xml += self.nrProc.xml
        xml += '</ideProcessoFGTS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrProc.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeProcessoIRRF(XMLNFe):
    def __init__(self):
        super(IdeProcessoIRRF, self).__init__()
        self.nrProc = TagCaracter(nome='nrProc', tamanho=[1, 21], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoIRRF', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codSusp = TagCaracter(nome='codSusp', tamanho=[1, 21], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoIRRF', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideProcessoIRRF>'
        xml += self.nrProc.xml
        xml += self.codSusp.xml
        xml += '</ideProcessoIRRF>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrProc.xml = arquivo
            self.codSusp.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeProcessoCP(XMLNFe):
    def __init__(self):
        super(IdeProcessoCP, self).__init__()
        self.tpProc = TagCaracter(nome='tpProc', tamanho=[1, 1], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoCP', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrProc = TagCaracter(nome='nrProc', tamanho=[1, 21], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoCP', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.extDecisao = TagCaracter(nome='extDecisao', tamanho=[1, 1], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoCP', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codSusp = TagCaracter(nome='codSusp', tamanho=[1, 21], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoCP', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideProcessoCP>'
        xml += self.tpProc.xml
        xml += self.nrProc.xml
        xml += self.extDecisao.xml
        xml += self.codSusp.xml
        xml += '</ideProcessoCP>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpProc.xml = arquivo
            self.nrProc.xml = arquivo
            self.extDecisao.xml = arquivo
            self.codSusp.xml = arquivo

    xml = property(get_xml, set_xml)


class DadosRubrica(XMLNFe):
    def __init__(self):
        super(DadosRubrica, self).__init__()
        self.dscRubr = TagCaracter(nome='dscRubr', tamanho=[1, 100], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.natRubr = TagCaracter(nome='natRubr', tamanho=[1, 4], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpRubr = TagCaracter(nome='tpRubr', tamanho=[1, 1], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codIncCP = TagCaracter(nome='codIncCP', tamanho=[1, 2], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codIncIRRF = TagCaracter(nome='codIncIRRF', tamanho=[1, 2], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codIncFGTS = TagCaracter(nome='codIncFGTS', tamanho=[1, 2], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codIncSIND = TagCaracter(nome='codIncSIND', tamanho=[1, 2], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.observacao = TagCaracter(nome='observacao', tamanho=[1, 2], raiz='//eSocial/evtTabRubrica/infoRubrica/dadosRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.ideProcessoCP = []
        self.ideProcessoIRRF = []
        self.ideProcessoFGTS = []
        self.ideProcessoSIND = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosRubrica>'
        xml += self.dscRubr.xml
        xml += self.natRubr.xml
        xml += self.tpRubr.xml
        xml += self.codIncCP.xml
        xml += self.codIncIRRF.xml
        xml += self.codIncFGTS.xml
        xml += self.codIncSIND.xml
        xml += self.observacao.xml
        if len(self.ideProcessoCP) > 0:
            for p in self.ideProcessoCP:
                xml += p.xml
        if len(self.ideProcessoIRRF) > 0:
            for p in self.ideProcessoIRRF:
                xml += p.xml
        if len(self.ideProcessoFGTS) > 0:
            for p in self.ideProcessoFGTS:
                xml += p.xml
        if len(self.ideProcessoSIND) > 0:
            for p in self.ideProcessoSIND:
                xml += p.xml
        xml += '</dadosRubrica>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dscRubr.xml = arquivo
            self.natRubr.xml = arquivo
            self.tpRubr.xml = arquivo
            self.codIncCP.xml = arquivo
            self.codIncIRRF.xml = arquivo
            self.codIncFGTS.xml = arquivo
            self.codIncSIND.xml = arquivo
            self.observacao.xml = arquivo
            self.ideProcessoCP = self.le_grupo('//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoCP', IdeProcessoCP, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.ideProcessoIRRF = self.le_grupo('//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoIRRF', IdeProcessoIRRF, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.ideProcessoFGTS = self.le_grupo('//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoFGTS', IdeProcessoFGTS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.ideProcessoSIND = self.le_grupo('//eSocial/evtTabRubrica/infoRubrica/dadosRubrica/ideProcessoSIND', IdeProcessoSIND, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeRubrica(XMLNFe):
    def __init__(self):
        super(IdeRubrica, self).__init__()
        self.codRubr = TagCaracter(nome='codRubr', tamanho=[1, 30], raiz='//eSocial/evtTabRubrica/infoRubrica/ideRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideTabRubr = TagCaracter(nome='ideTabRubr', tamanho=[1, 8], raiz='//eSocial/evtTabRubrica/infoRubrica/ideRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.iniValid = TagCaracter(nome='iniValid', raiz='//eSocial/evtTabRubrica/infoRubrica/ideRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//eSocial/evtTabRubrica/infoRubrica/ideRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideRubrica>'
        xml += self.codRubr.xml
        xml += self.ideTabRubr.xml
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</ideRubrica>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codRubr.xml = arquivo
            self.ideTabRubr.xml = arquivo
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoRubrica(XMLNFe):
    def __init__(self):
        super(InfoRubrica, self).__init__()
        self.ideRubrica = IdeRubrica()
        self.dadosRubrica = DadosRubrica()
        self.novaValidade = NovaValidade()
        self.operacao = 'I'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoRubrica>'
        if self.operacao == 'I':
            xml += '<inclusao>'
            xml += self.ideRubrica.xml
            xml += self.dadosRubrica.xml
            xml += '</inclusao>'
        elif self.operacao == 'A':
            xml += '<alteracao>'
            xml += self.ideRubrica.xml
            xml += self.dadosRubrica.xml
            xml += self.novaValidade.xml
            xml += '</alteracao>'

        elif self.operacao == 'E':
            xml += '<exclusao>'
            xml += self.ideRubrica.xml
            xml += '</exclusao>'

        xml += '</infoRubrica>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideRubrica.xml = arquivo
            self.dadosRubrica.xml = arquivo
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
        self.tpAmb   = TagInteiro(nome='tpAmb'   , raiz='//eSocial/evtTabEstab/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi' , raiz='//eSocial/evtTabEstab/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc = TagCaracter(nome='verProc', raiz='//eSocial/evtTabEstab/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtTabRubrica(XMLNFe):
    def __init__(self):
        super(EvtTabRubrica, self).__init__()
        self.Id = TagCaracter(nome='evtTabRubrica', propriedade='Id', raiz='//eSocial/evtTabRubrica', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.infoRubrica = InfoRubrica()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.infoRubrica.xml
        xml += '</evtTabRubrica>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoRubrica.xml = arquivo

    xml = property(get_xml, set_xml)


class S1010(XMLNFe):
    def __init__(self):
        super(S1010, self).__init__()
        self.evtTabRubrica = EvtTabRubrica()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtTabRubrica.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtTabRubrica
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtTabRubrica.xml

        #
        # Define a URI a ser assinada
        #
        # self.Signature.URI = '#' + self.evtInfoEmpregador.Id.valor
        # xml += self.Signature.xml
        xml += '</eSocial>'

        # Define o método de assinatura
        # self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtTabRubrica.xml = arquivo
            # self.Signature.xml = self._le_noh('//eSocial/sig:Signature')

    def gera_id_evento(self, data_hora, sequencia=False):
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

        if not sequencia:
            sequencia=1

        id_evento = 'ID'
        id_evento += self.tpInsc
        id_evento += self.nrInsc[0:8] + '000000'
        id_evento += data_hora
        id_evento += str(sequencia).zfill(5)

        # Define o Id
        #
        self.evtTabRubrica.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
