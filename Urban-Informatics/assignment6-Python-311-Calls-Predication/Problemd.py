import pandas as pd
import matplotlib.pyplot as plt
import numpy as ny
from pylab import *
import csv
from sklearn import cross_validation, linear_model, datasets
from random import shuffle

action = []
actions = open('labeled_data.csv','r')
for x in actions:
    action.append(x)
del action[0]

# parse the data
action2 = []
for x in action:
    action2.append(x.split(','))

population = []
incidents = []

for x in action2:
    population.append(float(x[1]))
    incidents.append(float(x[2]))
population1 = np.array(population, np.float)
incidents1 = np.array(incidents, np.float)
best = np.poly1d(np.polyfit(population1, incidents1, 3))

xaction = []
xactions = open('unlabeled_data.csv','r')
for x in xactions:
    xaction.append(x)
del xaction[0]

# parse the data
xaction2 = []
for x in xaction:
    xaction2.append(x.split(','))

popu = []
zip = []
pred = []

for x in xaction2:
    popu.append(float(x[1]))
    zip.append(float(x[0]))
popu1 = np.array(popu, np.float)
zip1 = np.array(zip, np.float)

for x in popu1:
    pred1 = best(x)
    pred.append(pred1)

act = open('predictdata.csv' ,'w')
act.write('zipcode'+','+'population'+','+'incident'+'\n')
for x in range(0, len(zip1)):
    act.write(str(zip1[x])+','+str(popu1[x])+','+str(pred[x])+'\n')
