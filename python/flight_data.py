class FlightData:
    def __init__(self, price, from_city, from_city_code, from_airport, to_city, to_city_code, to_airport, out_date, return_date, link, flight_no, operating_carrier):
        self.price = price
        self.from_city = from_city
        self.from_city_code = from_city_code
        self.from_airport = from_airport
        self.to_city = to_city
        self.to_city_code = to_city_code
        self.to_airport = to_airport
        self.out_date = out_date
        self.return_date = return_date
        self.link = link
        self.flight_no = flight_no
        self.operating_carrier = operating_carrier

        