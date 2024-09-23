from user import Users
from dotenv import load_dotenv
import os
import requests
from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()

print("woooo-hoooo, Welcome to Rosbiff's Flights Club!!!")
print("I gonna find the best flight deals and email you. But first, I need some personal information:")
add_user = input("Would you like to add new user (y/n)?")
if add_user == "y":
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    email = input("What is your email: ")
    confirm_email = input("Confirm your email: ")

    new_user = Users(first_name, last_name, email)
    new_user.add_new_user()

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

for destination_code in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code["iataCode"],
        from_date=tomorrow,
        to_date=six_months_from_today
    )

    if flight is None:
        continue

    if flight.price < destination_code["lowestPrice"]:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

       
        
        notification_manager.send_emails(emails, message)
