# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Wagner Pereira <wagner.pereira at tauga.com.br>
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

#
# Versão 1.03.02
#
ESQUEMA_ATUAL_VERSAO_1 = 'v1.03.02'


from .soap_10100 import SOAPEnvio as SOAPEnvio_10100
from .soap_10100 import SOAPRetorno as SOAPRetorno_10100

from .envioLoteEvento_10302 import LoteEventoEFDReinf as LoteEventoEFDReinf_v1_03_02
from .retornoLoteEventos_10302 import RetornoLoteEventos as RetornoLoteEventosEFDReinf_v1_03_02
from .retornoTotalizadorEvento_10302 import RetornoTotalizadorEvento as RetornoTotalizadorEventoEFDReinf_v1_03_02

from .evtInfoContribuinte_10302 import R1000 as R1000_1

from .evtTomadorServicos_10302 import R2010 as R2010_1
from .evtTomadorServicos_10302 import NFS as NFS_1
from .evtTomadorServicos_10302 import InfoTpServ as InfoTpServ_1