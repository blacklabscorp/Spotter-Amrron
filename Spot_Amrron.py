# Amrron conditions
import requests
from bs4 import BeautifulSoup
from Spot_Defaults import amrronConditionServiceUrl
amConnLevel=''

def AmConn(amConnLevel):
        page = requests.get(amrronConditionServiceUrl)
        soup = BeautifulSoup(page.text,'html.parser')     
        for tag in soup.find_all('AmConn-%'):
            amConnLevel=tag
        return (amConnLevel)

# Experimental to scrape AmConn #
#print('Test Block')
#AmConn(amConnLevel)
#print(amConnLevel,page)

# PRE-REQs to run this module
# Process URL requests
	# pip install request or requests
# Web scrapper
	# pip install bs4

