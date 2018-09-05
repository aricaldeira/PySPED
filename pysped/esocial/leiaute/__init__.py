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
# Versão 2.04.02
#
ESQUEMA_ATUAL_VERSAO_2 = 'v2.04.02'

from .soap_10100 import SOAPEnvio as SOAPEnvio_10100
from .soap_10100 import SOAPRetorno as SOAPRetorno_10100
from .soap_10100 import SOAPConsulta as SOAPConsulta_10100

from .envioLoteEventos_10101 import LoteEventosEsocial as LoteEventosEsocial_10101
from .retornoEnvioLoteEventos_10100 import RetornoLoteEventosEsocial as RetornoLoteEventosEsocial_10100
from .consultaLoteEventos_10000 import ConsultaLoteEventosEsocial as ConsultaLoteEventosEsocial_10000
from .retornoProcessamentoLote_10100 import RetornoProcessamentoLoteEsocial as RetornoProcessamentoLoteEsocial_10000

# S-1000
from .evtInfoEmpregador_20402 import S1000 as S1000_2

# S-1005
from .evtTabEstab_20402 import S1005 as S1005_2
from .evtTabEstab_20402 import InfoEntEduc as InfoEntEduc_2
from .evtTabEstab_20402 import InfoCaepf as S1005_InfoCaepf_2
from .evtTabEstab_20402 import InfoPCD as S1005_InfoPCD_2

# S-1010
from . evtTabRubrica_20402 import S1010 as S1010_2

# S-1020
from .evtTabLotacao_20402 import S1020 as S1020_2

# S-1030
from .evtTabCargo_20402 import S1030 as S1030_2
from .evtTabCargo_20402 import CargoPublico as S1030_CargoPublico_2

# S-1050
from .evtTabHorTur_20402 import S1050 as S1050_2
from .evtTabHorTur_20402 import HorarioIntervalo as HorarioIntervalo_2

# S-2200
from .evtAdmissao_20402 import S2200 as S2200_2
from .evtAdmissao_20402 import CTPS as S2200_CTPS_2
from .evtAdmissao_20402 import RIC as S2200_RIC_2
from .evtAdmissao_20402 import RG as S2200_RG_2
from .evtAdmissao_20402 import RNE as S2200_RNE_2
from .evtAdmissao_20402 import OC as S2200_OC_2
from .evtAdmissao_20402 import CNH as S2200_CNH_2
from .evtAdmissao_20402 import Brasil as S2200_Brasil_2
from .evtAdmissao_20402 import Dependente as S2200_Dependente_2
from .evtAdmissao_20402 import TrabEstrangeiro as S2200_TrabEstrangeiro_2
from .evtAdmissao_20402 import Contato as S2200_Contato_2
from .evtAdmissao_20402 import InfoCeletista as S2200_InfoCeletista_2
from .evtAdmissao_20402 import InfoEstatutario as S2200_InfoEstatutario_2
from .evtAdmissao_20402 import LocalTrabGeral as S2200_LocalTrabGeral_2
from .evtAdmissao_20402 import HorContratual as S2200_HorContratual_2
from .evtAdmissao_20402 import Horario as S2200_Horario_2
from .evtAdmissao_20402 import FiliacaoSindical as S2200_FiliacaoSindical_2
from .evtAdmissao_20402 import Observacoes as S2200_Observacoes_2
from .evtAdmissao_20402 import SucessaoVinc as S2200_SucessaoVinc_2

# S-2205
from .evtAltCadastral_20402 import S2205 as S2205_2
from .evtAltCadastral_20402 import CTPS as S2205_CTPS_2
from .evtAltCadastral_20402 import RG as S2205_RG_2
from .evtAltCadastral_20402 import CNH as S2205_CNH_2
from .evtAltCadastral_20402 import Dependente as S2205_Dependente_2
from .evtAltCadastral_20402 import TrabEstrangeiro as S2205_TrabEstrangeiro_2

# S-2206
from .evtAltContratual_20402 import S2206 as S2206_2
from .evtAltContratual_20402 import InfoCeletista as S2206_InfoCeletista_2
from .evtAltContratual_20402 import Vinculo as S2206_Vinculo_2
from .evtAltContratual_20402 import InfoRegimeTrab as S2206_InfoRegimeTrab_2
from .evtAltContratual_20402 import LocalTrabGeral as S2206_LocalTrabGeral_2
from .evtAltContratual_20402 import HorContratual as S2206_HorContratual_2
from .evtAltContratual_20402 import Horario as S2206_Horario_2
from .evtAltContratual_20402 import FiliacaoSindical as S2206_FiliacaoSindical_2

# S-2230
from .evtAfastTemp_20402 import S2230 as S2230_2
from .evtAfastTemp_20402 import IniAfastamento as S2230_IniAfastamento_2
from .evtAfastTemp_20402 import FimAfastamento as S2230_FimAfastamento_2

# S-2299
from .evtDeslig_20402 import S2299 as S2299_2
from .evtDeslig_20402 import IdeEstabLot as S2299_IdeEstabLot_2
from .evtDeslig_20402 import IdePeriodo as S2299_IdePeriodo_2
from .evtDeslig_20402 import IdeADC as S2299_IdeADC_2
from .evtDeslig_20402 import InfoTrabInterm as S2299_InfoTrabInterm_2
from .evtDeslig_20402 import InfoPerAnt as S2299_InfoPerAnt_2
from .evtDeslig_20402 import ProcCS as S2299_ProcCS_2
from .evtDeslig_20402 import RemunOutrEmpr as S2299_RemunOutrEmpr_2
from .evtDeslig_20402 import InfoMV as S2299_InfoMV_2
from .evtDeslig_20402 import ProcJudTrab as S2299_ProcJudTrab_2
from .evtDeslig_20402 import InfoSimples as S2299_InfoSimples_2
from .evtDeslig_20402 import InfoAgNocivo as S2299_InfoAgNocivo_2
from .evtDeslig_20402 import DetPlano as S2299_DetPlano_2
from .evtDeslig_20402 import DetVerbas as S2299_DetVerbas_2
from .evtDeslig_20402 import InfoPerApur as S2299_InforPerApur_2
from .evtDeslig_20402 import ConsigFGTS as S2299_ConsigFGTS_2
from .evtDeslig_20402 import Quarentena as S2299_Quarentena_2
from .evtDeslig_20402 import DmDev as S2299_DmDev_2
from .evtDeslig_20402 import TransfTit as S2299_TransfTit_2
from .evtDeslig_20402 import SucessaoVinc as S2299_SucessaoVinc_2
from .evtDeslig_20402 import Observacoes as S2299_Observacoes_2
from .evtDeslig_20402 import VerbasResc as S2299_VerbasResc_2
from .evtDeslig_20402 import InfoDeslig as S2299_InfoDeslig_2
from .evtDeslig_20402 import IdeVinculo as S2299_IdeVinculo_2
from .evtDeslig_20402 import EvtDeslig as S2299_EvtDeslig_2
from .evtDeslig_20402 import DetOper as S2299_DetOper_2
from .evtDeslig_20402 import IdeEmpregador as S2299_DetOper_2
from .evtDeslig_20402 import IdeEstabLotApur as S2299_IdeEstabLotApur_2
from .evtDeslig_20402 import IdeEvento as S2299_IdeEvento_2
from .evtDeslig_20402 import InfoSaudeColet as S2299_InfoSaudeColet_2

# S-1200
from .evtRemun_20402 import S1200 as S1200_2
from .evtRemun_20402 import InfoMV as S1200_InfoMV_2
from .evtRemun_20402 import InfoComplem as S1200_InfoComplem_2
from .evtRemun_20402 import ProcJudTrab as S1200_ProcJudTrab_2
from .evtRemun_20402 import InfoInterm as S1200_InfoInterm_2
from .evtRemun_20402 import DmDev as S1200_DmDev_2
from .evtRemun_20402 import RemunOutrEmpr as S1200_RemunOutrEmpr_2
from .evtRemun_20402 import SucessaoVinc as S1200_SucessaoVinc_2
from .evtRemun_20402 import InfoPerApur as S1200_InfoPerApur_2
from .evtRemun_20402 import RemunPerApur as S1200_RemunPerApur_2
from .evtRemun_20402 import InfoPerAnt as S1200_InfoPerAnt_2
from .evtRemun_20402 import InfoComplCont as S1200_InfoComplCont_2
from .evtRemun_20402 import ItensRemun as S1200_ItensRemun_2
from .evtRemun_20402 import InfoSaudeColet as S1200_InfoSaudeColet_2
from .evtRemun_20402 import InfoAgNocivo as S1200_InfoAgNocivo_2
from .evtRemun_20402 import InfoTrabInterm as S1200_InfoTrabInterm_2
from .evtRemun_20402 import DetOper as S1200_DetOper_2
from .evtRemun_20402 import DetPlano as S1200_DetPlano_2
from .evtRemun_20402 import IdeADC as S1200_IdeADC_2
from .evtRemun_20402 import IdePeriodo as S1200_IdePeriodo_2
from .evtRemun_20402 import IdePeriodoIdeEstabLot as S1200_IdePeriodoIdeEstabLot_2
from .evtRemun_20402 import RemunPerAntItensRemun as S1200_RemunPerAntItensRemun_2
from .evtRemun_20402 import RemunPerAntInfoAgNocivo as S1200_RemunPerAntInfoAgNocivo_2
from .evtRemun_20402 import RemunPerAntInfoTrabInterm as S1200_RemunPerAntInfoTrabInterm_2

# S-1202
from .evtRmnRPPS_20402 import S1202 as S1202_2
from .evtRmnRPPS_20402 import ProcJudTrab as S1202_ProcJudTrab_2
from .evtRmnRPPS_20402 import DmDev as S1202_DmDev_2
from .evtRmnRPPS_20402 import InfoPerApur as S1202_InfoPerApur_2
from .evtRmnRPPS_20402 import InfoPerAnt as S1202_InfoPerAnt_2
from .evtRmnRPPS_20402 import RemunPerApur as S1202_RemunPerApur_2
from .evtRmnRPPS_20402 import ItensRemun as S1202_ItensRemun_2
from .evtRmnRPPS_20402 import InfoSaudeColet as InfoSaudeColet_2
from .evtRmnRPPS_20402 import DetOper as S1202_DetOper_2
from .evtRmnRPPS_20402 import DetPlano as S1202_DetPlano_2
from .evtRmnRPPS_20402 import IdeADC as S1202_IdeADC_2
from .evtRmnRPPS_20402 import IdePeriodo as S1202_IdePeriodo_2
from .evtRmnRPPS_20402 import IdePeriodoIdeEstab as S1202_IdePeriodoIdeEstab_2
from .evtRmnRPPS_20402 import RemunPerAntItensRemun as S1202_RemunPerAntItensRemun_2

# S-1207
from .evtBenPrRP_20402 import S1207 as S1207_2
from .evtBenPrRP_20402 import DmDev as S1207_DmDev_2
from .evtBenPrRP_20402 import Itens as S1207_Itens_2

# S-1210
from .evtPgtos_20402 import S1210 as S1210_2
from .evtPgtos_20402 import InfoPgto as S1210_InfoPgto_2
from .evtPgtos_20402 import DetPgtoFl as S1210_DetPgtoFl_2
from .evtPgtos_20402 import RetPgtoTot as S1210_RetPgtoTot_2
from .evtPgtos_20402 import PenAlim as S1210_PenAlim_2
from .evtPgtos_20402 import InfoPgtoParc as S1210_InfoPgtoParc_2
from .evtPgtos_20402 import DetPgtoBenPr as S1210_DetPgtoBenPr_2
from .evtPgtos_20402 import DetPgtoBenPrRetPgtoTot as S1210_DetPgtoBenPrRetPgtoTot_2
from .evtPgtos_20402 import DetPgtoBenPrInfoPgtoParc as S1210_DetPgtoBenPrInfoPgtoParc_2
from .evtPgtos_20402 import DetPgtoFer as S1210_DetPgtoFer_2
from .evtPgtos_20402 import DetRubrFer as S1210_DetRubrFer_2
from .evtPgtos_20402 import DetRubrFerPenAlim as S1210_DetRubrFerPenAlim_2
from .evtPgtos_20402 import DetPgtoAnt as S1210_DetPgtoAnt_2
from .evtPgtos_20402 import IdePgtoExt as S1210_IdePgtoExt_2
from .evtPgtos_20402 import InfoPgtoAnt as S1210_InfoPgtoAnt_2

# S-1298
from .evtReabreEvPer_20402 import S1298 as S1298_2

# S-1299
from .evtFechaEvPer_20402 import S1299 as S1299_2

# S-2300
from .evtTSVInicio_20402 import S2300 as S2300_2
from .evtTSVInicio_20402 import CTPS as S2300_CTPS_2
from .evtTSVInicio_20402 import RIC as S2300_RIC_2
from .evtTSVInicio_20402 import RG as S2300_RG_2
from .evtTSVInicio_20402 import RNE as S2300_RNE_2
from .evtTSVInicio_20402 import OC as S2300_OC_2
from .evtTSVInicio_20402 import CNH as S2300_CNH_2
from .evtTSVInicio_20402 import Brasil as S2300_Brasil_2
from .evtTSVInicio_20402 import Dependente as S2300_Dependente_2
from .evtTSVInicio_20402 import TrabEstrangeiro as S2300_TrabEstrangeiro_2
from .evtTSVInicio_20402 import Contato as S2300_Contato_2
from .evtTSVInicio_20402 import InfoComplementares as S2300_InfoComplementares_2
from .evtTSVInicio_20402 import CargoFuncao as S2300_CargoFuncao_2
from .evtTSVInicio_20402 import Remuneracao as S2300_Remuneracao_2
from .evtTSVInicio_20402 import FGTS as S2300_FGTS_2
from .evtTSVInicio_20402 import InfoDirigenteSindical as S2300_InfoDirigenteSindical_2
from .evtTSVInicio_20402 import InfoTrabCedido as S2300_InfoTrabCedido_2
from .evtTSVInicio_20402 import InfoEstagiario as S2300_InfoEstagiario_2
from .evtTSVInicio_20402 import InstEnsino as S2300_InstEnsino_2
from .evtTSVInicio_20402 import AgeIntegracao as S2300_AgeIntegracao_2
from .evtTSVInicio_20402 import SupervisorEstagio as S2300_SupervisorEstagio_2
from .evtTSVInicio_20402 import Afastamento as S2300_Afastamento_2
from .evtTSVInicio_20402 import Termino as S2300_Termino_2

# S-2306
from .evtTSVAltContr_20402 import S2306 as S2306_2
from .evtTSVAltContr_20402 import CargoFuncao as S2306_CargoFuncao_2
from .evtTSVAltContr_20402 import Remuneracao as S2306_Remuneracao_2
from .evtTSVAltContr_20402 import InfoTrabCedido as S2306_InfoTrabCedido_2
from .evtTSVAltContr_20402 import InfoEstagiario as S2306_InfoEstagiario_2
from .evtTSVAltContr_20402 import InstEnsino as S2306_InstEnsino_2
from .evtTSVAltContr_20402 import AgeIntegracao as S2306_AgeIntegracao_2
from .evtTSVAltContr_20402 import SupervisorEstagio as S2306_SupervisorEstagio_2

# S-2399
from .evtTSVTermino_20402 import S2399 as S2399_2
from .evtTSVTermino_20402 import IdeEstabLot as S2399_IdeEstabLot_2
from .evtTSVTermino_20402 import RemunOutrEmpr as S2399_RemunOutrEmpr_2
from .evtTSVTermino_20402 import InfoMV as S2399_InfoMV_2
from .evtTSVTermino_20402 import ProcJudTrab as S2399_ProcJudTrab_2
from .evtTSVTermino_20402 import InfoSimples as S2399_InfoSimples_2
from .evtTSVTermino_20402 import InfoAgNocivo as S2399_InfoAgNocivo_2
from .evtTSVTermino_20402 import DetVerbas as S2399_DetVerbas_2
from .evtTSVTermino_20402 import Quarentena as S2399_Quarentena_2
from .evtTSVTermino_20402 import DmDev as S2399_DmDev_2
from .evtTSVTermino_20402 import VerbasResc as S2399_VerbasResc_2
from .evtTSVTermino_20402 import IdeEmpregador as S2399_DetOper_2
from .evtTSVTermino_20402 import IdeEvento as S2399_IdeEvento_2

# S-3000
from .evtExclusao import S3000 as S3000_2
from .evtExclusao import IdeTrabalhador as S3000_IdeTrabalhador_2
from .evtExclusao import IdeFolhaPagto as S3000_IdeFolhaPagto_2

# S-5001
from .evtBasesTrab_20402 import S5001 as S5001_2
from .evtBasesTrab_20402 import ProcJudTrab as S5001_ProcJudTrab_2
from .evtBasesTrab_20402 import IdeEstabLot as S5001_IdeEstabLot_2
from .evtBasesTrab_20402 import InfoCategIncid as S5001_InfoCategIncid_2
from .evtBasesTrab_20402 import InfoBaseCS as S5001_InfoBaseCS_2
from .evtBasesTrab_20402 import CalcTerc as S5001_CalcTerc_2

# S-5002
from .evtIrrfBenef_20402 import S5002 as S5002_2
from .evtIrrfBenef_20402 import InfoDep as S5002_InfoDep_2
from .evtIrrfBenef_20402 import InfoIrrf as S5002_InfoIrrf_2
from .evtIrrfBenef_20402 import BasesIrrf as S5002_BasesIrrf_2
from .evtIrrfBenef_20402 import Irrf as S5002_Irr2_2
from .evtIrrfBenef_20402 import IdePgtoExt as S5002_IdePgtoExt_2

# S-5011
from .evtCS_20402 import S5011 as S5011_2
from .evtCS_20402 import InfoCPSeg as S5011_InfoCPSeg_2
from .evtCS_20402 import IdeEstab as S5011_IdeEstab_2
from .evtCS_20402 import InfoCRContrib as S5011_InfoCRContrib_2
from .evtCS_20402 import InfoPJ as S5011_InfoPJ_2
from .evtCS_20402 import InfoAtConc as S5011_InfoAtConc_2
from .evtCS_20402 import InfoEstab as S5011_InfoEstab_2
from .evtCS_20402 import IdeLotacao as S5011_IdeLotacao_2
from .evtCS_20402 import BasesAquis as S5011_BasesAquis_2
from .evtCS_20402 import BasesComerc as S5011_BasesComerc_2
from .evtCS_20402 import InfoComplObra as S5011_InfoComplObra_2
from .evtCS_20402 import InfoTercSusp as S5011_InfoTercSusp_2
from .evtCS_20402 import InfoEmprParcial as S5011_InfoEmprParcial_2
from .evtCS_20402 import DadosOpPort as S5011_DadosOpPort_2
from .evtCS_20402 import BasesRemun as S5011_BasesRemun_2
from .evtCS_20402 import BasesAvNPort as S5011_BasesAvNPort_2
from .evtCS_20402 import InfoSubstPatrOpPort as S5011_InfoSubstPatrOpPort_2
from .evtCS_20402 import InfoCREstab as S5011_InfoCREstab_2

# S-5012
from .evtIrrf import S5012 as S5012_2
from .evtIrrf import InfoCRContrib as S5012_InfoCRContrib_2
