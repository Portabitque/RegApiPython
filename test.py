import regruapi

params = {
    'username' : 'test',
    'password' : 'test',
    'show_renew_data' : 1,
    'show_update_data' : 1,
    'currency' : 'RUR',
    'output_content_type':'plain',
    'show_input_params':0,
    }
params1 = {
    'username' : 'test',
    'password' : 'test',
    'output_content_type':'plain',
    'show_input_params':0,
    'domain_name': 'reg.ru'
    }
print (regruapi.regRuApiDomain.getApi(params1,'nop'))
print (regruapi.regRuApiDomain.getApi(params,'get_prices'))