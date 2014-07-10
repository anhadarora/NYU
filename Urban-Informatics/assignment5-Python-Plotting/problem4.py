# Gang Zhao, Assignment 5, Problem4

import pandas as pd
import matplotlib.pyplot as plt
import numpy as ny
from pylab import *

# read the file and deal with the data 
gen = [[],[],[],[]]
action = []
actions = open('genes.dat','r')
for x in actions:
    action.append(x)
del action[0]

# parse the data
action2 = []
for x in action:
    action2.append(x.split(','))
prolist = []
yearlist = []
translist = []
for x in action2:
    gen[0].append(x[0])
    gen[1].append(x[1])
    gen[2].append(x[2])
    gen[3].append(x[3].strip())

# draw the matrix
fig,axarray = plt.subplots(4,4)
xy = [0,0.5,1]
gen[0] = np.array(gen[0], np.float)
gen[1] = np.array(gen[1], np.float)
gen[2] = np.array(gen[2], np.float)
gen[3]= np.array(gen[3], np.float)

# draw each one in the matrix
for i in range (0,4):
    ax = axarray[i,0]
    ax.scatter(gen[0], gen[i], 5, color = 'k')
    p = ny.poly1d(ny.polyfit(gen[0],gen[i],5))
    ax.plot(xy, p(xy), color = 'r')
    ax.xaxis.set_major_locator(plt.FixedLocator([0,0.5,1]))
    ax.yaxis.set_major_locator(plt.FixedLocator([0,0.5,1]))
    ax.tick_params(axis='both', direction='out', labelsize=0)
    ax.set_xlim(-.2, 1.2)
    ax.set_ylim(-.2, 1.2)
    x0,x1 = ax.get_xlim()
    y0,y1 = ax.get_ylim()
    ax.set_aspect((x1-x0)/(y1-y0))
    ax.xaxis.grid()
    ax.yaxis.grid()

for i in range (0,4):
    for j in range (1,4):
        ax = axarray[i,j]
        ax.scatter(gen[i], gen[j], 5, color = 'k')
        ax.xaxis.set_major_locator(plt.FixedLocator([0,0.5,1]))
        ax.yaxis.set_major_locator(plt.FixedLocator([0,0.5,1]))
        ax.tick_params(axis='both', direction='out', labelsize=0)
        ax.set_xlim(-.2, 1.2)
        ax.set_ylim(-.2, 1.2)
        x0,x1 = ax.get_xlim()
        y0,y1 = ax.get_ylim()
        ax.set_aspect((x1-x0)/(y1-y0))
        ax.xaxis.grid()
        ax.yaxis.grid()

# set lables and title
axarray[0,0].set_ylabel('A', rotation = 'horizontal')
axarray[1,0].set_ylabel('B', rotation = 'horizontal')
axarray[2,0].set_ylabel('C', rotation = 'horizontal')
axarray[3,0].set_ylabel('D', rotation = 'horizontal')
axarray[3,0].set_xlabel('A')
axarray[3,1].set_xlabel('B')
axarray[3,2].set_xlabel('C')
axarray[3,3].set_xlabel('D')        
plt.suptitle('Gene Correlations', size=14)
plt.savefig("Problem 4.png")
