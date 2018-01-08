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

from pysped.xml_sped import (ABERTURA, NAMESPACE_NFE, Signature,
                             TagDecimal, TagCaracter, TagDataHoraUTC,
                             TagInteiro, XMLNFe, tira_abertura)
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

import os


DIRNAME = os.path.dirname(__file__)


class DetEvento(XMLNFe):
    def __init__(self):
        super(DetEvento, self).__init__()
        self.versao     = TagDecimal(nome='detEvento'  , codigo='HP18', propriedade='versao', valor='1.00', raiz='/')
        self.descEvento = TagCaracter(nome='descEvento', codigo='HP19', tamanho=[ 5,  60, 5], raiz='//detEvento')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.versao.xml
        xml += self.descEvento.xml
        xml += '</detEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.descEvento.xml = arquivo

    xml = property(get_xml, set_xml)

    @property
    def texto_formatado(self):
        return u''


class InfEvento(XMLNFe):
    def __init__(self):
        super(InfEvento, self).__init__()
        self.Id         = TagCaracter(nome='infEvento', codigo='HP07', tamanho=[54, 54]    , raiz='//evento', propriedade='Id')
        self.cOrgao     = TagInteiro(nome='cOrgao'    , codigo='HP08', tamanho=[ 2,  2, 2] , raiz='//evento/infEvento')
        self.tpAmb      = TagInteiro(nome='tpAmb'     , codigo='HP09', tamanho=[ 1,  1, 1] , raiz='//evento/infEvento', valor=2)
        self.CNPJ       = TagCaracter(nome='CNPJ'     , codigo='HP10', tamanho=[14, 14]    , raiz='//evento/infEvento')
        self.CPF        = TagCaracter(nome='CPF'      , codigo='HP11', tamanho=[11, 11]    , raiz='//evento/infEvento')
        self.chNFe      = TagCaracter(nome='chNFe'    , codigo='HP12', tamanho=[44, 44, 44], raiz='//evento/infEvento')
        self.dhEvento   = TagDataHoraUTC(nome='dhEvento' , codigo='HP13',                       raiz='//evento/infEvento')
        self.tpEvento   = TagCaracter(nome='tpEvento' , codigo='HP14', tamanho=[ 6,  6,  6], raiz='//evento/infEvento')
        self.nSeqEvento = TagInteiro(nome='nSeqEvento', codigo='HP15', tamanho=[ 1,  2, 1] , raiz='//evento/infEvento', valor=1)
        self.verEvento  = TagDecimal(nome='verEvento' , codigo='HP16',                       raiz='//evento/infEvento', valor='1.00')
        self.detEvento  = DetEvento()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        self.Id.valor = 'ID' + self.tpEvento.valor + self.chNFe.valor + str(self.nSeqEvento.valor).zfill(2)

        xml += self.Id.xml
        xml += self.cOrgao.xml
        xml += self.tpAmb.xml

        if self.CNPJ.valor:
            xml += self.CNPJ.xml
        else:
            xml += self.CPF.xml

        xml += self.chNFe.xml
        xml += self.dhEvento.xml
        xml += self.tpEvento.xml
        xml += self.nSeqEvento.xml
        xml += self.verEvento.xml
        xml += self.detEvento.xml
        xml += '</infEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml    = arquivo
            self.cOrgao.xml = arquivo
            self.tpAmb.xml = arquivo
            self.CNPJ.xml = arquivo
            self.CPF.xml = arquivo
            self.chNFe.xml = arquivo
            self.dhEvento.xml = arquivo
            self.tpEvento.xml = arquivo
            self.nSeqEvento.xml = arquivo
            self.verEvento.xml = arquivo
            self.detEvento.xml = arquivo

    xml = property(get_xml, set_xml)


class Evento(XMLNFe):
    def __init__(self):
        super(Evento, self).__init__()
        self.versao    = TagDecimal(nome='evento', codigo='HP04', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.00', raiz='/')
        self.infEvento = InfEvento()
        self.Signature = Signature()
        #self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        #self.arquivo_esquema = 'leiauteSRE_v1.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infEvento.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.infEvento.Id.valor

        xml += self.Signature.xml
        xml += '</evento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infEvento.xml = arquivo
            self.Signature.xml = self._le_noh('//evento/sig:Signature')

    xml = property(get_xml, set_xml)


class InfEventoRecebido(XMLNFe):
    def __init__(self):
        super(InfEventoRecebido, self).__init__()
        self.Id          = TagCaracter(nome='infEvento'  , codigo='HR12', tamanho=[15, 15]    , raiz='//retEvento', propriedade='Id', obrigatorio=False)
        self.tpAmb       = TagInteiro(nome='tpAmb'       , codigo='HR13', tamanho=[1, 1, 1]   , raiz='//retEvento/infEvento', valor=2)
        self.verAplic    = TagCaracter(nome='verAplic'   , codigo='HR14', tamanho=[1, 20]     , raiz='//retEvento/infEvento')
        self.cOrgao      = TagInteiro(nome='cOrgao'      , codigo='HR15', tamanho=[ 2,  2, 2] , raiz='//retEvento/infEvento')
        self.cStat       = TagCaracter(nome='cStat'      , codigo='HR16', tamanho=[3, 3, 3]   , raiz='//retEvento/infEvento')
        self.xMotivo     = TagCaracter(nome='xMotivo'    , codigo='HR17', tamanho=[1, 255]    , raiz='//retEvento/infEvento')
        self.chNFe       = TagCaracter(nome='chNFe'      , codigo='HR18', tamanho=[44, 44, 44], raiz='//retEvento/infEvento', obrigatorio=False)
        self.tpEvento    = TagCaracter(nome='tpEvento'   , codigo='HR19', tamanho=[ 6,  6,  6], raiz='//retEvento/infEvento', obrigatorio=False)
        self.xEvento     = TagCaracter(nome='xEvento'    , codigo='HR20', tamanho=[ 5,  60, 5], raiz='//retEvento/infEvento', obrigatorio=False)
        self.nSeqEvento  = TagInteiro(nome='nSeqEvento'  , codigo='HR21', tamanho=[ 1,  2, 1] , raiz='//retEvento/infEvento', obrigatorio=False)
        self.CNPJDest    = TagCaracter(nome='CNPJDest'   , codigo='HR22', tamanho=[14, 14]    , raiz='//retEvento/infEvento', obrigatorio=False)
        self.CPFDest     = TagCaracter(nome='CPFDest'    , codigo='HR23', tamanho=[11, 11]    , raiz='//retEvento/infEvento', obrigatorio=False)
        self.emailDest   = TagCaracter(nome='emailDest'  , codigo='HR24', tamanho=[1, 60]     , raiz='//retEvento/infEvento', obrigatorio=False)
        self.dhRegEvento = TagDataHoraUTC(nome='dhRegEvento', codigo='HR25',                       raiz='//retEvento/infEvento', obrigatorio=False)
        self.nProt       = TagCaracter(nome='nProt'      , codigo='HR26', tamanho=[15, 15, 15], raiz='//retEvento/infEvento', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.xml:
            xml += self.Id.xml
        else:
            xml += '<infEvento>'

        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cOrgao.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.chNFe.xml
        xml += self.tpEvento.xml
        xml += self.xEvento.xml
        xml += self.nSeqEvento.xml

        if self.CNPJDest.valor:
            xml += self.CNPJDest.xml
        elif self.CPFDest.valor:
            xml += self.CPFDest.xml

        xml += self.emailDest.xml
        xml += self.dhRegEvento.xml
        xml += self.nProt.xml
        xml += '</infEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml          = arquivo
            self.tpAmb.xml       = arquivo
            self.verAplic.xml    = arquivo
            self.cOrgao.xml      = arquivo
            self.cStat.xml       = arquivo
            self.xMotivo.xml     = arquivo
            self.chNFe.xml       = arquivo
            self.tpEvento.xml    = arquivo
            self.xEvento.xml     = arquivo
            self.nSeqEvento.xml  = arquivo
            self.CNPJDest.xml    = arquivo
            self.CPFDest.xml     = arquivo
            self.emailDest.xml   = arquivo
            self.dhRegEvento.xml = arquivo
            self.nProt.xml       = arquivo

    xml = property(get_xml, set_xml)


class RetEvento(XMLNFe):
    def __init__(self):
        super(RetEvento, self).__init__()
        self.versao = TagDecimal(nome='retEvento', codigo='HR10', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.00', raiz='/')
        self.infEvento = InfEventoRecebido()
        self.Signature = Signature()
        #self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        #self.arquivo_esquema = 'leiauteSRE_v1.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infEvento.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != '#'):
            xml += self.Signature.xml

        xml += '</retEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infEvento.xml   = arquivo
            self.Signature.xml = self._le_noh('//retEvento/sig:Signature')

    xml = property(get_xml, set_xml)

    @property
    def protocolo_formatado(self):
        if not self.infEvento.nProt.valor:
            return ''

        formatado = self.infEvento.nProt.valor
        formatado += ' - '
        formatado += self.infEvento.dhRegEvento.formato_danfe
        return formatado


class ProcEvento(XMLNFe):
    def __init__(self):
        super(ProcEvento, self).__init__()
        self.versao = TagDecimal(nome='procEventoNFe', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.00', raiz='/')
        self.evento = Evento()
        self.retEvento = RetEvento()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procEventoNFe_v1.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.evento.xml.replace(ABERTURA, '')
        xml += self.retEvento.xml.replace(ABERTURA, '')
        xml += '</procEventoNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evento.xml = arquivo
            self.retEvento.xml = arquivo

    xml = property(get_xml, set_xml)


class EnvEvento(XMLNFe):
    def __init__(self):
        super(EnvEvento, self).__init__()
        self.versao = TagDecimal(nome='envEvento', codigo='HP02', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.00', raiz='/')
        self.idLote = TagInteiro(nome='idLote'     , codigo='HP03', tamanho=[1, 15, 1], raiz='//envEvento')
        self.evento = []
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'envEvento_v1.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.idLote.xml

        for e in self.evento:
            xml += tira_abertura(e.xml)

        xml += '</envEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.idLote.xml    = arquivo
            self.evento = self.le_grupo('//envEvento/evento', Evento)

    xml = property(get_xml, set_xml)


class RetEnvEvento(XMLNFe):
    def __init__(self):
        super(RetEnvEvento, self).__init__()
        self.versao    = TagDecimal(nome='retEnvEvento', codigo='HR02', propriedade='versao', namespace=NAMESPACE_NFE, valor='1.00', raiz='/')
        self.idLote    = TagInteiro(nome='idLote'     , codigo='HR03', tamanho=[1, 15, 1], raiz='//retEnvEvento')
        self.tpAmb     = TagInteiro(nome='tpAmb'       , codigo='HR04', tamanho=[1, 1, 1]   , raiz='//retEnvEvento', valor=2)
        self.verAplic  = TagCaracter(nome='verAplic'   , codigo='HR05', tamanho=[1, 20]     , raiz='//retEnvEvento')
        self.cOrgao    = TagInteiro(nome='cOrgao'      , codigo='HR06', tamanho=[ 2,  2, 2] , raiz='//retEnvEvento')
        self.cStat     = TagCaracter(nome='cStat'      , codigo='HR07', tamanho=[3, 3, 3]   , raiz='//retEnvEvento')
        self.xMotivo   = TagCaracter(nome='xMotivo'    , codigo='HR08', tamanho=[1, 255]    , raiz='//retEnvEvento')
        self.retEvento = []

        #
        # Dicionário dos retornos, com a chave sendo a chave da NF-e
        #
        self.dic_retEvento = {}
        #
        # Dicionário dos processos (evento + retorno), com a chave sendo a chave da NF-e
        #
        self.dic_procEvento = {}

        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retEnvEvento_v1.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.idLote.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cOrgao.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml

        for r in self.retEvento:
            xml += tira_abertura(r.xml)

        xml += '</retEnvEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.idLote.xml    = arquivo
            self.tpAmb.xml       = arquivo
            self.verAplic.xml    = arquivo
            self.cOrgao.xml      = arquivo
            self.cStat.xml       = arquivo
            self.xMotivo.xml     = arquivo
            self.retEvento = self.le_grupo('//retEnvEvento/retEvento', RetEvento)

            #
            # Monta o dicionário dos retornos
            #
            for ret in self.retEvento:
                self.dic_retEvento[ret.infEvento.chNFe.valor] = ret


    xml = property(get_xml, set_xml)
