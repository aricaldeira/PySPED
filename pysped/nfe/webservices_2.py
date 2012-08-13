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

from .webservices_flags import *


METODO_WS = {
    WS_NFE_ENVIO_LOTE: {
        'webservice': 'NfeRecepcao2',
        'metodo'    : 'nfeRecepcaoLote2',
    },
    WS_NFE_CONSULTA_RECIBO: {
        'webservice': 'NfeRetRecepcao2',
        'metodo'    : 'nfeRetRecepcao2',
    },
    WS_NFE_CANCELAMENTO: {
        'webservice': 'NfeCancelamento2',
        'metodo'    : 'nfeCancelamentoNF2',
    },
    WS_NFE_INUTILIZACAO: {
        'webservice': 'NfeInutilizacao2',
        'metodo'    : 'nfeInutilizacaoNF2',
    },
    WS_NFE_CONSULTA: {
        'webservice': 'NfeConsulta2',
        'metodo'    : 'nfeConsultaNF2',
    },
    WS_NFE_SITUACAO: {
        'webservice': 'NfeStatusServico2',
        'metodo'    : 'nfeStatusServicoNF2',
    },
    WS_NFE_CONSULTA_CADASTRO: {
        'webservice': 'CadConsultaCadastro2',
        'metodo'    : 'consultaCadastro2',
    }
}

SVRS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'            : 'nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE        : 'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO: 'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : 'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : 'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : 'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : 'ws/nfestatusservico/NfeStatusServico2.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'homologacao.nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE        : 'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO: 'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : 'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : 'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : 'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : 'ws/nfestatusservico/NfeStatusServico2.asmx'
        }
}

SVAN = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'            : 'www.sefazvirtual.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : 'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : 'NFeRetRecepcao2/NFeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : 'NFeCancelamento2/NFeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : 'NFeInutilizacao2/NFeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : 'nfeconsulta2/nfeconsulta2.asmx',
        WS_NFE_SITUACAO        : 'NFeStatusServico2/NFeStatusServico2.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'hom.sefazvirtual.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : 'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : 'NFeRetRecepcao2/NFeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : 'NFeCancelamento2/NFeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : 'NFeInutilizacao2/NFeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : 'nfeconsulta2/nfeconsulta2.asmx',
        WS_NFE_SITUACAO        : 'NFeStatusServico2/NFeStatusServico2.asmx'
        }
}

SCAN = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'            : 'www.scan.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : 'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : 'NfeRetRecepcao2/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : 'NfeCancelamento2/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : 'NfeInutilizacao2/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : 'NfeConsulta2/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : 'NfeStatusServico2/NfeStatusServico2.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'hom.nfe.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : 'SCAN/NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : 'SCAN/NfeRetRecepcao2/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : 'SCAN/NfeCancelamento2/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : 'SCAN/NfeInutilizacao2/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : 'SCAN/NfeConsulta2/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : 'SCAN/NfeStatusServico2/NfeStatusServico2.asmx'
        }
}

DPEC = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'     : 'www.nfe.fazenda.gov.br',
        WS_DPEC_CONSULTA: 'SCERecepcaoRFB/SCERecepcaoRFB.asmx',
        WS_DPEC_RECEPCAO: 'SCEConsultaRFB/SCEConsultaRFB.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'     : 'hom.nfe.fazenda.gov.br',
        WS_DPEC_CONSULTA: 'SCERecepcaoRFB/SCERecepcaoRFB.asmx',
        WS_DPEC_RECEPCAO: 'SCEConsultaRFB/SCEConsultaRFB.asmx'
    }
}

#UFAM = {
    #NFE_AMBIENTE_PRODUCAO: {
        #'servidor'            : 'nfe.sefaz.am.gov.br',
        #WS_NFE_ENVIO_LOTE        : 'ws/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO: 'ws/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO    : 'ws/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO    : 'ws/services/NfeInutilizacao',
        #WS_NFE_CONSULTA        : 'ws/services/NfeConsulta',
        #WS_NFE_SITUACAO        : 'ws/services/NfeStatusServico'
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #'servidor'            : 'homnfe.sefaz.am.gov.br',
        #WS_NFE_ENVIO_LOTE        : 'ws/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO: 'ws/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO    : 'ws/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO    : 'ws/services/NfeInutilizacao',
        #WS_NFE_CONSULTA        : 'ws/services/NfeConsulta',
        #WS_NFE_SITUACAO        : 'ws/services/NfeStatusServico'
        #}
#}

UFBA = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : 'nfe.sefaz.ba.gov.br',
        WS_NFE_ENVIO_LOTE       : 'webservices/nfe/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : 'webservices/nfe/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : 'webservices/nfe/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : 'webservices/nfe/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA         : 'webservices/nfe/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : 'webservices/nfe/NfeStatusServico2.asmx',
        #WS_NFE_CONSULTA_CADASTRO: 'webservices/nfe/NfeConsulta2.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'hnfe.sefaz.ba.gov.br',
        WS_NFE_ENVIO_LOTE      : 'webservices/nfenw/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : 'webservices/nfenw/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : 'webservices/nfenw/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : 'webservices/nfenw/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : 'webservices/nfenw/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : 'webservices/nfenw/NfeStatusServico2.asmx'
        }
}

#UFCE = {
    #NFE_AMBIENTE_PRODUCAO: {
        #'servidor'             : 'nfe.sefaz.ce.gov.br',
        #WS_NFE_ENVIO_LOTE         : 'nfe/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : 'nfe/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : 'nfe/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : 'nfe/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : 'nfe/services/NfeConsulta',
        #WS_NFE_SITUACAO         : 'nfe/services/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: 'nfe/services/CadConsultaCadastro'
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #'servidor'             : 'nfeh.sefaz.ce.gov.br',
        #WS_NFE_ENVIO_LOTE         : 'nfe/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : 'nfe/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : 'nfe/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : 'nfe/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : 'nfe/services/NfeConsulta',
        #WS_NFE_SITUACAO         : 'nfe/services/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: 'nfe/services/CadConsultaCadastro'
        #}
#}

#UFDF = {
    #NFE_AMBIENTE_PRODUCAO: {
        #'servidor'             : 'dec.fazenda.df.gov.br',
        #WS_NFE_ENVIO_LOTE         : 'nfe/ServiceRecepcao.asmx',
        #WS_NFE_CONSULTA_RECIBO : 'nfe/ServiceRetRecepcao.asmx',
        #WS_NFE_CANCELAMENTO     : 'nfe/ServiceCancelamento.asmx',
        #WS_NFE_INUTILIZACAO     : 'nfe/ServiceInutilizacao.asmx',
        #WS_NFE_CONSULTA         : 'nfe/ServiceConsulta.asmx',
        #WS_NFE_SITUACAO         : 'nfe/ServiceStatus.asmx',
        #WS_NFE_CONSULTA_CADASTRO: 'nfe/ServiceConsultaCadastro.asmx',
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #'servidor'             : 'homolog.nfe.fazenda.df.gov.br',
        #WS_NFE_ENVIO_LOTE         : 'nfe/ServiceRecepcao.asmx',
        #WS_NFE_CONSULTA_RECIBO : 'nfe/ServiceRetRecepcao.asmx',
        #WS_NFE_CANCELAMENTO     : 'nfe/ServiceCancelamento.asmx',
        #WS_NFE_INUTILIZACAO     : 'nfe/ServiceInutilizacao.asmx',
        #WS_NFE_CONSULTA         : 'nfe/ServiceConsulta.asmx',
        #WS_NFE_SITUACAO         : 'nfe/ServiceStatus.asmx',
        #WS_NFE_CONSULTA_CADASTRO: 'nfe/ServiceConsultaCadastro.asmx'
        #}
#}

UFGO = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : 'nfe.sefaz.go.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe/services/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe/services/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe/services/v2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe/services/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe/services/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe/services/v2/NfeStatusServico2',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'homolog.sefaz.go.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe/services/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe/services/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe/services/v2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe/services/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe/services/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe/services/v2/NfeStatusServico2',
        }
}

UFMT = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : 'nfe.sefaz.mt.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfews/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfews/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfews/v2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfews/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfews/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfews/v2/NfeStatusServico2',
        #WS_NFE_CONSULTA_CADASTRO: 'nfews/CadConsultaCadastro'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'homologacao.sefaz.mt.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfews/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfews/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfews/v2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfews/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfews/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfews/v2/NfeStatusServico2',
        #WS_NFE_CONSULTA_CADASTRO: 'nfews/CadConsultaCadastro'
        }
}

#UFMS = {
    #NFE_AMBIENTE_PRODUCAO: {
        #'servidor'             : 'producao.nfe.ms.gov.br',
        #WS_NFE_ENVIO_LOTE         : 'producao/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : 'producao/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : 'producao/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : 'producao/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : 'producao/services/NfeConsulta',
        #WS_NFE_SITUACAO         : 'producao/services/NfeStatusServico'
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #'servidor'             : 'homologacao.nfe.ms.gov.br',
        #WS_NFE_ENVIO_LOTE         : 'homologacao/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : 'homologacao/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : 'homologacao/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : 'homologacao/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : 'homologacao/services/NfeConsulta',
        #WS_NFE_SITUACAO         : 'homologacao/services/NfeStatusServico'
        #}
#}

UFMG = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : 'nfe.fazenda.mg.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe2/services/NfeStatus2',
        #WS_NFE_CONSULTA_CADASTRO: 'nfe2/services/CadConsultaCadastro'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'hnfe.fazenda.mg.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe2/services/NfeStatus2',
        #WS_NFE_CONSULTA_CADASTRO: 'nfe2/services/CadConsultaCadastro'
        }
}

UFPR = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : 'nfe2.fazenda.pr.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe/NFeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe/NFeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe/NFeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe/NFeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe/NFeConsulta2',
        WS_NFE_SITUACAO         : 'nfe/NFeStatusServico2',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'homologacao.nfe2.fazenda.pr.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe/NFeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe/NFeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe/NFeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe/NFeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe/NFeConsulta2',
        WS_NFE_SITUACAO         : 'nfe/NFeStatusServico2',
    }
}

#UFPE = {
    #NFE_AMBIENTE_PRODUCAO: {
        #'servidor'             : 'nfe.sefaz.pe.gov.br',
        #WS_NFE_ENVIO_LOTE         : 'nfe-service/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : 'nfe-service/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : 'nfe-service/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : 'nfe-service/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : 'nfe-service/services/NfeConsulta',
        #WS_NFE_SITUACAO         : 'nfe-service/services/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: 'nfe-service/services/CadConsultaCadastro'
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #'servidor'             : 'nfehomolog.sefaz.pe.gov.br',
        #WS_NFE_ENVIO_LOTE         : 'nfe-service/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO : 'nfe-service/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO     : 'nfe-service/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : 'nfe-service/services/NfeInutilizacao',
        #WS_NFE_CONSULTA         : 'nfe-service/services/NfeConsulta',
        #WS_NFE_SITUACAO         : 'nfe-service/services/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: 'nfe-service/services/CadConsultaCadastro'
    #}
#}


UFRS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : 'nfe.sefaz.rs.gov.br',
        WS_NFE_ENVIO_LOTE         : 'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : 'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : 'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : 'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA         : 'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : 'ws/nfestatusservico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: 'ws/CadConsultaCadastro/CadConsultaCadastro2.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'homologacao.nfe.sefaz.rs.gov.br',
        WS_NFE_ENVIO_LOTE         : 'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : 'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : 'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : 'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA         : 'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : 'ws/nfestatusservico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: 'ws/CadConsultaCadastro/CadConsultaCadastro2.asmx'
    }
}

#UFRO = {
    #NFE_AMBIENTE_PRODUCAO: {
        #'servidor'             : 'ws.nfe.sefin.ro.gov.br',
        #WS_NFE_ENVIO_LOTE         : SVRS[NFE_AMBIENTE_PRODUCAO][WS_NFE_ENVIO_LOTE],
        #WS_NFE_CONSULTA_RECIBO : SVRS[NFE_AMBIENTE_PRODUCAO][WS_NFE_CONSULTA_RECIBO],
        #WS_NFE_CANCELAMENTO     : 'wsprod/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : SVRS[NFE_AMBIENTE_PRODUCAO][WS_NFE_INUTILIZACAO],
        #WS_NFE_CONSULTA         : 'wsprod/NfeConsulta',
        #WS_NFE_SITUACAO         : 'wsprod/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: 'wsprod/CadConsultaCadastro'
    #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #'servidor'             : 'ws.nfe.sefin.ro.gov.br',
        #WS_NFE_ENVIO_LOTE         : SVRS[NFE_AMBIENTE_HOMOLOGACAO][WS_NFE_ENVIO_LOTE],
        #WS_NFE_CONSULTA_RECIBO : SVRS[NFE_AMBIENTE_HOMOLOGACAO][WS_NFE_CONSULTA_RECIBO],
        #WS_NFE_CANCELAMENTO     : 'ws/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : SVRS[NFE_AMBIENTE_HOMOLOGACAO][WS_NFE_INUTILIZACAO],
        #WS_NFE_CONSULTA         : 'ws/NfeConsulta',
        #WS_NFE_SITUACAO         : 'ws/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: 'ws/CadConsultaCadastro'
    #}
#}

UFSP = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : 'nfe.fazenda.sp.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfeweb/services/nferecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : 'nfeweb/services/nferetrecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : 'nfeweb/services/nfecancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : 'nfeweb/services/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : 'nfeweb/services/nfeconsulta2.asmx',
        WS_NFE_SITUACAO         : 'nfeweb/services/nfestatusservico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: 'nfeweb/services/cadconsultacadastro.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'homologacao.nfe.fazenda.sp.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfeweb/services/nferecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : 'nfeweb/services/nferetrecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : 'nfeweb/services/nfecancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : 'nfeweb/services/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : 'nfeweb/services/nfeconsulta2.asmx',
        WS_NFE_SITUACAO         : 'nfeweb/services/nfestatusservico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: 'nfeWEB/services/cadconsultacadastro.asmx'
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
    'AC': SVRS,
    'AL': SVRS,
    'AM': SVRS,
    'AP': SVRS,
    'BA': UFBA,
    'CE': SVAN,
    'DF': SVRS,
    'ES': SVAN,
    'GO': UFGO,
    'MA': SVAN,
    'MG': UFMG,
    'MS': SVRS,
    #'MT': UFMT,
    'PA': SVAN,
    'PB': SVRS,
    #'PE': UFPE,
    'PI': SVAN,
    'PR': UFPR,
    'RJ': SVRS,
    'RN': SVAN,
    'RO': SVRS,
    'RR': SVRS,
    'RS': UFRS,
    'SC': SVRS,
    'SE': SVRS,
    'SP': UFSP,
    'TO': SVRS
}
