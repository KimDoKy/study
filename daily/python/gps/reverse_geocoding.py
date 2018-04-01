import requests
import json

def get_address(country, lat, lng, api_key):
    url = "https://maps.googleapis.com/maps/api/geocode/json?language=%s&latlng=%f,%f&key=%s" % (country, lat, lng, api_key)   
    r = requests.get(url).json()
    new_full_adr = r['results'][1]['formatted_address']
    city = r['results'][1]['address_components'][-3]['long_name']
    local = r['results'][1]['address_components'][-2]['long_name']
    country = r['results'][1]['address_components'][-1]['long_name']
    old_full_adr = r['results'][0]['formatted_address']
    return new_full_adr, old_full_adr, country, city, local
