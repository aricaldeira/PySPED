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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtTabEstab/v02_04_02'


class NovaValidade(XMLNFe):
    def __init__(self):
        super(NovaValidade, self).__init__()
        self.iniValid = TagCaracter(nome='iniValid', raiz='//eSocial/evtTabEstab/infoEstab/novaValidade', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//eSocial/evtTabEstab/infoEstab/novaValidade', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

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


class InfoPCD(XMLNFe):
    def __init__(self):
        super(InfoPCD, self).__init__()
        self.contPCD   = TagCaracter(nome='contPCD'  , tamanho=[1, 1] , raiz='//infoPCD', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrProcJud = TagCaracter(nome='nrProcJud', tamanho=[1, 20], raiz='//infoPCD', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPCD>'
        xml += self.contPCD.xml
        xml += self.nrProcJud.xml
        xml += '</infoPCD>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.contPCD.xml = arquivo
            self.nrProcJud.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoEntEduc(XMLNFe):
    def __init__(self):
        super(InfoEntEduc, self).__init__()
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//infoEntEduc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoEntEduc>'
        xml += self.nrInsc.xml
        xml += '</infoEntEduc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoApr(XMLNFe):
    def __init__(self):
        super(InfoApr, self).__init__()
        self.contApr   = TagCaracter(nome='contApr'  , tamanho=[1, 1] , raiz='//eSocial/evtTabEstab/infoEstab/dadosEstab/infoTrab/infoApr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrProcJud = TagCaracter(nome='nrProcJud', tamanho=[1, 20], raiz='//eSocial/evtTabEstab/infoEstab/dadosEstab/infoTrab/infoApr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.contEntEd = TagCaracter(nome='contEntEd', tamanho=[1, 1] , raiz='//eSocial/evtTabEstab/infoEstab/dadosEstab/infoTrab/infoApr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.infoEntEduc = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoApr>'
        xml += self.contApr.xml
        xml += self.nrProcJud.xml
        xml += self.contEntEd.xml
        for e in self.infoEntEduc:
            xml += e.xml
        xml += '</infoApr>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.contApr.xml = arquivo
            self.nrProcJud.xml = arquivo
            self.contEntEd.xml = arquivo
            self.infoEntEduc = self.le_grupo('//eSocial/evtTabEstab/infoEstab/dadosEstab/infoTrab/infoApr/infoEntEduc', InfoEntEduc, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoTrab(XMLNFe):
    def __init__(self):
        super(InfoTrab, self).__init__()
        self.regPt = TagCaracter(nome='regPt', tamanho=[1, 1], raiz='//eSocial/evtTabEstab/infoEstab/dadosEstab/infoTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoApr = InfoApr()
        self.infoPCD = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoTrab>'
        xml += self.regPt.xml
        xml += self.infoApr.xml
        if len(self.infoPCD) > 0:
            for p in self.infoPCD:
                xml += p.xml
        xml += '</infoTrab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.regPt.xml = arquivo
            self.infoApr.xml = arquivo
            self.infoPCD = self.le_grupo('//eSocial/evtTabEstab/infoEstab/dadosEstab/infoTrab/infoPCD', InfoPCD, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoObra(XMLNFe):
    def __init__(self):
        super(InfoObra, self).__init__()
        self.indSubstPatrObra = TagInteiro(nome='indSubstPatrObra', tamanho=[1, 1], raiz='//infoObra', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoObra>'
        xml += self.indSubstPatrObra.xml
        xml += '</infoObra>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indSubstPatrObra.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoCaepf(XMLNFe):
    def __init__(self):
        super(InfoCaepf, self).__init__()
        self.tpCaepf = TagInteiro(nome='tpCaepf', tamanho=[1, 1], raiz='//infoCaepf', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCaepf>'
        xml += self.tpCaepf.xml
        xml += '</infoCaepf>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpCaepf.xml = arquivo

    xml = property(get_xml, set_xml)


class ProcAdmJudFap(XMLNFe):
    def __init__(self):
        super(ProcAdmJudFap, self).__init__()
        self.tpProc  = TagInteiro( nome='tpProc' , tamanho=[1, 1] , raiz='//procAdmJudFap', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrProc  = TagCaracter(nome='nrProc' , tamanho=[1, 21], raiz='//procAdmJudFap', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codSusp = TagInteiro( nome='codSusp', tamanho=[1, 14], raiz='//procAdmJudFap', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<procAdmJudFap>'
        xml += self.tpProc.xml
        xml += self.nrProc.xml
        xml += self.codSusp.xml
        xml += '</procAdmJudFap>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpProc.xml = arquivo
            self.nrProc.xml = arquivo
            self.codSusp.xml = arquivo

    xml = property(get_xml, set_xml)


class ProcAdmJudRat(XMLNFe):
    def __init__(self):
        super(ProcAdmJudRat, self).__init__()
        self.tpProc  = TagInteiro( nome='tpProc' , tamanho=[1, 1] , raiz='//procAdmJudRat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrProc  = TagCaracter(nome='nrProc' , tamanho=[1, 21], raiz='//procAdmJudRat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codSusp = TagInteiro( nome='codSusp', tamanho=[1, 14], raiz='//procAdmJudRat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<procAdmJudRat>'
        xml += self.tpProc.xml
        xml += self.nrProc.xml
        xml += self.codSusp.xml
        xml += '</procAdmJudRat>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpProc.xml = arquivo
            self.nrProc.xml = arquivo
            self.codSusp.xml = arquivo

    xml = property(get_xml, set_xml)


class AliqGilrat(XMLNFe):
    def __init__(self):
        super(AliqGilrat, self).__init__()
        self.aliqRat       = TagInteiro(nome='aliqRat', tamanho=[1, 1], raiz='//eSocial/evtTabEstab/infoEstab/dadosEstab/aliqGilrat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fap           = TagDecimal(nome='fap', tamanho=[1, 5, 4], raiz='//eSocial/evtTabEstab/infoEstab/dadosEstab/aliqGilrat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.aliqRatAjust  = TagDecimal(nome='aliqRatAjust', tamanho=[1, 5, 4], raiz='//eSocial/evtTabEstab/infoEstab/dadosEstab/aliqGilrat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.procAdmJudRat = []
        self.procAdmJudFap = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<aliqGilrat>'
        xml += self.aliqRat.xml
        xml += self.fap.xml
        xml += self.aliqRatAjust.xml
        if len(self.procAdmJudRat) > 0:
            for p in self.procAdmJudRat:
                xml += p.xml
        if len(self.procAdmJudFap) > 0:
            for p in self.procAdmJudFap:
                xml += p.xml
        xml += '</aliqGilrat>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.aliqRat.xml = arquivo
            self.fap.xml = arquivo
            self.aliqRatAjust.xml = arquivo
            self.procAdmJudRat = self.le_grupo('//eSocial/evtTabEstab/infoEstab/dadosEstab/aliqGilrat/procAdmJudRat', ProcAdmJudRat, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.procAdmJudFap = self.le_grupo('//eSocial/evtTabEstab/infoEstab/dadosEstab/aliqGilrat/procAdmJudFap', ProcAdmJudRat, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class DadosEstab(XMLNFe):
    def __init__(self):
        super(DadosEstab, self).__init__()
        self.cnaePrep   = TagCaracter(nome='cnaePrep', tamanho=[1, 7], raiz='//eSocial/evtTabEstab/infoEstab/dadosEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.aliqGilrat = AliqGilrat()
        self.infoCaepf  = []
        self.infoObra   = []
        self.infoTrab   = InfoTrab()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosEstab>'
        xml += self.cnaePrep.xml
        xml += self.aliqGilrat.xml
        if len(self.infoCaepf) > 0:
            for c in self.infoCaepf:
                xml += c.xml
        if len(self.infoObra) > 0:
            for o in self.infoObra:
                xml += o.xml
        xml += self.infoTrab.xml
        xml += '</dadosEstab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnaePrep.xml = arquivo
            self.aliqGilrat.xml = arquivo
            self.infoCaepf = self.le_grupo('//eSocial/evtTabEstab/infoEstab/dadosEstab/infoCaepf', InfoCaepf, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoObra = self.le_grupo('//eSocial/evtTabEstab/infoEstab/dadosEstab/infoObra', InfoObra, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoTrab.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEstab(XMLNFe):
    def __init__(self):
        super(IdeEstab, self).__init__()
        self.tpInsc   = TagCaracter(nome='tpInsc',   raiz='//eSocial/evtTabEstab/infoEstab/ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc   = TagCaracter(nome='nrInsc',   raiz='//eSocial/evtTabEstab/infoEstab/ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.iniValid = TagCaracter(nome='iniValid', raiz='//eSocial/evtTabEstab/infoEstab/ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//eSocial/evtTabEstab/infoEstab/ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstab>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</ideEstab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoEstab(XMLNFe):
    def __init__(self):
        super(InfoEstab, self).__init__()
        self.ideEstab = IdeEstab()
        self.dadosEstab = DadosEstab()
        self.novaValidade = NovaValidade()
        self.operacao = 'I'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoEstab>'
        if self.operacao == 'I':
            xml += '<inclusao>'
            xml += self.ideEstab.xml
            xml += self.dadosEstab.xml
            xml += '</inclusao>'
        elif self.operacao == 'A':
            xml += '<alteracao>'
            xml += self.ideEstab.xml
            xml += self.dadosEstab.xml
            xml += self.novaValidade.xml
            xml += '</alteracao>'

        elif self.operacao == 'E':
            xml += '<exclusao>'
            xml += self.ideEstab.xml
            xml += '</exclusao>'

        xml += '</infoEstab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideEstab.xml = arquivo
            self.dadosEstab.xml = arquivo
            self.novaValidade.xml = arquivo
    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtTabEstab/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtTabEstab/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtTabEstab(XMLNFe):
    def __init__(self):
        super(EvtTabEstab, self).__init__()
        self.Id = TagCaracter(nome='evtTabEstab', propriedade='Id', raiz='//eSocial/evtTabEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.infoEstab = InfoEstab()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.infoEstab.xml
        xml += '</evtTabEstab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoEstab.xml = arquivo

    xml = property(get_xml, set_xml)


class S1005(XMLNFe):
    def __init__(self):
        super(S1005, self).__init__()
        self.evtTabEstab = EvtTabEstab()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtTabEstab.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtTabEstab
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtTabEstab.xml

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
            self.evtTabEstab.xml = arquivo
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
        self.evtTabEstab.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
