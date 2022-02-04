from os import add_dll_directory
from pycep_correios import get_address_from_cep, WebService
from geopy.geocoders import Nominatim
from geopy.distance import distance
from ipregistry import IpregistryClient
import geocoder
import time as tm 
import json
import urllib

GEO_API_KEY = 'ao0086vefvuncmph'
url = 'https://api.ipregistry.co/?key=' + GEO_API_KEY

print('Getting user local')

entregasCEP = [
                
                {'CEP': '06233-250', 'NUMBER': '146'},
                
                {'CEP': '06233-251', 'NUMBER': '147'},
                
                {'CEP': '06233-252', 'NUMBER': '148'}
              
               ]



user_CEP = entregasCEP[0]['CEP']
user_house_number = entregasCEP[0]['NUMBER']

print(user_CEP, user_house_number)

def get_user_local():

    address = get_address_from_cep(user_CEP, webservice=WebService.CORREIOS)
    
    local_sended = address['logradouro'] + '  '+ user_house_number + '  ' + address['cidade']  
        
    local = Nominatim(user_agent="getLoc") 
    
    getLoc = local.geocode(local_sended) 
    latitude = getLoc.latitude 
    longitude = getLoc.longitude 

    user_local = round(latitude,4), round(longitude,4)

    return user_local

print('Getting Van local')

def get_dist_van_to_local():
    resource = urllib.request.urlopen(url)
    payload = resource.read()
    latitude = json.loads(payload)['location']['latitude']
    longitude = json.loads(payload)['location']['longitude']
    vanLocation = round(latitude,4), round(longitude,4)
    dist = distance(vanLocation, get_user_local()).m # encontra distancia entre a van e o endereço do usuario
    return dist