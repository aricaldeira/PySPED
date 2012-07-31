# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from webservices_flags import *


WS_NFSE_ENVIO_LOTE = 0
WS_NFSE_CONSULTA_LOTE = 1
WS_NFSE_CANCELAMENTO = 2
WS_NFSE_CONSULTA_NOTA = 3
WS_NFSE_CONSULTA_NFSERPS = 4
WS_NFSE_CONSULTA_SEQUENCIA_RPS = 5


METODO_WS = {
    WS_NFSE_ENVIO_LOTE: {
        'metodo'    : 'enviar',
    },
    WS_NFSE_CONSULTA_LOTE: {
        'metodo'    : 'consultarLote',
    },
    WS_NFSE_CANCELAMENTO: {
        'metodo'    : 'cancelar',
    },
    WS_NFSE_CONSULTA_NOTA: {
        'metodo'    : 'consultarNota',
    },
    WS_NFSE_CONSULTA_NFSERPS: {
        'metodo'    : 'consultarNFSeRps',
    },
    WS_NFSE_CONSULTA_SEQUENCIA_RPS: {
        'metodo'    : 'consultarSequencialRps',
    }
}


CIDADE_SOROCABA_SP = {
    NFSE_AMBIENTE_HOMOLOGACAO: {
        'servidor': 'treinamento.dsfweb.com.br',
        'url'     : 'WsNFe2/LoteRps.jws'
    },
    NFSE_AMBIENTE_PRODUCAO: {
        'servidor': 'www.issdigitalsod.com.br',
        'url'     : 'WsNFe2/LoteRps.jws'
    }
}


CIDADE_WS = {
    SIAFI_SOROCABA_SP: CIDADE_SOROCABA_SP,
}   
