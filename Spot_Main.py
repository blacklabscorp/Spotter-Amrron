# Libraries
import os
import urllib.request, urllib.parse, urllib.error
import json

# Env Data & Working directories
workingDir=os.path.dirname(os.path.abspath(__file__))
dataDir='\\SpotData\\'
configDir='\\SpotConfigs\\'
dataPath=workingDir+dataDir
configsPath=workingDir+configDir

# FlMsg working directories
UserProfile=os.environ["USERPROFILE"]
flMsgWorkingDir=UserProfile+'\\NBEMS.files\\ICS\\messages\\'
k2sFileDefault=os.environ["s_K2sDefault"]
k2sFileCurrent=k2sFileDefault

# Env PII
amrron00User=os.environ["s_amrron00User"]
amrron01User=os.environ["s_amrron01User"]
amrron00Cell=os.environ["s_amrron00Cell"]
amrron01Cell=os.environ["s_amrron01Cell"]
callsignDefault=os.environ["s_callsignDefault"]
postalcodeDefault=os.environ["s_postalcodeDefault"]
cityStateDefault=os.environ["s_cityStateDefault"]

# Env Keys
twilioAccountSid=os.environ["s_twilioAccountSid"]
twilioAuthToken=os.environ["s_twilioAuthToken"]
twilioAmrronCell=os.environ["s_twilioAmrronCell"]
googleKey=os.environ["s_googleKey"]
openWeatherKey=os.environ["s_openWeatherKey"]

# Import Functions
from Spot_GoogleGeoCode import GoogleGeo
from Spot_Solar import SolarReport
from Spot_OTP import otp_main
from Spot_TransmitTwilio import Transmit,TransmitMenu

from Spot_OpenWeatherLight import DefaultWeather,ThreeDayForecast
from Spot_USGSEarthquake import USGSEarthquake
from Spot_EarthquakesMag import Earthquakes24hrs
from SpotConfigs import ConfigsJSONOut,ConfigsJSONInPrint,secretConfigs
from Spot_FLMsgOut_amrronv3_0  import *

# Load Defaults values
from SpotDefaults import *

# Set Constants
callsignCurrent=callsignDefault
postalcodeCurrent=postalcodeDefault
cityStateCurrent=cityStateDefault
gridCurrent=gridDefault
callsignLast=callsignCurrent
postalcodeLast=postalcodeCurrent
cityStateLast=cityStateCurrent
gridLast=gridCurrent
xCurrent=xDefault
xLast=xCurrent
yCurrent=yDefault
yLast=yCurrent

# Capturing time 
import datetime
timeLocalCurrent = datetime.datetime.now().isoformat()
timeUtcCurrent=datetime.datetime.utcnow()

# Function: Default values print
def HamDefaultsOutput():
    print()
    print('D E F A U L T S')
    print('Callsign Default: ',callsignDefault,' CallsignLast: ',callsignLast)
    print()
    print('Grid Default:       ',gridDefault,'        Grid Last:       ',gridLast)
    print('postalcode Default: ',postalcodeDefault,'         postalcode Last: ',postalcodeLast)
    print('City, State Default:',cityStateDefault,'    City,State Last: ',cityStateLast)
    print()
    print ('Your Default GPS coordinates: Decimal Lattitude: ',xDefault)
    print ('Your Default GPS coordiante Decimal Longitude:   ',yDefault)
    print()
    print('Current Local Time: ',timeLocalCurrent)
    print('Current GMT Time: ',timeUtcCurrent)
    print()

# Function: HamDefaultInput
def HamDefaultsInput():
    global callsignDefault
    global postalcodeDefault
    global cityStateDefault
    global gridDefault
    global xDefault
    global yDefault
    global callsignCurrent
    global postalcodeCurrent
    global cityStateCurrent
    global gridCurrent
    global xCurrent
    global yCurrent
    global callsignLast
    global postalcodeLast
    global cityStateLast
    global gridLast
    global xLast
    global yLast
    print('Values')
    print('______')
    print('D E F A U L T')
    print('CallsignDefault: ',callsignDefault)
    print('PostalcodeDefault: ',postalcodeDefault)
    print('City,StateDefault: ',cityStateDefault)
    print('GridDefault: ',gridDefault)
    print('xDefault: ',xDefault,' yDefault',yDefault)
    print('C U R R E N T')
    print('CallsignCurrent: ',callsignCurrent)
    print('PostalcodeCurrent: ',postalcodeCurrent)
    print('City,StateCurrent: ',cityStateCurrent)
    print('GrideCurrent: ',gridCurrent)
    print('xCurrent: ',xCurrent,' yCurrent',yCurrent)
    print('L A S T')
    print('CallsignLast: ',callsignLast)
    print('PostalcodeLast: ',postalcodeLast)
    print('City,StateLast: ',cityStateLast)
    print('GridLast: ',gridLast)
    print('xCurrent: ',xLast,' yCurrent',yLast)
    while True:
        print()
        print()
        correct=input ('Are these Correct, type [D]efault; [C]urrent, [N]ew:')
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
            HamDefaultsOutput()
            break
        if correct == "N": 
            callsignLast=callsignCurrent
            postalcodeLast=postalcodeCurrent
            citStateLast=cityStateCurrent
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
            print('You entered X coordinates: ',xCurrent,' and Y coordinates:',yCurrent)
            print('Previous X: ',xLast,' and Y was:',yLast)
            print()
            break
        if correct == "C":
            print()
            print()
            print('Y O U R  V A L U E S')
            print()
            print('Your Callsign: ',callsignCurrent)
            print('Your Postal code: ',postalcodeCurrent)
            print('YOur City, State: ',cityStateCurrent)
            print('Your Grid: ',gridCurrent)
            print('Your X:',xCurrent,' Your Y:',yCurrent)
            print()
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
        print('Option: [EQ] Earthquake activity')
        print('Option: [EM] Earthquake Magnitide last 24hrs')
        print('Option: [R] Radiation recordings')
        environmentMenu=input ('Which option would you like...')
        if environmentMenu=="M":
            print()
            break
        if environmentMenu=="S":
            print()
            SolarReport()
            break
        if environmentMenu=="EQ":
            print()
            print('Earthquake regional Reports')
            print()
            USGSEarthquake(USGSEarthquakeServiceUrl,USGSEarthquakeAllDayServiceUrl,USGSMethod01,USGSDateTime,USGSParameter02,USGSParameter03,USGSParameter04,xDefault,yDefault,postalcodeCurrent,dataPath)
            Earthquakes24hrs()
            break
        if environmentMenu=="EM":
            print()
            print('Earthquake Daily Mag Report')
            Earthquakes24hrs()
            break
        if environmentMenu=="R":
            print()
            print('Radiation regional Reports')
            print()
            break

def flmsgmenu ():
    while True:
        print('F L M s g  M E N U')
        print('________________________')
        print()
        print('Option: [M] Main Menu')
        print('Option: [spotv30] Spot Report v3_0')
        print('Option: [sitv30] Sit Report v3_0')
        print()
        flmsgout_amrronv3_0_main ()
        print()
        return

def locationsmenu ():
    while True:
        print('L O C A T I O N  M E N U')
        print('________________________')
        print()
        print('Option: [M] Main Menu')
        print('Option: [Location]  Location settings')
        print('Option: [Google Geo] Google GeoCode API using current postalcode: ',postalcodeCurrent)
        print()
        locationsMenu=input ('Which option would you like...')
        print()
        if locationsMenu=='M':
            print()
            mainmenu()
            print
            break
        if locationsMenu=="Location":
            print()
            print('GPS Settings new values')
            print('Your Current Postal code:',postalcodeCurrent,' Last: ',postalcodeLast,' Default: ',postalcodeDefault)
            print('Your City,State: ',cityStateCurrent,' Last: ',cityStateLast,' Default: ',cityStateDefault)
            print('Your Current Gridcode:',gridCurrent,' Last: ',gridLast,' Default: ',gridDefault)
            print('Your Current GPS coordinates:',xCurrent,yCurrent)
            print()
            HamDefaultsInput()
            break
        if locationsMenu=="Google Geo":
            print()
            GoogleGeo(postalcodeCurrent,xDefault,yDefault)
            break

def SettingsMenu ():
    while True:
        print('S E T T I N G S  M E N U')
        print('________________________')
        print()
        print('Option: [M] Main Menu')
        print('Option: [Ham]  Ham station settings')
        print('Option: [Hive] Hive settings')
        print('Option: [Out] Output current settings')
        print()
        settingsMenu=input ('Which option would you like...')
        print()
        if settingsMenu=='M':
            print()
            mainmenu()
            print
            break
        if settingsMenu=="Ham":
            print()
            print('Ham Settings new values')
            print('Your Current Callsign:',callsignCurrent,' Last: ',callsignLast,' Default: ',callsignDefault)
            print('Your Current Postal code:',postalcodeCurrent,' Last: ',postalcodeLast,' Default: ',postalcodeDefault)
            print('Your City,State: ',cityStateCurrent,' Last: ',cityStateLast,' Default: ',cityStateDefault)
            print('Your Current Gridcode:',gridCurrent,' Last: ',gridLast,' Default: ',gridDefault)
            print()
            HamDefaultsInput()
            break
        if settingsMenu=="Hive":
            print()
            break
        if settingsMenu=="Out":
            print()
            ConfigsJSONOut(secretConfigs,dataPath)
            ConfigsJSONInPrint(dataPath)
            break

def mainmenu():
    while True:
        print()
        print('M  A  I  N   M  E  N  U')
        print('________________________')
        print()
        print('[S] Settings Menu')
        print('[L] Locations Menu')      
        print('[W] Weather Menu')
        print('[E} Environment Menu')
        print('[F] FlMsg Menu')
        print('[T] Transmit Menu')
        print('[X] Exit & Quit Program')
        print()
        mainMenu=input ('Which option would you like...')
        if mainMenu=="S":
            print()
            SettingsMenu () 
        if mainMenu=="L":
            print()
            locationsmenu()
        if mainMenu=="W":
            print()
            print('Weather Menu')
            print()
            WeatherMenu()
            print()
        if mainMenu=="E":
            print()
            print('Environment Menu')
            print()
            EnvironmentMenu()
            print()
        if mainMenu=="F":
            print()
            flmsgmenu()
            print()       
        if mainMenu=="T":
            print()
            TransmitMenu()
            print()         
        if mainMenu=="X":
            quit()
# M A I N
if __name__ == "__main__":

    mainmenu ()



