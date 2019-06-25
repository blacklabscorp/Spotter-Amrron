# Module High-Level: Imports a default JSON (per report type) from the SpotData folder,
# this is to cold start data entry with some default values.
# Next step is a collection of input statements vetting defaults for changes
# These vetted inputs then become the new files to be written...
# Last JSON file representing the last generated HTML form per type (Spot vs Sit) can be
# used to re-warm the entry fields with the last sent report
# HTML forms are stored in the SpotData as well as the FLMsg messages folder for transmission

# Load libraries
import json
import os
import time
import shutil
import datetime
from Spot_Defaults import *

# Capturing time 
timeLocalCurrent = datetime.datetime.now().isoformat()
timeUtcCurrent = datetime.datetime.utcnow()

# Capturing GPS / Grid defaults
xDefault = os.environ['s_xDefault']
xDefaultStr = str (xDefault)
xCurrent = xDefault
yDefault = os.environ['s_yDefault']
yDefaultStr = str (yDefault)
yCurrent = yDefault
gridDefault = os.environ['s_gridDefault']
cityDefault = os.environ['s_cityDefault']
stateDefault = os.environ['s_stateDefault']

# Env Data & Working directories
workingDir = os.path.dirname(os.path.abspath(__file__))
dataDir = '\\SpotData\\'
dataPath = workingDir+dataDir
target = str(dataPath)

# FlMsg working directories
UserProfile = os.environ['USERPROFILE']
flMsgWorkingDir = UserProfile+'\\NBEMS.files\\ICS\\messages\\'
k2sFileDefault = os.environ['s_K2sDefault']

# Constants from Env variables not from Defaults file
callsignDefault = os.environ['s_callsignDefault']
k2sFileDefault = os.environ['s_k2sDefault']
k2sFileLatest = k2sFileDefault
k2sFileCurrent = k2sFileDefault

# DateTime
t = time.gmtime()
timestamp = time.strftime('%Y%m%d-%H%M%S',t)
timestampFlMsg = time.strftime('%Y%m%d-%H%M%S',t)

#Global scoped variables
oldL01_sr = ''
oldL21_sr = ''
oldL03_sr = ''
oldL04_sr = ''
oldL05_sr = ''
oldL06_sr = ''
oldL07_sr = ''
oldL08_sr = ''
oldL09_sr = ''
oldL10_sr = ''
oldL11_sr = ''
oldL12_sr = ''
oldL13_sr = ''
oldL14_sr = ''
oldL15_sr = ''
oldL16_sr = ''
oldL17_sr = ''
newL01_sr = ''
newL21_sr = ''
newL03_sr = ''
newL04_sr = ''
newL05_sr = ''
newL06_sr = ''
newL07_sr = ''
newL08_sr = ''
newL09_sr = ''
newL10_sr = ''
newL11_sr = ''
newL12_sr = ''
newL13_sr = ''
newL14_sr = ''
newL15_sr = ''
newL16_sr = ''
newL17_sr = ''
oldL01_sp = ''
oldL02_sp = ''
oldL03_sp = ''
oldL04_sp = ''
oldL05_sp = ''
oldL06_sp = ''
oldL07_sp = ''
oldL08_sp = ''
oldL09_sp = ''
oldL10_sp = ''
oldL11_sp = ''
newL01_sp = ''
newL02_sp = ''
newL03_sp = ''
newL04_sp = ''
newL05_sp = ''
newL06_sp = ''
newL07_sp = ''
newL08_sp = ''
newL09_sp = ''
newL10_sp = ''
newL11_sp = ''

# Set variables
from Spot_Defaults import *

configTarget = ''
spotRep = {}
sitRep = {}

# Create the new Spotv3_0 report data
# first writing the HTML form then creating the Last Json
def genspotrepv3_0(spotFileFormat,target):
    global newL01_sp
    global newL02_sp
    global newL03_sp
    global newL04_sp
    global newL05_sp
    global newL06_sp
    global newL07_sp
    global newL08_sp
    global newL09_sp
    global newL10_sp
    global newL11_sp
    global amrronSpotReportNew
    target = str(dataPath)
    amrronSpotReportNew = ''
    spotFileFormat=(timestampFlMsg+'-'+newL03_sp+'-'+stateDefault+'-'+callsignPrefix+'-SP000.k2s')
    amrronSpotReportNew = (spotFileFormat)
    with open((target+amrronSpotReportNew),'w',encoding = 'utf-8') as f:
        f.write('<flmsg>2.0.5'+'\n')
        f.write(':hdr_ed:22'+'\n')
        f.write('<customform>'+'\n')
        f.write('mg:179 CUSTOM_FORM,AMRRON_SPOTREPV3_0.html'+'\n')
        f.write('L01,'+newL01_sp+'\n')
        f.write('L02,'+callsignDefault+'\n')
        f.write('L03,'+newL03_sp+'\n')
        f.write('L04,'+newL04_sp+'\n')
        f.write('L05,'+newL05_sp+'\n')
        f.write('L06,'+newL06_sp+'\n')
        f.write('L07,'+newL07_sp+'\n')
        f.write('L08,'+newL08_sp+'\n')
        f.write('L09,'+newL09_sp+'\n')
        f.write('L10,'+newL10_sp+'\n')
        f.write('L11,'+newL11_sp+'\n')
    # Write of SpotRep JSON Last to Dict then Json
    spotRepJson = {}
    spotRepJson['FlMsgVersion']='<flmsg>2.0.5'
    spotRepJson['FlMsgTimestamp']=timestampFlMsg
    spotRepJson['FlMsgHeader']='hdr_ed:22'
    spotRepJson['FlgMsgCustom']='<customform>'
    spotRepJson['mg'] = '179 CUSTOM_FORM,AMRRON_SITREPV3_0.html'
    spotRepJson['L01'] = newL01_sp
    spotRepJson['L21'] = callsignDefault
    spotRepJson['L03'] = newL03_sp
    spotRepJson['L04'] = newL04_sp
    spotRepJson['L05'] = newL05_sp
    spotRepJson['L06'] = newL06_sp
    spotRepJson['L07'] = newL07_sp
    spotRepJson['L08'] = newL08_sp
    spotRepJson['L09'] = newL09_sp
    spotRepJson['L10'] = newL10_sp
    spotRepJson['L11'] = newL11_sp
    configTarget = (target+'SpotOut_SpotRepV3_0Last.json')
    with open(configTarget, 'w') as f:
        json.dump(spotRepJson, f, ensure_ascii=False)
    print()
    print('SpotOut Data Files for Spot Reports')
    print('-----------------------------------')
    print('JSON:')
    print('Last SpotRep report called: SpotOut_SpotRepV3_0Last')
    print(  'stored here: ',configTarget)
    print()
    print('HTML Form:')
    print(  'Stored here in FlMsg folder: ',flMsgWorkingDir) 
    print(' ',(flMsgWorkingDir+amrronSpotReportNew))
    print(  'Stored in the SpotData folder: ',target)
    print(' ',(target+amrronSpotReportNew))
    print()
    return (amrronSpotReportNew)
# Create the new SitRepv3_0 report data
# first writing the HTML form then creating the Last Json
def gensitrepv3_0(sitFileFormat,target):
    global newL01_sr
    global newL21_sr
    global newL03_sr
    global newL04_sr
    global newL05_sr
    global newL06_sr
    global newL07_sr
    global newL08_sr
    global newL09_sr
    global newL10_sr
    global newL11_sr
    global newL12_sr
    global newL13_sr
    global newL14_sr
    global newL15_sr
    global newL16_sr
    global newL17_sr
    global amrronSitReportNew
    target = str(dataPath)
    sitFileFormat=(timestampFlMsg+'-'+newL03_sr+'-'+stateDefault+'-'+callsignPrefix+'-SR000.k2s')
    amrronSitReportNew = (sitFileFormat)
    # Writes HTML file for the FLMsg folder then copies to SpotData
    with open((target+amrronSitReportNew),'w',encoding = 'utf-8') as f:
        f.write('<flmsg>2.0.5'+'\n')
        #f.write(callsignDefault+' '+timestampFlMsg+'\n')
        f.write(':hdr_ed:22'+'\n')
        f.write('<customform>'+'\n')
        f.write(':mg:179 CUSTOM_FORM,AMRRON_SITREPV3_0.html'+'\n')
        f.write('L01,'+newL01_sr+'\n')
        f.write('L21,'+callsignDefault+'\n')
        f.write('L03,'+newL03_sr+'\n')
        f.write('L04,'+newL04_sr+'\n')
        f.write('L05,'+newL05_sr+'\n')
        f.write('L06,'+newL06_sr+'\n')
        f.write('L07,'+newL07_sr+'\n')
        f.write('L08,'+newL08_sr+'\n')
        f.write('L09,'+newL09_sr+'\n')
        f.write('L10,'+newL10_sr+'\n')
        f.write('L11,'+newL11_sr+'\n')
        f.write('L12,'+newL12_sr+'\n')
        f.write('L13,'+newL13_sr+'\n')
        f.write('L14,'+newL14_sr+'\n')
        f.write('L15,'+newL15_sr+'\n')
        f.write('L16,'+newL16_sr+'\n')
        f.write('L17,'+newL17_sr+'\n')     
    # Write of SitRep JSON Last;Dict to Json
    sitRepJson={}
    sitRepJson['FlMsgVersion']='<flmsg>2.0.5'
    sitRepJson['FlMsgTimestamp']=timestampFlMsg
    sitRepJson['FlMsgHeader']='hdr_ed:22'
    sitRepJson['FlgMsgCustom']='<customform>'
    sitRepJson['mg:']='179 CUSTOM_FORM,AMRRON_SITREPV3_0.html'
    sitRepJson['L01']=newL01_sr
    sitRepJson['L21']=callsignDefault
    sitRepJson['L03']=newL03_sr
    sitRepJson['L04']=newL04_sr
    sitRepJson['L05']=newL05_sr
    sitRepJson['L06']=newL06_sr
    sitRepJson['L07']=newL07_sr
    sitRepJson['L08']=newL08_sr
    sitRepJson['L09']=newL09_sr
    sitRepJson['L10']=newL10_sr
    sitRepJson['L11']=newL11_sr
    sitRepJson['L12']=newL12_sr
    sitRepJson['L13']=newL13_sr
    sitRepJson['L14']=newL14_sr
    sitRepJson['L15']=newL15_sr
    sitRepJson['L16']=newL16_sr
    sitRepJson['L17']=newL17_sr
    configTarget = (target+'SpotOut_SitRepV3_0Last.json')
    with open(configTarget, 'w') as f:
        json.dump(sitRepJson, f, ensure_ascii=False)
    print()
    print('SpotOut Data Files')
    print('------------------')
    print('JSON:')
    print('Last SitRep report called: SpotOut_SitRepV3_0Last')
    print(  'stored here: ',configTarget)
    print()
    print('HTML Form:')
    print(  'Stored here in FlMsg folder: ',flMsgWorkingDir) 
    print(' ',(flMsgWorkingDir+amrronSitReportNew))
    print(  'Stored in the SpotData folder: ',target)
    print(' ',(target+amrronSitReportNew))
    print()
    return (amrronSitReportNew)
# Cold starts the input verification process
# aka 'SpotOut_AmrronSpotRepV3_0Default.json' file
def spotrepv3_0load(spotFileFormat,target):
    configSpotRepTarget=((target)+'SpotOut_SpotRepV3_0Default.json')
    with open(configSpotRepTarget) as json_file:
        spotRep = json.load(json_file)
    global oldL01_sp
    global oldL02_sp
    global oldL03_sp
    global oldL04_sp
    global oldL05_sp
    global oldL06_sp
    global oldL07_sp
    global oldL08_sp
    global oldL09_sp
    global oldL10_sp
    global oldL11_sp
    global newL01_sp
    global newL02_sp
    global newL03_sp
    global newL04_sp
    global newL05_sp
    global newL06_sp
    global newL07_sp
    global newL08_sp
    global newL09_sp
    global newL10_sp
    global newL11_sp
    oldL01_sp=str(spotRep['L01'])
    oldL02_sp=str(spotRep['L02'])
    oldL03_sp=str(spotRep['L03'])
    oldL04_sp=str(spotRep['L04'])
    oldL05_sp=str(spotRep['L05'])
    oldL06_sp=str(spotRep['L06'])
    oldL07_sp=str(spotRep['L07'])
    oldL08_sp=str(spotRep['L08'])
    oldL09_sp=str(spotRep['L09'])
    oldL10_sp=str(spotRep['L10'])
    oldL11_sp=str(spotRep['L11'])
    while True:
        print()
        print('[1] TO: Receipient: Current...')
        print(oldL01_sp)
        newL01_sp = str(input('Enter the change : ') or (oldL01_sp))
        print()
        print('[2] FROM: Sender): Current...')
        print(callsignDefault)
        newL02_sp = str(input('Enter the change : ') or (callsignDefault))
        print()
        print('[3] Precedence (Routine,Priority,Immediate,Flash): Current...')
        print(oldL03_sp)
        newL03_sp = str(input('Enter the change : ') or ('ROU'))
        print()
        print('[4] Current DTG: (YYYYMMDD-HHMMZ Use UTC):')
        print(timestamp)
        newL04_sp = str(input('Enter the change : ') or (timestamp))
        print()
        print('[5] Size(Platoon? Battalion? #Vehicles #Persons):')
        print(oldL05_sp)
        newL05_sp = str(input('Enter the change : ') or (oldL05_sp))
        print()
        print('[6] Activity(Convoy, Checkpoint, Patrol, Cordon, Training, Interrogation, Relocating/evacuating Citizens, Etc):')
        print(oldL06_sp)
        newL06_sp = str(input('Enter the change : ') or (oldL06_sp))
        print()
        print('[7] Location: ((GPS/Grid Coord, address, road name/#, Direction, proximity to landmarks, nearest town, etc.)')
        print ('Default GPS: ',xDefault,' ',yDefault,'   ''Default Grid',gridDefault)
        print('Current GPS: ',xCurrent,' ',yCurrent )
        newL07_sp = str(input('Enter the change : ') or (gridDefault)) 
        print()
        print('[8] Unit (Domestic/Foreign, Police, Military, branch, guard/reserve, Unit Designation, civ supt, volunteer, etc.):')
        print(oldL08_sp)
        newL08_sp = str(input('Enter the change : ') or (oldL08_sp))
        print()
        print('[9] Time & Duration (Time/Date Group: Yr mo date 24hr-time eg. 20131117 0930 Mtn/Pcfc/Zulu/etc.):')
        print(oldL09_sp)
        newL09_sp = str(input('Enter the change : ') or (oldL09_sp))
        print()
        print('[10] Equipment (Weapons, equip, supplies, vehicles, armor, etc.):')
        print(oldL10_sp)
        newL10_sp = str(input('Enter the change : ') or (oldL10_sp))
        print()
        print('[11] Narrative/Comment:')
        print(oldL11_sp)
        newL11_sp = str(input('Enter the change : ') or (oldL11_sp))
        print()
        print()
        print('New Answers are...')
        print()
        print('L01: ',newL01_sp)
        print('L02: ',newL02_sp)
        print('L03: ',newL03_sp)
        print('L04: ',newL04_sp)
        print('L05: ',newL05_sp)
        print('L06: ',newL06_sp)
        print('L07: ',newL07_sp)
        print('L08: ',newL08_sp)
        print('L09: ',newL09_sp)
        print('L10: ',newL10_sp)
        print('L11: ',newL11_sp)
        print()
        print('Are all changes made to SpotRep?')
        answer=input('[Y]es or [N]o? ')
        if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
            break
        return (newL03_sp)

# Cold starts the input verification process
# aka 'SpotOut_AmrronSitRepV3_0Default.json' file
def sitrepv3_0load(sitFileFormat,target):
    configSitRepTarget=((target)+'SpotOut_SitRepV3_0Default.json')
    with open(configSitRepTarget) as json_file:
        sitRep = json.load(json_file)
    global oldL01_sr
    global oldL21_sr
    global oldL03_sr
    global oldL04_sr
    global oldL05_sr
    global oldL06_sr
    global oldL07_sr
    global oldL08_sr
    global oldL09_sr
    global oldL10_sr
    global oldL11_sr
    global oldL12_sr
    global oldL13_sr
    global oldL14_sr
    global oldL15_sr
    global oldL16_sr
    global oldL17_sr
    global newL01_sr
    global newL21_sr
    global newL03_sr
    global newL04_sr
    global newL05_sr
    global newL06_sr
    global newL07_sr
    global newL08_sr
    global newL09_sr
    global newL10_sr
    global newL11_sr
    global newL12_sr
    global newL13_sr
    global newL14_sr
    global newL15_sr
    global newL16_sr
    global newL17_sr
    oldL01_sr=str(sitRep['L01'])
    oldL21_sr=str(sitRep['L21'])
    oldL03_sr=str(sitRep['L03'])
    oldL04_sr=str(sitRep['L04'])
    oldL05_sr=str(sitRep['L05'])
    oldL06_sr=str(sitRep['L06'])
    oldL07_sr=str(sitRep['L07'])
    oldL08_sr=str(sitRep['L08'])
    oldL09_sr=str(sitRep['L09'])
    oldL10_sr=str(sitRep['L10'])
    oldL11_sr=str(sitRep['L11'])
    oldL12_sr=str(sitRep['L12'])
    oldL13_sr=str(sitRep['L13'])
    oldL14_sr=str(sitRep['L14'])
    oldL15_sr=str(sitRep['L15'])
    oldL16_sr=str(sitRep['L16'])
    oldL17_sr=str(sitRep['L17'])
    while True:
        print()
        print('[1] TO: Receipient: Current...')
        print(oldL01_sr)
        newL01_sr = str(input('Enter the change : ') or (oldL01_sr))
        print()
        print('[2] FROM: Sender): Current...')
        print(callsignDefault)
        newL21_sr = str(input('Enter the change : ') or (callsignDefault))
        print()
        print('[3] Precedence: (Routine,Priority,Immediate,Flash) Current...')
        print(oldL03_sr)
        newL03_sr = str(input('Enter the change : ') or ('ROU'))
        print()
        print('[4] Current DTG: (YYYYMMDD-HHMMZ Use UTC):')
        print(timestamp)
        newL04_sr = str(input('Enter the change : ') or (timestamp))
        print()
        print('[5] Incident#:')
        print(oldL05_sr)
        newL05_sr = str(input('Enter the change : ') or (oldL05_sr))
        print()
        print('[6] Expirations YYYYMMDD-HHMMz use UTC:')
        print(oldL06_sr)
        newL06_sr = str(input('Enter the change : ') or (oldL06_sr))
        print()
        print('[7] Location (Location: (Lat/Lon, Grid Square, City):')
        print ('Default GPS: ',xDefault,' ',yDefault,'   ','Default Grid',gridDefault)
        print('Current GPS: ',xCurrent,' ',yCurrent )
        newL07_sr = str(input('Enter the change : ') or (gridDefault)) 
        print()
        print('[8] Incident Status (New, Ongoing, Resolved):')
        print(oldL07_sr)
        newL08_sr = str(input('Enter the change : ') or (oldL08_sr))
        print()
        print('[9] Size & Scope(Local,Regional,National):')
        print(oldL09_sr)
        newL09_sr = str(input('Enter the change : ') or (oldL09_sr))
        print()
        print('[10] Overall Hazard (Green, Yellow, Red):')
        print(oldL10_sr)
        newL10_sr = str(input('Enter the change : ') or (oldL10_sr))
        print()
        print('[11] Current Weather (Green,Yellow,Red):')
        print(oldL11_sr)
        newL11_sr = str(input('Enter the change : ') or (oldL11_sr))
        print()
        print('[12] 48 hr Weather (Green,Yellow,Red):')
        print(oldL12_sr)
        newL12_sr = str(input('Enter the change : ') or (oldL12_sr))
        print()
        print()
        print('[13] Infrastructure (Green,Yellow,Red):')
        print(oldL13_sr)
        newL13_sr = str(input('Enter the change : ') or (oldL13_sr))
        print()
        print('[14] Political (Green,Yellow,Red):')
        print(oldL14_sr)
        newL14_sr = str(input('Enter the change : ') or (oldL14_sr))
        print()
        print('[15] Civil(Green,Yellow,Red):')
        print(oldL15_sr)
        newL15_sr = str(input('Enter the change : ') or (oldL15_sr))
        print('New Answers are for Spot Report...')
        print()
        print('[16] Communications (Green,Yellow,Red):')
        print(oldL16_sr)
        newL16_sr = str(input('Enter the change : ') or (oldL16_sr))
        print()
        print('[17] Remarks:')
        print(oldL17_sr)
        newL17_sr = str(input('Enter the change : ') or (oldL17_sr))
        print()
        print()
        print('L01: ',newL01_sr)
        print('L02: ',newL21_sr)
        print('L03: ',newL03_sr)
        print('L04: ',newL04_sr)
        print('L05: ',newL05_sr)
        print('L06: ',newL06_sr)
        print('L07: ',newL07_sr)
        print('L08: ',newL08_sr)
        print('L09: ',newL09_sr)
        print('L10: ',newL10_sr)
        print('L11: ',newL11_sr)
        print('L12: ',newL12_sr)
        print('L13: ',newL13_sr)
        print('L14: ',newL14_sr)
        print('L15: ',newL15_sr)
        print('L16: ',newL16_sr)
        print('L17: ',newL17_sr)
        print()
        print('Are all changes made to the Spot Report?')
        answer=input('[Y]es or [N]o? ')
        if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
            break
        return (newL03_sr)

def flmsgout_amrronv3_0_main():
    print('Which Report do you want to create...')
    
    
    report=input('Create [spotv30] or [sitv30]?')
    if report in ['spotv30','sitv30']:
        if report=='spotv30':
            spotFileFormat=(timestampFlMsg+newL03_sp+'-'+stateDefault+'-'+callsignPrefix+'-000.k2s')
            spotrepv3_0load(spotFileFormat,target)
            genspotrepv3_0(spotFileFormat,target)
            shutil.copy2((target+amrronSpotReportNew),(flMsgWorkingDir+amrronSpotReportNew))
        if report=='sitv30':
            sitFileFormat=(timestampFlMsg+newL03_sr+'-'+stateDefault+'-'+callsignPrefix+'-000.k2s')
            sitrepv3_0load(sitFileFormat,target)
            gensitrepv3_0(sitFileFormat,target)
            shutil.copy((target+amrronSitReportNew),(flMsgWorkingDir+amrronSitReportNew))
 
# M A I N
if __name__ == "__main__":
          
   flmsgout_amrronv3_0_main ()














          
