# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)

condUso = "A Carta de Correcao e disciplinada pelo Art. 58-B do CONVENIO/SINIEF 06/89: Fica permitida a utilizacao de carta de correcao, para regularizacao de erro ocorrido na emissao de documentos fiscais relativos a prestacao de servico de transporte, desde que o erro nao esteja relacionado com: I - as variaveis que determinam o valor do imposto tais como: base de calculo, aliquota, diferenca de preco, quantidade, valor da prestacao;II - a correcao de dados cadastrais que implique mudanca do emitente, tomador, remetente ou do destinatario;III - a data de emissao ou de saida."


class EvCancCTe(XMLNFe):
    def __init__(self):
        super(EvCancCTe, self).__init__()
        self.descEvento = TagCaracter(nome=u'descEvento', codigo=u'EP02' , tamanho=[ 12, 12, 12]   , raiz=u'//evCancCTe', valor=u'Cancelamento')
        self.nProt = TagCaracter(nome=u'nProt', codigo=u'PE03' , tamanho=[15, 15, 15], raiz=u'//evCancCTe')
        self.xJust = TagCaracter(nome=u'xJust'  , codigo=u'EP04', tamanho=[15, 255]   , raiz=u'//evCancCTe')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'evCancCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evCancCTe>'
        xml += self.descEvento.xml
        xml += self.nProt.xml
        xml += self.xJust.xml
        xml += u'</evCancCTe>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.descEvento.xml = arquivo
            self.nProt.xml      = arquivo
            self.xJust.xml      = arquivo

    xml = property(get_xml, set_xml)
    
    
class Toma4(XMLNFe):
    def __init__(self):
        super(Toma4, self).__init__()
        self.Toma   = TagCaracter(nome=u'Toma', codigo=u'EP09' , tamanho=[ 1, 1, 1]   , raiz=u'//Toma4', valor=u'Cancelamento')
        self.UF     = TagCaracter(nome='UF'   , tamanho=[ 2,  2], raiz='//Toma4')
        self.CNPJ   = TagCaracter(nome='CNPJ' , tamanho=[ 0, 14], raiz='//Toma4', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.CPF    = TagCaracter(nome='CPF'  , tamanho=[11, 11], raiz='//Toma4', obrigatorio=False, namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.IE     = TagCaracter(nome='IE', codigo='EP13', tamanho=[ 2, 14], raiz='//Toma4', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Toma4>'
        xml += self.Toma.xml
        xml += self.UF.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.IE.xml
        xml += u'</Toma4>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Toma.xml = arquivo
            self.UF.xml = arquivo
            self.CNPJ.xml = arquivo
            self.CPF.xml = arquivo
            self.IE.xml = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class EvEPECCTe(XMLNFe):
    def __init__(self):
        super(EvCancCTe, self).__init__()
        self.descEvento = TagCaracter(nome=u'descEvento', codigo=u'EP02' , tamanho=[ 4, 12]   , raiz=u'//evEPECCTe', valor=u'EPEC')
        self.xJust      = TagCaracter(nome=u'xJust'  , codigo=u'EP04', tamanho=[15, 255]   , raiz=u'//evEPECCTe')
        self.vICMS      = TagDecimal(nome='vICMS', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//evEPECCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vTPrest    = TagDecimal(nome='vTPrest', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//evEPECCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vCarga     = TagDecimal(nome='vCarga', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//evEPECCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.Toma4      = Toma4()
        self.Modal      = TagCaracter(nome=u'Modal', codigo=u'EP14' , tamanho=[ 2, 2, 2]   , raiz=u'//evEPECCTe')
        self.UFIni      = TagCaracter(nome=u'UFIni', codigo=u'EP15' , tamanho=[ 2, 2, 2]   , raiz=u'//evEPECCTe')
        self.UFFIm      = TagCaracter(nome=u'UFFIm', codigo=u'EP16' , tamanho=[ 2, 2, 2]   , raiz=u'//evEPECCTe')
        self.tpCTe      =  TagCaracter(nome=u'tpCTe', codigo=u'EP17' , tamanho=[ 4, 12]   , raiz=u'//evEPECCTe', valor=u'0')
        self.dhEmi      = TagDataHora(nome='dhEmi', raiz='//evEPECCTe')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'evEPECCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evEPECCTe>'
        xml += self.descEvento.xml
        xml += self.xJust.xml
        xml += self.vICMS.xml
        xml += self.vTPrest.xml
        xml += self.vCarga.xml
        xml += self.Toma4.xml
        xml += self.Modal.xml
        xml += self.UFIni.xml
        xml += self.UFFIm.xml
        xml += self.tpCTe.xml
        xml += self.dhEmi.xml
        
        xml += u'</evEPECCTe>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.descEvento.xml = arquivo
            self.xJust.xml      = arquivo
            self.vICMS.xml      = arquivo
            self.vTPrest.xml    = arquivo
            self.vCarga.xml     = arquivo
            self.Toma4.xml      = arquivo
            self.Modal.xml      = arquivo
            self.UFIni.xml      = arquivo
            self.UFFIm.xml      = arquivo
            self.tpCTe.xml      = arquivo
            self.dhEmi.xml      = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class EvRegMultimodal(XMLNFe):
    def __init__(self):
        super(EvRegMultimodal, self).__init__()
        self.descEvento = TagCaracter(nome=u'descEvento', codigo=u'EP02' , tamanho=[ 4, 19]   , raiz=u'//evRegMultimodal', valor=u'Registro Multimodal')
        self.xRegistro  = TagCaracter(nome=u'xRegistro', codigo=u'EP03', tamanho=[15, 1000], raiz=u'//evRegMultimodal')
        self.nDoc       = TagCaracter(nome='nDoc', tamanho=[1, 44], raiz='//evRegMultimodal', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'evRegMultimodal_v3.00.xsd'
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evRegMultimodal>'
        xml += self.descEvento.xml
        xml += self.xRegistro.xml
        xml += self.nDoc.xml

        xml += u'</evRegMultimodal>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.descEvento.xml = arquivo
            self.xRegistro.xml  = arquivo
            self.nDoc.xml       = arquivo

    xml = property(get_xml, set_xml)
    
    
class InfCorrecao(XMLNFe):
    def __init__(self):
        super(InfCorrecao, self).__init__()
        self.grupoAlterado      = TagCaracter(nome=u'grupoAlterado', tamanho=[ 1, 20]   , raiz=u'//infCorrecao')
        self.campoAlterado      = TagCaracter(nome=u'campoAlterado', tamanho=[ 1, 20]   , raiz=u'//infCorrecao')
        self.valorAlterado      = TagCaracter(nome=u'valorAlterado', tamanho=[1, 500], raiz=u'//infCorrecao')
        self.nroItemAlterado    = TagCaracter(nome=u'nroItemAlterado', tamanho=[1, 4], raiz=u'//infCorrecao', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCorrecao>'
        xml += self.grupoAlterado.xml
        xml += self.campoAlterado.xml
        xml += self.valorAlterado.xml
        xml += self.nroItemAlterado.xml
        xml += u'</infCorrecao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.grupoAlterado.xml  = arquivo
            self.campoAlterado.xml        = arquivo
            self.valorAlterado.xml       = arquivo
            self.nroItemAlterado.xml       = arquivo

    xml = property(get_xml, set_xml)
    
    
class EvCCeCTe(XMLNFe):
    def __init__(self):
        super(EvCCeCTe, self).__init__()
        self.descEvento = TagCaracter(nome=u'descEvento', codigo=u'EP02' , tamanho=[ 5, 60]   , raiz=u'//evCCeCTe', valor=u'Carta de Correcao')
        self.infCorrecao = []
        self.xCondUso  = TagCaracter(nome=u'xCondUso', codigo=u'EP03', tamanho=[15, 1000], raiz=u'//evCCeCTe', valor=condUso)
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'evCCeCTe_v3.00.xsd'
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evCCeCTe>'
        xml += self.descEvento.xml
        for icorr in self.infCorrecao:
            xml += icorr.xml
        xml += self.xCondUso.xml

        xml += u'</evCCeCTe>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.descEvento.xml = arquivo
            self.infCorrecao = self.le_grupo('//eventoCTe/infEvento/detEvento/evCCeCTe/infCorrecao', InfCorrecao, sigla_ns='cte')
            self.xCondUso.xml       = arquivo

    xml = property(get_xml, set_xml)
    
    
class EvPrestDesacordo(XMLNFe):
    def __init__(self):
        super(EvPrestDesacordo, self).__init__()
        self.descEvento = TagCaracter(nome=u'descEvento', codigo=u'EP02' , tamanho=[ 33, 33]   , raiz=u'//evPrestDesacordo', valor=u'Prestação do Serviço em Desacordo')
        self.indDesacordoOper = TagCaracter(nome=u'indDesacordoOper', codigo=u'EP03', tamanho=[1, 1, 1], raiz=u'//evPrestDesacordo')
        self.xOBS  = TagCaracter(nome=u'xOBS', codigo=u'EP04', tamanho=[15, 255], raiz=u'//evPrestDesacordo', obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'evPrestDesacordo_v3.00.xsd'
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evPrestDesacordo>'
        xml += self.descEvento.xml
        xml += self.indDesacordoOper.xml
        xml += self.xOBS.xml
        xml += u'</evPrestDesacordo>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.descEvento.xml = arquivo
            self.indDesacordoOper.xml = arquivo
            self.xOBS.xml = arquivo

    xml = property(get_xml, set_xml)
    

class DestGTV(XMLNFe):
    def __init__(self):
        super(DestGTV, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , tamanho=[ 0, 14], raiz='//dest', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , tamanho=[11, 11], raiz='//dest', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , tamanho=[ 2, 14], raiz='//dest', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.UF        = TagCaracter(nome='UF'   , tamanho=[ 2,  2], raiz='//dest')
        self.xNome     = TagCaracter(nome='xNome', tamanho=[ 2, 60], raiz='//dest')
        
    def get_xml(self):       
        xml = XMLNFe.get_xml(self)
        xml += '<dest>'
        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml
        xml += self.IE.xml
        xml += self.UF.xml
        xml += self.xNome.xml
        xml += '</dest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CPF.xml  = arquivo
            self.CNPJ.xml  = arquivo
            self.IE.xml  = arquivo
            self.UF.xml  = arquivo
            self.xNome.xml  = arquivo

    xml = property(get_xml, set_xml)
 
 
class RemGTV(XMLNFe):
    def __init__(self):
        super(RemGTV, self).__init__()
        self.CNPJ      = TagCaracter(nome='CNPJ' , tamanho=[ 0, 14], raiz='//rem', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.CPF       = TagCaracter(nome='CPF'  , tamanho=[11, 11], raiz='//rem', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.IE        = TagCaracter(nome='IE'   , tamanho=[ 2, 14], raiz='//rem', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.UF        = TagCaracter(nome='UF'   , tamanho=[ 2,  2], raiz='//rem')
        self.xNome     = TagCaracter(nome='xNome', tamanho=[ 2, 60], raiz='//rem')
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<rem>'
        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml
        xml += self.IE.xml
        xml += self.UF.xml
        xml += self.xNome.xml
        xml += '</rem>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CPF.xml  = arquivo
            self.CNPJ.xml  = arquivo
            self.IE.xml  = arquivo
            self.UF.xml  = arquivo
            self.xNome.xml  = arquivo

    xml = property(get_xml, set_xml)
 
   
class InfEspecie(XMLNFe):
    def __init__(self):
        super(InfEspecie, self).__init__()
        self.tpEspecie = TagInteiro(nome=u'tpEspecie', tamanho=[ 1, 1, 1], raiz=u'//infEspecie')
        self.vEspecie  = TagDecimal(nome='vEspecie', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infEspecie', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infEspecie>'
        xml += self.tpEspecie.xml
        xml += self.vEspecie.xml
        
        xml += u'</infEspecie>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpEspecie.xml = arquivo
            self.vEspecie.xml = arquivo

    xml = property(get_xml, set_xml)
    
    
    
class InfGTV(XMLNFe):
    def __init__(self):
        super(InfGTV, self).__init__()
        self.nDoc       = TagCaracter(nome='nDoc', tamanho=[1, 20], raiz='//infGTV', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.id         = TagCaracter(nome='id', tamanho=[1, 20], raiz='//infGTV', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.serie      = TagCaracter(nome='serie', tamanho=[1, 3], raiz='//infGTV', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.subserie   = TagCaracter(nome='subserie', tamanho=[1, 3], raiz='//infGTV', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.dEmi       = TagData(nome='dEmi', raiz='//infGTV', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.nDV        = TagInteiro(nome='nDV', tamanho=[ 1,  1, 1], raiz='//infGTV')
        self.qCarga     = TagDecimal(nome='qCarga', tamanho=[1, 11, 1], decimais=[0, 4, 4], raiz='//infGTV', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.infEspecie = []
        self.rem        = RemGTV()
        self.dest       = DestGTV()
        self.placa      = TagCaracter(nome='placa', tamanho=[1, 20], raiz='//infGTV', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.UF         = TagCaracter(nome='UF', tamanho=[2, 2], raiz='//infGTV', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.RNTRC      = TagCaracter(nome='RNTRC', tamanho=[1, 20], raiz='//infGTV', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infGTV>'
        xml += self.nDoc.xml
        xml += self.id.xml
        xml += self.serie.xml
        xml += self.subserie.xml
        xml += self.dEmi.xml
        xml += self.nDV.xml
        xml += self.qCarga.xml
        for iesp in self.infEspecie:
            xml += iesp.xml
        xml += self.rem.xml
        xml += self.dest.xml
        xml += self.placa.xml
        xml += self.UF.xml
        xml += self.RNTRC.xml
        xml += u'</infGTV>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nDoc.xml       = arquivo
            self.id.xml         = arquivo
            self.serie.xml      = arquivo
            self.subserie.xml   = arquivo
            self.dEmi.xml       = arquivo
            self.nDV.xml        = arquivo
            self.qCarga.xml     = arquivo
            self.rem.xml        = arquivo
            self.dest.xml       = arquivo
            self.placa.xml      = arquivo
            self.UF.xml         = arquivo
            self.RNTRC.xml      = arquivo
            self.infEspecie = self.le_grupo('//eventoCTe/infEvento/detEvento/evGTV/infGTV/infEspecie', InfEspecie, sigla_ns='cte')

    xml = property(get_xml, set_xml)
    
    
class EvGTV(XMLNFe):
    def __init__(self):
        super(EvGTV, self).__init__()
        self.descEvento = TagCaracter(nome=u'descEvento', codigo=u'EP02' , tamanho=[ 18, 18]   , raiz=u'//evGTV', valor=u'Informações da GTV')
        self.infGTV = []
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'evGTV_v3.00.xsd'
        
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evGTV>'
        xml += self.descEvento.xml
        for igtv in self.infGTV:
            xml += igtv.xml
        xml += u'</evGTV>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.descEvento.xml = arquivo
            self.infGTV = self.le_grupo('//eventoCTe/infEvento/detEvento/evGTV/infGTV', InfGTV, sigla_ns='cte')

    xml = property(get_xml, set_xml)
