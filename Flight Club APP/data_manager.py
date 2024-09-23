from dotenv import load_dotenv
import os
import requests

load_dotenv()

#### SHEETY AUTHENTICATION ####

username = "9ab5c917ae5bab038b6a498359347229"
projectName = "flightDeals"
sheetName = "prices"
sheety_prices_endpoint = f"https://api.sheety.co/{username}/{projectName}/prices"#Bearer Token Authentication
sheety_users_endpoint = f"https://api.sheety.co/{username}/{projectName}/users"#Bearer Token Authentication
bearer_headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
    }

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url=sheety_prices_endpoint, headers=bearer_headers)
        data = sheet_response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data
    

    def update_destination_data(self):
        #print(self.destination_data)
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_prices_endpoint}/{city['id']}",
                json=new_data,
                headers=bearer_headers
            )
            #print(response.text)
    
    def get_customer_emails(self):
        customers_endpoint = sheety_users_endpoint
        response = requests.get(url=customers_endpoint, headers=bearer_headers)
        data = response.json()
        print(data)
        self.customer_data = data["users"]
        return self.customer_data

