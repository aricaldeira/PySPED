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
    WS_NFE_INUTILIZACAO: {
        'webservice': 'NFeInutilizacao4',
        'metodo'    : 'nfeInutilizacaoNF2',
    },
    WS_NFE_CONSULTA: {
        'webservice': 'NFeConsultaProtocolo4',
        'metodo'    : 'nfeConsultaNF2',
    },
    WS_NFE_SITUACAO: {
        'webservice': 'NFeStatusServico4',
        'metodo'    : 'nfeStatusServicoNF',
    },
    WS_NFE_CONSULTA_CADASTRO: {
        'webservice': 'CadConsultaCadastro4',
        'metodo'    : 'consultaCadastro2',
    },
    WS_NFE_RECEPCAO_EVENTO: {
        'webservice': 'NFeRecepcaoEvento4',
        'metodo'    : 'nfeRecepcaoEvento',
    },
    WS_NFE_AUTORIZACAO: {
        'webservice': 'NFeAutorizacao4',
        'metodo'    : 'NfeAutorizacao',
    },
    WS_NFE_CONSULTA_AUTORIZACAO: {
        'webservice': 'NFeRetAutorizacao4',
        'metodo'    : 'NfeRetAutorizacao',
    },
    #WS_NFE_DOWNLOAD: {
        #'webservice': 'NfeDownloadNF',
        #'metodo'    : 'nfeDownloadNF',
    #},
    #WS_NFE_CONSULTA_DESTINADAS: {
        #'webservice': 'NfeConsultaDest',
        #'metodo'    : 'nfeConsultaNFDest',
    #},
    WS_DFE_DISTRIBUICAO: {
        'webservice': 'NFeDistribuicaoDFe',
        'metodo'    : 'nfeDistDFeInteresse'
    }
}


SVRS = {
    # o servidor da consulta de cadastro é diferente dos demais...
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.svrs.rs.gov.br',
        'servidor%s' % WS_NFE_CONSULTA_CADASTRO: 'cad.svrs.rs.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NfeConsulta/NfeConsulta4.asmx',
        WS_NFE_SITUACAO            : 'ws/NfeStatusServico/NfeStatusServico4.asmx',
        WS_NFE_CONSULTA_CADASTRO   : 'ws/cadconsultacadastro/cadconsultacadastro4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/recepcaoevento/recepcaoevento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'nfe-homologacao.svrs.rs.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NfeConsulta/NfeConsulta4.asmx',
        WS_NFE_SITUACAO            : 'ws/NfeStatusServico/NfeStatusServico4.asmx',
        WS_NFE_CONSULTA_CADASTRO   : 'ws/cadconsultacadastro/cadconsultacadastro4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/recepcaoevento/recepcaoevento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
    }
}

SVAN = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'www.sefazvirtual.fazenda.gov.br',
        WS_NFE_INUTILIZACAO        : 'NFeInutilizacao4/NFeInutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx',
        WS_NFE_SITUACAO            : 'NFeStatusServico4/NFeStatusServico4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx',
        WS_NFE_AUTORIZACAO         : 'NFeAutorizacao4/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'NFeRetAutorizacao4/NFeRetAutorizacao4.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'hom.sefazvirtual.fazenda.gov.br',
        WS_NFE_INUTILIZACAO        : 'NFeInutilizacao4/NFeInutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx',
        WS_NFE_SITUACAO            : 'NFeStatusServico4/NFeStatusServico4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx',
        WS_NFE_AUTORIZACAO         : 'NFeAutorizacao4/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'NFeRetAutorizacao4/NFeRetAutorizacao4.asmx',
    }
}


SVC_AN = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'www.svc.fazenda.gov.br',
        WS_NFE_CONSULTA            : 'NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx',
        WS_NFE_SITUACAO            : 'NFeStatusServico4/NFeStatusServico4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx',
        WS_NFE_AUTORIZACAO         : 'NFeAutorizacao4/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'NFeRetAutorizacao4/NFeRetAutorizacao4.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'hom.nfe.fazenda.gov.br',
        WS_NFE_CONSULTA            : 'NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx',
        WS_NFE_SITUACAO            : 'NFeStatusServico4/NFeStatusServico4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx',
        WS_NFE_AUTORIZACAO         : 'NFeAutorizacao4/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'NFeRetAutorizacao4/NFeRetAutorizacao4.asmx',
    }
}


SVC_RS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.svrs.rs.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NfeConsulta/NfeConsulta4.asmx',
        WS_NFE_SITUACAO            : 'ws/NfeStatusServico/NfeStatusServico4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/recepcaoevento/recepcaoevento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'nfe-homologacao.svrs.rs.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NfeConsulta/NfeConsulta4.asmx',
        WS_NFE_SITUACAO            : 'ws/NfeStatusServico/NfeStatusServico4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/recepcaoevento/recepcaoevento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
    }
}


DPEC = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'      : 'www.nfe.fazenda.gov.br',
        WS_DPEC_CONSULTA: 'SCERecepcaoRFB/SCERecepcaoRFB.asmx',
        WS_DPEC_RECEPCAO: 'SCEConsultaRFB/SCEConsultaRFB.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'      : 'hom.nfe.fazenda.gov.br',
        WS_DPEC_CONSULTA: 'SCERecepcaoRFB/SCERecepcaoRFB.asmx',
        WS_DPEC_RECEPCAO: 'SCEConsultaRFB/SCEConsultaRFB.asmx'
    }
}


AN = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                : 'www.nfe.fazenda.gov.br',
        'servidor%s' % WS_DFE_DISTRIBUICAO: 'www1.nfe.fazenda.gov.br',
        WS_NFE_RECEPCAO_EVENTO    : 'RecepcaoEvento/RecepcaoEvento.asmx',
        #WS_NFE_CONSULTA_DESTINADAS: 'NFeConsultaDest/NFeConsultaDest.asmx',
        #WS_NFE_DOWNLOAD           : 'NfeDownloadNF/NfeDownloadNF.asmx',
        WS_DFE_DISTRIBUICAO       : 'NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                : 'hom.nfe.fazenda.gov.br',
        WS_NFE_RECEPCAO_EVENTO    : 'RecepcaoEvento/RecepcaoEvento.asmx',
        #WS_NFE_CONSULTA_DESTINADAS: 'NFeConsultaDest/NFeConsultaDest.asmx',
        #WS_NFE_DOWNLOAD           : 'NfeDownloadNF/NfeDownloadNF.asmx',
        WS_DFE_DISTRIBUICAO       : 'NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx',
    },
}


UFAM = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.sefaz.am.gov.br',
        WS_NFE_INUTILIZACAO        : 'services2/services/NfeInutilizacao4',
        WS_NFE_CONSULTA            : 'services2/services/NfeConsulta4',
        WS_NFE_SITUACAO            : 'services2/services/NfeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'services2/services/cadconsultacadastro2',
        WS_NFE_RECEPCAO_EVENTO     : 'services2/services/RecepcaoEvento',
        WS_NFE_AUTORIZACAO         : 'services2/services/NfeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'services2/services/NfeRetAutorizacao4',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homnfe.sefaz.am.gov.br',
        WS_NFE_INUTILIZACAO        : 'services2/services/NfeInutilizacao4',
        WS_NFE_CONSULTA            : 'services2/services/NfeConsulta4',
        WS_NFE_SITUACAO            : 'services2/services/NfeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'services2/services/cadconsultacadastro2',
        WS_NFE_RECEPCAO_EVENTO     : 'services2/services/RecepcaoEvento',
        WS_NFE_AUTORIZACAO         : 'services2/services/NfeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'services2/services/NfeRetAutorizacao4',
    }
}

UFBA = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.sefaz.ba.gov.br',
        WS_NFE_INUTILIZACAO        : 'webservices/NFeInutilizacao4/NFeInutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'webservices/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx',
        WS_NFE_SITUACAO            : 'webservices/NFeStatusServico4/NFeStatusServico4.asmx',
        WS_NFE_CONSULTA_CADASTRO   : 'webservices/CadConsultaCadastro4/CadConsultaCadastro4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'webservices/sre/recepcaoevento.asmx',
        WS_NFE_AUTORIZACAO         : 'webservices/NFeAutorizacao4/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'webservices/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'hnfe.sefaz.ba.gov.br',
        WS_NFE_INUTILIZACAO        : 'webservices/NFeInutilizacao4/NFeInutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'webservices/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx',
        WS_NFE_SITUACAO            : 'webservices/NFeStatusServico4/NFeStatusServico4.asmx',
        WS_NFE_CONSULTA_CADASTRO   : 'webservices/CadConsultaCadastro4/CadConsultaCadastro4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'webservices/sre/recepcaoevento.asmx',
        WS_NFE_AUTORIZACAO         : 'webservices/NFeAutorizacao4/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'webservices/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx',
    }
}

UFCE = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.sefaz.ce.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfe4/services/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfe4/services/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'nfe4/services/NFeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'nfe2/services/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_EVENTO     : 'nfe2/services/RecepcaoEvento',
        WS_NFE_AUTORIZACAO         : 'nfe4/services/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfe4/services/NFeRetAutorizacao4',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'nfeh.sefaz.ce.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfe4/services/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfe4/services/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'nfe4/services/NFeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'nfe2/services/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_EVENTO     : 'nfe2/services/RecepcaoEvento',
        WS_NFE_AUTORIZACAO         : 'nfe4/services/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfe4/services/NFeRetAutorizacao4',
    }
}

UFGO = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.sefaz.go.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfe/services/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfe/services/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'nfe/services/NFeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'nfe/services/CadConsultaCadastro4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfe/services/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfe/services/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfe/services/NFeRetAutorizacao4',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homolog.sefaz.go.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfe/services/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfe/services/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'nfe/services/NFeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'nfe/services/CadConsultaCadastro4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfe/services/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfe/services/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfe/services/NFeRetAutorizacao4',
    }
}

UFMT = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.sefaz.mt.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfews/v2/services/NfeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfews/v2/services/NfeConsulta4',
        WS_NFE_SITUACAO            : 'nfews/v2/services/NfeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'nfews/v2/services/CadConsultaCadastro4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfews/v2/services/RecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfews/v2/services/NfeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfews/v2/services/NfeRetAutorizacao4',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.sefaz.mt.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfews/v2/services/NfeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfews/v2/services/NfeConsulta4',
        WS_NFE_SITUACAO            : 'nfews/v2/services/NfeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'nfews/v2/services/CadConsultaCadastro4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfews/v2/services/RecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfews/v2/services/NfeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfews/v2/services/NfeRetAutorizacao4',
    }
}

UFMS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.fazenda.ms.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'ws/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'ws/NFeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'ws/CadConsultaCadastro4',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'ws/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NFeRetAutorizacao4',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.nfe.ms.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'ws/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'ws/NFeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'ws/CadConsultaCadastro4',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'ws/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NFeRetAutorizacao4',
    }
}

UFMG = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.fazenda.mg.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfe2/services/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfe2/services/NFeConsulta4',
        WS_NFE_SITUACAO            : 'nfe2/services/NFeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'nfe2/services/cadconsultacadastro2',
        WS_NFE_RECEPCAO_EVENTO     : 'nfe2/services/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfe2/services/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfe2/services/NFeRetAutorizacao4',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'hnfe.fazenda.mg.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfe2/services/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfe2/services/NFeConsulta4',
        WS_NFE_SITUACAO            : 'nfe2/services/NFeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'nfe2/services/cadconsultacadastro2',
        WS_NFE_RECEPCAO_EVENTO     : 'nfe2/services/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfe2/services/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfe2/services/NFeRetAutorizacao4',
    }
}

UFPR = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.sefa.pr.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfe/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfe/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'nfe/NFeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'nfe/CadConsultaCadastro4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfe/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfe/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfe/NFeRetAutorizacao4',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.nfe.sefa.pr.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfe/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfe/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'nfe/NFeStatusServico4',
        WS_NFE_CONSULTA_CADASTRO   : 'nfe/CadConsultaCadastro4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfe/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfe/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfe/NFeRetAutorizacao4',
    }
}

UFPE = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : 'nfe.sefaz.pe.gov.br',
        WS_NFE_INUTILIZACAO     : 'nfe-service/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe-service/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe-service/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe-service/services/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_EVENTO  : 'nfe-service/services/RecepcaoEvento',
        WS_NFE_AUTORIZACAO       : 'nfe-service/services/NfeAutorizacao',
        WS_NFE_CONSULTA_AUTORIZACAO  : 'nfe-service/services/NfeRetAutorizacao',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : 'nfehomolog.sefaz.pe.gov.br',
        WS_NFE_INUTILIZACAO     : 'nfe-service/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : 'nfe-service/services/NfeConsulta2',
        WS_NFE_SITUACAO         : 'nfe-service/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: 'nfe-service/services/CadConsultaCadastro2',
        WS_NFE_RECEPCAO_EVENTO  : 'nfe-service/services/RecepcaoEvento',
        WS_NFE_AUTORIZACAO       : 'nfe-service/services/NfeAutorizacao',
        WS_NFE_CONSULTA_AUTORIZACAO  : 'nfe-service/services/NfeRetAutorizacao',
    }
}


UFRS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.sefazrs.rs.gov.br',
        'servidor%s' % WS_NFE_CONSULTA_CADASTRO: 'cad.sefazrs.rs.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NfeConsulta/NfeConsulta4.asmx',
        WS_NFE_SITUACAO            : 'ws/NfeStatusServico/NfeStatusServico4.asmx',
        WS_NFE_CONSULTA_CADASTRO   : 'ws/cadconsultacadastro/cadconsultacadastro4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/recepcaoevento/recepcaoevento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'nfe-homologacao.sefazrs.rs.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NfeConsulta/NfeConsulta4.asmx',
        WS_NFE_SITUACAO            : 'ws/NfeStatusServico/NfeStatusServico4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/recepcaoevento/recepcaoevento4.asmx',
        WS_NFE_CONSULTA_CADASTRO   : 'ws/cadconsultacadastro/cadconsultacadastro4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
    }
}


UFSP = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfe.fazenda.sp.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/nfeconsultaprotocolo4.asmx',
        WS_NFE_SITUACAO            : 'ws/nfestatusservico4.asmx',
        WS_NFE_CONSULTA_CADASTRO   : 'ws/cadconsultacadastro4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/nferecepcaoevento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/nfeautorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/nferetautorizacao4.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.nfe.fazenda.sp.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/nfeconsultaprotocolo4.asmx',
        WS_NFE_SITUACAO            : 'ws/nfestatusservico4.asmx',
        WS_NFE_CONSULTA_CADASTRO   : 'ws/cadconsultacadastro4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/nferecepcaoevento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/nfeautorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/nferetautorizacao4.asmx',
    }
}

#
# Informação obtida em
# http://www.nfe.fazenda.gov.br/portal/webServices.aspx
#  Última verificação: 28/11/2017 16:15
#
# UF que utilizam a SVAN - Sefaz Virtual do Ambiente Nacional: MA, PA
# UF que utilizam a SVRS - Sefaz Virtual do RS:
# - Para serviço de Consulta Cadastro: AC, RN, PB, SC
# - Para demais serviços relacionados com o sistema da NF-e: AC, AL, AP, DF, PB, PI, RJ, RN, RO, RR, SC, SE, TO
# Autorizadores: AM BA CE GO MG MA MS MT PE PR RS SP
#

ESTADO_WS = {
    'AC': SVRS,
    'AL': SVRS,
    'AM': UFAM,
    'AP': SVRS,
    'BA': UFBA,
    'CE': UFCE,
    'DF': SVRS,
    'ES': SVRS,
    'GO': UFGO,
    'MA': SVAN,
    'MG': UFMG,
    'MS': UFMS,
    'MT': UFMT,
    'PA': SVAN,
    'PB': SVRS,
    'PE': UFPE,
    'PI': SVRS,
    'PR': UFPR,
    'RJ': SVRS,
    'RN': SVRS,
    'RO': SVRS,
    'RR': SVRS,
    'RS': UFRS,
    'SC': SVRS,
    'SE': SVRS,
    'SP': UFSP,
    'TO': SVRS,
}


#
# Informação obtida em
# http://www.nfe.fazenda.gov.br/portal/webServices.aspx
#  Última verificação: 15/08/2014 16:22
#
# Autorizadores em contingência:
# - UF que utilizam a SVC-AN - Sefaz Virtual de Contingência Ambiente Nacional: AC, AL, AP, DF, ES, MG, PB, RJ, RN, RO, RR, RS, SC, SE, SP, TO
# - UF que utilizam a SVC-RS - Sefaz Virtual de Contingência Rio Grande do Sul: AM, BA, CE, GO, MA, MS, MT, PA, PE, PI, PR
#

ESTADO_WS_CONTINGENCIA = {
    'AC': SVC_AN,
    'AL': SVC_AN,
    'AM': SVC_RS,
    'AP': SVC_AN,
    'BA': SVC_RS,
    'CE': SVC_RS,
    'DF': SVC_AN,
    'ES': SVC_AN,
    'GO': SVC_RS,
    'MA': SVC_RS,
    'MG': SVC_AN,
    'MS': SVC_RS,
    'MT': SVC_RS,
    'PA': SVC_RS,
    'PB': SVC_AN,
    'PE': SVC_RS,
    'PI': SVC_RS,
    'PR': SVC_RS,
    'RJ': SVC_AN,
    'RN': SVC_AN,
    'RO': SVC_AN,
    'RR': SVC_AN,
    'RS': SVC_AN,
    'SC': SVC_AN,
    'SE': SVC_AN,
    'SP': SVC_AN,
    'TO': SVC_AN,
}
