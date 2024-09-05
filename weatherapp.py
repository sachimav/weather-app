import requests

api_key='4ac5339e76a647be81b505f10b971df7'
user_input= input("enter city:")

weather_data= requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod']== '404':
    print("city is not found")
else:
    weather= weather_data.json()['weather'][0]['main']
    temp= round(weather_data.json()['main']['temp'])
    
    print(f"weather in {user_input} is: {weather}")
    print(f"temperature in {user_input} is: {temp}ºF")
  
 
