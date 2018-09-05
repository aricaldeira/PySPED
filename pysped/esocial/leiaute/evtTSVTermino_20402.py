# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtTSVTermino/v02_04_02'

class Quarentena(XMLNFe):
    def __init__(self):
        super(Quarentena, self).__init__()
        self.dtFimQuar = TagData(name='dtFimQuar', raiz='//dtFimQuar', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<quarentena>'
        xml += self.dtFimQuar.xml
        xml += '</quarentena>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtFimQuar.xml = arquivo

    xml = property(get_xml, set_xml)


class RemunOutrEmpr(XMLNFe):
    def __init__(self):
        super(RemunOutrEmpr, self).__init__()
        self.tpInsc = TagInteiro(name='tpInsc', raiz='//tpInsc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(name='nrInsc', tamanho=[1, 15], raiz='//nrInsc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codCateg = TagInteiro(name='codCateg', raiz='//codCateg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrRemunOE = TagInteiro(name='vlrRemunOE', raiz='//vlrRemunOE', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<remunOutrEmpr>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.codCateg.xml
        xml += self.vlrRemunOE.xml
        xml += '</remunOutrEmpr>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.codCateg.xml = arquivo
            self.vlrRemunOE.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoMV(XMLNFe):
    def __init__(self):
        super(InfoMV, self).__init__()
        self.indMV = TagInteiro(name='indMV', raiz='//infoMV', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.remunOutrEmpr = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoMV>'
        xml += self.indMV.xml
        if self.remunOutrEmpr:
            for remuneracao in self.remunOutrEmpr:
                xml += remuneracao.xml
        xml += '</infoMV>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indMV.xml = arquivo
            self.remunOutrEmpr = self.le_grupo('//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/infoMV/remunOutrEmpr', RemunOutrEmpr, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class ProcJudTrab(XMLNFe):
    def __init__(self):
        super(ProcJudTrab, self).__init__()
        self.tpTrib = TagInteiro(name='tpTrib', raiz='//tpTrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrProcJud = TagCaracter(name='nrProcJud', tamanho=[1, 20], raiz='//nrProcJud', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codSusp = TagInteiro(name='codSusp', raiz='//codSusp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<procJudTrab>'
        xml += self.tpTrib.xml
        xml += self.nrProcJud.xml
        xml += self.codSusp.xml
        xml += '</procJudTrab>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpTrib.xml = arquivo
            self.nrProcJud.xml = arquivo
            self.codSusp.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoSimples(XMLNFe):
    def __init__(self):
        super(InfoSimples, self).__init__()
        self.indSimples = TagInteiro(name='indSimples', raiz='//indSimples', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoSimples>'
        xml += self.indSimples.xml
        xml += '</infoSimples>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indSimples.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoAgNocivo(XMLNFe):
    def __init__(self):
        super(InfoAgNocivo, self).__init__()
        self.grauExp = TagInteiro(nome='grauExp', raiz='//grauExp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoAgNocivo>'
        xml += self.grauExp.xml
        xml += '</infoAgNocivo>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.grauExp.xml = arquivo

    xml = property(get_xml, set_xml)


class DetVerbas(XMLNFe):
    def __init__(self):
        super(DetVerbas, self).__init__()
        self.codRubr = TagCaracter(nome='codRubr', tamanho=[1, 30], raiz='//codRubr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideTabRubr = TagCaracter(nome='ideTabRubr', tamanho=[1, 8], raiz='//ideTabRubr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.qtdRubr = TagInteiro(nome='qtdRubr', raiz='//qtdRubr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.fatorRubr = TagInteiro(nome='fatorRubr', raiz='//fatorRubr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrUnit = TagInteiro(nome='vrUnit', raiz='//vrUnit', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vrRubr = TagDecimal(nome='vrRubr', raiz='//vrRubr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detVerbas>'
        xml += self.codRubr.xml
        xml += self.ideTabRubr.xml
        xml += self.qtdRubr.xml
        xml += self.fatorRubr.xml
        xml += self.vrUnit.xml
        xml += self.vrRubr.xml
        xml += '</detVerbas>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codRubr.xml = arquivo
            self.ideTabRubr.xml = arquivo
            self.qtdRubr.xml = arquivo
            self.fatorRubr.xml = arquivo
            self.vrUnit.xml = arquivo
            self.vrRubr.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEstabLot(XMLNFe):
    def __init__(self):
        super(IdeEstabLot, self).__init__()
        self.tpInsc = TagInteiro(nome='tpInsc', raiz='//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/dmDev/infoPerApur/ideEstabLot/', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/dmDev/infoPerApur/ideEstabLot/', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codLotacao = TagCaracter(nome='codLotacao', tamanho=[1, 30], raiz='//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/dmDev/infoPerApur/ideEstabLot/', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.detVerbas = []
        self.infoAgNocivo = []
        self.infoSimples = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstabLot>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.codLotacao.xml
        if self.detVerbas:
            for verba in self.detVerbas:
                xml += verba.xml
        if self.infoAgNocivo:
            for info in self.infoAgNocivo:
                xml += info.xml
        if self.infoSimples:
            for info_simples in self.infoSimples:
                xml += info_simples.xml
        xml += '</ideEstabLot>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.codLotacao.xml = arquivo
            self.detVerbas = self.le_grupo(     '//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/dmDev/infoPerApur/ideEstabLot/detVerbas', DetVerbas, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoAgNocivo = self.le_grupo(  '//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/dmDev/infoPerApur/ideEstabLot/infoAgNocivo', InfoAgNocivo, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoSimples = self.le_grupo(   '//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/dmDev/infoPerApur/ideEstabLot/infoSimples', InfoSimples, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)

class DmDev(XMLNFe):
    def __init__(self):
        super(DmDev, self).__init__()
        self.ideDmDev = TagCaracter(nome='ideDmDev', tamanho=[1, 30], raiz='//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/dmDev', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEstabLot = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dmDev>'
        xml += self.ideDmDev.xml
        for estabelecimento in self.ideEstabLot:
            xml += estabelecimento.xml
        xml += '</dmDev>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideDmDev.xml = arquivo
            if self._le_xml(arquivo):
                self.ideEstabLot = self.le_grupo('//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/dmDev/ideEstabLot', IdeEstabLot, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class VerbasResc(XMLNFe):
    def __init__(self):
        super(VerbasResc, self).__init__()
        self.dmDev = []
        self.procJudTrab = []
        self.infoMV = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<verbasResc>'
        if len(self.dmDev) > 0:
            for demostrativo in self.dmDev:
                xml += demostrativo.xml
        if len(self.procJudTrab) > 0:
            for processoJud in self.procJudTrab:
                xml += processoJud.xml
        if len(self.infoMV) > 0:
            for info in self.infoMV:
                xml += info.xml
        xml += '</verbasResc>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dmDev = self.le_grupo('//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/dmDev', DmDev, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.procJudTrab = self.le_grupo('//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/procJudTrab', ProcJudTrab, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoMV = self.le_grupo('//eSocial/evtTSVTermino/infoTSVTermino/verbasResc/infoMV', HorarioIntervalo, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoTSVTermino(XMLNFe):
    def __init__(self):
        super(InfoTSVTermino, self).__init__()
        self.dtTerm = TagData(nome='dtTerm', raiz='//eSocial/evtTSVTermino/infoTSVTermino', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.mtvDesligTSV = TagCaracter(nome='mtvDesligTSV', tamanho=[0, 2], raiz='//eSocial/evtTSVTermino/infoTSVTermino', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.verbasResc = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoTSVTermino>'
        xml += self.dtTerm.xml
        xml += self.mtvDesligTSV.xml
        if self.verbasResc:
            for verba in self.verbasResc:
                xml += verba.xml
        xml += '</infoTSVTermino>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtTerm.xml = arquivo
            self.mtvDesligTSV.xml = arquivo
            if self._le_xml(arquivo):
                self.verbasResc = self.le_grupo('//eSocial/evtTSVTermino/infoTSVTermino/verbasResc', DmDev, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeTrabSemVinculo(XMLNFe):
    def __init__(self):
        super(IdeTrabSemVinculo, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', tamanho=[1, 11], raiz='//eSocial/evtTSVTermino/ideTrabSemVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab = TagCaracter(nome='nisTrab', tamanho=[1, 11], raiz='//eSocial/evtTSVTermino/ideTrabSemVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codCateg = TagInteiro(nome='codCateg', tamanho=[1, 3], raiz='//eSocial/evtTSVTermino/ideTrabSemVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideTrabSemVinculo>'
        xml += self.cpfTrab.xml
        xml += self.nisTrab.xml
        xml += self.codCateg.xml
        xml += '</ideTrabSemVinculo>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrab.xml = arquivo
            self.nisTrab.xml = arquivo
            self.codCateg.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtTSVTermino/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtTSVTermino/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif = TagInteiro( nome='indRetif', raiz='//eSocial/evtTSVTermino/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', raiz='//eSocial/evtTSVTermino/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpAmb    = TagInteiro( nome='tpAmb'   , raiz='//eSocial/evtTSVTermino/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi  = TagInteiro( nome='procEmi' , raiz='//eSocial/evtTSVTermino/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc  = TagCaracter(nome='verProc' , raiz='//eSocial/evtTSVTermino/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtTSVTermino(XMLNFe):
    def __init__(self):
        super(EvtTSVTermino, self).__init__()
        self.Id = TagCaracter(nome='evtTSVTermino', propriedade='Id', raiz='//eSocial/evtTSVTermino', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideTrabSemVinculo = IdeTrabSemVinculo()
        self.infoTSVTermino = InfoTSVTermino()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideTrabSemVinculo.xml
        xml += self.infoTSVTermino.xml
        xml += '</evtTSVTermino>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideTrabSemVinculo.xml = arquivo
            self.infoTSVTermino.xml = arquivo

    xml = property(get_xml, set_xml)


class S2399(XMLNFe):
    def __init__(self):
        super(S2399, self).__init__()
        self.evtTSVTermino = EvtTSVTermino()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtTSVTermino.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtTSVTermino
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtTSVTermino.xml

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
            self.evtTSVTermino.xml = arquivo
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
        self.evtTSVTermino.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
