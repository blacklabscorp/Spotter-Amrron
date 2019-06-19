# Module High-Level: Imports the last working JSON save of the FLMsg and use as a seed for next report preparation; net result ...
# Creation of a new Spot report, with saved copies for sending during next communication in the FLMsg folder (NBEMS.Files\ICS\messages folder) & SpotData

# Load libraries
import json
import os
import time
import shutil
import datetime

#from Spot_AmrronSpotRepv3_Convert import AmrronSpotRepv3Json

# Capturing time 
timeLocalCurrent = datetime.datetime.now().isoformat()
timeUtcCurrent=datetime.datetime.utcnow()

# Capturing GPS / Grid defaults
xDefault=os.environ["s_xDefault"]
xDefaultStr=str (xDefault)
xCurrent=xDefault
yDefault=os.environ["s_yDefault"]
yDefaultStr=str (yDefault)
yCurrent=yDefault
gridDefault=os.environ["s_gridDefault"]

# Env Data & Working directories
workingDir=os.path.dirname(os.path.abspath(__file__))
dataDir='\\SpotData\\'
dataPath=workingDir+dataDir
target=str(dataPath)

# FlMsg working directories
UserProfile=os.environ["USERPROFILE"]
flMsgWorkingDir=UserProfile+'\\NBEMS.files\\ICS\\messages\\'
k2sFileDefault=os.environ["s_K2sDefault"]

# Constants from Env variables not from Defaults file
callsignDefault=os.environ["s_callsignDefault"]
k2sFileDefault=os.environ["s_k2sDefault"]
k2sFileLatest=k2sFileDefault
k2sFileCurrent=k2sFileDefault

# DateTime
t = time.gmtime()
timestamp=time.strftime('%Y%m%d-%H%M%S',t)

# Set variables
from Spot_Defaults import(oldL1,oldL2,oldL3,oldL4,oldL5,oldL6,oldL7,oldL8,oldL9,oldL10,oldL11)
from Spot_Defaults import(newL1,newL2,newL3,newL4,newL5,newL6,newL7,newL8,newL9,newL10,newL11)
configTarget=''
test=''
spotv3={}

# Create the new Spotv3 report data
def GenSpotv3():
          amrronSpotReportNew=''
          amrronSpotReportNew=(callsignDefault+'-'+timestamp+'.k2s')
          print('Most Recent reports can be found here...')
          print()
          print(target+amrronSpotReportNew)
          with open((target+amrronSpotReportNew),'w',encoding = 'utf-8') as f:
             f.write('<flmsg>2.0.5'+'\n')
             f.write(':hdr_ed:22'+'\n')
             f.write('<customform>'+'\n')
             f.write(':mg:179 CUSTOM_FORM,AMRRON_SPOTREPV3.html'+'\n')
             f.write('L01,'+newL1+'\n')
             f.write('L02,'+callsignDefault+'\n')
             f.write('L03,'+newL3+'\n')
             f.write('L04,'+newL4+'\n')
             f.write('L05,'+newL5+'\n')
             f.write('L06,'+newL6+'\n')
             f.write('L07,'+newL7+'\n')
             f.write('L08,'+newL8+'\n')
             f.write('L09,'+newL9+'\n')
             f.write('L10,'+newL10+'\n')
             f.write('L11,'+newL11+'\n')
          shutil.copy2((target+amrronSpotReportNew),(flMsgWorkingDir+amrronSpotReportNew))
          print(flMsgWorkingDir+amrronSpotReportNew)

# Load the AmrronSpotv3 last processed report (aka 'SpotOut_AmrronSpotV3.json' file)
def Spotv3Load():
          configTarget=((target)+'SpotOut_AmrronSpotV3Default.json')
          with open(configTarget) as json_file:
                    spotv3 = json.load(json_file)
          print()
          print('Loading... ',configTarget)
          print()
          print('This is the data...')
          print(spotv3)
          print()
          global oldL1
          global oldL2
          global oldL3
          global oldL4
          global oldL5
          global oldL6
          global oldL7
          global oldL8
          global oldL9
          global oldL10
          global oldL11
          oldL1=str(spotv3['L01'])
          oldL2=str(spotv3['L02'])
          oldL3=str(spotv3['L03'])
          oldL4=str(spotv3['L04'])
          oldL5=str(spotv3['L05'])
          oldL6=str(spotv3['L06'])
          oldL7=str(spotv3['L07'])
          oldL8=str(spotv3['L08'])
          oldL9=str(spotv3['L09'])
          oldL10=str(spotv3['L10'])
          oldL11=str(spotv3['L11'])
          return 
def main():
    Spotv3Load()
    # print('Variable Test')
    print('The last report had the following attributes, you will be asked to confirm any changes for the next spot report')
    print()
    updates=1
    while True:
              print()
              print('[1] TO: Receipient: Current...')
              print(oldL1)
              newL1 = str(input('Enter the change : ') or (oldL1))
              print()
              print('[2] FROM: Sender): Current...')
              print(callsignDefault)
              newL2 = str(input('Enter the change : ') or (callsignDefault))
              print()
              print('[3] Precedence: Current...')
              print(oldL3)
              newL3 = str(input('Enter the change : ') or ('Routine'))
              print()
              print('[4] Current DTG: (YYYYMMDD-HHMMZ Use UTC):')
              print(timestamp)
              newL4 = str(input('Enter the change : ') or (timestamp))
              print()
              print('[5] Size (Platoon? Battalion? #Vehicles #Persons):')
              print(oldL5)
              newL5 = str(input('Enter the change : ') or (oldL5))
              print()
              print('[6] Activity (Convoy, Checkpoint, Patrol, Cordon, Training, Interrogation, Relocating/evacuating Citizens, Etc):')
              print(oldL6)
              newL6 = str(input('Enter the change : ') or (oldL6))
              print()
              print('[7] Location (GPS/Grid Coord, address, road name/#, Direction, proximity to landmarks, nearest town, etc.):')
              print ('Default GPS: ',xDefault,' ',yDefault,'   ''Default Grid',gridDefault)
              print('Current GPS: ',xCurrent,' ',yCurrent )
              newL7 = str(input('Enter the change : ') or (gridDefault)) 
              print()
              print('[8] Unit (Domestic/Foreign, Police, Military, branch, guard/reserve, Unit Designation, civ supt, volunteer, etc.):')
              print(oldL8)
              newL8 = str(input('Enter the change : ') or (oldL8))
              print()
              print('[9] Time & Duration (Time/Date Group: Yr mo date 24hr-time eg. 20131117 0930 Mtn/Pcfc/Zulu/etc:')
              print(oldL9)
              newL9 = str(input('Enter the change : ') or (oldL9))
              print()
              print('[10] Equipment (Weapons, equip, supplies, vehicles, armor, etc.):')
              print(oldL10)
              newL10 = str(input('Enter the change : ') or (oldL10))
              print()
              print('[11] Narrative/Comments:')
              print(oldL11)
              newL11 = str(input('Enter the change : ') or (oldL11))
              print()
              print()
              print('New Answers are...')
              print()
              print('L01: ',newL1)
              print('L02: ',newL2)
              print('L03: ',newL3)
              print('L04: ',newL4)
              print('L05: ',newL5)
              print('L06: ',newL6)
              print('L07: ',newL7)
              print('L08: ',newL8)
              print('L09: ',newL9)
              print('L10: ',newL10)
              print('L11: ',newL11)
              print()
              print('Are all changes made to satisfaction?')
              answer=input('[Y]es or [N]o? ')
              if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
                    print('Spot updated')
                    break
    GenSpotv3()
    print('Files were created')


# M A I N
if __name__ == "__main__":
          
    main()













          
