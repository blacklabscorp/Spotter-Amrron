# Define path to program files
#import sys
import os
#sys.path.append('C:\Spot')
#userProfile=str(os.environ.get("USERPROFILE"))

# Import Modules
from Spot_Keys_PC import Spot_Env
from Spot_Geocode import geocode
from Spot_TransmitTwilio import Transmit
Spot_Env()

# Load Defaults values
from Spot_Defaults import xDefault,yDefault,dmrIdDefault,callsignDefault,gridDefault,zipDefault
#from Spot_Keys_PC import twilioAccountSid,twilioAuthToken,twilioAmrron,oscarRomeo01,romeo07,googleKey
from twilio.rest import Client

# Set Constants
callsign=callsignDefault
zipcode=zipDefault
grid=gridDefault

# Import 
import urllib.request, urllib.parse, urllib.error
import json
import urllib3

# Capturing time 
import datetime
timeLocalCurrent = datetime.datetime.now().isoformat()
timeUtcCurrent=datetime.datetime.utcnow()

# Function: Default values print
def HamDefaultsOutput():
    print()
    print('D E F A U L T S')
    print('Callsign Default: ',callsignDefault)
    print()
    print('Grid Default: ',gridDefault)
    print('Zipcode Default: ',zipDefault)
    print()
    print ('Your Default GPS coordinates: Decimal Lattitude: ',xDefault)
    print ('Your Default GPS coordiante Decimal Longitude: ',yDefault)
    print()
    print('Current Local Time: ',timeLocalCurrent)
    print('Current GMT Time: ',timeUtcCurrent)
    print()


# Function: HamDefaultInput
def HamDefaultsInput():
    HamDefaultsOutput()
    callsign=callsignDefault
    zipcode=zipDefault
    grid=gridDefault
    while True:
        print()
        correct=input ('Are these Correct, type [D]efault; Y[es], N[o]:')
        if correct == "D":
            print()
            print (HamDefaultsOutput())
            break
        if correct == "N": 
            print()
            callsign=input(' Hit Enter to accept or Callsign to change:')
            print()
            zipcode=input(' Hit Enter to accept or zipcode to change:')
            print()
            grid=input('Enter your Gridcode (or blank if unknown): ')
            print()
            print()
            print('You entered Callsign: ',callsign)
            print()
            print('You entered Zipcode: ',zipcode)
            print('You entered Grid: ',grid)
        if correct == "Y":
            print()
            print()
            HamDefaultsOutput()
            print('Y O U R  V A L U E S')
            print()
            print('Your Callsign: ',callsign)
            print()
            print('Your Zipcode: ',zipcode)
            print('Your Grid: ',grid)
            print()
        break

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
print ("C U R R E N T  D E F A U L T  S E T T I N G S")
print (HamDefaultsOutput())
print()
print('MAIN MENU')
print()
print('[M] Main Inputs')
print('[G] Get Google data')
print('[T[ Transmit Menu')
mainMenu=input ('Which option would you like...')        
if mainMenu=="M":
    print()
    HamDefaultsInput()
if mainMenu=="G":
    print()
    geocode(zipcode)
if mainMenu=="T":
    print()
    print('Off to Transmit...')
    print()
    TransmitMenu()


