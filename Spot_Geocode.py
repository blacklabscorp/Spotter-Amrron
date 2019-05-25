# Function: Geocode Web service
import urllib.request, urllib.parse, urllib.error
import json
import os

# Constants
googleKey=os.environ["s_googleKey"]
from Spot_Defaults import googleGeoCodeServiceUrl,key

def geocode(zipcodeCurrent):
    while True:
        url = (googleGeoCodeServiceUrl + urllib.parse.urlencode({'address': zipcodeCurrent})+key+googleKey)
        urlHandle = urllib.request.urlopen(url)
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        geocode = urlHandle.read().decode()
        try:
            js = json.loads(geocode)
        except:
            js = None
        if not js or 'status' not in js or js['status'] != 'OK':
            print('Errors making call...')
            print(data)
            continue
        #print(json.dumps(js, indent=4))
        meridian = js["results"][0]["geometry"]["location"]["lat"]
        parallel = js["results"][0]["geometry"]["location"]["lng"]
        physicalAddress = js['results'][0]['formatted_address']
        print()
        print()
        print('The Zip code you entered: ',zipcodeCurrent)
        print()
        print('results in the following: City, State, and Country:')
        print()
        print(physicalAddress)
        print()
        print('Your coordinates are:')
        print()
        print('meridian: ', meridian,'   parallel: ',parallel)      
        break
