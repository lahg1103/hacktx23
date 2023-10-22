import requests
from python.flight_data import FlightData
import datetime as dt
from datetime import timedelta

class GoogleSearch:
    def __init__(self):
        self.api_key = "AIzaSyC4pBLI_aO1wN9PfO3Z7Ebq9bcgPM-0BkQ"
        self.today = dt.datetime.now().strftime("%d/%m/%Y")
        self.sixmonths = dt.datetime.now() + timedelta(days=(6 * 30))
        self.next_date = 

    def search(self, origin, destination, operatingCarrierCode, flightNumber):
    #flight_info = FlightData()
        params = {
            "origin": origin,
            "destination": destination,
            "operatingCarrierCode": operatingCarrierCode,
            "flightNumber": flightNumber,
            "departureDate": {
                "year": self.next_date.split("-")[0],
                "month": self.next_date.split("-")[1],
                "day": self.next_date.split("-")[2]
            }
        }
        response = requests.get(url=f"https://travelimpactmodel.googleapis.com/v1/flights:computeFlightEmissions?key={self.api_key}", params=params)
        response.raise_for_status
        data = response.json()["flightEmission"][0]["emissionGramsPerPax"]
        
        return data
