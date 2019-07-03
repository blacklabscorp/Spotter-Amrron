# This is primarily a module to export the environment configs and saving as JSON to reload into other devices

import json
import os

# Env Data & Working directories
workingDir=os.environ["PWD"]
dataDir='/SpotData/'
configDir='/SpotConfigs/'
dataPath=workingDir+dataDir
configsPath=workingDir+configDir

# Load values from Env variables
callsignDefault=os.environ["s_callsignDefault"]
dmrIdDefault=os.environ["s_dmrIdDefault"]
xDefault=os.environ["s_xDefault"]
yDefault=os.environ["s_yDefault"]
gridDefault=os.environ["s_gridDefault"]
postalcodeDefault=os.environ["s_postalcodeDefault"]
k2sDefault=os.environ["s_k2sDefault"]
googleKey=os.environ["s_googleKey"]
#accuWeatherKey=os.environ["s_accuWeatherKey"]
OpenWeatherKey=os.environ["s_openWeatherKey"]
twilioAccountSid=os.environ["s_twilioAccountSid"]
twilioAmrronCell=os.environ["s_twilioAmrronCell"]
twilioAuthToken=os.environ["s_twilioAuthToken"]
amrron00User=os.environ["s_amrron00User"]
amrron01User=os.environ["s_amrron01User"]
#amrron02User=os.environ["s_amrron02User"]
#amrron03User=os.environ["s_amrron03User"]
#amrron04User=os.environ["s_amrron04User"]
#amrron05User=os.environ["s_amrron05User"]
amrron00Cell=os.environ["s_amrron00Cell"]
amrron01Cell=os.environ["s_amrron01Cell"]
#amrron02Cell=os.environ["s_amrron02Cell"]
#amrron03Cell=os.environ["s_amrron03Cell"]
#amrron04Cell=os.environ["s_amrron04Cell"]
#amrron05Cell=os.environ["s_amrron05Cell"]
amrron00Email=os.environ["s_amrron00Email"]
amrron01Email=os.environ["s_amrron01Email"]
#amrron02Email=os.environ["s_amrron02Email"]
#amrron03Email=os.environ["s_amrron03Email"]
#amrron04Email=os.environ["s_amrron04Email"]
#amrron05Email=os.environ["s_amrron05Email"]

# Create Dict
secretConfigs={}
secretConfigs={'s_callsignDefault':callsignDefault,
         's_dmrIdDefault':dmrIdDefault,
         's_k2sDefault':k2sDefault,
         's_xDefault':xDefault,
         's_yDefault':yDefault,
         's_gridDefault':gridDefault,
         's_postalcodeDefault':postalcodeDefault,
         's_googleKey':googleKey,
         #'s_accuWeatherKey':accuWeatherKey,
         's_OpenWeatherKey':OpenWeatherKey,
         's_twilioAccountSid':twilioAccountSid,
         's_twilioAmrronCell':twilioAmrronCell,
         's_twilioAuthToken':twilioAuthToken,
         's_amrron00User':amrron00User,
         's_amrron01User':amrron01User,
         #'s_amrron02User':amrron02User,
         #'s_amrron03User':amrron03User,
         #'s_amrron04User':amrron04User,
         #'s_amrron05User':amrron05User,
         's_amrron00Cell':amrron00Cell,
         's_amrron01Cell':amrron01Cell,
         #'s_amrron02Cell':amrron02Cell,
         #'s_amrron03Cell':amrron03Cell,
         #'s_amrron04Cell':amrron04Cell,
         #'s_amrron05Cell':amrron05Cell,
         's_amrron00Email':amrron00Email,
         's_amrron01Email':amrron01Email,
         #'s_amrron02Email':amrron02Email,
         #'s_amrron03Email':amrron03Email,
         #'s_amrron04Email':amrron04Email,
         #'s_amrron05Email':amrron05Email
         }

# Write Json
def ConfigsJSONOut(secretConfigs,configsPath):
    target=str(configsPath)
    configTarget=((target)+'SpotOut_Secrets.json')
    with open(configTarget, 'w') as f:
        json.dump(secretConfigs, f, ensure_ascii=False)
    return (configTarget)

# Load and Print            
def ConfigsJSONInPrint(configsPath):
    target=str(configsPath)
    configTarget=((target)+'SpotOut_Secrets.json')
    with open(configTarget, 'r') as f:
        parsed = json.load(f)
        print(parsed)
    return 

# print('Test Block')
# ConfigsJSONOut(secretConfigs,configsPath)
# ConfigsJSONInPrint(configsPath)
print('Secrets are here: ',configsPath)

