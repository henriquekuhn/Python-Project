## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
today = datetime.now().date()
yesterday = today - timedelta(days=1)
before_yesterday = today - timedelta(days=2)
print(yesterday)

KEY = "XPX02DU61DCLARE0"
ETF_URL = f'https://www.alphavantage.co/query'
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": KEY
} 
response = requests.get(ETF_URL, params=params)
response.raise_for_status()
tesla_stock = response.json()

tesla_stock_yesterday = tesla_stock["Time Series (Daily)"][f"{yesterday}"]
tesla_stock_before_yesterday = tesla_stock["Time Series (Daily)"][f"{before_yesterday}"]

print(tesla_stock_yesterday)