import smtplib
import datetime as dt

my_email = "kuhn.python@gmail.com"
password = "jijdcdzqrnkizysr"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs="iticafruni@hotmail.com", 
                        msg="Subject: Hello\n\nThis is the body message.")


now = dt.datetime.now()
print(now)
date_of_birth = dt.datetime(year=1990, month=5, day=27)
print(date_of_birth)