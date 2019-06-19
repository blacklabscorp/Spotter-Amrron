import json
import os

# Env Data & Working directories
workingDir=os.path.dirname(os.path.abspath(__file__))
dataDir='\\SpotData\\'
dataPath=workingDir+dataDir
configTarget={}

# Load and Print            
def ConfigsJSONInPrint(dataPath):
    target=str(dataPath)
    configTarget=((target)+'SpotOut_Secrets.json')
    print (configTarget)
    with open(configTarget, 'r') as f:
        parsed = json.load(f)
        print(parsed)
    return configTarget


ConfigsJSONInPrint(dataPath)
for item in configTarget:
    print('This is the file: ',item)
