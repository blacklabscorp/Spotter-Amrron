# Solar conditions
import requests
from bs4 import BeautifulSoup
from Spot_Defaults import solarServiceUrl

def SolarReport():
        page = requests.get(solarServiceUrl)
        soup = BeautifulSoup(page.text,'html.parser')
        print (soup)

# Test Block
#solar=SolarReport()
#print(solar)
