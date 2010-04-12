# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_401 import ESQUEMA_ATUAL
from pysped.nfe.manual_300 import cancnfe_107
import os


DIRNAME = os.path.dirname(__file__)


class InfCancEnviado(cancnfe_107.InfCancEnviado):
    def __init__(self):
        super(InfCancEnviado, self).__init__()


class CancNFe(cancnfe_107.CancNFe):
    def __init__(self):
        super(CancNFe, self).__init__()
        self.versao    = TagDecimal(nome=u'cancNFe', codigo=u'CP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.infCanc   = InfCancEnviado()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/') 
        self.arquivo_esquema = u'cancNFe_v2.00.xsd'


class InfCancRecebido(cancnfe_107.InfCancRecebido):
    def __init__(self):
        super(InfCancRecebido, self).__init__()

    
class RetCancNFe(cancnfe_107.RetCancNFe):
    def __init__(self):
        super(RetCancNFe, self).__init__()
        self.versao = TagDecimal(nome=u'retCancNFe', codigo=u'CR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.infCanc = InfCancRecebido()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retCancNFe_v2.00.xsd'


class ProcCancNFe(cancnfe_107.ProcCancNFe):
    def __init__(self):
        super(ProcCancNFe, self).__init__()
        #
        # Atenção --- a tag procCancNFe tem que começar com letra minúscula, para
        # poder validar no XSD.
        #
        self.versao = TagDecimal(nome=u'procCancNFe', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.cancNFe = CancNFe()
        self.retCancNFe = RetCancNFe()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'procCancNFe_v2.00.xsd'
