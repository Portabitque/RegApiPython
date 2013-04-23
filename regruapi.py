import regru
from urllib.parse import urlencode
from urllib.request import urlopen

class regRuApi:
 def __init__(self):
  pass
 def domainNop(varDomen):
   RegRu = regru.RegRu()
   domain = varDomen
   apiPathDir = '/domain/nop?'

   params = {
    'username' : 'test',
    'password' : 'test',
    'output_content_type':'plain',
    'show_input_params':1,
    'domain_name': domain
    }

   response = urlopen(RegRu.generateApiUrl(apiPathDir, params)) 
   jdata = eval(response.read().decode('utf8'))
   if(RegRu.checkCurrentErrors(jdata) == 1):
    return jdata
   else:
    return RegRu.checkCurrentErrors(jdata)