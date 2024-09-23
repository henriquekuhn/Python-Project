import smtplib
import datetime as dt
import os
import random
import pandas

DIR = os.getcwd() + "/Email Sender"
os.chdir(DIR)

MY_EMAIL = "kuhn.python@gmail.com"
PASSWORD = "jijdcdzqrnkizysr"

try:
    birth_dates = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("FIle not Found!")
finally:
    data_dict = birth_dates.to_dict(orient="records")
    

now = dt.datetime.now()
month = now.month
day = now.day
print(day)
print(month)

for person in data_dict:
    if person["day"] == day and person["month"] == month:
        name = person["name"]
        email = person["email"]
        print(f"PARABENS {name}")

with open("birth_letter.txt") as birth_file:
    content = birth_file.read()
    new_content = content.replace("[NAME]", name)
 

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, 
                    to_addrs=email, 
                    msg=f"Subject: Birthday\n\n{new_content}")