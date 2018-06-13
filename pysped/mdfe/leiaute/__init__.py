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
# Versão 3.00
#
ESQUEMA_ATUAL_VERSAO_3 = 'pl_300_NT012018'


#
# Envelopes SOAP
#
from .soap_200 import SOAPEnvio as SOAPEnvio_200
from .soap_200 import SOAPRetorno as SOAPRetorno_200

#
# Emissão de MDF-e
#
from .mdfe_300 import MDFe as MDFe_300
from .mdfe_300 import InfMunCarrega as InfMunCarrega_300
from .mdfe_300 import InfPercurso as InfPercurso_300
from .mdfe_300 import InfMunDescarga as InfMunDescarga_300
from .mdfe_300 import InfNFe as InfNFe_300
from .mdfe_300 import Lacres as Lacres_300
from .mdfe_300 import AutXML as AutXML_300

from .modal_rodoviario_300 import InfModalRodoviario as InfModalRodoviario_300
from .modal_rodoviario_300 import Condutor as Condutor_300

#
# Envio de lote de MDF-e
#
from .envimdfe_300 import EnviMDFe as EnviMDFe_300
from .envimdfe_300 import RetEnviMDFe as RetEnviMDFe_300

#
# Consulta do recibo do lote de MDF-e
#
from .consrecimdfe_300 import ConsReciMDFe as ConsReciMDFe_300
from .consrecimdfe_300 import RetConsReciMDFe as RetConsReciMDFe_300
from .consrecimdfe_300 import ProtMDFe as ProtMDFe_300
from .consrecimdfe_300 import ProcMDFe as ProcMDFe_300

#
# Consulta a situação de MDF-e
#
from .conssitmdfe_300 import ConsSitMDFe as ConsSitMDFe_300
from .conssitmdfe_300 import RetConsSitMDFe as RetConsSitMDFe_300

#
# Eventos do MDF-e - classes básicas
#
from .eventomdfe_300 import Evento as Evento_300
from .eventomdfe_300 import RetEvento as RetEvento_300
from .eventomdfe_300 import ProcEvento as ProcEvento_300

#
# Eventos do MDF-e - Cancelamento
#
from .evtcancmdfe_300 import EventoCancMDFe as EventoCancMDFe_300
from .evtcancmdfe_300 import RetEventoCancMDFe as RetEventoCancMDFe_300
from .evtcancmdfe_300 import ProcEventoCancMDFe as ProcEventoCancMDFe_300

#
# Eventos do MDF-e - Encerramento
#
from .evtencmdfe_300 import EventoEncMDFe as EventoEncMDFe_300
from .evtencmdfe_300 import RetEventoEncMDFe as RetEventoEncMDFe_300
from .evtencmdfe_300 import ProcEventoEncMDFe as ProcEventoEncMDFe_300
