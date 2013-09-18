# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals, absolute_import
import sys
import os


CURDIR = os.path.dirname(os.path.abspath(__file__))


class _Servico(object):
    def __init__(self, codigo='', descricao=''):
        self.codigo = codigo
        self.descricao = descricao

    def __str__(self):
        return unicode.encode(self.__unicode__(), 'utf-8')

    def __unicode__(self):
        return self.codigo + ' - ' + self.descricao

    def __repr__(self):
        return str(self)


def _monta_dicionario_codigo():
    dicionario = {}

    arquivo = open(os.path.join(CURDIR, 'servico.txt'), 'r')

    #
    # Pula a primeira linha
    #
    arquivo.readline()

    for linha in arquivo:
        linha = linha.decode('utf-8').replace('\n', '').replace('\r', '')
        campos = linha.split('|')
        s = _Servico(codigo=campos[0], descricao=campos[1])
        dicionario[s.codigo] = s

        #
        # Normaliza os códigos para terem quatro dígitos quando não for o caso
        #
        if len(s.codigo) < 4:
            dicionario['0' + s.codigo] = s

    return dicionario


if not hasattr(sys.modules[__name__], 'SERVICO_CODIGO'):
    SERVICO_CODIGO = _monta_dicionario_codigo()
