import requests 
import keys as k
import json
from datetime import date
from datetime import datetime

print("\n")
TODAY = date.today()
todays_date = TODAY.strftime("%B %dth %Y")
print(f"Todays Date: {todays_date}")

#### UNIX TIME CONVERSION CALCULATOR #####
#Exmple JSON format: "dt": 1651942690
def unix_time_conversion(unix_ts):
    '''Function that converts UNIX date/time into a user-friendly format.
    if you encounter a "year is out of range" error the timestamp
    may be in milliseconds, try `ts /= 1000` in that case.'''
    ts = int(unix_ts)
    return datetime.utcfromtimestamp(ts).strftime('%B %dth %Y %H:%M')

TODAY_API_KEY = k.TODAY_API_KEY #SENSITIVE (Do NOT SHARE) - Create an account and insert your API KEY here** https://openweathermap.org/
FORECAST_API_KEY = k.FORECAST_API_KEY

TODAY_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

x_http_200 = "<Response [200]>"

city = "Lancaster"
#city = input("Please enter a city name: ").title()
request_url_today = f"{TODAY_BASE_URL}?appid={TODAY_API_KEY}&q={city}"
request_url_forecast = f"{FORECAST_BASE_URL}?q={city}&appid={FORECAST_API_KEY}"
response_today = requests.get(request_url_today)
response_forecast = requests.get(request_url_forecast)
status_code_today = str(requests.get(request_url_today))
status_code_forecast = str(requests.get(request_url_forecast))

print("\n...")
if status_code_today == x_http_200:
    print("Connection for todays weather: SUCCESS\n") #HTTP200 - Healthy
else:
    print("Connection for todays weather: FAILURE\n")

print("...")
if status_code_forecast == x_http_200:
    print("Connection for forecasted weather: SUCCESS\n") #HTTP200 - Healthy
else:
    print("Connection for forecasted weather: FAILURE\n")


print("==== Current Weather ====")
if status_code_today == x_http_200:
    today_data = response_today.json()
    weather = today_data['weather'][0]['description']
    print(f"Today's Current Weather Description: {weather.title()}")
    temp = round(today_data["main"]["temp"] - 273.15, 2)
    print(f"Today's Current Temperature : {temp}°C")

    with open('today_data.json', "w") as today_f:
        json.dump(today_data, today_f) 

else:
    print("Connection Failure.")
print("\n")

print("==== Forecasted Weather ====")
# Data-time is provided in Time of data forecasted, unix, UTC
if status_code_forecast == x_http_200:
    fc_weather_var = 10
    forecast_data = response_forecast.json()
    weather_forecast = forecast_data['list'][fc_weather_var]['dt'] #We only want TWO days of the 4 day weather forecast - Need to create an average temperature function for the days - if this ran at 6pm on a monday we would need approx the first 16 rows of data
    print(unix_time_conversion(weather_forecast))
    print(weather_forecast)
    forecast_weather_descrption = forecast_data['list'][fc_weather_var]['weather']['main'] #Struggling to slice this data
    print(f"Weather Description: {weather}")
    forecast_temp = round(forecast_data['list'][fc_weather_var]['main']['temp'] - 273.15, 2)
    print(f"Forecasted Temperature : {temp}°C")

    with open('forecast_data.json', "w") as forecast_f:
        json.dump(forecast_data, forecast_f) 

else:
    print("Connection Failure.")

# ===== Notes =====
#Average of weather and temp for a 2 day period? 
#Create a list/ Dictionary from the Json file and then iterate the next X days - 2 days if its re. office 
#Shell script to automate the job on a tuesday midday? 
#for loop so if a forecast says rain it highlights "Rain is forecast!" - Advanced - highlight which day and time 



#Future task - Python & CronJob (possibly schedule? ) - Create a Python job that gets the days weather and then create an email to send the weather forecast to my email in the morning