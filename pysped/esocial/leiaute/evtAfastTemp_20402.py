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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtAfastTemp/v02_04_02'


class FimAfastamento(XMLNFe):
    def __init__(self):
        super(FimAfastamento, self).__init__()
        self.dtTermAfast = TagData(nome='dtTermAfast', raiz='//fimAfastamento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<fimAfastamento>'
        xml += self.dtTermAfast.xml
        xml += '</fimAfastamento>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtTermAfast.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoRetif(XMLNFe):
    def __init__(self):
        super(InfoRetif, self).__init__()
        self.origRetif = TagInteiro(nome='origRetif', raiz='//infoRetif', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpProc = TagInteiro(nome='origRetif', raiz='//infoRetif', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoRetif>'
        xml += self.origRetif.xml
        xml += self.tpProc.xml
        xml += '</infoRetif>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.origRetif.xml = arquivo
            self.tpProc.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoMandSind(XMLNFe):
    def __init__(self):
        super(InfoMandSind, self).__init__()
        self.cnpjSind = TagCaracter(nome='cnpjSind', tamanho=[1, 14], raiz='//infoMandSind', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infOnusRemun = TagInteiro(nome='infOnusRemun', raiz='//infoMandSind', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoMandSind>'
        xml += self.cnpjSind.xml
        xml += self.infOnusRemun.xml
        xml += '</infoMandSind>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjSind.xml = arquivo
            self.infOnusRemun.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoCessao(XMLNFe):
    def __init__(self):
        super(InfoCessao, self).__init__()
        self.cnpjCess = TagCaracter(nome='cnpjCess', tamanho=[1, 14], raiz='//infoCessao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infOnus = TagInteiro(nome='infOnus', raiz='//infoCessao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCessao>'
        xml += self.cnpjCess.xml
        xml += self.infOnus.xml
        xml += '</infoCessao>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjCess.xml = arquivo
            self.infOnus.xml = arquivo

    xml = property(get_xml, set_xml)


class Emitente(XMLNFe):
    def __init__(self):
        super(Emitente, self).__init__()
        self.nmEmit = TagCaracter(nome='nmEmit', tamanho=[1, 70], raiz='//emitente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideOC = TagInteiro(nome='ideOC', raiz='//emitente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrOc = TagCaracter(nome='nrOc', tamanho=[1, 14], raiz='//emitente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ufOC = TagCaracter(nome='nrOc', tamanho=[1, 2], raiz='//emitente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<emitente>'
        xml += self.nmEmit.xml
        xml += self.ideOC.xml
        xml += self.nrOc.xml
        xml += self.ufOC.xml
        xml += '</emitente>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nmEmit.xml = arquivo
            self.ideOC.xml = arquivo
            self.nrOc.xml = arquivo
            self.ufOC.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoAtestado(XMLNFe):
    def __init__(self):
        super(InfoAtestado, self).__init__()
        self.codCID = TagCaracter(nome='codCID', tamanho=[1, 4], raiz='//infoAtestado', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.qtdDiasAfast = TagInteiro(nome='qtdDiasAfast', raiz='//infoAtestado', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.emitente = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoAtestado>'
        xml += self.codCID.xml
        xml += self.qtdDiasAfast.xml
        for emitente in self.emitente:
            xml += emitente.xml
        xml += '</infoAtestado>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codCID.xml = arquivo
            self.qtdDiasAfast.xml = arquivo
            self.emitente.xml = self.le_grupo('//eSocial/evtAfastTemp/infoAfastamento/iniAfastamento/infoAtestado/emitente', Emitente, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IniAfastamento(XMLNFe):
    def __init__(self):
        super(IniAfastamento, self).__init__()
        self.dtIniAfast = TagData(nome='dtIniAfast', raiz='//iniAfastamento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMotAfast = TagCaracter(nome='codMotAfast', tamanho=[1, 2], raiz='//iniAfastamento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoMesmoMtv = TagCaracter(nome='infoMesmoMtv', tamanho=[1, 1], raiz='//iniAfastamento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpAcidTransito = TagInteiro(nome='iniAfastamento', raiz='//iniAfastamento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.observacao = TagCaracter(nome='observacao', raiz='//iniAfastamento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.infoAtestado = []
        self.infoCessao = []
        self.infoMandSind = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<iniAfastamento>'
        xml += self.dtIniAfast.xml
        xml += self.codMotAfast.xml
        xml += self.infoMesmoMtv.xml
        xml += self.tpAcidTransito.xml
        xml += self.observacao.xml
        for info_atestado in self.infoAtestado:
            xml += info_atestado.xml
        for info_cessao in self.infoCessao:
            xml += info_cessao.xml
        for info_mandato_sindical in self.infoMandSind:
            xml += info_mandato_sindical.xml
        xml += '</iniAfastamento>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtIniAfast.xml = arquivo
            self.codMotAfast.xml = arquivo
            self.infoMesmoMtv.xml = arquivo
            self.tpAcidTransito.xml = arquivo
            self.observacao.xml = arquivo
            self.infoAtestado.xml = self.le_grupo('//eSocial/evtAfastTemp/infoAfastamento/iniAfastamento/infoAtestado', InfoAtestado, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoCessao.xml = self.le_grupo('//eSocial/evtAfastTemp/infoAfastamento/iniAfastamento/infoCessao', InfoCessao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoMandSind.xml = self.le_grupo('//eSocial/evtAfastTemp/infoAfastamento/iniAfastamento/infoMandSind', InfoMandSind, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoAfastamento(XMLNFe):
    def __init__(self):
        super(InfoAfastamento, self).__init__()
        self.iniAfastamento = []
        self.infoRetif = []
        self.fimAfastamento = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoAfastamento>'
        for inicio_afastamento in self.iniAfastamento:
            xml += inicio_afastamento.xml
        for info_retificacao in self.infoRetif:
            xml += info_retificacao.xml
        for fim_afastamento in self.fimAfastamento:
            xml += fim_afastamento.xml
        xml += '</infoAfastamento>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.iniAfastamento = self.le_grupo('//eSocial/evtAfastTemp/infoAfastamento/iniAfastamento', IniAfastamento, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoRetif = self.le_grupo('//eSocial/evtAfastTemp/infoAfastamento/infoRetif', InfoRetif, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.fimAfastamento = self.le_grupo('//eSocial/evtAfastTemp/infoAfastamento/fimAfastamento', FimAfastamento, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeVinculo(XMLNFe):
    def __init__(self):
        super(IdeVinculo, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', tamanho=[1, 11], raiz='//eSocial/evtAfastTemp/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab = TagCaracter(nome='nisTrab', tamanho=[1, 11], raiz='//eSocial/evtAfastTemp/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.matricula = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//eSocial/evtAfastTemp/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//eSocial/evtAfastTemp/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideVinculo>'
        xml += self.cpfTrab.xml
        xml += self.nisTrab.xml
        xml += self.matricula.xml
        xml += self.codCateg.xml
        xml += '</ideVinculo>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrab.xml = arquivo
            self.nisTrab.xml = arquivo
            self.matricula.xml = arquivo
            self.codCateg.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagInteiro(nome='tpInsc', raiz='//eSocial/evtAfastTemp/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtAfastTemp/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif = TagInteiro(nome='indRetif', raiz='//eSocial/evtAfastTemp/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrRecibo = TagCaracter(nome='nrRecibo', tamanho=[1, 40], raiz='//eSocial/evtAfastTemp/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpAmb = TagInteiro(nome='tpAmb', raiz='//eSocial/evtAfastTemp/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.procEmi = TagInteiro(nome='procEmi', raiz='//eSocial/evtAfastTemp/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20], raiz='//eSocial/evtAfastTemp/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.indRetif.xml
        xml += self.nrRecibo.xml
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indRetif.xml = arquivo
            self.nrRecibo.xml = arquivo
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtAfastTemp(XMLNFe):
    def __init__(self):
        super(EvtAfastTemp, self).__init__()
        self.Id = TagCaracter(nome='evtAfastTemp', propriedade='Id', raiz='//eSocial/evtAfastTemp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideVinculo = IdeVinculo()
        self.infoAfastamento = InfoAfastamento()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideVinculo.xml
        xml += self.infoAfastamento.xml
        xml += '</evtAfastTemp>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideVinculo.xml = arquivo
            self.infoAfastamento.xml = arquivo

    xml = property(get_xml, set_xml)


class S2230(XMLNFe):
    def __init__(self):
        super(S2230, self).__init__()
        self.evtAfastTemp = EvtAfastTemp()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtAfastTemp.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtAfastTemp
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtAfastTemp.xml

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
            self.evtAfastTemp.xml = arquivo
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
        self.evtAfastTemp.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
