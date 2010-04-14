# -*- coding: utf-8 -*-

from lxml import etree
from StringIO import StringIO
from datetime import datetime
from decimal import Decimal
import locale


NAMESPACE_NFE = u'http://www.portalfiscal.inf.br/nfe'
NAMESPACE_SIG = u'http://www.w3.org/2000/09/xmldsig#'
ABERTURA = u'<?xml version="1.0" encoding="utf-8"?>'

CAMINHO_ESQUEMA_110 = u'schema/pl_005d/'
CAMINHO_ESQUEMA_200 = u'schema/pl_006e/'

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')


class NohXML(object):
    def __init__(self, *args, **kwargs):
        self._xml = None
        self.alertas = []
    
    def _le_xml(self, arquivo):
        if arquivo is None:
            return False
        
        #print arquivo    
        if not isinstance(arquivo, basestring):
            arquivo = etree.tounicode(arquivo)
            #self._xml = arquivo
            #return True
            
        #elif arquivo is not None:
        if arquivo is not None:
            if arquivo[0] == u'<':
                arquivo = StringIO(arquivo)
            self._xml = etree.parse(arquivo)
            return True
            
        return False

    def _preenche_namespace(self, tag):
        tag = u'/nfe:'.join(tag.split(u'/')).replace(u'/nfe:/nfe:', u'//nfe:').replace(u'nfe:sig:', u'sig:')
        return tag

    def _le_nohs(self, tag, ns=None):
        #
        # Tenta ler a tag sem os namespaces
        # Necessário para ler corretamente as tags de grupo reenraizadas
        #
        nohs = self._xml.xpath(tag)
        if len(nohs) >= 1:
            return nohs
            
        #
        # Não deu certo, tem que botar mesmo os namespaces
        #
        namespaces = {u'nfe': NAMESPACE_NFE, u'sig': NAMESPACE_SIG}
        
        if ns is not None:
            namespaces[u'res'] = ns
        
        if not tag.startswith(u'//*/res'):
            tag = self._preenche_namespace(tag)    

        nohs = self._xml.xpath(tag, namespaces=namespaces)

        if len(nohs) >= 1:
            return nohs
        else:
            return None

    def _le_noh(self, tag, ns=None, ocorrencia=1):
        nohs = self._le_nohs(tag, ns)

        if (nohs is not None) and (len(nohs) >= ocorrencia):
            return nohs[ocorrencia-1]
        else:
            return None

    def _le_tag(self, tag, propriedade=None, ns=None, ocorrencia=1):
        noh = self._le_noh(tag,  ns, ocorrencia)

        if noh is None:
            valor = u''
        else:
            if propriedade is None:
                valor = noh.text
            elif (noh.attrib is not None) and (len(noh.attrib) > 0):
                valor = noh.attrib[propriedade]
            else:
                valor = u''

        return valor


class ErroObrigatorio(Exception):
    def __init__(self, codigo, nome, propriedade):
        if propriedade:
            self.value = u'No campo código ' + codigo + u', "' + nome + u'", a propriedade "' + propriedade + u'" é de envio obrigatório, mas não foi preenchida.'
        else:
            self.value = u'O campo código ' + codigo + u', "' + nome + u'" é de envio obrigatório, mas não foi preenchido.'
        
    def __str__(self):
        return repr(self.value)
        
    def __unicode__(self):
        return unicode(self.value)


class TamanhoInvalido(Exception):
    def __init__(self, codigo, nome, valor, tam_min=None, tam_max=None, dec_min=None, dec_max=None):
        if tam_min:
           self.value = u'O campo código ' + codigo + u', "' + nome + u'", deve ter o tamanho mínimo de ' + unicode(tam_min) + u', mas o tamanho enviado foi ' + unicode(len(unicode(valor))) + u': ' + unicode(valor)
        elif tam_max:
           self.value = u'O campo código ' + codigo + u', "' + nome + u'", deve ter o tamanho máximo de ' + unicode(tam_max) + u', mas o tamanho enviado foi ' + unicode(len(unicode(valor))) + u': ' + unicode(valor)
        elif dec_min:
           self.value = u'O campo código ' + codigo + u', "' + nome + u'", deve ter o mínimo de ' + unicode(dec_min) + u' casas decimais, mas o enviado foi ' + unicode(len(unicode(valor))) + u': ' + unicode(valor)
        elif dec_max:
           self.value = u'O campo código ' + codigo + u', "' + nome + u'", deve ter o máximo de ' + unicode(dec_max) + u' casas decimais, mas o enviado foi ' + unicode(len(unicode(valor))) + u': ' + unicode(valor)
        
    def __str__(self):
        return repr(self.value)

    def __unicode__(self):
        return unicode(self.value)


class ErroCaracterInvalido(Exception):
    def __init__(self, codigo, nome, propriedade, valor, caracter):
        if propriedade:
            self.value = u'No campo código ' + codigo + u', "' + nome + u'", a propriedade "' + propriedade + u'" possui um caracter inválido: "' + caracter + u'".'
        else:
            self.value = u'O campo código ' + codigo + u', "' + nome + u'" possui um caracter inválido: "' + caracter + u'".'
        
    def __str__(self):
        return repr(self.value)
        
    def __unicode__(self):
        return unicode(self.value)


class TagCaracter(NohXML):
    def __init__(self, *args, **kwargs):
        super(TagCaracter, self).__init__(*args, **kwargs)
        self.codigo = u''
        self.nome = u''
        self._valor_string = u''
        self.obrigatorio = True
        self.tamanho = [None, None, None]
        self.propriedade = None
        self.namespace = None
        self.alertas = []
        self.raiz = None
        
        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)
            
        if kwargs.has_key('valor'):
            self.valor = kwargs['valor']
    
    def _testa_obrigatorio(self, valor):
        if self.obrigatorio and (not valor):
            return ErroObrigatorio(self.codigo, self.nome, self.propriedade)
            #raise ErroObrigatorio(self.codigo, self.nome, self.propriedade)
            
    def _testa_tamanho_minimo(self, valor):
        if self.tamanho[0] and (len(unicode(valor)) < self.tamanho[0]):
            return TamanhoInvalido(self.codigo, self.nome, valor, tam_min=self.tamanho[0])
            #raise TamanhoInvalido(self.codigo, self.nome, valor, tam_min=self.tamanho[0])
    
    def _testa_tamanho_maximo(self, valor):
        if self.tamanho[1] and (len(unicode(valor)) > self.tamanho[1]):
            return TamanhoInvalido(self.codigo, self.nome, valor, tam_max=self.tamanho[1])
            #raise TamanhoInvalido(self.codigo, self.nome, valor, tam_max=self.tamanho[1])

    def _valida(self, valor):
        self.alertas = []
        
        if self._testa_obrigatorio(valor):
            self.alertas.append(self._testa_obrigatorio(valor))
            
        if self._testa_tamanho_minimo(valor):
            self.alertas.append(self._testa_tamanho_minimo(valor))
            
        if self._testa_tamanho_maximo(valor):
            self.alertas.append(self._testa_tamanho_maximo(valor))
            
        return self.alertas == []
        
    def set_valor(self, novo_valor):
        if novo_valor is not None:
            #
            # Remover caratceres inválidos
            #
            for c in novo_valor:
                if c > u'ÿ':
                    raise ErroCaracterInvalido(self.codigo, self.nome, self.propriedade, novo_valor, c)
        
            #
            # É obrigatório remover os espaços no início e no final do valor
            #
            novo_valor = novo_valor.strip()
        
        if self._valida(novo_valor):
            self._valor_string = tirar_acentos(novo_valor)
        else:
            self._valor_string = u''

    def get_valor(self):
        return self._valor_string
    
    valor = property(get_valor, set_valor)
    
    def __unicode__(self):
        if (not self.obrigatorio) and (not self.valor):
            texto = u''
        else:
            texto = u'<%s' % self.nome
            
            if self.namespace:
                texto += u' xmlns="%s"' % self.namespace
                
            if self.propriedade:
                texto += u' %s="%s">' % (self.propriedade, self._valor_string)
            elif self.valor or (len(self.tamanho) == 3 and self.tamanho[2]):
                texto += u'>%s</%s>' % (self._valor_string, self.nome)
            else:
                texto += u' />'
                
        return texto
    
    def __repr__(self):
        return self.__unicode__()
        
    def get_xml(self):
        return self.__unicode__()
        
    def set_xml(self, arquivo, ocorrencia=1):
        if self._le_xml(arquivo):
            self.valor = self._le_tag(self.raiz + u'/' + self.nome, propriedade=self.propriedade, ns=self.namespace, ocorrencia=ocorrencia)
        
    xml = property(get_xml, set_xml)
    
    def get_text(self):
        if self.propriedade:
            return u'%s=%s' % (self.propriedade, self._valor_string)
        else:
            return u'%s=%s' % (self.nome, self._valor_string)
        
    text = property(get_text)


class TagData(TagCaracter):
    def __init__(self, **kwargs):
        super(TagData, self).__init__(**kwargs)
        self._valor_data = None
        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)
            
        if kwargs.has_key('valor'):
            self.valor = kwargs['valor']

    def _valida(self, valor):
        self.alertas = []
        
        if self._testa_obrigatorio(valor):
            self.alertas.append(self._testa_obrigatorio(valor))
            
        return self.alertas == []

    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if novo_valor:
                novo_valor = datetime.strptime(novo_valor, u'%Y-%m-%d')
            else:
                novo_valor = None
        
        if isinstance(novo_valor, datetime) and self._valida(novo_valor):
            self._valor_data = novo_valor
            # Cuidado!!!
            # Aqui não dá pra usar a função strftime pois em alguns
            # casos a data retornada é 01/01/0001 00:00:00
            # e a função strftime só aceita data com anos a partir de 1900
            self._valor_string = u'%04d-%02d-%02d' % (self._valor_data.year, self._valor_data.month, self._valor_data.day)
        else:
            self._valor_data = None
            self._valor_string = u''

    def get_valor(self):
        return self._valor_data
        
    valor = property(get_valor, set_valor)
    
    def formato_danfe(self):
        return self._valor_data.strftime(u'%d/%m/%Y')

class TagHora(TagData):
    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if novo_valor:
                novo_valor = datetime.strptime(novo_valor, u'%H:%M:%S')
            else:
                novo_valor = None

        if isinstance(novo_valor, datetime) and self._valida(novo_valor):
            self._valor_data = novo_valor
            # Cuidado!!!
            # Aqui não dá pra usar a função strftime pois em alguns
            # casos a data retornada é 01/01/0001 00:00:00
            # e a função strftime só aceita data com anos a partir de 1900
            self._valor_string = u'%02d:%02d:%02d' % (self._valor_data.hour, self._valor_data.minute, self._valor_data.second)
        else:
            self._valor_data = None
            self._valor_string = u''

    def get_valor(self):
        return self._valor_data
        
    valor = property(get_valor, set_valor)

    def formato_danfe(self):
        return self._valor_data.strftime(u'%H:%M:%S')


class TagDataHora(TagData):
    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if novo_valor:
                novo_valor = datetime.strptime(novo_valor, u'%Y-%m-%dT%H:%M:%S')
            else:
                novo_valor = None
        
        if isinstance(novo_valor, datetime) and self._valida(novo_valor):
            self._valor_data = novo_valor
            # Cuidado!!!
            # Aqui não dá pra usar a função strftime pois em alguns
            # casos a data retornada é 01/01/0001 00:00:00
            # e a função strftime só aceita data com anos a partir de 1900
            self._valor_string = u'%04d-%02d-%02dT%02d:%02d:%02d' % (self._valor_data.year, self._valor_data.month, self._valor_data.day, 
                self._valor_data.hour, self._valor_data.minute, self._valor_data.second)
        else:
            self._valor_data = None
            self._valor_string = u''

    def get_valor(self):
        return self._valor_data
        
    valor = property(get_valor, set_valor)

    def formato_danfe(self):
        return self._valor_data.strftime(u'%d/%m/%Y %H:%M:%S')


class TagInteiro(TagCaracter):
    def __init__(self, **kwargs):
        super(TagInteiro, self).__init__(**kwargs)
        self._valor_inteiro = 0
        self._valor_string = u'0'

        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)
            
        if kwargs.has_key('valor'):
            self.valor = kwargs['valor']

    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if novo_valor:
                novo_valor = int(novo_valor)
            else:
                novo_valor = 0

        if isinstance(novo_valor, (int, long, Decimal)) and self._valida(novo_valor):
            self._valor_inteiro = novo_valor
            self._valor_string = unicode(self._valor_inteiro)
            
            if (len(self.tamanho) >= 3) and self.tamanho[2] and (len(self._valor_string) < self.tamanho[2]):
                self._valor_string = self._valor_string.rjust(self.tamanho[2], u'0')
            
        else:
            self._valor_inteiro = 0
            self._valor_string = u'0'

    def get_valor(self):
        return self._valor_inteiro
        
    valor = property(get_valor, set_valor)

    def formato_danfe(self):
        return locale.format(u'%d', self._valor_inteiro, grouping=True)


class TagDecimal(TagCaracter):
    def __init__(self, *args, **kwargs):
        self._valor_decimal = Decimal('0.0')
        self._valor_string = u'0.0'
        self.decimais = [None, None, None]
        super(TagDecimal, self).__init__(*args, **kwargs)

        self._valor_decimal = Decimal('0.0')
        self._valor_string = self._formata(self._valor_decimal)
        self.decimais = [None, None, None]
       
        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def _parte_inteira(self, valor=None):
        if valor is None:
            valor = self._valor_decimal

        valor = unicode(valor).strip()
        
        if u'.' in valor:
            valor = valor.split(u'.')[0]
            
        return valor
    
    def _parte_decimal(self, valor=None):
        if valor is None:
            valor = self._valor_decimal
        
        valor = unicode(valor).strip()
        
        if u'.' in valor:
            valor = valor.split(u'.')[1]
        else:
            valor = u''
            
        return valor
    
    def _formata(self, valor):
        texto = self._parte_inteira(valor)
        
        dec = self._parte_decimal(valor)
        if not dec:
            dec = u'0'

        # Tamanho mínimo das casas decimais
        if (len(self.decimais) >= 3) and self.decimais[2] and (len(dec) < self.decimais[2]):
            dec = dec.rjust(self.decimais[2], u'0')
            
        texto += u'.' + dec
        return texto
    
    def _testa_decimais_minimo(self, decimal):
        if self.decimais[0] and (len(decimal) < self.decimais[0]):
            #return TamanhoInvalido(self.codigo, self.nome, decimal, dec_min=self.decimais[0])
            raise TamanhoInvalido(self.codigo, self.nome, decimal, dec_min=self.decimais[0])
    
    def _testa_decimais_maximo(self, decimal):
        if self.decimais[1] and (len(decimal) > self.decimais[1]):
            #return TamanhoInvalido(self.codigo, self.nome, decimal, dec_max=self.decimais[1])
            raise TamanhoInvalido(self.codigo, self.nome, decimal, dec_max=self.decimais[1])

    def _valida(self, valor):
        self.alertas = []
        
        if self._testa_obrigatorio(valor):
            self.alertas.append(self._testa_obrigatorio(valor))
            
        inteiro = self._parte_inteira(valor)
        decimal = self._parte_decimal(valor)
            
        if self._testa_tamanho_minimo(inteiro):
            self.alertas.append(self._testa_tamanho_minimo(inteiro))
            
        if self._testa_tamanho_maximo(inteiro):
            self.alertas.append(self._testa_tamanho_maximo(inteiro))
            
        if self._testa_decimais_minimo(decimal):
            self.alertas.append(self._testa_decimais_minimo(decimal))

        if self._testa_decimais_maximo(decimal):
            self.alertas.append(self._testa_decimais_maximo(decimal))

        return self.alertas == []
        
    
    def set_valor(self, novo_valor):
        if isinstance(novo_valor, basestring):
            if novo_valor:
                novo_valor = Decimal(novo_valor)
            else:
                novo_valor = Decimal('0.0')

        if isinstance(novo_valor, (int, long, Decimal)) and self._valida(novo_valor):
            self._valor_decimal = Decimal(novo_valor)
            self._valor_string = self._formata(self._valor_decimal)
        else:
            self._valor_decimal = Decimal('0.0')
            self._valor_string = self._formata(self._valor_decimal)

    def get_valor(self):
        return self._valor_decimal
        
    valor = property(get_valor, set_valor)

    def formato_danfe(self):
        
        # Tamanho mínimo das casas decimais
        if (len(self.decimais) >= 3) and self.decimais[2]:
            if len(self._parte_decimal()) <= self.decimais[2]:
                formato = u'%.' + unicode(self.decimais[2]) + u'f'
            else:
                formato = u'%.' + unicode(len(self._parte_decimal())) + u'f'
        else:
            formato = u'%.2f'
            
        return locale.format(formato, self._valor_decimal, grouping=True)


class XMLNFe(NohXML):
    def __init__(self, *args, **kwargs):
        super(XMLNFe, self).__init__(*args, **kwargs)
        self._xml = None
        self.alertas = []
        self.arquivo_esquema = None
        self.caminho_esquema = None
    
    def get_xml(self):
        self.alertas = []
        return u''
        
    def validar(self):
        arquivo_esquema = self.caminho_esquema + self.arquivo_esquema
        
        # Aqui é importante remover a declaração do encoding
        # para evitar erros de conversão unicode para ascii
        xml = tira_abertura(self.xml).encode(u'utf-8')
        
        esquema = etree.XMLSchema(etree.parse(arquivo_esquema))
        esquema.assertValid(etree.fromstring(xml))
        #esquema.validate(etree.fromstring(xml))
        
        return esquema.error_log
        
    def le_grupo(self, raiz_grupo, classe_grupo):
        tags = []
        
        grupos = self._le_nohs(raiz_grupo)
        
        if grupos is not None:
            tags = [classe_grupo() for g in grupos]
            for i in range(len(grupos)):
                tags[i].xml = grupos[i]
        
        return tags
        
        
def tirar_acentos(texto):
    if not texto:
        return texto
        
    texto = texto.replace(u'&', u'&amp;')
    texto = texto.replace(u'<', u'&lt;')
    texto = texto.replace(u'>', u'&gt;')
    texto = texto.replace(u'"', u'&quot;')
    texto = texto.replace(u"'", u'&apos;')
    
    #
    # Trocar ENTER e TAB
    #
    texto = texto.replace(u'\t', u' ')
    texto = texto.replace(u'\n', u'| ')
    
    # Remove espaços seguidos
    # Nem pergunte...
    while u'  ' in texto:
        texto = texto.replace(u'  ', u' ')
    
    return texto
    
def por_acentos(texto):
    if not texto:
        return texto
        
    texto = texto.replace(u'&#39;', u"'")
    texto = texto.replace(u'&apos;', u"'")
    texto = texto.replace(u'&quot;', u'"')
    texto = texto.replace(u'&gt;'   , u'>')
    texto = texto.replace(u'&lt;'   , u'<')
    texto = texto.replace(u'&amp;' , u'&')
    
    return texto
    
def tira_abertura(texto):
    aberturas = (u'<?xml version="1.0" encoding="utf-8"?>',
        u'<?xml version="1.0" encoding="utf-8" ?>', 
        u'<?xml version="1.0" encoding="UTF-8"?>',
        u'<?xml version="1.0" encoding="UTF-8" ?>')
        
    for a in aberturas:
        texto = texto.replace(a,  u'')
        
    return texto

def _tipo_para_string(valor, tipo, obrigatorio, dec_min):
    if (not obrigatorio) and (not valor):
        return u'', u''

    decimais = u''

    # Cuidado!!!
    # Aqui não dá pra usar a função strftime pois em alguns
    # casos a data retornada é 01/01/0001 00:00:00
    # e a função strftime só aceita data com anos a partir de 1900
    if (tipo in (u'd', u'h', u'dh')) and isinstance(valor, datetime):
        valor = formata_datahora(valor, tipo)
    elif (tipo == u'n') and isinstance(valor, (int, long, float, Decimal)):
        if isinstance(valor, (int, long, float)):
            valor = Decimal(unicode(valor))
            
        valor = unicode(valor).strip()
        
        if u'.' in valor:
            decimais = valor.split(u'.')[1]
            
        if dec_min:
            decimais = decimais.ljust(dec_min, u'0')
            
            if u'.' in valor:
                valor = valor.split(u'.')[0]
                
            valor += u'.' + decimais
            
    return valor, decimais    
    
def _string_para_tipo(valor, tipo):
    if valor == None:
        return valor
    
    if tipo == u'd':
        valor = datetime.strptime(valor, u'%Y-%m-%d')
    elif tipo == u'h':
        valor = datetime.strptime(valor, u'%H:%M:%S')
    elif tipo == u'dh':
        valor = datetime.strptime(valor, u'%Y-%m-%dT%H:%M:%S')
    elif tipo == u'n':
        valor = Decimal(valor)
        
    return valor

def formata_datahora(valor, tipo):
    if (tipo == u'd') and isinstance(valor, datetime):
        valor = u'%04d-%02d-%02d' % (valor.year, valor.month, valor.day)
    elif (tipo == u'h') and isinstance(valor, datetime):
        valor = u'%02d:%02d:%02d' % (valor.hour, valor.minute, valor.second)
        valor = valor.strftime(u'%H:%M:%S')
    elif (tipo == u'dh') and isinstance(valor, datetime):
        valor = u'%04d-%02d-%02dT%02d:%02d:%02d' % (valor.year, valor.month, valor.day, valor.hour, valor.minute, valor.second)
        
    return valor
