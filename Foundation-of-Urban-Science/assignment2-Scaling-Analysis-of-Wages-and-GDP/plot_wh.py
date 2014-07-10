import pylab
import scipy
import csv
import sys
import scipy
import array
from matplotlib import *
from pylab import *
from scipy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def linreg(X, Y):
    """
    Summary
        Linear regression of y = ax + b
    Usage
        real, real, real = linreg(list, list)
    Returns coefficients to the regression line "y=ax+b" from x[] and y[], and R^2 Value
    """
    if len(X) != len(Y):  raise ValueError, 'unequal length'
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in map(None, X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    a, b = (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det
    meanerror = residual = 0.0
    for x, y in map(None, X, Y):
        meanerror = meanerror + (y - Sy/N)**2
        residual = residual + (y - a * x - b)**2
    RR = 1 - residual/meanerror
    ss = residual / (N-2)
    Var_a, Var_b = ss * N / det, ss * Sxx / det
    print sqrt(Var_a),sqrt(Var_b)
    #print "y=ax+b"
    #print "N= %d" % N
    #print "a= %g \pm t_{%d;\alpha/2} %g" % (a, N-2, sqrt(Var_a))
    #print "b= %g \pm t_{%d;\alpha/2} %g" % (b, N-2, sqrt(Var_b))
    #print "R^2= %g" % RR
    #print "s^2= %g" % ss
    return a, b, RR


params = {'axes.labelsize': 24,
          'text.fontsize': 20,
          'legend.fontsize': 20,
          'xtick.labelsize': 20,
          'ytick.labelsize': 20,
          'text.usetex': True}

pylab.rcParams.update(params)


for ii in range(42,43):

    g=open('pop_all.csv', 'r')
    reader=csv.reader(g,delimiter=',')

    gg=open('wages_all.csv', 'r')
    readerg=csv.reader(gg,delimiter=',')
    
    ggg=open('down.csv','rU')
    readggg=csv.reader(ggg,delimiter=',')

    clf()
    count=0
    name=[]
    FIPS=[]
    pop=[]
    sami=[]
    m = 0
    metro = []
    
    for y in readggg:
        if y[0]!= 'Fips':
            if y[0]!= '998':
                metro.append(y[0])
    for row in reader:
#        print row[3],row[2]
        if row[1]in metro and row[ii]>=50000:
            FIPS.append(row[1])
            name.append(row[2])
#        for i in range(3,len(row)):
            pop.append(int(float(row[ii])))
            count += 1
    for x in metro:
        if x not in FIPS:
            print x
    poplog=log10(pop)
    count=0
    wages=[]
    for row in readerg:
        for x in FIPS:
#            print 'new run', row[3],row[2],FIPS[count-2],row[1]
            if (x == row[1]):
#                print row[2],name[count-2]
#            for i in range(3,len(row)):                
                wages.append(float(row[ii]))
#        print row[ii]
        count+=1
    year=int(1966+ii)
    wageslog=log10(wages)

    print 'The year is',year
    print 'Number of Metropolitan Areas: pop, wages= ',len(poplog),len(wageslog)
    plot(poplog,wageslog,color='green',marker='o',ls='None',alpha=0.4)
   
    wgradient, wintercept, wr_value, wp_value, std_err = stats.linregress(poplog,wageslog)
    print "Gradient and intercept, wages", wgradient, wintercept
    print "R-squared", wr_value**2
    print "p-value", wp_value
    
    for x in range(0,len(poplog)):
        sami.append(wageslog[x]-wintercept-wgradient*poplog[x])
    plt.hist(sami, bins=20, normed=True)
    plt.title("2008 Metro Wages")
    plt.xlable("SAMIs")
    plt.ylabel("Probability")
    
    g.close()
    gg.close()
