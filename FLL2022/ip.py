import ipregistry
import urllib
import json

GEO_API_KEY = 'ao0086vefvuncmph'
IP = '200.155.128.62'
url = 'https://api.ipregistry.co/'+ IP +'?key=' + GEO_API_KEY



resource = urllib.request.urlopen(url)
payload = resource.read()
latitude = json.loads(payload)['location']['latitude']
longitude = json.loads(payload)['location']['longitude']
print(latitude, longitude)