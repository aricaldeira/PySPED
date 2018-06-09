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

import sys
import locale

if sys.version_info.major == 2:
    locale.setlocale(locale.LC_ALL, b'pt_BR.UTF-8')
    locale.setlocale(locale.LC_COLLATE, b'pt_BR.UTF-8')
else:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')

from pysped.nfe.leiaute import *
from pysped.cte.leiaute import *
from pysped.mdfe.leiaute import *
from pysped.esocial.leiaute import *
from pysped.efdreinf.leiaute import *

from pysped.nfe.processador_nfe import ProcessadorNFe, Certificado
from pysped.cte.processador_cte import ProcessadorCTe
from pysped.mdfe.processador_mdfe import ProcessadorMDFe
from pysped.esocial.processador_esocial import ProcessadorESocial
from pysped.efdreinf.processador_efdreinf import ProcessadorEFDReinf

from pysped.nfse.processador_nfse import ProcessadorNFSe
