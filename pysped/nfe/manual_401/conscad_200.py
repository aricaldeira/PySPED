# -*- coding: utf-8 -*-

from base import *
from soap_100 import conectar_servico
from soap_200 import SOAPEnvio, SOAPRetorno
import conscad_101


class ConsCad(conscad_101.ConsCad):
    versao = TagDecimal(nome=u'ConsCad', codigo=u'GP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
    caminho_esquema = u'schema/pl_006e/'
    arquivo_esquema = u'consCad_v2.00.xsd'


    def _servico(self):
        envio = SOAPEnvio()
        envio.wsdl = u'CadConsultaCadastro2'
        envio.servico = u'consultaCadastro2'
        envio.nfeCabecMsg.cUF.valor = 35
        envio.nfeCabecMsg.versaoDados.valor = self.versao.valor
        envio.nfeDadosMsg.dados = self
        
        retorno = SOAPRetorno()
        retorno.wsdl = envio.wsdl
        retorno.servico = envio.servico
        self.retorno = RetConsCad()
        retorno.resposta = self.retorno
        
        conectar_servico(envio, retorno, self.certificado, self.senha)


class RetConsCad(conscad_101.RetConsCad):
    versao    = TagDecimal(nome=u'retConsCad', codigo=u'GR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'2.00', raiz=u'/')
    caminho_esquema = u'schema/pl_006e/'
    arquivo_esquema = u'retConsCad_v2.00.xsd'
