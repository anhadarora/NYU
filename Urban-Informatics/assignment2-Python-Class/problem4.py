# Gang Zhao, Assignment 2, Problem 4
from zipcode import Zipcode
from borough import Borough
import csv
import sys

boroughname = sys.argv[1]
boroughs = {}
average = {}
boroughfile = open('boroughs.csv','r')
boroughcon = csv.reader(boroughfile,delimiter= ',')
popfile = open('zipCodes.csv','r')
popcon = csv.reader(popfile,delimiter= ',')
# remove the duplicates
def clean(list):
    checked = []
    for x in list:
       if x not in checked:
           checked.append(x)
    return checked
# make a dict
boroughs['Manhattan'] = Borough('Manhattan')
boroughs['Brooklyn'] = Borough('Brooklyn')
boroughs['Queens'] = Borough('Queens')
boroughs['Bronx'] = Borough('Bronx')
boroughs['Staten'] = Borough('Staten')
# find the zipcodes in each borough 
for zipline in boroughcon:
    zipcode = zipline[0]
    for x in boroughs.keys():
        if zipline[1]== x:
            boroughs[x].addZipcode(zipcode)
# clean
for x in boroughs.keys():
    boroughs[x].zipcodes = clean(boroughs[x].zipcodes)
# calculate the population of each borough
popcon.next()
for popline in popcon:
    zippop = popline[10]
    if zippop !='':
        for x in boroughs.keys():
            for y in boroughs[x].zipcodes:
                if popline[1] == y:
                    boroughs[x].addPopulation(int(popline[10]))
# calculate the average population of each borough
for x in boroughs.keys():
    average[x] = boroughs[x].populations/float(len(boroughs[x].zipcodes))
    if x == boroughname.capitalize():
        print x,average[x]
