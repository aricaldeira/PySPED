#!/usr/bin/python
# -*- coding: utf-8 -*-


import libxml2
import xmlsec
import os

DIRNAME = os.path.dirname(__file__)


if __name__ == u'__main__':
    certificados = os.listdir(DIRNAME + 'certificados')
    certificados.sort()  # ?????

    # Ativa as funções da API de criptografia
    xmlsec.init()
    xmlsec.cryptoAppInit(None)
    xmlsec.cryptoInit()

    #
    # Prepara o gerenciador dos certificados confiáveis
    #
    certificados_confiaveis = xmlsec.KeysMngr()
    xmlsec.cryptoAppDefaultKeysMngrInit(certificados_confiaveis)

    for certificado in certificados:
        certificados_confiaveis.certLoad(filename=str(DIRNAME + 'certificados/' + certificado), format=xmlsec.KeyDataFormatPem, type=xmlsec.KeyDataTypeTrusted)

    xmlsec.cryptoShutdown()
    xmlsec.cryptoAppShutdown()
    xmlsec.shutdown()
