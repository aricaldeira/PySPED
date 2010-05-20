# -*- coding: utf-8 -*-

from pysped.xml_sped import *
#from soap_100 import SOAPEnvio, SOAPRetorno, conectar_servico
from pysped.nfe.manual_300 import ESQUEMA_ATUAL
import os
import random

DIRNAME = os.path.dirname(__file__)


class ISSQN(XMLNFe):
    def __init__(self):
        super(ISSQN, self).__init__()
        self.vBC       = TagDecimal(nome=u'vBC'      , codigo=u'U02', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/ISSQN')
        self.vAliq     = TagDecimal(nome=u'vAliq'    , codigo=u'U03', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/ISSQN')
        self.vISSQN    = TagDecimal(nome=u'vISSQN'   , codigo=u'U04', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/ISSQN')
        self.cMunFG    = TagInteiro(nome=u'cMunFG'   , codigo=u'U05', tamanho=[7,  7, 7],                     raiz=u'//det/imposto/ISSQN')
        self.cListServ = TagInteiro(nome=u'cListServ', codigo=u'U06', tamanho=[3,  4]   ,                     raiz=u'//det/imposto/ISSQN')

    def get_xml(self):
        if not (self.vBC.valor or self.vAliq.valor or self.vISSQN.valor or self.cMunFG.valor or self.cListServ.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<ISSQN>'
        xml += self.vBC.xml
        xml += self.vAliq.xml
        xml += self.vISSQN.xml
        xml += self.cMunFG.xml
        xml += self.cListServ.xml
        xml += u'</ISSQN>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml       = arquivo
            self.vAliq.xml     = arquivo
            self.vISSQN.xml    = arquivo
            self.cMunFG.xml    = arquivo
            self.cListServ.xml = arquivo

    xml = property(get_xml, set_xml)


class COFINSST(XMLNFe):
    def __init__(self):
        super(COFINSST, self).__init__()
        self.vBC       = TagDecimal(nome=u'vBC'      , codigo=u'T02', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/COFINS/COFINSST')
        self.pCOFINS   = TagDecimal(nome=u'pCOFINS'  , codigo=u'T03', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/COFINS/COFINSST')
        self.qBCProd   = TagDecimal(nome=u'qBCProd'  , codigo=u'T04', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz=u'//det/imposto/COFINS/COFINSST')
        self.vAliqProd = TagDecimal(nome=u'vAliqProd', codigo=u'T05', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz=u'//det/imposto/COFINS/COFINSST')
        self.vCOFINS   = TagDecimal(nome=u'vCOFINS'  , codigo=u'T06', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/COFINS/COFINSST')

    def get_xml(self):
        if not (self.vBC.valor or self.pCOFINS.valor or self.qBCProd.valor or self.vAliqProd.valor or self.vCOFINS.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<COFINSST>'

        if self.qBCProd.valor or self.vAliqProd.valor:
            xml += self.qBCProd.xml
            xml += self.vAliqProd.xml
        else:
            xml += self.vBC.xml
            xml += self.pCOFINS.xml

        xml += self.vCOFINS.xml
        xml += u'</COFINSST>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml       = arquivo
            self.pCOFINS.xml   = arquivo
            self.qBCProd.xml   = arquivo
            self.vAliqProd.xml = arquivo
            self.vCOFINS.xml   = arquivo

    xml = property(get_xml, set_xml)


class TagCSTCOFINS(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagCSTCOFINS, self).__init__(*args, **kwargs)
        self.nome = u'CST'
        self.codigo = u'S06'
        self.tamanho = [2, 2]
        self.raiz = u''
        self.grupo_cofins = None

    def set_valor(self, novo_valor):
        super(TagCSTCOFINS, self).set_valor(novo_valor)

        if not self.grupo_cofins:
            return None

        #
        # Definimos todas as tags como não obrigatórias
        #
        self.grupo_cofins.vBC.obrigatorio       = False
        self.grupo_cofins.pCOFINS.obrigatorio   = False
        self.grupo_cofins.vCOFINS.obrigatorio   = False
        self.grupo_cofins.qBCProd.obrigatorio   = False
        self.grupo_cofins.vAliqProd.obrigatorio = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo COFINS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_cofins.vBC.valor       = u'0.00'
        self.grupo_cofins.pCOFINS.valor   = u'0.00'
        self.grupo_cofins.vCOFINS.valor   = u'0.00'
        self.grupo_cofins.qBCProd.valor   = u'0.00'
        self.grupo_cofins.vAliqProd.valor = u'0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de COFINS
        #
        if self.valor in (u'01', u'02'):
            self.grupo_cofins.nome_tag = u'COFINSAliq'
            self.grupo_cofins.raiz_tag = u'//det/imposto/COFINS/COFINSAliq'
            self.grupo_cofins.vBC.obrigatorio       = True
            self.grupo_cofins.pCOFINS.obrigatorio   = True
            self.grupo_cofins.vCOFINS.obrigatorio   = True
            #self.grupo_cofins.qBCProd.obrigatorio   = True
            #self.grupo_cofins.vAliqProd.obrigatorio = True

        elif self.valor == u'03':
            self.grupo_cofins.nome_tag = u'COFINSQtde'
            self.grupo_cofins.raiz_tag = u'//det/imposto/COFINS/COFINSQtde'
            #self.grupo_cofins.vBC.obrigatorio       = True
            #self.grupo_cofins.pCOFINS.obrigatorio   = True
            self.grupo_cofins.vCOFINS.obrigatorio   = True
            self.grupo_cofins.qBCProd.obrigatorio   = True
            self.grupo_cofins.vAliqProd.obrigatorio = True

        elif self.valor == u'99':
            self.grupo_cofins.nome_tag = u'COFINSOutr'
            self.grupo_cofins.raiz_tag = u'//det/imposto/COFINS/COFINSOutr'
            self.grupo_cofins.vBC.obrigatorio       = True
            self.grupo_cofins.pCOFINS.obrigatorio   = True
            self.grupo_cofins.vCOFINS.obrigatorio   = True
            self.grupo_cofins.qBCProd.obrigatorio   = True
            self.grupo_cofins.vAliqProd.obrigatorio = True

        else:
            self.grupo_cofins.nome_tag = u'COFINSNT'
            self.grupo_cofins.raiz_tag = u'//det/imposto/COFINS/COFINSNT'
            #self.grupo_cofins.vBC.obrigatorio       = True
            #self.grupo_cofins.pCOFINS.obrigatorio   = True
            #self.grupo_cofins.vCOFINS.obrigatorio   = True
            #self.grupo_cofins.qBCProd.obrigatorio   = True
            #self.grupo_cofins.vAliqProd.obrigatorio = True

        #
        # Redefine a raiz para todas as tags do grupo COFINS
        #
        self.grupo_cofins.CST.raiz       = self.grupo_cofins.raiz_tag
        self.grupo_cofins.vBC.raiz       = self.grupo_cofins.raiz_tag
        self.grupo_cofins.pCOFINS.raiz   = self.grupo_cofins.raiz_tag
        self.grupo_cofins.vCOFINS.raiz   = self.grupo_cofins.raiz_tag
        self.grupo_cofins.qBCProd.raiz   = self.grupo_cofins.raiz_tag
        self.grupo_cofins.vAliqProd.raiz = self.grupo_cofins.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class COFINS(XMLNFe):
    def __init__(self):
        super(COFINS, self).__init__()
        self.nome_tag = u'COFINSAliq'
        self.raiz_tag = u'//det/imposto/COFINS/COFINSAliq'

        self.vBC       = TagDecimal(nome=u'vBC'      , codigo=u'S07', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.pCOFINS   = TagDecimal(nome=u'pCOFINS'  , codigo=u'S08', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'')
        self.vCOFINS   = TagDecimal(nome=u'vCOFINS'  , codigo=u'S11', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.qBCProd   = TagDecimal(nome=u'qBCProd'  , codigo=u'S09', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz=u'')
        self.vAliqProd = TagDecimal(nome=u'vAliqProd', codigo=u'S10', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz=u'')

        self.CST      = TagCSTCOFINS()
        self.CST.grupo_cofins = self
        self.CST.valor = u'07'

    def get_xml(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += u'<COFINS>'
        xml += '<' + self.nome_tag + u'>'
        xml += self.CST.xml

        if self.CST.valor in (u'01', u'02'):
            xml += self.vBC.xml
            xml += self.pCOFINS.xml
            xml += self.vCOFINS.xml

        elif self.CST.valor == u'03':
            xml += self.qBCProd.xml
            xml += self.vAliqProd.xml
            xml += self.vCOFINS.xml

        elif self.CST.valor != u'99':
            pass

        else:
            if self.qBCProd.valor or self.vAliqProd.valor:
                xml += self.qBCProd.xml
                xml += self.vAliqProd.xml
            else:
                xml += self.vBC.xml
                xml += self.pCOFINS.xml
            xml += self.vCOFINS.xml

        xml += u'</' + self.nome_tag + u'></COFINS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o COFINS, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            if self._le_noh(u'//det/imposto/COFINS/COFINSAliq') is not None:
                self.CST.valor = u'01'
            elif self._le_noh(u'//det/imposto/COFINS/COFINSQtde') is not None:
                self.CST.valor = u'03'
            elif self._le_noh(u'//det/imposto/COFINS/COFINSNT') is not None:
                self.CST.valor = u'04'
            else:
                self.CST.valor = u'99'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            self.CST.xml       = arquivo
            self.vBC.xml       = arquivo
            self.pCOFINS.xml   = arquivo
            self.vCOFINS.xml   = arquivo
            self.qBCProd.xml   = arquivo
            self.vAliqProd.xml = arquivo

    xml = property(get_xml, set_xml)


class PISST(XMLNFe):
    def __init__(self):
        super(PISST, self).__init__()
        self.vBC       = TagDecimal(nome=u'vBC'      , codigo=u'R02', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/PIS/PISST')
        self.pPIS      = TagDecimal(nome=u'pPIS'     , codigo=u'R03', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/PIS/PISST')
        self.qBCProd   = TagDecimal(nome=u'qBCProd'  , codigo=u'R04', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz=u'//det/imposto/PIS/PISST')
        self.vAliqProd = TagDecimal(nome=u'vAliqProd', codigo=u'R05', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz=u'//det/imposto/PIS/PISST')
        self.vPIS      = TagDecimal(nome=u'vPIS'     , codigo=u'R06', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/PIS/PISST')

    def get_xml(self):
        if not (self.vBC.valor or self.pPIS.valor or self.qBCProd.valor or self.vAliqProd.valor or self.vPIS.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<PISST>'

        if self.qBCProd.valor or self.vAliqProd.valor:
            xml += self.qBCProd.xml
            xml += self.vAliqProd.xml
        else:
            xml += self.vBC.xml
            xml += self.pPIS.xml

        xml += self.vPIS.xml
        xml += u'</PISST>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml       = arquivo
            self.pPIS.xml      = arquivo
            self.qBCProd.xml   = arquivo
            self.vAliqProd.xml = arquivo
            self.vPIS.xml      = arquivo

    xml = property(get_xml, set_xml)


class TagCSTPIS(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagCSTPIS, self).__init__(*args, **kwargs)
        self.nome = u'CST'
        self.codigo = u'Q06'
        self.tamanho = [2, 2]
        self.raiz = u''
        self.grupo_pis = None

    def set_valor(self, novo_valor):
        super(TagCSTPIS, self).set_valor(novo_valor)

        if not self.grupo_pis:
            return None

        #
        # Definimos todas as tags como não obrigatórias
        #
        self.grupo_pis.vBC.obrigatorio       = False
        self.grupo_pis.pPIS.obrigatorio      = False
        self.grupo_pis.vPIS.obrigatorio      = False
        self.grupo_pis.qBCProd.obrigatorio   = False
        self.grupo_pis.vAliqProd.obrigatorio = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo PIS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_pis.vBC.valor       = u'0.00'
        self.grupo_pis.pPIS.valor      = u'0.00'
        self.grupo_pis.vPIS.valor      = u'0.00'
        self.grupo_pis.qBCProd.valor   = u'0.00'
        self.grupo_pis.vAliqProd.valor = u'0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de PIS
        #
        if self.valor in (u'01', u'02'):
            self.grupo_pis.nome_tag = u'PISAliq'
            self.grupo_pis.raiz_tag = u'//det/imposto/PIS/PISAliq'
            self.grupo_pis.vBC.obrigatorio       = True
            self.grupo_pis.pPIS.obrigatorio      = True
            self.grupo_pis.vPIS.obrigatorio      = True
            #self.grupo_pis.qBCProd.obrigatorio   = True
            #self.grupo_pis.vAliqProd.obrigatorio = True

        elif self.valor == u'03':
            self.grupo_pis.nome_tag = u'PISQtde'
            self.grupo_pis.raiz_tag = u'//det/imposto/PIS/PISQtde'
            #self.grupo_pis.vBC.obrigatorio       = True
            #self.grupo_pis.pPIS.obrigatorio      = True
            self.grupo_pis.vPIS.obrigatorio      = True
            self.grupo_pis.qBCProd.obrigatorio   = True
            self.grupo_pis.vAliqProd.obrigatorio = True

        elif self.valor == u'99':
            self.grupo_pis.nome_tag = u'PISOutr'
            self.grupo_pis.raiz_tag = u'//det/imposto/PIS/PISOutr'
            self.grupo_pis.vBC.obrigatorio       = True
            self.grupo_pis.pPIS.obrigatorio      = True
            self.grupo_pis.vPIS.obrigatorio      = True
            self.grupo_pis.qBCProd.obrigatorio   = True
            self.grupo_pis.vAliqProd.obrigatorio = True

        else:
            self.grupo_pis.nome_tag = u'PISNT'
            self.grupo_pis.raiz_tag = u'//det/imposto/PIS/PISNT'
            #self.grupo_pis.vBC.obrigatorio       = True
            #self.grupo_pis.pPIS.obrigatorio      = True
            #self.grupo_pis.vPIS.obrigatorio      = True
            #self.grupo_pis.qBCProd.obrigatorio   = True
            #self.grupo_pis.vAliqProd.obrigatorio = True

        #
        # Redefine a raiz para todas as tags do grupo PIS
        #
        self.grupo_pis.CST.raiz       = self.grupo_pis.raiz_tag
        self.grupo_pis.vBC.raiz       = self.grupo_pis.raiz_tag
        self.grupo_pis.pPIS.raiz      = self.grupo_pis.raiz_tag
        self.grupo_pis.vPIS.raiz      = self.grupo_pis.raiz_tag
        self.grupo_pis.qBCProd.raiz   = self.grupo_pis.raiz_tag
        self.grupo_pis.vAliqProd.raiz = self.grupo_pis.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class PIS(XMLNFe):
    def __init__(self):
        super(PIS, self).__init__()
        self.nome_tag = u'PISAliq'
        self.raiz_tag = u'//det/imposto/PIS/PISAliq'

        self.vBC       = TagDecimal(nome=u'vBC'      , codigo=u'Q07', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.pPIS      = TagDecimal(nome=u'pPIS'     , codigo=u'Q08', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'')
        self.vPIS      = TagDecimal(nome=u'vPIS'     , codigo=u'Q09', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.qBCProd   = TagDecimal(nome=u'qBCProd'  , codigo=u'Q10', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz=u'')
        self.vAliqProd = TagDecimal(nome=u'vAliqProd', codigo=u'Q11', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz=u'')

        self.CST      = TagCSTPIS()
        self.CST.grupo_pis = self
        self.CST.valor = u'07'

    def get_xml(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += u'<PIS>'
        xml += '<' + self.nome_tag + u'>'
        xml += self.CST.xml

        if self.CST.valor in (u'01', u'02'):
            xml += self.vBC.xml
            xml += self.pPIS.xml
            xml += self.vPIS.xml

        elif self.CST.valor == u'03':
            xml += self.qBCProd.xml
            xml += self.vAliqProd.xml
            xml += self.vPIS.xml

        elif self.CST.valor != u'99':
            pass

        else:
            if self.qBCProd.valor or self.vAliqProd.valor:
                xml += self.qBCProd.xml
                xml += self.vAliqProd.xml
            else:
                xml += self.vBC.xml
                xml += self.pPIS.xml
            xml += self.vPIS.xml

        xml += u'</' + self.nome_tag + u'></PIS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o PIS, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            if self._le_noh(u'//det/imposto/PIS/PISAliq') is not None:
                self.CST.valor = u'01'
            elif self._le_noh(u'//det/imposto/PIS/PISQtde') is not None:
                self.CST.valor = u'03'
            elif self._le_noh(u'//det/imposto/PIS/PISNT') is not None:
                self.CST.valor = u'04'
            else:
                self.CST.valor = u'99'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            self.CST.xml       = arquivo
            self.vBC.xml       = arquivo
            self.pPIS.xml      = arquivo
            self.vPIS.xml      = arquivo
            self.qBCProd.xml   = arquivo
            self.vAliqProd.xml = arquivo

    xml = property(get_xml, set_xml)


class II(XMLNFe):
    def __init__(self):
        super(II, self).__init__()
        self.vBC      = TagDecimal(nome=u'vBC'     , codigo=u'P02', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/II')
        self.vDespAdu = TagDecimal(nome=u'vDespAdu', codigo=u'P03', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/II')
        self.vII      = TagDecimal(nome=u'vII'     , codigo=u'P04', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/II')
        self.vIOF     = TagDecimal(nome=u'vIOF'    , codigo=u'P05', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/imposto/II')

    def get_xml(self):
        if not (self.vBC.valor or self.vDespAdu.valor or self.vII.valor or self.vIOF.valor):
            return u''

        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += u'<II>'
        xml += self.vBC.xml
        xml += self.vDespAdu.xml
        xml += self.vII.xml
        xml += self.vIOF.xml
        xml += u'</II>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml      = arquivo
            self.vDespAdu.xml = arquivo
            self.vII.xml      = arquivo
            self.vIOF.xml     = arquivo

    xml = property(get_xml, set_xml)


class TagCSTIPI(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagCSTIPI, self).__init__(*args, **kwargs)
        self.nome = u'CST'
        self.codigo = u'O09'
        self.tamanho = [2, 2]
        self.raiz = u''
        self.grupo_ipi = None

    def set_valor(self, novo_valor):
        super(TagCSTIPI, self).set_valor(novo_valor)

        if not self.grupo_ipi:
            return None

        #
        # Definimos todas as tags como não obrigatórias
        #
        self.grupo_ipi.vBC.obrigatorio   = False
        self.grupo_ipi.qUnid.obrigatorio = False
        self.grupo_ipi.vUnid.obrigatorio = False
        self.grupo_ipi.pIPI.obrigatorio  = False
        self.grupo_ipi.vIPI.obrigatorio  = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo IPI ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_ipi.vBC.valor   = u'0.00'
        self.grupo_ipi.qUnid.valor = u'0.00'
        self.grupo_ipi.vUnid.valor = u'0.00'
        self.grupo_ipi.pIPI.valor  = u'0.00'
        self.grupo_ipi.vIPI.valor  = u'0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de IPI
        #
        if self.valor in (u'00', u'49', u'50', u'99'):
            self.grupo_ipi.nome_tag = u'IPITrib'
            self.grupo_ipi.raiz_tag = u'//det/imposto/IPI/IPITrib'
            self.grupo_ipi.vBC.obrigatorio   = True
            self.grupo_ipi.qUnid.obrigatorio = True
            self.grupo_ipi.vUnid.obrigatorio = True
            self.grupo_ipi.pIPI.obrigatorio  = True
            self.grupo_ipi.vIPI.obrigatorio  = True

        else:
            self.grupo_ipi.nome_tag = u'IPINT'
            self.grupo_ipi.raiz_tag = u'//det/imposto/IPI/IPINT'

        #
        # Redefine a raiz para todas as tags do grupo IPI
        #
        self.grupo_ipi.CST.raiz   = self.grupo_ipi.raiz_tag
        self.grupo_ipi.vBC.raiz   = self.grupo_ipi.raiz_tag
        self.grupo_ipi.qUnid.raiz = self.grupo_ipi.raiz_tag
        self.grupo_ipi.vUnid.raiz = self.grupo_ipi.raiz_tag
        self.grupo_ipi.pIPI.raiz  = self.grupo_ipi.raiz_tag
        self.grupo_ipi.vIPI.raiz  = self.grupo_ipi.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class IPI(XMLNFe):
    def __init__(self):
        super(IPI, self).__init__()
        self.nome_tag = u'IPITrib'
        self.raiz_tag = u'//det/imposto/IPI/IPITrib'

        self.clEnq    = TagCaracter(nome=u'clEnq'   , codigo=u'O02', tamanho=[ 5,  5], raiz=u'//det/imposto/IPI', obrigatorio=False)
        self.CNPJProd = TagCaracter(nome=u'CNPJProd', codigo=u'O03', tamanho=[14, 14], raiz=u'//det/imposto/IPI', obrigatorio=False)
        self.cSelo    = TagCaracter(nome=u'cSelo'   , codigo=u'O04', tamanho=[ 1, 60], raiz=u'//det/imposto/IPI', obrigatorio=False)
        self.qSelo    = TagInteiro(nome=u'qSelo'    , codigo=u'O05', tamanho=[ 1, 12], raiz=u'//det/imposto/IPI', obrigatorio=False)
        self.cEnq     = TagCaracter(nome=u'cEnq'    , codigo=u'O06', tamanho=[ 3,  3], raiz=u'//det/imposto/IPI', valor=u'999')

        self.vBC      = TagDecimal(nome=u'vBC'      , codigo=u'O10', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.qUnid    = TagDecimal(nome=u'qUnid'    , codigo=u'O11', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz=u'')
        self.vUnid    = TagDecimal(nome=u'vUnid'    , codigo=u'O12', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz=u'')
        self.pIPI     = TagDecimal(nome=u'pIPI'     , codigo=u'O13', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'')
        self.vIPI     = TagDecimal(nome=u'vIPI'     , codigo=u'O13', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')

        self.CST      = TagCSTIPI()
        self.CST.grupo_ipi = self
        self.CST.valor = u'52'

    def get_xml(self):
        if not ((self.CST.valor in (u'00', u'49', u'50', u'99')) or
           (self.qUnid.valor or self.vUnid.valor or self.vBC.valor or self.pIPI.valor or self.vIPI.valor)):
            return u''

        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += u'<IPI>'
        xml += self.clEnq.xml
        xml += self.CNPJProd.xml
        xml += self.cSelo.xml
        xml += self.qSelo.xml
        xml += self.cEnq.xml

        xml += '<' + self.nome_tag + u'>'
        xml += self.CST.xml

        if self.CST.valor in (u'00', u'49', u'50', u'99'):
            if self.qUnid.valor or self.vUnid.valor:
                xml += self.qUnid.xml
                xml += self.vUnid.xml
            else:
                xml += self.vBC.xml
                xml += self.pIPI.xml
            xml += self.vIPI.xml

        xml += u'</' + self.nome_tag + u'></IPI>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o IPI, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            if self._le_noh(u'//det/imposto/IPI/IPINT') is not None:
                self.CST.valor = u'01'
            else:
                self.CST.valor = u'00'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            self.CST.xml      = arquivo
            self.vBC.xml      = arquivo

    xml = property(get_xml, set_xml)


class TagCSTICMS(TagCaracter):
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
        self.grupo_icms.modBC.obrigatorio    = False
        self.grupo_icms.vBC.obrigatorio      = False
        self.grupo_icms.pRedBC.obrigatorio   = False
        self.grupo_icms.pICMS.obrigatorio    = False
        self.grupo_icms.vICMS.obrigatorio    = False
        self.grupo_icms.modBCST.obrigatorio  = False
        self.grupo_icms.pMVAST.obrigatorio   = False
        self.grupo_icms.pRedBCST.obrigatorio = False
        self.grupo_icms.vBCST.obrigatorio    = False
        self.grupo_icms.pICMSST.obrigatorio  = False
        self.grupo_icms.vICMSST.obrigatorio  = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo ICMS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_icms.modBC.valor    = 3
        self.grupo_icms.vBC.valor      = u'0.00'
        self.grupo_icms.pRedBC.valor   = u'0.00'
        self.grupo_icms.pICMS.valor    = u'0.00'
        self.grupo_icms.vICMS.valor    = u'0.00'
        self.grupo_icms.modBCST.valor  = 4
        self.grupo_icms.pMVAST.valor   = u'0.00'
        self.grupo_icms.pRedBCST.valor = u'0.00'
        self.grupo_icms.vBCST.valor    = u'0.00'
        self.grupo_icms.pICMSST.valor  = u'0.00'
        self.grupo_icms.vICMSST.valor  = u'0.00'

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
            self.grupo_icms.nome_tag = u'ICMS10'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS10'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

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
            self.grupo_icms.nome_tag = u'ICMS40'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS40'

        elif self.valor == u'51':
            self.grupo_icms.nome_tag = u'ICMS51'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS51'

        elif self.valor == u'60':
            self.grupo_icms.nome_tag = u'ICMS60'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS60'
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.vICMSST.obrigatorio  = True

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
            self.grupo_icms.nome_tag = u'ICMS90'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS90'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

        #
        # Redefine a raiz para todas as tags do grupo ICMS
        #
        self.grupo_icms.orig.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.CST.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.modBC.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vBC.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBC.raiz   = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMS.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMS.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.modBCST.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.pMVAST.raiz   = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBCST.raiz = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCST.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMSST.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSST.raiz  = self.grupo_icms.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class ICMS(XMLNFe):
    def __init__(self):
        super(ICMS, self).__init__()
        self.nome_tag = u'ICMS00'
        self.raiz_tag = u'//det/imposto/ICMS/ICMS00'
        self.orig     = TagInteiro(nome=u'orig'    , codigo=u'N11', tamanho=[1,  1, 1],                     raiz=u'')
        #                                            codigo=u'N12' é o campo CST
        self.modBC    = TagInteiro(nome=u'modBC'   , codigo=u'N13', tamanho=[1,  1, 1],                     raiz=u'')
        self.pRedBC   = TagDecimal(nome=u'pRedBC'  , codigo=u'N14', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'')
        self.vBC      = TagDecimal(nome=u'vBC'     , codigo=u'N15', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.pICMS    = TagDecimal(nome=u'pICMS'   , codigo=u'N16', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'')
        self.vICMS    = TagDecimal(nome=u'vICMS'   , codigo=u'N17', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.modBCST  = TagInteiro(nome=u'modBCST' , codigo=u'N18', tamanho=[1,  1, 1],                     raiz=u'')
        self.pMVAST   = TagDecimal(nome=u'pMVAST'  , codigo=u'N19', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'')
        self.pRedBCST = TagDecimal(nome=u'pRedBCST', codigo=u'N20', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'')
        self.vBCST    = TagDecimal(nome=u'vBCST'   , codigo=u'N21', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')
        self.pICMSST  = TagDecimal(nome=u'pICMSST' , codigo=u'N22', tamanho=[1,  5, 1], decimais=[0, 2, 2], raiz=u'')
        self.vICMSST  = TagDecimal(nome=u'vICMSST' , codigo=u'N23', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'')

        self.CST      = TagCSTICMS()
        self.CST.grupo_icms = self
        self.CST.valor = u'40'

    def get_xml(self):
        #
        # Define as tags baseado no código da situação tributária
        #
        xml = XMLNFe.get_xml(self)
        xml += u'<ICMS><' + self.nome_tag + u'>'
        xml += self.orig.xml
        xml += self.CST.xml

        if self.CST.valor == u'00':
            xml += self.modBC.xml
            xml += self.vBC.xml
            xml += self.pICMS.xml
            xml += self.vICMS.xml

        elif self.CST.valor == u'10':
            xml += self.modBC.xml
            xml += self.vBC.xml
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
            pass

        elif self.CST.valor == u'51':
            xml += self.modBC.xml
            xml += self.pRedBC.xml
            xml += self.vBC.xml
            xml += self.pICMS.xml
            xml += self.vICMS.xml

        elif self.CST.valor == u'60':
            xml += self.vBCST.xml
            xml += self.vICMSST.xml

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

        xml += u'</' + self.nome_tag + u'></ICMS>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            #
            # Para ler corretamente o ICMS, primeiro temos que descobrir em
            # qual grupo de situação tributária ele está
            #
            if self._le_noh(u'//det/imposto/ICMS/ICMS00') is not None:
                self.CST.valor = u'00'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS10') is not None:
                self.CST.valor = u'10'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS20') is not None:
                self.CST.valor = u'20'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS30') is not None:
                self.CST.valor = u'30'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS40') is not None:
                self.CST.valor = u'40'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS51') is not None:
                self.CST.valor = u'51'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS60') is not None:
                self.CST.valor = u'60'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS70') is not None:
                self.CST.valor = u'70'
            elif self._le_noh(u'//det/imposto/ICMS/ICMS90') is not None:
                self.CST.valor = u'90'

            #
            # Agora podemos ler os valores tranquilamente...
            #
            self.orig.xml     = arquivo
            self.CST.xml      = arquivo
            self.modBC.xml    = arquivo
            self.vBC.xml      = arquivo
            self.pRedBC.xml   = arquivo
            self.pICMS.xml    = arquivo
            self.vICMS.xml    = arquivo
            self.modBCST.xml  = arquivo
            self.pMVAST.xml   = arquivo
            self.pRedBCST.xml = arquivo
            self.vBCST.xml    = arquivo
            self.pICMSST.xml  = arquivo
            self.vICMSST.xml  = arquivo

    xml = property(get_xml, set_xml)


class Imposto(XMLNFe):
    def __init__(self):
        super(Imposto, self).__init__()
        self.ICMS     = ICMS()
        self.IPI      = IPI()
        self.II       = II()
        self.PIS      = PIS()
        self.PISST    = PISST()
        self.COFINS   = COFINS()
        self.COFINSST = COFINSST()
        self.ISSQN    = ISSQN()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<imposto>'
        xml += self.ICMS.xml
        xml += self.IPI.xml
        xml += self.II.xml
        xml += self.PIS.xml
        xml += self.PISST.xml
        xml += self.COFINS.xml
        xml += self.COFINSST.xml
        xml += self.ISSQN.xml
        xml += u'</imposto>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ICMS.xml     = arquivo
            self.IPI.xml      = arquivo
            self.II.xml       = arquivo
            self.PIS.xml      = arquivo
            self.PISST.xml    = arquivo
            self.COFINS.xml   = arquivo
            self.COFINSST.xml = arquivo
            self.ISSQN.xml    = arquivo

    xml = property(get_xml, set_xml)


class ICMSCons(XMLNFe):
    def __init__(self):
        super(ICMSCons, self).__init__()
        self.vBCICMSSTCons = TagDecimal(nome=u'vBCICMSSTCons', codigo=u'L118', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/prod/comb/ICMSCons')
        self.vICMSSTCons   = TagDecimal(nome=u'vICMSSTCons'  , codigo=u'L119', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/prod/comb/ICMSCons')
        self.UFcons        = TagCaracter(nome=u'UFcons'      , codigo=u'L120', tamanho=[2,  2],                        raiz=u'//det/prod/comb/ICMSCons')

    def get_xml(self):
        if not (self.vBCICMSSTCons.valor or self.vICMSSTCons.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<ICMSCons>'
        xml += self.vBCICMSSTCons.xml
        xml += self.vICMSSTCons.xml
        xml += self.UFcons.xml
        xml += u'</ICMSCons>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBCICMSSTCons.xml = arquivo
            self.vICMSSTCons.xml   = arquivo
            self.UFcons.xml        = arquivo

    xml = property(get_xml, set_xml)


class ICMSInter(XMLNFe):
    def __init__(self):
        super(ICMSInter, self).__init__()
        self.vBCICMSSTDest = TagDecimal(nome=u'vBCICMSSTDest', codigo=u'L115', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/prod/comb/ICMSInter')
        self.vICMSSTDest   = TagDecimal(nome=u'vICMSSTDest'  , codigo=u'L116', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/prod/comb/ICMSInter')

    def get_xml(self):
        if not (self.vBCICMSSTDest.valor or self.vICMSSTDest.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<ICMSInter>'
        xml += self.vBCICMSSTDest.xml
        xml += self.vICMSSTDest.xml
        xml += u'</ICMSInter>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBCICMSSTDest.xml = arquivo
            self.vICMSSTDest.xml   = arquivo

    xml = property(get_xml, set_xml)


class ICMSComb(XMLNFe):
    def __init__(self):
        super(ICMSComb, self).__init__()
        self.vBCICMS   = TagDecimal(nome=u'vBCICMS'  , codigo=u'L110', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/prod/comb/ICMSComb')
        self.vICMS     = TagDecimal(nome=u'vICMS'    , codigo=u'L111', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/prod/comb/ICMSComb')
        self.vBCICMSST = TagDecimal(nome=u'vBCICMSST', codigo=u'L112', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/prod/comb/ICMSComb')
        self.vICMSST   = TagDecimal(nome=u'vICMSST'  , codigo=u'L113', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//det/prod/comb/ICMSComb')

    def get_xml(self):
        if not (self.vBCICMS.valor or self.vICMS.valor or self.vBCICMSST.valor or self.vICMSST.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<ICMSComb>'
        xml += self.vBCICMS.xml
        xml += self.vICMS.xml
        xml += self.vBCICMSST.xml
        xml += self.vICMSST.xml
        xml += u'</ICMSComb>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBCICMS.xml   = arquivo
            self.vICMS.xml     = arquivo
            self.vBCICMSST.xml = arquivo
            self.vICMSST.xml   = arquivo

    xml = property(get_xml, set_xml)


class CIDE(XMLNFe):
    def __init__(self):
        super(CIDE, self).__init__()
        self.qBCProd   = TagDecimal(nome=u'qBCProd'  , codigo=u'L106', tamanho=[1, 16]  , decimais=[0, 4, 4], raiz=u'//det/prod/comb/CIDE')
        self.vAliqProd = TagDecimal(nome=u'vAliqProd', codigo=u'L107', tamanho=[1, 15]  , decimais=[0, 4, 4], raiz=u'//det/prod/comb/CIDE')
        self.vCIDE     = TagDecimal(nome=u'vCIDE'    , codigo=u'L108', tamanho=[1, 15]  , decimais=[0, 2, 2], raiz=u'//det/prod/comb/CIDE')

    def get_xml(self):
        if not (self.qBCProd.valor or self.vAliqProd.valor or self.vCIDE.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<CIDE>'
        xml += self.qBCProd.xml
        xml += self.vAliqProd.xml
        xml += self.vCIDE.xml
        xml += u'</CIDE>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.qBCProd.xml   = arquivo
            self.vAliqProd.xml = arquivo
            self.vCIDE.xml     = arquivo

    xml = property(get_xml, set_xml)


class Comb(XMLNFe):
    def __init__(self):
        super(Comb, self).__init__()
        self.cProdANP  = TagInteiro(nome=u'cProdANP', codigo=u'L102', tamanho=[9,  9, 9],                     raiz=u'//det/prod/comb')
        self.CODIF     = TagInteiro(nome=u'CODIF'   , codigo=u'L103', tamanho=[0, 21]   ,                     raiz=u'//det/prod/comb', obrigatorio=False)
        self.qTemp     = TagDecimal(nome=u'qTemp'   , codigo=u'L104', tamanho=[1, 16, 1], decimais=[0, 4, 4], raiz=u'//det/prod/comb', obrigatorio=False)
        self.CIDE      = CIDE()
        self.ICMSComb  = ICMSComb()
        self.ICMSInter = ICMSInter()
        self.ICMSCons  = ICMSCons()

    def get_xml(self):
        if not self.cProdANP.valor:
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<comb>'
        xml += self.cProdANP.xml
        xml += self.CODIF.xml
        xml += self.qTemp.xml
        xml += self.CIDE.xml
        xml += self.ICMSComb.xml
        xml += self.ICMSInter.xml
        xml += self.ICMSCons.xml
        xml += u'</comb>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cProdANP.xml  = arquivo
            self.CODIF.xml     = arquivo
            self.qTemp.xml     = arquivo
            self.CIDE.xml      = arquivo
            self.ICMSComb.xml  = arquivo
            self.ICMSInter.xml = arquivo
            self.ICMSCons.xml  = arquivo

    xml = property(get_xml, set_xml)


class Arma(XMLNFe):
    def __init__(self):
        super(Arma, self).__init__()
        self.tpArma = TagInteiro(nome=u'tpArma', codigo=u'L02', tamanho=[1,   1], raiz=u'//arma')
        self.nSerie = TagInteiro(nome=u'nSerie', codigo=u'L03', tamanho=[1,   9], raiz=u'//arma')
        self.nCano  = TagInteiro(nome=u'nCano',  codigo=u'L04', tamanho=[1,   9], raiz=u'//arma')
        self.descr  = TagCaracter(nome=u'descr', codigo=u'L05', tamanho=[1, 256], raiz=u'//arma')

    def get_xml(self):
        if not self.nSerie:
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<arma>'
        xml += self.tpArma.xml
        xml += self.nSerie.xml
        xml += self.nCano.xml
        xml += self.descr.xml
        xml += u'</arma>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpArma.xml = arquivo
            self.nSerie.xml = arquivo
            self.nCano.xml  = arquivo
            self.descr.xml  = arquivo

    xml = property(get_xml, set_xml)


class Med(XMLNFe):
    def __init__(self):
        super(Med, self).__init__()
        self.nLote = TagCaracter(nome=u'nLote', codigo=u'K02', tamanho=[1, 20]                    , raiz=u'//med')
        self.qLote = TagDecimal(nome=u'qLote' , codigo=u'K03', tamanho=[1, 11], decimais=[0, 3, 3], raiz=u'//med')
        self.dFab  = TagData(nome=u'dFab'     , codigo=u'K04'                                     , raiz=u'//med')
        self.dVal  = TagData(nome=u'dVal'     , codigo=u'K05'                                     , raiz=u'//med')
        self.vPMC  = TagDecimal(nome=u'vPMC'  , codigo=u'K06', tamanho=[1, 15], decimais=[0, 2, 2], raiz=u'//med')

    def get_xml(self):
        if not self.nLote.valor:
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<med>'
        xml += self.nLote.xml
        xml += self.qLote.xml
        xml += self.dFab.xml
        xml += self.dVal.xml
        xml += self.vPMC.xml
        xml += u'</med>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nLote.xml = arquivo
            self.qLote.xml = arquivo
            self.dFab.xml  = arquivo
            self.dVal.xml  = arquivo
            self.vPMC.xml  = arquivo

    xml = property(get_xml, set_xml)


class VeicProd(XMLNFe):
    def __init__(self):
        super(VeicProd, self).__init__()
        self.tpOp     = TagInteiro(nome=u'tpOp'    , codigo=u'J02', tamanho=[ 1,  1, 1], raiz=u'//det/prod/veicProd')
        self.chassi   = TagCaracter(nome=u'chassi' , codigo=u'J03', tamanho=[ 1, 17]   , raiz=u'//det/prod/veicProd')
        self.cCor     = TagCaracter(nome=u'cCor'   , codigo=u'J04', tamanho=[ 1,  4]   , raiz=u'//det/prod/veicProd')
        self.xCor     = TagCaracter(nome=u'xCor'   , codigo=u'J05', tamanho=[ 1, 40]   , raiz=u'//det/prod/veicProd')
        self.pot      = TagCaracter(nome=u'pot'    , codigo=u'J06', tamanho=[ 1,  4]   , raiz=u'//det/prod/veicProd')
        self.CM3      = TagCaracter(nome=u'CM3'    , codigo=u'J07', tamanho=[ 1,  4]   , raiz=u'//det/prod/veicProd')
        self.pesoL    = TagCaracter(nome=u'pesoL'  , codigo=u'J08', tamanho=[ 1,  9]   , raiz=u'//det/prod/veicProd')
        self.pesoB    = TagCaracter(nome=u'pesoB'  , codigo=u'J09', tamanho=[ 1,  9]   , raiz=u'//det/prod/veicProd')
        self.nSerie   = TagCaracter(nome=u'nSerie' , codigo=u'J10', tamanho=[ 1,  9]   , raiz=u'//det/prod/veicProd')
        self.tpComb   = TagCaracter(nome=u'tpComb' , codigo=u'J11', tamanho=[ 1,  8]   , raiz=u'//det/prod/veicProd')
        self.nMotor   = TagCaracter(nome=u'nMotor' , codigo=u'J12', tamanho=[ 1, 21]   , raiz=u'//det/prod/veicProd')
        self.CMKG     = TagCaracter(nome=u'CMKG'   , codigo=u'J13', tamanho=[ 1,  9]   , raiz=u'//det/prod/veicProd')
        self.dist     = TagCaracter(nome=u'dist'   , codigo=u'J14', tamanho=[ 1,  4]   , raiz=u'//det/prod/veicProd')
        self.RENAVAM  = TagCaracter(nome=u'RENAVAM', codigo=u'J15', tamanho=[ 1,  9]   , raiz=u'//det/prod/veicProd', obrigatorio=False)
        self.anoMod   = TagInteiro(nome=u'anoMod'  , codigo=u'J16', tamanho=[ 4,  4, 4], raiz=u'//det/prod/veicProd')
        self.anoFab   = TagInteiro(nome=u'anoFab'  , codigo=u'J17', tamanho=[ 4,  4, 4], raiz=u'//det/prod/veicProd')
        self.tpPint   = TagCaracter(nome=u'tpPint' , codigo=u'J18', tamanho=[ 1,  1]   , raiz=u'//det/prod/veicProd')
        self.tpVeic   = TagInteiro(nome=u'tpVeic'  , codigo=u'J19', tamanho=[ 2,  2, 2], raiz=u'//det/prod/veicProd')
        self.espVeic  = TagInteiro(nome=u'espVeic' , codigo=u'J20', tamanho=[ 1,  1]   , raiz=u'//det/prod/veicProd')
        self.VIN      = TagCaracter(nome=u'VIN'    , codigo=u'J21', tamanho=[ 1,  1]   , raiz=u'//det/prod/veicProd')
        self.condVeic = TagInteiro(nome=u'condVeic', codigo=u'J22', tamanho=[ 1,  1]   , raiz=u'//det/prod/veicProd')
        self.cMod     = TagInteiro(nome=u'cMod'    , codigo=u'J23', tamanho=[ 6,  6, 6], raiz=u'//det/prod/veicProd')

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
        xml += self.CM3.xml
        xml += self.pesoL.xml
        xml += self.pesoB.xml
        xml += self.nSerie.xml
        xml += self.tpComb.xml
        xml += self.nMotor.xml
        xml += self.CMKG.xml
        xml += self.dist.xml
        xml += self.RENAVAM.xml
        xml += self.anoMod.xml
        xml += self.anoFab.xml
        xml += self.tpPint.xml
        xml += self.tpVeic.xml
        xml += self.espVeic.xml
        xml += self.VIN.xml
        xml += self.condVeic.xml
        xml += self.cMod.xml
        xml += u'</veicProd>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpOp.xml     = arquivo
            self.chassi.xml   = arquivo
            self.cCor.xml     = arquivo
            self.xCor.xml     = arquivo
            self.pot.xml      = arquivo
            self.CM3.xml      = arquivo
            self.pesoL.xml    = arquivo
            self.pesoB.xml    = arquivo
            self.nSerie.xml   = arquivo
            self.tpComb.xml   = arquivo
            self.nMotor.xml   = arquivo
            self.CMKG.xml     = arquivo
            self.dist.xml     = arquivo
            self.RENAVAM.xml  = arquivo
            self.anoMod.xml   = arquivo
            self.anoFab.xml   = arquivo
            self.tpPint.xml   = arquivo
            self.tpVeic.xml   = arquivo
            self.espVeic.xml  = arquivo
            self.VIN.xml      = arquivo
            self.condVeic.xml = arquivo
            self.cMod.xml     = arquivo

    xml = property(get_xml, set_xml)


class Adi(XMLNFe):
    def __init__(self):
        super(Adi, self).__init__()
        self.nAdicao     = TagInteiro(nome=u'nAdicao'     , codigo=u'I26', tamanho=[1,  3],                     raiz=u'//adi')
        self.nSeqAdic    = TagInteiro(nome=u'nSeqAdic'    , codigo=u'I27', tamanho=[1,  3],                     raiz=u'//adi')
        self.cFabricante = TagCaracter(nome=u'cFabricante', codigo=u'I28', tamanho=[1, 60],                     raiz=u'//adi')
        self.vDescDI     = TagDecimal(nome=u'vDescDI'     , codigo=u'I29', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//adi', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<adi>'
        xml += self.nAdicao.xml
        xml += self.nSeqAdic.xml
        xml += self.cFabricante.xml
        xml += self.vDescDI.xml
        xml += u'</adi>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nAdicao.xml  = arquivo
            self.nSeqAdic.xml = arquivo
            self.cFabricante  = arquivo
            self.vDescDI      = arquivo

    xml = property(get_xml, set_xml)


class DI(XMLNFe):
    def __init__(self):
        super(DI, self).__init__()
        self.nDI         = TagCaracter(nome=u'nDI'        , codigo=u'I19', tamanho=[1, 10], raiz=u'//DI')
        self.dDI         = TagData(nome=u'dDI'            , codigo=u'I20',                  raiz=u'//DI')
        self.xLocDesemb  = TagCaracter(nome=u'xLocDesemb' , codigo=u'I21', tamanho=[1, 60], raiz=u'//DI')
        self.UFDesemb    = TagCaracter(nome=u'UFDesemb'   , codigo=u'I22', tamanho=[2,  2], raiz=u'//DI')
        self.dDesemb     = TagData(nome=u'dDesemb'        , codigo=u'I23',                  raiz=u'//DI')
        self.cExportador = TagCaracter(nome=u'cExportador', codigo=u'I24', tamanho=[1, 60], raiz=u'//DI')
        self.adi         = [Adi()]

    def get_xml(self):
        if not self.nDI:
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<DI>'
        xml += self.nDI.xml
        xml += self.dDI.xml
        xml += self.xLocDesemb.xml
        xml += self.UFDesemb.xml
        xml += self.dDesemb.xml
        xml += self.cExportador.xml

        for a in self.adi:
            xml += a.xml

        xml += u'</DI>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nDI.xml     = arquivo
            self.dDI.xml     = arquivo
            self.xLocDesemb  = arquivo
            self.UFDesemb    = arquivo
            self.dDesemb     = arquivo
            self.cExportador = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            adis = self._le_nohs('//DI/adi')
            self.adi = []
            if adis is not None:
                self.adi = [_Adi() for a in adis]
                for i in range(len(adis)):
                    self.adi[i].xml = adis[i]

    xml = property(get_xml, set_xml)


class Prod(XMLNFe):
    def __init__(self):
        super(Prod, self).__init__()
        self.cProd    = TagCaracter(nome=u'cProd'   , codigo=u'I02' , tamanho=[1,  60]                       , raiz=u'//det/prod')
        self.cEAN     = TagCaracter(nome=u'cEAN'    , codigo=u'I03' , tamanho=[0,  14]                       , raiz=u'//det/prod')
        self.xProd    = TagCaracter(nome=u'xProd'   , codigo=u'I04' , tamanho=[1, 120]                       , raiz=u'//det/prod')
        self.NCM      = TagCaracter(nome=u'NCM'     , codigo=u'I05' , tamanho=[2,   8]                       , raiz=u'//det/prod', obrigatorio=False)
        self.EXTIPI   = TagCaracter(nome=u'EXTIPI'  , codigo=u'I06' , tamanho=[2,   3]                       , raiz=u'//det/prod', obrigatorio=False)
        self.genero   = TagCaracter(nome=u'genero'  , codigo=u'I07' , tamanho=[2,   2, 2]                    , raiz=u'//det/prod', obrigatorio=False)
        self.CFOP     = TagInteiro(nome=u'CFOP'     , codigo=u'I08' , tamanho=[4,   4, 4]                    , raiz=u'//det/prod')
        self.uCom     = TagCaracter(nome=u'uCom'    , codigo=u'I09' , tamanho=[1,   6]                       , raiz=u'//det/prod')
        self.qCom     = TagDecimal(nome=u'qCom'     , codigo=u'I10' , tamanho=[1,  12, 1], decimais=[0, 4, 4], raiz=u'//det/prod')
        self.vUnCom   = TagDecimal(nome=u'vUnCom'   , codigo=u'I10a', tamanho=[1,  16, 1], decimais=[0, 4, 4], raiz=u'//det/prod')
        self.vProd    = TagDecimal(nome=u'vProd'    , codigo=u'I11' , tamanho=[1,  15, 1], decimais=[0, 2, 2], raiz=u'//det/prod')
        self.cEANTrib = TagCaracter(nome=u'cEANTrib', codigo=u'I12' , tamanho=[0,  14]                       , raiz=u'//det/prod')
        self.uTrib    = TagCaracter(nome=u'uTrib'   , codigo=u'I13' , tamanho=[1,   6]                       , raiz=u'//det/prod')
        self.qTrib    = TagDecimal(nome=u'qTrib'    , codigo=u'I14' , tamanho=[1,  12, 1], decimais=[0, 4, 4], raiz=u'//det/prod')
        self.vUnTrib  = TagDecimal(nome=u'vUnTrib'  , codigo=u'I14a', tamanho=[1,  16, 1], decimais=[0, 4, 4], raiz=u'//det/prod')
        self.vTrib    = TagDecimal(nome=u'vTrib'    , codigo=u''    , tamanho=[1,  15, 1], decimais=[0, 2, 2], raiz=u'//det/prod', obrigatorio=False)
        self.vFrete   = TagDecimal(nome=u'vFrete'   , codigo=u'I15' , tamanho=[1,  15, 1], decimais=[0, 2, 2], raiz=u'//det/prod', obrigatorio=False)
        self.vSeg     = TagDecimal(nome=u'vSeg'     , codigo=u'I16' , tamanho=[1,  15, 1], decimais=[0, 2, 2], raiz=u'//det/prod', obrigatorio=False)
        self.vDesc    = TagDecimal(nome=u'vDesc'    , codigo=u'I17' , tamanho=[1,  15, 1], decimais=[0, 2, 2], raiz=u'//det/prod', obrigatorio=False)
        self.DI       = []
        self.veicProd = VeicProd()
        self.med      = []
        self.arma     = []
        self.comb     = Comb()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<prod>'
        xml += self.cProd.xml
        xml += self.cEAN.xml
        xml += self.xProd.xml
        xml += self.NCM.xml
        xml += self.EXTIPI.xml
        xml += self.genero.xml
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

        for d in self.DI:
            xml += d.xml

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


class Det(XMLNFe):
    def __init__(self):
        super(Det, self).__init__()
        self.nItem     = TagInteiro(nome=u'det'       , codigo=u'H01', tamanho=[1,   3], propriedade=u'nItem', raiz=u'/') #, namespace=NAMESPACE_NFE)
        self.prod      = Prod()
        self.imposto   = Imposto()
        self.infAdProd = TagCaracter(nome=u'infAdProd', codigo=u'V01', tamanho=[1, 500], raiz=u'//det', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.nItem.xml
        xml += self.prod.xml
        xml += self.imposto.xml
        xml += self.infAdProd.xml
        xml += u'</det>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nItem.xml     = arquivo
            self.prod.xml      = arquivo
            self.imposto.xml   = arquivo
            self.infAdProd.xml = arquivo

    xml = property(get_xml, set_xml)

    def descricao_produto_formatada(self):
        formatado = self.prod.xProd.valor.replace(u'|', u'<br />')

        if len(self.infAdProd.valor):
            formatado += u'<br />'
            formatado += self.infAdProd.valor.replace(u'|', u'<br />')

        return formatado

    def cst_formatado(self):
        formatado = unicode(self.imposto.ICMS.orig.valor).zfill(1)
        formatado += unicode(self.imposto.ICMS.CST.valor).zfill(2)
        return formatado

class Compra(XMLNFe):
    def __init__(self):
        super(Compra, self).__init__()
        self.xNEmp = TagCaracter(nome=u'xNEmp', codigo=u'ZB02', tamanho=[1, 17], raiz=u'//NFe/infNFe/compra', obrigatorio=False)
        self.xPed  = TagCaracter(nome=u'xPed' , codigo=u'ZB03', tamanho=[1, 60], raiz=u'//NFe/infNFe/compra', obrigatorio=False)
        self.xCont = TagCaracter(nome=u'xCont', codigo=u'ZB04', tamanho=[1, 60], raiz=u'//NFe/infNFe/compra', obrigatorio=False)

    def get_xml(self):
        if not (self.xNEmp.valor or self.xPed.valor or self.xCont.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<compra>'
        xml += self.xNEmp.xml
        xml += self.xPed.xml
        xml += self.xCont.xml
        xml += u'</compra>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xNEmp.xml = arquivo
            self.xPed.xml  = arquivo
            self.xCont.xml = arquivo

    xml = property(get_xml, set_xml)


class Exporta(XMLNFe):
    def __init__(self):
        super(Exporta, self).__init__()
        self.UFEmbarq   = TagCaracter(nome=u'UFEmbarq'  , codigo=u'ZA02', tamanho=[2,  2], raiz=u'//NFe/infNFe/exporta', obrigatorio=False)
        self.xLocEmbarq = TagCaracter(nome=u'xLocEmbarq', codigo=u'ZA03', tamanho=[1, 60], raiz=u'//NFe/infNFe/exporta', obrigatorio=False)

    def get_xml(self):
        if not (self.UFEmbarq.valor or self.xLocEmbarq.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<exporta>'
        xml += self.UFEmbarq.xml
        xml += self.xLocEmbarq.xml
        xml += u'</exporta>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.UFEmbarq.xml   = arquivo
            self.xLocEmbarq.xml = arquivo

    xml = property(get_xml, set_xml)


class ProcRef(XMLNFe):
    def __init__(self):
        super(ProcRef, self).__init__()
        self.nProc   = TagCaracter(nome=u'nProc' , codigo=u'Z11', tamanho=[1, 60], raiz=u'//procRef')
        self.indProc = TagInteiro(nome=u'indProc', codigo=u'Z12', tamanho=[1,  1], raiz=u'//procRef')

    def get_xml(self):
        if not (self.nProc.valor or self.indProc.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<procRef>'
        xml += self.nProc.xml
        xml += self.indProc.xml
        xml += u'</procRef>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nProc.xml = arquivo
            self.indProc.xml = arquivo

    xml = property(get_xml, set_xml)


class ObsFisco(XMLNFe):
    def __init__(self):
        super(ObsFisco, self).__init__()
        self.xCampo = TagCaracter(nome=u'xCampo', codigo=u'Z08', tamanho=[1, 20], raiz=u'//obsFisco')
        self.xTexto = TagCaracter(nome=u'xTexto', codigo=u'Z09', tamanho=[1, 60], raiz=u'//obsFisco')

    def get_xml(self):
        if not (self.xCampo.valor or self.xTexto.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<obsFisco>'
        xml += self.xCampo.xml
        xml += self.xTexto.xml
        xml += u'</obsFisco>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xCampo.xml = arquivo
            self.xTexto.xml = arquivo

    xml = property(get_xml, set_xml)


class ObsCont(XMLNFe):
    def __init__(self):
        super(ObsCont, self).__init__()
        self.xCampo = TagCaracter(nome=u'xCampo', codigo=u'Z05', tamanho=[1, 20], raiz=u'//obsCont')
        self.xTexto = TagCaracter(nome=u'xTexto', codigo=u'Z06', tamanho=[1, 60], raiz=u'//obsCont')

    def get_xml(self):
        if not (self.xCampo.valor or self.xTexto.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<obsCont>'
        xml += self.xCampo.xml
        xml += self.xTexto.xml
        xml += u'</obsCont>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xCampo.xml = arquivo
            self.xTexto.xml = arquivo

    xml = property(get_xml, set_xml)


class InfAdic(XMLNFe):
    def __init__(self):
        super(InfAdic, self).__init__()
        self.infAdFisco = TagCaracter(nome=u'infAdFisco', codigo=u'Z02', tamanho=[1,  256], raiz=u'//NFe/infNFe/infAdic', obrigatorio=False)
        self.infCpl     = TagCaracter(nome=u'infCpl'    , codigo=u'Z03', tamanho=[1, 5000], raiz=u'//NFe/infNFe/infAdic', obrigatorio=False)
        self.obsCont    = []
        self.obsFisco   = []
        self.procRef    = []

    def get_xml(self):
        if not (self.infAdFisco.valor or self.infCpl.valor or len(self.obsCont) or len(self.obsFisco) or len(self.procRef)):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<infAdic>'
        xml += self.infAdFisco.xml
        xml += self.infCpl.xml

        for o in self.obsCont:
            xml += o.xml

        for o in self.obsFisco:
            xml += o.xml

        for p in self.procRef:
            xml += p.xml

        xml += u'</infAdic>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infAdFisco.xml = arquivo
            self.infCpl.xml     = arquivo
            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.obsCont = self.le_grupo('//NFe/infNFe/infAdic/obsCont', ObsCont)
            self.obsFisco = self.le_grupo('//NFe/infNFe/infAdic/obsFisco', ObsFisco)
            self.procRef = self.le_grupo('//NFe/infNFe/infAdic/procRef', ProcRef)

    xml = property(get_xml, set_xml)


class Dup(XMLNFe):
    def __init__(self):
        super(Dup, self).__init__()
        self.nDup  = TagCaracter(nome=u'nDup', codigo=u'Y08', tamanho=[1, 60],                        raiz=u'//dup', obrigatorio=False)
        self.dVenc = TagData(nome=u'dVenc'   , codigo=u'Y09',                                         raiz=u'//dup', obrigatorio=False)
        self.vDup  = TagDecimal(nome=u'vDup' , codigo=u'Y10', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//dup', obrigatorio=False)

    def get_xml(self):
        if not (self.nDup.valor or self.dVenc.valor or self.vDup.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<dup>'
        xml += self.nDup.xml
        xml += self.dVenc.xml
        xml += self.vDup.xml
        xml += u'</dup>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nDup.xml  = arquivo
            self.dVenc.xml = arquivo
            self.vDup.xml  = arquivo

    xml = property(get_xml, set_xml)


class Fat(XMLNFe):
    def __init__(self):
        super(Fat, self).__init__()
        self.nFat  = TagCaracter(nome=u'nFat', codigo=u'Y03', tamanho=[1, 60],                        raiz=u'//NFe/infNFe/cobr/fat', obrigatorio=False)
        self.vOrig = TagDecimal(nome=u'vOrig', codigo=u'Y04', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/cobr/fat', obrigatorio=False)
        self.vDesc = TagDecimal(nome=u'vDesc', codigo=u'Y05', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/cobr/fat', obrigatorio=False)
        self.vLiq  = TagDecimal(nome=u'vLiq' , codigo=u'Y06', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/cobr/fat', obrigatorio=False)

    def get_xml(self):
        if not (self.nFat.valor or self.vOrig.valor or self.vDesc.valor or self.vLiq.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<fat>'
        xml += self.nFat.xml
        xml += self.vOrig.xml
        xml += self.vDesc.xml
        xml += self.vLiq.xml
        xml += u'</fat>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nFat.xml  = arquivo
            self.vOrig.xml = arquivo
            self.vDesc.xml = arquivo
            self.vLiq.xml  = arquivo

    xml = property(get_xml, set_xml)


class Cobr(XMLNFe):
    def __init__(self):
        super(Cobr, self).__init__()
        self.fat = Fat()
        self.dup = []

    def get_xml(self):
        if not (self.fat.xml or len(self.dup)):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<cobr>'
        xml += self.fat.xml

        for d in self.dup:
            xml += d.xml

        xml += u'</cobr>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.fat.xml  = arquivo
            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.dup = self.le_grupo('//NFe/infNFe/cobr/dup', Dup)

    xml = property(get_xml, set_xml)


class Lacres(XMLNFe):
    def __init__(self):
        super(Lacres, self).__init__()
        self.nLacre = TagCaracter(nome=u'nLacre', codigo=u'X34', tamanho=[1, 60], raiz=u'//lacres')

    def get_xml(self):
        if not self.nLacre.valor:
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<lacres>'
        xml += self.nLacre.xml
        xml += u'</lacres>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nLacre.xml = arquivo

    xml = property(get_xml, set_xml)


class Vol(XMLNFe):
    #
    # No caso dos volumes, se o valor da quantidade, peso bruto ou líquido for zero ou inexistente
    # não imprime os valores no DANFE
    #
    class TagInteiroVolume(TagInteiro):
        def formato_danfe(self):
            if not self._valor_inteiro:
                return u''
            else:
                return super(Vol.TagInteiroVolume, self).formato_danfe()

    class TagDecimalVolume(TagDecimal):
        def formato_danfe(self):
            if not self._valor_decimal:
                return u''
            else:
                return super(Vol.TagDecimalVolume, self).formato_danfe()

    def __init__(self, xml=None):
        super(Vol, self).__init__()
        self.qVol   = TagInteiro(nome=u'qVol'  , codigo=u'X27', tamanho=[1, 15], raiz=u'//vol', obrigatorio=False)
        #self.qVol   = self.TagInteiroVolume(nome=u'qVol'  , codigo=u'X27', tamanho=[1, 15], raiz=u'//vol', obrigatorio=False)
        self.esp    = TagCaracter(nome=u'esp'  , codigo=u'X28', tamanho=[1, 60], raiz=u'//vol', obrigatorio=False)
        self.marca  = TagCaracter(nome=u'marca', codigo=u'X29', tamanho=[1, 60], raiz=u'//vol', obrigatorio=False)
        self.nVol   = TagCaracter(nome=u'nVol' , codigo=u'X30', tamanho=[1, 60], raiz=u'//vol', obrigatorio=False)
        self.pesoL  = TagDecimal(nome=u'pesoL' , codiog=u'X31', tamanho=[1, 15, 1], decimais=[0, 3, 3], raiz=u'//vol', obrigatorio=False)
        self.pesoB  = TagDecimal(nome=u'pesoB' , codiog=u'X32', tamanho=[1, 15, 1], decimais=[0, 3, 3], raiz=u'//vol', obrigatorio=False)
        #self.pesoL  = self.TagDecimalVolume(nome=u'pesoL' , codiog=u'X31', tamanho=[1, 15, 1], decimais=[0, 3, 3], raiz=u'//vol', obrigatorio=False)
        #self.pesoB  = self.TagDecimalVolume(nome=u'pesoB' , codiog=u'X32', tamanho=[1, 15, 1], decimais=[0, 3, 3], raiz=u'//vol', obrigatorio=False)
        self.lacres = []

    def get_xml(self):
        if not (self.qVol.valor or self.esp.valor or self.marca.valor or self.nVol.valor or self.pesoL.valor or self.pesoB.valor or len(self.lacres.nLacre)):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<vol>'
        xml += self.qVol.xml
        xml += self.esp.xml
        xml += self.marca.xml
        xml += self.nVol.xml
        xml += self.pesoL.xml
        xml += self.pesoB.xml

        for l in self.lacres:
            xml += l.xml

        xml += u'</vol>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.qVol.xml = arquivo
            self.esp.xml = arquivo
            self.marca.xml = arquivo
            self.nVol.xml = arquivo
            self.pesoL.xml = arquivo
            self.pesoB.xml = arquivo
            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.lacres = self.le_grupo('//vol/lacres', Lacres)

    xml = property(get_xml, set_xml)


class Reboque(XMLNFe):
    def __init__(self):
        super(Reboque, self).__init__()
        self.placa = TagCaracter(nome=u'placa', codigo=u'X23', tamanho=[1,  8], raiz=u'//reboque')
        self.UF    = TagCaracter(nome=u'UF'   , codigo=u'X24', tamanho=[2,  2], raiz=u'//reboque')
        self.RNTC  = TagCaracter(nome=u'RNTC' , codigo=u'X25', tamanho=[1, 20], raiz=u'//reboque', obrigatorio=False)

    def get_xml(self):
        if not (self.placa.valor or self.UF.valor or self.RNTC.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<reboque>'
        xml += self.placa.xml
        xml += self.UF.xml
        xml += self.RNTC.xml
        xml += u'</reboque>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.placa.xml = arquivo
            self.UF.xml    = arquivo
            self.RNTC.xml  = arquivo

    xml = property(get_xml, set_xml)


class VeicTransp(XMLNFe):
    def __init__(self):
        super(VeicTransp, self).__init__()
        self.placa = TagCaracter(nome=u'placa', codigo=u'X19', tamanho=[1,  8], raiz=u'//NFe/infNFe/transp/veicTransp')
        self.UF    = TagCaracter(nome=u'UF'   , codigo=u'X20', tamanho=[2,  2], raiz=u'//NFe/infNFe/transp/veicTransp')
        self.RNTC  = TagCaracter(nome=u'RNTC' , codigo=u'X21', tamanho=[1, 20], raiz=u'//NFe/infNFe/transp/veicTransp', obrigatorio=False)

    def get_xml(self):
        if not (self.placa.valor or self.UF.valor or self.RNTC.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<veicTransp>'
        xml += self.placa.xml
        xml += self.UF.xml
        xml += self.RNTC.xml
        xml += u'</veicTransp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.placa.xml = arquivo
            self.UF.xml    = arquivo
            self.RNTC.xml  = arquivo

    xml = property(get_xml, set_xml)


class RetTransp(XMLNFe):
    def __init__(self):
        super(RetTransp, self).__init__()
        self.vServ    = TagDecimal(nome=u'vServ'   , codigo=u'X12', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/transp/retTransp')
        self.vBCRet   = TagDecimal(nome=u'vBCRet'  , codigo=u'X13', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/transp/retTransp')
        self.pICMSRet = TagDecimal(nome=u'vICMSRet', codigo=u'X14', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/transp/retTransp')
        self.vICMSRet = TagDecimal(nome=u'vICMSRet', codigo=u'X15', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/transp/retTransp')
        self.CFOP     = TagInteiro(nome=u'CFOP'    , codigo=u'X16', tamanho=[4,  4, 4],                     raiz=u'//NFe/infNFe/transp/retTransp')
        self.cMunFG   = TagInteiro(nome=u'cMunFG'  , codigo=u'X17', tamanho=[7,  7, 7],                     raiz=u'//NFe/infNFe/transp/retTransp')

    def get_xml(self):
        if not (self.vServ.valor or self.vBCRet.valor or self.pICMSRet.valor or self.vICMSRet.valor or self.CFOP.valor or self.cMunFG.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<retTransp>'
        xml += self.vServ.xml
        xml += self.vBCRet.xml
        xml += self.pICMSRet.xml
        xml += self.vICMSRet.xml
        xml += self.CFOP.xml
        xml += self.cMunFG.xml
        xml += u'</retTransp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vServ.xml    = arquivo
            self.vBCRet.xml   = arquivo
            self.pICMSRet.xml = arquivo
            self.vICMSRet.xml = arquivo
            self.CFOP.xml     = arquivo
            self.cMunFG.xml   = arquivo

    xml = property(get_xml, set_xml)


class Transporta(XMLNFe):
    def __init__(self):
        super(Transporta, self).__init__()
        self.CNPJ   = TagCaracter(nome=u'CNPJ'  , codigo=u'X04', tamanho=[14, 14], raiz=u'//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.CPF    = TagCaracter(nome=u'CPF'   , codigo=u'X05', tamanho=[11, 11], raiz=u'//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.xNome  = TagCaracter(nome=u'xNome' , codigo=u'X06', tamanho=[ 1, 60], raiz=u'//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.IE     = TagCaracter(nome=u'IE'    , codigo=u'X07', tamanho=[ 2, 14], raiz=u'//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.xEnder = TagCaracter(nome=u'xEnder', codigo=u'X08', tamanho=[ 1, 60], raiz=u'//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.xMun   = TagCaracter(nome=u'xMun'  , codigo=u'X09', tamanho=[ 1, 60], raiz=u'//NFe/infNFe/transp/transporta', obrigatorio=False)
        self.UF     = TagCaracter(nome=u'UF'    , codigo=u'X10', tamanho=[ 2,  2], raiz=u'//NFe/infNFe/transp/transporta', obrigatorio=False)

    def get_xml(self):
        if not (self.CNPJ.valor or self.CPF.valor or self.xNome.valor or self.IE.valor or self.xEnder.valor or self.xMun.valor or self.UF.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<transporta>'
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.xNome.xml
        xml += self.IE.xml
        xml += self.xEnder.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += u'</transporta>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml   = arquivo
            self.CPF.xml    = arquivo
            self.xNome.xml  = arquivo
            self.IE.xml     = arquivo
            self.xEnder.xml = arquivo
            self.xMun.xml   = arquivo
            self.UF.xml     = arquivo

    xml = property(get_xml, set_xml)


class Transp(XMLNFe):
    def __init__(self):
        super(Transp, self).__init__()
        self.modFrete   = TagInteiro(nome=u'modFrete', codigo=u'X02', tamanho=[ 1, 1, 1], raiz=u'//NFe/infNFe/transp')
        self.transporta = Transporta()
        self.retTransp  = RetTransp()
        self.veicTransp = VeicTransp()
        self.reboque    = []
        self.vol        = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<transp>'
        xml += self.modFrete.xml
        xml += self.transporta.xml
        xml += self.retTransp.xml
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
            self.reboque = self.le_grupo('//NFe/infNFe/transp/reboque', Reboque)
            self.vol = self.le_grupo('//NFe/infNFe/transp/vol', Vol)

    xml = property(get_xml, set_xml)


class RetTrib(XMLNFe):
    def __init__(self):
        super(RetTrib, self).__init__()
        self.vRetPIS    = TagDecimal(nome=u'vRetPIS'   , codigo=u'W24', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vRetCOFINS = TagDecimal(nome=u'vRetCOFINS', codigo=u'W25', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vRetCSLL   = TagDecimal(nome=u'vRetCSLL'  , codigo=u'W26', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vBCIRRF    = TagDecimal(nome=u'vBCIRRF'   , codigo=u'W27', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vIRRF      = TagDecimal(nome=u'vIRRF'     , codigo=u'W28', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vBCRetPrev = TagDecimal(nome=u'vBCRetPrev', codigo=u'W29', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/retTrib', obrigatorio=False)
        self.vRetPrev   = TagDecimal(nome=u'vRetPrev'  , codigo=u'W30', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/retTrib', obrigatorio=False)

    def get_xml(self):
        if not (self.vRetPIS.valor or self.vRetCOFINS.valor or self.vRetCSLL.valor or self.vBCIRRF.valor or self.vIRRF.valor or self.vBCRetPrev.valor or self.vRetPrev.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<retTrib>'
        xml += self.vRetPIS.xml
        xml += self.vRetCOFINS.xml
        xml += self.vRetCSLL.xml
        xml += self.vBCIRRF.xml
        xml += self.vIRRF.xml
        xml += self.vBCRetPrev.xml
        xml += self.vRetPrev.xml
        xml += u'</retTrib>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vRetPIS.xml    = arquivo
            self.vRetCOFINS.xml = arquivo
            self.vRetCSLL.xml   = arquivo
            self.vBCIRRF.xml    = arquivo
            self.vIRRF.xml      = arquivo
            self.vBCRetPrev.xml = arquivo
            self.vRetPrev.xml   = arquivo

    xml = property(get_xml, set_xml)


class ISSQNTot(XMLNFe):
    def __init__(self):
        super(ISSQNTot, self).__init__()
        self.vServ   = TagDecimal(nome=u'vServ'  , codigo=u'W18', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vBC     = TagDecimal(nome=u'vBC'    , codigo=u'W19', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vISS    = TagDecimal(nome=u'vISS'   , codigo=u'W20', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vPIS    = TagDecimal(nome=u'vPIS'   , codigo=u'W21', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vCOFINS = TagDecimal(nome=u'vCOFINS', codigo=u'W22', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ISSQNtot', obrigatorio=False)

    def get_xml(self):
        if not (self.vServ.valor or self.vBC.valor or self.vISS.valor or self.vPIS.valor or self.vCOFINS.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<ISSQNtot>'
        xml += self.vServ.xml
        xml += self.vBC.xml
        xml += self.vISS.xml
        xml += self.vPIS.xml
        xml += self.vCOFINS.xml
        xml += u'</ISSQNtot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vServ.xml   = arquivo
            self.vBC.xml     = arquivo
            self.vISS.xml    = arquivo
            self.vPIS.xml    = arquivo
            self.vCOFINS.xml = arquivo

    xml = property(get_xml, set_xml)


class ICMSTot(XMLNFe):
    def __init__(self):
        super(ICMSTot, self).__init__()
        self.vBC     = TagDecimal(nome=u'vBC'    , codigo=u'W03', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vICMS   = TagDecimal(nome=u'vICMS'  , codigo=u'W04', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vBCST   = TagDecimal(nome=u'vBCST'  , codigo=u'W05', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vST     = TagDecimal(nome=u'vST'    , codigo=u'W06', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vProd   = TagDecimal(nome=u'vProd'  , codigo=u'W07', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vFrete  = TagDecimal(nome=u'vFrete' , codigo=u'W08', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vSeg    = TagDecimal(nome=u'vSeg'   , codigo=u'W09', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vDesc   = TagDecimal(nome=u'vDesc'  , codigo=u'W10', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vII     = TagDecimal(nome=u'vII'    , codigo=u'W11', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vIPI    = TagDecimal(nome=u'vIPI'   , codigo=u'W12', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vPIS    = TagDecimal(nome=u'vPIS'   , codigo=u'W13', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vCOFINS = TagDecimal(nome=u'vCOFINS', codigo=u'W14', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vOutro  = TagDecimal(nome=u'vOutro' , codigo=u'W15', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')
        self.vNF     = TagDecimal(nome=u'vNF'    , codigo=u'W16', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<ICMSTot>'
        xml += self.vBC.xml
        xml += self.vICMS.xml
        xml += self.vBCST.xml
        xml += self.vST.xml
        xml += self.vProd.xml
        xml += self.vFrete.xml
        xml += self.vSeg.xml
        xml += self.vDesc.xml
        xml += self.vII.xml
        xml += self.vIPI.xml
        xml += self.vPIS.xml
        xml += self.vCOFINS.xml
        xml += self.vOutro.xml
        xml += self.vNF.xml
        xml += u'</ICMSTot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml     = arquivo
            self.vICMS.xml   = arquivo
            self.vBCST.xml   = arquivo
            self.vST.xml     = arquivo
            self.vProd.xml   = arquivo
            self.vFrete.xml  = arquivo
            self.vSeg.xml    = arquivo
            self.vDesc.xml   = arquivo
            self.vII.xml     = arquivo
            self.vIPI.xml    = arquivo
            self.vPIS.xml    = arquivo
            self.vCOFINS.xml = arquivo
            self.vOutro.xml  = arquivo
            self.vNF.xml     = arquivo

    xml = property(get_xml, set_xml)


class Total(XMLNFe):
    def __init__(self):
        super(Total, self).__init__()
        self.ICMSTot = ICMSTot()
        self.ISSQNTot = ISSQNTot()
        self.retTrib  = RetTrib()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<total>'
        xml += self.ICMSTot.xml
        xml += self.ISSQNTot.xml
        xml += self.retTrib.xml
        xml += u'</total>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ICMSTot.xml  = arquivo
            self.ISSQNTot.xml = arquivo
            self.retTrib.xml  = arquivo

    xml = property(get_xml, set_xml)


class Entrega(XMLNFe):
    def __init__(self):
        super(Entrega, self).__init__()
        self.CNPJ    = TagCaracter(nome=u'CNPJ'   , codigo=u'G01', tamanho=[14, 14]   , raiz=u'//NFe/infNFe/entrega')
        self.xLgr    = TagCaracter(nome=u'xLgr'   , codigo=u'G02', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/entrega')
        self.nro     = TagCaracter(nome=u'nro'    , codigo=u'G03', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/entrega')
        self.xCpl    = TagCaracter(nome=u'xCpl'   , codigo=u'G04', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/entrega', obrigatorio=False)
        self.xBairro = TagCaracter(nome=u'xBairro', codigo=u'G05', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/entrega')
        self.cMun    = TagInteiro(nome=u'cMun'    , codigo=u'G06', tamanho=[ 7,  7, 7], raiz=u'//NFe/infNFe/entrega')
        self.xMun    = TagCaracter(nome=u'xMun'   , codigo=u'G07', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/entrega')
        self.UF      = TagCaracter(nome=u'UF'     , codigo=u'G08', tamanho=[ 2,  2]   , raiz=u'//NFe/infNFe/entrega')


    def get_xml(self):
        if not len(self.CNPJ.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<entrega>'
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
            self.CNPJ.xml = arquivo
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.UF.xml      = arquivo

    xml = property(get_xml, set_xml)


class Retirada(XMLNFe):
    def __init__(self):
        super(Retirada, self).__init__()
        self.CNPJ    = TagCaracter(nome=u'CNPJ'   , codigo=u'F01', tamanho=[14, 14]   , raiz=u'//NFe/infNFe/retirada')
        self.xLgr    = TagCaracter(nome=u'xLgr'   , codigo=u'F02', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/retirada')
        self.nro     = TagCaracter(nome=u'nro'    , codigo=u'F03', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/retirada')
        self.xCpl    = TagCaracter(nome=u'xCpl'   , codigo=u'F04', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/retirada', obrigatorio=False)
        self.xBairro = TagCaracter(nome=u'xBairro', codigo=u'F05', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/retirada')
        self.cMun    = TagInteiro(nome=u'cMun'    , codigo=u'F06', tamanho=[ 7,  7, 7], raiz=u'//NFe/infNFe/retirada')
        self.xMun    = TagCaracter(nome=u'xMun'   , codigo=u'F07', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/retirada')
        self.UF      = TagCaracter(nome=u'UF'     , codigo=u'F08', tamanho=[ 2,  2]   , raiz=u'//NFe/infNFe/retirada')


    def get_xml(self):
        if not len(self.CNPJ.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<retirada>'
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
            self.CNPJ.xml = arquivo
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.UF.xml      = arquivo

    xml = property(get_xml, set_xml)


class EnderDest(XMLNFe):
    def __init__(self):
        super(EnderDest, self).__init__()
        self.xLgr    = TagCaracter(nome=u'xLgr'   , codigo=u'E06', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/dest/enderDest')
        self.nro     = TagCaracter(nome=u'nro'    , codigo=u'E07', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/dest/enderDest')
        self.xCpl    = TagCaracter(nome=u'xCpl'   , codigo=u'E08', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.xBairro = TagCaracter(nome=u'xBairro', codigo=u'E09', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/dest/enderDest')
        self.cMun    = TagInteiro(nome=u'cMun'    , codigo=u'E10', tamanho=[ 7,  7, 7], raiz=u'//NFe/infNFe/dest/enderDest')
        self.xMun    = TagCaracter(nome=u'xMun'   , codigo=u'E11', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/dest/enderDest')
        self.UF      = TagCaracter(nome=u'UF'     , codigo=u'E12', tamanho=[ 2,  2]   , raiz=u'//NFe/infNFe/dest/enderDest')
        self.CEP     = TagCaracter(nome=u'CEP'    , codigo=u'E13', tamanho=[ 8,  8, 8], raiz=u'//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.cPais   = TagInteiro(nome=u'cPais'   , codigo=u'E14', tamanho=[ 4,  4, 4], raiz=u'//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.xPais   = TagCaracter(nome=u'xPais'  , codigo=u'E15', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.fone    = TagInteiro(nome=u'fone'    , codigo=u'E16', tamanho=[ 1, 10]   , raiz=u'//NFe/infNFe/dest/enderDest', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<enderDest>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += self.CEP.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += self.fone.xml
        xml += u'</enderDest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.UF.xml      = arquivo
            self.CEP.xml     = arquivo
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo
            self.fone.xml    = arquivo

    xml = property(get_xml, set_xml)


class Dest(XMLNFe):
    def __init__(self):
        super(Dest, self).__init__()
        self.CNPJ      = TagCaracter(nome=u'CNPJ' , codigo=u'E02', tamanho=[0 , 14]   , raiz=u'//NFe/infNFe/dest', obrigatorio=False)
        self.CPF       = TagCaracter(nome=u'CPF'  , codigo=u'E03', tamanho=[11, 11]   , raiz=u'//NFe/infNFe/dest', obrigatorio=False)
        self.xNome     = TagCaracter(nome=u'xNome', codigo=u'E04', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/dest')
        self.enderDest = EnderDest()
        self.IE        = TagCaracter(nome=u'IE'   , codigo=u'E17', tamanho=[ 2, 14]   , raiz=u'//NFe/infNFe/dest')
        self.ISUF      = TagCaracter(nome=u'ISUF' , codigo=u'E18', tamanho=[ 9,  9]   , raiz=u'//NFe/infNFe/dest', obrigatorio=False)

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

    xml = property(get_xml, set_xml)


class Avulsa(XMLNFe):
    def __init__(self):
        super(Avulsa, self).__init__()
        self.CNPJ    = TagCaracter(nome=u'CNPJ'   , codigo=u'D02', tamanho=[14, 14], raiz=u'//NFe/infNFe/avulsa')
        self.xOrgao  = TagCaracter(nome=u'xOrgao' , codigo=u'D03', tamanho=[ 1, 60], raiz=u'//NFe/infNFe/avulsa')
        self.matr    = TagCaracter(nome=u'matr'   , codigo=u'D04', tamanho=[ 1, 60], raiz=u'//NFe/infNFe/avulsa')
        self.xAgente = TagCaracter(nome=u'xAgente', codigo=u'D05', tamanho=[ 1, 60], raiz=u'//NFe/infNFe/avulsa')
        self.fone    = TagInteiro(nome=u'fone'    , codigo=u'D06', tamanho=[ 1, 10], raiz=u'//NFe/infNFe/avulsa')
        self.UF      = TagCaracter(nome=u'UF'     , codigo=u'D07', tamanho=[ 2,  2], raiz=u'//NFe/infNFe/avulsa')
        self.nDAR    = TagCaracter(nome=u'nDAR'   , codigo=u'D08', tamanho=[ 1, 60], raiz=u'//NFe/infNFe/avulsa')
        self.dEmi    = TagData(nome=u'dEmi'       , codigo=u'D09',                   raiz=u'//NFe/infNFe/avulsa')
        self.vDAR    = TagDecimal(nome=u'vDAR'    , codigo=u'D10', tamanho=[ 1, 15], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/avulsa')
        self.repEmi  = TagCaracter(nome=u'repEmi' , codigo=u'D11', tamanho=[ 1, 60], raiz=u'//NFe/infNFe/avulsa')
        self.dPag    = TagData(nome=u'dPag'       , codigo=u'D12',                   raiz=u'//NFe/infNFe/avulsa', obrigatorio=False)

    def get_xml(self):
        if not len(self.CNPJ.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<avulsa>'
        xml += self.CNPJ.xml
        xml += self.xOrgao.xml
        xml += self.matr.xml
        xml += self.xAgente.xml
        xml += self.fone.xml
        xml += self.UF.xml
        xml += self.nDAR.xml
        xml += self.dEmi.xml
        xml += self.vDAR.xml
        xml += self.repEmi.xml
        xml += self.dPag.xml
        xml += u'</avulsa>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml    = arquivo
            self.xOrgao.xml  = arquivo
            self.matr.xml    = arquivo
            self.xAgente.xml = arquivo
            self.fone.xml    = arquivo
            self.UF.xml      = arquivo
            self.nDAR.xml    = arquivo
            self.dEmi.xml    = arquivo
            self.vDAR.xml    = arquivo
            self.repEmi.xml  = arquivo
            self.dPag.xml    = arquivo

    xml = property(get_xml, set_xml)


class EnderEmit(XMLNFe):
    def __init__(self):
        super(EnderEmit, self).__init__()
        self.xLgr    = TagCaracter(nome=u'xLgr'   , codigo=u'C06', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/emit/enderEmit')
        self.nro     = TagCaracter(nome=u'nro'    , codigo=u'C07', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/emit/enderEmit')
        self.xCpl    = TagCaracter(nome=u'xCpl'   , codigo=u'C08', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/emit/enderEmit', obrigatorio=False)
        self.xBairro = TagCaracter(nome=u'xBairro', codigo=u'C09', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/emit/enderEmit')
        self.cMun    = TagInteiro(nome=u'cMun'    , codigo=u'C10', tamanho=[ 7,  7, 7], raiz=u'//NFe/infNFe/emit/enderEmit')
        self.xMun    = TagCaracter(nome=u'xMun'   , codigo=u'C11', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/emit/enderEmit')
        self.UF      = TagCaracter(nome=u'UF'     , codigo=u'C12', tamanho=[ 2,  2]   , raiz=u'//NFe/infNFe/emit/enderEmit')
        self.CEP     = TagCaracter(nome=u'CEP'    , codigo=u'C13', tamanho=[ 8,  8, 8], raiz=u'//NFe/infNFe/emit/enderEmit', obrigatorio=False)
        self.cPais   = TagInteiro(nome=u'cPais'   , codigo=u'C14', tamanho=[ 4,  4, 4], raiz=u'//NFe/infNFe/emit/enderEmit', obrigatorio=False)
        self.xPais   = TagCaracter(nome=u'xPais'  , codigo=u'C15', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/emit/enderEmit', obrigatorio=False)
        self.fone    = TagInteiro(nome=u'fone'    , codigo=u'C16', tamanho=[ 1, 10]   , raiz=u'//NFe/infNFe/emit/enderEmit', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<enderEmit>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += self.CEP.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += self.fone.xml
        xml += u'</enderEmit>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.UF.xml      = arquivo
            self.CEP.xml     = arquivo
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo
            self.fone.xml    = arquivo

    xml = property(get_xml, set_xml)

class Emit(XMLNFe):
    def __init__(self):
        super(Emit, self).__init__()
        self.CNPJ      = TagCaracter(nome=u'CNPJ' , codigo=u'C02' , tamanho=[14, 14], raiz=u'//NFe/infNFe/emit', obrigatorio=False)
        self.CPF       = TagCaracter(nome=u'CPF'  , codigo=u'C02a', tamanho=[11, 11], raiz=u'//NFe/infNFe/emit', obrigatorio=False)
        self.xNome     = TagCaracter(nome=u'xNome', codigo=u'C03' , tamanho=[ 2, 60], raiz=u'//NFe/infNFe/emit')
        self.xFant     = TagCaracter(nome=u'xFant', codigo=u'C04' , tamanho=[ 1, 60], raiz=u'//NFe/infNFe/emit', obrigatorio=False)
        self.enderEmit = EnderEmit()
        self.IE        = TagCaracter(nome=u'IE'   , codigo=u'C17' , tamanho=[ 2, 14], raiz=u'//NFe/infNFe/emit', obrigatorio=False)
        self.IEST      = TagCaracter(nome=u'IEST' , codigo=u'C18' , tamanho=[ 2, 14], raiz=u'//NFe/infNFe/emit', obrigatorio=False)
        self.IM        = TagCaracter(nome=u'IM'   , codigo=u'C19' , tamanho=[ 1, 15], raiz=u'//NFe/infNFe/emit', obrigatorio=False)
        self.CNAE      = TagCaracter(nome=u'CNAE' , codigo=u'C20' , tamanho=[ 7,  7], raiz=u'//NFe/infNFe/emit', obrigatorio=False)


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

    xml = property(get_xml, set_xml)


class RefNF(XMLNFe):
    def __init__(self):
        super(RefNF, self).__init__()
        self.cUF   = TagInteiro(nome=u'cUF'  , codigo=u'B15', tamanho=[ 2,  2, 2], raiz=u'//NFref/refNF')
        self.AAMM  = TagCaracter(nome=u'AAMM', codigo=u'B16', tamanho=[ 4,  4, 4], raiz=u'//NFref/refNF')
        self.CNPJ  = TagCaracter(nome=u'CNPJ', codigo=u'B17', tamanho=[14, 14]   , raiz=u'//NFref/refNF')
        self.mod   = TagCaracter(nome=u'mod' , codigo=u'B18', tamanho=[ 2,  2, 2], raiz=u'//NFref/refNF')
        self.serie = TagInteiro(nome=u'serie', codigo=u'B19', tamanho=[ 1,  3, 1], raiz=u'//NFref/refNF')
        self.nNF   = TagInteiro(nome=u'nNF'  , codigo=u'B20', tamanho=[ 1,  9, 1], raiz=u'//NFref/refNF')

    def get_xml(self):
        if not (self.cUF.valor or self.AAMM.valor or self.CNPJ.valor or self.mod.valor or self.serie.valor or self.nNF.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<refNF>'
        xml += self.cUF.xml
        xml += self.AAMM.xml
        xml += self.CNPJ.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNF.xml
        xml += u'</refNF>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml   = arquivo
            self.AAMM.xml  = arquivo
            self.CNPJ.xml  = arquivo
            self.mod.xml   = arquivo
            self.serie.xml = arquivo
            self.nNF.xml   = arquivo

    xml = property(get_xml, set_xml)


class NFRef(XMLNFe):
    def __init__(self):
        super(NFRef, self).__init__()
        self.refNFe = TagCaracter(nome=u'refNFe', codigo=u'B13', tamanho=[44, 44], raiz=u'//NFRef', obrigatorio=False)
        self.refNF  = RefNF()

    def get_xml(self):
        if not (self.refNFe.valor or self.refNF.xml):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<NFref>'
        xml += self.refNFe.xml
        xml += self.refNF.xml
        #if self.refNFe.valor:
            #xml += self.refNFe.xml
        #else:
            #xml += self.refNF.xml
        xml += u'</NFref>'
        return xml

    def set_xml(self):
        if self._le_xml(arquivo):
            self.refNFe.xml = arquivo
            self.refNF.xml  = arquivo

    xml = property(get_xml, set_xml)


class Ide(XMLNFe):
    def __init__(self):
        super(Ide, self).__init__()
        self.cUF     = TagInteiro(nome=u'cUF'     , codigo=u'B02', tamanho=[ 2,  2, 2], raiz=u'//NFe/infNFe/ide')
        self.cNF     = TagCaracter(nome=u'cNF'    , codigo=u'B03', tamanho=[ 9,  9, 9], raiz=u'//NFe/infNFe/ide')
        self.natOp   = TagCaracter(nome=u'natOp'  , codigo=u'B04', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/ide')
        self.indPag  = TagInteiro(nome=u'indPag'  , codigo=u'B05', tamanho=[ 1,  1, 1], raiz=u'//NFe/infNFe/ide')
        self.mod     = TagInteiro(nome=u'mod'     , codigo=u'B06', tamanho=[ 2,  2, 2], raiz=u'//NFe/infNFe/ide', valor=55)
        self.serie   = TagInteiro(nome=u'serie'   , codigo=u'B07', tamanho=[ 1,  3, 1], raiz=u'//NFe/infNFe/ide')
        self.nNF     = TagInteiro(nome=u'nNF'     , codigo=u'B08', tamanho=[ 1,  9, 1], raiz=u'//NFe/infNFe/ide')
        self.dEmi    = TagData(nome=u'dEmi'       , codigo=u'B09',                      raiz=u'//NFe/infNFe/ide')
        self.dSaiEnt = TagData(nome=u'dSaiEnt'    , codigo=u'B10',                      raiz=u'//NFe/infNFe/ide', obrigatorio=False)
        self.tpNF    = TagInteiro(nome=u'tpNF'    , codigo=u'B11', tamanho=[ 1,  1, 1], raiz=u'//NFe/infNFe/ide', valor=1)
        self.cMunFG  = TagInteiro(nome=u'cMunFG'  , codigo=u'B12', tamanho=[ 7,  7, 7], raiz=u'//NFe/infNFe/ide')
        self.NFref   = []
        self.tpImp   = TagInteiro(nome=u'tpImp'   , codigo=u'B21', tamanho=[ 1,  1, 1], raiz=u'//NFe/infNFe/ide', valor=1)
        self.tpEmis  = TagInteiro(nome=u'tpEmis'  , codigo=u'B22', tamanho=[ 1,  1, 1], raiz=u'//NFe/infNFe/ide', valor=1)
        self.cDV     = TagInteiro(nome=u'cDV'     , codigo=u'B23', tamanho=[ 1,  1, 1], raiz=u'//NFe/infNFe/ide')
        self.tpAmb   = TagInteiro(nome=u'tpAmb'   , codigo=u'B24', tamanho=[ 1,  1, 1], raiz=u'//NFe/infNFe/ide', valor=2)
        self.finNFe  = TagInteiro(nome=u'finNFe'  , codigo=u'B25', tamanho=[ 1,  1, 1], raiz=u'//NFe/infNFe/ide', valor=1)
        self.procEmi = TagInteiro(nome=u'procEmi' , codigo=u'B26', tamanho=[ 1,  1, 1], raiz=u'//NFe/infNFe/ide')
        self.verProc = TagCaracter(nome=u'verProc', codigo=u'B27', tamanho=[ 1, 20]   , raiz=u'//NFe/infNFe/ide')
        self.hSaiEnt = TagHora(nome=u'hSaiEnt'    , codigo=u''   ,                      raiz=u'//NFe/infNFe/ide', obrigatorio=False)

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

    xml = property(get_xml, set_xml)


class InfNFe(XMLNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.versao   = TagDecimal(nome=u'infNFe' , codigo=u'A01', propriedade=u'versao', raiz=u'//NFe', namespace=NAMESPACE_NFE, valor=u'1.10')
        self.Id       = TagCaracter(nome=u'infNFe', codigo=u'A03', propriedade=u'Id'    , raiz=u'//NFe', namespace=NAMESPACE_NFE)
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

    xml = property(get_xml, set_xml)


class NFe(XMLNFe):
    def __init__(self):
        super(NFe, self).__init__()
        self.infNFe = InfNFe()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'nfe_v1.10.xsd'
        self.chave = u''
        self.dados_contingencia_fsda = u''
        self.site = u''
        self.email = u''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += u'<NFe xmlns="http://www.portalfiscal.inf.br/nfe">'
        xml += self.infNFe.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = u'#' + self.infNFe.Id.valor

        xml += self.Signature.xml
        xml += u'</NFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infNFe.xml    = arquivo
            self.Signature.xml = self._le_noh('//NFe/sig:Signature')

    xml = property(get_xml, set_xml)

    def _calcula_dv(self, valor):
        soma = 0
        m = 2
        for i in range(len(valor)-1, -1, -1):
            c = valor[i]
            soma += int(c) * m
            m += 1
            if m > 9:
                m = 2

        digito = 11 - (soma % 11)
        if digito > 9:
            digito = 0

        return digito

    def gera_nova_chave(self):
        chave = unicode(self.infNFe.ide.cUF.valor).zfill(2)
        chave += unicode(self.infNFe.ide.dEmi.valor.strftime(u'%y%m')).zfill(4)
        chave += unicode(self.infNFe.emit.CNPJ.valor).zfill(14)
        chave += unicode(self.infNFe.ide.mod.valor).zfill(2)
        chave += unicode(self.infNFe.ide.serie.valor).zfill(3)
        chave += unicode(self.infNFe.ide.nNF.valor).zfill(9)

        #
        # A inclusão do tipo de emissão na chave já torna a chave válida também
        # para a versão 2.00 da NF-e
        #
        chave += unicode(self.infNFe.ide.tpEmis.valor).zfill(1)

        #
        # O código numério é um número aleatório
        #
        #chave += unicode(random.randint(0, 99999999)).strip().rjust(8, u'0')

        #
        # Mas, por segurança, é preferível que esse número não seja aleatório de todo
        #
        soma = 0
        for c in chave:
            soma += int(c) ** 3 ** 2

        codigo = unicode(soma)
        if len(codigo) > 8:
            codigo = codigo[-8:]
        else:
            codigo = codigo.rjust(8, u'0')

        chave += codigo

        #
        # Define na estrutura do XML o campo cNF
        #
        self.infNFe.ide.cNF.valor = unicode(self.infNFe.ide.tpEmis.valor).zfill(1) + codigo

        #
        # Gera o dígito verificador
        #
        digito = self._calcula_dv(chave)

        #
        # Define na estrutura do XML o campo cDV
        #
        self.infNFe.ide.cDV.valor = digito

        chave += unicode(digito)
        self.chave = chave

        #
        # Define o Id
        #
        self.infNFe.Id.valor = u'NFe' + chave

    def monta_chave(self):
        chave = unicode(self.infNFe.ide.cUF.valor).zfill(2)
        chave += unicode(self.infNFe.ide.dEmi.valor.strftime(u'%y%m')).zfill(4)
        chave += unicode(self.infNFe.emit.CNPJ.valor).zfill(14)
        chave += unicode(self.infNFe.ide.mod.valor).zfill(2)
        chave += unicode(self.infNFe.ide.serie.valor).zfill(3)
        chave += unicode(self.infNFe.ide.nNF.valor).zfill(9)
        chave += unicode(self.infNFe.ide.cNF.valor).zfill(9)
        chave += unicode(self.infNFe.ide.cDV.valor).zfill(1)
        self.chave = chave

    def chave_para_codigo_barras(self):
        #
        # As funções do reportlabs para geração de códigos de barras não estão
        # aceitando strings unicode
        #
        return self.chave.encode(u'utf-8')

    def monta_dados_contingencia_fsda(self):
        dados = unicode(self.infNFe.ide.cUF.valor).zfill(2)
        dados += unicode(self.infNFe.ide.tpEmis.valor).zfill(1)
        dados += unicode(self.infNFe.emit.CNPJ.valor).zfill(14)
        dados += unicode(int(self.infNFe.total.ICMSTot.vNF.valor * 100)).zfill(14)

        #
        # Há ICMS próprio?
        #
        if self.infNFe.total.ICMSTot.vICMS.valor:
            dados += u'1'
        else:
            dados += u'2'

        #
        # Há ICMS ST?
        #
        if self.infNFe.total.ICMSTot.vST.valor:
            dados += u'1'
        else:
            dados += u'2'

        dados += self.infNFe.ide.dEmi.valor.strftime(u'%d').zfill(2)

        digito = self._calcula_dv(dados)
        dados += unicode(digito)
        self.dados_contingencia_fsda = dados

    def dados_contingencia_fsda_para_codigo_barras(self):
        #
        # As funções do reportlabs para geração de códigos de barras não estão
        # aceitando strings unicode
        #
        self.monta_dados_contingencia_fsda()
        return self.dados_contingencia_fsda.encode(u'utf-8')

    #
    # Funções para formatar campos para o DANFE
    #

    def chave_formatada(self):
        chave = self.chave
        chave_formatada = u' '.join((chave[0:4], chave[4:8], chave[8:12], chave[12:16], chave[16:20], chave[20:24], chave[24:28], chave[28:32], chave[32:36], chave[36:40], chave[40:44]))
        return chave_formatada

    def dados_contingencia_fsda_formatados(self):
        self.monta_dados_contingencia_fsda()
        dados = self.dados_contingencia_fsda
        dados_formatados = u' '.join((dados[0:4], dados[4:8], dados[8:12], dados[12:16], dados[16:20], dados[20:24], dados[24:28], dados[28:32], dados[32:36]))
        return dados_formatados

    def numero_formatado(self):
        num = unicode(self.infNFe.ide.nNF.valor).zfill(9)
        num_formatado = u'.'.join((num[0:3], num[3:6], num[6:9]))
        return u'Nº ' + num_formatado

    def serie_formatada(self):
        return u'SÉRIE ' + unicode(self.infNFe.ide.serie.valor).zfill(3)


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

    def cnpj_emitente_formatado(self):
        if len(self.infNFe.emit.CPF.valor):
            return self._formata_cpf(unicode(self.infNFe.emit.CPF.valor))
        else:
            return self._formata_cnpj(unicode(self.infNFe.emit.CNPJ.valor))

    def endereco_emitente_formatado(self):
        formatado = self.infNFe.emit.enderEmit.xLgr.valor
        formatado += u', ' + self.infNFe.emit.enderEmit.nro.valor

        if len(self.infNFe.emit.enderEmit.xCpl.valor.strip()):
            formatado += u' - ' + self.infNFe.emit.enderEmit.xCpl.valor

        return formatado

    def _formata_cep(self, cep):
        if not len(cep.strip()):
            return u''

        return cep[0:5] + u'-' + cep[5:8]

    def cep_emitente_formatado(self):
        return self._formata_cep(self.infNFe.emit.enderEmit.CEP.valor)

    def endereco_emitente_formatado_linha_1(self):
        formatado = self.endereco_emitente_formatado()
        formatado += u' - ' + self.infNFe.emit.enderEmit.xBairro.valor
        return formatado

    def endereco_emitente_formatado_linha_2(self):
        formatado = self.infNFe.emit.enderEmit.xMun.valor
        formatado += u' - ' + self.infNFe.emit.enderEmit.UF.valor
        formatado += u' - ' + self.cep_emitente_formatado()
        return formatado

    def endereco_emitente_formatado_linha_3(self):
        formatado = u'Fone: ' + self.fone_emitente_formatado()
        return formatado

    def endereco_emitente_formatado_linha_4(self):
        return self.site

    def _formata_fone(self, fone):
        if not len(fone.strip()):
            return u''

        if len(fone) <= 8:
            formatado = fone[:-4] + u'-' + fone[-4:]
        elif len(fone) <= 10:
            ddd = fone[0:2]
            fone = fone[2:]
            formatado = u'(' + ddd + u') ' + fone[:-4] + u'-' + fone[-4:]

        return formatado

    def fone_emitente_formatado(self):
        return self._formata_fone(unicode(self.infNFe.emit.enderEmit.fone.valor))

    def cnpj_destinatario_formatado(self):
        if len(self.infNFe.dest.CPF.valor):
            return self._formata_cpf(unicode(self.infNFe.dest.CPF.valor))
        else:
            return self._formata_cnpj(unicode(self.infNFe.dest.CNPJ.valor))

    def endereco_destinatario_formatado(self):
        formatado = self.infNFe.dest.enderDest.xLgr.valor
        formatado += u', ' + self.infNFe.dest.enderDest.nro.valor

        if len(self.infNFe.dest.enderDest.xCpl.valor.strip()):
            formatado += u' - ' + self.infNFe.dest.enderDest.xCpl.valor

        return formatado

    def cep_destinatario_formatado(self):
        return self._formata_cep(self.infNFe.dest.enderDest.CEP.valor)

    def fone_destinatario_formatado(self):
        return self._formata_fone(unicode(self.infNFe.dest.enderDest.fone.valor))

    def cnpj_retirada_formatado(self):
        return self._formata_cnpj(self.infNFe.retirada.CNPJ.valor)

    def endereco_retirada_formatado(self):
        formatado = self.infNFe.retirada.xLgr.valor
        formatado += u', ' + self.infNFe.retirada.nro.valor

        if len(self.infNFe.retirada.xCpl.valor.strip()):
            formatado += u' - ' + self.infNFe.retirada.xCpl.valor

        formatado += u' - ' + self.infNFe.retirada.xBairro.valor
        formatado += u' - ' + self.infNFe.retirada.xMun.valor
        formatado += u'-' + self.infNFe.retirada.UF.valor
        return formatado

    def cnpj_entrega_formatado(self):
        return self._formata_cnpj(self.infNFe.entrega.CNPJ.valor)

    def endereco_entrega_formatado(self):
        formatado = self.infNFe.entrega.xLgr.valor
        formatado += u', ' + self.infNFe.entrega.nro.valor

        if len(self.infNFe.entrega.xCpl.valor.strip()):
            formatado += u' - ' + self.infNFe.entrega.xCpl.valor

        formatado += u' - ' + self.infNFe.entrega.xBairro.valor
        formatado += u' - ' + self.infNFe.entrega.xMun.valor
        formatado += u'-' + self.infNFe.entrega.UF.valor
        return formatado

    def cnpj_transportadora_formatado(self):
        if self.infNFe.transp.transporta.CPF.valor:
            return self._formata_cpf(self.infNFe.transp.transporta.CPF.valor)
        else:
            return self._formata_cnpj(self.infNFe.transp.transporta.CNPJ.valor)

    def placa_veiculo_formatada(self):
        if not self.infNFe.transp.veicTransp.placa.valor:
            return u''

        placa = self.infNFe.transp.veicTransp.placa.valor
        placa = placa[:-4] + u'-' + placa[-4:]
        return placa

    def dados_adicionais(self):
        da = u''

        if self.infNFe.infAdic.infAdFisco.valor:
            da = self.infNFe.infAdic.infAdFisco.valor.replace(u'|', u'<br />')

        if self.infNFe.infAdic.infCpl.valor:
            if len(da) > 0:
                da += u'<br />'

            da += self.infNFe.infAdic.infCpl.valor.replace(u'|', u'<br />')

        return da

    def canhoto_formatado(self):
        formatado = u'RECEBEMOS DE <b>'
        formatado += self.infNFe.emit.xNome.valor.upper()
        formatado += u'</b> OS PRODUTOS E/OU SERVIÇOS CONSTANTES DA <b>NOTA FISCAL ELETRÔNICA</b> INDICADA AO LADO'
        return formatado

    def frete_formatado(self):
        if self.infNFe.transp.modFrete.valor == 0:
            formatado = u'0-EMITENTE'

        elif self.infNFe.transp.modFrete.valor == 1:
            if self.infNFe.ide.tpNF.valor == 0:
                formatado = u'1-REMETENTE'
            else:
                formatado = u'1-DESTINATÁRIO'

        elif self.infNFe.transp.modFrete.valor == 2:
            formatado = u'2-DE TERCEIROS'

        elif self.infNFe.transp.modFrete.valor == 9:
            formatado = u'9-SEM FRETE'

        else:
            formatado = u''

        return formatado