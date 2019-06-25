# Function: Google GeoCode Web service
import urllib.request, urllib.parse, urllib.error
import json
import os
import pprint, pickle

# Constants
from SpotDefaults import USGSEarthquakeServiceUrl,USGSEarthquakeAllDayServiceUrl,USGSMethod01,USGSDateTime,USGSParameter01,USGSParameter02,USGSParameter03,USGSParameter04,spotterTimeDate,xDefault,yDefault
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
USGSParameter02=x[0]

y={}
yDefault=os.environ["s_yDefault"]
yDefaultStr=str (yDefault)
y[0]=yDefaultStr
y[1]=y[0]
parallel={}
USGSParameter03=y[0]

DT={}
USGSDateTime=spotterTimeDate
USGSDateTimeStr=str (USGSDateTime)
DT[0]=USGSDateTimeStr
DT[1]=DT[0]

#print('Test Block')
#print(pc[0],pc[1],x[0],x[1],y[0],y[1])

# Dict Initialization
mag={}
place={}
time={}

def USGSEarthquake(USGSEarthquakeServiceUrl,USGSEarthquakeAllDayServiceUrl,USGSMethod01,USGSDateTime,USGSParameter02,USGSParameter03,USGSParameter04,xDefault,yDefault,postalcodeCurrent,dataPath):
    while True:
        USGSDateTimeStr=str (USGSDateTime)
        DT[0]=USGSDateTimeStr
        DT[1]=DT[0]
        url0=(USGSEarthquakeServiceUrl+USGSMethod01+USGSDateTimeStr+USGSParameter01+USGSParameter02+USGSParameter03+USGSParameter04)
        url1=USGSEarthquakeAllDayServiceUrl
        print(url1)
        urlHandle = urllib.request.urlopen(url1)
        req = urllib.request.Request(url1)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        earthquake = urlHandle.read().decode()
        try:
            js = json.loads(earthquake)
        except:
            js = None
        if not js or 'status' not in js or js['status'] != 'OK' or js['status']!=200:
            print('Errors making call...')
            print(earthquake)
        target=str(dataPath)
        configTarget=((target)+'SpotOut_Earthquakes.json')
        print(json.dumps(js, indent=4))
        for line in earthquake:
                mag[line] = js["features"][0]["properties"]["mag"]
                place[line]=js["features"][0]["properties"]["place"]
                time[line]=js["features"][0]["properties"]["time"]
        with open(configTarget, 'w') as f:
                json.dump(js, f, ensure_ascii=False)
        break
    print()
    print('The Postal code you entered: ',postalcodeCurrent)
    print()
    print('results in the following: City, State, and Country:')
    print()
    print('Your coordinates are:')
    print()
    print('meridian: ', x[1],'   parallel: ',y[1])
    return None

# Experiment Block
        #coordinates={"meridianXCurrent":[meridian],
                     #"parallelYCurrent":[parallel],
                     #"physicalAddressZCurrent":physicalAddress}       
        #output = open('data.pkl', 'wb')
        # Pickle dictionary using protocol 0.
        #pickle.dump(coordinates, output)
        # Pickle the list using the highest protocol available.
        #pickle.dump(selfref_list, output, -1)
        #output.close()
        #break
    #return (postalcodeCurrent,meridianCurrent,parallelCurrent)


#print('Test Block')
#postalcodeCurrent=95070
#USGSEarthquake(USGSEarthquakeServiceUrl,USGSEarthquakeAllDayServiceUrl,USGSMethod01,USGSDateTime,USGSParameter02,USGSParameter03,USGSParameter04,xDefault,yDefault,postalcodeCurrent)
#print('Print Again....')
#print ('xCurrent',x[1],'xDefault',x[0])
#print ('yCurrent',x[1],'yDefault',x[0])
# Pickle solution
#pkl_file = open('data.pkl', 'rb')
#data1 = pickle.load(pkl_file)
#pprint.pprint(coordinates)
#pkl_file.close()

# PRE-REQs to run this module
# Process URL requests
	# pip install request or requests

