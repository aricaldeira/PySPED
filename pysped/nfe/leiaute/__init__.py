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

#
# Versão 2.00, usada a partir de maio/2010
#
#

#
# O esquemar pl_006m contém os esquemas dos enventos da NF-e
#
ESQUEMA_ATUAL_VERSAO_2 = 'pl_006n'

#
# Versão 1.00, usada até abril/2010
#
ESQUEMA_ATUAL_VERSAO_1 = 'pl_005f'


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

#
# Eventos da NF-e - classes básicas
#
from eventonfe_100 import Evento as Evento_100
from eventonfe_100 import RetEvento as RetEvento_100
from eventonfe_100 import ProcEvento as ProcEvento_100
from eventonfe_100 import EnvEvento as EnvEvento_100
from eventonfe_100 import RetEnvEvento as RetEnvEvento_100

#
# Eventos da NF-e - Carta de Correção Eletrônica
#
from evtccenfe_100 import EventoCCe as EventoCCe_100
from evtccenfe_100 import RetEventoCCe as RetEventoCCe_100
from evtccenfe_100 import ProcEventoCCe as ProcEventoCCe_100
from evtccenfe_100 import EnvEventoCCe as EnvEventoCCe_100
from evtccenfe_100 import RetEnvEventoCCe as RetEnvEventoCCe_100

#
# Eventos da NF-e - Cancelamento como Evento
#
from evtcancnfe_100 import EventoCancNFe as EventoCancNFe_100
from evtcancnfe_100 import RetEventoCancNFe as RetEventoCancNFe_100
from evtcancnfe_100 import ProcEventoCancNFe as ProcEventoCancNFe_100
from evtcancnfe_100 import EnvEventoCancNFe as EnvEventoCancNFe_100
from evtcancnfe_100 import RetEnvEventoCancNFe as RetEnvEventoCancNFe_100

#
# Eventos da NF-e - Confirmação de Recebimento/Manifestação do Destinatário
#
from evtconfrecebimento_100 import EventoConfRecebimento as EventoConfRecebimento_100
from evtconfrecebimento_100 import RetEventoConfRecebimento as RetEventoConfRecebimento_100
from evtconfrecebimento_100 import ProcEventoConfRecebimento as ProcEventoConfRecebimento_100
from evtconfrecebimento_100 import EnvEventoConfRecebimento as EnvEventoConfRecebimento_100
from evtconfrecebimento_100 import RetEnvEventoConfRecebimento as RetEnvEventoConfRecebimento_100
from evtconfrecebimento_100 import CONF_RECEBIMENTO_CONFIRMAR_OPERACAO
from evtconfrecebimento_100 import CONF_RECEBIMENTO_CIENCIA_OPERACAO
from evtconfrecebimento_100 import CONF_RECEBIMENTO_DESCONHECIMENTO_OPERACAO
from evtconfrecebimento_100 import CONF_RECEBIMENTO_OPERACAO_NAO_REALIZADA
from evtconfrecebimento_100 import DESCEVENTO_CONF_RECEBIMENTO

#
# Consulta NF-e destinadas
#
from consnfedest_101 import ConsNFeDest as ConsNFeDest_101
from consnfedest_101 import RetConsNFeDest as RetConsNFeDest_101


#
# Consulta a situação de NF-e - nova versão com os eventos
#
from conssitnfe_201 import ConsSitNFe as ConsSitNFe_201
from conssitnfe_201 import RetConsSitNFe as RetConsSitNFe_201

#
# Download de NF-e
#
from downloadnfe_100 import DownloadNFe as DownloadNFe_100
from downloadnfe_100 import TagChNFe as TagChNFe_100
from downloadnfe_100 import RetDownloadNFe as RetDownloadNFe_100

#
# Envelopes SOAP
#
from soap_100 import SOAPEnvio as SOAPEnvio_110
from soap_100 import SOAPRetorno as SOAPRetorno_110

#
# Emissão de NF-e
#
from nfe_110 import NFe as NFe_110
from nfe_110 import NFRef as NFRef_110
from nfe_110 import Det as Det_110
from nfe_110 import DI as DI_110
from nfe_110 import Adi as Adi_110
from nfe_110 import Med as Med_110
from nfe_110 import Arma as Arma_110
from nfe_110 import Reboque as Reboque_110
from nfe_110 import Vol as Vol_110
from nfe_110 import Lacres as Lacres_110
from nfe_110 import Dup as Dup_110
from nfe_110 import ObsCont as ObsCont_110
from nfe_110 import ObsFisco as ObsFisco_110
from nfe_110 import ProcRef as ProcRef_110

#
# Envio de lote de NF-e
#
from envinfe_110 import EnviNFe as EnviNFe_110
from envinfe_110 import RetEnviNFe as RetEnviNFe_110

#
# Consulta do recibo do lote de NF-e
#
from consrecinfe_110 import ConsReciNFe as ConsReciNFe_110
from consrecinfe_110 import RetConsReciNFe as RetConsReciNFe_110
from consrecinfe_110 import ProtNFe as ProtNFe_110
from consrecinfe_110 import ProcNFe as ProcNFe_110

#
# Cancelamento de NF-e
#
from cancnfe_107 import CancNFe as CancNFe_107
from cancnfe_107 import RetCancNFe as RetCancNFe_107
from cancnfe_107 import ProcCancNFe as ProcCancNFe_107

#
# Inutilização de NF-e
#
from inutnfe_107 import InutNFe as InutNFe_107
from inutnfe_107 import RetInutNFe as RetInutNFe_107
from inutnfe_107 import ProcInutNFe as ProcInutNFe_107

#
# Consulta a situação de NF-e
#
from conssitnfe_107 import ConsSitNFe as ConsSitNFe_107
from conssitnfe_107 import RetConsSitNFe as RetConsSitNFe_107

#
# Consulta a situação do serviço
#
from consstatserv_107 import ConsStatServ as ConsStatServ_107
from consstatserv_107 import RetConsStatServ as RetConsStatServ_107

#
# Consulta cadastro
#
from conscad_101 import ConsCad as ConsCad_101
from conscad_101 import RetConsCad as RetConsCad_101

