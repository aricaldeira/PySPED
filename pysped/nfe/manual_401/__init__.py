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

#
# Versão 2.00, usada a partir de maio/2010
#
#

#
# O esquemar pl_006m contém os esquemas dos enventos da NF-e
#
from pysped.nfe.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

#
# Envelopes SOAP
#
from pysped.nfe.leiaute.soap_200 import SOAPEnvio as SOAPEnvio_200
from pysped.nfe.leiaute.soap_200 import SOAPRetorno as SOAPRetorno_200

#
# Emissão de NF-e
#
from pysped.nfe.leiaute.nfe_200 import NFe as NFe_200
from pysped.nfe.leiaute.nfe_200 import NFRef as NFRef_200
from pysped.nfe.leiaute.nfe_200 import Det as Det_200
from pysped.nfe.leiaute.nfe_200 import DI as DI_200
from pysped.nfe.leiaute.nfe_200 import Adi as Adi_200
from pysped.nfe.leiaute.nfe_200 import Med as Med_200
from pysped.nfe.leiaute.nfe_200 import Arma as Arma_200
from pysped.nfe.leiaute.nfe_200 import Reboque as Reboque_200
from pysped.nfe.leiaute.nfe_200 import Vol as Vol_200
from pysped.nfe.leiaute.nfe_200 import Lacres as Lacres_200
from pysped.nfe.leiaute.nfe_200 import Dup as Dup_200
from pysped.nfe.leiaute.nfe_200 import ObsCont as ObsCont_200
from pysped.nfe.leiaute.nfe_200 import ObsFisco as ObsFisco_200
from pysped.nfe.leiaute.nfe_200 import ProcRef as ProcRef_200

#
# Envio de lote de NF-e
#
from pysped.nfe.leiaute.envinfe_200 import EnviNFe as EnviNFe_200
from pysped.nfe.leiaute.envinfe_200 import RetEnviNFe as RetEnviNFe_200

#
# Consulta do recibo do lote de NF-e
#
from pysped.nfe.leiaute.consrecinfe_200 import ConsReciNFe as ConsReciNFe_200
from pysped.nfe.leiaute.consrecinfe_200 import RetConsReciNFe as RetConsReciNFe_200
from pysped.nfe.leiaute.consrecinfe_200 import ProtNFe as ProtNFe_200
from pysped.nfe.leiaute.consrecinfe_200 import ProcNFe as ProcNFe_200

#
# Cancelamento de NF-e
#
from pysped.nfe.leiaute.cancnfe_200 import CancNFe as CancNFe_200
from pysped.nfe.leiaute.cancnfe_200 import RetCancNFe as RetCancNFe_200
from pysped.nfe.leiaute.cancnfe_200 import ProcCancNFe as ProcCancNFe_200

#
# Inutilização de NF-e
#
from pysped.nfe.leiaute.inutnfe_200 import InutNFe as InutNFe_200
from pysped.nfe.leiaute.inutnfe_200 import RetInutNFe as RetInutNFe_200
from pysped.nfe.leiaute.inutnfe_200 import ProcInutNFe as ProcInutNFe_200

#
# Consulta a situação de NF-e
#
from pysped.nfe.leiaute.conssitnfe_200 import ConsSitNFe as ConsSitNFe_200
from pysped.nfe.leiaute.conssitnfe_200 import RetConsSitNFe as RetConsSitNFe_200

#
# Consulta a situação do serviço
#
from pysped.nfe.leiaute.consstatserv_200 import ConsStatServ as ConsStatServ_200
from pysped.nfe.leiaute.consstatserv_200 import RetConsStatServ as RetConsStatServ_200

#
# Consulta cadastro
#
#from pysped.nfe.leiaute.conscad_101 import ConsCad as ConsCad_101
#from pysped.nfe.leiaute.conscad_101 import RetConsCad as RetConsCad_101

#
# Eventos da NF-e - Carta de Correção Eletrônica
#
from pysped.nfe.leiaute.evtccenfe_100 import EventoCCe as EventoCCe_100
from pysped.nfe.leiaute.evtccenfe_100 import RetEventoCCe as RetEventoCCe_100
from pysped.nfe.leiaute.evtccenfe_100 import ProcEventoCCe as ProcEventoCCe_100
from pysped.nfe.leiaute.evtccenfe_100 import EnvEventoCCe as EnvEventoCCe_100
from pysped.nfe.leiaute.evtccenfe_100 import RetEnvEventoCCe as RetEnvEventoCCe_100

#
# Eventos da NF-e - Cancelamento como Evento
#
from pysped.nfe.leiaute.evtcancnfe_100 import EventoCancNFe as EventoCancNFe_100
from pysped.nfe.leiaute.evtcancnfe_100 import RetEventoCancNFe as RetEventoCancNFe_100
from pysped.nfe.leiaute.evtcancnfe_100 import ProcEventoCancNFe as ProcEventoCancNFe_100
from pysped.nfe.leiaute.evtcancnfe_100 import EnvEventoCancNFe as EnvEventoCancNFe_100
from pysped.nfe.leiaute.evtcancnfe_100 import RetEnvEventoCancNFe as RetEnvEventoCancNFe_100

#
# Eventos da NF-e - Confirmação de Recebimento/Manifestação do Destinatário
#
from pysped.nfe.leiaute.evtconfrecebimento_100 import EventoConfRecebimento as EventoConfRecebimento_100
from pysped.nfe.leiaute.evtconfrecebimento_100 import RetEventoConfRecebimento as RetEventoConfRecebimento_100
from pysped.nfe.leiaute.evtconfrecebimento_100 import ProcEventoConfRecebimento as ProcEventoConfRecebimento_100
from pysped.nfe.leiaute.evtconfrecebimento_100 import EnvEventoConfRecebimento as EnvEventoConfRecebimento_100
from pysped.nfe.leiaute.evtconfrecebimento_100 import RetEnvEventoConfRecebimento as RetEnvEventoConfRecebimento_100
from pysped.nfe.leiaute.evtconfrecebimento_100 import CONF_RECEBIMENTO_CONFIRMAR_OPERACAO
from pysped.nfe.leiaute.evtconfrecebimento_100 import CONF_RECEBIMENTO_CIENCIA_OPERACAO
from pysped.nfe.leiaute.evtconfrecebimento_100 import CONF_RECEBIMENTO_DESCONHECIMENTO_OPERACAO
from pysped.nfe.leiaute.evtconfrecebimento_100 import CONF_RECEBIMENTO_OPERACAO_NAO_REALIZADA
from pysped.nfe.leiaute.evtconfrecebimento_100 import DESCEVENTO_CONF_RECEBIMENTO

# Pyflakes

Adi_200
Arma_200
CONF_RECEBIMENTO_CIENCIA_OPERACAO
CONF_RECEBIMENTO_CONFIRMAR_OPERACAO
CONF_RECEBIMENTO_DESCONHECIMENTO_OPERACAO
CONF_RECEBIMENTO_OPERACAO_NAO_REALIZADA
CancNFe_200
ConsReciNFe_200
ConsSitNFe_200
ConsStatServ_200
DESCEVENTO_CONF_RECEBIMENTO
DI_200
Det_200
Dup_200
ESQUEMA_ATUAL
EnvEventoCCe_100
EnvEventoCancNFe_100
EnvEventoConfRecebimento_100
EnviNFe_200
EventoCCe_100
EventoCancNFe_100
EventoConfRecebimento_100
InutNFe_200
Lacres_200
Med_200
NFRef_200
NFe_200
ObsCont_200
ObsFisco_200
ProcCancNFe_200
ProcEventoCCe_100
ProcEventoCancNFe_100
ProcEventoConfRecebimento_100
ProcInutNFe_200
ProcNFe_200
ProcRef_200
ProtNFe_200
Reboque_200
RetCancNFe_200
RetConsReciNFe_200
RetConsSitNFe_200
RetConsStatServ_200
RetEnvEventoCCe_100
RetEnvEventoCancNFe_100
RetEnvEventoConfRecebimento_100
RetEnviNFe_200
RetEventoCCe_100
RetEventoCancNFe_100
RetEventoConfRecebimento_100
RetInutNFe_200
SOAPEnvio_200
SOAPRetorno_200
Vol_200
