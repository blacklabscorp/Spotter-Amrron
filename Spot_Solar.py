# Solar conditions
import requests
from bs4 import BeautifulSoup
from SpotDefaults import solarServiceUrl

def SolarReport():
        page = requests.get(solarServiceUrl)
        soup = BeautifulSoup(page.text,'html.parser')
        print (soup)

#print('Test Block')
#solar=SolarReport()
#print(solar)


# PRE-REQs to run this module
# Process URL requests
	# pip install request or requests
# Web scrapper
	# pip install bs4
