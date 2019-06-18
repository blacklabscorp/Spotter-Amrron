# Open Weather Web service
# Library loads
import urllib.request, urllib.parse, urllib.error
import json
import os
import datetime

#Functions:
from pyowm import OWM
from Spot_Defaults import xDefault,yDefault,dmrIdDefault,callsignDefault,postalcodeDefault,gridDefault,openWeatherServiceUrl,openWeatherPreKey

# Constants initialization
openWeatherKey=os.environ["s_openWeatherKey"]
owm=OWM(openWeatherKey)
now = datetime.datetime.now()
date_0day = now.strftime('%Y-%m-%d')
date_1day = now + datetime.timedelta(days=1)
date_2day = now + datetime.timedelta(days=2)
date_3day = now + datetime.timedelta(days=3)


# Cache provider
from pyowm.caches.lrucache import LRUCache
cache=LRUCache()

def DefaultWeather (postalcodeCurrent,postalcodeDefault):
    obs=owm.weather_at_place(postalcodeDefault)
    #obs_list=owm.weather_at_places("Oakland","accurate")
# Wind
    w=obs.get_weather()
    winds={}
    wind=w.get_wind()
    for i in wind:
        winds=(i,wind[i])
        print(date_0day)
        print(winds)
    return (winds)

def ThreeDayForecast(cityStateCurrent):
# Forecaster 3 days
	fc = owm.three_hours_forecast(cityStateCurrent)
	from datetime import datetime
# Day1
	fc.get_weather_at(date_1day)
	print (fc.get_weather_at(date_1day))
# Day2
	fc.get_weather_at(date_2day)
	print (fc.get_weather_at(date_2day))
# Day3
	fc.get_weather_at(date_3day)
	print (fc.get_weather_at(date_3day))


#print('Test Block')
#postalcodeDefault=os.environ["s_postalcodeDefault"]
#postalcodeCurrent=postalcodeDefault
#DefaultWeather(postalcodeCurrent,postalcodeDefault)
#print()
#print()
#cityStateDefault='Oakland,CA'
#cityStateCurrent=cityStateDefault
#ThreeDayForecast(cityStateCurrent)
#print(cityStateCurrent)


# PRE-REQs to run this module
# Process URL requests
	# pip install request or requests
# Libraru for working with Open Weather Maps
	# pip install pyowm 
