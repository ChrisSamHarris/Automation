import requests 
import keys as k
import json

TODAY_API_KEY = k.TODAY_API_KEY #SENSITIVE (Do NOT SHARE) - Create an account and insert your API KEY here** https://openweathermap.org/
FORECAST_API_KEY = k.FORECAST_API_KEY

TODAY_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

city = "Manchester"
request_url_today = f"{TODAY_BASE_URL}?appid={TODAY_API_KEY}&q={city}"
request_url_forecast = f"{FORECAST_BASE_URL}?q={city}&appid={FORECAST_API_KEY}"
response_today = requests.get(request_url_today)
response_forecast = requests.get(request_url_forecast)

print(response_today) #HTTP200 - Healthy
print(response_forecast) #HTTP401 - Unauthorised? 

#==== Current Weather ====#
# if response_today.status_code == 200:
#     data = response_today.json()
#     print("Connection Success!")
#     weather = data['weather'][0]['description']
#     print(f"Weather Description: {weather}")
#     temp = round(data["main"]["temp"] - 273.15, 2)
#     print(f"Temperature in Celcius : {temp}")

# else:
#     print("Connection Failure.")

#==== Current Weather ====#
if response_forecast.status_code == 200:
    forecast_data = response_forecast.json()
    print("Connection Success!")
    print(forecast_data)
    with open('data.json', "w") as f:
        json.dump(forecast_data, f) 
    #weather = data['weather'][0]['description']
    #print(f"Weather Description: {weather}")
    #temp = round(data["main"]["temp"] - 273.15, 2)
    #print(f"Temperature in Celcius : {temp}")

else:
    print("Connection Failure.")

# ===== Notes =====
#Forecast : Weather is in unix data forecast - time from jan1 - 1970 - Conversion? 
#Average of weather and temp for a 2 day period? 
#Create a list/ Dictionary from the Json file and then iterate the next X days - 2 days if its re. office 
#Shell script to automate the job on a tuesday midday? 
#for loop so if a forecast says rain it highlights "Rain is forecast!" - Advanced - highlight which day and time 



#Future task - Python & CronJob (possibly schedule? ) - Create a Python job that gets the days weather and then create an email to send the weather forecast to my email in the morning