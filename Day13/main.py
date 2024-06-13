import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = "twilio_auth_id"
auth_token = "twilio_auth_token"

stock_apikey = "stock_api"
news_apikey = "new_api"
parameter_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_apikey
}
news_parameter ={
    'apiKey':news_apikey,
    'qInTitle': COMPANY_NAME
}
headlines = []
description = []
response_stock = requests.get(url="https://www.alphavantage.co/query", params= parameter_stock)
data = response_stock.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]

yesterday = float(data_list[0]['4. close'])

day_yesterday = float(data_list[1]['4. close'])

diff = yesterday-day_yesterday
if diff > 0:
    emoji = "🔺"
else:
    emoji = "🔻"

per_diff = round((abs(diff)/yesterday)*100.0, 2)


if per_diff > 1:
    news_response = requests.get(url="https://newsapi.org/v2/everything?",params=news_parameter).json()['articles']
    top3 = news_response[:3]
    for x in top3:
        headlines.append(x['title'])
        description.append(x['description'])

    for x in range(1):
        sms = f"\nTESLA {per_diff}{emoji}\nHeadline:{headlines[x]}\nBrief:{description[x]}"
        client = Client(account_sid,auth_token)
        message = client.messages.create(
            from_='twilioo_virtual_number',
            body=sms,
            to='Your verified number in twilio'
        )



# website for stock details
#https://www.alphavantage.co


# website for news realted stock company
#https://newsapi.org


# website for twilio
#https://www.twilio.com
