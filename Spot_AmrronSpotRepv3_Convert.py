# K2S file conversion from HTML form data to Dict to Json file

# Load libraries
import json
import os
import glob

from Spot_FLMsgOut_Spotv3 import GenSpotv3

# Env Data & Working directories
workingDir=os.path.dirname(os.path.abspath(__file__))
dataDir='\\SpotData\\'
dataPath=workingDir+dataDir

# FlMsg working directories
UserProfile=os.environ["USERPROFILE"]
flMsgWorkingDir=UserProfile+'\\NBEMS.files\\ICS\\messages\\'
k2sFileDefault=os.environ["s_K2sDefault"]
fileBucket = glob.glob(flMsgWorkingDir+'\\*.k2s')
k2sFileLatest = max(fileBucket, key=os.path.getctime)
k2sFileCurrent=k2sFileLatest

# Constants from Env variables not from Defaults file
callsignDefault=os.environ["s_callsignDefault"]
k2sFileDefault=os.environ["s_k2sDefault"]
k2sFileLatest=k2sFileDefault
xsdict={}

def AmrronSpotRepv3(workingDir,dataDir,k2sFileDefault,flMsgWorkingDir,callsignDefault,k2sFileCurrent,dataPath):
        print('K2S Menu for FlMsg file')
        print()
        print('[E]nter file name:')
        print()
        print('[D]efault (last file) from FlMsg folder:',flMsgWorkingDir,'using latest file...')
        print(k2sFileCurrent)
        print()
        print('[N]ew Spotv3 Report')
        print()
        while True:
                k2sMenu=input('K2s Menu: ')
                if k2sMenu=="E":
                        print()
                        k2sFileEntry=input('file name: ')
                        if k2sFileEntry == "x" : break
                        try:
                                k2sDataPath=str(dataPath)
                                k2sFileCurrent=dataPath+k2sFileEntry
                        except:
                                print('Invalid Input')
                                continue
                        print(k2sFileCurrent)
                        AmrronSpotRepv3Json(workingDir,dataDir,k2sFileDefault,flMsgWorkingDir,callsignDefault,k2sFileCurrent,dataPath)
                        break
                if k2sMenu=="D":
                        print()
                        fileBucket = glob.glob(flMsgWorkingDir+'\\*.k2s')
                        #print(fileBucket)
                        k2sFileLatest = max(fileBucket, key=os.path.getctime)
                        k2sFileCurrent=k2sFileLatest
                        print(k2sFileCurrent)
                        AmrronSpotRepv3Json(workingDir,dataDir,k2sFileDefault,flMsgWorkingDir,callsignDefault,k2sFileCurrent,dataPath)
                        break
                if k2sMenu=="N":
                        print()
                        k2sFileCurrent=k2sFileDefault
                        GenSpotv3()
                        break
        return (k2sFileCurrent)

#iterating through FlMsg file into a JSON format
def AmrronSpotRepv3Json (workingDir,dataDir,k2sFileDefault,flMsgWorkingDir,callsignDefault,k2sFileCurrent,dataPath):
        for line in open(k2sFileCurrent):
        # trim whitespace
                line=line.rstrip()
                print()
                if line.startswith('<flmsg>'):
                        flmsg=line
                        print(line,end=' ')
                        a='<flmsg>'
                        b=line
                        xsdict[a]=b
                if line.startswith(':hdr'):
                        header=line
                        print(line,end=' ')
                        a=':hdr'
                        b=line
                        xsdict[a]=b
                if line.startswith(callsignDefault):
                        callDate=line
                        print(line,end=' ')
                        a='callDate'
                        b=line
                        xsdict[a]=b
                if line.startswith('<customform>'):
                        formType=line
                        print(line,end=' ')
                        a='<customform>'
                        b=line
                        xsdict[a]=b
                if line.startswith(':mg:179'):
                        body=line
                        print(line,end=' ')
                        a=':mg:179'
                        b=line
                        xsdict[a]=b
                if line.startswith('L01'):
                        xs=line.split(',')
                        print(line,end=' ')
                        a=xs[0]
                        b=xs[1]
                        xsdict[a]=b
                if line.startswith('L03'):
                        xs=line.split(',')
                        print(line,end=' ')
                        a=xs[0]
                        b=xs[1]
                        xsdict[a]=b
                if line.startswith('L04'):
                        xs=line.split(',')
                        print(line,end=' ')
                        a=xs[0]
                        b=xs[1]
                        xsdict[a]=b
                if line.startswith('L05'):
                        xs=line.split(',')
                        print(line,end=' ')
                        a=xs[0]
                        b=xs[1]
                        xsdict[a]=b
                if line.startswith('L06'):
                        xs=line.split(',')
                        print(line,end=' ')
                        a=xs[0]
                        b=xs[1]
                        xsdict[a]=b
                if line.startswith('L07'):
                        xs=line.split(',')
                        print(line,end=' ')
                        a=xs[0]
                        b=xs[1]
                        xsdict[a]=b
                if line.startswith('L08'):
                        xs=line.split(',')
                        print(line,end=' ')
                        a=xs[0]
                        b=xs[1]
                        xsdict[a]=b
                if line.startswith('L09'):
                        xs=line.split(',')
                        print(line,end=' ')
                        a=xs[0]
                        b=xs[1]
                        xsdict[a]=b
                if line.startswith('L10'):
                        xs=line.split(',')
                        print(line,end=' ')
                        a=xs[0]
                        b=xs[1]
                        xsdict[a]=b
                if line.startswith('L11'):
                        xs=line.split(',')
                        print(line,end=' ')
                        a=xs[0]
                        b=xs[1]
                        xsdict[a]=b
        # Write the json file
        target=str(dataPath)
        configTarget=((target)+'SpotOut_AmrronSpotV3.json')
        with open(configTarget, 'w') as f:
                json.dump(xsdict, f, ensure_ascii=False)
        return (xsdict)

# Test Block
AmrronSpotRepv3(workingDir,dataDir,k2sFileDefault,flMsgWorkingDir,callsignDefault,k2sFileCurrent,dataPath)
#AmrronSpotRepv3Json(workingDir,dataDir,k2sFileDefault,flMsgWorkingDir,callsignDefault,k2sFileCurrent,dataPath)


# Pre-Req Pip Install
# NONE
