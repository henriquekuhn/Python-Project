from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

DIR = os.getcwd() + "/Amazon Price Tracker"
os.chdir(DIR)

MAIL_PROVIDER_SMTP_ADDRESS = os.getenv("MAIL_PROVIDER_SMTP_ADDRESS")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

# Practice
URL = "https://appbrewery.github.io/instant_pot/"
# Live Site
#URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Full headers would look something like this
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# A minimal header would look like this:
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }


response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
# Check you are getting the actual Amazon page back and not something else:
print(soup.prettify())

whole_price = soup.find(class_ = "a-price-whole").getText()
decimal_price = soup.find(class_ = "a-price-fraction").getText()

price = float(whole_price + decimal_price)
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

if price < 100:
    message = f"{title} is now {price}"

    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
                )
else:
    print("The price still higher.")