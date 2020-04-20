import requests
import json

def barra():
    print('=====================================================')

req = requests.get('https://api.hgbrasil.com/weather') #pegar os dados na API
req2 = json.loads(req.text) #transformar JSON em DICT python

barra()
print('Clima em',req2['results']['city_name'],'-',req2['results']['date'],'(',req2['results']['time'],')','(',(req2['results']['forecast'][0]['weekday']),')','\n')
print('Atual:',req2['results']['temp'],'ºC')
print('Vento:',req2['results']['wind_speedy'])
print('Mín:',req2['results']['forecast'][0]['min'],'ºC')
print('Max:',req2['results']['forecast'][0]['max'],'ºC')
print(req2['results']['description'])
barra()