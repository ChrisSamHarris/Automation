import requests 
import keys as k
import json
import weather_advanced_meta as meta
from datetime import date

print("\n")
TODAY = date.today()
todays_date = TODAY.strftime("%dth %B %Y")

TODAY_API_KEY = k.TODAY_API_KEY #SENSITIVE (Do NOT SHARE) - Create an account and insert your API KEY here** https://openweathermap.org/
FORECAST_API_KEY = k.FORECAST_API_KEY

TODAY_BASE_URL = "https://api.openweathermap.org/data/2.5/weather" #Current Weather Data
FORECAST_BASE_URL = "https://api.openweathermap.org/data/2.5/forecast" #Call 5 day / 3 hour forecast data - Weather forecast data with a 3 hour step

DIVIDE = 0

city = "Manchester"
#city = input("Please enter a city name: ").title()
request_url_today = f"{TODAY_BASE_URL}?appid={TODAY_API_KEY}&q={city}"
request_url_forecast = f"{FORECAST_BASE_URL}?q={city}&appid={FORECAST_API_KEY}"
response_today = requests.get(request_url_today)
response_forecast = requests.get(request_url_forecast)
status_code_today = response_today.status_code
status_code_forecast = response_forecast.status_code

print("\n...")
if status_code_today == 200:
    print("Connection for todays weather: SUCCESS\n") #HTTP200 - Healthy
else:
    print("Connection for todays weather: FAILURE\n")

print("...")
if status_code_forecast == 200:
    print("Connection for forecasted weather: SUCCESS\n") #HTTP200 - Healthy
else:
    print("Connection for forecasted weather: FAILURE\n")


print("====== Current Weather ======")
print(f"Todays Date: {todays_date}\n")
if status_code_today == 200:
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

print("====== Forecasted Weather ======")
# Data-time is provided in Time of data forecasted, unix, UTC
indx = 31
if status_code_forecast == 200:
    forecast_data = response_forecast.json()
    weather_forecast = forecast_data['list'][indx]['dt'] #We only want TWO days of the 4 day weather forecast - Need to create an average temperature function for the days - if this ran at 6pm on a monday we would need approx the first 16 rows of data
    print(meta.unix_time_conversion(weather_forecast))
    #print(weather_forecast) - Returns UNIX time
    forecast_weather_descrption = forecast_data['list'][indx]['weather'][0]['description'] # The Dictionary is WITHIN a list, needed to specify the dictionary item and then the key!
    print(f"\nWeather Description: {forecast_weather_descrption.title()}")
    static_forecasted_temp = round(forecast_data['list'][indx]['main']['temp'] - 273.15, 2)
    print(f"Forecasted Temperature : {static_forecasted_temp}°C\n")
    forecast_temp_num = 0
    for num in range(8, 18): 
        ###
        # Need to decipher how to break this down into only core hours forecast i.e. 8am - 6pm
        # cut weather in two seperate values - TUE and WED
        ###
        forecast_temp = round(forecast_data['list'][num]['main']['temp'] - 273.15, 2)
        #print(f"{forecast_temp}°C")
        forecast_temp_num += forecast_temp
        DIVIDE += 1

    forecast_avg_temp = round(forecast_temp_num / DIVIDE, 2)
    #print(f"Average Forecasted Temperature : {forecast_avg_temp}°C\n")

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