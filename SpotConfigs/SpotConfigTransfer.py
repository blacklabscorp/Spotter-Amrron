# Module Purpose: Using a SpotOut_secrets.json file created using SpotConfigs.py or from the Output in the Inputs directory off main

import json
import os

# Env Data & Working directories
workingDir=os.path.dirname(os.path.abspath(__file__))
configDir='\\'
configPath=workingDir+configDir
configTarget={}
configExports={}

# Load and Print            
def ConfigsJSONInPrint(configPath):
    global configExports
    target=str(configPath)
    configTarget=((target)+'SpotOut_Secrets.json')
    with open(configTarget, 'r') as f:
       configExports  = json.load(f)
       print(json.dumps(configExports, indent=4, sort_keys=True))
    return (target)

def config_main():
    ConfigsJSONInPrint(configPath)
    print()
    print()
    print('Config Import Menu')
    print('__________________')
    print()
    print('[PC Empty] settings text file')
    print()
    print('[PC Secrets] settings text file')
    print()
    print('[RPI Empty] settings text file')
    print()
    print('[RPI Secrets] settings text file')
    print()
    print('[X] Exit no exports')
    print()
    export=input('which export would you like? ')
    print()
    if export=='PC Empty':
        print ('PC_Empty.txt will be placed in Config folder: ',configPath)
        with open(('PC_Empty.txt'),'w',encoding = 'utf-8') as f:
            for item in configExports:
                f.write('Key'+item+'='+'\n')
        print()
    if export=='PC Secrets':
        print ('PcEnvironmentSetup_Secrets.txt will be placed in Config folder: ',configPath)
        with open(('PC_Secrets.txt'),'w',encoding = 'utf-8') as f:
            for item in configExports:
                f.write('echo '+item+'='+configExports[item]+'\n')
    if export=='RPI Empty':
        print ('RPI_Empty.txt will be placed in Config folder: ',configPath)
        print (configPath)
        print()
        with open(('RPI_Empty.txt'),'w',encoding = 'utf-8') as f:
            for item in configExports:
                f.write('echo '+item+'='+'\n')
    if export=='RPI Secrets':
        print ('RPI_Secrets.txt will be placed in Config folder: ',configPath)
        print (configPath)
        print()
        with open(('RPI_Secrets.txt'),'w',encoding = 'utf-8') as f:
            for item in configExports:
                f.write('echo '+item+'='+configExports[item]+'\n')
    if export=='X':
       quit()

        
# M A I N
if __name__ == "__main__":
          
   config_main ()



