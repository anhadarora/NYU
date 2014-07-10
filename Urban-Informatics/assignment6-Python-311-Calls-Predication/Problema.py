import pandas as pd
import matplotlib.pyplot as plt
import numpy as ny
from pylab import *
import csv

action = []
actions = open('labeled_data.csv','r')
for x in actions:
    action.append(x)
del action[0]

# parse the data
action2 = []
for x in action:
    action2.append(x.split(','))

zipcode = []
population = []
incidents = []
incidents2 = []
population2 = []
zipcode2 = []

for x in action2:
    zipcode.append(x[0])
    population.append(x[1])
    incidents.append(x[2])
    if float(x[2]) >= 100: # the areas with more than 100 incidents
        incidents2.append(x[2])
        population2.append(x[1])
        zipcode2.append(x[0])

zipcode = np.array(zipcode)
zipcode1 = np.array(zipcode, np.float)
population1 = np.array(population, np.float)
incidents1 = np.array(incidents, np.float)
incidents2 = np.array(incidents2,np.float)
zipcode2 = np.array(zipcode2, np.float)
population2 = np.array(population2, np.float)

# plot all the data
plt.scatter(population1, incidents1, 5, color = 'b')
plt.xlim((-10000, 125000))
plt.ylim((-10000, 140000))
plt.title('Population VS Incidents')
plt.savefig('Problem a1.png')
plt.clf()

plt.scatter(zipcode1,incidents1, 5, color = 'b')
plt.ylim((-10000, 140000))
plt.title('Zipcodes VS Incidents')
plt.savefig('Problem a2.png')
plt.clf()

plt.scatter(population2, incidents2, 5, color = 'b')
plt.xlim((-10000, 125000))
plt.ylim((-10000, 140000))
plt.title('Population VS Incidents')
plt.savefig('Problem a3.png')
plt.clf()

plt.scatter(zipcode2,incidents2, 5, color = 'b')
plt.ylim((-10000, 140000))
plt.title('Zipcodes VS Incidents')
plt.savefig('Problem a4.png')
