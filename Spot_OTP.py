# Libraries
import os
import json
import random
import pickle
import time
import fnmatch
import shutil

# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 

# Capturing time 
import datetime
timeLocalCurrent = datetime.datetime.now().isoformat()
timeUtcCurrent=datetime.datetime.utcnow()

# Env Data & Working directories
workingDir=os.path.dirname(os.path.abspath(__file__))
dataDir='\\SpotData\\'
dataPath=workingDir+dataDir

# Write Pickle file
def SpotOTP_PickleOut(OTP):
    target=str(dataPath)
    configTargetPickle=((target)+'SpotOut_OTP_'+timestamp+'.pickle')
    configTargetSvg=((target)+'SpotOut_OTP_'+timestamp+'.svg')
    # String which represent the QR code 
    print(configTargetSvg)
    # Generate QR code 
    url = pyqrcode.create(configTargetSvg) 
    # Create and save the png file naming "[references download location].png" 
    url.svg(configTargetSvg, scale = 8)
    with open(configTargetPickle, 'wb') as f:
        pickle.dump(OTP, f)
    return (configTargetSvg)
  


# OTP for Inbound 
x=0
y=0
z=0
z5=1
z25=0
z50=0
z250=0
target=''
configTarget=0
configTargetStr=''
ingress={}
ingressSolo={}
ingress5={}
ingress25={}

while z250 <250:
          ingressSolo[z250]=(random.sample(range(0, 9),1))
          #ingress[x,y]=(random.sample(range(0, 9), 5))
          #print(z250,ingress[x,y])
          z250=z250+1
          x=x+1
          y=y+1
while z50 <51:
          ingress5[z50]=(ingressSolo[z50+0]+ingressSolo[z50+1]+ingressSolo[z50+2]+ingressSolo[z50+3]+ingressSolo[z50+4])
          z50=z50+1
while z25 <25:
          ingress25[z25]=(ingress5[z25+0]+ingress5[z25+1]+ingress5[z25+2]+ingress5[z25+3]+ingress5[z25+4])
          z25=z25+1

IngressS2500=str(ingress5[0])
IngressS2501=str(ingress5[1])
IngressS2502=str(ingress5[2])
IngressS2503=str(ingress5[3])
IngressS2504=str(ingress5[4])
IngressS2505=str(ingress5[5])
IngressS2506=str(ingress5[6])
IngressS2507=str(ingress5[7])
IngressS2508=str(ingress5[8])
IngressS2509=str(ingress5[9])
IngressS2510=str(ingress5[10])
IngressS2511=str(ingress5[11])
IngressS2512=str(ingress5[12])
IngressS2513=str(ingress5[13])
IngressS2514=str(ingress5[14])
IngressS2515=str(ingress5[15])
IngressS2516=str(ingress5[16])
IngressS2517=str(ingress5[17])
IngressS2518=str(ingress5[18])
IngressS2519=str(ingress5[19])
IngressS2520=str(ingress5[20])
IngressS2521=str(ingress5[21])
IngressS2522=str(ingress5[22])
IngressS2523=str(ingress5[23])
IngressS2524=str(ingress5[24])
IngressS2525=str(ingress5[25])
IngressS2526=str(ingress5[26])
IngressS2527=str(ingress5[27])
IngressS2528=str(ingress5[28])
IngressS2529=str(ingress5[29])
IngressS2530=str(ingress5[30])
IngressS2531=str(ingress5[31])
IngressS2532=str(ingress5[32])
IngressS2533=str(ingress5[33])
IngressS2534=str(ingress5[34])
IngressS2535=str(ingress5[35])
IngressS2536=str(ingress5[36])
IngressS2537=str(ingress5[37])
IngressS2538=str(ingress5[38])
IngressS2539=str(ingress5[39])
IngressS2540=str(ingress5[40])
IngressS2541=str(ingress5[41])
IngressS2542=str(ingress5[42])
IngressS2543=str(ingress5[43])
IngressS2544=str(ingress5[44])
IngressS2545=str(ingress5[45])
IngressS2546=str(ingress5[46])
IngressS2547=str(ingress5[47])
IngressS2548=str(ingress5[48])
IngressS2549=str(ingress5[49])

IngressS25_00=IngressS2500+' '+IngressS2501+' '+IngressS2502+' '+IngressS2503+' '+IngressS2504
IngressS25_05=IngressS2505+' '+IngressS2506+' '+IngressS2507+' '+IngressS2508+' '+IngressS2509
IngressS25_10=IngressS2510+' '+IngressS2511+' '+IngressS2512+' '+IngressS2513+' '+IngressS2514
IngressS25_15=IngressS2515+' '+IngressS2516+' '+IngressS2517+' '+IngressS2518+' '+IngressS2519
IngressS25_20=IngressS2520+' '+IngressS2521+' '+IngressS2522+' '+IngressS2523+' '+IngressS2524
IngressS25_25=IngressS2525+' '+IngressS2526+' '+IngressS2527+' '+IngressS2528+' '+IngressS2529
IngressS25_30=IngressS2530+' '+IngressS2531+' '+IngressS2532+' '+IngressS2533+' '+IngressS2534
IngressS25_35=IngressS2535+' '+IngressS2536+' '+IngressS2537+' '+IngressS2538+' '+IngressS2539
IngressS25_40=IngressS2540+' '+IngressS2541+' '+IngressS2542+' '+IngressS2543+' '+IngressS2544
IngressS25_45=IngressS2545+' '+IngressS2546+' '+IngressS2547+' '+IngressS2548+' '+IngressS2549

print('Inbound')
print('Local Time: ',timeLocalCurrent)
print('UTC Time:   ',timeUtcCurrent)
print()
print(IngressS25_00)
print(IngressS25_05)
print(IngressS25_10)
print(IngressS25_15)
print(IngressS25_20)
print(IngressS25_25)
print(IngressS25_30)
print(IngressS25_35)
print(IngressS25_40)
print(IngressS25_45)
print()

OTPIn={}
OTPIn={IngressS25_00,IngressS25_05,IngressS25_10,IngressS25_15,IngressS25_20,IngressS25_25,IngressS25_30,IngressS25_35,IngressS25_40,IngressS25_45}



# OTP for Outbound 

x=0
y=0
z=0
z5=1
z25=0
z50=0
z250=0
egress={}
egressSolo={}
egress5={}
egress25={}

while z250 <250:
          egressSolo[z250]=(random.sample(range(0, 9),1))
          #egress[x,y]=(random.sample(range(0, 9), 5))
          #print(z250,egress[x,y])
          z250=z250+1
          x=x+1
          y=y+1
while z50 <51:
          egress5[z50]=(egressSolo[z50+0]+egressSolo[z50+1]+egressSolo[z50+2]+egressSolo[z50+3]+egressSolo[z50+4])
          z50=z50+1
while z25 <25:
          egress25[z25]=(egress5[z25+0]+egress5[z25+1]+egress5[z25+2]+egress5[z25+3]+egress5[z25+4])
          z25=z25+1

EgressS2500=str(egress5[0])
EgressS2501=str(egress5[1])
EgressS2502=str(egress5[2])
EgressS2503=str(egress5[3])
EgressS2504=str(egress5[4])
EgressS2505=str(egress5[5])
EgressS2506=str(egress5[6])
EgressS2507=str(egress5[7])
EgressS2508=str(egress5[8])
EgressS2509=str(egress5[9])
EgressS2510=str(egress5[10])
EgressS2511=str(egress5[11])
EgressS2512=str(egress5[12])
EgressS2513=str(egress5[13])
EgressS2514=str(egress5[14])
EgressS2515=str(egress5[15])
EgressS2516=str(egress5[16])
EgressS2517=str(egress5[17])
EgressS2518=str(egress5[18])
EgressS2519=str(egress5[19])
EgressS2520=str(egress5[20])
EgressS2521=str(egress5[21])
EgressS2522=str(egress5[22])
EgressS2523=str(egress5[23])
EgressS2524=str(egress5[24])
EgressS2525=str(egress5[25])
EgressS2526=str(egress5[26])
EgressS2527=str(egress5[27])
EgressS2528=str(egress5[28])
EgressS2529=str(egress5[29])
EgressS2530=str(egress5[30])
EgressS2531=str(egress5[31])
EgressS2532=str(egress5[32])
EgressS2533=str(egress5[33])
EgressS2534=str(egress5[34])
EgressS2535=str(egress5[35])
EgressS2536=str(egress5[36])
EgressS2537=str(egress5[37])
EgressS2538=str(egress5[38])
EgressS2539=str(egress5[39])
EgressS2540=str(egress5[40])
EgressS2541=str(egress5[41])
EgressS2542=str(egress5[42])
EgressS2543=str(egress5[43])
EgressS2544=str(egress5[44])
EgressS2545=str(egress5[45])
EgressS2546=str(egress5[46])
EgressS2547=str(egress5[47])
EgressS2548=str(egress5[48])
EgressS2549=str(egress5[49])

EgressS25_00=EgressS2500+' '+EgressS2501+' '+EgressS2502+' '+EgressS2503+' '+EgressS2504
EgressS25_05=EgressS2505+' '+EgressS2506+' '+EgressS2507+' '+EgressS2508+' '+EgressS2509
EgressS25_10=EgressS2510+' '+EgressS2511+' '+EgressS2512+' '+EgressS2513+' '+EgressS2514
EgressS25_15=EgressS2515+' '+EgressS2516+' '+EgressS2517+' '+EgressS2518+' '+EgressS2519
EgressS25_20=EgressS2520+' '+EgressS2521+' '+EgressS2522+' '+EgressS2523+' '+EgressS2524
EgressS25_25=EgressS2525+' '+EgressS2526+' '+EgressS2527+' '+EgressS2528+' '+EgressS2529
EgressS25_30=EgressS2530+' '+EgressS2531+' '+EgressS2532+' '+EgressS2533+' '+EgressS2534
EgressS25_35=EgressS2535+' '+EgressS2536+' '+EgressS2537+' '+EgressS2538+' '+EgressS2539
EgressS25_40=EgressS2540+' '+EgressS2541+' '+EgressS2542+' '+EgressS2543+' '+EgressS2544
EgressS25_45=EgressS2545+' '+EgressS2546+' '+EgressS2547+' '+EgressS2548+' '+EgressS2549

OTPOut={}
OTPOut={EgressS25_00,EgressS25_05,EgressS25_10,EgressS25_15,EgressS25_20,EgressS25_25,EgressS25_30,EgressS25_35,EgressS25_40,EgressS25_45}


print('Outbound')
print('Local Time: ',timeLocalCurrent)
print('UTC Time:   ',timeUtcCurrent)
print()
print(EgressS25_00)
print(EgressS25_05)
print(EgressS25_10)
print(EgressS25_15)
print(EgressS25_20)
print(EgressS25_25)
print(EgressS25_30)
print(EgressS25_35)
print(EgressS25_40)
print(EgressS25_45)

# Conversion Table CT NO 1 English
code=0
Code={}
Code[code,0]='Code0'
Code[code,1]='A'
Code[code,2]='E'
Code[code,3]='I'
Code[code,4]='N'
Code[code,5]='O'
Code[code,6]='T'
Code[code,70]='B'
Code[code,71]='C'
Code[code,72]='D'
Code[code,73]='F'
Code[code,74]='G'
Code[code,75]='H'
Code[code,76]='J'
Code[code,77]='K'
Code[code,78]='L'
Code[code,79]='M'
Code[code,80]='P'
Code[code,81]='Q'
Code[code,82]='R'
Code[code,83]='S'
Code[code,84]='U'
Code[code,85]='V'
Code[code,86]='W'
Code[code,87]='X'
Code[code,88]='Y'
Code[code,89]='Z'
Code[code,90]='Fig'
Code[code,91]='.'
Code[code,92]=':'
Code[code,93]='""'
Code[code,94]=' '
Code[code,95]='+'
Code[code,96]='-'
Code[code,97]='='
Code[code,98]='REQ'
Code[code,99]='SPC'


# Main
print()
print()
OTPtStampUTC=()
OTPtStampUTC=str(timeUtcCurrent)
OTPtStampLocal=()
OTPtStampLocal=str(timeLocalCurrent)


t = time.localtime()
timestamp=time.strftime('%Y%m%d-%H%M%S',t)
#timestamp =time.str


from datetime import tzinfo, timedelta, datetime
class TZ(tzinfo):
          def utcoffset(self, dt): return timedelta(minutes=-399)



OTP=()
OTPtIn=()
OTPtOut=()
OTPtOut=(OTPOut)
OTPtIn=(OTPIn)
OTP=(OTPtStampUTC,OTPtStampLocal,'OUT',OTPtOut,'IN',OTPtIn)
SpotOTP_PickleOut(OTP)
