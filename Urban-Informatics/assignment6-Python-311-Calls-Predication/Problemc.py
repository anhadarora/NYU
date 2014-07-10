import pandas as pd
import matplotlib.pyplot as plt
import numpy as ny
from pylab import *
import csv
from sklearn import cross_validation, linear_model, datasets
from random import shuffle
from scipy import stats

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

# practice 10-fold cross validation
km = cross_validation.KFold(len(incidents), n_folds = 10, shuffle = False)# set false to have one fixed outcome
rmse = []
r2 = []
rmsestd = []
finalr2 = []
ginalrmse = []
stdlist = []
for x in range(1, 6):
    rmseord = []
    r2ord = []
    for y, z in km:
        poly1 = np.polyfit(population1[y] ,incidents1[y] ,x )
        polyval = np.polyval(poly1, population1[z])
        rm = (((polyval - incidents1[z])**2).mean(axis = None))**.5
        rmseord.append(rm)
        testavg = sum(incidents1[z])/len(incidents1)
        avg = []
        for i in range(0, len(incidents1[z])):
            avg.append(testavg)
        residential = sum((polyval - incidents1[z])**2)
        total = sum((incidents1[z] - avg)**2)
        r2ord.append(1-(residential/total))
    rmse.append(sum(rmseord)/len(rmseord))
    r2.append(sum(r2ord)/len(r2ord))
    std = np.std(rmseord)
    stdlist.append(std)

# fit all the data
rmseall = []
stdall = []
for x in range(1, 6):
    poly1 = np.polyfit(population1, incidents1, x)
    polyval = np.polyval(poly1, population1)
    rm = (((polyval - incidents1)**2).mean(axis = None))**.5
    rmseall.append(rm)
    std = np.std(rmseall)
    stdall.append(std)
count = [i for i in range(1,6)]

# plot the data
f, ax = plt.subplots()
a, = plt.plot(count, rmse, marker = 'o', linestyle= '', color = 'r')

for x in range(1, 6):
    b, = plt.plot([x,x], [rmse[x-1]-stdlist[x-1],rmse[x-1]+stdlist[x-1]], color = 'r')

c, =  plt.plot(count, rmseall, marker = 'o', linestyle= '', color = 'b')
plt.legend([a, c, b],["10-fold CV","All Data Fit", "10-fold Error"], loc = 2) 
ax.xaxis.grid()
ax.yaxis.grid()
plt.ylim((3000, 23000))
plt.xlim((0, 6))
plt.title('10-fold CV RMSE VS all data fit by order of polynomial')
plt.savefig('Problem c.png')
