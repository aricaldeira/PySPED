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

from os.path import abspath, dirname
from datetime import datetime
from pysped.nfe import ProcessadorNFe
from pysped.nfe.webservices_flags import *
from pysped.nfe.leiaute import *


FILE_DIR = abspath(dirname(__file__))


if __name__ == '__main__':
    p = ProcessadorNFe()
    p.versao              = '1.10'
    p.estado              = 'SP'
    #p.certificado.arquivo = 'certificado.pfx'
    #p.certificado.senha   = 'senha'

    #
    # arquivo 'certificado_caminho.txt' deve conter o caminho para o 'certificado.pfx'
    #
    p.certificado.arquivo = open(FILE_DIR+'/certificado_caminho.txt').read().strip()

    #
    # arquivo 'certificado_senha.txt' deve conter a senha para o 'certificado.pfx'
    #
    p.certificado.senha   = open(FILE_DIR+'/certificado_senha.txt').read().strip()

    p.salva_arquivos      = True
    p.contingencia_SCAN   = False
    p.caminho = ''

    #
    # Instancia uma NF-e
    #
    n = NFe_110()

    #
    # Identificação da NF-e
    #
    n.infNFe.ide.cUF.valor     = UF_CODIGO['SP']
    n.infNFe.ide.natOp.valor   = 'Venda de produto do estabelecimento'
    n.infNFe.ide.indPag.valor  = 2
    n.infNFe.ide.serie.valor   = 101
    n.infNFe.ide.nNF.valor     = 27
    n.infNFe.ide.dEmi.valor    = datetime(2010, 4, 12)
    n.infNFe.ide.dSaiEnt.valor = datetime(2010, 4, 12)
    n.infNFe.ide.cMunFG.valor  = 3513801
    n.infNFe.ide.tpImp.valor   = 1
    n.infNFe.ide.tpEmis.valor  = 1
    n.infNFe.ide.indPag.valor  = 1
    n.infNFe.ide.finNFe.valor  = 1
    n.infNFe.ide.procEmi.valor = 0
    n.infNFe.ide.verProc.valor = 'PySPED NF-e'

    #
    # Emitente
    #
    n.infNFe.emit.CNPJ.valor  = '11111111111111'
    n.infNFe.emit.xNome.valor = 'Razão Social Ltda. EPP'
    n.infNFe.emit.xFant.valor = 'Nome Fantasia'
    n.infNFe.emit.enderEmit.xLgr.valor    = 'Al. Kenworthy'
    n.infNFe.emit.enderEmit.nro.valor     = '140'
    n.infNFe.emit.enderEmit.xCpl.valor    = ''
    n.infNFe.emit.enderEmit.xBairro.valor = 'Jd. Santa Rosália'
    n.infNFe.emit.enderEmit.cMun.valor    = '3552205'
    n.infNFe.emit.enderEmit.xMun.valor    = 'Sorocaba'
    n.infNFe.emit.enderEmit.UF.valor      = 'SP'
    n.infNFe.emit.enderEmit.CEP.valor     = '18095360'
    #n.infNFe.emit.enderEmit.cPais.valor   = '1058'
    #n.infNFe.emit.enderEmit.xPais.valor   = 'Brasil'
    n.infNFe.emit.enderEmit.fone.valor    = '1534110602'
    n.infNFe.emit.IE.valor = '111111111111'

    #
    # Destinatário
    #
    n.infNFe.dest.CNPJ.valor  = '11111111111111'
    n.infNFe.dest.xNome.valor = 'Razão Social Ltda. EPP'
    n.infNFe.dest.enderDest.xLgr.valor    = 'Al. Kenworthy'
    n.infNFe.dest.enderDest.nro.valor     = '140'
    n.infNFe.dest.enderDest.xCpl.valor    = ''
    n.infNFe.dest.enderDest.xBairro.valor = 'Jd. Santa Rosália'
    n.infNFe.dest.enderDest.cMun.valor    = '3552205'
    n.infNFe.dest.enderDest.xMun.valor    = 'Sorocaba'
    n.infNFe.dest.enderDest.UF.valor      = 'SP'
    n.infNFe.dest.enderDest.CEP.valor     = '18095360'
    #n.infNFe.dest.enderDest.cPais.valor   = '1058'
    #n.infNFe.dest.enderDest.xPais.valor   = 'Brasil'
    n.infNFe.dest.enderDest.fone.valor    = '1534110602'
    n.infNFe.dest.IE.valor = '111111111111'

    #
    # Detalhe
    #
    d1 = Det_110()

    d1.nItem.valor = 1
    d1.prod.cProd.valor    = 'código do produto'
    d1.prod.cEAN.valor     = ''
    d1.prod.xProd.valor    = 'Descrição do produto'
    d1.prod.NCM.valor      = ''
    d1.prod.EXTIPI.valor   = ''
    d1.prod.genero.valor   = ''
    d1.prod.CFOP.valor     = '5101'
    d1.prod.uCom.valor     = 'UN'
    d1.prod.qCom.valor     = '100.00'
    d1.prod.vUnCom.valor   = '10.0000'
    d1.prod.vProd.valor    = '1000.00'
    d1.prod.cEANTrib.valor = ''
    d1.prod.uTrib.valor    = d1.prod.uCom.valor
    d1.prod.qTrib.valor    = d1.prod.qCom.valor
    d1.prod.vUnTrib.valor  = d1.prod.vUnCom.valor
    d1.prod.vFrete.valor   = '0.00'
    d1.prod.vSeg.valor     = '0.00'
    d1.prod.vDesc.valor    = '0.00'

    #
    # Impostos
    #
    d1.imposto.ICMS.CST.valor   = '00'
    d1.imposto.ICMS.modBC.valor = 3
    d1.imposto.ICMS.vBC.valor   = '1000.00'
    d1.imposto.ICMS.pICMS.valor = '18.00'
    d1.imposto.ICMS.vICMS.valor = '180.00'

    d1.imposto.IPI.CST.valor    = '50'
    d1.imposto.IPI.vBC.valor    = '1000.00'
    d1.imposto.IPI.pIPI.valor   = '10.00'
    d1.imposto.IPI.vIPI.valor   = '100.00'

    d1.imposto.PIS.CST.valor    = '01'
    d1.imposto.PIS.vBC.valor    = '1000.00'
    d1.imposto.PIS.pPIS.valor   = '0.65'
    d1.imposto.PIS.vPIS.valor   = '6.50'

    d1.imposto.COFINS.CST.valor    = '01'
    d1.imposto.COFINS.vBC.valor    = '1000.00'
    d1.imposto.COFINS.pCOFINS.valor   = '3.00'
    d1.imposto.COFINS.vCOFINS.valor   = '30.00'

    #
    # Os primeiros 188 caracteres desta string
    # são todos os caracteres válidos em tags da NF-e
    #
    d1.infAdProd.valor = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿À'

    #
    # Inclui o detalhe na NF-e
    #
    n.infNFe.det.append(d1)

    #
    # Totais
    #
    n.infNFe.total.ICMSTot.vBC.valor     = '1000.00'
    n.infNFe.total.ICMSTot.vICMS.valor   = '180.00'
    n.infNFe.total.ICMSTot.vBCST.valor   = '0.00'
    n.infNFe.total.ICMSTot.vST.valor     = '0.00'
    n.infNFe.total.ICMSTot.vProd.valor   = '1000.00'
    n.infNFe.total.ICMSTot.vFrete.valor  = '0.00'
    n.infNFe.total.ICMSTot.vSeg.valor    = '0.00'
    n.infNFe.total.ICMSTot.vDesc.valor   = '0.00'
    n.infNFe.total.ICMSTot.vII.valor     = '0.00'
    n.infNFe.total.ICMSTot.vIPI.valor    = '100.00'
    n.infNFe.total.ICMSTot.vPIS.valor    = '6.50'
    n.infNFe.total.ICMSTot.vCOFINS.valor = '30.00'
    n.infNFe.total.ICMSTot.vOutro.valor  = '0.00'
    n.infNFe.total.ICMSTot.vNF.valor     = '1100.00'
    n.gera_nova_chave()

    #
    # O retorno de cada webservice é um objeto
    # com as seguintes propriedades
    #  .webservice - o webservice que foi consultado
    #  .envio - o objeto da classe XMLNFE enviado
    #  .envio.original - o texto do xml (envelope SOAP) enviado ao webservice
    #  .resposta - o objeto da classe XMLNFE retornado
    #  .resposta.version - version da HTTPResponse
    #  .resposta.status - status da HTTPResponse
    #  .resposta.reason - reason da HTTPResponse
    #  .resposta.msg - msg da HTTPResponse
    #  .resposta.original - o texto do xml (SOAP) recebido do webservice
    #
    for processo in p.processar_notas([n]):
        print(processo)
        print()
        print(processo.envio.xml)
        print()
        print(processo.envio.original)
        print()
        print(processo.resposta.xml)
        print()
        print(processo.resposta.original)
        print()
        print(processo.resposta.reason)

        #
        # A consulta dos recibos também retorna dois dicionários, cujas chaves
        # são as chaves das NF-es enviadas;
        #    . dic_protNFe - dicionário com os protocolos de cada NF-e
        #    . dic_procNFe - dicionário com os processos (NF-e + protocolo) de cada NF-e
        #    cada procNFe tem ainda uma propriedade:
        #        .danfe_pdf - conteúdo binário do DANFE em PDF
        #
        if processo.webservice == WS_NFE_CONSULTA_RECIBO:
            print()
            print(processo.resposta.dic_protNFe)
            print()
            print(processo.resposta.dic_procNFe)

