import requests
from PIL import Image
from io import BytesIO

api_server = 'http://search-maps.yandex.ru/v1/'
api_key = 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3'

address_ll = '37.588392, 55.734036'
params = {
    'apikey': api_key,
    'text': 'apteka',
    'll': address_ll,
    'lang': 'ru_RU',
    'type': 'biz'
}
response = requests.get(api_server, params=params)
if not response:
    ...
else:
    json_response = response.json()
    organisation = json_response['features'][0]
    name = organisation['properties']['CompanyMetaData']['name']
    address = organisation['properties']['CompanyMetaData']['address']
    point = organisation['geometry']['coordinates']
    org_point = f'{point[0]}, {point[0]}'
    delta = '0.005'

map_params = {
    'll': address_ll,
    'spn': ','.join([delta, delta]),
    'l': 'sat',
    'pt': f'{org_point}, pm2dgl'
}
api_server = 'http://static-maps.yandex.ru/1.x/'
response = requests.get(api_server, params=map_params)
Image.open(BytesIO(response.content)).show()