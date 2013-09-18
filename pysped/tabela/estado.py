# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals, absolute_import
import os
import sys


CURDIR = os.path.dirname(os.path.abspath(__file__))


class _Estado(object):
    def __init__(self, sigla='', nome='', codigo_ibge='', fuso_horario='America/Sao_Paulo',
        codigo_geoip=''):
        self.sigla = sigla
        self.nome = nome
        self.codigo_ibge = codigo_ibge
        self.fuso_horario = fuso_horario
        self.codigo_geoip = codigo_geoip

    def __str__(self):
        return unicode.encode(self.__unicode__(), 'utf-8')

    def __unicode__(self):
        return self.nome + ' - ' + self.sigla + ' - IBGE: ' + self.codigo_ibge

    def __repr__(self):
        return str(self)


def _monta_dicionario_ibge():
    dicionario = {}

    arquivo = open(os.path.join(CURDIR, 'estado.txt'), 'r')

    #
    # Pula a primeira linha
    #
    arquivo.readline()

    for linha in arquivo:
        linha = linha.decode('utf-8').replace('\n', '').replace('\r', '')
        campos = linha.split('|')
        e = _Estado(sigla=campos[0], nome=campos[1], codigo_ibge=campos[2], fuso_horario=campos[3],
            codigo_geoip=campos[4])

        dicionario[e.codigo_ibge] = e

    return dicionario


def _monta_dicionario_sigla():
    dicionario = {}

    for k, v in ESTADO_IBGE.items():
        dicionario[v.sigla] = v

    return dicionario


if not hasattr(sys.modules[__name__], 'ESTADO_IBGE'):
    ESTADO_IBGE = _monta_dicionario_ibge()

if not hasattr(sys.modules[__name__], 'ESTADO_SIGLA'):
    ESTADO_SIGLA = _monta_dicionario_sigla()
