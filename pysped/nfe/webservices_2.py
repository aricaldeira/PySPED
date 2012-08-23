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
    },
    WS_NFE_RECEPCAO_ENVENTO: {
        'webservice': 'RecepcaoEvento',
        'metodo'    : 'nfeRecepcaoEvento',
    },
    WS_NFE_DOWNLOAD: {
        'webservice': 'NfeDownloadNF',
        'metodo'    : 'nfeDownloadNF',
    },
    WS_NFE_CONSULTA_DESTINADAS: {
        'webservice': 'NFeConsultaDest',
        'metodo'    : 'nfeConsultaNFDest',
    },
}

SVRS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : 'nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE      : 'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : 'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : 'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : 'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : 'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : 'ws/nfestatusservico/NfeStatusServico2.asmx',
        WS_NFE_RECEPCAO_ENVENTO: 'ws/recepcaoevento/recepcaoevento.asmx',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'homologacao.nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE      : 'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : 'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : 'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : 'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : 'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : 'ws/nfestatusservico/NfeStatusServico2.asmx',
        WS_NFE_RECEPCAO_ENVENTO: 'ws/recepcaoevento/recepcaoevento.asmx',
        }
}

SVAN = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : 'www.sefazvirtual.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : 'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : 'NFeRetRecepcao2/NFeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : 'NFeCancelamento2/NFeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : 'NFeInutilizacao2/NFeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : 'nfeconsulta2/nfeconsulta2.asmx',
        WS_NFE_SITUACAO        : 'NFeStatusServico2/NFeStatusServico2.asmx',
        WS_NFE_RECEPCAO_ENVENTO: 'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_DOWNLOAD        : 'NfeDownloadNF/NfeDownloadNF.asmx',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'hom.sefazvirtual.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : 'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : 'NFeRetRecepcao2/NFeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : 'NFeCancelamento2/NFeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO    : 'NFeInutilizacao2/NFeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : 'nfeconsulta2/nfeconsulta2.asmx',
        WS_NFE_SITUACAO        : 'NFeStatusServico2/NFeStatusServico2.asmx',
        WS_NFE_RECEPCAO_ENVENTO: 'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_DOWNLOAD        : 'NfeDownloadNF/NfeDownloadNF.asmx',
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

AN = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor': 'www.nfe.fazenda.gov.br',
        WS_NFE_RECEPCAO_ENVENTO   : 'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_CONSULTA_DESTINADAS: 'NFeConsultaDest/NFeConsultaDest.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor': 'hom.nfe.fazenda.gov.br',
        WS_NFE_RECEPCAO_ENVENTO   : 'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_CONSULTA_DESTINADAS: 'NFeConsultaDest/NFeConsultaDest.asmx',
    },
}

UFAM = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : 'nfe.sefaz.am.gov.br',
        WS_NFE_ENVIO_LOTE       : 'services2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'services2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'services2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'services2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'services2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'services2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'services2/services/cadconsultacadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'services2/services/RecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'homnfe.sefaz.am.gov.br',
        WS_NFE_ENVIO_LOTE       : 'services2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'services2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'services2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'services2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'services2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'services2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'services2/services/cadconsultacadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'services2/services/RecepcaoEvento',
        }
}

UFBA = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : 'nfe.sefaz.ba.gov.br',
        WS_NFE_ENVIO_LOTE       : 'webservices/nfenw/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : 'webservices/nfenw/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : 'webservices/nfenw/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : 'webservices/nfenw/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA         : 'webservices/nfenw/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : 'webservices/nfenw/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: 'webservices/nfenw/CadConsultaCadastro2.asmx',
        WS_NFE_RECEPCAO_ENVENTO : 'webservices/sre/RecepcaoEvento.asmx',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'hnfe.sefaz.ba.gov.br',
        WS_NFE_ENVIO_LOTE       : 'webservices/nfenw/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : 'webservices/nfenw/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : 'webservices/nfenw/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : 'webservices/nfenw/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA         : 'webservices/nfenw/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : 'webservices/nfenw/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: 'webservices/nfenw/CadConsultaCadastro2.asmx',
        WS_NFE_RECEPCAO_ENVENTO : 'webservices/sre/RecepcaoEvento.asmx',
        }
}

UFCE = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : 'nfe.sefaz.ce.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe2/services/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'nfe2/services/RecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'              : 'nfeh.sefaz.ce.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe2/services/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'nfe2/services/RecepcaoEvento',
        }
}


UFGO = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : 'nfe.sefaz.go.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe/services/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe/services/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe/services/v2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe/services/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe/services/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe/services/v2/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe/services/v2/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'nfe/services/v2/NfeRecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'              : 'homolog.sefaz.go.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe/services/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe/services/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe/services/v2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe/services/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe/services/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe/services/v2/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe/services/v2/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'nfe/services/v2/NfeRecepcaoEvento',
        }
}

UFMT = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : 'nfe.sefaz.mt.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfews/v2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfews/v2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfews/v2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfews/v2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfews/v2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfews/v2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'nfews/CadConsultaCadastro',
        WS_NFE_RECEPCAO_ENVENTO : 'nfews/v2/services/RecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'              : 'homologacao.sefaz.mt.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfews/v2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfews/v2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfews/v2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfews/v2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfews/v2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfews/v2/services/NfeStatusServico2',
        #WS_NFE_CONSULTA_CADASTRO: 'nfews/CadConsultaCadastro',
        WS_NFE_RECEPCAO_ENVENTO : 'nfews/v2/services/RecepcaoEvento',
        }
}

UFMS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : 'nfe.fazenda.ms.gov.br',
        WS_NFE_ENVIO_LOTE       : 'producao/services2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'producao/services2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'producao/services2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'producao/services2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'producao/services2/NfeConsulta2',
        WS_NFE_SITUACAO         : 'producao/services2/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'producao/services2/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'producao/services2/RecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'homologacao.nfe.ms.gov.br',
        WS_NFE_ENVIO_LOTE       : 'homologacao/services2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'homologacao/services2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'homologacao/services2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'homologacao/services2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'homologacao/services2/NfeConsulta2',
        WS_NFE_SITUACAO         : 'homologacao/services2/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'homologacao/services2/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'homologacao/services2/RecepcaoEvento',
        }
}

UFMG = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : 'nfe.fazenda.mg.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe2/services/NfeStatus2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe2/services/cadconsultacadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'nfe2/services/RecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'hnfe.fazenda.mg.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe2/services/NfeStatus2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe2/services/cadconsultacadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'nfe2/services/RecepcaoEvento',
        }
}

UFPR = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : 'nfe2.fazenda.pr.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe/NFeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe/NFeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe/NFeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe/NFeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe/NFeConsulta2',
        WS_NFE_SITUACAO         : 'nfe/NFeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'nfe-evento/NFeRecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'              : 'homologacao.nfe2.fazenda.pr.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe/NFeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe/NFeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe/NFeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe/NFeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe/NFeConsulta2',
        WS_NFE_SITUACAO         : 'nfe/NFeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'nfe-evento/NFeRecepcaoEvento',
    }
}

UFPE = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : 'nfe.sefaz.pe.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe-service/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe-service/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe-service/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe-service/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe-service/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe-service/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe-service/services/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'nfe-service/services/RecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'nfehomolog.sefaz.pe.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfe-service/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : 'nfe-service/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : 'nfe-service/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : 'nfe-service/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe-service/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe-service/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe-service/services/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_ENVENTO : 'nfe-service/services/RecepcaoEvento',
    }
}


UFRS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : 'nfe.sefaz.rs.gov.br',
        WS_NFE_ENVIO_LOTE       : 'ws/Nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : 'ws/NfeRetRecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : 'ws/NfeCancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : 'ws/nfeinutilizacao/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : 'ws/NfeConsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : 'ws/NfeStatusServico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: 'ws/cadconsultacadastro/cadconsultacadastro2.asmx',
        WS_NFE_RECEPCAO_ENVENTO : 'ws/recepcaoevento/recepcaoevento.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'homologacao.nfe.sefaz.rs.gov.br',
        WS_NFE_ENVIO_LOTE       : 'ws/Nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : 'ws/NfeRetRecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : 'ws/NfeCancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : 'ws/nfeinutilizacao/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : 'ws/NfeConsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : 'ws/NfeStatusServico/NfeStatusServico2.asmx',
        #WS_NFE_CONSULTA_CADASTRO: 'ws/cadconsultacadastro/cadconsultacadastro2.asmx',
        WS_NFE_RECEPCAO_ENVENTO : 'ws/recepcaoevento/recepcaoevento.asmx',
    }
}


UFSP = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : 'nfe.fazenda.sp.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfeweb/services/nferecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : 'nfeweb/services/nferetrecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : 'nfeweb/services/nfecancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : 'nfeweb/services/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : 'nfeweb/services/nfeconsulta2.asmx',
        WS_NFE_SITUACAO         : 'nfeweb/services/nfestatusservico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: 'nfeweb/services/cadconsultacadastro2.asmx',
        WS_NFE_RECEPCAO_ENVENTO : 'eventosWEB/services/RecepcaoEvento.asmx',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'homologacao.nfe.fazenda.sp.gov.br',
        WS_NFE_ENVIO_LOTE       : 'nfeweb/services/nferecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : 'nfeweb/services/nferetrecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : 'nfeweb/services/nfecancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : 'nfeweb/services/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : 'nfeweb/services/nfeconsulta2.asmx',
        WS_NFE_SITUACAO         : 'nfeweb/services/nfestatusservico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: 'nfeweb/services/CadConsultaCadastro2.asmx',
        WS_NFE_RECEPCAO_ENVENTO : 'eventosWEB/services/RecepcaoEvento.asmx',
        }
}

#
# Informação obtida em
# http://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=2.00&tipoConteudo=Skeuqr8PQBY=
#  Última verificação: 20/08/2012 14:22
#  * Estados Emissores pela Sefaz Virtual RS (Rio Grande do Sul): AC, AL, AM, AP, DF, MS, PB, RJ, RO, RR, SC, SE e TO.
#  ** Estados Emissores pela Sefaz Virtual AN (Ambiente Nacional): ES, MA, PA, PI e RN.
#


ESTADO_WS = {
    'AC': SVRS,
    'AL': SVRS,
    'AM': UFAM,
    'AP': SVRS,
    'BA': UFBA,
    'CE': UFCE,
    'DF': SVRS,
    'ES': SVAN,
    'GO': UFGO,
    'MA': SVAN,
    'MG': UFMG,
    'MS': SVRS,
    'MT': UFMT,
    'PA': SVAN,
    'PB': SVRS,
    'PE': UFPE,
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
    'TO': SVRS,
}
