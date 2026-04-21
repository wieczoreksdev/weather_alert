import os

import requests
import os

api_key = os.environ.get("API_KEY_OWM")
auth_token = os.environ.get("AUTH_TWILIO_TOKEN")
auth_twilio_sid = os.environ.get("AUTH_TWILIO_SID")
lat ="41.716667"
lon ="19.700000"

url_forecast = "http://api.openweathermap.org/data/2.5/forecast"
params_forecast = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": "4",
    "units": "metric"
}
response3 = requests.get(
    url=f"{url_forecast}",params=params_forecast)

is_raining = False
for item in response3.json()["list"]:
    if int(item["weather"][0]["id"]) <= 700:
        is_raining = True
if is_raining:

    from twilio.rest import Client
    account_sid = auth_twilio_sid
    auth_token = auth_token
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Halo Sebciu, bedzie dzisiaj padac moze parasoleczka?☂️',
        to='whatsapp:+48883815505'
    )
    print(message.sid)
