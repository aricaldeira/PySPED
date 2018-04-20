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

from .webservices_flags import *


METODO_WS = {
    WS_CTE_AUTORIZACAO: {
        'webservice': 'CteRecepcao',
        'metodo'    : 'cteRecepcaoLote',
    },
    WS_CTE_CONSULTA_AUTORIZACAO: {
        'webservice': 'CteRetRecepcao',
        'metodo'    : 'cteRetRecepcao',
    },
    WS_CTE_INUTILIZACAO: {
        'webservice': 'CteInutilizacao',
        'metodo'    : 'cteInutilizacaoCT',
    },
    WS_CTE_CONSULTA: {
        #'webservice': 'CteConsultaProtocolo',
        'webservice': 'CteConsulta',
        'metodo'    : 'cteConsultaCT',
    },
    WS_CTE_SITUACAO: {
        'webservice': 'CteStatusServico',
        'metodo'    : 'cteStatusServicoCT',
    },
    WS_CTE_RECEPCAO_EVENTO: {
        'webservice': 'CteRecepcaoEvento',
        'metodo'    : 'cteRecepcaoEvento',
    },
    WS_CTE_RECEPCAO_OS: {
        'webservice': 'CTeRecepcaoOS',
        'metodo'    : 'cteRecepcaoOS',
    },
    WS_CTE_DISTRIBUICAO: {
        'webservice': 'CTeDistribuicaoDFe',
        'metodo'    : 'cteDistDFeInteresse',
    },
}

SVRS = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'cte.svrs.rs.gov.br',
        WS_CTE_AUTORIZACAO         : 'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_CONSULTA_AUTORIZACAO: 'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO        : 'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA            : 'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_SITUACAO            : 'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_RECEPCAO_EVENTO     : 'ws/cterecepcaoevento/cterecepcaoevento.asmx',
        WS_CTE_RECEPCAO_OS         : 'ws/cterecepcaoos/cterecepcaoos.asmx',
    },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'cte-homologacao.svrs.rs.gov.br',
        WS_CTE_AUTORIZACAO         : 'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_CONSULTA_AUTORIZACAO: 'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO        : 'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA            : 'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_SITUACAO            : 'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_RECEPCAO_EVENTO     : 'ws/cterecepcaoevento/cterecepcaoevento.asmx',
        WS_CTE_RECEPCAO_OS         : 'ws/cterecepcaoos/cterecepcaoos.asmx',
    },
}

SVSP = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.fazenda.sp.gov.br',
        WS_CTE_AUTORIZACAO         : 'cteWEB/services/CteRecepcao.asmx',
        WS_CTE_CONSULTA_AUTORIZACAO: 'cteWEB/services/CteRetRecepcao.asmx',
        WS_CTE_CONSULTA            : 'cteWEB/services/CteConsulta.asmx',
        WS_CTE_SITUACAO            : 'cteWEB/services/CteStatusServico.asmx',
    },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.nfe.fazenda.sp.gov.br',
        WS_CTE_AUTORIZACAO         : 'cteWEB/services/CteRecepcao.asmx',
        WS_CTE_CONSULTA_AUTORIZACAO: 'cteWEB/services/CteRetRecepcao.asmx',
        WS_CTE_CONSULTA            : 'cteWEB/services/CteConsulta.asmx',
        WS_CTE_SITUACAO            : 'cteWEB/services/CteStatusServico.asmx',
    },
}

AN = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor': 'www1.cte.fazenda.gov.br',
        WS_CTE_DISTRIBUICAO: 'CTeDistribuicaoDFe/CTeDistribuicaoDFe.asmx',
    },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor': 'hom1.cte.fazenda.gov.br',
        WS_CTE_DISTRIBUICAO: 'CTeDistribuicaoDFe/CTeDistribuicaoDFe.asmx',
    },
}

UFMT = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'cte.sefaz.mt.gov.br',
        WS_CTE_AUTORIZACAO         : 'ctews/services/CteRecepcao',
        WS_CTE_CONSULTA_AUTORIZACAO: 'ctews/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO        : 'ctews/services/CteInutilizacao',
        WS_CTE_CONSULTA            : 'ctews/services/CteConsulta',
        WS_CTE_SITUACAO            : 'ctews/services/CteStatusServico',
        WS_CTE_RECEPCAO_EVENTO     : 'ctews2/services/CteRecepcaoEvento?wsdl',
        WS_CTE_RECEPCAO_OS         : 'ctews/services/CteRecepcaoOS',
    },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.sefaz.mt.gov.br',
        WS_CTE_AUTORIZACAO         : 'ctews/services/CteRecepcao',
        WS_CTE_CONSULTA_AUTORIZACAO: 'ctews/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO        : 'ctews/services/CteInutilizacao',
        WS_CTE_CONSULTA            : 'ctews/services/CteConsulta',
        WS_CTE_SITUACAO            : 'ctews/services/CteStatusServico',
        WS_CTE_RECEPCAO_EVENTO     : 'ctews2/services/CteRecepcaoEvento?wsdl',
        WS_CTE_RECEPCAO_OS         : 'ctews/services/CteRecepcaoOS',
    },
}

UFMS = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'producao.cte.ms.gov.br',
        WS_CTE_AUTORIZACAO         : 'ws/CteRecepcao',
        WS_CTE_CONSULTA_AUTORIZACAO: 'ws/CteRetRecepcao',
        WS_CTE_INUTILIZACAO        : 'ws/CteInutilizacao',
        WS_CTE_CONSULTA            : 'ws/CteConsulta',
        WS_CTE_SITUACAO            : 'ws/CteStatusServico',
        WS_CTE_RECEPCAO_EVENTO     : 'ws/CteRecepcaoEvento',
        WS_CTE_RECEPCAO_OS         : 'ws/CteRecepcaoOS',
    },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.cte.ms.gov.br',
        WS_CTE_AUTORIZACAO         : 'ws/CteRecepcao',
        WS_CTE_CONSULTA_AUTORIZACAO: 'ws/CteRetRecepcao',
        WS_CTE_INUTILIZACAO        : 'ws/CteInutilizacao',
        WS_CTE_CONSULTA            : 'ws/CteConsulta',
        WS_CTE_SITUACAO            : 'ws/CteStatusServico',
        WS_CTE_RECEPCAO_EVENTO     : 'ws/CteRecepcaoEvento',
        WS_CTE_RECEPCAO_OS         : 'ws/CteRecepcaoOS',
    },
}

UFMG = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'cte.fazenda.mg.gov.br',
        WS_CTE_AUTORIZACAO         : 'cte/services/CteRecepcao',
        WS_CTE_CONSULTA_AUTORIZACAO: 'cte/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO        : 'cte/services/CteInutilizacao',
        WS_CTE_CONSULTA            : 'cte/services/CteConsulta',
        WS_CTE_SITUACAO            : 'cte/services/CteStatusServico',
        WS_CTE_RECEPCAO_EVENTO     : 'cte/services/RecepcaoEvento',
        WS_CTE_RECEPCAO_OS         : 'cte/services/CteRecepcaoOS',
    },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'hcte.fazenda.mg.gov.br',
        WS_CTE_AUTORIZACAO         : 'cte/services/CteRecepcao',
        WS_CTE_CONSULTA_AUTORIZACAO: 'cte/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO        : 'cte/services/CteInutilizacao',
        WS_CTE_CONSULTA            : 'cte/services/CteConsulta',
        WS_CTE_SITUACAO            : 'cte/services/CteStatusServico',
        WS_CTE_RECEPCAO_EVENTO     : 'cte/services/RecepcaoEvento',
        WS_CTE_RECEPCAO_OS         : 'cte/services/CteRecepcaoOS',
    },
}

UFPR = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'cte.fazenda.pr.gov.br',
        WS_CTE_AUTORIZACAO         : 'cte/CteRecepcao',
        WS_CTE_CONSULTA_AUTORIZACAO: 'cte/CteRetRecepcao',
        WS_CTE_INUTILIZACAO        : 'cte/CteInutilizacao',
        WS_CTE_CONSULTA            : 'cte/CteConsulta',
        WS_CTE_SITUACAO            : 'cte/CteStatusServico',
        WS_CTE_RECEPCAO_EVENTO     : 'cte/CteRecepcaoEvento',
        WS_CTE_RECEPCAO_OS         : 'cte/CteRecepcaoOS',
    },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.cte.fazenda.pr.gov.br',
        WS_CTE_AUTORIZACAO         : 'cte/CteRecepcao',
        WS_CTE_CONSULTA_AUTORIZACAO: 'cte/CteRetRecepcao',
        WS_CTE_INUTILIZACAO        : 'cte/CteInutilizacao',
        WS_CTE_CONSULTA            : 'cte/CteConsulta',
        WS_CTE_SITUACAO            : 'cte/CteStatusServico',
        WS_CTE_RECEPCAO_EVENTO     : 'cte/CteRecepcaoEvento',
        WS_CTE_RECEPCAO_OS         : 'cte/CteRecepcaoOS',
    },
}

UFRS = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'cte.svrs.rs.gov.br',
        WS_CTE_AUTORIZACAO         : 'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_CONSULTA_AUTORIZACAO: 'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO        : 'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA            : 'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_SITUACAO            : 'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_RECEPCAO_EVENTO     : 'ws/cterecepcaoevento/cterecepcaoevento.asmx',
        WS_CTE_RECEPCAO_OS         : 'ws/cterecepcaoos/cterecepcaoos.asmx',
    },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'cte-homologacao.svrs.rs.gov.br',
        WS_CTE_AUTORIZACAO         : 'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_CONSULTA_AUTORIZACAO: 'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO        : 'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA            : 'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_SITUACAO            : 'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_RECEPCAO_EVENTO     : 'ws/cterecepcaoevento/cterecepcaoevento.asmx',
        WS_CTE_RECEPCAO_OS         : 'ws/cterecepcaoos/cterecepcaoos.asmx',
    },
}

UFSP = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.fazenda.sp.gov.br',
        WS_CTE_AUTORIZACAO         : 'cteWEB/services/cteRecepcao.asmx',
        WS_CTE_CONSULTA_AUTORIZACAO: 'cteWEB/services/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO        : 'cteWEB/services/cteInutilizacao.asmx',
        WS_CTE_CONSULTA            : 'cteWEB/services/cteConsulta.asmx',
        WS_CTE_SITUACAO            : 'cteWEB/services/cteStatusServico.asmx',
        WS_CTE_RECEPCAO_EVENTO     : 'cteweb/services/cteRecepcaoEvento.asmx',
        WS_CTE_RECEPCAO_OS         : 'cteWEB/services/cteRecepcaoOS.asmx',
    },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.nfe.fazenda.sp.gov.br',
        WS_CTE_AUTORIZACAO         : 'cteWEB/services/cteRecepcao.asmx',
        WS_CTE_CONSULTA_AUTORIZACAO: 'cteWEB/services/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO        : 'cteWEB/services/cteInutilizacao.asmx',
        WS_CTE_CONSULTA            : 'cteWEB/services/cteConsulta.asmx',
        WS_CTE_SITUACAO            : 'cteWEB/services/cteStatusServico.asmx',
        WS_CTE_RECEPCAO_EVENTO     : 'cteweb/services/cteRecepcaoEvento.asmx',
        WS_CTE_RECEPCAO_OS         : 'cteWEB/services/cteRecepcaoOS.asmx',
    },
}

#
# Informação obtida em
# http://www.cte.fazenda.gov.br/portal/webServices.aspx?tipoConteudo=wpdBtfbTMrw=
#  Última verificação: 20/04/2018
#Estados que utilizam a SVSP - Sefaz Virtual de São Paulo: AP, PE, RR
#Estados que utilizam a SVRS - Sefaz Virtual do RS: AC, AL, AM, BA, CE, DF, ES, GO, MA, PA, PB, PI, RJ, RN, RO, SC, SE, TO
#

ESTADO_WS = {
    'AC': SVRS,
    'AL': SVRS,
    'AM': SVRS,
    'AP': SVSP,
    'BA': SVRS,
    'CE': SVRS,
    'DF': SVRS,
    'ES': SVRS,
    'GO': SVRS,
    'MA': SVRS,
    'MG': UFMG,
    'MS': SVRS,
    'MT': UFMT,
    'PA': SVRS,
    'PB': SVRS,
    'PE': SVSP,
    'PI': SVRS,
    'PR': UFPR,
    'RJ': SVRS,
    'RN': SVRS,
    'RO': SVRS,
    'RR': SVSP,
    'RS': UFRS,
    'SC': SVRS,
    'SE': SVRS,
    'SP': UFSP,
    'TO': SVRS
}
