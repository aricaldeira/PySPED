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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtAltCadastral/v02_04_02'


class Contato(XMLNFe):
    def __init__(self):
        super(Contato, self).__init__()
        self.fonePrinc     = TagCaracter(nome='fonePrinc'    , tamanho=[1, 13], raiz='//contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.foneAlternat  = TagCaracter(nome='foneAlternat' , tamanho=[1, 13], raiz='//contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.emailPrinc    = TagCaracter(nome='emailPrinc'   , tamanho=[1, 60], raiz='//contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.emailAlternat = TagCaracter(nome='emailAlternat', tamanho=[1, 60], raiz='//contato', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<contato>'
        xml += self.fonePrinc.xml
        xml += self.foneAlternat.xml
        xml += self.emailPrinc.xml
        xml += self.emailAlternat.xml
        xml += '</contato>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.fonePrinc.xml = arquivo
            self.foneAlternat.xml = arquivo
            self.emailPrinc.xml = arquivo
            self.emailAlternat.xml = arquivo

    xml = property(get_xml, set_xml)


class Aposentadoria(XMLNFe):
    def __init__(self):
        super(Aposentadoria, self).__init__()
        self.trabAposent = TagCaracter(nome='trabAposent', tamanho=[1, 1], raiz='//aposentadoria', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<aposentadoria>'
        xml += self.trabAposent.xml
        xml += '</aposentadori>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.trabAposent.xml = arquivo

    xml = property(get_xml, set_xml)


class Dependente(XMLNFe):
    def __init__(self):
        super(Dependente, self).__init__()
        self.tpDep            = TagCaracter(nome='tpDep'           , tamanho=[1,  2], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmDep            = TagCaracter(nome='nmDep'           , tamanho=[1, 70], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtNascto         = TagData(    nome='dtNascto'        ,                  raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cpfDep           = TagCaracter(nome='cpfDep'          , tamanho=[1, 11], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.depIRRF          = TagCaracter(nome='depIRRF'         , tamanho=[1,  1], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.depSF            = TagCaracter(nome='depSF'           , tamanho=[1,  1], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.incTrab          = TagCaracter(nome='incTrab'         , tamanho=[1,  1], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dependente>'
        xml += self.tpDep.xml
        xml += self.nmDep.xml
        xml += self.dtNascto.xml
        xml += self.cpfDep.xml
        xml += self.depIRRF.xml
        xml += self.depSF.xml
        xml += self.incTrab.xml
        xml += '</dependente>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpDep.xml = arquivo
            self.nmDep.xml = arquivo
            self.dtNascto.xml = arquivo
            self.cpfDep.xml = arquivo
            self.depIRRF.xml = arquivo
            self.depSF.xml = arquivo
            self.incTrab.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoDeficiencia(XMLNFe):
    def __init__(self):
        super(InfoDeficiencia, self).__init__()
        self.defFisica        = TagCaracter(nome='defFisica'       , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.defVisual        = TagCaracter(nome='defVisual'       , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.defAuditiva      = TagCaracter(nome='defAuditiva'     , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.defMental        = TagCaracter(nome='defMental'       , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.defIntelectual   = TagCaracter(nome='defIntelectual'  , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.reabReadp        = TagCaracter(nome='reabReadp'       , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoCota         = TagCaracter(nome='infoCota'        , tamanho=[1,   1], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.observacao       = TagCaracter(nome='observacao'      , tamanho=[1, 255], raiz='//infoDeficiencia', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoDeficiencia>'
        xml += self.defFisica.xml
        xml += self.defVisual.xml
        xml += self.defAuditiva.xml
        xml += self.defMental.xml
        xml += self.defIntelectual.xml
        xml += self.reabReadp.xml
        xml += self.infoCota.xml
        xml += self.observacao.xml
        xml += '</infoDeficiencia>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.defFisica.xml = arquivo
            self.defVisual.xml = arquivo
            self.defAuditiva.xml = arquivo
            self.defMental.xml = arquivo
            self.defIntelectual.xml = arquivo
            self.reabReadp.xml = arquivo
            self.infoCota.xml = arquivo
            self.observacao.xml = arquivo

    xml = property(get_xml, set_xml)


class TrabEstrangeiro(XMLNFe):
    def __init__(self):
        super(TrabEstrangeiro, self).__init__()
        self.dtChegada        = TagData(    nome='dtChegada'       ,                 raiz='//trabEstrangeiro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.classTrabEstrang = TagCaracter(nome='classTrabEstrang', tamanho=[1, 2], raiz='//trabEstrangeiro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.casadoBr         = TagCaracter(nome='casadoBr'        , tamanho=[1, 1], raiz='//trabEstrangeiro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.filhosBr          = TagCaracter(nome='filhosBr'        , tamanho=[1, 1], raiz='//trabEstrangeiro', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<trabEstrangeiro>'
        xml += self.dtChegada.xml
        xml += self.classTrabEstrang.xml
        xml += self.casadoBr.xml
        xml += self.filhosBr.xml
        xml += '</trabEstrangeiro>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtChegada.xml = arquivo
            self.classTrabEstrang.xml = arquivo
            self.casadoBr.xml = arquivo
            self.filhosBr.xml = arquivo

    xml = property(get_xml, set_xml)


class Exterior(XMLNFe):
    def __init__(self):
        super(Exterior, self).__init__()
        self.paisResid    = TagCaracter(nome='paisResid'   , tamanho=[1,  3], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscLograd    = TagCaracter(nome='dscLograd'   , tamanho=[1, 80], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrLograd     = TagCaracter(nome='nrLograd'    , tamanho=[1, 10], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.complemento  = TagCaracter(nome='complemento' , tamanho=[1, 30], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.bairro       = TagCaracter(nome='bairro'      , tamanho=[1, 60], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmCid        = TagCaracter(nome='nmCid'       , tamanho=[1, 50], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codPostal    = TagCaracter(nome='codPostal'   , tamanho=[1, 12], raiz='//Exterior', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<exterior>'
        xml += self.paisResid.xml
        xml += self.dscLograd.xml
        xml += self.nrLograd.xml
        xml += self.complemento.xml
        xml += self.bairro.xml
        xml += self.nmCid.xml
        xml += self.codPostal.xml
        xml += '</exterior>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.paisResid.xml = arquivo
            self.dscLograd.xml = arquivo
            self.nrLograd.xml = arquivo
            self.complemento.xml = arquivo
            self.bairro.xml = arquivo
            self.nmCid.xml = arquivo
            self.codPostal.xml = arquivo

    xml = property(get_xml, set_xml)


class Brasil(XMLNFe):
    def __init__(self):
        super(Brasil, self).__init__()
        self.tpLograd     = TagCaracter(nome='tpLograd'    , tamanho=[1,  4], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscLograd    = TagCaracter(nome='dscLograd'   , tamanho=[1, 80], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrLograd     = TagCaracter(nome='nrLograd'    , tamanho=[1, 10], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.complemento  = TagCaracter(nome='complemento' , tamanho=[1, 30], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.bairro       = TagCaracter(nome='bairro'      , tamanho=[1, 60], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.cep          = TagCaracter(nome='cep'         , tamanho=[1,  8], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMunic     = TagCaracter(nome='codMunic'    , tamanho=[1,  7], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.uf           = TagCaracter(nome='uf'          , tamanho=[1,  2], raiz='//Brasil', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<brasil>'
        xml += self.tpLograd.xml
        xml += self.dscLograd.xml
        xml += self.nrLograd.xml
        xml += self.complemento.xml
        xml += self.bairro.xml
        xml += self.cep.xml
        xml += self.codMunic.xml
        xml += self.uf.xml
        xml += '</brasil>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpLograd.xml = arquivo
            self.dscLograd.xml = arquivo
            self.nrLograd.xml = arquivo
            self.complemento.xml = arquivo
            self.bairro.xml = arquivo
            self.cep.xml = arquivo
            self.codMunic.xml = arquivo
            self.uf.xml = arquivo

    xml = property(get_xml, set_xml)


class CNH(XMLNFe):
    def __init__(self):
        super(CNH, self).__init__()
        self.nrRegCnh     = TagCaracter(nome='nrRegCnh'    , tamanho=[1, 12], raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtExped      = TagData(    nome='dtExped'     ,                  raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.ufCnh        = TagCaracter(nome='ufCnh'       , tamanho=[1,  2], raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtValid      = TagData(    nome='dtValid'     ,                  raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtPriHab     = TagData(    nome='dtPriHab'    ,                  raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.categoriaCnh = TagCaracter(nome='categoriaCnh', tamanho=[1,  2], raiz='//CNH', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<CNH>'
        xml += self.nrRegCnh.xml
        xml += self.dtExped.xml
        xml += self.ufCnh.xml
        xml += self.dtValid.xml
        xml += self.dtPriHab.xml
        xml += self.categoriaCnh.xml
        xml += '</CNH>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRegCnh.xml = arquivo
            self.dtExped.xml = arquivo
            self.ufCnh.xml = arquivo
            self.dtValid.xml = arquivo
            self.dtPriHab.xml = arquivo
            self.categoriaCnh.xml = arquivo

    xml = property(get_xml, set_xml)


class OC(XMLNFe):
    def __init__(self):
        super(OC, self).__init__()
        self.nrOc         = TagCaracter(nome='nrOc'        , tamanho=[1, 14], raiz='//OC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.orgaoEmissor = TagCaracter(nome='orgaoEmissor', tamanho=[1, 20], raiz='//OC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtExped      = TagData(    nome='dtExped'     ,                  raiz='//OC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtValid      = TagData(    nome='dtValid'     ,                  raiz='//OC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<OC>'
        xml += self.nrOc.xml
        xml += self.orgaoEmissor.xml
        xml += self.dtExped.xml
        xml += self.dtValid.xml
        xml += '</OC>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrOc.xml = arquivo
            self.orgaoEmissor.xml = arquivo
            self.dtExped.xml = arquivo
            self.dtValid.xml = arquivo

    xml = property(get_xml, set_xml)


class RNE(XMLNFe):
    def __init__(self):
        super(RNE, self).__init__()
        self.nrRne        = TagCaracter(nome='nrRne'       , tamanho=[1, 14], raiz='//RNE', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.orgaoEmissor = TagCaracter(nome='orgaoEmissor', tamanho=[1, 20], raiz='//RNE', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtExped      = TagData(    nome='dtExped'     ,                  raiz='//RNE', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RNE>'
        xml += self.nrRne.xml
        xml += self.orgaoEmissor.xml
        xml += self.dtExped.xml
        xml += '</RNE>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRne.xml = arquivo
            self.orgaoEmissor.xml = arquivo
            self.dtExped.xml = arquivo

    xml = property(get_xml, set_xml)


class RG(XMLNFe):
    def __init__(self):
        super(RG, self).__init__()
        self.nrRg         = TagCaracter(nome='nrRg'        , tamanho=[1, 14], raiz='//RG', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.orgaoEmissor = TagCaracter(nome='orgaoEmissor', tamanho=[1, 20], raiz='//RG', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtExped      = TagData(    nome='dtExped'     ,                  raiz='//RG', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RG>'
        xml += self.nrRg.xml
        xml += self.orgaoEmissor.xml
        xml += self.dtExped.xml
        xml += '</RG>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRg.xml = arquivo
            self.orgaoEmissor.xml = arquivo
            self.dtExped.xml = arquivo

    xml = property(get_xml, set_xml)


class RIC(XMLNFe):
    def __init__(self):
        super(RIC, self).__init__()
        self.nrRic        = TagCaracter(nome='nrRic'       , tamanho=[1, 14], raiz='//RIC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.orgaoEmissor = TagCaracter(nome='orgaoEmissor', tamanho=[1, 20], raiz='//RIC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtExped      = TagData(    nome='dtExped'     ,                  raiz='//RIC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<RIC>'
        xml += self.nrRic.xml
        xml += self.orgaoEmissor.xml
        xml += self.dtExped.xml
        xml += '</RIC>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRic.xml = arquivo
            self.orgaoEmissor.xml = arquivo
            self.dtExped.xml = arquivo

    xml = property(get_xml, set_xml)


class CTPS(XMLNFe):
    def __init__(self):
        super(CTPS, self).__init__()
        self.nrCtps    = TagCaracter(nome='nrCtps'   , tamanho=[1, 11], raiz='//CTPS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.serieCtps = TagCaracter(nome='serieCtps', tamanho=[1,  5], raiz='//CTPS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ufCtps    = TagCaracter(nome='ufCtps'   , tamanho=[1,  2], raiz='//CTPS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<CTPS>'
        xml += self.nrCtps.xml
        xml += self.serieCtps.xml
        xml += self.ufCtps.xml
        xml += '</CTPS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrCtps.xml = arquivo
            self.serieCtps.xml = arquivo
            self.ufCtps.xml = arquivo

    xml = property(get_xml, set_xml)


class Endereco(XMLNFe):
    def __init__(self):
        super(Endereco, self).__init__()
        self.brasil = Brasil()
        self.exterior = Exterior()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<endereco>'
        xml += self.brasil.xml
        xml += '</endereco>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.brasil = self.le_grupo('//eSocial/evtAltContratual/trabalhador/endereco/brasil', CTPS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.exterior = self.le_grupo('//eSocial/evtAltContratual/trabalhador/endereco/exterior', CTPS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Documentos(XMLNFe):
    def __init__(self):
        super(Documentos, self).__init__()
        self.CTPS        = []
        self.RIC         = []
        self.RG          = []
        self.RNE         = []
        self.OC          = []
        self.CNH         = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<documentos>'
        if len(self.CTPS) > 0:
            for c in self.CTPS:
                xml += c.xml
        if len(self.RIC) > 0:
            for r in self.RIC:
                xml += r.xml
        if len(self.RG) > 0:
            for r in self.RG:
                xml += r.xml
        if len(self.RNE) > 0:
            for r in self.RNE:
                xml += r.xml
        if len(self.OC) > 0:
            for o in self.OC:
                xml += o.xml
        if len(self.CNH) > 0:
            for c in self.CNH:
                xml += c.xml
        xml += '</documentos>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CTPS = self.le_grupo('//eSocial/evtAltContratual/trabalhador/documentos/CTPS', CTPS, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.RIC  = self.le_grupo('//eSocial/evtAltContratual/trabalhador/documentos/RIC' , RIC , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.RG   = self.le_grupo('//eSocial/evtAltContratual/trabalhador/documentos/RG'  , RG  , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.RNE  = self.le_grupo('//eSocial/evtAltContratual/trabalhador/documentos/RNE' , RNE , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.OC   = self.le_grupo('//eSocial/evtAltContratual/trabalhador/documentos/OC'  , OC  , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.CNH  = self.le_grupo('//eSocial/evtAltContratual/trabalhador/documentos/CNH' , CNH , namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Nascimento(XMLNFe):
    def __init__(self):
        super(Nascimento, self).__init__()
        self.dtNascto    = TagData(    nome='dtNascto'  ,                  raiz='//eSocial/evtAltContratual/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMunic    = TagCaracter(nome='codMunic'  , tamanho=[1, 7] , raiz='//eSocial/evtAltContratual/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.uf          = TagCaracter(nome='uf'        , tamanho=[1, 2] , raiz='//eSocial/evtAltContratual/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.paisNascto  = TagCaracter(nome='paisNascto', tamanho=[1, 3] , raiz='//eSocial/evtAltContratual/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.paisNac     = TagCaracter(nome='paisNac'   , tamanho=[1, 3] , raiz='//eSocial/evtAltContratual/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmMae       = TagCaracter(nome='nmMae'     , tamanho=[1, 70], raiz='//eSocial/evtAltContratual/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmPai       = TagCaracter(nome='nmPai'     , tamanho=[1, 70], raiz='//eSocial/evtAltContratual/trabalhador/nascimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<nascimento>'
        xml += self.dtNascto.xml
        xml += self.codMunic.xml
        xml += self.uf.xml
        xml += self.paisNascto.xml
        xml += self.paisNac.xml
        xml += self.nmMae.xml
        xml += self.nmPai.xml
        xml += '</nascimento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtNascto.xml = arquivo
            self.codMunic.xml = arquivo
            self.uf.xml = arquivo
            self.paisNascto.xml = arquivo
            self.paisNac.xml = arquivo
            self.nmMae.xml = arquivo
            self.nmPai.xml = arquivo

    xml = property(get_xml, set_xml)


class DadosTrabalhador(XMLNFe):
    def __init__(self):
        super(DadosTrabalhador, self).__init__()
        self.nisTrab = TagCaracter(nome='nisTrab', tamanho=[1, 11], raiz='//eSocial/evtAltContratual/alteracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmTrab = TagCaracter(nome='nmTrab', tamanho=[1, 70], raiz='//eSocial/evtAltContratual/alteracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.sexo = TagCaracter(nome='sexo', tamanho=[1, 1], raiz='//eSocial/evtAltContratual/alteracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.racaCor = TagCaracter(nome='racaCor', tamanho=[1, 1], raiz='//eSocial/evtAltContratual/alteracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.estCiv = TagCaracter(nome='estCiv', tamanho=[1, 1], raiz='//eSocial/evtAltContratual/alteracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False,obrigatorio=False)
        self.grauInstr = TagCaracter(nome='grauInstr', tamanho=[1, 2], raiz='//eSocial/evtAltContratual/alteracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmSoc = TagCaracter(nome='nmSoc', tamanho=[1, 70], raiz='//eSocial/evtAltContratual/alteracao/', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nascimento = Nascimento()
        self.documentos = Documentos()
        self.endereco = Endereco()
        self.trabEstrangeiro = []
        self.infoDeficiencia = []
        self.dependente = []
        self.aposentadoria = []
        self.contato = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosTrabalhador>'
        xml += self.nisTrab.xml
        xml += self.nmTrab.xml
        xml += self.sexo.xml
        xml += self.racaCor.xml
        xml += self.estCiv.xml
        xml += self.grauInstr.xml
        xml += self.nmSoc.xml
        xml += self.nascimento.xml
        xml += self.documentos.xml
        xml += self.endereco.xml
        if len(self.trabEstrangeiro) > 0:
            for t in self.trabEstrangeiro:
                xml += t.xml
        if len(self.infoDeficiencia) > 0:
            for i in self.infoDeficiencia:
                xml += i.xml
        if len(self.dependente) > 0:
            for d in self.dependente:
                xml += d.xml
        if len(self.aposentadoria) > 0:
            for a in self.aposentadoria:
                xml += a.xml
        if len(self.contato) > 0:
            for c in self.contato:
                xml += c.xml
        xml += '</dadosTrabalhador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nisTrab.xml = arquivo
            self.nmTrab.xml = arquivo
            self.sexo.xml = arquivo
            self.racaCor.xml = arquivo
            self.estCiv.xml = arquivo
            self.grauInstr.xml = arquivo
            self.nmSoc.xml = arquivo
            self.nascimento.xml = arquivo
            self.documentos.xml = arquivo
            self.endereco.xml = arquivo
            self.trabEstrangeiro = self.le_grupo(
                '//eSocial/evtAltContratual/alteracao/trabEstrangeiro',
                TrabEstrangeiro, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoDeficiencia = self.le_grupo(
                '//eSocial/evtAltContratual/alteracao/infoDeficiencia',
                InfoDeficiencia, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.dependente = self.le_grupo(
                '//eSocial/evtAltContratual/alteracao/dependente', Dependente,
                namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.aposentadoria = self.le_grupo(
                '//eSocial/evtAltContratual/alteracao/aposentadoria',
                Aposentadoria, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.contato = self.le_grupo(
                '//eSocial/evtAltContratual/alteracao/contato', Contato,
                namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Alteracao(XMLNFe):
    def __init__(self):
        super(Alteracao, self).__init__()
        self.dtAlteracao = TagData(nome='dtAlteracao', raiz='//eSocial/evtAltContratual/alteracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dadosTrabalhador = DadosTrabalhador()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<alteracao>'
        xml += self.dtAlteracao.xml
        xml += self.dadosTrabalhador.xml
        xml += '</alteracao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtAlteracao.xml = arquivo
            self.dadosTrabalhador.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeTrabalhador(XMLNFe):
    def __init__(self):
        super(IdeTrabalhador, self).__init__()
        self.cpfTrab    = TagCaracter(nome='cpfTrab'   , tamanho=[1, 11], raiz='//eSocial/evtAltContratual/ideTrabalhador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideTrabalhador>'
        xml += self.cpfTrab.xml
        xml += '</ideTrabalhador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrab.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtAltContratual/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtAltContratual/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif = TagInteiro( nome='indRetif', raiz='//eSocial/evtAltCadastral/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', raiz='//eSocial/evtAltCadastral/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpAmb    = TagInteiro( nome='tpAmb'   , raiz='//eSocial/evtAltCadastral/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi  = TagInteiro( nome='procEmi' , raiz='//eSocial/evtAltCadastral/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc  = TagCaracter(nome='verProc' , raiz='//eSocial/evtAltCadastral/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtAltCadastral(XMLNFe):
    def __init__(self):
        super(EvtAltCadastral, self).__init__()
        self.Id = TagCaracter(nome='evtAltCadastral', propriedade='Id', raiz='//eSocial/evtAltCadastral', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideTrabalhador = IdeTrabalhador()
        self.alteracao = Alteracao()
        # self.vinculo = Vinculo()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideTrabalhador.xml
        xml += self.alteracao.xml
        xml += '</evtAltCadastral>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideTrabalhador.xml = arquivo
            self.alteracao.xml = arquivo

    xml = property(get_xml, set_xml)


class S2205(XMLNFe):
    def __init__(self):
        super(S2205, self).__init__()
        self.evtAltCadastral = EvtAltCadastral()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtAltCadastral.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtAltCadastral
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtAltCadastral.xml
        xml += '</eSocial>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtAltCadastral.xml = arquivo

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
        self.evtAltCadastral.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
