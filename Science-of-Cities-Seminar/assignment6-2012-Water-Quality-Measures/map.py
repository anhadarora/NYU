import csv
import sys
import time
import datetime as dt
from matplotlib.dates import date2num
import matplotlib.dates as date
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import cKDTree
import pandas as pd


# define the function to plot on the map
def getmap(xcord, ycord, labels):
    fig = plt.figure(figsize =(15, 15))
    lllat = 40.473; urlat = 40.93; lllon = -74.27; urlon = -73.69 # define the boundary of the map
    m = Basemap(projection = 'stere', lon_0 = (urlon + lllon)/2, lat_0 = (urlat +lllat)/2, llcrnrlon = lllon, llcrnrlat = lllat, urcrnrlon = urlon, urcrnrlat = urlat, resolution= 'l')# create the basemap
    m.readshapefile('e:/cusp/datateam/project/taxi_data/desktop/nyczipregion','nyc',drawbounds = True)# indicate the absolute path of the map used       
    xcord = map(float , xcord)
    ycord = map(float, ycord)
    areaxx, areayy = m(xcord, ycord)# transfer into basemap x and y positions

    dropoff, = plt.plot(areaxx, areayy, '.', markersize = 10, color= 'r')
    plt.legend([dropoff],["Locations"], loc = 2) 
    for label, x, y in zip(labels,areaxx, areayy ):
        plt.text(x+300, y, label, color = 'r')
    plt.title('NYC Water Sampling Locations')
    plt.savefig('12.png', dpi=300)



if __name__ == '__main__':

    data = pd.read_csv('MG+harbor_sampling_coordinates.csv')
    xcord = data['LATITUDE']
    ycord = data['LONGITUDE']
    label = data['SITE']
    y = getmap(xcord, ycord, label)
 