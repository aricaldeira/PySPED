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
    processo = p.inutilizar_nota(cnpj=u'11111111111111',
        serie=u'101',
        numero_inicial=18,
        justificativa=u'Testando a inutilização de NF-e')
    
    print processo[WS_NFE_INUTILIZACAO][u'envio'].xml
    print
    print processo[WS_NFE_INUTILIZACAO][u'resposta'].xml
    
    #
    # Inutilizar uma faixa de numeração
    #
    processo = p.inutilizar_nota(cnpj=u'11111111111111',
        serie=u'101',
        numero_inicial=18,
        numero_final=28,
        justificativa=u'Testando a inutilização de NF-e')
    
    print processo[WS_NFE_INUTILIZACAO][u'envio'].xml
    print
    print processo[WS_NFE_INUTILIZACAO][u'resposta'].xml
