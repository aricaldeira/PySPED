# -*- coding: utf-8 -*-


ESQUEMA_ATUAL = u'pl_005d'


#
# Envelopes SOAP
#
from soap_100 import SOAPEnvio as SOAPEnvio_110
from soap_100 import SOAPRetorno as SOAPRetorno_110

#
# Emissão de NF-e
#
from nfe_110 import NFe as NFe_110
from nfe_110 import NFRef as NFRef_110
from nfe_110 import Det as Det_110
from nfe_110 import DI as DI_110
from nfe_110 import Adi as Adi_110
from nfe_110 import Med as Med_110
from nfe_110 import Arma as Arma_110
from nfe_110 import Reboque as Reboque_110
from nfe_110 import Vol as Vol_110
from nfe_110 import Lacres as Lacres_110
from nfe_110 import Dup as Dup_110
from nfe_110 import ObsCont as ObsCont_110
from nfe_110 import ObsFisco as ObsFisco_110
from nfe_110 import ProcRef as ProcRef_110

#
# Envio de lote de NF-e
#
from envinfe_110 import EnviNFe as EnviNFe_110
from envinfe_110 import RetEnviNFe as RetEnviNFe_110

#
# Consulta do recibo do lote de NF-e
#
from consrecinfe_110 import ConsReciNFe as ConsReciNFe_110
from consrecinfe_110 import RetConsReciNFe as RetConsReciNFe_110
from consrecinfe_110 import ProtNFe as ProtNFe_110
from consrecinfe_110 import ProcNFe as ProcNFe_110

#
# Cancelamento de NF-e
#
from cancnfe_107 import CancNFe as CancNFe_107
from cancnfe_107 import RetCancNFe as RetCancNFe_107
from cancnfe_107 import ProcCancNFe as ProcCancNFe_107

#
# Inutilização de NF-e
#
from inutnfe_107 import InutNFe as InutNFe_107
from inutnfe_107 import RetInutNFe as RetInutNFe_107
from inutnfe_107 import ProcInutNFe as ProcInutNFe_107

#
# Consulta a situação de NF-e
#
from conssitnfe_107 import ConsSitNFe as ConsSitNFe_107
from conssitnfe_107 import RetConsSitNFe as RetConsSitNFe_107

#
# Consulta a situação do serviço
#
from consstatserv_107 import ConsStatServ as ConsStatServ_107
from consstatserv_107 import RetConsStatServ as RetConsStatServ_107

#
# Consulta cadastro
#
from conscad_101 import ConsCad as ConsCad_101
from conscad_101 import RetConsCad as RetConsCad_101

