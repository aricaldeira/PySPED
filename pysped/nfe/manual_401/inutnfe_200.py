# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_401 import ESQUEMA_ATUAL
from pysped.nfe.manual_300 import inutnfe_107
import os


DIRNAME = os.path.dirname(__file__)


class InfInutEnviado(inutnfe_107.InfInutEnviado):
    def __init__(self):
        super(InfInutEnviado, self).__init__()
        self.Id     = TagCaracter(nome=u'infInut', codigo=u'DP03', tamanho=[43, 43] , raiz=u'//inutNFe', propriedade=u'Id')


class InutNFe(inutnfe_107.InutNFe):
    def __init__(self):
        super(InutNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'inutNFe', codigo=u'DP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.infInut = InfInutEnviado()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'inutNFe_v2.00.xsd'
        
        self.chave = u''
    
    def gera_nova_chave(self):
        chave = self.monta_chave()
        
        #
        # Na versão 1.07 da NF-e a chave de inutilização não tem
        # o ano
        #
        # Mas na versão 2.00 tem
        #
        #chave = chave[0:2] + chave[4:]
        
        #
        # Define o Id
        #
        self.infInut.Id.valor = u'ID' + chave


class InfInutRecebido(inutnfe_107.InfInutRecebido):
    def __init__(self):
        super(InfInutRecebido, self).__init__()

    
class RetInutNFe(inutnfe_107.RetInutNFe):
    def __init__(self):
        super(RetInutNFe, self).__init__()
        self.versao = TagDecimal(nome=u'retInutNFe', codigo=u'DR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.infInut = InfInutRecebido()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retInutNFe_v2.00.xsd'


class ProcInutNFe(inutnfe_107.ProcInutNFe):
    def __init__(self):
        super(ProcInutNFe, self).__init__()
        #
        # Atenção --- a tag ProcInutNFe tem que começar com letra maiúscula, para
        # poder validar no XSD. Os outros arquivos proc, procCancNFe, e procNFe
        # começam com minúscula mesmo
        #
        self.versao = TagDecimal(nome=u'ProcInutNFe', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.inutNFe = InutNFe()
        self.retInutNFe = RetInutNFe()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'procInutNFe_v2.00.xsd'
