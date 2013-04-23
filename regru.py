import json
from urllib.parse import urlencode
from urllib.request import urlopen
#from urllib.request import urlencode
'''Базовый класс'''
class RegRu:
 apiPath = 'https://api.reg.ru/api/regru2'
 def __init__(self):
  pass

#Парсим стандартные ошибки. На вход передаем то, что у нас вернулось от АПИ
 def errorParse(self,errorCode):
  dictErrors = {
   'NO_USERNAME' : 'No username given.',
   'NO_AUTH' : 'No authorization mechanism selected.',
   'PASSWORD_AUTH_FAILED' : 'Username/password Incorrect.',
   'RESELLER_AUTH_FAILED' : 'Only resellers can access to this function.',
   'ACCESS_DENIED' : 'Your access to API denied. Please, contact us.',
   'PURCHASES_DISABLED' : 'Purchases disabled for this account.',
   'DOMAIN_NOT_FOUND' : 'Domain domain_name not found or not owned by you',
   'SERVICE_NOT_FOUND' : 'Service $servtype for ext domain $domain_name not found.',
   'SERVICE_NOT_SPECIFIED' : 'Service identification failed.',
   'SERVICE_ID_NOT_FOUND' : 'Service $service_id not found or not owned by You.',
   'NO_DOMAIN' : 'domain_name not given or empty.',
   'INVALID_DOMAIN_NAME_FORMAT' : 'Domain_name is invalid or domain from unsupported zone.',
   'INVALID_SERVICE_ID' : 'Service_id is invalid.',
   'INVALID_DOMAIN_NAME_PUNYCODE' : 'Invalid punycode value for domain_name.',
   'BAD_USER_SERVID' : 'Invalid value for user_servid.',
   'USER_SERVID_IS_NOT_UNIQUE' : 'Not Unique value in user_servid.',
   'TOO_MANY_OBJECTS_IN_ONE_REQUEST' : 'Too many objects (more than 1000) specified in one request.',
   'DOMAIN_BAD_NAME' : 'Invalid domain name:$domain_name',
   'DOMAIN_BAD_NAME_ONLYDIGITS' : 'Domain names that contains only digits can not be registered in this zone',
   'HAVE_MIXED_CODETABLES' : 'You can\'t mix latin and cyrillic letters in domain names',
   'DOMAIN_BAD_TLD' : 'Registration in $tld TLD is not available',
   'TLD_DISABLED' : 'Registration in $tld TLD is not available',
   'DOMAIN_NAME_MUSTBEENG' : 'Russian letters are not allowed in chosen TLD ( $tld )',
   'DOMAIN_NAME_MUSTBERUS' : 'Latin letters are not allowed in chosen TLD ( $tld )',
   'DOMAIN_ALREADY_EXISTS' : 'Domain already exists, use whois service',
   'DOMAIN_INVALID_LENGTH' : 'Invalid domain name length, You have entered too short or too long name',
   'DOMAIN_STOP_LIST' : 'Domain is unavailable, this domain name is either reserved or this is premium-domain with special price',
   'DOMAIN_STOP_PATTERN' : 'Unfortunately domain name ($domain_name) can\'t be registered',
   'FREE_DATE_IN_FUTURE' : 'Domain freeing date is in the long time future',
   'NO_DOMAINS_CHECKED' : 'You have chosen no domains for registration',
   'NO_CONTRACT' : 'Filing preschedule for the domain registration after freeing is impossible before You signing up the contract on the domain registration',
   'INVALID_PUNYCODE_INPUT' : 'Invalud Punycode name (error while converting from punycode)',
   'CONNECTION_FAILED' : 'Domain check failed: can\'t connect to server. Please, try again later',
   'DOMAIN_ALREADY_ORDERED' : 'The domain name $domain_namewas order by you, You can pay for the registration and domain will be registered',
   'DOMAIN_EXPIRED' : 'Domain $domain_name is either expired or will expire in near future',
   'DOMAIN_TOO_YOUNG' : 'From registration date of domain$domain_name passed less than 60 days. Please, try to transfer domain later',
   'CANT_OBTAIN_EXPDATE' : 'Can\'t determine expiration date of domain $domain_name',
   'DOMAIN_CLIENT_TRANSFER_PROHIBITED' : 'Domain $domain_name prohibited for transfer, contact previous registrar to unlock domain transfer',
   'DOMAIN_TRANSFER_PROHIBITED_UNKNOWN' : 'Domain $domain_name transfer prohibited, contact our technical support staff for details',
   'DOMAIN_REGISTERED_VIA_DIRECTI' : 'Automatical internal transfers are unavailable in present time',
   'NOT_FOUND_UNIQUE_REQUIRED_DATA' : 'Not found all data for check unique: dname, servtype or user_id',
   'ORDER_ALREADY_PAYED' : 'Order on $dname $servtype is already payed',
   'DOUBLE_ORDER' : 'You already have not payed order on $dname $servtype',
   'DOMAIN_ORDER_LOCKED' : 'The order of the domain is disabled since processing of other order for the same domain isn\'t completed yet',
   'UNAVAILABLE_DOMAIN_ZONE' : '$tld is unavailable domain zone',
   'DOMAIN_IS_NOT_USE_REGRU_NSS' : 'This domain not use REG.RU name services',
   'REVERSE_ZONE_API_NOT_SUPPORTED' : 'Reverse zone not supported now',
   'ZONES_VARY' : 'Domains in list have vary zones',
   'IP_INVALID' : 'Invalid IP address',
   'SUBD_INVALID' : 'Invalid subdomain',
   'CONFLICT_CNAME' : 'Can not set CNAME record together with other record for one subdomain',
   'NO_SUCH_COMMAND' : 'Command $command_name not found.',
   'HTTPS_ONLY' : 'Access to api over non secure interface (http) prohibited! Please use https only.',
   'PARAMETER_MISSING' : '$param required.',
   'PARAMETER_INCORRECT' : '$param has incorrect format or data.',
   'NOT_ENOUGH_MONEY' : 'Not enough money at account for this operation.',
   'INTERNAL_ERROR' : 'Internal error: $error_detail.',
   'SERVICE_OPERATIONS_DISABLED' : 'Operations on this service disabled',
   'UNSUPPORTED_CURRENCY' : 'Unsupported currency'
   }

  if (errorCode in dictErrors):
     return (dictErrors[errorCode])
  else:
     return ('Unspecified error')
 
#Общая проверка на ошибки
 def checkCurrentErrors(self,variables):
    if ('error_code' in variables) :
      return self.errorParse(variables['error_code'])
    else :
      return 1

#Генерируем общий путь до функции
 def generateApiUrl(self, apiPathDir, params):
    return (self.apiPath + apiPathDir + urlencode(params))