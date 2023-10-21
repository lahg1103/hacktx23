import requests
from flight_data import FlightData

class GoogleSearch:
    def __init__(self):
        self.api_key = "AIzaSyC4pBLI_aO1wN9PfO3Z7Ebq9bcgPM-0BkQ"

    def search(self):
        flight_info = FlightData()
        params = {
            "origin": flight_info.from_city_code,
            "destination": flight_info.to_city_code,
            "operatingCarrierCode": 0,
            "flightNumber": flight_info.flight_no,
            "departureDate": {
                "year":2000,
                "month":2,
                "day":7
            }
        }
        response = requests.get(url=f"https://travelimpactmodel.googleapis.com/v1/flights:computeFlightEmissions?key={self.api_key}", params=params)
        response.raise_for_status
