#!/usr/bin/python
# -*- coding: utf-8 -*-


if __name__ == u'__main__':
    #
    # Prepara a cadeia certificadora, separando individualmente cada um
    #
    #import pdb; pdb.set_trace()
    arq_tmp = open('cadeia.pem')
    cadeia = u''.join(arq_tmp.readlines())
    arq_tmp.close()
    cadeia_certificados = cadeia.split(u'-----END CERTIFICATE-----')

    #
    # Burramente, temos que salvar cada um num arquivo, para poder ler
    # no xmlsec...
    #
    i = 1
    for certificado in cadeia_certificados:
        if certificado.replace(u'\n', u'').strip() != '':
            certificado = u'-----BEGIN CERTIFICATE-----%s-----END CERTIFICATE-----\n' % certificado.split(u'-----BEGIN CERTIFICATE-----')[1]
            arq_tmp = open('certificados/cert-' + str(i).zfill(2) + '.pem', 'w')
            arq_tmp.write(certificado)
            arq_tmp.close()
            i += 1
