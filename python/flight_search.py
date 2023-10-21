import requests
from flight_data import FlightData

class FlightSearch:
    def __init__(self):
        self.api_key = "iU9_tEkv_I7zvvau3VbbX81zWamNeLqP"
        self.url = "https://api.tequila.kiwi.com/v2/search"
        

    def search(self, city_from, city_to_fly, date_from, date_to):
        header = {
            "apikey": self.api_key
        }

        parameters = {
            "fly_from": city_from,
            "fly_to": city_to_fly,
            "date_fly": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "curr": "USD",
            "max_stopovers": 0
        }

        response = requests.get(url=self.url, params=parameters, headers=header)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print("Index Error")
        else:
            flight_info = FlightData(
                price=data["price"],
                from_city=data["route"][0]["cityFrom"],
                from_city_code=data["route"][0]["cityCodeFrom"],
                from_airport=data["route"][0]["flyFrom"],
                to_city=data["route"][0]["cityTo"],
                to_city_code=["route"][0]["cityCodeTo"],
                to_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                link=data["deep_link"],
                flight_no=data["route"][0]["flight_no"]
            )
            return flight_info


