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
# Versão 3.10, usada a partir de novembro/2013 para a NFC-e, e
# março/2014 para a NF-e
#
ESQUEMA_ATUAL_VERSAO_3 = 'pl_006r'

#
# Versão 2.00, usada a partir de maio/2010
#
ESQUEMA_ATUAL_VERSAO_2 = 'pl_006r'

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
from consnfedest_101 import CONS_NFE_TODAS
from consnfedest_101 import CONS_NFE_SEM_CONFIRMACAO_OPERACAO
from consnfedest_101 import CONS_NFE_SEM_CIENCIA_OPERACAO
from consnfedest_101 import CONS_NFE_EMISSAO_TODOS_EMITENTES
from consnfedest_101 import CONS_NFE_EMISSAO_SOMENTE_TERCEIROS

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
# Consulta cadastro
#
from conscad_200 import ConsCad as ConsCad_200
from conscad_200 import RetConsCad as RetConsCad_200

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

# Pyflakes

Adi_110
Adi_200
Arma_110
Arma_200
CONF_RECEBIMENTO_CIENCIA_OPERACAO
CONF_RECEBIMENTO_CONFIRMAR_OPERACAO
CONF_RECEBIMENTO_DESCONHECIMENTO_OPERACAO
CONF_RECEBIMENTO_OPERACAO_NAO_REALIZADA
CONS_NFE_EMISSAO_SOMENTE_TERCEIROS
CONS_NFE_EMISSAO_TODOS_EMITENTES
CONS_NFE_SEM_CIENCIA_OPERACAO
CONS_NFE_SEM_CONFIRMACAO_OPERACAO
CONS_NFE_TODAS
CancNFe_107
CancNFe_200
ConsCad_101
ConsCad_200
ConsNFeDest_101
ConsReciNFe_110
ConsReciNFe_200
ConsSitNFe_107
ConsSitNFe_200
ConsSitNFe_201
ConsStatServ_107
ConsStatServ_200
DESCEVENTO_CONF_RECEBIMENTO
DI_110
DI_200
Det_110
Det_200
DownloadNFe_100
Dup_110
Dup_200
EnvEventoCCe_100
EnvEventoCancNFe_100
EnvEventoConfRecebimento_100
EnvEvento_100
EnviNFe_110
EnviNFe_200
EventoCCe_100
EventoCancNFe_100
EventoConfRecebimento_100
Evento_100
InutNFe_107
InutNFe_200
Lacres_110
Lacres_200
Med_110
Med_200
NFRef_110
NFRef_200
NFe_110
NFe_200
ObsCont_110
ObsCont_200
ObsFisco_110
ObsFisco_200
ProcCancNFe_107
ProcCancNFe_200
ProcEventoCCe_100
ProcEventoCancNFe_100
ProcEventoConfRecebimento_100
ProcEvento_100
ProcInutNFe_107
ProcInutNFe_200
ProcNFe_110
ProcNFe_200
ProcRef_110
ProcRef_200
ProtNFe_110
ProtNFe_200
Reboque_110
Reboque_200
RetCancNFe_107
RetCancNFe_200
RetConsCad_101
RetConsCad_200
RetConsNFeDest_101
RetConsReciNFe_110
RetConsReciNFe_200
RetConsSitNFe_107
RetConsSitNFe_200
RetConsSitNFe_201
RetConsStatServ_107
RetConsStatServ_200
RetDownloadNFe_100
RetEnvEventoCCe_100
RetEnvEventoCancNFe_100
RetEnvEventoConfRecebimento_100
RetEnvEvento_100
RetEnviNFe_110
RetEnviNFe_200
RetEventoCCe_100
RetEventoCancNFe_100
RetEventoConfRecebimento_100
RetEvento_100
RetInutNFe_107
RetInutNFe_200
SOAPEnvio_110
SOAPEnvio_200
SOAPRetorno_110
SOAPRetorno_200
TagChNFe_100
Vol_110
Vol_200
