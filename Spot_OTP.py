# Libraries
import os
import json
import random
import pickle
import time
import fnmatch
import shutil

# Import QRCode from pyqrcode 
#import pyqrcode 
#from pyqrcode import QRCode 

# Capturing time 
import datetime
timestamp=''
timeLocalCurrent = datetime.datetime.now().isoformat()
timeUtcCurrent=datetime.datetime.utcnow()

# Env Data & Working directories
workingDir=os.path.dirname(os.path.abspath(__file__))
dataDir='\\SpotData\\'
dataPath=workingDir+dataDir

# Variables
OTP=''

def otp_main():
    print()
    print()
    OTPtStampUTC=()
    OTPtStampUTC=str(timeUtcCurrent)
    OTPtStampLocal=()
    OTPtStampLocal=str(timeLocalCurrent)
    t = time.localtime()
    timestamp=time.strftime('%Y%m%d-%H%M%S',t)
    from datetime import tzinfo, timedelta, datetime
    class TZ(tzinfo):
        def utcoffset(self, dt): return timedelta(minutes=-399)
    OTP=()
    OTPtIn=()
    OTPtOut=()
    OTP=(OTPtStampUTC,OTPtStampLocal,'OUT',OTPtOut,'IN',OTPtIn)
    target=str(dataPath)
    configTargetPickle=((target)+'SpotOut_OTP_'+timestamp+'.pickle')
    configTargetSvg=((target)+'SpotOut_OTP_'+timestamp+'.svg')
    # String which represent the QR code 
    print(configTargetSvg)
    # Generate QR code 
    #url = pyqrcode.create(configTargetSvg) 
    # Create and save the png file naming "[references download location].png" 
    #url.svg(configTargetSvg, scale = 8)
    with open(configTargetPickle, 'wb') as f:
        pickle.dump(OTP, f)
    return (configTargetSvg)

# Building the IN Pads
def padin():
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
    ingressS2500=str(ingress5[0])
    ingressS2501=str(ingress5[1])
    ingressS2502=str(ingress5[2])
    ingressS2503=str(ingress5[3])
    ingressS2504=str(ingress5[4])
    ingressS2505=str(ingress5[5])
    ingressS2506=str(ingress5[6])
    ingressS2507=str(ingress5[7])
    ingressS2508=str(ingress5[8])
    ingressS2509=str(ingress5[9])
    ingressS2510=str(ingress5[10])
    ingressS2511=str(ingress5[11])
    ingressS2512=str(ingress5[12])
    ingressS2513=str(ingress5[13])
    ingressS2514=str(ingress5[14])
    ingressS2515=str(ingress5[15])
    ingressS2516=str(ingress5[16])
    ingressS2517=str(ingress5[17])
    ingressS2518=str(ingress5[18])
    ingressS2519=str(ingress5[19])
    ingressS2520=str(ingress5[20])
    ingressS2521=str(ingress5[21])
    ingressS2522=str(ingress5[22])
    ingressS2523=str(ingress5[23])
    ingressS2524=str(ingress5[24])
    ingressS2525=str(ingress5[25])
    ingressS2526=str(ingress5[26])
    ingressS2527=str(ingress5[27])
    ingressS2528=str(ingress5[28])
    ingressS2529=str(ingress5[29])
    ingressS2530=str(ingress5[30])
    ingressS2531=str(ingress5[31])
    ingressS2532=str(ingress5[32])
    ingressS2533=str(ingress5[33])
    ingressS2534=str(ingress5[34])
    ingressS2535=str(ingress5[35])
    ingressS2536=str(ingress5[36])
    ingressS2537=str(ingress5[37])
    ingressS2538=str(ingress5[38])
    ingressS2539=str(ingress5[39])
    ingressS2540=str(ingress5[40])
    ingressS2541=str(ingress5[41])
    ingressS2542=str(ingress5[42])
    ingressS2543=str(ingress5[43])
    ingressS2544=str(ingress5[44])
    ingressS2545=str(ingress5[45])
    ingressS2546=str(ingress5[46])
    ingressS2547=str(ingress5[47])
    ingressS2548=str(ingress5[48])
    ingressS2549=str(ingress5[49])
    ingressS25_00=ingressS2500+' '+ingressS2501+' '+ingressS2502+' '+ingressS2503+' '+ingressS2504
    ingressS25_05=ingressS2505+' '+ingressS2506+' '+ingressS2507+' '+ingressS2508+' '+ingressS2509
    ingressS25_10=ingressS2510+' '+ingressS2511+' '+ingressS2512+' '+ingressS2513+' '+ingressS2514
    ingressS25_15=ingressS2515+' '+ingressS2516+' '+ingressS2517+' '+ingressS2518+' '+ingressS2519
    ingressS25_20=ingressS2520+' '+ingressS2521+' '+ingressS2522+' '+ingressS2523+' '+ingressS2524
    ingressS25_25=ingressS2525+' '+ingressS2526+' '+ingressS2527+' '+ingressS2528+' '+ingressS2529
    ingressS25_30=ingressS2530+' '+ingressS2531+' '+ingressS2532+' '+ingressS2533+' '+ingressS2534
    ingressS25_35=ingressS2535+' '+ingressS2536+' '+ingressS2537+' '+ingressS2538+' '+ingressS2539
    ingressS25_40=ingressS2540+' '+ingressS2541+' '+ingressS2542+' '+ingressS2543+' '+ingressS2544
    ingressS25_45=ingressS2545+' '+ingressS2546+' '+ingressS2547+' '+ingressS2548+' '+ingressS2549
    print('Inbound')
    print('Local Time: ',timeLocalCurrent)
    print('UTC Time:   ',timeUtcCurrent)
    print()
    print(ingressS25_00)
    print(ingressS25_05)
    print(ingressS25_10)
    print(ingressS25_15)
    print(ingressS25_20)
    print(ingressS25_25)
    print(ingressS25_30)
    print(ingressS25_35)
    print(ingressS25_40)
    print(ingressS25_45)
    print()
    OTPIn={}
    OTPIn={ingressS25_00,ingressS25_05,ingressS25_10,ingressS25_15,ingressS25_20,ingressS25_25,ingressS25_30,ingressS25_35,ingressS25_40,ingressS25_45}

# Building the OUT Pads
def padout():
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
    egress={}
    egressSolo={}
    egress5={}
    egress25={}
    while z250 <250:
           egressSolo[z250]=(random.sample(range(0, 9),1))
           z250=z250+1
    while z50 <51:
           egress5[z50]=(egressSolo[z50+0]+egressSolo[z50+1]+egressSolo[z50+2]+egressSolo[z50+3]+egressSolo[z50+4])
           z50=z50+1
    while z25 <25:
           egress25[z25]=(egress5[z25+0]+egress5[z25+1]+egress5[z25+2]+egress5[z25+3]+egress5[z25+4])
           z25=z25+1

              
    egressS2500=str(egress5[0])
    egressS2501=str(egress5[1])
    egressS2502=str(egress5[2])
    egressS2503=str(egress5[3])
    egressS2504=str(egress5[4])
    egressS2505=str(egress5[5])
    egressS2506=str(egress5[6])
    egressS2507=str(egress5[7])
    egressS2508=str(egress5[8])
    egressS2509=str(egress5[9])
    egressS2510=str(egress5[10])
    egressS2511=str(egress5[11])
    egressS2512=str(egress5[12])
    egressS2513=str(egress5[13])
    egressS2514=str(egress5[14])
    egressS2515=str(egress5[15])
    egressS2516=str(egress5[16])
    egressS2517=str(egress5[17])
    egressS2518=str(egress5[18])
    egressS2519=str(egress5[19])
    egressS2520=str(egress5[20])
    egressS2521=str(egress5[21])
    egressS2522=str(egress5[22])
    egressS2523=str(egress5[23])
    egressS2524=str(egress5[24])
    egressS2525=str(egress5[25])
    egressS2526=str(egress5[26])
    egressS2527=str(egress5[27])
    egressS2528=str(egress5[28])
    egressS2529=str(egress5[29])
    egressS2530=str(egress5[30])
    egressS2531=str(egress5[31])
    egressS2532=str(egress5[32])
    egressS2533=str(egress5[33])
    egressS2534=str(egress5[34])
    egressS2535=str(egress5[35])
    egressS2536=str(egress5[36])
    egressS2537=str(egress5[37])
    egressS2538=str(egress5[38])
    egressS2539=str(egress5[39])
    egressS2540=str(egress5[40])
    egressS2541=str(egress5[41])
    egressS2542=str(egress5[42])
    egressS2543=str(egress5[43])
    egressS2544=str(egress5[44])
    egressS2545=str(egress5[45])
    egressS2546=str(egress5[46])
    egressS2547=str(egress5[47])
    egressS2548=str(egress5[48])
    egressS2549=str(egress5[49])
    egressS25_00=egressS2500+' '+egressS2501+' '+egressS2502+' '+egressS2503+' '+egressS2504
    egressS25_05=egressS2505+' '+egressS2506+' '+egressS2507+' '+egressS2508+' '+egressS2509
    egressS25_10=egressS2510+' '+egressS2511+' '+egressS2512+' '+egressS2513+' '+egressS2514
    egressS25_15=egressS2515+' '+egressS2516+' '+egressS2517+' '+egressS2518+' '+egressS2519
    egressS25_20=egressS2520+' '+egressS2521+' '+egressS2522+' '+egressS2523+' '+egressS2524
    egressS25_25=egressS2525+' '+egressS2526+' '+egressS2527+' '+egressS2528+' '+egressS2529
    egressS25_30=egressS2530+' '+egressS2531+' '+egressS2532+' '+egressS2533+' '+egressS2534
    egressS25_35=egressS2535+' '+egressS2536+' '+egressS2537+' '+egressS2538+' '+egressS2539
    egressS25_40=egressS2540+' '+egressS2541+' '+egressS2542+' '+egressS2543+' '+egressS2544
    egressS25_45=egressS2545+' '+egressS2546+' '+egressS2547+' '+egressS2548+' '+egressS2549
    OTPOut={}
    OTPOut={egressS25_00,egressS25_05,egressS25_10,egressS25_15,egressS25_20,egressS25_25,egressS25_30,egressS25_35,egressS25_40,egressS25_45}
    print('Outbound')
    print('Local Time: ',timeLocalCurrent)
    print('UTC Time:   ',timeUtcCurrent)
    print()
    print(egressS25_00)
    print(egressS25_05)
    print(egressS25_10)
    print(egressS25_15)
    print(egressS25_20)
    print(egressS25_25)
    print(egressS25_30)
    print(egressS25_35)
    print(egressS25_40)
    print(egressS25_45)

# Conversion Table CT NO 1 English
def ctno1english():
    z100=0
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
    # Print Reference Grid
    print ('code',code,'01',Code[code,1],' 02',Code[code,2],' 03',Code[code,3],' 04',Code[code,4],' 05',Code[code,5],' 06',Code[code,6])
    print ('70',Code[code,70],'  71',Code[code,71],' 72',Code[code,72],' 73',Code[code,73],' 74',Code[code,74],' 75',Code[code,75],' 76',Code[code,76],' 77',Code[code,77],' 78',Code[code,78],'   79',Code[code,79])
    print ('80',Code[code,80],'  81',Code[code,81],' 82',Code[code,82],' 83',Code[code,83],' 84',Code[code,84],' 85',Code[code,85],' 86',Code[code,86],' 87',Code[code,87],' 88',Code[code,88],'   89',Code[code,89])
    print ('90',Code[code,90],'91',Code[code,91],' 92',Code[code,92],' 93',Code[code,93],'94',Code[code,94],' 95',Code[code,95],' 96',Code[code,96],' 97',Code[code,97],' 98',Code[code,98],' 99',Code[code,99])
    print()

# M A I N
if __name__ == "__main__":
    otp_main()
    ctno1english()
    padin()
    padout()
    
