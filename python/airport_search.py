import requests
import json

class AirportSearch: 
    def __init__(self):
        pass

    def search(self, lat, lng):
        params = {
            'api_key': '56bee120-b2e2-4a86-bb67-41cd7110a28f',
            'lat': lat, 
            'lng': lng, 
            'distance': 3000,
         


        }
        method = 'nearby'
        api_base = 'http://airlabs.co/api/v9/'
        response = requests.get(api_base+method, params)
        data = response.json()["response"]["airports"][0]["iata_code"]
        return data