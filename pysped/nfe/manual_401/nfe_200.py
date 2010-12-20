# -*- coding: utf-8 -*-

from pysped.xml_sped import *
#from soap_100 import SOAPEnvio, SOAPRetorno, conectar_servico
from pysped.nfe.manual_401 import ESQUEMA_ATUAL
from pysped.nfe.manual_300 import nfe_110
import os
from lxml.etree import tounicode

DIRNAME = os.path.dirname(__file__)


class Deduc(XMLNFe):
    def __init__(self):
        super(Deduc, self).__init__()
        self.xDed = TagCaracter(nome=u'xDed', codigo=u'ZC11', tamanho=[1, 60]                       , raiz=u'//deduc')
        self.vDed = TagDecimal(nome=u'vDed' , codigo=u'ZC12', tamanho=[1, 15, 1], decimais=[1, 2, 2], raiz=u'//deduc')

    def get_xml(self):
        if not (self.xDed.valor or self.vDed.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<deduc>'
        xml += self.xDed.xml
        xml += self.vDed.xml
        xml += u'</deduc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xDed.xml = arquivo
            self.vDed.xml = arquivo

    xml = property(get_xml, set_xml)


class ForDia(XMLNFe):
    def __init__(self):
        super(ForDia, self).__init__()
        self.dia  = TagInteiro(nome=u'dia' , codigo=u'ZC05', tamanho=[1,  2, 1]                      , raiz=u'//forDia')
        self.qtde = TagDecimal(nome=u'qtde', codigo=u'ZC06', tamanho=[1, 11, 1], decimais=[1, 10, 10], raiz=u'//forDia')

    def get_xml(self):
        if not (self.dia.valor or self.qtde.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<forDia>'
        xml += self.dia.xml
        xml += self.qtde.xml
        xml += u'</forDia>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dia.xml  = arquivo
            self.qtde.xml = arquivo

    xml = property(get_xml, set_xml)


class Cana(XMLNFe):
    def __init__(self):
        super(Cana, self).__init__()
        self.safra   = TagCaracter(nome=u'safra' , codigo=u'ZC02', tamanho=[4,  9]                         , raiz=u'//NFe/infNFe/cana')
        self.ref     = TagCaracter(nome=u'ref'   , codigo=u'ZC03', tamanho=[6,  6]                         , raiz=u'//NFe/infNFe/cana')
        self.forDia  = []
        self.qTotMes = TagDecimal(nome=u'qTotMes', codigo=u'ZC07', tamanho=[1, 11, 1], decimais=[1, 10, 10], raiz=u'//NFe/infNFe/cana')
        self.qTotAnt = TagDecimal(nome=u'qTotAnt', codigo=u'ZC08', tamanho=[1, 11, 1], decimais=[1, 10, 10], raiz=u'//NFe/infNFe/cana')
        self.qTotGer = TagDecimal(nome=u'qTotGer', codigo=u'ZC09', tamanho=[1, 11, 1], decimais=[1, 10, 10], raiz=u'//NFe/infNFe/cana')
        self.deduc   = []
        self.vFor    = TagDecimal(nome=u'vFor'   , codigo=u'ZC13', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz=u'//NFe/infNFe/cana')
        self.vTotDed = TagDecimal(nome=u'vTotDed', codigo=u'ZC14', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz=u'//NFe/infNFe/cana')
        self.vLiqFor = TagDecimal(nome=u'vLiqFor', codigo=u'ZC15', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz=u'//NFe/infNFe/cana')

    def get_xml(self):
        if not (self.safra.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<cana>'
        xml += self.safra.xml
        xml += self.ref.xml

        for fd in self.forDia:
            xml += fd.xml

        xml += self.qTotMes.xml
        xml += self.qTotAnt.xml
        xml += self.qTotGer.xml

        for d in self.deduc:
            xml += d.xml

        xml += self.vFor.xml
        xml += self.vTotDed.xml
        xml += self.vLiqFor.xml
        xml += u'</cana>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.safra.xml   = arquivo
            self.ref.xml     = arquivo
            self.forDia      = self.le_grupo(u'//NFe/infNFe/cana/forDia', ForDia)
            self.qTotMes.xml = arquivo
            self.qTotAnt.xml = arquivo
            self.qTotGer.xml = arquivo
            self.deduc       = self.le_grupo(u'//NFe/infNFe/cana/deduc', Deduc)
            self.vFor.xml    = arquivo
            self.vTotDed.xml = arquivo
            self.vLiqFor.xml = arquivo

    xml = property(get_xml, set_xml)


class ISSQN(nfe_110.ISSQN):
    def __init__(self):
        super(ISSQN, self).__init__()
        self.cSitTrib  = TagCaracter(nome=u'cSitTrib', codigo=u'U07', tamanho=[1,  1], raiz=u'//det/imposto/ISSQN')

    def get_xml(self):
        if not (self.cSitTrib.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<ISSQN>'
        xml += self.vBC.xml
        xml += self.vAliq.xml
        xml += self.vISSQN.xml
        xml += self.cMunFG.xml
        xml += self.cListServ.xml
        xml += self.cSitTrib.xml
        xml += u'</ISSQN>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml       = arquivo
            self.vAliq.xml     = arquivo
            self.vISSQN.xml    = arquivo
            self.cMunFG.xml    = arquivo
            self.cListServ.xml = arquivo
            self.cSitTrib.xml  = arquivo

    xml = property(get_xml, set_xml)


class COFINSST(nfe_110.COFINSST):
    def __init__(self):
        super(COFINSST, self).__init__()


class TagCSTCOFINS(nfe_110.TagCSTCOFINS):
    def __init__(self, *args, **kwargs):
        super(TagCSTCOFINS, self).__init__(*args, **kwargs)


class COFINS(nfe_110.COFINS):
    def __init__(self):
        super(COFINS, self).__init__()


class PISST(nfe_110.PISST):
    def __init__(self):
        super(PISST, self).__init__()


class TagCSTPIS(nfe_110.TagCSTPIS):
    def __init__(self, *args, **kwargs):
        super(TagCSTPIS, self).__init__(*args, **kwargs)


class PIS(nfe_110.PIS):
    def __init__(self):
        super(PIS, self).__init__()


class II(nfe_110.II):
    def __init__(self):
        super(II, self).__init__()


class TagCSTIPI(nfe_110.TagCSTIPI):
    def __init__(self, *args, **kwargs):
        super(TagCSTIPI, self).__init__(*args, **kwargs)


class IPI(nfe_110.IPI):
    def __init__(self):
        super(IPI, self).__init__()


class TagCSOSN(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagCSOSN, self).__init__(*args, **kwargs)
        self.nome = u'CSOSN'
        self.codigo = u'N12a'
        self.tamanho = [3, 3]
        self.raiz = u''
        self.grupo_icms = None

    def set_valor(self, novo_valor):
        super(TagCSOSN, self).set_valor(novo_valor)

        if not self.grupo_icms:
            return None

        #
        # Definimos todas as tags como não obrigatórias
        #
        self.grupo_icms.modBC.obrigatorio       = False
        self.grupo_icms.vBC.obrigatorio         = False
        self.grupo_icms.pRedBC.obrigatorio      = False
        self.grupo_icms.pICMS.obrigatorio       = False
        self.grupo_icms.vICMS.obrigatorio       = False
        self.grupo_icms.modBCST.obrigatorio     = False
        self.grupo_icms.pMVAST.obrigatorio      = False
        self.grupo_icms.pRedBCST.obrigatorio    = False
        self.grupo_icms.vBCST.obrigatorio       = False
        self.grupo_icms.pICMSST.obrigatorio     = False
        self.grupo_icms.vICMSST.obrigatorio     = False
        self.grupo_icms.vBCSTRet.obrigatorio    = False
        self.grupo_icms.vICMSSTRet.obrigatorio  = False
        self.grupo_icms.pCredSN.obrigatorio     = False
        self.grupo_icms.vCredICMSSN.obrigatorio = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo ICMS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_icms.modBC.valor       = 3
        self.grupo_icms.vBC.valor         = u'0.00'
        self.grupo_icms.pRedBC.valor      = u'0.00'
        self.grupo_icms.pICMS.valor       = u'0.00'
        self.grupo_icms.vICMS.valor       = u'0.00'
        self.grupo_icms.modBCST.valor     = 4
        self.grupo_icms.pMVAST.valor      = u'0.00'
        self.grupo_icms.pRedBCST.valor    = u'0.00'
        self.grupo_icms.vBCST.valor       = u'0.00'
        self.grupo_icms.pICMSST.valor     = u'0.00'
        self.grupo_icms.vICMSST.valor     = u'0.00'
        self.grupo_icms.vBCSTRet.valor    = u'0.00'
        self.grupo_icms.vICMSSTRet.valor  = u'0.00'
        self.grupo_icms.pCredSN.valor     = u'0.00'
        self.grupo_icms.vCredICMSSN.valor = u'0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de ICMS
        #
        # Definimos também o valor da tag CST do ICMS
        # tradicional para mapear os novos valores
        # na impressão do DANFE
        #
        # Mapeamento de acordo com a Nota Técnica 2009.004
        #
        #
        # Usamos a propriedade privada, para evitar
        # o processamento do set_valor da classe TagCSTICMS
        #
        if self.valor == u'101':
            self.grupo_icms.nome_tag = u'ICMSSN101'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSSN101'
            self.grupo_icms.pCredSN.obrigatorio     = True
            self.grupo_icms.vCredICMSSN.obrigatorio = True
            self.grupo_icms.CST._valor_string       = u'41'

        elif self.valor in (u'102', u'103', u'300', u'400'):
            self.grupo_icms.nome_tag = u'ICMSSN102'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSSN102'
            self.grupo_icms.CST._valor_string       = u'41'

        elif self.valor == u'201':
            self.grupo_icms.nome_tag = u'ICMSSN201'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSSN201'
            self.grupo_icms.modBCST.obrigatorio     = True
            self.grupo_icms.vBCST.obrigatorio       = True
            self.grupo_icms.pICMSST.obrigatorio     = True
            self.grupo_icms.vICMSST.obrigatorio     = True
            self.grupo_icms.pCredSN.obrigatorio     = True
            self.grupo_icms.vCredICMSSN.obrigatorio = True
            self.grupo_icms.CST._valor_string       = u'30'

        elif self.valor in (u'202', u'203'):
            self.grupo_icms.nome_tag = u'ICMSSN202'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSSN202'
            self.grupo_icms.modBCST.obrigatorio     = True
            self.grupo_icms.vBCST.obrigatorio       = True
            self.grupo_icms.pICMSST.obrigatorio     = True
            self.grupo_icms.vICMSST.obrigatorio     = True
            self.grupo_icms.CST._valor_string       = u'30'

        elif self.valor == u'500':
            self.grupo_icms.nome_tag = u'ICMSSN500'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSSN500'
            self.grupo_icms.vBCSTRet.obrigatorio    = True
            self.grupo_icms.vICMSSTRet.obrigatorio  = True
            self.grupo_icms.CST._valor_string       = u'60'

        elif self.valor == u'900':
            self.grupo_icms.nome_tag = u'ICMSSN900'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSSN900'
            self.grupo_icms.modBC.obrigatorio       = True
            self.grupo_icms.vBC.obrigatorio         = True
            self.grupo_icms.pICMS.obrigatorio       = True
            self.grupo_icms.vICMS.obrigatorio       = True
            self.grupo_icms.modBCST.obrigatorio     = True
            self.grupo_icms.vBCST.obrigatorio       = True
            self.grupo_icms.pICMSST.obrigatorio     = True
            self.grupo_icms.vICMSST.obrigatorio     = True
            self.grupo_icms.pCredSN.obrigatorio     = True
            self.grupo_icms.vCredICMSSN.obrigatorio = True
            self.grupo_icms.CST._valor_string       = u'90'

        #
        # Redefine a raiz para todas as tags do grupo ICMS
        #
        self.grupo_icms.orig.raiz        = self.grupo_icms.raiz_tag
        self.grupo_icms.CSOSN.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.modBC.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.vBC.raiz         = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBC.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMS.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMS.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.modBCST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.pMVAST.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBCST.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCST.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMSST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCSTRet.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSSTRet.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.pCredSN.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.vCredICMSSN.raiz = self.grupo_icms.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class TagCSTICMS(nfe_110.TagCSTICMS):
    def __init__(self, *args, **kwargs):
        super(TagCSTICMS, self).__init__(*args, **kwargs)
        self.nome = u'CST'
        self.codigo = u'N12'
        self.tamanho = [2, 2]
        self.raiz = u''
        self.grupo_icms = None

    def set_valor(self, novo_valor):
        super(TagCSTICMS, self).set_valor(novo_valor)

        if not self.grupo_icms:
            return None

        #
        # Definimos todas as tags como não obrigatórias
        #
        self.grupo_icms.modBC.obrigatorio       = False
        self.grupo_icms.vBC.obrigatorio         = False
        self.grupo_icms.pRedBC.obrigatorio      = False
        self.grupo_icms.pICMS.obrigatorio       = False
        self.grupo_icms.vICMS.obrigatorio       = False
        self.grupo_icms.modBCST.obrigatorio     = False
        self.grupo_icms.pMVAST.obrigatorio      = False
        self.grupo_icms.pRedBCST.obrigatorio    = False
        self.grupo_icms.vBCST.obrigatorio       = False
        self.grupo_icms.pICMSST.obrigatorio     = False
        self.grupo_icms.vICMSST.obrigatorio     = False
        self.grupo_icms.motDesICMS.obrigatorio  = False
        self.grupo_icms.vBCSTRet.obrigatorio    = False
        self.grupo_icms.vICMSSTRet.obrigatorio  = False
        self.grupo_icms.vBCSTDest.obrigatorio   = False
        self.grupo_icms.vICMSSTDest.obrigatorio = False
        self.grupo_icms.UFST.obrigatorio        = False
        self.grupo_icms.pBCOp.obrigatorio       = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo ICMS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_icms.modBC.valor       = 3
        self.grupo_icms.vBC.valor         = u'0.00'
        self.grupo_icms.pRedBC.valor      = u'0.00'
        self.grupo_icms.pICMS.valor       = u'0.00'
        self.grupo_icms.vICMS.valor       = u'0.00'
        self.grupo_icms.modBCST.valor     = 4
        self.grupo_icms.pMVAST.valor      = u'0.00'
        self.grupo_icms.pRedBCST.valor    = u'0.00'
        self.grupo_icms.vBCST.valor       = u'0.00'
        self.grupo_icms.pICMSST.valor     = u'0.00'
        self.grupo_icms.vICMSST.valor     = u'0.00'
        self.grupo_icms.motDesICMS.valor  = 0
        self.grupo_icms.vBCSTRet.valor    = u'0.00'
        self.grupo_icms.vICMSSTRet.valor  = u'0.00'
        self.grupo_icms.vBCSTDest.valor   = u'0.00'
        self.grupo_icms.vICMSSTDest.valor = u'0.00'
        self.grupo_icms.UFST.valor        = u''
        self.grupo_icms.pBCOp.valor       = u'0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de ICMS
        #
        if self.valor == u'00':
            self.grupo_icms.nome_tag = u'ICMS00'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS00'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True

        elif self.valor == u'10':
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

            if not self.grupo_icms.partilha:
                self.grupo_icms.nome_tag = u'ICMS10'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS10'
            else:
                self.grupo_icms.nome_tag = u'ICMSPart'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSPart'
                self.grupo_icms.pBCOp.obrigatorio    = True
                self.grupo_icms.UFST.obrigatorio     = True

        elif self.valor == u'20':
            self.grupo_icms.nome_tag = u'ICMS20'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS20'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pRedBC.obrigatorio   = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True

        elif self.valor == u'30':
            self.grupo_icms.nome_tag = u'ICMS30'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS30'
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

        elif self.valor in (u'40', u'41', u'50'):
            if self.grupo_icms.repasse and self.valor == u'41':
                self.grupo_icms.nome_tag = u'ICMSST'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSST'
                self.grupo_icms.vBCSTRet.obrigatorio    = True
                self.grupo_icms.vICMSSTRet.obrigatorio  = True
                self.grupo_icms.vBCSTDest.obrigatorio   = True
                self.grupo_icms.vICMSSTDest.obrigatorio = True
            else:
                self.grupo_icms.nome_tag = u'ICMS40'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS40'

        elif self.valor == u'51':
            self.grupo_icms.nome_tag = u'ICMS51'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS51'

        elif self.valor == u'60':
            self.grupo_icms.nome_tag = u'ICMS60'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS60'
            self.grupo_icms.vBCSTRet.obrigatorio   = True
            self.grupo_icms.vICMSSTRet.obrigatorio = True

        elif self.valor == u'70':
            self.grupo_icms.nome_tag = u'ICMS70'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS70'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pRedBC.obrigatorio   = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

        elif self.valor == u'90':
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

            if not self.grupo_icms.partilha:
                self.grupo_icms.nome_tag = u'ICMS90'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS90'
            else:
                self.grupo_icms.nome_tag = u'ICMSPart'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSPart'
                self.grupo_icms.pBCOp.obrigatorio    = True
                self.grupo_icms.UFST.obrigatorio     = True

        #
        # Redefine a raiz para todas as tags do grupo ICMS
        #
        self.grupo_icms.orig.raiz        = self.grupo_icms.raiz_tag
        self.grupo_icms.CST.raiz         = self.grupo_icms.raiz_tag
        self.grupo_icms.modBC.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.vBC.raiz         = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBC.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMS.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMS.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.modBCST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.pMVAST.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBCST.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCST.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMSST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.motDesICMS.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCSTRet.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSSTRet.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCSTDest.raiz   = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSSTDest.raiz = self.grupo_icms.raiz_tag
        self.grupo_icms.UFST.raiz        = self.grupo_icms.raiz_tag
        self.grupo_icms.pBCOp.raiz       = self.grupo_icms.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class ICMS(nfe_110.ICMS):
    def __init__(self):
        super(ICMS, self).__init__()
        self.nome_tag = u'ICMSSN102'
        self.raiz_tag = u'//det/imposto/ICMS/ICMSSN102'

        #
        # Valores de controle, para gerar corretamente as tags
        # com os novos campos
        #
        self.regime_tributario = 1 # Simples Nacional
        self.partilha          = False # Para o grupo ICMSPart
        self.repasse           = False # Para o grupo ICMSST

        #
        # Novos campos para o ICMS
        #
        self.UFST        = TagCaracter(nome=u'UFST'      , codigo=u'N24', tamanho=[2,  2]                       , raiz=u'')
        self.pBCOp       = TagDecimal(nome=u'pBCOp'      , codigo=u'N25', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'')
        self.vBCSTRet    = TagDecimal(nome=u'vBCSTRet'   , codigo=u'N26', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.vICMSSTRet  = TagDecimal(nome=u'vICMSSTRet' , codigo=u'N27', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.motDesICMS  = TagInteiro(nome=u'motDesICMS' , codigo=u'N28', tamanho=[1, 1]                        , raiz=u'')
        self.pCredSN     = TagDecimal(nome=u'pCredSN'    , codigo=u'N29', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.vCredICMSSN = TagDecimal(nome=u'vCredICMSSN', codigo=u'N30', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.vBCSTDest   = TagDecimal(nome=u'vBCSTDest'  , codigo=u'N31', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.vICMSSTDest = TagDecimal(nome=u'vICMSSTDest', codigo=u'N32', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')

        #
        # Situação tributária do Simples Nacional
        #
        self.CSOSN = TagCSOSN()
        self.CSOSN.grupo_icms = self
        self.CSOSN.valor = u'400'

        #
        # Situação tributária tradicional
        #
        self.CST = TagCSTICMS()
        self.CST.grupo_icms = self
        self.CST.valor = u'41'

    def get_xml(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += u'<ICMS><' + self.nome_tag + u'>'
        xml += self.orig.xml

        #
        # Se for regime tradicional (não Simples Nacional)
        #
        if self.regime_tributario != 1:
            xml += self.CST.xml

            if self.CST.valor == u'00':
                xml += self.modBC.xml
                xml += self.vBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml

            elif self.CST.valor == u'10':
                if not self.partilha:
                    xml += self.modBC.xml
                    xml += self.vBC.xml
                    #xml += self.pRedBC.xml
                    xml += self.pICMS.xml
                    xml += self.vICMS.xml
                    xml += self.modBCST.xml

                    # Somente quando for marge de valor agregado
                    if self.modBCST.valor == 4:
                        xml += self.pMVAST.xml

                    xml += self.pRedBCST.xml
                    xml += self.vBCST.xml
                    xml += self.pICMSST.xml
                    xml += self.vICMSST.xml
                else:
                    xml += self.modBC.xml
                    xml += self.vBC.xml
                    xml += self.pRedBC.xml
                    xml += self.pICMS.xml
                    xml += self.vICMS.xml
                    xml += self.modBCST.xml

                    # Somente quando for marge de valor agregado
                    if self.modBCST.valor == 4:
                        xml += self.pMVAST.xml

                    xml += self.pRedBCST.xml
                    xml += self.vBCST.xml
                    xml += self.pICMSST.xml
                    xml += self.vICMSST.xml
                    xml += self.pBCOp.xml
                    xml += self.UFST.xml

            elif self.CST.valor == u'20':
                xml += self.modBC.xml
                xml += self.vBC.xml
                xml += self.pRedBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml

            elif self.CST.valor == u'30':
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

            elif self.CST.valor in (u'40', u'41', u'50'):
                if self.repasse and self.CST.valor == u'41':
                    xml += self.vBCSTRet.xml
                    xml += self.vICMSSTRet.xml
                    xml += self.vBCSTDest.xml
                    xml += self.vICMSSTDest.xml

                elif self.motDesICMS.valor:
                    xml += self.vICMS.xml
                    xml += self.motDesICMS.xml

            elif self.CST.valor == u'51':
                xml += self.modBC.xml
                xml += self.pRedBC.xml
                xml += self.vBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml

            elif self.CST.valor == u'60':
                xml += self.vBCSTRet.xml
                xml += self.vICMSSTRet.xml

            elif self.CST.valor == u'70':
                xml += self.modBC.xml
                xml += self.vBC.xml
                xml += self.pRedBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

            elif self.CST.valor == u'90':
                xml += self.modBC.xml
                xml += self.vBC.xml
                xml += self.pRedBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

                if self.partilha:
                    xml += self.pBCOp.xml
                    xml += self.UFST.xml

        #
        # O regime tributário é o Simples Nacional
        #
        else:
            xml += self.CSOSN.xml

            if self.CSOSN.valor == u'101':
                xml += self.pCredSN.xml
                xml += self.vCredICMSSN.xml

            elif self.CSOSN.valor in (u'102', u'103', u'300', u'400'):
                pass

            elif self.CSOSN.valor == u'201':
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml
                xml += self.pCredSN.xml
                xml += self.vCredICMSSN.xml

            elif self.CSOSN.valor in (u'202', u'203'):
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml

            elif self.CSOSN.valor == u'500':
                xml += self.vBCSTRet.xml
                xml += self.vICMSSTRet.xml

            elif self.CSOSN.valor == u'900':
                xml += self.modBC.xml
                xml += self.vBC.xml
                xml += self.pRedBC.xml
                xml += self.pICMS.xml
                xml += self.vICMS.xml
                xml += self.modBCST.xml

                # Somente quando for marge de valor agregado
                if self.modBCST.valor == 4:
                    xml += self.pMVAST.xml

                xml += self.pRedBCST.xml
                xml += self.vBCST.xml
                xml += self.pICMSST.xml
                xml += self.vICMSST.xml
                xml += self.pCredSN.xml
                xml += self.vCredICMSSN.xml

        xml += u'</' + self.nome_tag + u'></ICMS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o ICMS, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            self.partilha = False
            self.repasse  = False

            if self._le_noh(u'//det/imposto/ICMS/ICMS00') is not None:
                self.regime_tributario = 3
                self.CST.valor = u'00'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS10') is not None:
                self.regime_tributario = 3
                self.CST.valor = u'10'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS20') is not None:
                self.regime_tributario = 3
                self.CST.valor = u'20'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS30') is not None:
                self.regime_tributario = 3
                self.CST.valor = u'30'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS40') is not None:
                self.regime_tributario = 3
                self.CST.valor = u'40'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS51') is not None:
                self.regime_tributario = 3
                self.CST.valor = u'51'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS60') is not None:
                self.regime_tributario = 3
                self.CST.valor = u'60'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS70') is not None:
                self.regime_tributario = 3
                self.CST.valor = u'70'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS90') is not None:
                self.regime_tributario = 3
                self.CST.valor = u'90'
            elif self._le_noh(u'//det/imposto/ICMS/ICMSPart') is not None:
                self.regime_tributario = 3
                self.partilha = True
                self.CST.valor = u'10'
            elif self._le_noh(u'//det/imposto/ICMS/ICMSST') is not None:
                self.regime_tributario = 3
                self.repasse = True
                self.CST.valor = u'41'
            elif self._le_noh(u'//det/imposto/ICMS/ICMSSN101') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = u'101'
            elif self._le_noh(u'//det/imposto/ICMS/ICMSSN102') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = u'102'
            elif self._le_noh(u'//det/imposto/ICMS/ICMSSN201') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = u'201'
            elif self._le_noh(u'//det/imposto/ICMS/ICMSSN202') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = u'202'
            elif self._le_noh(u'//det/imposto/ICMS/ICMSSN500') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = u'500'
            elif self._le_noh(u'//det/imposto/ICMS/ICMSSN900') is not None:
                self.regime_tributario = 1
                self.CSOSN.valor = u'900'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            self.orig.xml       = arquivo
            self.CST.xml        = arquivo
            self.modBC.xml      = arquivo
            self.vBC.xml        = arquivo
            self.pRedBC.xml     = arquivo
            self.pICMS.xml      = arquivo
            self.vICMS.xml      = arquivo
            self.modBCST.xml    = arquivo
            self.pMVAST.xml     = arquivo
            self.pRedBCST.xml   = arquivo
            self.vBCST.xml      = arquivo
            self.pICMSST.xml    = arquivo
            self.vICMSST.xml    = arquivo
            self.vBCSTRet.xml   = arquivo
            self.vICMSSTRet.xml = arquivo

            if self.regime_tributario == 1:
                self.CSOSN.xml       = arquivo
                self.pCredSN.xml     = arquivo
                self.vCredICMSSN.xml = arquivo
            else:
                self.UFST.xml        = arquivo
                self.pBCOp.xml       = arquivo
                self.motDesICMS.xml  = arquivo
                self.vBCSTDest.xml   = arquivo
                self.vICMSSTDest.xml = arquivo

    xml = property(get_xml, set_xml)


class Imposto(nfe_110.Imposto):
    def __init__(self):
        super(Imposto, self).__init__()
        self.ICMS     = ICMS()
        self.ISSQN    = ISSQN()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<imposto>'

        # Enviar ICMS, IPI e II somente quando não for serviço
        if not self.ISSQN.cSitTrib.valor:
            xml += self.ICMS.xml
            xml += self.IPI.xml
            xml += self.II.xml

        xml += self.PIS.xml
        xml += self.PISST.xml
        xml += self.COFINS.xml
        xml += self.COFINSST.xml

        if self.ISSQN.cSitTrib.valor:
            xml += self.ISSQN.xml

        xml += u'</imposto>'
        return xml

    #def set_xml(self, arquivo):
        #if self._le_xml(arquivo):
            #self.ICMS.xml     = arquivo
            #self.IPI.xml      = arquivo
            #self.II.xml       = arquivo
            #self.PIS.xml      = arquivo
            #self.PISST.xml    = arquivo
            #self.COFINS.xml   = arquivo
            #self.COFINSST.xml = arquivo
            #self.ISSQN.xml    = arquivo

    #xml = property(get_xml, set_xml)


class CIDE(nfe_110.CIDE):
    def __init__(self):
        super(CIDE, self).__init__()


class Comb(nfe_110.Comb):
    def get_xml(self):
        if not self.cProdANP.valor:
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<comb>'
        xml += self.cProdANP.xml
        xml += self.CODIF.xml
        xml += self.qTemp.xml
        xml += self.CIDE.xml
        xml += u'</comb>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cProdANP.xml  = arquivo
            self.CODIF.xml     = arquivo
            self.qTemp.xml     = arquivo
            self.CIDE.xml      = arquivo

    xml = property(get_xml, set_xml)


class Arma(nfe_110.Arma):
    def __init__(self):
        super(Arma, self).__init__()


class Med(nfe_110.Med):
    def __init__(self):
        super(Med, self).__init__()


class VeicProd(nfe_110.VeicProd):
    def __init__(self):
        super(VeicProd, self).__init__()
        self.cilin        = TagCaracter(nome=u'cilin'       , codigo=u'J07', tamanho=[ 1,  4], raiz=u'//det/prod/veicProd')
        self.tpComb       = TagCaracter(nome=u'tpComb'      , codigo=u'J11', tamanho=[ 2,  2], raiz=u'//det/prod/veicProd')
        self.CMT          = TagCaracter(nome=u'CMT'         , codigo=u'J13', tamanho=[ 1,  9], raiz=u'//det/prod/veicProd')
        self.cCorDENATRAN = TagCaracter(nome=u'cCorDENATRAN', codigo=u'J24', tamanho=[ 2,  2], raiz=u'//det/prod/veicProd')
        self.lota         = TagInteiro(nome=u'lota'         , codigo=u'J25', tamanho=[ 1,  3], raiz=u'//det/prod/veicProd')
        self.tpRest       = TagInteiro(nome=u'tpRest'       , codigo=u'J26', tamanho=[ 1,  3], raiz=u'//det/prod/veicProd')

    def get_xml(self):
        if not self.chassi.valor:
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<veicProd>'
        xml += self.tpOp.xml
        xml += self.chassi.xml
        xml += self.cCor.xml
        xml += self.xCor.xml
        xml += self.pot.xml
        xml += self.cilin.xml
        xml += self.pesoL.xml
        xml += self.pesoB.xml
        xml += self.nSerie.xml
        xml += self.tpComb.xml
        xml += self.nMotor.xml
        xml += self.CMT.xml
        xml += self.dist.xml
        xml += self.anoMod.xml
        xml += self.anoFab.xml
        xml += self.tpPint.xml
        xml += self.tpVeic.xml
        xml += self.espVeic.xml
        xml += self.VIN.xml
        xml += self.condVeic.xml
        xml += self.cMod.xml
        xml += self.cCorDENATRAN.xml
        xml += self.lota.xml
        xml += self.tpRest.xml
        xml += u'</veicProd>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpOp.xml     = arquivo
            self.chassi.xml   = arquivo
            self.cCor.xml     = arquivo
            self.xCor.xml     = arquivo
            self.pot.xml      = arquivo
            self.cilin.xml      = arquivo
            self.pesoL.xml    = arquivo
            self.pesoB.xml    = arquivo
            self.nSerie.xml   = arquivo
            self.tpComb.xml   = arquivo
            self.nMotor.xml   = arquivo
            self.CMT.xml     = arquivo
            self.dist.xml     = arquivo
            self.anoMod.xml   = arquivo
            self.anoFab.xml   = arquivo
            self.tpPint.xml   = arquivo
            self.tpVeic.xml   = arquivo
            self.espVeic.xml  = arquivo
            self.VIN.xml      = arquivo
            self.condVeic.xml = arquivo
            self.cMod.xml     = arquivo
            self.cCorDENATRAN.xml = arquivo
            self.lota.xml     = arquivo
            self.tpRest.xml   = arquivo

    xml = property(get_xml, set_xml)


class Adi(nfe_110.Adi):
    def __init__(self):
        super(Adi, self).__init__()


class DI(nfe_110.DI):
    def __init__(self):
        super(DI, self).__init__()


class Prod(nfe_110.Prod):
    def __init__(self):
        super(Prod, self).__init__()
        self.NCM      = TagCaracter(nome=u'NCM'     , codigo=u'I05' , tamanho=[2,  8]                        , raiz=u'//det/prod')
        self.qCom     = TagDecimal(nome=u'qCom'     , codigo=u'I10' , tamanho=[1, 15, 1], decimais=[0,  4, 4], raiz=u'//det/prod')
        self.vUnCom   = TagDecimal(nome=u'vUnCom'   , codigo=u'I10a', tamanho=[1, 21, 1], decimais=[0, 10, 4], raiz=u'//det/prod')
        self.qTrib    = TagDecimal(nome=u'qTrib'    , codigo=u'I14' , tamanho=[1, 15, 1], decimais=[0,  4, 4], raiz=u'//det/prod')
        self.vUnTrib  = TagDecimal(nome=u'vUnTrib'  , codigo=u'I14a', tamanho=[1, 21, 1], decimais=[0, 10, 4], raiz=u'//det/prod')
        self.vOutro   = TagDecimal(nome=u'vOutro'   , codigo=u'I17a', tamanho=[1, 15, 1], decimais=[0,  2, 2], raiz=u'//det/prod', obrigatorio=False)
        self.indTot   = TagInteiro(nome=u'indTot'   , codigo=u'I17b', tamanho=[1,  1, 1],                      raiz=u'//det/prod', valor=1)
        self.xPed     = TagCaracter(nome=u'xPed'    , codigo=u'I30' , tamanho=[1, 15],                         raiz=u'//det/prod', obrigatorio=False)
        self.nItemPed = TagCaracter(nome=u'nItemPed', codigo=u'I31' , tamanho=[1,  6],                         raiz=u'//det/prod', obrigatorio=False)
        self.veicProd = VeicProd()
        self.comb     = Comb()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<prod>'
        xml += self.cProd.xml
        xml += self.cEAN.xml
        xml += self.xProd.xml
        xml += self.NCM.xml
        xml += self.EXTIPI.xml
        #xml += self.genero.xml
        xml += self.CFOP.xml
        xml += self.uCom.xml
        xml += self.qCom.xml
        xml += self.vUnCom.xml
        xml += self.vProd.xml
        xml += self.cEANTrib.xml
        xml += self.uTrib.xml
        xml += self.qTrib.xml
        xml += self.vUnTrib.xml
        xml += self.vFrete.xml
        xml += self.vSeg.xml
        xml += self.vDesc.xml
        xml += self.vOutro.xml
        xml += self.indTot.xml

        for d in self.DI:
            xml += d.xml

        xml += self.xPed.xml
        xml += self.nItemPed.xml
        xml += self.veicProd.xml

        for m in self.med:
            xml += m.xml

        for a in self.arma:
            xml += a.xml

        xml += self.comb.xml
        xml += u'</prod>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cProd.xml    = arquivo
            self.cEAN.xml     = arquivo
            self.xProd.xml    = arquivo
            self.NCM.xml      = arquivo
            self.EXTIPI.xml   = arquivo
            self.genero.xml   = arquivo
            self.CFOP.xml     = arquivo
            self.uCom.xml     = arquivo
            self.qCom.xml     = arquivo
            self.vUnCom.xml   = arquivo
            self.vProd.xml    = arquivo
            self.cEANTrib.xml = arquivo
            self.uTrib.xml    = arquivo
            self.qTrib.xml    = arquivo
            self.vUnTrib.xml  = arquivo
            self.vFrete.xml   = arquivo
            self.vSeg.xml     = arquivo
            self.vDesc.xml    = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.DI = self.le_grupo('//det/prod/DI', DI)

            self.veicProd.xml = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.med = self.le_grupo('//det/prod/med', Med)
            self.arma = self.le_grupo('//det/prod/arma', Arma)

            self.comb.xml = arquivo

    xml = property(get_xml, set_xml)


class Det(nfe_110.Det):
    def __init__(self):
        super(Det, self).__init__()
        self.prod      = Prod()
        self.imposto   = Imposto()

    def cst_formatado(self):
        if self.imposto.regime_tributario != 1:
            super(Det, self).cst_formatado()
        
        formatado = unicode(self.imposto.ICMS.orig.valor).zfill(1)
        formatado += unicode(self.imposto.ICMS.CSOSN.valor).zfill(3)
        return formatado


class Compra(nfe_110.Compra):
    def __init__(self):
        super(Compra, self).__init__()


class Exporta(nfe_110.Exporta):
    def __init__(self):
        super(Exporta, self).__init__()


class ProcRef(nfe_110.ProcRef):
    def __init__(self):
        super(ProcRef, self).__init__()


class ObsFisco(nfe_110.ObsFisco):
    def __init__(self):
        super(ObsFisco, self).__init__()


class ObsCont(nfe_110.ObsCont):
    def __init__(self):
        super(ObsCont, self).__init__()


class InfAdic(nfe_110.InfAdic):
    def __init__(self):
        super(InfAdic, self).__init__()
        self.infAdFisco = TagCaracter(nome=u'infAdFisco', codigo=u'Z02', tamanho=[1, 2000], raiz=u'//NFe/infNFe/infAdic', obrigatorio=False)


class Dup(nfe_110.Dup):
    def __init__(self):
        super(Dup, self).__init__()


class Fat(nfe_110.Fat):
    def __init__(self):
        super(Fat, self).__init__()


class Cobr(nfe_110.Cobr):
    def __init__(self):
        super(Cobr, self).__init__()


class Lacres(nfe_110.Lacres):
    def __init__(self):
        super(Lacres, self).__init__()


class Vol(nfe_110.Vol):
    def __init__(self, xml=None):
        super(Vol, self).__init__()


class Reboque(nfe_110.Reboque):
    def __init__(self):
        super(Reboque, self).__init__()


class VeicTransp(nfe_110.VeicTransp):
    def __init__(self):
        super(VeicTransp, self).__init__()


class RetTransp(nfe_110.RetTransp):
    def __init__(self):
        super(RetTransp, self).__init__()


class Transporta(nfe_110.Transporta):
    def __init__(self):
        super(Transporta, self).__init__()


class Transp(nfe_110.Transp):
    def __init__(self):
        super(Transp, self).__init__()
        self.vagao = TagCaracter(nome=u'vagao', codigo=u'X25a', tamanho=[1, 20], raiz=u'//NFe/infNFe/transp', obrigatorio=False)
        self.balsa = TagCaracter(nome=u'balsa', codigo=u'X25b', tamanho=[1, 20], raiz=u'//NFe/infNFe/transp', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<transp>'
        xml += self.modFrete.xml
        xml += self.transporta.xml
        xml += self.retTransp.xml

        if self.balsa.valor:
            xml += self.balsa.xml
        elif self.vagao.valor:
            xml += self.vagao.xml
        else:
            xml += self.veicTransp.xml

            for r in self.reboque:
                xml += r.xml

        for v in self.vol:
            xml += v.xml

        xml += u'</transp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.modFrete.xml   = arquivo
            self.transporta.xml = arquivo
            self.retTransp.xml  = arquivo
            self.veicTransp.xml = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.reboque = self.le_grupo('//NFe/infNFe/transp/reboque', nfe_110.Reboque)

            self.vagao.xml = arquivo
            self.balsa.xml = arquivo

            self.vol = self.le_grupo('//NFe/infNFe/transp/vol', nfe_110.Vol)


    xml = property(get_xml, set_xml)


class RetTrib(nfe_110.RetTrib):
    def __init__(self):
        super(RetTrib, self).__init__()


class ISSQNTot(nfe_110.ISSQNTot):
    def __init__(self):
        super(ISSQNTot, self).__init__()


class ICMSTot(nfe_110.ICMSTot):
    def __init__(self):
        super(ICMSTot, self).__init__()


class Total(nfe_110.Total):
    def __init__(self):
        super(Total, self).__init__()


class Entrega(nfe_110.Entrega):
    def __init__(self):
        super(Entrega, self).__init__()
        self.CNPJ    = TagCaracter(nome=u'CNPJ'   , codigo=u'G02' , tamanho=[ 0, 14]   , raiz=u'//NFe/infNFe/retirada')
        self.CPF     = TagCaracter(nome=u'CPF'    , codigo=u'G02a', tamanho=[11, 11]   , raiz=u'//NFe/infNFe/retirada')


    def get_xml(self):
        if not (self.CNPJ.valor or self.CPF.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<entrega>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += u'</entrega>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml    = arquivo
            self.CPF.xml     = arquivo
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.UF.xml      = arquivo

    xml = property(get_xml, set_xml)


class Retirada(nfe_110.Retirada):
    def __init__(self):
        super(Retirada, self).__init__()
        self.CNPJ    = TagCaracter(nome=u'CNPJ'   , codigo=u'F02' , tamanho=[ 0, 14]   , raiz=u'//NFe/infNFe/retirada')
        self.CPF     = TagCaracter(nome=u'CPF'    , codigo=u'F02a', tamanho=[11, 11]   , raiz=u'//NFe/infNFe/retirada')


    def get_xml(self):
        if not (self.CNPJ.valor or self.CPF.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<retirada>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += u'</retirada>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml    = arquivo
            self.CPF.xml     = arquivo
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.UF.xml      = arquivo

    xml = property(get_xml, set_xml)


class EnderDest(nfe_110.EnderDest):
    def __init__(self):
        super(EnderDest, self).__init__()
        self.fone    = TagInteiro(nome=u'fone'    , codigo=u'E16', tamanho=[ 6, 14]   , raiz=u'//NFe/infNFe/dest/enderDest', obrigatorio=False)


class Dest(nfe_110.Dest):
    def __init__(self):
        super(Dest, self).__init__()
        self.enderDest = EnderDest()
        self.ISUF      = TagCaracter(nome=u'ISUF' , codigo=u'E18', tamanho=[ 8,  9], raiz=u'//NFe/infNFe/dest', obrigatorio=False)
        self.email     = TagCaracter(nome=u'email', codigo=u'E19', tamanho=[1, 60], raiz=u'//NFe/infNFe/dest', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<dest>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.xNome.xml
        xml += self.enderDest.xml
        xml += self.IE.xml
        xml += self.ISUF.xml
        xml += self.email.xml
        xml += u'</dest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.xNome.xml     = arquivo
            self.enderDest.xml = arquivo
            self.IE.xml        = arquivo
            self.ISUF.xml      = arquivo
            self.email.xml     = arquivo

    xml = property(get_xml, set_xml)


class Avulsa(nfe_110.Avulsa):
    def __init__(self):
        super(Avulsa, self).__init__()
        self.fone    = TagInteiro(nome=u'fone'    , codigo=u'D05', tamanho=[ 6, 14], raiz=u'//NFe/infNFe/avulsa')


class EnderEmit(nfe_110.EnderEmit):
    def __init__(self):
        super(EnderEmit, self).__init__()
        self.fone    = TagInteiro(nome=u'fone'    , codigo=u'C16', tamanho=[ 6, 14]   , raiz=u'//NFe/infNFe/emit/enderEmit', obrigatorio=False)


class Emit(nfe_110.Emit):
    def __init__(self):
        super(Emit, self).__init__()
        self.enderEmit = EnderEmit()
        self.CRT       = TagInteiro(nome=u'CRT'  , codigo=u'C21' , tamanho=[ 1,  1], raiz=u'//NFe/infNFe/emit', valor=1)


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<emit>'
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.xNome.xml
        xml += self.xFant.xml
        xml += self.enderEmit.xml
        xml += self.IE.xml
        xml += self.IEST.xml
        xml += self.IM.xml
        xml += self.CNAE.xml
        xml += self.CRT.xml
        xml += u'</emit>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.xNome.xml     = arquivo
            self.xFant.xml     = arquivo
            self.enderEmit.xml = arquivo
            self.IE.xml        = arquivo
            self.IEST.xml      = arquivo
            self.IM.xml        = arquivo
            self.CNAE.xml      = arquivo
            self.CRT.xml       = arquivo

    xml = property(get_xml, set_xml)


class RefECF(XMLNFe):
    def __init__(self):
        super(RefECF, self).__init__()
        self.mod   = TagCaracter(nome=u'mod', codigo=u'B20l', tamanho=[ 2,  2, 2], raiz=u'//NFref/refECF')
        self.nECF  = TagInteiro(nome=u'nECF', codigo=u'B20m', tamanho=[ 1,  3, 1], raiz=u'//NFref/refECF')
        self.nCOO  = TagInteiro(nome=u'nCOO', codigo=u'B20n', tamanho=[ 1,  6, 1], raiz=u'//NFref/refECF')

    def get_xml(self):
        if not (self.mod.valor or self.nECF.valor or self.nCOO.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<refECF>'
        xml += self.mod.xml
        xml += self.nECF.xml
        xml += self.nCOO.xml
        xml += u'</refECF>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.mod.xml   = arquivo
            self.nECF.xml = arquivo
            self.nCOO.xml   = arquivo

    xml = property(get_xml, set_xml)


class RefNFP(XMLNFe):
    def __init__(self):
        super(RefNFP, self).__init__()
        self.cUF   = TagInteiro(nome=u'cUF'  , codigo=u'B20b', tamanho=[ 2,  2, 2], raiz=u'//NFref/refNFP')
        self.AAMM  = TagCaracter(nome=u'AAMM', codigo=u'B20c', tamanho=[ 4,  4, 4], raiz=u'//NFref/refNFP')
        self.CNPJ  = TagCaracter(nome=u'CNPJ', codigo=u'B20d', tamanho=[14, 14]   , raiz=u'//NFref/refNFP')
        self.CPF   = TagCaracter(nome=u'CPF' , codigo=u'B20e', tamanho=[11, 11]   , raiz=u'//NFref/refNFP')
        self.IE    = TagCaracter(nome=u'IE'  , codigo=u'B20f', tamanho=[ 1, 14]   , raiz=u'//NFref/refNFP')
        self.mod   = TagCaracter(nome=u'mod' , codigo=u'B20g', tamanho=[ 2,  2, 2], raiz=u'//NFref/refNFP')
        self.serie = TagInteiro(nome=u'serie', codigo=u'B20h', tamanho=[ 1,  3, 1], raiz=u'//NFref/refNFP')
        self.nNF   = TagInteiro(nome=u'nNF'  , codigo=u'B20i', tamanho=[ 1,  9, 1], raiz=u'//NFref/refNFP')

    def get_xml(self):
        if not (self.cUF.valor or self.AAMM.valor or self.CNPJ.valor or self.CPF.valor or self.IE.valor or self.mod.valor or self.serie.valor or self.nNF.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<refNFP>'
        xml += self.cUF.xml
        xml += self.AAMM.xml

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml

        xml += self.IE.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNF.xml
        xml += u'</refNFP>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml   = arquivo
            self.AAMM.xml  = arquivo
            self.CNPJ.xml  = arquivo
            self.CPF.xml   = arquivo
            self.IE.xml    = arquivo
            self.mod.xml   = arquivo
            self.serie.xml = arquivo
            self.nNF.xml   = arquivo

    xml = property(get_xml, set_xml)


class RefNF(nfe_110.RefNF):
    def __init__(self):
        super(RefNF, self).__init__()


class NFRef(nfe_110.NFRef):
    def __init__(self):
        super(NFRef, self).__init__()
        #self.refNFe = TagCaracter(nome=u'refNFe', codigo=u'B13', tamanho=[44, 44], raiz=u'//NFRef', obrigatorio=False)
        #self.refNF  = RefNF()
        self.refNFP = RefNFP()
        self.refCTe = TagCaracter(nome=u'refCTe', codigo=u'B20j', tamanho=[44, 44], raiz=u'//NFRef', obrigatorio=False)
        self.refECF = RefECF()

    def get_xml(self):
        if not (self.refNFe.valor or self.refNF.xml or self.refNFP.xml or self.refCTe.valor or self.refECF.xml):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<NFref>'

        if self.refNFe.valor:
            xml += self.refNFe.xml
        elif self.refNF.xml:
            xml += self.refNF.xml
        elif self.refNFP.xml:
            xml += self.refNFP.xml
        elif self.refCTe.valor:
            xml += self.refCTe.xml
        elif self.refECF.xml:
            xml += self.refECF.xml

        xml += u'</NFref>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.refNFe.xml = arquivo
            self.refNF.xml  = arquivo
            self.refNFP.xml = arquivo
            self.refCTe.xml = arquivo
            self.refECF.xml = arquivo

    xml = property(get_xml, set_xml)


class Ide(nfe_110.Ide):
    def __init__(self):
        super(Ide, self).__init__()
        self.cNF     = TagCaracter(nome=u'cNF'     , codigo=u'B03', tamanho=[ 8,  8, 8], raiz=u'//NFe/infNFe/ide')
        self.hSaiEnt = TagHora(nome=u'hSaiEnt'    , codigo=u'B10a',                     raiz=u'//NFe/infNFe/ide', obrigatorio=False)
        self.dhCont   = TagDataHora(nome=u'dhCont', codigo=u'B28',                      raiz=u'//NFe/infNFe/ide', obrigatorio=False)
        self.xJust    = TagCaracter(nome=u'xJust',  codigo=u'B29',                      raiz=u'//NFe/infNFe/ide', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<ide>'
        xml += self.cUF.xml
        xml += self.cNF.xml
        xml += self.natOp.xml
        xml += self.indPag.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNF.xml
        xml += self.dEmi.xml
        xml += self.dSaiEnt.xml
        xml += self.tpNF.xml
        xml += self.cMunFG.xml

        for nr in self.NFref:
            xml += nr.xml

        xml += self.tpImp.xml
        xml += self.tpEmis.xml
        xml += self.cDV.xml
        xml += self.tpAmb.xml
        xml += self.finNFe.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += self.dhCont.xml
        xml += self.xJust.xml
        xml += u'</ide>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml     = arquivo
            self.cNF.xml     = arquivo
            self.natOp.xml   = arquivo
            self.indPag.xml  = arquivo
            self.mod.xml     = arquivo
            self.serie.xml   = arquivo
            self.nNF.xml     = arquivo
            self.dEmi.xml    = arquivo
            self.dSaiEnt.xml = arquivo
            self.tpNF.xml    = arquivo
            self.cMunFG.xml  = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.NFRef = self.le_grupo('//NFe/infNFe/ide/NFref', NFRef)

            self.tpImp.xml   = arquivo
            self.tpEmis.xml  = arquivo
            self.cDV.xml     = arquivo
            self.tpAmb.xml   = arquivo
            self.finNFe.xml  = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo
            self.dhCont.xml  = arquivo
            self.xJust.xml   = arquivo

    xml = property(get_xml, set_xml)


class InfNFe(nfe_110.InfNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.versao   = TagDecimal(nome=u'infNFe' , codigo=u'A01', propriedade=u'versao', raiz=u'//NFe', namespace=NAMESPACE_NFE, valor=u'2.00')
        #self.Id       = TagCaracter(nome=u'infNFe', codigo=u'A03', propriedade=u'Id'    , raiz=u'//NFe', namespace=NAMESPACE_NFE)
        self.ide      = Ide()
        self.emit     = Emit()
        self.avulsa   = Avulsa()
        self.dest     = Dest()
        self.retirada = Retirada()
        self.entrega  = Entrega()
        self.det      = []
        self.total    = Total()
        self.transp   = Transp()
        self.cobr     = Cobr()
        self.infAdic  = InfAdic()
        self.exporta  = Exporta()
        self.compra   = Compra()
        self.cana     = Cana()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<infNFe versao="' + unicode(self.versao.valor) + u'" Id="' + self.Id.valor + u'">'
        xml += self.ide.xml
        xml += self.emit.xml
        xml += self.avulsa.xml
        xml += self.dest.xml
        xml += self.retirada.xml
        xml += self.entrega.xml

        for d in self.det:
            xml += d.xml

        xml += self.total.xml
        xml += self.transp.xml
        xml += self.cobr.xml
        xml += self.infAdic.xml
        xml += self.exporta.xml
        xml += self.compra.xml
        xml += self.cana.xml
        xml += u'</infNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.Id.xml       = arquivo
            self.ide.xml      = arquivo
            self.emit.xml     = arquivo
            self.avulsa.xml   = arquivo
            self.dest.xml     = arquivo
            self.retirada.xml = arquivo
            self.entrega.xml  = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.det = self.le_grupo('//NFe/infNFe/det', Det)

            self.total.xml    = arquivo
            self.transp.xml   = arquivo
            self.cobr.xml     = arquivo
            self.infAdic.xml  = arquivo
            self.exporta.xml  = arquivo
            self.compra.xml   = arquivo
            self.cana.xml     = arquivo

    xml = property(get_xml, set_xml)


class NFe(nfe_110.NFe):
    def __init__(self):
        super(NFe, self).__init__()
        self.infNFe = InfNFe()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'nfe_v2.00.xsd'

    def gera_nova_chave(self):
        super(NFe, self).gera_nova_chave()

        #
        # Ajustar o campo cNF para remover o 1º dígito, que é
        # o tipo da emissão
        #
        self.infNFe.ide.cNF.valor = self.chave[35:43]

    def monta_chave(self):
        chave = unicode(self.infNFe.ide.cUF.valor).strip().rjust(2, u'0')
        chave += unicode(self.infNFe.ide.dEmi.valor.strftime(u'%y%m')).strip().rjust(4, u'0')
        chave += unicode(self.infNFe.emit.CNPJ.valor).strip().rjust(14, u'0')
        chave += u'55'
        chave += unicode(self.infNFe.ide.serie.valor).strip().rjust(3, u'0')
        chave += unicode(self.infNFe.ide.nNF.valor).strip().rjust(9, u'0')

        #
        # Inclui agora o tipo da emissão
        #
        chave += unicode(self.infNFe.ide.tpEmis.valor).strip().rjust(1, u'0')

        chave += unicode(self.infNFe.ide.cNF.valor).strip().rjust(8, u'0')
        chave += unicode(self.infNFe.ide.cDV.valor).strip().rjust(1, u'0')
        self.chave = chave
