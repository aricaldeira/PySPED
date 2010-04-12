# -*- coding: utf-8 -*-

from pysped.nfe import ProcessadorNFe
from pysped.nfe.webservices_flags import *


if __name__ == '__main__':
    p = ProcessadorNFe()
    p.versao              = u'2.00'
    p.estado              = u'SP'
    p.certificado.arquivo = u'certificado.pfx'
    p.certificado.senha   = u'senha'
    p.salva_arquivos      = True
    p.contingencia_SCAN   = False
    p.caminho = u'' 

    #
    # O retorno de cada webservice é um dicionário
    # estruturado da seguinte maneira:
    # { TIPO_DO_WS_EXECUTADO: {
    #       u'envio'   : InstanciaDaMensagemDeEnvio,
    #       u'resposta': InstanciaDaMensagemDeResposta,
    #       }
    # }
    #
    processo = p.cancelar_nota(chave_nfe=u'35100411111111111111551010000000271123456789',
        protocolo=u'135100018751878',
        justificativa=u'Somente um teste de cancelamento')
    
    print processo[WS_NFE_CANCELAMENTO][u'envio'].xml
    print
    print processo[WS_NFE_CANCELAMENTO][u'resposta'].xml
    
