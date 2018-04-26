#How to filter data
#matplotlib makes best Python plots

import json

import random

import pprint

import matplotlib.pyplot as plt

with open('broadway.json') as json_data:
    shows = json.load(json_data)

def from2001(c):
    return c['Date']['Year']==2001
                      
only2001=[]
for c in shows:
    if from2001(c):
        only2001.append(c)

with open('shows2001.json','w') as outfile:
    json.dump(only2001,outfile)

randomShow=random.sample(only2001,3)
##
##for show in randomShow:
##    print('name:', show['Show']['Name'])
##    print('show type:', show['Show']['Type'])
##    print('gross:','$', show['Statistics']['Gross'])
##    print('percentage of filled theater capacity over the week:', show['Statistics']['Capacity'],'%')
##    print('performance year:', show['Date']['Year'])
##    print('number of performances in the week:', show['Statistics']['Performances'])

print('{:25}'.format(randomShow['Show']['Name']))
