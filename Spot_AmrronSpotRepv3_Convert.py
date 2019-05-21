import json
import os
callsign='YOUR CALLSIGN HERE'
xsdict={}
from Spot_Defaults import callsign
#iterating through FlMsg file into a JSON format
for line in open('KK6JGJ-20190511-231736Z-2.html.k2s'):
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
with open('amrronSpot.txt', 'w') as f:
        json.dump(xsdict, f, ensure_ascii=False) 

print(flmsg)
print(header)
print(callDate)
print(formType)
print(body) 




