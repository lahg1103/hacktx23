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
            'distance': 300,
         
        }
        method = 'nearby'
        api_base = 'http://airlabs.co/api/v9/'
        response = requests.get(api_base+method, params)
        
        iatas = []
        cities = []
        countries = []
        count = 0; 
        for code in response.json()["response"]["airports"]:
            if (code["iata_code"]): 
                iatas.append(code["iata_code"])
                cities.append(response.json()["response"]["cities"][count]["name"])
                countries.append(response.json()["response"]["cities"][count]["country_code"])
        return iatas, cities, countries
    
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
        lat = response.json()["request"]["client"]["geo"]["lat"]
        lng = response.json()["request"]["client"]["geo"]["lng"]

        return city, lat, lng