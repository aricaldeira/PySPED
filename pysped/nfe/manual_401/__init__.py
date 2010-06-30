# -*- coding: utf-8 -*-


ESQUEMA_ATUAL = u'pl_006g'


#
# Envelopes SOAP
#
from soap_200 import SOAPEnvio as SOAPEnvio_200
from soap_200 import SOAPRetorno as SOAPRetorno_200

#
# Emissão de NF-e
#
from nfe_200 import NFe as NFe_200
from nfe_200 import NFRef as NFRef_200
from nfe_200 import Det as Det_200
from nfe_200 import DI as DI_200
from nfe_200 import Adi as Adi_200
from nfe_200 import Med as Med_200
from nfe_200 import Arma as Arma_200
from nfe_200 import Reboque as Reboque_200
from nfe_200 import Vol as Vol_200
from nfe_200 import Lacres as Lacres_200
from nfe_200 import Dup as Dup_200
from nfe_200 import ObsCont as ObsCont_200
from nfe_200 import ObsFisco as ObsFisco_200
from nfe_200 import ProcRef as ProcRef_200

#
# Envio de lote de NF-e
#
from envinfe_200 import EnviNFe as EnviNFe_200
from envinfe_200 import RetEnviNFe as RetEnviNFe_200

#
# Consulta do recibo do lote de NF-e
#
from consrecinfe_200 import ConsReciNFe as ConsReciNFe_200
from consrecinfe_200 import RetConsReciNFe as RetConsReciNFe_200
from consrecinfe_200 import ProtNFe as ProtNFe_200
from consrecinfe_200 import ProcNFe as ProcNFe_200

#
# Cancelamento de NF-e
#
from cancnfe_200 import CancNFe as CancNFe_200
from cancnfe_200 import RetCancNFe as RetCancNFe_200
from cancnfe_200 import ProcCancNFe as ProcCancNFe_200

#
# Inutilização de NF-e
#
from inutnfe_200 import InutNFe as InutNFe_200
from inutnfe_200 import RetInutNFe as RetInutNFe_200
from inutnfe_200 import ProcInutNFe as ProcInutNFe_200

#
# Consulta a situação de NF-e
#
from conssitnfe_200 import ConsSitNFe as ConsSitNFe_200
from conssitnfe_200 import RetConsSitNFe as RetConsSitNFe_200

#
# Consulta a situação do serviço
#
from consstatserv_200 import ConsStatServ as ConsStatServ_200
from consstatserv_200 import RetConsStatServ as RetConsStatServ_200

#
# Consulta cadastro
#
#from conscad_101 import ConsCad as ConsCad_101
#from conscad_101 import RetConsCad as RetConsCad_101