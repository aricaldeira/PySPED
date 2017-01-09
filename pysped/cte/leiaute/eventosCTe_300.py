# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)

condUso = "A Carta de Correcao e disciplinada pelo Art. 58-B do CONVENIO/SINIEF 06/89: Fica permitida a utilizacao de carta de correcao, para regularizacao de erro ocorrido na emissao de documentos fiscais relativos a prestacao de servico de transporte, desde que o erro nao esteja relacionado com: I - as variaveis que determinam o valor do imposto tais como: base de calculo, aliquota, diferenca de preco, quantidade, valor da prestacao;II - a correcao de dados cadastrais que implique mudanca do emitente, tomador, remetente ou do destinatario;III - a data de emissao ou de saida."


class EvCancCTe(XMLNFe):
    def __init__(self):
        super(EvCancCTe, self).__init__()
        self.descEvento = TagCaracter(nome='descEvento', codigo='EP02' , tamanho=[ 12, 12, 12]   , raiz='//evCancCTe', valor='Cancelamento')
        self.nProt = TagCaracter(nome='nProt', codigo='PE03' , tamanho=[15, 15, 15], raiz='//evCancCTe')
        self.xJust = TagCaracter(nome='xJust'  , codigo='EP04', tamanho=[15, 255]   , raiz='//evCancCTe')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evCancCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evCancCTe>'
        xml += self.descEvento.xml
        xml += self.nProt.xml
        xml += self.xJust.xml
        xml += '</evCancCTe>'

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
        self.Toma   = TagCaracter(nome='Toma', codigo='EP09' , tamanho=[ 1, 1, 1]   , raiz='//Toma4', valor='Cancelamento')
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
        xml += '</Toma4>'

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
        super(EvEPECCTe, self).__init__()
        self.descEvento = TagCaracter(nome='descEvento', codigo='EP02' , tamanho=[ 4, 12]   , raiz='//evEPECCTe', valor='EPEC')
        self.xJust      = TagCaracter(nome='xJust'  , codigo='EP04', tamanho=[15, 255]   , raiz='//evEPECCTe')
        self.vICMS      = TagDecimal(nome='vICMS', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//evEPECCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vTPrest    = TagDecimal(nome='vTPrest', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//evEPECCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.vCarga     = TagDecimal(nome='vCarga', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//evEPECCTe', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.Toma4      = Toma4()
        self.Modal      = TagCaracter(nome='Modal', codigo='EP14' , tamanho=[ 2, 2, 2]   , raiz='//evEPECCTe')
        self.UFIni      = TagCaracter(nome='UFIni', codigo='EP15' , tamanho=[ 2, 2, 2]   , raiz='//evEPECCTe')
        self.UFFIm      = TagCaracter(nome='UFFIm', codigo='EP16' , tamanho=[ 2, 2, 2]   , raiz='//evEPECCTe')
        self.tpCTe      =  TagCaracter(nome='tpCTe', codigo='EP17' , tamanho=[ 4, 12]   , raiz='//evEPECCTe', valor='0')
        self.dhEmi      = TagDataHora(nome='dhEmi', raiz='//evEPECCTe')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evEPECCTe_v3.00.xsd'

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

        xml += '</evEPECCTe>'

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
        self.descEvento = TagCaracter(nome='descEvento', codigo='EP02' , tamanho=[ 4, 19]   , raiz='//evRegMultimodal', valor='Registro Multimodal')
        self.xRegistro  = TagCaracter(nome='xRegistro', codigo='EP03', tamanho=[15, 1000], raiz='//evRegMultimodal')
        self.nDoc       = TagCaracter(nome='nDoc', tamanho=[1, 44], raiz='//evRegMultimodal', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evRegMultimodal_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evRegMultimodal>'
        xml += self.descEvento.xml
        xml += self.xRegistro.xml
        xml += self.nDoc.xml

        xml += '</evRegMultimodal>'

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
        self.grupoAlterado      = TagCaracter(nome='grupoAlterado', tamanho=[ 1, 20]   , raiz='//infCorrecao')
        self.campoAlterado      = TagCaracter(nome='campoAlterado', tamanho=[ 1, 20]   , raiz='//infCorrecao')
        self.valorAlterado      = TagCaracter(nome='valorAlterado', tamanho=[1, 500], raiz='//infCorrecao')
        self.nroItemAlterado    = TagCaracter(nome='nroItemAlterado', tamanho=[1, 4], raiz='//infCorrecao', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCorrecao>'
        xml += self.grupoAlterado.xml
        xml += self.campoAlterado.xml
        xml += self.valorAlterado.xml
        xml += self.nroItemAlterado.xml
        xml += '</infCorrecao>'
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
        self.descEvento = TagCaracter(nome='descEvento', codigo='EP02' , tamanho=[ 5, 60]   , raiz='//evCCeCTe', valor='Carta de Correcao')
        self.infCorrecao = []
        self.xCondUso  = TagCaracter(nome='xCondUso', codigo='EP03', tamanho=[15, 1000], raiz='//evCCeCTe', valor=condUso)
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evCCeCTe_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evCCeCTe>'
        xml += self.descEvento.xml
        for icorr in self.infCorrecao:
            xml += icorr.xml
        xml += self.xCondUso.xml

        xml += '</evCCeCTe>'

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
        self.descEvento = TagCaracter(nome='descEvento', codigo='EP02' , tamanho=[ 33, 33]   , raiz='//evPrestDesacordo', valor='Prestação do Serviço em Desacordo')
        self.indDesacordoOper = TagCaracter(nome='indDesacordoOper', codigo='EP03', tamanho=[1, 1, 1], raiz='//evPrestDesacordo')
        self.xOBS  = TagCaracter(nome='xOBS', codigo='EP04', tamanho=[15, 255], raiz='//evPrestDesacordo', obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evPrestDesacordo_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evPrestDesacordo>'
        xml += self.descEvento.xml
        xml += self.indDesacordoOper.xml
        xml += self.xOBS.xml
        xml += '</evPrestDesacordo>'

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
        self.tpEspecie = TagInteiro(nome='tpEspecie', tamanho=[ 1, 1, 1], raiz='//infEspecie')
        self.vEspecie  = TagDecimal(nome='vEspecie', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz='//infEspecie', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infEspecie>'
        xml += self.tpEspecie.xml
        xml += self.vEspecie.xml

        xml += '</infEspecie>'

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
        xml += '</infGTV>'
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
        self.descEvento = TagCaracter(nome='descEvento', codigo='EP02' , tamanho=[ 18, 18]   , raiz='//evGTV', valor='Informações da GTV')
        self.infGTV = []
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evGTV_v3.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<evGTV>'
        xml += self.descEvento.xml
        for igtv in self.infGTV:
            xml += igtv.xml
        xml += '</evGTV>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.descEvento.xml = arquivo
            self.infGTV = self.le_grupo('//eventoCTe/infEvento/detEvento/evGTV/infGTV', InfGTV, sigla_ns='cte')

    xml = property(get_xml, set_xml)
