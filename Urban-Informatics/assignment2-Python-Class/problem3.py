# Gang Zhao, Assignment 2, Problem 3
from zipcode import Zipcode
from borough import Borough
import csv

boroughs = {}
boroughfile = open('boroughs.csv','r')
boroughcon = csv.reader(boroughfile,delimiter= ',')
popfile = open('zipCodes.csv','r')
popcon = csv.reader(popfile,delimiter= ',')
incidfile = open('Incidents_grouped_by_Address_and_Zip.csv','r')
incidcon = csv.reader(incidfile,delimiter= ',')
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
# calculate the incidents of each borough
incidcon.next()
for incidline in incidcon:
    zipincid = incidline[2]
    for x in boroughs.keys():
        for y in boroughs[x].zipcodes:
            if incidline[1] == y:
                boroughs[x].addIncident(int(incidline[2]))
#output
outputFile = open('output_problem3.txt','w')
for x in sorted(boroughs.keys()):
    outputFile.write(x + ' '+ str(boroughs[x].incidents/float(boroughs[x].populations)) +'\n')
outputFile.close()
