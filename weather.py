import requests 
import keys as k

API_KEY = k.API_KEY #SENSITIVE (Do NOT SHARE) - Create an account and insert your API KEY here** https://openweathermap.org/
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print("Connection Success!")
    weather = data['weather'][0]['description']
    print(f"Weather Description: {weather}")
    temp = round(data["main"]["temp"] - 273.15, 2)
    print(f"Temperature in Celcius : {temp}")

else:
    print("Connection Failure.")

#Future task - Python & CronJob (possibly schedule? ) - Create a Python job that gets the days weather and then create an email to send the weather forecast to my email in the morning