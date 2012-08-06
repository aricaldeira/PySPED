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

from pysped.xml_sped import *
from pysped.nfse.versao_100 import ESQUEMA_ATUAL
import os
from decimal import Decimal as D
from hashlib import sha1

DIRNAME = os.path.dirname(__file__)


class Item(XMLNFe):
    def __init__(self):
        super(Item, self).__init__()
        self.DiscriminacaoServico = TagCaracter(nome='DiscriminacaoServico', tamanho=[ 1, 80]   , raiz='//Item')
        self.Quantidade           = TagDecimal(nome='Quantidade'           , tamanho=[ 1, 10, 1], decimais=[0, 4, 4], raiz='//Item')
        self.ValorUnitario        = TagDecimal(nome='ValorUnitario'        , tamanho=[ 1, 15, 1], decimais=[0, 4, 4], raiz='//Item')
        self.ValorTotal           = TagDecimal(nome='ValorTotal'           , tamanho=[ 1, 15, 1], decimais=[0, 2, 2], raiz='//Item')
        self.Tributavel           = TagCaracter(nome='Tributavel'          , tamanho=[ 1,  1]   , raiz='//Item', obrigatorio=False)

    @somente_ascii
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Item>'
        xml += self.DiscriminacaoServico.xml
        xml += self.Quantidade.xml
        xml += self.ValorUnitario.xml
        xml += self.ValorTotal.xml
        xml += self.Tributavel.xml
        xml += '</Item>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.DiscriminacaoServico.xml = arquivo
            self.Quantidade.xml           = arquivo
            self.ValorUnitario.xml        = arquivo
            self.ValorTotal.xml           = arquivo
            self.Tributavel.xml           = arquivo

    xml = property(get_xml, set_xml)

    def tributavel_formatado(self):
        if self.Tributavel.valor == 'S':
            return 'SIM'
        else:
            return 'NÃO'


class Deducao(XMLNFe):
    def __init__(self):
        super(Deducao, self).__init__()
        self.DeducaoPor           = TagCaracter(nome='DeducaoPor'         , tamanho=[ 1,  20]   , raiz='//Deducao')
        self.TipoDeducao          = TagCaracter(nome='TipoDeducao'        , tamanho=[ 1, 255]   , raiz='//Deducao')
        self.CPFCNPJReferencia    = TagCaracter(nome='CPFCNPJReferencia'  , tamanho=[11,  14]   , raiz='//Deducao', obrigatorio=False)
        self.NumeroNFReferencia   = TagInteiro(nome='NumeroNFReferencia'  , tamanho=[ 1,  12, 1], raiz='//Deducao', obrigatorio=False)
        self.ValorTotalReferencia = TagDecimal(nome='ValorTotalReferencia', tamanho=[ 1,  15, 1], decimais=[0, 2, 2], raiz='//Deducao', obrigatorio=False)
        self.PercentualDeduzir    = TagDecimal(nome='PercentualDeduzir'   , tamanho=[ 1,   5, 1], decimais=[0, 2, 2], raiz='//Deducao')
        self.ValorDeduzir         = TagDecimal(nome='ValorDeduzir'        , tamanho=[ 1,  15, 1], decimais=[0, 2, 2], raiz='//Deducao')

    @somente_ascii
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Deducao>'
        xml += self.DeducaoPor.xml
        xml += self.TipoDeducao.xml
        xml += self.CPFCNPJReferencia.xml
        xml += self.NumeroNFReferencia.xml
        xml += self.ValorTotalReferencia.xml
        xml += self.PercentualDeduzir.xml
        xml += self.ValorDeduzir.xml
        xml += '</Deducao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.DeducaoPor.xml           = arquivo
            self.TipoDeducao.xml          = arquivo
            self.CPFCNPJReferencia.xml    = arquivo
            self.NumeroNFReferencia.xml   = arquivo
            self.ValorTotalReferencia.xml = arquivo
            self.PercentualDeduzir.xml    = arquivo
            self.ValorDeduzir.xml         = arquivo

    xml = property(get_xml, set_xml)


class RPS(XMLNFe):
    def __init__(self):
        super(RPS, self).__init__()
        self.Id = TagCaracter(nome='RPS', propriedade='Id', raiz=u'//', obrigatorio=False)
        self.Assinatura                  = TagCaracter(nome='Assinatura'                 , tamanho=[ 1, 2000]   , raiz='//RPS')
        self.InscricaoMunicipalPrestador = TagCaracter(nome='InscricaoMunicipalPrestador', tamanho=[ 6,   11]   , raiz='//RPS')
        self.RazaoSocialPrestador        = TagCaracter(nome='RazaoSocialPrestador'       , tamanho=[ 1,  120]   , raiz='//RPS')
        self.TipoRPS                     = TagCaracter(nome='TipoRPS'                    , tamanho=[ 1,   20]   , raiz='//RPS', valor='RPS')
        self.SerieRPS                    = TagCaracter(nome='SerieRPS'                   , tamanho=[ 2,    2]   , raiz='//RPS', valor='NF')
        self.NumeroRPS                   = TagInteiro(nome='NumeroRPS'                   , tamanho=[ 1,   12, 1], raiz='//RPS')
        self.DataEmissaoRPS              = TagDataHora(nome='DataEmissaoRPS'                                    , raiz='//RPS')
        self.SituacaoRPS                 = TagCaracter(nome='SituacaoRPS'                , tamanho=[ 1,    1]   , raiz='//RPS', valor='N')
        self.SerieRPSSubstituido         = TagCaracter(nome='SerieRPSSubstituido'        , tamanho=[ 2,    2]   , raiz='//RPS', obrigatorio=False)
        self.NumeroRPSSubstituido        = TagInteiro(nome='NumeroRPSSubstituido'        , tamanho=[ 1,   12, 1], raiz='//RPS', obrigatorio=False)
        self.NumeroNFSeSubstituida       = TagInteiro(nome='NumeroNFSeSubstituida'       , tamanho=[ 1,   12, 1], raiz='//RPS', obrigatorio=False)
        self.DataEmissaoNFSeSubstituida  = TagData(nome='DataEmissaoNFSeSubstituida'                        , raiz='//RPS', obrigatorio=False)
        self.SeriePrestacao              = TagCaracter(nome='SeriePrestacao'             , tamanho=[ 2,    2]   , raiz='//RPS')
        self.InscricaoMunicipalTomador   = TagCaracter(nome='InscricaoMunicipalTomador'  , tamanho=[ 6,   11]   , raiz='//RPS')
        self.CPFCNPJTomador              = TagCaracter(nome='CPFCNPJTomador'             , tamanho=[11,   14]   , raiz='//RPS')
        self.RazaoSocialTomador          = TagCaracter(nome='RazaoSocialTomador'         , tamanho=[ 1,  120]   , raiz='//RPS')
        self.DocTomadorEstrangeiro       = TagCaracter(nome='DocTomadorEstrangeiro'      , tamanho=[ 0,   20]   , raiz='//RPS', obrigatorio=False)
        self.TipoLogradouroTomador       = TagCaracter(nome='TipoLogradouroTomador'      , tamanho=[ 0,   10]   , raiz='//RPS')
        self.LogradouroTomador           = TagCaracter(nome='LogradouroTomador'          , tamanho=[ 0,   50]   , raiz='//RPS')
        self.NumeroEnderecoTomador       = TagCaracter(nome='NumeroEnderecoTomador'      , tamanho=[ 0,    9]   , raiz='//RPS')
        self.ComplementoEnderecoTomador  = TagCaracter(nome='ComplementoEnderecoTomador' , tamanho=[ 0,   30]   , raiz='//RPS', obrigatorio=False)
        self.TipoBairroTomador           = TagCaracter(nome='TipoBairroTomador'          , tamanho=[ 0,   10]   , raiz='//RPS')
        self.BairroTomador               = TagCaracter(nome='BairroTomador'              , tamanho=[ 0,   50]   , raiz='//RPS')
        self.CidadeTomador               = TagInteiro(nome='CidadeTomador'               , tamanho=[ 1,   10, 1], raiz='//RPS')
        self.CidadeTomadorDescricao      = TagCaracter(nome='CidadeTomadorDescricao'     , tamanho=[ 0,   50]   , raiz='//RPS')
        self.CEPTomador                  = TagCaracter(nome='CEPTomador'                 , tamanho=[ 8,    8]   , raiz='//RPS')
        self.EmailTomador                = TagCaracter(nome='EmailTomador'               , tamanho=[ 0,   60]   , raiz='//RPS')
        self.CodigoAtividade             = TagCaracter(nome='CodigoAtividade'            , tamanho=[ 9,    9]   , raiz='//RPS')
        self.AliquotaAtividade           = TagDecimal(nome='AliquotaAtividade'           , tamanho=[ 1,    5, 1], decimais=[0, 2, 2], raiz='//RPS')
        self.TipoRecolhimento            = TagCaracter(nome='TipoRecolhimento'           , tamanho=[ 1,    1]   , raiz='//RPS')
        self.MunicipioPrestacao          = TagInteiro(nome='MunicipioPrestacao'          , tamanho=[ 1,   10, 1], raiz='//RPS')
        self.MunicipioPrestacaoDescricao = TagCaracter(nome='MunicipioPrestacaoDescricao', tamanho=[ 0,   30]   , raiz='//RPS')
        self.Operacao                    = TagCaracter(nome='Operacao'                   , tamanho=[ 1,    1]   , raiz='//RPS')
        self.Tributacao                  = TagCaracter(nome='Tributacao'                 , tamanho=[ 1,    1]   , raiz='//RPS')
        self.ValorPIS                    = TagDecimal(nome='ValorPIS'                    , tamanho=[ 1,   15, 1], decimais=[0, 2, 2], raiz='//RPS')
        self.ValorCOFINS                 = TagDecimal(nome='ValorCOFINS'                 , tamanho=[ 1,   15, 1], decimais=[0, 2, 2], raiz='//RPS')
        self.ValorINSS                   = TagDecimal(nome='ValorINSS'                   , tamanho=[ 1,   15, 1], decimais=[0, 2, 2], raiz='//RPS')
        self.ValorIR                     = TagDecimal(nome='ValorIR'                     , tamanho=[ 1,   15, 1], decimais=[0, 2, 2], raiz='//RPS')
        self.ValorCSLL                   = TagDecimal(nome='ValorCSLL'                   , tamanho=[ 1,   15, 1], decimais=[0, 2, 2], raiz='//RPS')
        self.AliquotaPIS                 = TagDecimal(nome='AliquotaPIS'                 , tamanho=[ 1,    5, 1], decimais=[0, 2, 2], raiz='//RPS')
        self.AliquotaCOFINS              = TagDecimal(nome='AliquotaCOFINS'              , tamanho=[ 1,    5, 1], decimais=[0, 2, 2], raiz='//RPS')
        self.AliquotaINSS                = TagDecimal(nome='AliquotaINSS'                , tamanho=[ 1,    5, 1], decimais=[0, 2, 2], raiz='//RPS')
        self.AliquotaIR                  = TagDecimal(nome='AliquotaIR'                  , tamanho=[ 1,    5, 1], decimais=[0, 2, 2], raiz='//RPS')
        self.AliquotaCSLL                = TagDecimal(nome='AliquotaCSLL'                , tamanho=[ 1,    5, 1], decimais=[0, 2, 2], raiz='//RPS')
        self.DescricaoRPS                = TagCaracter(nome='DescricaoRPS'               , tamanho=[ 0, 1500]   , raiz='//RPS')
        self.DDDPrestador                = TagInteiro(nome='DDDPrestador'                , tamanho=[ 0,    3, 0], raiz='//RPS')
        self.TelefonePrestador           = TagInteiro(nome='TelefonePrestador'           , tamanho=[ 0,    8, 0], raiz='//RPS')
        self.DDDTomador                  = TagInteiro(nome='DDDTomador'                  , tamanho=[ 0,    3, 0], raiz='//RPS')
        self.TelefoneTomador             = TagInteiro(nome='TelefoneTomador'             , tamanho=[ 0,    8, 0], raiz='//RPS')
        self.MotCancelamento             = TagCaracter(nome='MotCancelamento'            , tamanho=[ 0,   80]   , raiz='//RPS', obrigatorio=False)
        self.CPFCNPJIntermediario        = TagCaracter(nome='CPFCNPJIntermediario'       , tamanho=[11,   14]   , raiz='//RPS', obrigatorio=False)
        self.Deducoes = []
        self.Itens = []

        #
        # Tags usadas somente para a impressão, não fazem parte do XML a ser gerado
        #
        self.ValorTotalRPS = TagDecimal(nome='ValorTotalRPS', tamanho=[ 1,   15, 1], decimais=[0, 2, 2])
        self.ValorDeducoes = TagDecimal(nome='ValorDeducoes', tamanho=[ 1,   15, 1], decimais=[0, 2, 2])
        self.BaseCalculo   = TagDecimal(nome='BaseCalculo'  , tamanho=[ 1,   15, 1], decimais=[0, 2, 2])
        self.ValorISS      = TagDecimal(nome='ValorISS'     , tamanho=[ 1,   15, 1], decimais=[0, 2, 2])
        self.Informacoes   = TagCaracter(nome='Informacoes' , tamanho=[ 0, 5000])
        self.Informacoes.valor = 'Este Recibo Provisório de Serviços - RPS não é válido como documento fiscal. O prestador do serviço, no prazo de até 5 (cinco) dias corridos da emissão deste RPS, deverá substituí-lo por uma Nota Fiscal de Serviços Eletrônica - NFS-e.'


    def gera_assinatura(self):
        '''
        Gera o hash sha1 para a tag Assinatura
        '''
        texto = self.InscricaoMunicipalPrestador.valor.zfill(11)
        texto += self.SerieRPS.valor.ljust(5)
        texto += unicode(self.NumeroRPS.valor).zfill(12)
        texto += self.DataEmissaoRPS.valor.strftime(r'%Y%m%d')
        texto += self.Tributacao.valor.ljust(2)
        texto += self.SituacaoRPS.valor

        if self.TipoRecolhimento.valor == 'A':
            texto += 'N'
        else:
            texto += 'S'

        valor_servicos = D(0)
        base_calculo = D(0)
        valor_deducoes = D(0)

        for s in self.Itens:
            valor_servicos += s.ValorTotal.valor

            if s.Tributavel.valor == 'S':
                base_calculo += s.ValorTotal.valor

        for d in self.Deducoes:
            valor_deducoes += d.ValorDeduzir.valor

        self.ValorTotalRPS.valor = valor_servicos
        self.ValorDeducoes.valor = valor_deducoes
        self.BaseCalculo.valor = base_calculo - valor_deducoes
        self.ValorISS.valor = (self.BaseCalculo.valor * self.AliquotaAtividade.valor / 100).quantize(D('0.01'))

        texto += unicode(((valor_servicos - valor_deducoes) * 100).quantize(1)).zfill(15)
        texto += unicode((valor_deducoes * 100).quantize(1)).zfill(15)
        texto += self.CodigoAtividade.valor.zfill(10)
        texto += self.CPFCNPJTomador.valor.zfill(14)

        print(texto)

        gerador_sha1 = sha1()
        gerador_sha1.update(texto)
        self.Assinatura.valor = gerador_sha1.hexdigest()

    @somente_ascii
    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.valor.strip() == '':
            xml += '<RPS>'
        else:
            xml += self.Id.xml

        if self.Assinatura.valor.strip() == '':
            self.gera_assinatura()

        xml += self.Assinatura.xml
        xml += self.InscricaoMunicipalPrestador.xml
        xml += self.RazaoSocialPrestador.xml
        xml += self.TipoRPS.xml
        xml += self.SerieRPS.xml
        xml += self.NumeroRPS.xml
        xml += self.DataEmissaoRPS.xml
        xml += self.SituacaoRPS.xml
        xml += self.SerieRPSSubstituido.xml
        xml += self.NumeroRPSSubstituido.xml
        xml += self.NumeroNFSeSubstituida.xml
        xml += self.DataEmissaoNFSeSubstituida.xml
        xml += self.SeriePrestacao.xml
        xml += self.InscricaoMunicipalTomador.xml
        xml += self.CPFCNPJTomador.xml
        xml += self.RazaoSocialTomador.xml
        xml += self.DocTomadorEstrangeiro.xml
        xml += self.TipoLogradouroTomador.xml
        xml += self.LogradouroTomador.xml
        xml += self.NumeroEnderecoTomador.xml
        xml += self.ComplementoEnderecoTomador.xml
        xml += self.TipoBairroTomador.xml
        xml += self.BairroTomador.xml
        xml += self.CidadeTomador.xml
        xml += self.CidadeTomadorDescricao.xml
        xml += self.CEPTomador.xml
        xml += self.EmailTomador.xml
        xml += self.CodigoAtividade.xml
        xml += self.AliquotaAtividade.xml
        xml += self.TipoRecolhimento.xml
        xml += self.MunicipioPrestacao.xml
        xml += self.MunicipioPrestacaoDescricao.xml
        xml += self.Operacao.xml
        xml += self.Tributacao.xml
        xml += self.ValorPIS.xml
        xml += self.ValorCOFINS.xml
        xml += self.ValorINSS.xml
        xml += self.ValorIR.xml
        xml += self.ValorCSLL.xml
        xml += self.AliquotaPIS.xml
        xml += self.AliquotaCOFINS.xml
        xml += self.AliquotaINSS.xml
        xml += self.AliquotaIR.xml
        xml += self.AliquotaCSLL.xml
        xml += self.DescricaoRPS.xml
        xml += self.DDDPrestador.xml
        xml += self.TelefonePrestador.xml
        xml += self.DDDTomador.xml
        xml += self.TelefoneTomador.xml
        xml += self.MotCancelamento.xml
        xml += self.CPFCNPJIntermediario.xml

        if len(self.Deducoes):
            xml += '<Deducoes>'

            for d in self.Deducoes:
                xml += d.xml

            xml += '</Deducoes>'

        if len(self.Itens):
            xml += '<Itens>'

            for i in self.Itens:
                xml += i.xml

            xml += '</Itens>'

        xml += '</RPS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml                          = arquivo
            self.Assinatura.xml                  = arquivo
            self.InscricaoMunicipalPrestador.xml = arquivo
            self.RazaoSocialPrestador.xml        = arquivo
            self.TipoRPS.xml                     = arquivo
            self.SerieRPS.xml                    = arquivo
            self.NumeroRPS.xml                   = arquivo
            self.DataEmissaoRPS.xml              = arquivo
            self.SituacaoRPS.xml                 = arquivo
            self.SerieRPSSubstituido.xml         = arquivo
            self.NumeroRPSSubstituido.xml        = arquivo
            self.NumeroNFSeSubstituida.xml       = arquivo
            self.DataEmissaoNFSeSubstituida.xml  = arquivo
            self.SeriePrestacao.xml              = arquivo
            self.InscricaoMunicipalTomador.xml   = arquivo
            self.CPFCNPJTomador.xml              = arquivo
            self.RazaoSocialTomador.xml          = arquivo
            self.DocTomadorEstrangeiro.xml       = arquivo
            self.TipoLogradouroTomador.xml       = arquivo
            self.LogradouroTomador.xml           = arquivo
            self.NumeroEnderecoTomador.xml       = arquivo
            self.ComplementoEnderecoTomador.xml  = arquivo
            self.TipoBairroTomador.xml           = arquivo
            self.BairroTomador.xml               = arquivo
            self.CidadeTomador.xml               = arquivo
            self.CidadeTomadorDescricao.xml      = arquivo
            self.CEPTomador.xml                  = arquivo
            self.EmailTomador.xml                = arquivo
            self.CodigoAtividade.xml             = arquivo
            self.AliquotaAtividade.xml           = arquivo
            self.TipoRecolhimento.xml            = arquivo
            self.MunicipioPrestacao.xml          = arquivo
            self.MunicipioPrestacaoDescricao.xml = arquivo
            self.Operacao.xml                    = arquivo
            self.Tributacao.xml                  = arquivo
            self.ValorPIS.xml                    = arquivo
            self.ValorCOFINS.xml                 = arquivo
            self.ValorINSS.xml                   = arquivo
            self.ValorIR.xml                     = arquivo
            self.ValorCSLL.xml                   = arquivo
            self.AliquotaPIS.xml                 = arquivo
            self.AliquotaCOFINS.xml              = arquivo
            self.AliquotaINSS.xml                = arquivo
            self.AliquotaIR.xml                  = arquivo
            self.AliquotaCSLL.xml                = arquivo
            self.DescricaoRPS.xml                = arquivo
            self.DDDPrestador.xml                = arquivo
            self.TelefonePrestador.xml           = arquivo
            self.DDDTomador.xml                  = arquivo
            self.TelefoneTomador.xml             = arquivo
            self.MotCancelamento.xml             = arquivo
            self.CPFCNPJIntermediario.xml        = arquivo

            deducoes = self._le_nohs('//RPS/Deducoes/Deducao')
            self.Deducoes = []
            if deducoes is not None:
                self.Deducoes = [Deducao() for d in deducoes]
                for i in range(len(deducoes)):
                    self.Deducoes[i].xml = deducoes[i]

            itens = self._le_nohs('//RPS/Itens/Item')
            self.Itens = []
            if itens is not None:
                self.Itens = [Item() for i in itens]
                for i in range(len(itens)):
                    self.Itens[i].xml = itens[i]

    xml = property(get_xml, set_xml)

    #
    # Funções para formatar campos para a impressão do RPS
    #

    def numero_formatado(self):
        num = unicode(self.NumeroRPS.valor).zfill(12)
        num_formatado = '.'.join((num[0:3], num[3:6], num[6:9], num[9:12]))
        return num_formatado

    def _formata_cpf(self, cpf):
        if not len(cpf.strip()):
            return u''

        formatado = cpf[0:3] + u'.' + cpf[3:6] + u'.' + cpf[6:9] + u'-' + cpf[9:11]
        return formatado

    def _formata_cnpj(self, cnpj):
        if not len(cnpj.strip()):
            return u''

        formatado = cnpj[0:2] + u'.' + cnpj[2:5] + u'.' + cnpj[5:8] + u'/' + cnpj[8:12] + u'-' + cnpj[12:14]
        return formatado

    def cnpj_tomador_formatado(self):
        if len(self.CPFCNPJTomador.valor) == 11:
            return self._formata_cpf(self.CPFCNPJTomador.valor)
        else:
            return self._formata_cnpj(self.CPFCNPJTomador.valor)

    def endereco_tomador_formatado(self):
        end = ''

        if len(self.TipoLogradouroTomador.valor.strip()):
            end = self.TipoLogradouroTomador.valor.strip() + ' '

        end += self.LogradouroTomador.valor

        if len(self.NumeroEnderecoTomador.valor.strip()):
            end += ', ' + self.NumeroEnderecoTomador.valor

        if len(self.ComplementoEnderecoTomador.valor.strip()):
            end += ' - ' + self.ComplementoEnderecoTomador.valor

        if len(self.TipoBairroTomador.valor.strip()):
            end += ' - ' + self.TipoBairroTomador.valor + ' ' + self.BairroTomador.valor
        else:
            end += ' - ' + self.BairroTomador.valor

        end += ' - ' + self.CEPTomador.valor[0:5] + '-' + self.CEPTomador.valor[5:]

        return end

    def descricao_formatada(self):
        return self.DescricaoRPS.valor.replace('|', '<br />')

    def informacoes_formatadas(self):
        return self.Informacoes.valor.replace('|', '<br />')

    def _formata_aliquota_federal(self, descricao, aliquota):
        return descricao + ' (' + aliquota.rjust(5) + '%)'

    def aliquota_pis_formatada(self):
        return self._formata_aliquota_federal('PIS', self.AliquotaPIS.formato_danfe())

    def aliquota_cofins_formatada(self):
        return self._formata_aliquota_federal('COFINS', self.AliquotaCOFINS.formato_danfe())

    def aliquota_inss_formatada(self):
        return self._formata_aliquota_federal('INSS', self.AliquotaINSS.formato_danfe())

    def aliquota_ir_formatada(self):
        return self._formata_aliquota_federal('IR', self.AliquotaIR.formato_danfe())

    def aliquota_csll_formatada(self):
        return self._formata_aliquota_federal('CSLL', self.AliquotaCSLL.formato_danfe())


class _Lote(XMLNFe):
    def __init__(self):
        super(_Lote, self).__init__()
        self.Id = TagCaracter(nome='Lote', propriedade=u'Id', raiz=u'//nfse:ReqEnvioLoteRPS')
        self.RPS  = []

    @somente_ascii
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml

        if len(self.RPS):
            for r in self.RPS:
                xml += r.xml

        xml += '</Lote>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml        = arquivo

            rps = self._le_nohs('//nfse:ReqEnvioLoteRPS/Lote/RPS')
            self.RPS = []
            if rps is not None:
                self.RPS = [RPS() for r in rps]
                for i in range(len(rps)):
                    self.RPS[i].xml = rps[i]

    xml = property(get_xml, set_xml)


class _Cabecalho(XMLNFe):
    def __init__(self):
        super(_Cabecalho, self).__init__()
        self.CodCidade            = TagInteiro(nome='CodCidade'            , tamanho=[ 1, 10, 1], raiz='//nfse:ReqEnvioLoteRPS/Cabecalho')
        self.CPFCNPJRemetente     = TagCaracter(nome='CPFCNPJRemetente'    , tamanho=[11, 14]   , raiz='//nfse:ReqEnvioLoteRPS/Cabecalho')
        self.RazaoSocialRemetente = TagCaracter(nome='RazaoSocialRemetente', tamanho=[ 1, 120]  , raiz='//nfse:ReqEnvioLoteRPS/Cabecalho')
        self.transacao            = TagBoolean(nome='transacao'            ,                      raiz='//nfse:ReqEnvioLoteRPS/Cabecalho', valor=True)
        self.dtInicio             = TagData(nome='dtInicio'                ,                      raiz='//nfse:ReqEnvioLoteRPS/Cabecalho')
        self.dtFim                = TagData(nome='dtFim'                   ,                      raiz='//nfse:ReqEnvioLoteRPS/Cabecalho')
        self.QtdRPS               = TagInteiro(nome='QtdRPS'               , tamanho=[ 1, 15, 1], raiz='//nfse:ReqEnvioLoteRPS/Cabecalho')
        self.ValorTotalServicos   = TagDecimal(nome='ValorTotalServicos'   , tamanho=[ 1, 15, 1], decimais=[0, 2, 2], raiz='//nfse:ReqEnvioLoteRPS/Cabecalho')
        self.ValorTotalDeducoes   = TagDecimal(nome='ValorTotalDeducoes'   , tamanho=[ 1, 15, 1], decimais=[0, 2, 2], raiz='//nfse:ReqEnvioLoteRPS/Cabecalho')
        self.Versao               = TagInteiro(nome='Versao'               , tamanho=[ 1,  3, 1], raiz='//nfse:ReqEnvioLoteRPS/Cabecalho', valor=1)
        self.MetodoEnvio          = TagCaracter(nome='MetodoEnvio'         , tamanho=[ 2,  3]   , raiz='//nfse:ReqEnvioLoteRPS/Cabecalho', valor='WS')
        self.VersaoComponente     = TagCaracter(nome='VersaoComponente'    , tamanho=[ 0, 10]   , raiz='//nfse:ReqEnvioLoteRPS/Cabecalho', obrigatorio=False)

    @somente_ascii
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Cabecalho>'
        xml += self.CodCidade.xml
        xml += self.CPFCNPJRemetente.xml
        xml += self.RazaoSocialRemetente.xml
        xml += self.transacao.xml
        xml += self.dtInicio.xml
        xml += self.dtFim.xml
        xml += self.QtdRPS.xml
        xml += self.ValorTotalServicos.xml
        xml += self.ValorTotalDeducoes.xml
        xml += self.Versao.xml
        xml += self.MetodoEnvio.xml
        xml += self.VersaoComponente.xml
        xml += '</Cabecalho>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CodCidade.xml            = arquivo
            self.CPFCNPJRemetente.xml     = arquivo
            self.RazaoSocialRemetente.xml = arquivo
            self.transacao.xml            = arquivo
            self.dtInicio.xml             = arquivo
            self.dtFim.xml                = arquivo
            self.QtdRPS.xml               = arquivo
            self.ValorTotalServicos.xml   = arquivo
            self.ValorTotalDeducoes.xml   = arquivo
            self.Versao.xml               = arquivo
            self.MetodoEnvio.xml          = arquivo
            self.VersaoComponente.xml     = arquivo

    xml = property(get_xml, set_xml)


class ReqEnvioLoteRPS(XMLNFe):
    def __init__(self):
        super(ReqEnvioLoteRPS, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'ReqEnvioLoteRPS.xsd'
        self.Cabecalho = _Cabecalho()
        self.Lote = _Lote()
        self.Signature = Signature()

    def prepara_cabecalho(self):
        '''
        Preenche as tags dos valores totais do cabecalho com o conteúdo real
        dos RPS no lote
        '''
        valor_servicos = D(0)
        valor_deducoes = D(0)

        for r in self.Lote.RPS:
            for s in r.Itens:
                valor_servicos += s.ValorTotal.valor
            for d in r.Deducoes:
                valor_deducoes += d.ValorDeduzir.valor

        self.Cabecalho.QtdRPS.valor = len(self.Lote.RPS)

        if len(self.Lote.RPS):
            self.Cabecalho.dtInicio.valor = self.Lote.RPS[0].DataEmissaoRPS.valor
            self.Cabecalho.dtFim.valor = self.Lote.RPS[-1].DataEmissaoRPS.valor

        self.Cabecalho.ValorTotalServicos.valor = valor_servicos - valor_deducoes
        self.Cabecalho.ValorTotalDeducoes.valor = valor_deducoes

    @somente_ascii
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<nfse:ReqEnvioLoteRPS xmlns:nfse="http://localhost:8080/WsNFe2/lote" xmlns:tipos="http://localhost:8080/WsNFe2/tp" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://localhost:8080/WsNFe2/lote http://localhost:8080/WsNFe2/xsd/ReqEnvioLoteRPS.xsd">'

        if not self.Cabecalho.QtdRPS.valor:
            self.prepara_cabecalho()

        xml += self.Cabecalho.xml
        xml += self.Lote.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.Lote.Id.valor

        xml += self.Signature.xml

        xml += '</nfse:ReqEnvioLoteRPS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Cabecalho.xml = arquivo
            self.Lote.xml = arquivo
            self.Signature.xml = self._le_noh('//nfse:ReqEnvioLoteRPS/sig:Signature')

    xml = property(get_xml, set_xml)
