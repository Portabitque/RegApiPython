#import regru
import config
#from regru import RegRu
from urllib.parse import urlencode
from urllib.request import urlopen

class regRuApiDomain:
 def __init__(self):
  pass

#Получаем функцию у регру
 def getApi(params, action):
   RegRu = regru.RegRu()
   apiPathDir = config.domainGlobalConsts.pathPrefix + action + config.domainGlobalConsts.pathPostfix
   response = urlopen(RegRu.generateApiUrl(apiPathDir, params)) 
   jdata = eval(response.read().decode('utf8'))
   if(RegRu.checkCurrentErrors(jdata) == 1):
    return jdata
   else:
    return RegRu.checkCurrentErrors(jdata)