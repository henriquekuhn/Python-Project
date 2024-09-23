from dotenv import load_dotenv
import os
import requests
from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

load_dotenv()

data_manager = DataManager()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()

#print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

    #print(f"sheet_data:\n {sheet_data}")
else:
    flight_search = FlightSearch()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(30*6))

for destination in sheet_data:
    
    flight = flight_search.check_flights(destination["iataCode"], tomorrow, six_months_from_today)
    
    if flight != None and flight.price < destination["lowestPrice"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            )
    
