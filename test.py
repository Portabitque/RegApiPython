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

paramsSuggest = {
    'username' : 'test',
    'password' : 'test',
    'output_content_type':'plain',
    'show_input_params' : 0,
    'word' : 'test', # Главное ключевое слово, например «дом» или «domain». Обязательное поле.
#    'additional_word' : 'regru', # Дополнительное ключевое слово, например «новый» или «cool». Необязательное поле.
#    'category' : 'search_trends', # Категория подбираемых имён. Может принимать значения: 'pattern' — шаблонные («имя + префикс»), 'search_trends' — поисковые тренды, 'all' — все. По умолчанию возвращаются имена из всех категорий.
#    'use_hyphen' : 1, # Если значение истинно, использовать дефис в для разделения отдельных слов в доменном имени ("cool-domain"). По умолчанию слова склеиваются без разделителя ("cooldomain").
#    'use_plural' : 1, # Если значение истинно, предлагать варианты во множественном числе. Необязательное поле.
#    'tlds' : 'ru' # Зона, в которой проверяется доступность доменного имени к регистрации. Зоны могут быть такими: 'ru', 'рф', 'su', 'com', 'net', 'org', 'biz', 'info'. Для задания нескольких зон одновременно, необходимо добавить в запрос это поле для каждой зоны: например "...&tlds=ru&tlds=su&tlds=com". Если поле не задано ни разу, то доступность проверяется во всех перечисленных выше зонах.
    }


print (regruapi.regRuApiDomain.getApi(paramsSuggest,'get_suggest'))
#print (regruapi.regRuApiDomain.getApi(params,'get_prices'))