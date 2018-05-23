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
import sys
from datetime import datetime
import time
from uuid import uuid4
from builtins import str
from io import open


from ..nfe.processador_nfe import ProcessadorNFe, ProcessoNFe as ProcessoCTe
#from .dacte import DACTE

from .webservices_flags import *
from . import webservices

from .leiaute import SOAPEnvio_300, SOAPRetorno_300
from .leiaute import DistDFeInt_100, RetDistDFeInt_100, SOAPEnvioDistDFe_100, SOAPRetornoDistDFe_100


class ProcessadorCTe(ProcessadorNFe):
    def __init__(self):
        super().__init__()
        #self.dacte = DACTE()
        self.versao = '3.00'
        self.modelo = '57'

    def _configura_servico(self, servico, envio, resposta, ambiente=None, somente_ambiente_nacional=False):
        if ambiente is None:
            ambiente = self.ambiente

        #webservices = webservices_3
        metodo_ws = webservices.METODO_WS

        if servico == WS_CTE_DISTRIBUICAO:
            self._soap_envio   = SOAPEnvioDistDFe_100()
            self._soap_retorno = SOAPRetornoDistDFe_100()
        else:
            self._soap_envio   = SOAPEnvio_300()
            self._soap_retorno = SOAPRetorno_300()
            self._soap_envio.versao = self.versao
            self._soap_envio.cteCabecMsg.versao = self.versao
            self._soap_envio.cUF = UF_CODIGO[self.estado]

        if somente_ambiente_nacional:
            ws_a_usar = webservices.AN
        else:
            ws_a_usar = webservices.ESTADO_WS[self.estado]

        self._servidor = ws_a_usar[ambiente]['servidor']
        self._url      = ws_a_usar[ambiente][servico]

        self._soap_envio.webservice = metodo_ws[servico]['webservice']
        self._soap_envio.metodo     = metodo_ws[servico]['metodo']
        self._soap_envio.envio      = envio

        self._soap_retorno.webservice = self._soap_envio.webservice
        self._soap_retorno.metodo     = self._soap_envio.metodo
        self._soap_retorno.resposta   = resposta

    def consultar_distribuicao(self, estado=None, cnpj_cpf=None, ultimo_nsu=None, nsu=None, ambiente=None):
        envio = DistDFeInt_100()
        resposta = RetDistDFeInt_100()

        envio.tpAmb.valor = ambiente or self.ambiente
        envio.cUFAutor.valor = UF_CODIGO[estado or self.estado]

        if len(cnpj_cpf) == 14:
            envio.CNPJ.valor = cnpj_cpf
        else:
            envio.CPF.valor = cnpj_cpf

        if nsu is not None:
            envio.consNSU.NSU.valor = str(nsu)
        else:
            envio.distNSU.ultNSU.valor = ultimo_nsu or '000000000000000'

        processo = ProcessoCTe(webservice=WS_CTE_DISTRIBUICAO, envio=envio, resposta=resposta)

        envio.validar()

        #
        # Monta caminhos para os arquivos DF-e
        #
        if (ambiente or self.ambiente) == 1:
            self.caminho = os.path.join(self.caminho, 'producao/dfe/')
        else:
            self.caminho = os.path.join(self.caminho, 'homologacao/dfe/')
        self.caminho = os.path.join(self.caminho, datetime.now().strftime('%Y-%m') + '/')
        try:
            os.makedirs(self.caminho)
        except:
            pass

        nome_arq = self.caminho + datetime.now().strftime('%Y%m%dT%H%M%S')
        if self.salvar_arquivos:
            arq = open(nome_arq + '-cons-dist-dfe.xml', 'w', encoding='utf-8')
            arq.write(envio.xml)
            arq.close()

        self._conectar_servico(WS_CTE_DISTRIBUICAO, envio, resposta, somente_ambiente_nacional=True)

        #resposta.validar()
        if self.salvar_arquivos:
            arq = open(nome_arq + '-ret-dist-dfe.xml', 'w', encoding='utf-8')
            arq.write(resposta.original.decode('utf-8'))
            arq.close()

        return processo
