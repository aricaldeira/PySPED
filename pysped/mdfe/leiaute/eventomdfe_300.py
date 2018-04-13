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

from pysped.xml_sped import (ABERTURA, NAMESPACE_MDFE, Signature,
                             TagDecimal, TagCaracter, TagDataHoraUTC,
                             TagInteiro, XMLNFe, tira_abertura)
from pysped.mdfe.leiaute import ESQUEMA_ATUAL_VERSAO_3 as ESQUEMA_ATUAL

import os


DIRNAME = os.path.dirname(__file__)


class DetEvento(XMLNFe):
    def __init__(self):
        super(DetEvento, self).__init__()
        self.versaoEvento = TagDecimal(nome='detEvento'  , propriedade='versaoEvento', valor='3.00', raiz='/', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.descEvento = TagCaracter(nome='descEvento', tamanho=[ 5,  60, 5], raiz='//detEvento', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)

    def get_xml(self):
        xml = self.versaoEvento.xml
        xml += self.descEvento.xml
        xml += '</detEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versaoEvento.xml = arquivo
            self.descEvento.xml = arquivo

    xml = property(get_xml, set_xml)

    @property
    def texto_formatado(self):
        return u''


class InfEvento(XMLNFe):
    def __init__(self):
        super(InfEvento, self).__init__()
        self.Id         = TagCaracter(nome='infEvento', tamanho=[54, 54]    , raiz='//eventoMDFe', propriedade='Id', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cOrgao     = TagInteiro(nome='cOrgao'    , tamanho=[ 2,  2, 2] , raiz='//eventoMDFe/infEvento', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.tpAmb      = TagInteiro(nome='tpAmb'     , tamanho=[ 1,  1, 1] , raiz='//eventoMDFe/infEvento', valor=2, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.CNPJ       = TagCaracter(nome='CNPJ'     , tamanho=[14, 14]    , raiz='//eventoMDFe/infEvento', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.CPF        = TagCaracter(nome='CPF'      , tamanho=[11, 11]    , raiz='//eventoMDFe/infEvento', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.chMDFe      = TagCaracter(nome='chMDFe'  , tamanho=[44, 44, 44], raiz='//eventoMDFe/infEvento', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.dhEvento   = TagDataHoraUTC(nome='dhEvento'                    , raiz='//eventoMDFe/infEvento', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.tpEvento   = TagCaracter(nome='tpEvento' , tamanho=[ 6,  6,  6], raiz='//eventoMDFe/infEvento', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.nSeqEvento = TagInteiro(nome='nSeqEvento', tamanho=[ 1,  2, 1] , raiz='//eventoMDFe/infEvento', valor=1, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        #self.verEvento  = TagDecimal(nome='verEvento'                       ,raiz='//eventoMDFe/infEvento', valor='3.00', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.detEvento  = DetEvento()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        self.Id.valor = 'ID' + self.tpEvento.valor + self.chMDFe.valor + str(self.nSeqEvento.valor).zfill(2)

        xml += self.Id.xml
        xml += self.cOrgao.xml
        xml += self.tpAmb.xml

        if self.CNPJ.valor:
            xml += self.CNPJ.xml
        else:
            xml += self.CPF.xml

        xml += self.chMDFe.xml
        xml += self.dhEvento.xml
        xml += self.tpEvento.xml
        xml += self.nSeqEvento.xml
        #xml += self.verEvento.xml
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
            self.chMDFe.xml = arquivo
            self.dhEvento.xml = arquivo
            self.tpEvento.xml = arquivo
            self.nSeqEvento.xml = arquivo
            #self.verEvento.xml = arquivo
            self.detEvento.xml = arquivo

    xml = property(get_xml, set_xml)


class Evento(XMLNFe):
    def __init__(self):
        super(Evento, self).__init__()
        self.versao    = TagDecimal(nome='eventoMDFe', propriedade='versao', namespace=NAMESPACE_MDFE, valor='3.00', raiz='/')
        self.infEvento = InfEvento()
        self.Signature = Signature()
        #self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        #self.arquivo_esquema = 'leiauteSRE_v3.00.xsd'

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
        xml += '</eventoMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infEvento.xml = arquivo
            self.Signature.xml = self._le_noh('//eventoMDFe/sig:Signature')

    xml = property(get_xml, set_xml)


class InfEventoRecebido(XMLNFe):
    def __init__(self):
        super(InfEventoRecebido, self).__init__()
        self.Id          = TagCaracter(nome='infEvento'  , tamanho=[15, 15]    , raiz='//retEventoMDFe', propriedade='Id', obrigatorio=False, namespace=NAMESPACE_MDFE)
        self.tpAmb       = TagInteiro(nome='tpAmb'       , tamanho=[1, 1, 1]   , raiz='//retEventoMDFe/infEvento', valor=2, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.verAplic    = TagCaracter(nome='verAplic'   , tamanho=[1, 20]     , raiz='//retEventoMDFe/infEvento', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cOrgao      = TagInteiro(nome='cOrgao'      , tamanho=[ 2,  2, 2] , raiz='//retEventoMDFe/infEvento', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.cStat       = TagCaracter(nome='cStat'      , tamanho=[3, 3, 3]   , raiz='//retEventoMDFe/infEvento', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.xMotivo     = TagCaracter(nome='xMotivo'    , tamanho=[1, 255]    , raiz='//retEventoMDFe/infEvento', namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.chMDFe      = TagCaracter(nome='chMDFe'     , tamanho=[44, 44, 44], raiz='//retEventoMDFe/infEvento', obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.tpEvento    = TagCaracter(nome='tpEvento'   , tamanho=[ 6,  6,  6], raiz='//retEventoMDFe/infEvento', obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.xEvento     = TagCaracter(nome='xEvento'    , tamanho=[ 5,  60, 5], raiz='//retEventoMDFe/infEvento', obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.nSeqEvento  = TagInteiro(nome='nSeqEvento'  , tamanho=[ 1,  2, 1] , raiz='//retEventoMDFe/infEvento', obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.CNPJDest    = TagCaracter(nome='CNPJDest'   , tamanho=[14, 14]    , raiz='//retEventoMDFe/infEvento', obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.CPFDest     = TagCaracter(nome='CPFDest'    , tamanho=[11, 11]    , raiz='//retEventoMDFe/infEvento', obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.emailDest   = TagCaracter(nome='emailDest'  , tamanho=[1, 60]     , raiz='//retEventoMDFe/infEvento', obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.dhRegEvento = TagDataHoraUTC(nome='dhRegEvento'                   , raiz='//retEventoMDFe/infEvento', obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)
        self.nProt       = TagCaracter(nome='nProt'      , tamanho=[15, 15, 15], raiz='//retEventoMDFe/infEvento', obrigatorio=False, namespace=NAMESPACE_MDFE, namespace_obrigatorio=False)

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
        xml += self.chMDFe.xml
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
            self.chMDFe.xml       = arquivo
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
        self.versao = TagDecimal(nome='retEventoMDFe', propriedade='versao', namespace=NAMESPACE_MDFE, valor='3.00', raiz='/')
        self.infEvento = InfEventoRecebido()
        self.Signature = Signature()
        #self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        #self.arquivo_esquema = 'leiauteSRE_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infEvento.xml

        if len(self.Signature.URI) and (self.Signature.URI.strip() != '#'):
            xml += self.Signature.xml

        xml += '</retEventoMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infEvento.xml   = arquivo
            self.Signature.xml = self._le_noh('//retEventoMDFe/sig:Signature')

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
        self.versao = TagDecimal(nome='procEventoMDFe', propriedade='versao', namespace=NAMESPACE_MDFE, valor='3.00', raiz='/')
        self.eventoMDFe = Evento()
        self.retEventoMDFe = RetEvento()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'procEventoMDFe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.eventoMDFe.xml.replace(ABERTURA, '')
        xml += self.retEventoMDFe.xml.replace(ABERTURA, '')
        xml += '</procEventoMDFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.eventoMDFe.xml = arquivo
            self.retEventoMDFe.xml = arquivo

    xml = property(get_xml, set_xml)
