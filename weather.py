
import requests, json
from api import *

def take_city(city):
   #city = str(input("enter the city you want to know it's weather summary:- "))
   city[0].capitalize()
   URL = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '+&appid=' + weather_key
   # HTTP request
   response = requests.get(URL)
   # checking the status code of the request
   if response.status_code == 200:
      # getting data in the json format
      data = response.json()
      # getting the main dict block
      main = data['main']
      # getting temperature
      temperature = main['temp']
      # getting the humidity
      humidity = main['humidity']
      # getting the pressure
      pressure = main['pressure']
      # weather report
      report = data['weather']
      tempo={int(temperature)-273}
      himpo={humidity}
      print(f"Temperature is : {int(temperature)-273}" + ", " + f"Humidityis is : {humidity}"+", "f"Weather Report: {report[0]['description']}")
      return "tempreture is",tempo,"degree celcius.","humidity is " , himpo,"percentage","weather report is " ,{report[0]['description']}

   else:
      # showing the error message
      print("Error in the HTTP request")
