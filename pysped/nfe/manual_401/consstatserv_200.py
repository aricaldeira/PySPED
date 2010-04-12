# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.nfe.manual_401 import ESQUEMA_ATUAL
from pysped.nfe.manual_300 import consstatserv_107
import os


DIRNAME = os.path.dirname(__file__)


class ConsStatServ(consstatserv_107.ConsStatServ):
    def __init__(self):
        super(ConsStatServ, self).__init__()
        self.versao = TagDecimal(nome=u'consStatServ', codigo=u'FP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'consStatServ_v2.00.xsd'

class RetConsStatServ(consstatserv_107.RetConsStatServ):
    def __init__(self):
        super(RetConsStatServ, self).__init__()    
        self.versao    = TagDecimal(nome=u'retConsStatServ', codigo=u'FR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retConsStatServ_v2.00.xsd'
