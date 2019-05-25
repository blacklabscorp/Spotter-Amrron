# K2S file conversion from HTML form data to Dict to Json file

# Load libraries
import json
import os

# Constants from Env variables not from Defaults file
callsign=os.environ["s_callsign"]
k2sFileDefault=os.environ["s_k2sDefault"]
k2SFileLatest=k2sFileDefault
xsdict={}

def AmrronSpotRepv3(workingDir,dataDir,k2sDefault):
        print('K2S Menu for FlMsg file')
        print()
        print('[E] Enter file name')
        print('[D[ Default file name')
        print('[L] Latest file name:')
        print()
        while True:
                K2SMenu=input('K2s Menu')
                if K2SMenu=="E":
                        print()
                        k2sFileEntry=input('file name: ')
                        k2sFileCurrent=workingDir+dataDir+k2sFileEntry
                        break
                if K2SMenu=="D":
                        print()
                        k2sFileCurrent=workingDir+dataDir+k2sDefault
                        break
                if K2sMenu=="L":
                        print()
                        k2sFileCurrent=dataDir+k2sFileLatest
#iterating through FlMsg file into a JSON format
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
                if line.startswith(callsign):
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
        with open('amrronSpot.json', 'w') as f:
                json.dump(xsdict, f, ensure_ascii=False)
        print(flmsg)
        print(header)
        print(callDate)
        print(formType)
        print(body) 




