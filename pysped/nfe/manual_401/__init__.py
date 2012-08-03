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


ESQUEMA_ATUAL = u'pl_006g'


#
# Envelopes SOAP
#
from soap_200 import SOAPEnvio as SOAPEnvio_200
from soap_200 import SOAPRetorno as SOAPRetorno_200

#
# Emissão de NF-e
#
from nfe_200 import NFe as NFe_200
from nfe_200 import NFRef as NFRef_200
from nfe_200 import Det as Det_200
from nfe_200 import DI as DI_200
from nfe_200 import Adi as Adi_200
from nfe_200 import Med as Med_200
from nfe_200 import Arma as Arma_200
from nfe_200 import Reboque as Reboque_200
from nfe_200 import Vol as Vol_200
from nfe_200 import Lacres as Lacres_200
from nfe_200 import Dup as Dup_200
from nfe_200 import ObsCont as ObsCont_200
from nfe_200 import ObsFisco as ObsFisco_200
from nfe_200 import ProcRef as ProcRef_200

#
# Envio de lote de NF-e
#
from envinfe_200 import EnviNFe as EnviNFe_200
from envinfe_200 import RetEnviNFe as RetEnviNFe_200

#
# Consulta do recibo do lote de NF-e
#
from consrecinfe_200 import ConsReciNFe as ConsReciNFe_200
from consrecinfe_200 import RetConsReciNFe as RetConsReciNFe_200
from consrecinfe_200 import ProtNFe as ProtNFe_200
from consrecinfe_200 import ProcNFe as ProcNFe_200

#
# Cancelamento de NF-e
#
from cancnfe_200 import CancNFe as CancNFe_200
from cancnfe_200 import RetCancNFe as RetCancNFe_200
from cancnfe_200 import ProcCancNFe as ProcCancNFe_200

#
# Inutilização de NF-e
#
from inutnfe_200 import InutNFe as InutNFe_200
from inutnfe_200 import RetInutNFe as RetInutNFe_200
from inutnfe_200 import ProcInutNFe as ProcInutNFe_200

#
# Consulta a situação de NF-e
#
from conssitnfe_200 import ConsSitNFe as ConsSitNFe_200
from conssitnfe_200 import RetConsSitNFe as RetConsSitNFe_200

#
# Consulta a situação do serviço
#
from consstatserv_200 import ConsStatServ as ConsStatServ_200
from consstatserv_200 import RetConsStatServ as RetConsStatServ_200

#
# Consulta cadastro
#
#from conscad_101 import ConsCad as ConsCad_101
#from conscad_101 import RetConsCad as RetConsCad_101
