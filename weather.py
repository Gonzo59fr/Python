import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=f7ae191dccb8d0627661f101a2ce2f72&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
format_add = json_data['weather'][0]['description']
print(format_add)
