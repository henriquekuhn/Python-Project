import smtplib
import datetime as dt
import os
import random

DIR = os.getcwd() + "/Day 32 - Email Sender"
os.chdir(DIR)

MY_EMAIL = "kuhn.python@gmail.com"
PASSWORD = "jijdcdzqrnkizysr"

now = dt.datetime.now()
week_day = now.weekday()
#change for the current week day for debug.
if week_day == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                        to_addrs=MY_EMAIL, 
                        msg=f"Subject: Monday motivation\n\n{quote}")

