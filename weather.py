import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=f7ae191dccb8d0627661f101a2ce2f72&units=metric&lang=fr&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
weather = json_data['weather'][0]['description']
temperature = json_data['main']['temp']
windspeed = json_data['wind']['speed']
print(weather)
print(temperature)
print(windspeed)
