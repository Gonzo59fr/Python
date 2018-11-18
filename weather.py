import requests
import datetime
from datetime import datetime

#api requests
current_weather_api='http://api.openweathermap.org/data/2.5/weather?appid=f7ae191dccb8d0627661f101a2ce2f72&units=metric&lang=fr&q='
five_days_weather_forecast_api='http://api.openweathermap.org/data/2.5/forecast?appid=f7ae191dccb8d0627661f101a2ce2f72&units=metric&lang=fr&mode=json&q='

#user input
city = input('City Name :')

#################
#CURRENT WEATHER#
#################

#city adding
current_weather_url = current_weather_api + city

#json calls
json_data_current_weather = requests.get(current_weather_url).json()
current_weather = json_data_current_weather['weather'][0]['description']
current_temperature = json_data_current_weather['main']['temp']
current_windspeed = json_data_current_weather['wind']['speed']

#results display
print('\n*** Météo actuelle à ',city,' ***')
print('Ciel : ',current_weather)
print('Température : ',int(current_temperature),'°C')
print('Vitesse du vent : ',int(current_windspeed),'km/h')

####################
#WEATHER IN ONE DAY#
####################

#city adding
five_days_weather_forecast_url = five_days_weather_forecast_api + city

#json calls
json_data_five_days_weather_forecast = requests.get(five_days_weather_forecast_url).json()
time_in_one_day = json_data_five_days_weather_forecast['list'][7]['dt']
weather_in_one_day = json_data_five_days_weather_forecast['list'][7]['weather'][0]['description']
temperature_in_one_day = json_data_five_days_weather_forecast['list'][7]['main']['temp']
windspeed_in_one_day = json_data_five_days_weather_forecast['list'][7]['wind']['speed']

#results display
print('\n*** Prévisions météo pour le',(datetime.utcfromtimestamp(time_in_one_day).strftime('%d/%m/%Y %Hh')), ' à ',city,' ***')
print('Ciel : ',weather_in_one_day)
print('Température : ',int(temperature_in_one_day),'°C')
print('Vitesse du vent : ',int(windspeed_in_one_day),'km/h')

####################
#WEATHER IN TWO DAY#
####################

#city adding
five_days_weather_forecast_url = five_days_weather_forecast_api + city

#json calls
json_data_five_days_weather_forecast = requests.get(five_days_weather_forecast_url).json()
time_in_two_day = json_data_five_days_weather_forecast['list'][15]['dt']
weather_in_two_day = json_data_five_days_weather_forecast['list'][15]['weather'][0]['description']
temperature_in_two_day = json_data_five_days_weather_forecast['list'][15]['main']['temp']
windspeed_in_two_day = json_data_five_days_weather_forecast['list'][15]['wind']['speed']

#results display
print('\n*** Prévisions météo pour le',(datetime.utcfromtimestamp(time_in_two_day).strftime('%d/%m/%Y %Hh')), ' à ',city,' ***')
print('Ciel : ',weather_in_two_day)
print('Température : ',int(temperature_in_two_day),'°C')
print('Vitesse du vent : ',int(windspeed_in_two_day),'km/h')

######################
#WEATHER IN THREE DAY#
######################

#city adding
five_days_weather_forecast_url = five_days_weather_forecast_api + city

#json calls
json_data_five_days_weather_forecast = requests.get(five_days_weather_forecast_url).json()
time_in_three_day = json_data_five_days_weather_forecast['list'][23]['dt']
weather_in_three_day = json_data_five_days_weather_forecast['list'][23]['weather'][0]['description']
temperature_in_three_day = json_data_five_days_weather_forecast['list'][23]['main']['temp']
windspeed_in_three_day = json_data_five_days_weather_forecast['list'][23]['wind']['speed']

#results display
print('\n*** Prévisions météo pour le',(datetime.utcfromtimestamp(time_in_three_day).strftime('%d/%m/%Y %Hh')), ' à ',city,' ***')
print('Ciel : ',weather_in_three_day)
print('Température : ',int(temperature_in_three_day),'°C')
print('Vitesse du vent : ',int(windspeed_in_three_day),'km/h')

#####################
#WEATHER IN FOUR DAY#
#####################

#city adding
five_days_weather_forecast_url = five_days_weather_forecast_api + city

#json calls
json_data_five_days_weather_forecast = requests.get(five_days_weather_forecast_url).json()
time_in_four_day = json_data_five_days_weather_forecast['list'][31]['dt']
weather_in_four_day = json_data_five_days_weather_forecast['list'][31]['weather'][0]['description']
temperature_in_four_day = json_data_five_days_weather_forecast['list'][31]['main']['temp']
windspeed_in_four_day = json_data_five_days_weather_forecast['list'][31]['wind']['speed']

#results display
print('\n*** Prévisions météo pour le',(datetime.utcfromtimestamp(time_in_four_day).strftime('%d/%m/%Y %Hh')), ' à ',city,' ***')
print('Ciel : ',weather_in_four_day)
print('Température : ',int(temperature_in_four_day),'°C')
print('Vitesse du vent : ',int(windspeed_in_four_day),'km/h')


