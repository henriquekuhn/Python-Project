import requests
from flight_data import FlightData


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "GX0cX2pLQvMxgowJ9zROX7yI2V2BAr9x"
HEADERS = {"apikey": TEQUILA_API_KEY}

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        
        query = {"term": city_name, 
                 "location_types": "city",
                 "location_types": "airport"}
        print(city_name)
        response = requests.get(url=location_endpoint, params=query, headers=HEADERS)
        result = response.json()["locations"]
        code = result[0]["code"]    
        return code
    
    def check_flights(self, destination, from_date, to_date):
        
        flights_endpoint = f"{TEQUILA_ENDPOINT}/search"
        query = {"fly_from": "LON",
                 "fly_to": destination,  
                 "date_from": from_date.strftime("%d/%m/%Y"),
                 "date_to": to_date.strftime("%d/%m/%Y"),
                 "nights_in_dst_from": 7,
                 "nights_in_dst_to": 28,
                 "one_for_city": 1,
                 "max_stopovers": 0,
                 "curr": "GBP"
                 }
        response = requests.get(url=flights_endpoint, params=query, headers=HEADERS)
        try:    
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["dTimeUTC"],
            return_date=data["route"][0]["aTimeUTC"]
        )

        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data