# Solar conditions
import requests
from bs4 import BeautifulSoup
from Spot_Defaults import solarServiceUrl
#from Spot_Keys_PC import solarKey

def solarReports():
        page = requests.get(solarServiceUrl)
        soup = BeautifulSoup(page.text,'html.parser')
        print (soup)
