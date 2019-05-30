# Function: Google GeoCode Web service
import urllib.request, urllib.parse, urllib.error
import json
import os
import pprint, pickle

# Constants
from Spot_Defaults import googleGeoCodeServiceUrl,googleGeoPreKey,spotterTimeDate,xDefault,yDefault
googleKey=os.environ["s_googleKey"]
pc={}
postalcode=os.environ["s_postalcodeDefault"]
postalcodeStr=str (postalcode)
pc[0]=postalcodeStr
postalcodeCurrent=pc[0]
pc[1]=postalcodeCurrent

x={}
xDefault=os.environ["s_xDefault"]
xDefaultStr=str (xDefault)
x[0]=xDefaultStr
x[1]=x[0]
meridian={}

y={}
yDefault=os.environ["s_yDefault"]
yDefaultStr=str (yDefault)
y[0]=yDefaultStr
y[1]=y[0]
parallel={}

DT={}
geocodeDateTime=spotterTimeDate
geocodeDateTimeStr=str (geocodeDateTime)
DT[0]=geocodeDateTimeStr
DT[1]=DT[0]

#Test Block
#print(x[0],x[1],y[0],y[1])

def GoogleGeo(postalcodeCurrent,xDefault,yDefault):
    while True:
        print(geocodeDateTimeStr)
        url = (googleGeoCodeServiceUrl + urllib.parse.urlencode({'address': postalcodeCurrent})+googleGeoPreKey+googleKey)
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
            print(geocode)
            continue
        print(json.dumps(js, indent=4))
        meridianCurrent = js["results"][0]["geometry"]["location"]["lat"]
        parallelCurrent = js["results"][0]["geometry"]["location"]["lng"]
        physicalAddressCurrent = js['results'][0]['formatted_address']
        x[1]=str(meridianCurrent)
        y[1]=str(parallelCurrent)
        print()
        print('The Postal code you entered: ',postalcodeCurrent)
        print()
        print('results in the following: City, State, and Country:')
        print()
        print(physicalAddressCurrent)
        print()
        print('Your coordinates are:')
        print()
        print('meridian: ', x[1],'   parallel: ',y[1])
        #coordinates={"meridianXCurrent":[meridian],
                     #"parallelYCurrent":[parallel],
                     #"physicalAddressZCurrent":physicalAddress}       
        #output = open('data.pkl', 'wb')
        # Pickle dictionary using protocol 0.
        #pickle.dump(coordinates, output)
        # Pickle the list using the highest protocol available.
        #pickle.dump(selfref_list, output, -1)
        #output.close()
        break
    return None
    #return (postalcodeCurrent,meridianCurrent,parallelCurrent)
# Test Block
#postalcodeCurrent=95070
#GoogleGeo(postalcodeCurrent,xDefault,yDefault)
#print('Print Again....')
#print ('xCurrent',x[1],'xDefault',x[0])
#print ('yCurrent',x[1],'yDefault',x[0])
# Pickle solution
#pkl_file = open('data.pkl', 'rb')
#data1 = pickle.load(pkl_file)
#pprint.pprint(coordinates)
#pkl_file.close()
