import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

NUTRITION_ID = os.getenv("NT_APP_ID") 
NUTRITION_KEY = os.getenv("NT_API_KEY")

NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

#Bearer Token Authentication
bearer_headers = {
    "Authorization": f"Bearer {os.getenv('TOKEN')}"
    }

#Get Exercise Stats with Natural Language Queries
#input example: Ran 5km in 20 minutes.
exercise_text = input("Which exercises you did: ")

nutrition_params = {
    "query": exercise_text, 
    "weight_kg": 90,
    "height_cm": 178,
    "age": 33
}

header = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_KEY
}

response = requests.post(url=NUTRITION_ENDPOINT, json=nutrition_params, headers=header)
result = response.json()
print(result)

username = "9ab5c917ae5bab038b6a498359347229"
projectName = "myWorkouts"
sheetName = "workouts"
sheety_endpoint = f"https://api.sheety.co/{username}/{projectName}/{sheetName}"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=bearer_headers)
    print(sheet_response.text)
