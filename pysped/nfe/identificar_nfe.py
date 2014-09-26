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

from __future__ import division, print_function, unicode_literals

import os
import re
from lxml import etree

from leiaute import *
from pysped.xml_sped import XMLNFe, tira_abertura
from pysped.xml_sped.certificado import Certificado


MAPA_ESQUEMAS = {}

for tipo in dir():
    if type(eval(tipo)) == type and issubclass(eval(tipo), XMLNFe) and eval(tipo + '().arquivo_esquema'):
            MAPA_ESQUEMAS[tipo] = os.path.join(eval(tipo + '().caminho_esquema'), eval(tipo + '().arquivo_esquema'))


LIMPA_ESPACO_ENTRE_TAGS = re.compile(r'(>)\s+(<)')


def valida_codificacao(arq_xml):
    try:
        xml = open(arq_xml).read()
        xml = xml.decode('utf-8')

        #
        # Remove caracteres desnecessários
        #
        xml = xml.replace('\r', '')
        xml = xml.replace('\n', '')

        #
        # Remove espaços entre as tags
        #
        xml = LIMPA_ESPACO_ENTRE_TAGS.sub(r'\1\2', xml)

        #
        # Tira tag de abertura com a codificação
        #
        xml = tira_abertura(xml)
    except:
        return ''

    return xml


def correcoes_xml(xml):
    CORRECOES = [
        #
        # Corrige falta de versão no CT-e
        #
        ('<cteProc xmlns="http://www.portalfiscal.inf.br/cte" versao="">', '<cteProc xmlns="http://www.portalfiscal.inf.br/cte" versao="1.04">'),
        ('<cteProc versao="1.04" xmlns="http://www.portalfiscal.inf.br/cte" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.portalfiscal.inf.br/cte procCTe_v1.04.xsd">', '<cteProc xmlns="http://www.portalfiscal.inf.br/cte" versao="1.04">'),

        #
        # Corrige schema da assinatura no lugar errado
        #
        ('<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.portalfiscal.inf.br/nfe procNFe_v2.00.xsd" versao="2.00">', '<nfeProc versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe">'),

        ('<nfeProc versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance&quot;">', '<nfeProc versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe">'),

        ('<nfeProc versao="2.00" xmlns:ns2="http://www.w3.org/2000/09/xmldsig#" xmlns="http://www.portalfiscal.inf.br/nfe">', '<nfeProc versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe">'),

        ('<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" versao="2.00">', '<nfeProc versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe">'),

        ('<nfeProc versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.portalfiscal.inf.br/nfe procNFe_v2.00.xsd">', '<nfeProc versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe">'),

        ('<nfeProc xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe">', '<nfeProc versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe">'),

        ('<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" versao="2.00">', '<nfeProc versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe">'),

        ('<nfeProc versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">', '<nfeProc versao="2.00" xmlns="http://www.portalfiscal.inf.br/nfe">'),
    ]

    for errado, certo in CORRECOES:
        if errado in xml:
            xml = xml.replace(errado, certo)

    return xml


def valida_esquema(xml, tipo):
    arquivo_esquema = MAPA_ESQUEMAS[tipo]
    esquema = etree.XMLSchema(etree.parse(arquivo_esquema))

    #try:
    esquema.validate(etree.fromstring(xml.encode('utf-8')))
    erros = esquema.error_log
    #except:
        #return [False]

    return erros


def identifica_xml(xml, cria_instancia=False):
    tipos = []

    for tipo in MAPA_ESQUEMAS:
        erros = valida_esquema(xml, tipo)

        if len(erros) == 0:
            #
            # Tenta identificar o tipo exato do evento
            #
            if issubclass(eval(tipo), EnvEvento_100):
                if not tipo == 'EnvEvento_100':
                    #if valida_esquema.evento[0].infEvento.tpEvento.xml in arq:
                    tipos += [tipo]

            elif issubclass(eval(tipo), RetEnvEvento_100):
                if not tipo == 'RetEnvEvento_100':
                    #if valida_esquema.retEvento[0].infEvento.tpEvento.xml in arq:
                    tipos += [tipo]

            elif issubclass(eval(tipo), Evento_100):
                if not tipo == 'Evento_100':
                    #if valida_esquema.infEvento.tpEvento.xml in arq:
                    tipos += [tipo]

            elif issubclass(eval(tipo), RetEvento_100):
                if not tipo == 'RetEvento_100':
                    #if valida_esquema.infEvento.tpEvento.xml in arq:
                    tipos += [tipo]

            elif issubclass(eval(tipo), ProcEvento_100):
                if not tipo == 'ProcEvento_100':
                    #if valida_esquema.evento.infEvento.tpEvento.xml in arq:
                    tipos += [tipo]

            else:
                tipos += [tipo]

    if cria_instancia:
        instancia = eval(tipos[0] + '()')
        instancia.xml = xml
        return instancia, tipos[0]

    return tipos


def valida_assinatura(xml, arq_xml, tipo):
    if tipo not in ('NFe_110', 'CancNFe_107', 'InutNFe_107', 'ProcNFe_110', 'EnviNFe_110',
                    'NFe_200', 'CancNFe_200', 'InutNFe_200', 'ProcNFe_200', 'EnviNFe_200',
                    'NFe_310', 'InutNFe_310', 'ProcNFe_310', 'EnviNFe_310',
                    'CTe_104', 'CancCTe_104', 'InutCTe_104', 'ProcCTe_104', 'EnviCTe_104',
                    'Evento_100', 'EnvEvento_100', 'ProcEvento_100',
                    'EventoCCe_100', 'EnvEventoCCe_100', 'ProcEventoCCe_100',
                    'EventoCancNFe_100', 'EnvEventoCancNFe_100', 'ProcEventoCancNFe_100',
                    'EventoConfRecebimento_100', 'EnvEventoConfRecebimento_100', 'ProcEventoConfRecebimento_100'):
        return True

    assinatura_valida = False
    try:
        c = Certificado()
        assinatura_valida = c.verifica_assinatura_xml(xml)
    except:
        pass

    if not assinatura_valida:
        try:
            assinatura_valida = c.verifica_assinatura_arquivo(arq_xml)
        except:
            pass

    return assinatura_valida
