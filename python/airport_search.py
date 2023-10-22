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
            'distance': 30000,
         
        }
        method = 'nearby'
        api_base = 'http://airlabs.co/api/v9/'
        response = requests.get(api_base+method, params)
           
        iata = response.json()["response"]["airports"][0]["iata_code"]
        city = response.json()["response"]["cities"][0]["name"]
        api_response = response.json()

        print(city)
        return iata, city
    
    def user_location(self):
        params = {
            'api_key': '56bee120-b2e2-4a86-bb67-41cd7110a28f',
            'params1': 'value1'
         
        }
        method = 'ping'
        api_base = 'http://airlabs.co/api/v9/'
        response = requests.get(api_base+method, params)
        api_response = response.json()

        city = response.json()["request"]["client"]["geo"]["city"]
        #return data