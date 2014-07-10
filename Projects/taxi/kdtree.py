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


# define the function to get all the pickups or dropoffs in the defined region
def getspace(dataframe, p_or_d, long_1, lat_1, long_2, lat_2):#receive the input of "pickup" or "dropoff" and two points which define the boundary
    long = [float(long_1), float(long_2)]
    lat = [float(lat_1), float(lat_2)]
    record = []
    x = dataframe[p_or_d+'_latitude']# read latitude column
    y = dataframe[p_or_d+'_longitude']# read longitude column
    z = [0 for i in range (0, len(x))]
    tree = cKDTree(zip(x, z))# build query tree of latitude
    tree1 = cKDTree(zip(y, z))# build query tree of longitude
    latrange = tree.query_ball_point([sum(lat)/float(len(lat)), 0], max(lat)-(sum(lat)/float(len(lat))))# query point indexes between two given latitudes
    longrange = tree1.query_ball_point([sum(long)/float(len(long)), 0], max(long)-(sum(long)/float(len(long)))) # query point indexes between two given longitudes
    inter_index = sorted(list(set(longrange).intersection(set(latrange))))# find the intersection of the two queries
    total_index = [i for i in range (0, len(x))]
    final_index = sorted(list(set(total_index).difference(set(inter_index))))
    record = stocks_df.drop(stocks_df.index[final_index])
    record.index = range(0, len(record))
    return(record)

# define the function to find out the records on certain day of the week
def gettime( data , inputday, pord):
    data[pord+'_time'] = pd.to_datetime(data[pord+'_time'],unit='s')
    data.index = data[pord+'_time']
    df = pd.DataFrame(np.arange(7), index = ['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun'])
    if inputday not in df.index:
        print 'Wrong weekday! Please enter Mon, Tues, Wednes, Thurs, Fri, Satur or Sun as the weekday'
        sys.exit()
    data = data[data.index.weekday == int(df.ix[inputday])]
    return(data)

# define the function to plot on the map
def getmap(inputday, pord, data, long1, lat1, long2, lat2):
    fig = plt.figure(figsize =(15, 15))
    lllat = 40.473; urlat = 40.93; lllon = -74.27; urlon = -73.69 # define the boundary of the map
    m = Basemap(projection = 'stere', lon_0 = (urlon + lllon)/2, lat_0 = (urlat +lllat)/2, llcrnrlon = lllon, llcrnrlat = lllat, urcrnrlon = urlon, urcrnrlat = urlat, resolution= 'l')# create the basemap
    m.readshapefile('e:/cusp/datateam/project/taxi_data/desktop/nyczipregion','nyc',drawbounds = True)# indicate the absolute path of the map used       
    pickx, picky = m(data['pickup_longitude'], data['pickup_latitude'])#transfer into basemap positions
    dropx, dropy = m(data['dropoff_longitude'], data['dropoff_latitude'])#transfer into basemap positions
    along = [float(long1), float(long2)]
    alat = [float(lat1), float(lat2)]
    areax = [min(along), max(along), max(along), min(along), min(along)]# the x positions of the boundary
    areay = [min(alat), min(alat), max(alat), max(alat), min(alat)]# the y positions of the boundary
    areaxx, areayy = m(areax, areay)# transfer into basemap x and y positions
    if pord == 'pickup':# check whether it's "pickup" or "dropoff", plot points of the queried one the later in case they are covered
        dropoff, = plt.plot(dropx, dropy, '.', markersize = 2, color= 'b')# plot the points
        pickup, = plt.plot( pickx, picky, '.', markersize = 2,  color = 'r')
        pordx, = plt.plot(areaxx, areayy, '--', color = 'r')# plot the boundary
        plt.legend([pickup, dropoff, pordx],["Pickups","Dropoffs","Pickup Area"], loc = 2)# plot the legend
    if pord == 'dropoff':  
        pickup, = plt.plot( pickx, picky, '.', markersize = 2,  color = 'r')
        dropoff, = plt.plot(dropx, dropy, '.', markersize = 2, color= 'b')
        pordy, = plt.plot(areaxx, areayy, '--', color = 'b') 
        plt.legend([pickup, dropoff, pordy],["Pickups","Dropoffs", "Dropoff Area"], loc = 2)   
    plt.title('NYC Taxi Pickups and Dropoffs'+' On '+ inputday+'day')
    plt.savefig('Taxi.png', dpi=300)

# define the function to get matrix
def getmatrix(data):
    pickupzip = data['pickup_zipcode']
    dropoffzip = data['dropoff_zipcode']
    zipcodes = sorted(list(set(pickupzip).union(set(dropoffzip))))
    zipmatrix = np.zeros((int(len(zipcodes)),int(len(zipcodes))))
    df = pd.DataFrame(zipmatrix, index = zipcodes, columns = zipcodes)
    df.fillna(0, inplace = True)
    
    x = np.array(df['10001':'10001'])
    print x

#    for x in range (0, len(data)):
 #       if frame[pickupzip[x]:dropoffzip[x]] == 0:
  #          frame[pickupzip[x]:dropoffzip[x]] = 1
   #         frame[dropoffzip[x]:pickupzip[x]] = 1
    return(x)


if __name__ == '__main__':
    if len(sys.argv) != 7:# check the length of the input
        print 'Wrong input! The input format should be: python *.py pickup(or dropoff) longitude1 latitude1 longitude2 latitude2 weekday'
        sys.exit()
    stocks_df = pd.read_csv('janjune_data.csv')
    x = getspace(stocks_df, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    if len(x)==0:
        print 'No data found! Please check the longitude and latitude'
        sys.exit()
    data = gettime(x, sys.argv[6], sys.argv[1])
    y = getmatrix(data)
  #  getmap(sys.argv[6], sys.argv[1], x, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
