# Libraries
import os
import urllib.request, urllib.parse, urllib.error
import json

# Env Data & Working directories
workingDir=os.path.dirname(os.path.abspath(__file__))
dataDir='\\SpotData\\'
dataPath=print(workingDir+dataDir)

# FlMsg working directories
UserProfile=os.environ["USERPROFILE"]
flMsgWorkingDir=UserProfile+'\\NBEMS.files\\ICS\\messages'
k2sFileDefault=os.environ["s_K2sDefault"]

# Env PII
oscarRoeo01=os.environ["s_oscarRomeo01"]
romeo07=os.environ["s_romeo07"]
callsign=os.environ["s_callsign"]
postalcodeDefault=os.environ["s_postalcode"]
cityStateDefault=os.environ["s_cityState"]

# Env Keys
twilioAccountSid=os.environ["s_twilioAccountSid"]
twilioAuthToken=os.environ["s_twilioAuthToken"]
twilioAmrron=os.environ["s_twilioAmrron"]
googleKey=os.environ["s_googleKey"]
openWeatherKey=os.environ["s_openWeatherKey"]

# Import Functions
from Spot_GoogleGeoCode import GoogleGeo
from Spot_Solar import SolarReport
from Spot_TransmitTwilio import Transmit
from Spot_AmrronSpotRepv3_Convert import AmrronSpotRepv3
from Spot_OpenWeatherLight import DefaultWeather,ThreeDayForecast

# Load Defaults values
from Spot_Defaults import xDefault,yDefault,dmrIdDefault,callsignDefault,postalcodeDefault,gridDefault,openWeatherServiceUrl,openWeatherPreKey

# Set Constants
callsignCurrent=callsignDefault
postalcodeCurrent=postalcodeDefault
cityStateCurrent=cityStateDefault
gridCurrent=gridDefault
callsignLast=callsignCurrent
postalcodeLast=postalcodeCurrent
cityStateLast=cityStateCurrent
gridLast=gridCurrent


# Capturing time 
import datetime
timeLocalCurrent = datetime.datetime.now().isoformat()
timeUtcCurrent=datetime.datetime.utcnow()

# Function: Default values print
def HamDefaultsOutput(callsignDefault,callsignLast,callsignCurrent,postalcodeDefault,postalcodeLast,postalcodeCurrent,cityStateDefault,cityStateLast,cityStateCurrent,gridDefault,gridLast,gridCurrent):
    print()
    print('D E F A U L T S')
    print('Callsign Default: ',callsignDefault,' CallsignLast: ',callsignLast)
    print()
    print('Grid Default: ',gridDefault,' Grid Last: ',gridLast)
    print('postalcode Default: ',postalcodeDefault,' postalcode Last: ',postalcodeLast)
    print('City, State Default: ',cityStateDefault,' City,State Last: ',cityStateLast)
    print()
    print ('Your Default GPS coordinates: Decimal Lattitude: ',xDefault)
    print ('Your Default GPS coordiante Decimal Longitude: ',yDefault)
    print()
    print('Current Local Time: ',timeLocalCurrent)
    print('Current GMT Time: ',timeUtcCurrent)
    print()

# Function: HamDefaultInput
def HamDefaultsInput(callsignDefault,callsignLast,callsignCurrent,postalcodeDefault,postalcodeLast,postalcodeCurrent,cityStateDefault,cityStateLast,cityStateCurrent,gridDefault,gridLast,gridCurrent):
    print('Values')
    print('______')
    print('D E F A U L T')
    print('CallsignDefault: ',callsignDefault)
    print('PostalcodeDefault: ',postalcodeDefault)
    print('City,StateDefault: ',cityStateDefault)
    print('GridDefault: ',gridDefault)
    print('C U R R E N T')
    print('CallsignCurrent: ',callsignCurrent)
    print('PostalcodeCurrent: ',postalcodeCurrent)
    print('City,StateCurrent: ',cityStateCurrent)
    print('GrideCurrent: ',gridCurrent)
    print('L A S T')
    print('CallsignLast: ',callsignLast)
    print('PostalcodeLast: ',postalcodeLast)
    print('City,StateLast: ',cityStateLast)
    print('GridLast: ',gridLast)
    while True:
        print()
        print()
        correct=input ('Are these Correct, type [D]efault; Y[es], N[o]:')
        if correct == "D":
            print()
            callsignLast=callsignCurrent
            postalcodeLast=postalcodeCurrent
            cityStateLast=cityStateCurrent
            gridLast=gridCurrent
            callsignCurrent=callsignDefault
            postalcodeCurrent=postalcodeDefault
            cityStateCurrent=cityStateDefault
            gridCurrent=gridDefault
            HamDefaultsOutput(callsignDefault,callsignLast,callsignCurrent,postalcodeDefault,postalcodeLast,postalcodeCurrent,cityStateCurrent,cityStateDefault,cityStateLast,gridDefault,gridLast,gridCurrent)
            break
        if correct == "N": 
            callsignLast=callsignCurrent
            postalcodeLast=postalcodeCurrent
            gridLast=gridCurrent
            print()
            callsignNew=input(' Hit Enter to accept or Callsign to change:')
            print()
            postalcodeNew=input(' Hit Enter to accept or Postal code to change:')
            print()
            cityStateNew=input(' Hit Enter to accept or City,State code (ex: Los Angeles, CA) to change:')
            print()
            gridNew=input('Enter your Gridcode (or blank if unknown): ')
            print()
            callsignCurrent=callsignNew
            postalcodeCurrent=postalcodeNew
            cityStateCurrent=cityStateNew
            gridCurrent=gridNew
            print()
            print('You entered Callsign: ',callsignCurrent,' Previous entry was: ',callsignLast)
            print('You entered Postal code: ',postalcodeCurrent, ' Previous Postal code was: ',postalcodeLast)
            print('You entered City,State:',cityStateCurrent,' Previous City,State was:',cityStateLast)
            print('You entered Grid: ',gridCurrent,' Previous Grid was: ',gridLast)
            break
        if correct == "Y":
            print()
            print()
            print('Y O U R  V A L U E S')
            print()
            print('Your Callsign: ',callsignCurrent)
            print('Your Postal code: ',postalcodeCurrent)
            print('YOur City, State: ',cityStateCurrent)
            print('Your Grid: ',gridCurrent)
            print()
            break
    return callsignDefault,callsignLast,callsignCurrent,postalcodeDefault,postalcodeLast,postalcodeCurrent,cityStateDefault,cityStateLast,cityStateCurrent,gridDefault,gridLast,gridCurrent

# Transmit Menu
def TransmitMenu():
    print('T R A N S M I T  M E N U')
    print('_________________________')
    print()
    while True:
        print('Option: [M] Return to Main Inputs')
        print('Option: [G] Fetch Google Data')
        print('Option: [OT] Oscar Romeo 01 SMS delivery')
        print('Option: [OP] Oscar Romeo 01 Phone delivery')
        print('Option: [RT] Romeo 07 SMS Delivery')
        print('Option: [RP] Romeo 07 Phone Delivery')
        print('Option: [CAT] All CA SMS Delivery')
        print('Option: [CAP] All CA Phone Delivery')
        transmitMenu=input ('Which option would you like...')        
        if transmitMenu=="M":
            print()
            break
        if transmitMenu=="G":
            print()
            GooogleGeo(postalcodeCurrent,xDefault,yDefault)
        if transmitMenu=="OT":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
        if transmitMenu=="OP":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
        if transmitMenu=="RT":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
        if transmitMenu=="RP":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
        if transmitMenu=="CAT":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
        if transmitMenu=="CAP":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
        break

def WeatherMenu():
    print('W E A T H E R  M E N U')
    print('________________________')
    print()
    while True:
        print('Option: [M] Return to Main Inputs')
        print('Option: [Dow] Default Open Weather')
        print('Option: [Low] Local Open Weather')
        print('Option: [Tow] Default & Local Open Weather')
        print('Option: [LDW] Local Device Weather')
        print('Option: [DDW] Default Device Weather')
        weatherMenu=input ('Which option would you like...')        
        if weatherMenu=="M":
            print()
            break
        if weatherMenu=="Dow":
            print()
            print('Default Weather: Wind')
            print('_______________________________')
            print()
            DefaultWeather(postalcodeCurrent,postalcodeDefault)
            print()
            print('Default Weather: 3 day Forecast')
            print('_______________________________')
            print(cityStateCurrent)
            ThreeDayForecast(cityStateCurrent)
            print()
            break
        if weatherMenu=="Low":
            print()
            print('Local Open Weather')
            print()
            break
        if weatherMenu=="Tow":
            print()
            print('Local & Default Open Weather')
            print()
            break
        if weatherMenu=="LDW":
            print()
            print('Local Device Weather')
            print()
            break
        if weatherMenu=="DDW":
            print()
            print('Default Device Weather')
            print()
            break      
def EnvironmentMenu ():
    print('E N V I R O N M E N T  M E N U')
    print('________________________')
    print()
    while True:
        print('Option: [M] Return to Main Inputs')
        print('Option: [S] Default Sun Weather')
        print('Option: [E] Earthquake activity')
        print('Option: [R] Radiation recordings')
        environmentMenu=input ('Which option would you like...')
        if environmentMenu=="M":
            print()
            break
        if environmentMenu=="S":
            print()
            SolarReport()
            break
        if environmentMenu=="E":
            print()
            print('Earthquake regional Reports')
            print()
            break
        if environmentMenu=="R":
            print()
            print('Radiation regional Reports')
            print()
            break

# Main Block
while True: 
    print()
    print('M  A  I  N   M  E  N  U')
    print('________________________')
    print()
    print('[I] Inputs Menu')
    print('[G] Google data Menu')
    print('[T[ Transmit Menu')
    print('[F] FlMsg Menu')
    print('[W] Weather Menu')
    print('[E} Environment Menu')
    print('[X] Exit & Quit Program')
    print()
    mainMenu=input ('Which option would you like...')
    if mainMenu=="I":
        print()
        callsignDefault,callsignLast,callsignCurrent,postalcodeDefault,postalcodeLast,postalcodeCurrent,cityStateDefault,cityStateLast,cityStateCurrent,gridDefault,gridLast,gridCurrent=HamDefaultsInput(callsignDefault,callsignLast,callsignCurrent,postalcodeDefault,postalcodeLast,postalcodeCurrent,cityStateDefault,cityStateLast,cityStateCurrent,gridDefault,gridLast,gridCurrent)
       # print('Input Menu new values')
       # print('Your Current Callsign:',callsignCurrent,' Last: ',callsignLast,' Default: ',callsignDefault)
       # print('Your Current Postal code:',postalcodeCurrent,' Last: ',postalcodeLast,' Default: ',postalcodeDefault)
       # print('Your City,State: ',cityStateCurrent,' Last: ',cityStateLast,' Default: ',cityStateDefault)
       # print('Your Current Gridcode:',gridCurrent,' Last: ',gridLast,' Default: ',gridDefault)
    if mainMenu=="G":
        print()
        GoogleGeo(postalcodeCurrent,xDefault,yDefault)
    if mainMenu=="T":
        print()
        print('Off to Transmit...')
        print()
        TransmitMenu()
    if mainMenu=="F":
        print()
        AmrronSpotRepv3(workingDir,dataDir,k2sFileDefault,flMsgWorkingDir)
        print() 
    if mainMenu=="W":
        print()
        print('Weather Menu')
        print()
        WeatherMenu()
        print()
    if mainMenu=="E":
        print()
        print
        print('Environment Menu')
        print()
        EnvironmentMenu()
        print()
    if mainMenu=="X":
        quit()
        
    # Test variable prints
#print('I have reached the end')
#print('Main Resuls')
#print('CallsignCurrent: ',callsignCurrent)
#print('Postal code Current: ',postalcodeCurrent)
#print('GrideCurrent: ',gridCurrent)
#print('CallsignDefault: ',callsignDefault)
#print('Postal code Default: ',postalcodeDefault)
#print('GridDefault: ',gridDefault)
#print('CallsignLast: ',callsignLast)
#print('Postal code Last: ',postalcodeLast)
#print('GridLast: ',gridLast)

#k2sDataPathTarget = os.path.join(dataPath,k2sDefault)
#print(workingDir)
#print(dataDir)
#print(k2sDefault,'k2sDataPathTarget')
#print(workingDir+dataDir+k2sDefault)
