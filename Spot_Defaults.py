import os
import datetime


# All Global Time
spotterTimeDate=datetime.datetime.now()
spotterTimeDateStr=str(spotterTimeDate)

# Default values
xDefault=os.environ["s_xDefault"]
yDefault=os.environ["s_yDefault"]
dmrIdDefault=os.environ["s_dmrIdDefault"]
callsignDefault=os.environ["s_callsignDefault"]
callsignPrefix='KK6'
gridDefault=os.environ["s_gridDefault"]
postalcodeDefault=os.environ["s_postalcodeDefault"]
cityDefault=os.environ["s_cityDefault"]
stateDefault=os.environ["s_stateDefault"]

# Google API Path/Key
googleGeoCodeServiceUrl = 'https://maps.googleapis.com/maps/api/geocode/json?'
googleGeoPreKey='&key='

# Nasa API
nasaServiceUrl='https://api.nasa.gov/DONKI/FLR?'
nasaPreAttribute1='startDate=2016-01-01'
nasaPreAttribute2='&endDate=2016-01-30'
nasaKey='&api_keyDEMO_KEY'
nasaPostAttribute1=''

# Solar API
solarServiceUrl='http://www.hamqsl.com/solarxml.php'

# Amrron Condition feed
amrronConditionServiceUrl='https://amrron.com/net-resourcestools/amcon-amrron-communications-condition-level/feed/'

#Accu Weather API
accuWeatherServiceUrl = ' "http://dataservice.accuweather.com/locations/v1/postalcodes/search'
accuWeatherPreKey='?apikey='
accuWeatherPreParameter='&q='
accuWeatherPostParameter='&language=en-us&details=false'
#http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey=&q=94611&language=en-us&details=false
accuWeatherLocationKey='347626'
#http://dataservice.accuweather.com/locations/v1/cities/search?apikey=&q=Oakland&details=true

#Open Weather API
# 96hrs weather forecast
openWeatherServiceUrl = 'https://api.openweathermap.org/data/2.5/forecast?zip='
openWeatherPreKey='&appid='

# USGS Earthquake JSON
USGSEarthquakeServiceUrl='https://earthquake.usgs.gov/fdsnws/event/1/application.json?'
USGSEarthquakeAllDayServiceUrl='https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
USGSMethod01='format=geojson'
    # DateTime
USGSDateTime=datetime.datetime.now()
    # Longitude (Positive/Negative 90-,90 range)
USGSParameter01=xDefault
    # Lattitude (Positive/Negative -180,180)
USGSParameter02=yDefault
    # Maxradius (0,180)
USGSParameter03='maxradius' 
    # order results by time ascending
USGSParameter04='orderby=time-asc'