import requests
from twilio.rest import Client
from datetime import datetime, timedelta
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
today = datetime.now().date()
yesterday = today - timedelta(days=1)
before_yesterday = today - timedelta(days=2)


ETF_URL = f'https://www.alphavantage.co/query'
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("KEY")
} 
response = requests.get(ETF_URL, params=params)
response.raise_for_status()
tesla_stock = response.json()

tesla_data = tesla_stock["Time Series (Daily)"]
tesla_data_list = [value for (key, value) in tesla_data.items()]
yesterday_close_price = tesla_data_list[0]["4. close"]
before_yesterday_close_price = tesla_data_list[1]["4. close"]

difference = round(float(yesterday_close_price) - float(before_yesterday_close_price))

symbol = None
if difference > 0:
    symbol = "🔺"
else:
    symbol = "🔻"
diff_percent = (difference / float(yesterday_close_price)) * 100
if abs(diff_percent) > 5:
   print("Get News")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_params = {
    "apiKey": os.getenv("NEWS_KEY"),
    "q": COMPANY_NAME,
    "language": "en"
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
articles = news_response.json()["articles"]
three_articles = articles[:3]

formated_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}." for article in three_articles]
#print(formated_articles)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

print(diff_percent)
if abs(diff_percent) > 5:
    for article in formated_articles:
        client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))
        message = client.messages.create(
            body=f"{COMPANY_NAME}: {symbol}{diff_percent}%\n {article}",
            from_='+12566023791',
            to=os.getenv("TWILIO_VERIFIED_NUMBER")
            )
