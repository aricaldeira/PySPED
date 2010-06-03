# -*- coding: utf-8 -*-

from webservices_flags import *


METODO_WS = {
    WS_NFE_ENVIO_LOTE: {
        u'webservice': u'NfeRecepcao2',
        u'metodo'    : u'nfeRecepcaoLote2',
    },
    WS_NFE_CONSULTA_RECIBO: {
        u'webservice': u'NfeRetRecepcao2',
        u'metodo'    : u'nfeRetRecepcao2',
    },
    WS_NFE_CANCELAMENTO: {
        u'webservice': u'NfeCancelamento2',
        u'metodo'    : u'nfeCancelamentoNF2',
    },
    WS_NFE_INUTILIZACAO: {
        u'webservice': u'NfeInutilizacao2',
        u'metodo'    : u'nfeInutilizacaoNF2',
    },
    WS_NFE_CONSULTA: {
        u'webservice': u'NfeConsulta2',
        u'metodo'    : u'nfeConsultaNF2',
    },
    WS_NFE_SITUACAO: {
        u'webservice': u'NfeStatusServico2',
        u'metodo'    : u'nfeStatusServicoNF2',
    },
    WS_NFE_CONSULTA_CADASTRO: {
        u'webservice': u'CadConsultaCadastro2',
        u'metodo'    : u'consultaCadastro2',
    }
}

SVRS = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE        : u'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO: u'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : u'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'ws/nfestatusservico/NfeStatusServico2.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'homologacao.nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE        : u'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO: u'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : u'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'ws/nfestatusservico/NfeStatusServico2.asmx'
        }
}

SVAN = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'www.sefazvirtual.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'NFeRetRecepcao2/NFeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'NFeCancelamento2/NFeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : u'NFeInutilizacao2/NFeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'nfeconsulta2/nfeconsulta2.asmx',
        WS_NFE_SITUACAO        : u'NFeStatusServico2/NFeStatusServico2.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'hom.sefazvirtual.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'NFeRetRecepcao2/NFeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'NFeCancelamento2/NFeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : u'NFeInutilizacao2/NFeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'nfeconsulta2/nfeconsulta2.asmx',
        WS_NFE_SITUACAO        : u'NFeStatusServico2/NFeStatusServico2.asmx'
        }
}

SCAN = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'www.scan.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'NfeRetRecepcao2/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'NfeCancelamento2/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : u'NfeInutilizacao2/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'NfeConsulta2/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'NfeStatusServico2/NfeStatusServico2.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'hom.nfe.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'SCAN/NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'SCAN/NfeRetRecepcao2/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'SCAN/NfeCancelamento2/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : u'SCAN/NfeInutilizacao2/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'SCAN/NfeConsulta2/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'SCAN/NfeStatusServico2/NfeStatusServico2.asmx'
        }
}

DPEC = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'     : u'www.nfe.fazenda.gov.br',
        WS_DPEC_CONSULTA: u'SCERecepcaoRFB/SCERecepcaoRFB.asmx',
        WS_DPEC_RECEPCAO: u'SCEConsultaRFB/SCEConsultaRFB.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'     : u'hom.nfe.fazenda.gov.br',
        WS_DPEC_CONSULTA: u'SCERecepcaoRFB/SCERecepcaoRFB.asmx',
        WS_DPEC_RECEPCAO: u'SCEConsultaRFB/SCEConsultaRFB.asmx'
    }
}

#UFAM = {
    #NFE_AMBIENTE_PRODUCAO: {
        #u'servidor'            : u'nfe.sefaz.am.gov.br',
        #WS_NFE_ENVIO_LOTE        : u'ws/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO: u'ws/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO    : u'ws/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO    : u'ws/services/NfeInutilizacao',
        #WS_NFE_CONSULTA        : u'ws/services/NfeConsulta',
        #WS_NFE_SITUACAO        : u'ws/services/NfeStatusServico'
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #u'servidor'            : u'homnfe.sefaz.am.gov.br',
        #WS_NFE_ENVIO_LOTE        : u'ws/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO: u'ws/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO    : u'ws/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO    : u'ws/services/NfeInutilizacao',
        #WS_NFE_CONSULTA        : u'ws/services/NfeConsulta',
        #WS_NFE_SITUACAO        : u'ws/services/NfeStatusServico'
        #}
#}

UFBA = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.sefaz.ba.gov.br',
        WS_NFE_ENVIO_LOTE       : u'webservices/nfe/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'webservices/nfe/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'webservices/nfe/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'webservices/nfe/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'webservices/nfe/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : u'webservices/nfe/NfeStatusServico2.asmx',
        #WS_NFE_CONSULTA_CADASTRO: u'webservices/nfe/NfeConsulta2.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'hnfe.sefaz.ba.gov.br',
        WS_NFE_ENVIO_LOTE      : u'webservices/nfenw/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'webservices/nfenw/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'webservices/nfenw/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : u'webservices/nfenw/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'webservices/nfenw/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'webservices/nfenw/NfeStatusServico2.asmx'
        }
}

#UFCE = {
    #NFE_AMBIENTE_PRODUCAO: {
        #u'servidor'             : u'nfe.sefaz.ce.gov.br',
        #WS_NFE_ENVIO_LOTE         : u'nfe/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : u'nfe/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : u'nfe/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : u'nfe/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : u'nfe/services/NfeConsulta',
        #WS_NFE_SITUACAO         : u'nfe/services/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: u'nfe/services/CadConsultaCadastro'
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #u'servidor'             : u'nfeh.sefaz.ce.gov.br',
        #WS_NFE_ENVIO_LOTE         : u'nfe/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : u'nfe/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : u'nfe/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : u'nfe/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : u'nfe/services/NfeConsulta',
        #WS_NFE_SITUACAO         : u'nfe/services/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: u'nfe/services/CadConsultaCadastro'
        #}
#}

#UFDF = {
    #NFE_AMBIENTE_PRODUCAO: {
        #u'servidor'             : u'dec.fazenda.df.gov.br',
        #WS_NFE_ENVIO_LOTE         : u'nfe/ServiceRecepcao.asmx',
        #WS_NFE_CONSULTA_RECIBO : u'nfe/ServiceRetRecepcao.asmx',
        #WS_NFE_CANCELAMENTO     : u'nfe/ServiceCancelamento.asmx',
        #WS_NFE_INUTILIZACAO     : u'nfe/ServiceInutilizacao.asmx',
        #WS_NFE_CONSULTA         : u'nfe/ServiceConsulta.asmx',
        #WS_NFE_SITUACAO         : u'nfe/ServiceStatus.asmx',
        #WS_NFE_CONSULTA_CADASTRO: u'nfe/ServiceConsultaCadastro.asmx',
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #u'servidor'             : u'homolog.nfe.fazenda.df.gov.br',
        #WS_NFE_ENVIO_LOTE         : u'nfe/ServiceRecepcao.asmx',
        #WS_NFE_CONSULTA_RECIBO : u'nfe/ServiceRetRecepcao.asmx',
        #WS_NFE_CANCELAMENTO     : u'nfe/ServiceCancelamento.asmx',
        #WS_NFE_INUTILIZACAO     : u'nfe/ServiceInutilizacao.asmx',
        #WS_NFE_CONSULTA         : u'nfe/ServiceConsulta.asmx',
        #WS_NFE_SITUACAO         : u'nfe/ServiceStatus.asmx',
        #WS_NFE_CONSULTA_CADASTRO: u'nfe/ServiceConsultaCadastro.asmx'
        #}
#}

UFGO = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.sefaz.go.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe/services/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe/services/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe/services/v2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe/services/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe/services/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe/services/v2/NfeStatusServico2',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homolog.sefaz.go.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe/services/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe/services/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe/services/v2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe/services/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe/services/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe/services/v2/NfeStatusServico2',
        }
}

UFMT = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.sefaz.mt.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfews/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfews/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfews/v2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfews/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfews/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfews/v2/NfeStatusServico2',
        #WS_NFE_CONSULTA_CADASTRO: u'nfews/CadConsultaCadastro'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homologacao.sefaz.mt.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfews/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfews/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfews/v2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfews/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfews/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfews/v2/NfeStatusServico2',
        #WS_NFE_CONSULTA_CADASTRO: u'nfews/CadConsultaCadastro'
        }
}

#UFMS = {
    #NFE_AMBIENTE_PRODUCAO: {
        #u'servidor'             : u'producao.nfe.ms.gov.br',
        #WS_NFE_ENVIO_LOTE         : u'producao/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : u'producao/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : u'producao/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : u'producao/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : u'producao/services/NfeConsulta',
        #WS_NFE_SITUACAO         : u'producao/services/NfeStatusServico'
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #u'servidor'             : u'homologacao.nfe.ms.gov.br',
        #WS_NFE_ENVIO_LOTE         : u'homologacao/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : u'homologacao/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : u'homologacao/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : u'homologacao/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : u'homologacao/services/NfeConsulta',
        #WS_NFE_SITUACAO         : u'homologacao/services/NfeStatusServico'
        #}
#}

UFMG = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.fazenda.mg.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe2/services/NfeStatus2',
        #WS_NFE_CONSULTA_CADASTRO: u'nfe2/services/CadConsultaCadastro'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'hnfe.fazenda.mg.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe2/services/NfeStatus2',
        #WS_NFE_CONSULTA_CADASTRO: u'nfe2/services/CadConsultaCadastro'
        }
}

UFPR = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.fazenda.pr.gov.br',
        WS_NFE_ENVIO_LOTE         : u'NFENWebServices/services/nfeRecepcao',
        WS_NFE_CONSULTA_RECIBO : u'NFENWebServices/services/nfeRetRecepcao',
        WS_NFE_CANCELAMENTO     : u'NFENWebServices/services/nfeCancelamentoNF',
        WS_NFE_INUTILIZACAO     : u'NFENWebServices/services/nfeInutilizacaoNF',
        WS_NFE_CONSULTA         : u'NFENWebServices/services/nfeConsultaNF',
        WS_NFE_SITUACAO         : u'NFENWebServices/services/nfeStatusServicoNF'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homologacao.nfe.fazenda.pr.gov.br',
        WS_NFE_ENVIO_LOTE         : u'NFENWebServices/services/nfeRecepcao',
        WS_NFE_CONSULTA_RECIBO : u'NFENWebServices/services/nfeRetRecepcao',
        WS_NFE_CANCELAMENTO     : u'NFENWebServices/services/nfeCancelamentoNF',
        WS_NFE_INUTILIZACAO     : u'NFENWebServices/services/nfeInutilizacaoNF',
        WS_NFE_CONSULTA         : u'NFENWebServices/services/nfeConsultaNF',
        WS_NFE_SITUACAO         : u'NFENWebServices/services/nfeStatusServicoNF'
        }
}

#UFPE = {
    #NFE_AMBIENTE_PRODUCAO: {
        #u'servidor'             : u'nfe.sefaz.pe.gov.br',
        #WS_NFE_ENVIO_LOTE         : u'nfe-service/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : u'nfe-service/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : u'nfe-service/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : u'nfe-service/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : u'nfe-service/services/NfeConsulta',
        #WS_NFE_SITUACAO         : u'nfe-service/services/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: u'nfe-service/services/CadConsultaCadastro'
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #u'servidor'             : u'nfehomolog.sefaz.pe.gov.br',
        #WS_NFE_ENVIO_LOTE         : u'nfe-service/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : u'nfe-service/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : u'nfe-service/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : u'nfe-service/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : u'nfe-service/services/NfeConsulta',
        #WS_NFE_SITUACAO         : u'nfe-service/services/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: u'nfe-service/services/CadConsultaCadastro'
    #}
#}


UFRS = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.sefaz.rs.gov.br',
        WS_NFE_ENVIO_LOTE         : u'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : u'ws/nfestatusservico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'ws/CadConsultaCadastro/CadConsultaCadastro2.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homologacao.nfe.sefaz.rs.gov.br',
        WS_NFE_ENVIO_LOTE         : u'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : u'ws/nfestatusservico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'ws/CadConsultaCadastro/CadConsultaCadastro2.asmx'
    }
}

#UFRO = {
    #NFE_AMBIENTE_PRODUCAO: {
        #u'servidor'             : u'ws.nfe.sefin.ro.gov.br',
        #WS_NFE_ENVIO_LOTE         : SVRS[NFE_AMBIENTE_PRODUCAO][WS_NFE_ENVIO_LOTE],
        #WS_NFE_CONSULTA_RECIBO : SVRS[NFE_AMBIENTE_PRODUCAO][WS_NFE_CONSULTA_RECIBO],
        #WS_NFE_CANCELAMENTO     : u'wsprod/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : SVRS[NFE_AMBIENTE_PRODUCAO][WS_NFE_INUTILIZACAO],
        #WS_NFE_CONSULTA         : u'wsprod/NfeConsulta',
        #WS_NFE_SITUACAO         : u'wsprod/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: u'wsprod/CadConsultaCadastro'
    #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #u'servidor'             : u'ws.nfe.sefin.ro.gov.br',
        #WS_NFE_ENVIO_LOTE         : SVRS[NFE_AMBIENTE_HOMOLOGACAO][WS_NFE_ENVIO_LOTE],
        #WS_NFE_CONSULTA_RECIBO : SVRS[NFE_AMBIENTE_HOMOLOGACAO][WS_NFE_CONSULTA_RECIBO],
        #WS_NFE_CANCELAMENTO     : u'ws/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : SVRS[NFE_AMBIENTE_HOMOLOGACAO][WS_NFE_INUTILIZACAO],
        #WS_NFE_CONSULTA         : u'ws/NfeConsulta',
        #WS_NFE_SITUACAO         : u'ws/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: u'ws/CadConsultaCadastro'
    #}
#}

UFSP = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.fazenda.sp.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfeweb/services/nferecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'nfeweb/services/nferetrecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'nfeweb/services/nfecancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'nfeweb/services/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'nfeweb/services/nfeconsulta2.asmx',
        WS_NFE_SITUACAO         : u'nfeweb/services/nfestatusservico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'nfeweb/services/cadconsultacadastro.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homologacao.nfe.fazenda.sp.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfeweb/services/nferecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'nfeweb/services/nferetrecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'nfeweb/services/nfecancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'nfeweb/services/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'nfeweb/services/nfeconsulta2.asmx',
        WS_NFE_SITUACAO         : u'nfeweb/services/nfestatusservico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'nfeWEB/services/cadconsultacadastro.asmx'
        }
}

#
# Informação obtida em
# http://www.nfe.fazenda.gov.br/portal/VerificacaoDeServicos/VerificacaoServicos.aspx
#  Última verificação: 07/04/2010 16:30:14
#  * Estados Emissores pela Sefaz Virtual RS (Rio Grande do Sul): AC, AL, AM, AP, DF, MS, PB, RJ, RO, RR, SC, SE e TO.
#  ** Estados Emissores pela Sefaz Virtual AN (Ambiente Nacional): CE, ES, MA, PA, PI e RN.
# Estados que têm seus próprios servidores: BA, GO, MG, MT, PE, PR, SP.
#


ESTADO_WS = {
    u'AC': SVRS,
    u'AL': SVRS,
    u'AM': SVRS,
    u'AP': SVRS,
    u'BA': UFBA,
    u'CE': SVAN,
    u'DF': SVRS,
    u'ES': SVAN,
    u'GO': UFGO,
    u'MA': SVAN,
    u'MG': UFMG,
    u'MS': SVRS,
    #u'MT': UFMT,
    u'PA': SVAN,
    u'PB': SVRS,
    #u'PE': UFPE,
    u'PI': SVAN,
    u'PR': UFPR,
    u'RJ': SVRS,
    u'RN': SVAN,
    u'RO': SVRS,
    u'RR': SVRS,
    u'RS': UFRS,
    u'SC': SVRS,
    u'SE': SVRS,
    u'SP': UFSP,
    u'TO': SVRS
}
