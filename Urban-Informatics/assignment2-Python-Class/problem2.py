# Gang Zhao, Assignment 2, Problem 2
import csv
import sys
myFile = open('zipCodes.csv','r')
content = csv.reader(myFile, delimiter = ',')
rawlines = []
content.next()
for line in content:
    total = line[10]
    if total != '': # ignore the zip area without population
        density = float(line[10])/float(line[7]) # calculate the density of each zip area
        zip = int(line[1])
        lines = zip, density
        rawlines.append(lines)
# sort by zip and output
newlines = sorted(rawlines)
outputFile = open('output_density_problem2.txt','w')
for x in newlines:
    outputFile.write(str(x)+'\n')
outputFile.close()
myFile.close()
