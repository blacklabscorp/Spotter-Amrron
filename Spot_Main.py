# Set Enviroment
import os

twilioAccountSid=os.environ["s_twilioAccountSid"]
twilioAuthToken=os.environ["s_twilioAuthToken"]
twilioAmrron=os.environ["s_twilioAmrron"]
oscarRoeo01=os.environ["s_oscarRomeo01"]
romeo07=os.environ["s_romeo07"]
googleKey=os.environ["s_googleKey"]

# Import Functions
from Spot_Geocode import geocode
from Spot_Solar import solarReports
from Spot_TransmitTwilio import Transmit
#from Spot_Input import HamDefaultsInput


# Load Defaults values
from Spot_Defaults import xDefault,yDefault,dmrIdDefault,callsignDefault,zipcodeDefault,gridDefault

# Set Constants
callsignCurrent=callsignDefault
zipcodeCurrent=zipcodeDefault
gridCurrent=gridDefault
callsignLast=callsignCurrent
zipcodeLast=zipcodeCurrent
gridLast=gridCurrent


# Import modules
import urllib.request, urllib.parse, urllib.error
import json


# Capturing time 
import datetime
timeLocalCurrent = datetime.datetime.now().isoformat()
timeUtcCurrent=datetime.datetime.utcnow()

# Function: Default values print
def HamDefaultsOutput(callsignDefault,callsignLast,callsignCurrent,zipcodeDefault,zipcodeLast,zipcodeCurrent,gridDefault,gridLast,gridCurrent):
    print()
    print('D E F A U L T S')
    print('Callsign Default: ',callsignDefault,' CallsignLast: ',callsignLast)
    print()
    print('Grid Default: ',gridDefault,' Grid Last: ',gridLast)
    print('Zipcode Default: ',zipcodeDefault,' Zipcode Last: ',zipcodeLast)
    print()
    print ('Your Default GPS coordinates: Decimal Lattitude: ',xDefault)
    print ('Your Default GPS coordiante Decimal Longitude: ',yDefault)
    print()
    print('Current Local Time: ',timeLocalCurrent)
    print('Current GMT Time: ',timeUtcCurrent)
    print()

# Function: HamDefaultInput
def HamDefaultsInput(callsignDefault,callsignLast,callsignCurrent,zipcodeDefault,zipcodeLast,zipcodeCurrent,gridDefault,gridLast,gridCurrent):
    print('CallsignCurrent: ',callsignCurrent)
    print('ZipcodeCurrent: ',zipcodeCurrent)
    print('GrideCurrent: ',gridCurrent)
    print('CallsignDefault: ',callsignDefault)
    print('ZipcodeDefault: ',zipcodeDefault)
    print('GridDefault: ',gridDefault)
    print('CallsignLast: ',callsignLast)
    print('ZipcodeLast: ',zipcodeLast)
    print('GridLast: ',gridLast)
    while True:
        print()
        print()
        correct=input ('Are these Correct, type [D]efault; Y[es], N[o]:')
        if correct == "D":
            print()
            callsignLast=callsignCurrent
            zipcodeLast=zipcodeCurrent
            gridLast=gridCurrent
            callsignCurrent=callsignDefault
            zipcodeCurrent=zipcodeDefault
            gridCurrent=gridDefault
            HamDefaultsOutput(callsignDefault,callsignLast,callsignCurrent,zipcodeDefault,zipcodeLast,zipcodeCurrent,gridDefault,gridLast,gridCurrent)
            break
        if correct == "N": 
            callsignLast=callsignCurrent
            zipcodeLast=zipcodeCurrent
            gridLast=gridCurrent
            print()
            callsignNew=input(' Hit Enter to accept or Callsign to change:')
            print()
            zipcodeNew=input(' Hit Enter to accept or zipcode to change:')
            print()
            gridNew=input('Enter your Gridcode (or blank if unknown): ')
            print()
            callsignCurrent=callsignNew
            zipcodeCurrent=zipcodeNew
            gridCurrent=gridNew
            print()
            print('You entered Callsign: ',callsignCurrent,' Previous entry was: ',callsignLast)
            print()
            print('You entered Zipcode: ',zipcodeCurrent, ' Previous zipcode was: ',zipcodeLast)
            print('You entered Grid: ',gridCurrent,' Previous Grid was: ',gridLast)
            break
        if correct == "Y":
            print()
            print()
            print('Y O U R  V A L U E S')
            print()
            print('Your Callsign: ',callsignCurrent)
            print()
            print('Your Zipcode: ',zipcodeCurrent)
            print('Your Grid: ',gridCurrent)
            print()
            break
    print('Exit Function: HamInput')
    print('CallsignCurrent: ',callsignCurrent)
    print('ZipcodeCurrent: ',zipcodeCurrent)
    print('GrideCurrent: ',gridCurrent)
    print('CallsignDefault: ',callsignDefault)
    print('ZipcodeDefault: ',zipcodeDefault)
    print('GridDefault: ',gridDefault)
    print('CallsignLast: ',callsignLast)
    print('ZipcodeLast: ',zipcodeLast)
    print('GridLast: ',gridLast)
    return callsignDefault,callsignLast,callsignCurrent,zipcodeDefault,zipcodeLast,zipcodeCurrent,gridDefault,gridLast,gridCurrent

# Transmit Menu
def TransmitMenu():
    print('T R A N S M I T  M E N U')
    print('________________________')
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
            HamDefaultsInput()
        if transmitMenu=="G":
            print()
            geocode(zipcode)
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

# Main Block
while True:
    #sunDict=solarReports()
    print()
    print('MAIN MENU')
    print()
    print('[M] Main Inputs')
    print('[G] Get Google data')
    print('[T[ Transmit Menu')
    print()
    mainMenu=input ('Which option would you like...')
    if mainMenu=="M":
        print()
        callsignDefault,callsignLast,callsignCurrent,zipcodeDefault,zipcodeLast,zipcodeCurrent,gridDefault,gridLast,gridCurrent=HamDefaultsInput(callsignDefault,callsignLast,callsignCurrent,zipcodeDefault,zipcodeLast,zipcodeCurrent,gridDefault,gridLast,gridCurrent)
        print('Main Menu new values')
        print()
        print('Your Current Callsign:',callsignCurrent,' Default Callsign: ',callsignDefault)
        print()
        print('Your Current Zipcode:',zipcodeCurrent,' Default Zipcode: ',zipcodeDefault)
        print()
        print('Your Current Gridcode:',gridCurrent,' Default Gridcode: ',gridDefault)
    if mainMenu=="G":
        print()
        geocode(zipcodeCurrent)
        break
    if mainMenu=="T":
        print()
        print('Off to Transmit...')
        print()
        TransmitMenu()
        break
    print()
    print('I have reached the end')
    print('Main Resuls')
    print('CallsignCurrent: ',callsignCurrent)
    print('ZipcodeCurrent: ',zipcodeCurrent)
    print('GrideCurrent: ',gridCurrent)
    print('CallsignDefault: ',callsignDefault)
    print('ZipcodeDefault: ',zipcodeDefault)
    print('GridDefault: ',gridDefault)
    print('CallsignLast: ',callsignLast)
    print('ZipcodeLast: ',zipcodeLast)
    print('GridLast: ',gridLast)

