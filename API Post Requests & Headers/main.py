#### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ####
#### URL TO ACCESS THE GRAPH: https://pixe.la/v1/users/cafrunikuhn/graphs/graph1.html ####

import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USER_NAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

##### CREATE MY USER #####
pixela_enpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes" 
}
# USER FOR CREATE THE USER
#response = requests.post(url=pixela_enpoint, json=user_params)
#print(response.text)

##### CREATE A NEW GRAPH DEFINITION #####
graph_endpoint = f'{pixela_enpoint}/{USERNAME}/graphs'

graph_congfig = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_congfig, headers=headers)
#print(response.text)

##### POST NEW PIXEL #####
today = datetime.now()
ENTRY_DATE = today.strftime("%Y%m%d")

pixel_endpoint = f"{pixela_enpoint}/cafrunikuhn/graphs/{GRAPH_ID}"
pixel_config = {
    "date": ENTRY_DATE,
    "quantity": input("How many kilometer did you cycle today: ")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

##### PUT -> UPDATE EXISTING PIXEL #####
update_endpoint = f"{pixela_enpoint}/{USERNAME}/graphs/{GRAPH_ID}/{ENTRY_DATE}"

#response = requests.put(url=update_endpoint, json=pixel_config, headers=headers)
#print(response.text)

##### DELETE -> DELETE EXISTING PIXEL #####
#response = requests.delete(url=update_endpoint, headers=headers)
#print(response.text)

