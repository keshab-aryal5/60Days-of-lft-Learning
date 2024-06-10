import requests
from twilio.rest import Client


account_sid = "<sid of account created in twilio>"
auth_token = "<auth_token provided by auth_token>"
api_key = "<unique api_key provided by openweather>"
parameter = {
    "lat": 27.717245, #latitude of kathmandu
    "lon": 85.323959, #longitude of kathmandu
    "cnt": 4,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()
weather_data = response.json()
time_slot = weather_data['list']

will_rain = False
for x in time_slot:
    for y in x["weather"]:
        if y['id'] < 700:
            will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+12073679777',
        body="Pani parni wala xa xata lera jam hai aaja. ☔",
        to='+9779869393678'
    )

    print(message.status)
