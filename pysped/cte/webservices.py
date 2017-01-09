# -*- coding: utf-8 -*-

from webservices_flags import *

#Ultima atualização: 01/12/2016

METODO_WS = {
    WS_CTE_RECEPCAO: {
        u'webservice': u'CteRecepcao',
        u'metodo'    : u'cteRecepcaoLote',
    },
    WS_CTE_RET_RECEPCAO: {
        u'webservice': u'CteRetRecepcao',
        u'metodo'    : u'cteRetRecepcao',
    },
    WS_CTE_INUTILIZACAO: {
        u'webservice': u'CteInutilizacao',
        u'metodo'    : u'cteInutilizacaoCT',
    },
    WS_CTE_CONSULTA: {
        #u'webservice': u'CteConsultaProtocolo',
        u'webservice': u'CteConsulta',
        u'metodo'    : u'cteConsultaCT',
    },
    WS_CTE_STATUS_SERVICO: {
        u'webservice': u'CteStatusServico',
        u'metodo'    : u'cteStatusServicoCT',
    },
    WS_CTE_EVENTO: {
        u'webservice': u'CteRecepcaoEvento',
        u'metodo'    : u'cteRecepcaoEvento',
    },
    WS_CTE_CONSULTA_CADASTRO: {
        u'webservice': u'CadConsultaCadastro',
        u'metodo'    : u'consultaCadastro2',
    }
}

SVRS = {
    CTE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'cte.svrs.rs.gov.br',
        WS_CTE_RECEPCAO        : u'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO : u'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO    : u'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA    : u'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO        : u'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_EVENTO        : u'ws/cterecepcaoevento/cterecepcaoevento.asmx'
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'cte-homologacao.svrs.rs.gov.br',
        WS_CTE_RECEPCAO        : u'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO : u'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO    : u'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA    : u'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO        : u'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_EVENTO        : u'ws/cterecepcaoevento/cterecepcaoevento.asmx'
        }
}

SVSP = {
    CTE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'nfe.fazenda.sp.gov.br',
        WS_CTE_RECEPCAO        : u'cteWEB/services/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO : u'cteWEB/services/CteRetRecepcao.asmx',
        WS_CTE_CONSULTA    : u'cteWEB/services/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO        : u'cteWEB/services/CteStatusServico.asmx',
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'homologacao.nfe.fazenda.sp.gov.br',
        WS_CTE_RECEPCAO        : u'cteWEB/services/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO : u'cteWEB/services/CteRetRecepcao.asmx',
        WS_CTE_CONSULTA    : u'cteWEB/services/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO        : u'cteWEB/services/CteStatusServico.asmx',
        }
}

UFMT = {
    CTE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'cte.sefaz.mt.gov.br',
        WS_CTE_RECEPCAO        : u'ctews/services/CteRecepcao',
        WS_CTE_RET_RECEPCAO : u'ctews/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : u'ctews/services/CteInutilizacao',
        WS_CTE_CONSULTA    : u'ctews/services/CteConsulta',
        WS_CTE_STATUS_SERVICO        : u'ctews/services/CteStatusServico',
        WS_CTE_EVENTO        : u'ctews2/services/CteRecepcaoEvento?wsdl'
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'homologacao.sefaz.mt.gov.br',
        WS_CTE_RECEPCAO        : u'ctews/services/CteRecepcao',
        WS_CTE_RET_RECEPCAO : u'ctews/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : u'ctews/services/CteInutilizacao',
        WS_CTE_CONSULTA    : u'ctews/services/CteConsulta',
        WS_CTE_STATUS_SERVICO        : u'ctews/services/CteStatusServico',
        WS_CTE_EVENTO        : u'ctews2/services/CteRecepcaoEvento?wsdl'
        }
}

UFMS = {
    CTE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'producao.cte.ms.gov.br',
        WS_CTE_RECEPCAO        : u'ws/CteRecepcao',
        WS_CTE_RET_RECEPCAO : u'ws/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : u'ws/CteInutilizacao',
        WS_CTE_CONSULTA    : u'ws/CteConsulta',
        WS_CTE_STATUS_SERVICO        : u'ws/CteStatusServico',
        WS_CTE_CONSULTA_CADASTRO : u'ws/CadConsultaCadastro',
        WS_CTE_EVENTO        : u'ws/CteRecepcaoEvento'
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'homologacao.cte.ms.gov.br',
        WS_CTE_RECEPCAO        : u'ws/CteRecepcao',
        WS_CTE_RET_RECEPCAO : u'ws/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : u'ws/CteInutilizacao',
        WS_CTE_CONSULTA    : u'ws/CteConsulta',
        WS_CTE_STATUS_SERVICO        : u'ws/CteStatusServico',
        WS_CTE_CONSULTA_CADASTRO : u'ws/CadConsultaCadastro',
        WS_CTE_EVENTO        : u'ws/CteRecepcaoEvento'
        }
}

UFMG = {
    CTE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'cte.fazenda.mg.gov.br',
        WS_CTE_RECEPCAO        : u'cte/services/CteRecepcao',
        WS_CTE_RET_RECEPCAO : u'cte/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : u'cte/services/CteInutilizacao',
        WS_CTE_CONSULTA    : u'cte/services/CteConsulta',
        WS_CTE_STATUS_SERVICO        : u'cte/services/CteStatusServico',
        WS_CTE_EVENTO        : u'cte/services/RecepcaoEvento'
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'hcte.fazenda.mg.gov.br',
        WS_CTE_RECEPCAO        : u'cte/services/CteRecepcao',
        WS_CTE_RET_RECEPCAO : u'cte/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : u'cte/services/CteInutilizacao',
        WS_CTE_CONSULTA    : u'cte/services/CteConsulta',
        WS_CTE_STATUS_SERVICO        : u'cte/services/CteStatusServico',
        WS_CTE_EVENTO        : u'cte/services/RecepcaoEvento'
        }
}

UFPR = {
    CTE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'cte.fazenda.pr.gov.br',
        WS_CTE_RECEPCAO         : u'cte/CteRecepcao',
        WS_CTE_RET_RECEPCAO     : u'cte/CteRetRecepcao',
        WS_CTE_INUTILIZACAO     : u'cte/CteInutilizacao',
        WS_CTE_CONSULTA         : u'cte/CteConsulta',
        WS_CTE_STATUS_SERVICO   : u'cte/CteStatusServico',
        WS_CTE_EVENTO           : u'cte/CteRecepcaoEvento'
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'homologacao.cte.fazenda.pr.gov.br',
        WS_CTE_RECEPCAO         : u'cte/CteRecepcao',
        WS_CTE_RET_RECEPCAO     : u'cte/CteRetRecepcao',
        WS_CTE_INUTILIZACAO     : u'cte/CteInutilizacao',
        WS_CTE_CONSULTA         : u'cte/CteConsulta',
        WS_CTE_STATUS_SERVICO   : u'cte/CteStatusServico',
        WS_CTE_EVENTO           : u'cte/CteRecepcaoEvento'
        }
}

UFRS = {
    CTE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'cte.svrs.rs.gov.br',
        WS_CTE_RECEPCAO         : u'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO     : u'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO     : u'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA         : u'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO   : u'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_EVENTO           : u'ws/cterecepcaoevento/cterecepcaoevento.asmx',
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'cte-homologacao.svrs.rs.gov.br',
        WS_CTE_RECEPCAO         : u'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO     : u'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO     : u'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA         : u'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO   : u'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_EVENTO           : u'ws/cterecepcaoevento/cterecepcaoevento.asmx',
        }
}

UFSP = {
    CTE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'nfe.fazenda.sp.gov.br',
        WS_CTE_RECEPCAO         : u'cteWEB/services/cteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO     : u'cteWEB/services/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO     : u'cteWEB/services/cteInutilizacao.asmx',
        WS_CTE_CONSULTA         : u'cteWEB/services/cteConsulta.asmx',
        WS_CTE_STATUS_SERVICO   : u'cteWEB/services/cteStatusServico.asmx',
        WS_CTE_EVENTO           : u'cteweb/services/cteRecepcaoEvento.asmx',
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'homologacao.nfe.fazenda.sp.gov.br',
        WS_CTE_RECEPCAO         : u'cteWEB/services/cteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO     : u'cteWEB/services/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO     : u'cteWEB/services/cteInutilizacao.asmx',
        WS_CTE_CONSULTA         : u'cteWEB/services/cteConsulta.asmx',
        WS_CTE_STATUS_SERVICO   : u'cteWEB/services/cteStatusServico.asmx',
        WS_CTE_EVENTO           : u'cteweb/services/cteRecepcaoEvento.asmx',
        }
}

#
# Informação obtida em 
# http://www.cte.fazenda.gov.br/portal/webServices.aspx?tipoConteudo=wpdBtfbTMrw=
#  Última verificação: 01/12/2016
#Estados que utilizam a SVSP - Sefaz Virtual de São Paulo: AP, PE, RR 
#Estados que utilizam a SVRS - Sefaz Virtual do RS: AC, AL, AM, BA, CE, DF, ES, GO, MA, PA, PB, PI, RJ, RN, RO, SC, SE, TO
#

ESTADO_WS = {
    u'AC': SVRS,
    u'AL': SVRS,
    u'AM': SVRS,
    u'AP': SVSP,
    u'BA': SVRS,
    u'CE': SVRS,
    u'DF': SVRS,
    u'ES': SVRS,
    u'GO': SVRS,
    u'MA': SVRS,
    u'MG': UFMG,
    u'MS': SVRS,
    u'MT': UFMT,
    u'PA': SVRS,
    u'PB': SVRS,
    u'PE': SVSP,
    u'PI': SVRS,
    u'PR': UFPR,
    u'RJ': SVRS,
    u'RN': SVRS,
    u'RO': SVRS,
    u'RR': SVSP,
    u'RS': UFRS,
    u'SC': SVRS,
    u'SE': SVRS,
    u'SP': UFSP,
    u'TO': SVRS
}   
