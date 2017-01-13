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

from lxml import etree
from datetime import datetime, date, time
from decimal import Decimal
import locale
import unicodedata
import re
import pytz
from time import strftime


NAMESPACE_NFE = 'http://www.portalfiscal.inf.br/nfe'
NAMESPACE_CTE = 'http://www.portalfiscal.inf.br/cte'
NAMESPACE_SIG = 'http://www.w3.org/2000/09/xmldsig#'
NAMESPACE_NFSE = 'http://localhost:8080/WsNFe2/lote'
ABERTURA = '<?xml version="1.0" encoding="utf-8"?>'

locale.setlocale(locale.LC_ALL, b'pt_BR.UTF-8')
locale.setlocale(locale.LC_COLLATE, b'pt_BR.UTF-8')


class NohXML(object):
    def __init__(self, *args, **kwargs):
        self._xml = None
        self.alertas = []

    def _le_xml(self, arquivo):
        if arquivo is None:
            return False

        if not isinstance(arquivo, basestring):
            arquivo = etree.tounicode(arquivo)
            #self._xml = arquivo
            #return True

        #elif arquivo is not None:
        if arquivo is not None:
            if isinstance(arquivo, basestring):
                if isinstance(arquivo, str):
                    arquivo = unicode(arquivo.encode('utf-8'))

                if '<' in arquivo:
                    self._xml = etree.fromstring(tira_abertura(arquivo).encode('utf-8'))
                else:
                    arq = open(arquivo)
                    txt = b''.join(arq.readlines())
                    txt = unicode(txt.decode('utf-8'))
                    txt = tira_abertura(txt)
                    arq.close()
                    self._xml = etree.fromstring(txt)
            else:
                self._xml = etree.parse(arquivo)
            return True

        return False

    def _preenche_namespace(self, tag, sigla_ns):
        if sigla_ns != '':
            sigla_sig = sigla_ns + ':sig'
            sigla_ns = '/' + sigla_ns + ':'
            tag = sigla_ns.join(tag.split('/')).replace(sigla_ns + sigla_ns, '/' + sigla_ns).replace(sigla_sig, 'sig')

        return tag

    def _le_nohs(self, tag, ns=None, sigla_ns='nfe'):
        #
        # Tenta ler a tag sem os namespaces
        # Necessário para ler corretamente as tags de grupo reenraizadas
        #
        try:
            nohs = self._xml.xpath(tag)
            if len(nohs) >= 1:
                return nohs
        except:
            pass

        #
        # Não deu certo, tem que botar mesmo os namespaces
        #
        namespaces = {'nfe': NAMESPACE_NFE, 'sig': NAMESPACE_SIG, 'nfse': NAMESPACE_NFSE, 'cte': NAMESPACE_CTE}

        if ns is not None:
            namespaces['res'] = ns

        if '//NFe' in tag or ns == NAMESPACE_NFE:
            sigla_ns = 'nfe'
        elif '//CTe' in tag or ns == NAMESPACE_CTE:
            sigla_ns = 'cte'

        if not tag.startswith('//*/res'):
            tag = self._preenche_namespace(tag, sigla_ns)

        nohs = self._xml.xpath(tag, namespaces=namespaces)

        if len(nohs) >= 1:
            return nohs
        else:
            return None

    def _le_noh(self, tag, ns=None, ocorrencia=1):
        nohs = self._le_nohs(tag, ns)

        if (nohs is not None) and (len(nohs) >= ocorrencia):
            return nohs[ocorrencia-1]
        else:
            return None

    def _le_tag(self, tag, propriedade=None, ns=None, ocorrencia=1):
        noh = self._le_noh(tag,  ns, ocorrencia)

        if noh is None:
            valor = ''
        else:
            if propriedade is None:
                valor = noh.text
            elif (noh.attrib is not None) and (len(noh.attrib) > 0):
                valor = noh.attrib[propriedade]
            else:
                valor = ''

        return valor


class ErroObrigatorio(Exception):
    def __init__(self, codigo, nome, propriedade):
        if propriedade:
            self.value = 'No campo código ' + codigo + ', "' + nome + '", a propriedade "' + propriedade + '" é de envio obrigatório, mas não foi preenchida.'
        else:
            self.value = 'O campo código ' + codigo + ', "' + nome + '" é de envio obrigatório, mas não foi preenchido.'

    def __str__(self):
        return repr(self.value)

    def __unicode__(self):
        return unicode(self.value)


class TamanhoInvalido(Exception):
    def __init__(self, codigo, nome, valor, tam_min=None, tam_max=None, dec_min=None, dec_max=None):
        if tam_min:
           self.value = 'O campo código ' + codigo + ', "' + nome + '", deve ter o tamanho mínimo de ' + unicode(tam_min) + ', mas o tamanho enviado foi ' + unicode(len(unicode(valor))) + ': ' + unicode(valor)
        elif tam_max:
           self.value = 'O campo código ' + codigo + ', "' + nome + '", deve ter o tamanho máximo de ' + unicode(tam_max) + ', mas o tamanho enviado foi ' + unicode(len(unicode(valor))) + ': ' + unicode(valor)
        elif dec_min:
           self.value = 'O campo código ' + codigo + ', "' + nome + '", deve ter o mínimo de ' + unicode(dec_min) + ' casas decimais, mas o enviado foi ' + unicode(len(unicode(valor))) + ': ' + unicode(valor)
        elif dec_max:
           self.value = 'O campo código ' + codigo + ', "' + nome + '", deve ter o máximo de ' + unicode(dec_max) + ' casas decimais, mas o enviado foi ' + unicode(len(unicode(valor))) + ': ' + unicode(valor)

    def __str__(self):
        return repr(self.value)

    def __unicode__(self):
        return unicode(self.value)


class ErroCaracterInvalido(Exception):
    def __init__(self, codigo, nome, propriedade, valor, caracter):
        if propriedade:
            self.value = 'No campo código ' + codigo + ', "' + nome + '", a propriedade "' + propriedade + '" possui um caracter inválido: "' + caracter + '".'
        else:
            self.value = 'O campo código ' + codigo + ', "' + nome + '" possui um caracter inválido: "' + caracter + '".'

    def __str__(self):
        return repr(self.value)

    def __unicode__(self):
        return unicode(self.value)


class TagCaracter(NohXML):
    def __init__(self, *args, **kwargs):
        super(TagCaracter, self).__init__(*args, **kwargs)
        self.codigo = ''
        self.nome = ''
        self._valor_string = ''
        self.obrigatorio = True
        self.tamanho = [None, None, None]
        self.propriedade = None
        self.namespace = None
        self.namespace_obrigatorio = True
        self.alertas = []
        self.raiz = None
        self.cdata = False

        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)

        if kwargs.has_key('valor'):
            self.valor = kwargs['valor']

    def _testa_obrigatorio(self, valor):
        if self.obrigatorio and (not valor):
            return ErroObrigatorio(self.codigo, self.nome, self.propriedade)
            #raise ErroObrigatorio(self.codigo, self.nome, self.propriedade)

    def _testa_tamanho_minimo(self, valor):
        if self.tamanho[0] and (len(unicode(valor)) < self.tamanho[0]):
            return TamanhoInvalido(self.codigo, self.nome, valor, tam_min=self.tamanho[0])
            #raise TamanhoInvalido(self.codigo, self.nome, valor, tam_min=self.tamanho[0])

    def _testa_tamanho_maximo(self, valor):
        if self.tamanho[1] and (len(unicode(valor)) > self.tamanho[1]):
            return TamanhoInvalido(self.codigo, self.nome, valor, tam_max=self.tamanho[1])
            #raise TamanhoInvalido(self.codigo, self.nome, valor, tam_max=self.tamanho[1])

    def _valida(self, valor):
        self.alertas = []

        v = valor
        if self.cdata:
            v = valor.replace('<![CDATA[', '')
            v = v.replace(']]>', '')

        if self._testa_obrigatorio(v):
            self.alertas.append(self._testa_obrigatorio(v))

        if self._testa_tamanho_minimo(v):
            self.alertas.append(self._testa_tamanho_minimo(v))

        if self._testa_tamanho_maximo(v):
            self.alertas.append(self._testa_tamanho_maximo(v))

        return self.alertas == []

    def set_valor(self, novo_valor):
        if novo_valor is not None:
            novo_valor = unicode(novo_valor)
            #
            # Remover caratceres inválidos
            #
            for c in novo_valor:
                if c > 'ÿ':
                    raise ErroCaracterInvalido(self.codigo, self.nome, self.propriedade, novo_valor, c)

            #
            # É obrigatório remover os espaços no início e no final do valor
            #
            novo_valor = novo_valor.strip()

        if self._valida(novo_valor):
            if self.cdata:
                self._valor_string = unicode(novo_valor)
            else:
                self._valor_string = unicode(tirar_acentos(novo_valor))
        else:
            self._valor_string = ''

    def get_valor(self):
        return unicode(por_acentos(self._valor_string))

    valor = property(get_valor, set_valor)

    def __unicode__(self):
        if (not self.obrigatorio) and (not self.valor):
            texto = ''
        else:
            texto = '<%s' % self.nome

            if self.namespace and self.namespace_obrigatorio:
                texto += ' xmlns="%s"' % self.namespace

            if self.propriedade:
                texto += ' %s="%s">' % (self.propriedade, self._valor_string)
            elif self.valor or (len(self.tamanho) == 3 and self.tamanho[2]):
                if self.cdata:
                    texto += '><![CDATA[%s]]></%s>' % (self._valor_string, self.nome)
                else:
                    texto += '>%s</%s>' % (self._valor_string, self.nome)
            else:
                texto += ' />'

        return texto

    def __repr__(self):
        return self.__unicode__()

    def get_xml(self):
        return self.__unicode__()

    def set_xml(self, arquivo, ocorrencia=1):
        if self._le_xml(arquivo):
            self.valor = self._le_tag(self.raiz + '/' + self.nome, propriedade=self.propriedade, ns=self.namespace, ocorrencia=ocorrencia)

    xml = property(get_xml, set_xml)

    def get_text(self):
        if self.propriedade:
            return '%s_%s=%s' % (self.nome, self.propriedade, self._valor_string)
        else:
            return '%s=%s' % (self.nome, self._valor_string)

    text = property(get_text)

    def get_txt(self):
        if self.obrigatorio:
            return self._valor_string

        if self.valor:
            return self._valor_string

        return ''

    txt = property(get_txt)


class TagBoolean(TagCaracter):
    def __init__(self, **kwargs):
        super(TagBoolean, self).__init__(**kwargs)
        self._valor_boolean = None
        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)

        if kwargs.has_key('valor'):
            self.valor = kwargs['valor']


    def _testa_obrigatorio(self, valor):
        # No caso da tag booleana, False deve ser tratado como preenchido
        if self.obrigatorio and (valor is None):
            return ErroObrigatorio(self.codigo, self.nome, self.propriedade)

    def _valida(self, valor):
        self.alertas = []

        if self._testa_obrigatorio(valor):
            self.alertas.append(self._testa_obrigatorio(valor))

        return self.alertas == []

    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if novo_valor.lower() == 'true':
                novo_valor = True
            elif novo_valor.lower() == 'false':
                novo_valor = False
            else:
                novo_valor = None

        if isinstance(novo_valor, bool) and self._valida(novo_valor):
            self._valor_boolean = novo_valor

            if novo_valor == None:
                self._valor_string = ''
            elif novo_valor:
                self._valor_string = 'true'
            else:
                self._valor_string = 'false'
        else:
            self._valor_boolean = None
            self._valor_string = ''

    def get_valor(self):
        return self._valor_boolean

    valor = property(get_valor, set_valor)

    def __unicode__(self):
        if (not self.obrigatorio) and (self.valor == None):
            texto = ''
        else:
            texto = '<%s' % self.nome

            if self.namespace:
                texto += ' xmlns="%s"' % self.namespace

            if self.propriedade:
                texto += ' %s="%s">' % (self.propriedade, self._valor_string)
            elif not self.valor == None:
                texto += '>%s</%s>' % (self._valor_string, self.nome)
            else:
                texto += ' />'

        return texto


class TagData(TagCaracter):
    def __init__(self, **kwargs):
        super(TagData, self).__init__(**kwargs)
        self._valor_data = None
        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)

        if kwargs.has_key('valor'):
            self.valor = kwargs['valor']

    def _valida(self, valor):
        self.alertas = []

        if self._testa_obrigatorio(valor):
            self.alertas.append(self._testa_obrigatorio(valor))

        return self.alertas == []

    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if novo_valor:
                novo_valor = datetime.strptime(novo_valor[:10], '%Y-%m-%d')
            else:
                novo_valor = None

        if isinstance(novo_valor, (datetime, date,)) and self._valida(novo_valor):
            self._valor_data = novo_valor
            # Cuidado!!!
            # Aqui não dá pra usar a função strftime pois em alguns
            # casos a data retornada é 01/01/0001 00:00:00
            # e a função strftime só aceita data com anos a partir de 1900
            self._valor_string = '%04d-%02d-%02d' % (self._valor_data.year, self._valor_data.month, self._valor_data.day)
        else:
            self._valor_data = None
            self._valor_string = ''

    def get_valor(self):
        return self._valor_data

    valor = property(get_valor, set_valor)

    @property
    def formato_danfe(self):
        if self._valor_data is None:
            return ''
        else:
            return self._valor_data.strftime('%d/%m/%Y')

class TagHora(TagData):
    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if novo_valor:
                novo_valor = datetime.strptime(novo_valor[:8], '%H:%M:%S')
            else:
                novo_valor = None

        if isinstance(novo_valor, (datetime, time,)) and self._valida(novo_valor):
            self._valor_data = novo_valor
            # Cuidado!!!
            # Aqui não dá pra usar a função strftime pois em alguns
            # casos a data retornada é 01/01/0001 00:00:00
            # e a função strftime só aceita data com anos a partir de 1900
            self._valor_string = '%02d:%02d:%02d' % (self._valor_data.hour, self._valor_data.minute, self._valor_data.second)
        else:
            self._valor_data = None
            self._valor_string = ''

    def get_valor(self):
        return self._valor_data

    valor = property(get_valor, set_valor)

    @property
    def formato_danfe(self):
        if self._valor_data is None:
            return ''
        else:
            return self._valor_data.strftime('%H:%M:%S')


class TagDataHora(TagData):
    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if novo_valor:
                #
                # Força a ignorar os microssegundos enviados pelo webservice
                # de distribuição de DF-e
                #
                if '.' in novo_valor:
                    novo_valor = novo_valor.split('.')[0]

                novo_valor = datetime.strptime(novo_valor, '%Y-%m-%dT%H:%M:%S')
            else:
                novo_valor = None

        if isinstance(novo_valor, datetime) and self._valida(novo_valor):
            self._valor_data = novo_valor
            self._valor_data = self._valor_data.replace(microsecond=0)
            # Cuidado!!!
            # Aqui não dá pra usar a função strftime pois em alguns
            # casos a data retornada é 01/01/0001 00:00:00
            # e a função strftime só aceita data com anos a partir de 1900
            self._valor_string = '%04d-%02d-%02dT%02d:%02d:%02d' % (self._valor_data.year, self._valor_data.month, self._valor_data.day,
                self._valor_data.hour, self._valor_data.minute, self._valor_data.second)
        else:
            self._valor_data = None
            self._valor_string = ''

    def get_valor(self):
        return self._valor_data

    valor = property(get_valor, set_valor)

    @property
    def formato_danfe(self):
        if self._valor_data is None:
            return ''
        else:
            return self._valor_data.strftime('%d/%m/%Y %H:%M:%S')


def fuso_horario_sistema():
    diferenca = int(strftime('%z')) // 100

    if diferenca < 0:
        return pytz.timezone('Etc/GMT+' + str(diferenca * -1))

    if diferenca > 0:
        return pytz.timezone('Etc/GMT-' + str(diferenca))

    return pytz.UTC


class TagDataHoraUTC(TagData):
    def __init__(self, **kwargs):
        super(TagDataHoraUTC, self).__init__(**kwargs)
        #
        # Expressão de validação do formato (vinda do arquivo leiauteSRE_V1.00.xsd
        # Alterada para tornar a informação do fuso horário opcional
        #
        self._validacao = re.compile(r'(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d(-0[1-4]:00)?')
        self._valida_fuso = re.compile(r'.*[-+]0[0-9]:00$')
        self._brasilia = pytz.timezone('America/Sao_Paulo')
        self.fuso_horario = 'America/Sao_Paulo'

    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if self._validacao.match(novo_valor):
                if self._valida_fuso.match(novo_valor):
                    #
                    # Extrai e determina qual o fuso horário informado
                    #
                    self.fuso_horario = novo_valor[19:]
                    novo_valor = novo_valor[:19]

                #
                # Converte a data sem fuso horário para o fuso horário atual
                # Isso é necessário pois a função strptime ignora a informação
                # do fuso horário na string de entrada
                #
                novo_valor = self.fuso_horario.localize(datetime.strptime(novo_valor, '%Y-%m-%dT%H:%M:%S'))
            else:
                novo_valor = None

        if isinstance(novo_valor, datetime) and self._valida(novo_valor):

            if not novo_valor.tzinfo:
                novo_valor = fuso_horario_sistema().localize(novo_valor)
                novo_valor = pytz.UTC.normalize(novo_valor)
                novo_valor = self._brasilia.normalize(novo_valor)

            self._valor_data = novo_valor
            self._valor_data = self._valor_data.replace(microsecond=0)
            try:
                self._valor_data = self.fuso_horario.localize(self._valor_data)
            except:
                pass
            # Cuidado!!!
            # Aqui não dá pra usar a função strftime pois em alguns
            # casos a data retornada é 01/01/0001 00:00:00
            # e a função strftime só aceita data com anos a partir de 1900
            #self._valor_string = '%04d-%02d-%02dT%02d:%02d:%02d' % (self._valor_data.year, self._valor_data.month, self._valor_data.day,
            #    self._valor_data.hour, self._valor_data.minute, self._valor_data.second)

            self._valor_string = self._valor_data.isoformat()
        else:
            self._valor_data = None
            self._valor_string = ''

    def get_valor(self):
        return self._valor_data

    valor = property(get_valor, set_valor)

    def set_fuso_horaro(self, novo_valor):
        if novo_valor in pytz.country_timezones['br']:
            self._fuso_horario = pytz.timezone(novo_valor)

        #
        # Nos valores abaixo, não entendi ainda até agora, mas para o resultado
        # correto é preciso usar GMT+ (mais), não (menos) como seria de se
        # esperar...
        #
        elif novo_valor == '-04:00' or novo_valor == '-0400':
            self._fuso_horario = pytz.timezone('Etc/GMT+4')
        elif novo_valor == '-03:00' or novo_valor == '-0300':
            self._fuso_horario = pytz.timezone('Etc/GMT+3')
        elif novo_valor == '-02:00' or novo_valor == '-0200':
            self._fuso_horario = pytz.timezone('Etc/GMT+2')
        elif novo_valor == '-01:00' or novo_valor == '-0100':
            self._fuso_horario = pytz.timezone('Etc/GMT+1')

    def get_fuso_horario(self):
        return self._fuso_horario

    fuso_horario = property(get_fuso_horario, set_fuso_horaro)

    @property
    def formato_danfe(self):
        if self._valor_data is None:
            return ''
        else:
            valor = self._brasilia.normalize(self._valor_data).strftime('%d/%m/%Y %H:%M:%S %Z (%z)')
            #
            # Troca as siglas:
            # BRT - Brasília Time -> HOB - Horário Oficial de Brasília
            # BRST - Brasília Summer Time -> HVOB - Horário de Verão Oficial de Brasília
            # AMT - Amazon Time -> HOA - Horário Oficial da Amazônia
            # AMST - Amazon Summer Time -> HVOA - Horário de Verão Oficial da Amazônia
            # FNT - Fernando de Noronha Time -> HOFN - Horário Oficial de Fernando de Noronha
            #
            valor = valor.replace('(-0100)', '(-01:00)')
            valor = valor.replace('(-0200)', '(-02:00)')
            valor = valor.replace('(-0300)', '(-03:00)')
            valor = valor.replace('(-0400)', '(-04:00)')
            valor = valor.replace('BRT', 'HOB')
            valor = valor.replace('BRST', 'HVOB')
            valor = valor.replace('AMT', 'HOA')
            valor = valor.replace('AMST', 'HVOA')
            valor = valor.replace('FNT', 'HOFN')
            return valor


class TagInteiro(TagCaracter):
    def __init__(self, **kwargs):
        super(TagInteiro, self).__init__(**kwargs)
        self._valor_inteiro = 0
        self._valor_string = '0'

        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)

        if kwargs.has_key('valor'):
            self.valor = kwargs['valor']

    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if novo_valor:
                novo_valor = int(novo_valor)
            else:
                novo_valor = 0

        if isinstance(novo_valor, (int, long, Decimal)) and self._valida(novo_valor):
            self._valor_inteiro = novo_valor
            self._valor_string = unicode(self._valor_inteiro)

            if (len(self.tamanho) >= 3) and self.tamanho[2] and (len(self._valor_string) < self.tamanho[2]):
                self._valor_string = self._valor_string.rjust(self.tamanho[2], '0')

        else:
            self._valor_inteiro = 0
            self._valor_string = '0'

    def get_valor(self):
        return self._valor_inteiro

    valor = property(get_valor, set_valor)

    @property
    def formato_danfe(self):
        if not (self.obrigatorio or self._valor_inteiro):
            return ''

        return locale.format('%d', self._valor_inteiro, grouping=True)


class TagDecimal(TagCaracter):
    def __init__(self, *args, **kwargs):
        self._valor_decimal = Decimal('0.0')
        self._valor_string = '0.0'
        self.decimais = [None, None, None]
        super(TagDecimal, self).__init__(*args, **kwargs)

        self._valor_decimal = Decimal('0.0')
        self._valor_string = self._formata(self._valor_decimal)
        self.decimais = [None, None, None]

        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)

    def _parte_inteira(self, valor=None):
        if valor is None:
            valor = self._valor_decimal

        valor = unicode(valor).strip()

        if '.' in valor:
            valor = valor.split('.')[0]

        return valor

    def _parte_decimal(self, valor=None):
        if valor is None:
            valor = self._valor_decimal

        valor = unicode(valor).strip()

        if '.' in valor:
            valor = valor.split('.')[1]
        else:
            valor = ''

        return valor

    def _formata(self, valor):
        texto = self._parte_inteira(valor)

        dec = self._parte_decimal(valor)
        if not dec:
            dec = '0'

        # Tamanho mínimo das casas decimais
        if (len(self.decimais) >= 3) and self.decimais[2] and (len(dec) < self.decimais[2]):
            dec = dec.ljust(self.decimais[2], '0')

        texto += '.' + dec
        return texto

    def _testa_decimais_minimo(self, decimal):
        if self.decimais[0] and (len(decimal) < self.decimais[0]):
            #return TamanhoInvalido(self.codigo, self.nome, decimal, dec_min=self.decimais[0])
            raise TamanhoInvalido(self.codigo, self.nome, decimal, dec_min=self.decimais[0])

    def _testa_decimais_maximo(self, decimal):
        if self.decimais[1] and (len(decimal) > self.decimais[1]):
            #return TamanhoInvalido(self.codigo, self.nome, decimal, dec_max=self.decimais[1])
            raise TamanhoInvalido(self.codigo, self.nome, decimal, dec_max=self.decimais[1])

    def _valida(self, valor):
        self.alertas = []

        if self._testa_obrigatorio(valor):
            self.alertas.append(self._testa_obrigatorio(valor))

        inteiro = self._parte_inteira(valor)
        decimal = self._parte_decimal(valor)

        if self._testa_tamanho_minimo(inteiro):
            self.alertas.append(self._testa_tamanho_minimo(inteiro))

        if self._testa_tamanho_maximo(inteiro):
            self.alertas.append(self._testa_tamanho_maximo(inteiro))

        #
        # Analisando as exp.reg. de validação das tags com decimais,
        # parece haver um número máximo de casas decimais, mas as tags
        # podem ser enviadas sem nenhuma casa decimal, então, não
        # há um mínimo de casas decimais
        #
        #if self._testa_decimais_minimo(decimal):
        #    self.alertas.append(self._testa_decimais_minimo(decimal))

        if self._testa_decimais_maximo(decimal):
            self.alertas.append(self._testa_decimais_maximo(decimal))

        return self.alertas == []

    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if novo_valor:
                novo_valor = Decimal(novo_valor)
            else:
                novo_valor = Decimal('0.0')

        if isinstance(novo_valor, (int, long, Decimal)) and self._valida(novo_valor):
            self._valor_decimal = Decimal(novo_valor)
            self._valor_string = self._formata(self._valor_decimal)
        else:
            self._valor_decimal = Decimal('0.0')
            self._valor_string = self._formata(self._valor_decimal)

    def get_valor(self):
        return self._valor_decimal

    valor = property(get_valor, set_valor)

    @property
    def formato_danfe(self):
        if not (self.obrigatorio or self._valor_decimal):
            return ''

        # Tamanho mínimo das casas decimais
        if (len(self.decimais) >= 3) and self.decimais[2]:
            if len(self._parte_decimal()) <= self.decimais[2]:
                formato = '%.' + unicode(self.decimais[2]) + 'f'
            else:
                formato = '%.' + unicode(len(self._parte_decimal())) + 'f'
        else:
            formato = '%.2f'

        return locale.format(formato, self._valor_decimal, grouping=True)

    @property
    def formato_danfce(self):
        if not (self.obrigatorio or self._valor_decimal):
            return ''

        # Tamanho mínimo das casas decimais
        #if (len(self.decimais) >= 3) and self.decimais[2]:
            #if len(self._parte_decimal()) <= self.decimais[2]:
                #formato = '%.' + unicode(self.decimais[2]) + 'f'
            #else:
                #formato = '%.' + unicode(len(self._parte_decimal())) + 'f'
        #else:
        formato = '%.2f'

        return locale.format(formato, self._valor_decimal, grouping=True)


class XMLNFe(NohXML):
    def __init__(self, *args, **kwargs):
        super(XMLNFe, self).__init__(*args, **kwargs)
        self._xml = None
        self.alertas = []
        self.arquivo_esquema = None
        self.caminho_esquema = None

    def get_xml(self):
        self.alertas = []
        return ''

    def validar(self):
        arquivo_esquema = self.caminho_esquema + self.arquivo_esquema

        # Aqui é importante remover a declaração do encoding
        # para evitar erros de conversão unicode para ascii
        xml = tira_abertura(self.xml).encode('utf-8')

        esquema = etree.XMLSchema(etree.parse(arquivo_esquema)) 
        esquema.validate(etree.fromstring(xml))

        namespace = '{http://www.portalfiscal.inf.br/nfe}'
        return "\n".join([x.message.replace(namespace, '') for x in esquema.error_log])

    def le_grupo(self, raiz_grupo, classe_grupo, sigla_ns='nfe'):
        tags = []

        grupos = self._le_nohs(raiz_grupo, sigla_ns=sigla_ns)

        if grupos is not None:
            tags = [classe_grupo() for g in grupos]
            for i in range(len(grupos)):
                tags[i].xml = grupos[i]

        return tags


def tirar_acentos(texto):
    if not texto:
        return texto

    texto = texto.replace('&', '&amp;')
    texto = texto.replace('<', '&lt;')
    texto = texto.replace('>', '&gt;')
    texto = texto.replace('"', '&quot;')
    texto = texto.replace("'", '&apos;')

    #
    # Trocar ENTER e TAB
    #
    texto = texto.replace('\t', ' ')
    texto = texto.replace('\n', '| ')

    # Remove espaços seguidos
    # Nem pergunte...
    while '  ' in texto:
        texto = texto.replace('  ', ' ')

    return texto

def por_acentos(texto):
    if not texto:
        return texto

    texto = texto.replace('&#39;', "'")
    texto = texto.replace('&apos;', "'")
    texto = texto.replace('&quot;', '"')
    texto = texto.replace('&gt;', '>')
    texto = texto.replace('&lt;', '<')
    texto = texto.replace('&amp;', '&')
    texto = texto.replace('&APOS;', "'")
    texto = texto.replace('&QUOT;', '"')
    texto = texto.replace('&GT;', '>')
    texto = texto.replace('&LT;', '<')
    texto = texto.replace('&AMP;', '&')

    return texto

def tira_abertura(texto):
    #aberturas = (
        #'<?xml version="1.0" encoding="utf-8"?>',
        #'<?xml version="1.0" encoding="utf-8" ?>',
        #'<?xml version="1.0" encoding="utf-8" standalone="no"?>',
        #'<?xml version="1.0" encoding="utf-8" standalone="no" ?>',
        #'<?xml version="1.0" encoding="utf-8" standalone="yes"?>',
        #'<?xml version="1.0" encoding="utf-8" standalone="yes" ?>',

        #'<?xml version="1.0" encoding="UTF-8"?>',
        #'<?xml version="1.0" encoding="UTF-8" ?>',
        #'<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        #'<?xml version="1.0" encoding="UTF-8" standalone="no" ?>',
        #'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        #'<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>',

        #"<?xml version='1.0' encoding='utf-8'?>",
        #"<?xml version='1.0' encoding='utf-8' ?>",
        #"<?xml version='1.0' encoding='utf-8' standalone='no'?>",
        #"<?xml version='1.0' encoding='utf-8' standalone='no' ?>",
        #"<?xml version='1.0' encoding='utf-8' standalone='yes'?>",
        #"<?xml version='1.0' encoding='utf-8' standalone='yes' ?>",

        #"<?xml version='1.0' encoding='UTF-8'?>",
        #"<?xml version='1.0' encoding='UTF-8' ?>",
        #"<?xml version='1.0' encoding='UTF-8' standalone='no'?>",
        #"<?xml version='1.0' encoding='UTF-8' standalone='no' ?>",
        #"<?xml version='1.0' encoding='UTF-8' standalone='yes'?>",
        #"<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>",
        #)

    #for a in aberturas:
        #texto = texto.replace(a,  '')

    if '?>' in texto:
        texto = texto.split('?>')[1:]
        texto = ''.join(texto)

    return texto

def _tipo_para_string(valor, tipo, obrigatorio, dec_min):
    if (not obrigatorio) and (not valor):
        return '', ''

    decimais = ''

    # Cuidado!!!
    # Aqui não dá pra usar a função strftime pois em alguns
    # casos a data retornada é 01/01/0001 00:00:00
    # e a função strftime só aceita data com anos a partir de 1900
    if (tipo in ('d', 'h', 'dh')) and isinstance(valor, (datetime, date, time,)):
        valor = formata_datahora(valor, tipo)
    elif (tipo == 'n') and isinstance(valor, (int, long, float, Decimal)):
        if isinstance(valor, (int, long, float)):
            valor = Decimal(unicode(valor))

        valor = unicode(valor).strip()

        if '.' in valor:
            decimais = valor.split('.')[1]

        if dec_min:
            decimais = decimais.ljust(dec_min, '0')

            if '.' in valor:
                valor = valor.split('.')[0]

            valor += '.' + decimais

    return valor, decimais

def _string_para_tipo(valor, tipo):
    if valor == None:
        return valor

    if tipo == 'd':
        valor = datetime.strptime(valor, b'%Y-%m-%d')
    elif tipo == 'h':
        valor = datetime.strptime(valor, b'%H:%M:%S')
    elif tipo == 'dh':
        valor = datetime.strptime(valor, b'%Y-%m-%dT%H:%M:%S')
    elif tipo == 'n':
        valor = Decimal(valor)

    return valor

def formata_datahora(valor, tipo):
    if (tipo == 'd') and isinstance(valor, (datetime, date,)):
        valor = '%04d-%02d-%02d' % (valor.year, valor.month, valor.day)
    elif (tipo == 'h') and isinstance(valor, (datetime, time,)):
        valor = '%02d:%02d:%02d' % (valor.hour, valor.minute, valor.second)
        valor = valor.strftime('%H:%M:%S')
    elif (tipo == 'dh') and isinstance(valor, datetime):
        valor = '%04d-%02d-%02dT%02d:%02d:%02d' % (valor.year, valor.month, valor.day, valor.hour, valor.minute, valor.second)

    return valor

def somente_ascii(funcao):
    '''
    Usado como decorator para a nota fiscal eletrônica de servicos
    '''
    def converter_para_ascii_puro(*args, **kwargs):
        return unicodedata.normalize(b'NFKD', funcao(*args, **kwargs)).encode('ascii', 'ignore')

    return converter_para_ascii_puro

