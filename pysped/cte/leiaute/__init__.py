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


ESQUEMA_ATUAL_VERSAO_104 = 'pl_104c'

#
# Envelopes SOAP
#
from soap_104 import SOAPEnvio as SOAPEnvio_104
from soap_104 import SOAPRetorno as SOAPRetorno_104

#
# Emissão de CT-e
#
from cte_104 import CTe as CTe_104
from cte_104 import InfNF as InfNF_104
from cte_104 import InfNFe as InfNFe_104
from cte_104 import InfOutros as InfOutros_104
from cte_104 import Pass as Pass_104
from cte_104 import ObsCont as ObsCont_104
from cte_104 import ObsFisco as ObsFisco_104
#from cte_104 import NFRef as NFRef_104
#from cte_104 import Det as Det_104
#from cte_104 import DI as DI_104
#from cte_104 import Adi as Adi_104
#from cte_104 import Med as Med_104
#from cte_104 import Arma as Arma_104
#from cte_104 import Reboque as Reboque_104
#from cte_104 import Vol as Vol_104
#from cte_104 import Lacres as Lacres_104
#from cte_104 import Dup as Dup_104
#from cte_104 import ProcRef as ProcRef_104

#
# Envio de lote de CT-e
#
from envicte_104 import EnviCTe as EnviCTe_104
from envicte_104 import RetEnviCTe as RetEnviCTe_104

#
# Consulta do recibo do lote de CT-e
#
from consrecicte_104 import ConsReciCTe as ConsReciCTe_104
from consrecicte_104 import RetConsReciCTe as RetConsReciCTe_104
from consrecicte_104 import ProtCTe as ProtCTe_104
from consrecicte_104 import ProcCTe as ProcCTe_104

#
# Cancelamento de CT-e
#
from canccte_104 import CancCTe as CancCTe_104
from canccte_104 import RetCancCTe as RetCancCTe_104
from canccte_104 import ProcCancCTe as ProcCancCTe_104

#
# Inutilização de CT-e
#
from inutcte_104 import InutCTe as InutCTe_104
from inutcte_104 import RetInutCTe as RetInutCTe_104
from inutcte_104 import ProcInutCTe as ProcInutCTe_104

#
# Consulta a situação de CT-e
#
from conssitcte_104 import ConsSitCTe as ConsSitCTe_104
from conssitcte_104 import RetConsSitCTe as RetConsSitCTe_104

#
# Consulta a situação do serviço
#
from consstatserv_104 import ConsStatServCTe as ConsStatServCTe_104
from consstatserv_104 import RetConsStatServCTe as RetConsStatServCTe_104

