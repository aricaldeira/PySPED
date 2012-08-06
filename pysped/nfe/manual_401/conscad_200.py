# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Affero General Public License,
# publicada pela Free Software Foundation, em sua versão 3 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Affero General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Affero General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import division, print_function, unicode_literals

from base import *
from soap_100 import conectar_servico
from soap_200 import SOAPEnvio, SOAPRetorno
import conscad_101


class ConsCad(conscad_101.ConsCad):
    versao = TagDecimal(nome=u'ConsCad', codigo=u'GP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
    caminho_esquema = u'schema/pl_006e/'
    arquivo_esquema = u'consCad_v2.00.xsd'


    def _servico(self):
        envio = SOAPEnvio()
        envio.wsdl = u'CadConsultaCadastro2'
        envio.servico = u'consultaCadastro2'
        envio.nfeCabecMsg.cUF.valor = 35
        envio.nfeCabecMsg.versaoDados.valor = self.versao.valor
        envio.nfeDadosMsg.dados = self

        retorno = SOAPRetorno()
        retorno.wsdl = envio.wsdl
        retorno.servico = envio.servico
        self.retorno = RetConsCad()
        retorno.resposta = self.retorno

        conectar_servico(envio, retorno, self.certificado, self.senha)


class RetConsCad(conscad_101.RetConsCad):
    versao    = TagDecimal(nome=u'retConsCad', codigo=u'GR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
    caminho_esquema = u'schema/pl_006e/'
    arquivo_esquema = u'retConsCad_v2.00.xsd'
