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

from pysped.cte.leiaute.canccte_104 import CancCTe as CancCTe_104
from pysped.cte.leiaute.canccte_104 import ProcCancCTe as ProcCancCTe_104
from pysped.cte.leiaute.canccte_104 import RetCancCTe as RetCancCTe_104
from pysped.cte.leiaute.consrecicte_104 import ConsReciCTe as ConsReciCTe_104
from pysped.cte.leiaute.consrecicte_104 import ProcCTe as ProcCTe_104
from pysped.cte.leiaute.consrecicte_104 import ProtCTe as ProtCTe_104
from pysped.cte.leiaute.consrecicte_104 import RetConsReciCTe as RetConsReciCTe_104
from pysped.cte.leiaute.conssitcte_104 import ConsSitCTe as ConsSitCTe_104
from pysped.cte.leiaute.conssitcte_104 import RetConsSitCTe as RetConsSitCTe_104
from pysped.cte.leiaute.consstatserv_104 import ConsStatServCTe as ConsStatServCTe_104
from pysped.cte.leiaute.consstatserv_104 import RetConsStatServCTe as RetConsStatServCTe_104
from pysped.cte.leiaute.cte_104 import CTe as CTe_104
from pysped.cte.leiaute.cte_104 import Dup as Dup_104
from pysped.cte.leiaute.cte_104 import InfNF as InfNF_104
from pysped.cte.leiaute.cte_104 import InfNFe as InfNFe_104
from pysped.cte.leiaute.cte_104 import InfOutros as InfOutros_104
from pysped.cte.leiaute.cte_104 import InfQ as InfQ_104
from pysped.cte.leiaute.cte_104 import ObsCont as ObsCont_104
from pysped.cte.leiaute.cte_104 import ObsFisco as ObsFisco_104
from pysped.cte.leiaute.cte_104 import Pass as Pass_104
from pysped.cte.leiaute.envicte_104 import EnviCTe as EnviCTe_104
from pysped.cte.leiaute.envicte_104 import RetEnviCTe as RetEnviCTe_104
from pysped.cte.leiaute.inutcte_104 import InutCTe as InutCTe_104
from pysped.cte.leiaute.inutcte_104 import ProcInutCTe as ProcInutCTe_104
from pysped.cte.leiaute.inutcte_104 import RetInutCTe as RetInutCTe_104
from pysped.cte.leiaute.soap_104 import SOAPEnvio as SOAPEnvio_104
from pysped.cte.leiaute.soap_104 import SOAPRetorno as SOAPRetorno_104
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_1 as ESQUEMA_ATUAL
from pysped.nfe.leiaute.cancnfe_107 import CancNFe as CancNFe_107
from pysped.nfe.leiaute.cancnfe_107 import ProcCancNFe as ProcCancNFe_107
from pysped.nfe.leiaute.cancnfe_107 import RetCancNFe as RetCancNFe_107
from pysped.nfe.leiaute.conscad_101 import ConsCad as ConsCad_101
from pysped.nfe.leiaute.conscad_101 import RetConsCad as RetConsCad_101
from pysped.nfe.leiaute.consrecinfe_110 import ConsReciNFe as ConsReciNFe_110
from pysped.nfe.leiaute.consrecinfe_110 import ProcNFe as ProcNFe_110
from pysped.nfe.leiaute.consrecinfe_110 import ProtNFe as ProtNFe_110
from pysped.nfe.leiaute.consrecinfe_110 import RetConsReciNFe as RetConsReciNFe_110
from pysped.nfe.leiaute.conssitnfe_107 import ConsSitNFe as ConsSitNFe_107
from pysped.nfe.leiaute.conssitnfe_107 import RetConsSitNFe as RetConsSitNFe_107
from pysped.nfe.leiaute.consstatserv_107 import ConsStatServ as ConsStatServ_107
from pysped.nfe.leiaute.consstatserv_107 import RetConsStatServ as RetConsStatServ_107
from pysped.nfe.leiaute.envinfe_110 import EnviNFe as EnviNFe_110
from pysped.nfe.leiaute.envinfe_110 import RetEnviNFe as RetEnviNFe_110
from pysped.nfe.leiaute.inutnfe_107 import InutNFe as InutNFe_107
from pysped.nfe.leiaute.inutnfe_107 import ProcInutNFe as ProcInutNFe_107
from pysped.nfe.leiaute.inutnfe_107 import RetInutNFe as RetInutNFe_107
from pysped.nfe.leiaute.nfe_110 import Adi as Adi_110
from pysped.nfe.leiaute.nfe_110 import Arma as Arma_110
from pysped.nfe.leiaute.nfe_110 import DI as DI_110
from pysped.nfe.leiaute.nfe_110 import Det as Det_110
from pysped.nfe.leiaute.nfe_110 import Dup as Dup_110
from pysped.nfe.leiaute.nfe_110 import Lacres as Lacres_110
from pysped.nfe.leiaute.nfe_110 import Med as Med_110
from pysped.nfe.leiaute.nfe_110 import NFRef as NFRef_110
from pysped.nfe.leiaute.nfe_110 import NFe as NFe_110
from pysped.nfe.leiaute.nfe_110 import ObsCont as ObsCont_110
from pysped.nfe.leiaute.nfe_110 import ObsFisco as ObsFisco_110
from pysped.nfe.leiaute.nfe_110 import ProcRef as ProcRef_110
from pysped.nfe.leiaute.nfe_110 import Reboque as Reboque_110
from pysped.nfe.leiaute.nfe_110 import Vol as Vol_110
from pysped.nfe.leiaute.soap_100 import SOAPEnvio as SOAPEnvio_110
from pysped.nfe.leiaute.soap_100 import SOAPRetorno as SOAPRetorno_110
#from pysped.nfe.processador_nfe import ProcessadorNFe, DANFE, Certificado
from pysped.nfe.processador_nfe import ProcessadorNFe, Certificado
