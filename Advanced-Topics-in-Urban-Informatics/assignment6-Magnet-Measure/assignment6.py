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
 #   pickx, picky = m(data['pickup_longitude'], data['pickup_latitude'])#transfer into basemap positions
 #   dropx, dropy = m(data['dropoff_longitude'], data['dropoff_latitude'])#transfer into basemap positions
 #   along = [float(long1), float(long2)]
 #   alat = [float(lat1), float(lat2)]
 #   areax = [min(along), max(along), max(along), min(along), min(along)]# the x positions of the boundary
 #   areay = [min(alat), min(alat), max(alat), max(alat), min(alat)]# the y positions of the boundary
    xcord = map(float , xcord)
    ycord = map(float, ycord)
    areaxx, areayy = m(xcord, ycord)# transfer into basemap x and y positions
  #  if pord == 'pickup':# check whether it's "pickup" or "dropoff", plot points of the queried one the later in case they are covered
   #     dropoff, = plt.plot(dropx, dropy, '.', markersize = 2, color= 'b')# plot the points
    #    pickup, = plt.plot( pickx, picky, '.', markersize = 2,  color = 'r')
     #   pordx, = plt.plot(areaxx, areayy, '--', color = 'r')# plot the boundary
      #  plt.legend([pickup, dropoff, pordx],["Pickups","Dropoffs","Pickup Area"], loc = 2)# plot the legend
    #if pord == 'dropoff':  
#	pickup, = plt.plot( pickx, picky, '.', markersize = 2,  color = 'r')
    dropoff, = plt.plot(areaxx, areayy, '.', markersize = 10, color= 'r')
#	pordy, = plt.plot(areaxx, areayy, '--', color = 'b') 
    plt.legend([dropoff],["Stations"], loc = 2) 
    for label, x, y in zip(labels,areaxx, areayy ):
        plt.text(x+1000, y, label, color = 'r')
    plt.title('NYC Stations')
 #   plt.show()
    plt.savefig('12.png', dpi=300)

# define the function to get matrix


if __name__ == '__main__':

    xcord = ['-73.879267',' -73.909047', '-73.925588', '-73.937186', '-73.955302', '-73.968016', '-73.975078','-73.994320','-73.980846','-73.994702', '-74.004113', '-73.981082' ]
    ycord = ['40.874902', '40.846354', '40.828011','40.804517', '40.779661','40.762069', '40.750851','40.725845', '40.576900','40.636139', '40.654365', '40.689817' ]
    label = ['205 Street', '174-175 Street', '161 Street Yankee Stadium','125 Street', '86 Street','59 Street', 'Grand Central 42 St', 'Bleecker Street','Coney Island-Stillwell Avenue','50 Street', '36 Street', 'Dekalb Avenue' ]
    y = getmap(xcord, ycord, label)
	
    stocks = pd.read_table('Worksheet.csv', sep=',')
    x = stocks['Total']
    y = stocks['Total Field']
    x = x[:12]
    y = y[:12]
    datas = np.arange(12)
    print x
    print y

    xx, = plt.plot( datas, x, 'bo--')
    yy, = plt.plot( datas, y, 'ro--')
    plt.legend([xx, yy],["Cals","Obse"], loc = 1)   
    plt.title('Magnet total field Calulations VS Observations')
    plt.savefig('informatics.png', dpi=300)

 
