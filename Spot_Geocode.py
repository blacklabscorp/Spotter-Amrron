# Function: Geocode Web service
import urllib.request, urllib.parse, urllib.error
import json
import urllib3
from Spot_Keys_PC import googleKey
from Spot_Defaults import serviceurl,key

def geocode(zipcode):
    while True:
        url = (serviceurl + urllib.parse.urlencode({'address': zipcode})+key+googleKey)
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
        print('The Zip code you entered: ',zipcode)
        print()
        print('results in the following: City, State, and Country:')
        print()
        print(physicalAddress)
        print()
        print('Your coordinates are:')
        print()
        print('meridian: ', meridian,'   parallel: ',parallel)      
        break
