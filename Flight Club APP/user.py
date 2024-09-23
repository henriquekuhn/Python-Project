import requests
from dotenv import load_dotenv
import os

load_dotenv()

#### SHEETY AUTHENTICATION ####

USER_NAME = os.getenv("USER_NAME") 
PROJECT_NAME = os.getenv("PROJECT_NAME") 
SHEET_NAME = os.getenv("SHEET_NAME") 

print(USER_NAME)
USER_NAME = "9ab5c917ae5bab038b6a498359347229"
PROJECT_NAME = "flightDeals"
SHEET_NAME = "users"

sheety_endpoint = f"https://api.sheety.co/{USER_NAME}/{PROJECT_NAME}/{SHEET_NAME}"#Bearer Token Authentication
bearer_headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
    }


class Users:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def add_new_user(self):
        new_user = {
                "user": {
                    "firstName": self.first_name,
                    "lastName": self.last_name,
                    "email": self.email
                }
            }
        response = requests.post(
                url=sheety_endpoint,
                json=new_user,
                headers=bearer_headers
            )
        response.raise_for_status()

        result = response.json()
        print(result)