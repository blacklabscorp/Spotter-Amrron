# Uses 'SpotOut_EarthquakeMags.json' file to extract last 24 hr earthquakes Mag/location

import json
import objectpath
import os
from objectpath import *

# Env Data & Working directories
workingDir=os.path.dirname(os.path.abspath(__file__))
dataDir='\\SpotData\\'
dataPath=workingDir+dataDir
target=str(dataPath)

def Earthquakes24hrs():
    xCount=0
    configTarget=((target)+'SpotOut_Earthquakes.json')
    with open(configTarget) as json_file:  
        data = json.load(json_file)
    tree_obj = objectpath.Tree(data)
    place=tuple(tree_obj.execute('$..properties.place'))
    mag=tuple(tree_obj.execute('$..properties.mag'))
    url=tuple(tree_obj.execute('$..properties.url'))
    detail=tuple(tree_obj.execute('$..properties.detail'))
    x=tuple(tree_obj.execute('$..properties.geometry.coordinates.0'))
    y=tuple(tree_obj.execute('$..properties.geometry.coordinates.1'))
    earthquakes = dict(zip(mag,place))
    for item in place:
        xCount=xCount+1
    print('Total Earthquakes in last 24 hrs: ',xCount)
    print(earthquakes)
    configTarget=((target)+'SpotOut_EarthquakeMags.json')
    with open(configTarget, 'w') as f:
        json.dump(earthquakes, f, ensure_ascii=False)
    print (configTarget)
#print('Test case')
#Earthquakes24hrs()
