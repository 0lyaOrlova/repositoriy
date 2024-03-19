import requests
from PIL import Image
from io import BytesIO
import sys

api_server = 'http://static-maps.yandex.ru/1.x/'
toponim = ' '.join(sys.argv[1:])
geocoder_api = 'http://static-maps.yandex.ru/1.x/'
params = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'geocode': toponim,
    'format': 'json'
}
response = requests.get(api_server, params=params)
if not response:
    ...
else:
    json_response = response.json()
    coords = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
lon, lat = coords.split(' ')
delta = '0.005'

map_params = {
    'll': ','.join([lon, lat]),
    'spn': ','.join([delta, delta]),
    'l': 'sat'
}
api_server = 'http://static-maps.yandex.ru/1.x/'
response = requests.get(api_server, params=map_params)
Image.open(BytesIO(response.content)).show()