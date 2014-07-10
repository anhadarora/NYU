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
from scipy import linalg as LA
from scipy.cluster.vq import vq, kmeans2, whiten
import Pycluster
#import dbflib
from shapelib import ShapeFile
import dbflib
from  scipy.linalg import sqrtm, inv
from sklearn.preprocessing import normalize
from sklearn import datasets
from sklearn.metrics import *
from matplotlib.collections import LineCollection
from matplotlib import cm
from sklearn import cluster
from scipy.stats import ttest_ind



# define the function to get all the pickups or dropoffs in the defined region
def getspace(p_or_d, long_1, lat_1, long_2, lat_2):#receive the input of "pickup" or "dropoff" and two points which define the boundary
    janjune_data= open('janjune_data.csv','r')
    janjune_con = janjune_data.readlines()
    stocks_df = pd.read_table('janjune_data.csv', sep=',')
    long = []
    lat = []
    record = []
    i =0
    long.append(float(long_1))
    long.append(float(long_2))
    lat.append(float(lat_1))
    lat.append(float(lat_2))
#    if p_or_d == 'pickup':# check whether it's "pickup" or "dropoff"
    x = stocks_df['pickup_latitude']# read pickup latitude column
    y = stocks_df['pickup_longitude']# read pickup longitude column
    z = [0 for i in range (0, len(x))]
    tree = cKDTree(zip(x, z))# build query tree of latitude
    tree1 = cKDTree(zip(y, z))# build query tree of longitude
    long_mid = (float(long_1) + float(long_2))/2
    lat_mid = (float(lat_1) + float(lat_2))/2
    long_r = max(long) - long_mid
    lat_r = max(lat) - lat_mid
    latrange = tree.query_ball_point([lat_mid,0],lat_r)# query point indexes between two given latitudes
    longrange = tree1.query_ball_point([long_mid, 0], long_r) # query point indexes between two given longitudes
    final_index = sorted(list(set(longrange).intersection(set(latrange))))# find the intersection of the two queries
    for i in final_index: # collect the whole records of the points found
        original = janjune_con[i+1].split(',')
        record.append(original[:-1])
#    if p_or_d == 'dropoff':# check whether it's "pickup" or "dropoff"
    x = stocks_df['dropoff_latitude']
    y = stocks_df['dropoff_longitude']
    z = [0 for i in range (0, len(x))]
    tree = cKDTree(zip(x, z))
    tree1 = cKDTree(zip(y, z))
    long_mid = (float(long_1) + float(long_2))/2
    lat_mid = (float(lat_1) + float(lat_2))/2
    long_r = max(long) - long_mid
    lat_r = max(lat) - lat_mid
    latrange = tree.query_ball_point([lat_mid,0],lat_r)
    longrange = tree1.query_ball_point([long_mid, 0], long_r)
    final_index = sorted(list(set(longrange).intersection(set(latrange))))
    for i in final_index:
        original = janjune_con[i+1].split(',')
        record.append(original[:-1])
    janjune_data.close()
    return(record)

# define the function to find out the records on certain day of the week
def gettime(data, inputday, pord):
    class Sortdays: # create a class to store the numbers of the days on certain day of the week
        day  = None
        pdays = None
    
        def  __init__(self, day):
            self.day = day
            self.pdays = []
    
        def addday(self, weekday):
            self.pdays.append(weekday)
    sortdays = {}
    record = []
    weekday = ['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun']
    for x in weekday:
        sortdays[x]= Sortdays(x)
    new_time = time.gmtime(float(data[0][1]))
    a = time.strftime('%Y-%m-%d %H:%M:%S',new_time)
    b = dt.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
    day_number = date.date2num(b)# transfer the time to "number" of days since 0001-01-01 00:00:00 UTC, plus one.
    first_day = int(day_number)
    for x in range(0, 52):# store all the "number"s of certain days of the weeks in 2011 using class defined
        sortdays['Satur'].addday(first_day)
        sortdays['Sun'].addday(first_day + 1)
        sortdays['Mon'].addday(first_day + 2)
        sortdays['Tues'].addday(first_day + 3)
        sortdays['Wednes'].addday(first_day + 4)
        sortdays['Thurs'].addday(first_day + 5)
        sortdays['Fri'].addday(first_day + 6)
        first_day += 7 
    if inputday not in sortdays.keys():
        print 'Wrong weekday! Please enter Mon, Tues, Wednes, Thurs, Fri, Satur or Sun as the weekday'
        sys.exit()
    if pord == 'pickup':# check whether it's "pickup" or "dropoff"
        for x in range(0, len(data)):
            new_time = time.gmtime(float(data[x][1]))
            a = time.strftime('%Y-%m-%d %H:%M:%S',new_time)
            b = dt.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
            day_number = date.date2num(b)# get the "number" of each record
            first_day = int(day_number)
            if first_day in sortdays[inputday].pdays:# check whether the "number" is in the list of input day of the week
                record.append(data[x])
    else:
         for x in range(0, len(data)):
            new_time = time.gmtime(float(data[x][2]))
            a = time.strftime('%Y-%m-%d %H:%M:%S',new_time)
            b = dt.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
            day_number = date.date2num(b)
            first_day = int(day_number)
            if first_day in sortdays[inputday].pdays:
                record.append(data[x])
    return(record)

# define the function to plot on the map
def getmap(inputday, pord, data, long1, lat1, long2, lat2):
    fig = plt.figure(figsize =(15, 15))
    lllat = 40.473; urlat = 40.93; lllon = -74.27; urlon = -73.69 # define the boundary of the map
    m = Basemap(projection = 'stere', lon_0 = (urlon + lllon)/2, lat_0 = (urlat +lllat)/2, llcrnrlon = lllon, llcrnrlat = lllat, urcrnrlon = urlon, urcrnrlat = urlat, resolution= 'l')# create the basemap
    m.readshapefile('c:/Users/gang/Desktop/nyczipregion','nyc',drawbounds = True)# indicate the absolute path of the map used
    picklong = []
    picklat = []
    droplong = []
    droplat = []
    for x in data:
        picklong.append(float(x[3]))
        picklat.append(float(x[4]))
        droplong.append(float(x[5]))
        droplat.append(float(x[6]))
        
    pickx, picky = m(picklong, picklat)#transfer into basemap positions
    dropx, dropy = m(droplong, droplat)#transfer into basemap positions

    along = [float(long1), float(long2)]
    alat = [float(lat1), float(lat2)]
    areax = [min(along), max(along), max(along), min(along), min(along)]# the x positions of the boundary
    areay = [min(alat), min(alat), max(alat), max(alat), min(alat)]# the y positions of the boundary
    areaxx, areayy = m(areax, areay)# transfer into basemap x and y positions
 #   if pord == 'pickup':# check whether it's "pickup" or "dropoff", plot points of the queried one the later in case they are covered
  #      dropoff, = plt.plot(dropx, dropy, '.', markersize = 2, color= 'b')# plot the points
   #     pickup, = plt.plot( pickx, picky, '.', markersize = 2,  color = 'r')
    #    pordx, = plt.plot(areaxx, areayy, '--', color = 'r')# plot the boundary
    #    plt.legend([pickup, dropoff],["Pickups","Dropoffs"], loc = 2)# plot the legend
  #  if pord == 'dropoff':  
   #     pickup, = plt.plot( pickx, picky, '.', markersize = 2,  color = 'r')
   #     dropoff, = plt.plot(dropx, dropy, '.', markersize = 2, color= 'b')
    pordy, = plt.plot(areaxx, areayy, '--', color = 'g') 
#        plt.legend([pickup, dropoff, pordy],["Pickups","Dropoffs", "Financial Center"], loc = 2)   
 #   plt.title('NYC Taxi Trips')
    plt.savefig('NYC_ttTaxi.png', dpi=300)
#    plt.show()

# define the function to get matrix
def getmatrix(data1):
    data = np.array(data1)
    pickupzip = data[:,18]
    dropoffzip = data[:,19]
    tip = data[:, 12]
    fare = data[:, 9]
    tip = map(int, tip)
    fare = map(int , fare)
    zipcodes = sorted(list(set(pickupzip).union(set(dropoffzip))))
    zipmatrix = np.zeros((int(len(zipcodes)),int(len(zipcodes))))
    tframe = pd.DataFrame(zipmatrix, index = zipcodes, columns = zipcodes).copy()
    tnframe = pd.DataFrame(zipmatrix, index = zipcodes, columns = zipcodes).copy()
    tipframe = pd.DataFrame(zipmatrix, index = zipcodes, columns = zipcodes).copy()
    fareframe =  pd.DataFrame(zipmatrix, index = zipcodes, columns = zipcodes).copy()
 #   for x in range (0, len(data1)):
  #      if tframe.ix[[pickupzip[x]],[dropoffzip[x]]] == 0:
   #         tframe.ix[[pickupzip[x]],[dropoffzip[x]]] = 1
    #        tframe.ix[[dropoffzip[x]],[pickupzip[x]]] = 1
    for x in range (0, len(data1)):
        tnframe.ix[[pickupzip[x]],[dropoffzip[x]]] += 1
        tnframe.ix[[dropoffzip[x]],[pickupzip[x]]] += 1      
    for x in range (0, len(data1)):
        tipframe.ix[[pickupzip[x]],[dropoffzip[x]]] += tip[x]
        tipframe.ix[[dropoffzip[x]],[pickupzip[x]]] += tip[x]   
 #   for x in range (0, len(data1)):
  #      fareframe.ix[[pickupzip[x]],[dropoffzip[x]]] += fare[x]
   #     fareframe.ix[[dropoffzip[x]],[pickupzip[x]]] += fare[x]  
    tn = tnframe.values
    tip = tipframe.values
    print tn[0], tip[0]
    avtip = np.where(tip>0, tip/tn, tip)
    avtipframe = pd.DataFrame( avtip, index = zipcodes, columns = zipcodes)
    print np.array(avtipframe)[0]
 #   fare = np.array(fareframe)
 #   avfare = np.where(fare>0, fare/tn, 0)
  #  avfareframe = pd.DataFrame( avfare, index = zipcodes, columns = zipcodes)
    return(tframe,tnframe , avtipframe ,  zipcodes)


def clustering(tripmatrix):
    k = 4
    trip1matrix = tripmatrix.copy()
    weight = tripmatrix.sum(axis = 1)
    a = int(len(weight))
    dmatrix = np.zeros((a ,a))
    np.fill_diagonal(dmatrix, weight)
    ddmatrix = np.zeros((a ,a))
    ght = [0 for i in range(0, a)]
    np.fill_diagonal(trip1matrix, ght )
    wweight = trip1matrix.sum(axis = 1)
    np.fill_diagonal(ddmatrix, weight)

    hdmatrix = sqrtm(ddmatrix)
    hdmatrix = inv(hdmatrix)
    ulmatrix = np.dot(hdmatrix, trip1matrix)
    ulmatrix = np.dot(ulmatrix, hdmatrix)
    le_vals, le_vecs = LA.eig(ulmatrix)
    lwrit = le_vecs[:, :4]
    lwrit = normalize(lwrit, norm='l1', axis=1)
  #  print lwrit
    lcenter , llabel = kmeans2(lwrit, k, iter = 20, minit ='random' )
   # print llabel


    lmatrix = dmatrix - tripmatrix
    e_vals, e_vecs = LA.eig(lmatrix)
    writ = e_vecs[:, :4]
    center , label = kmeans2(writ, k, iter = 20, minit ='random')
 #   print label
#    la, er, nfoun = Pycluster.kcluster(writ , 3)
    spectral = cluster.SpectralClustering(n_clusters = 4, eigen_solver = 'arpack', affinity = 'precomputed')
    spectral.fit(tripmatrix)
    spectralpredict = spectral.fit_predict(tripmatrix)
    
 #   print spectralpredict
    print llabel
    print label
    print spectralpredict
    return(label,spectralpredict ,llabel,k)

def plotclustering(label, zipcodes, nameee):
#    print len(zipcodes)
    label = np.array(label)
    zipcodes = np.array(zipcodes)
    cluster1 = zipcodes[label == 1]
    cluster2 = zipcodes[label == 2]
    cluster0 = zipcodes[label == 0]
    cluster3 = zipcodes[label == 3]

    fig = plt.figure(figsize =(15, 15))
    ax = plt.subplot(111)
    lllat = 40.473; urlat = 40.93; lllon = -74.27; urlon = -73.69 # define the boundary of the map
    m = Basemap(ax=ax, projection = 'stere', lon_0 = (urlon + lllon)/2, lat_0 = (urlat +lllat)/2, llcrnrlon = lllon, llcrnrlat = lllat, urcrnrlon = urlon, urcrnrlat = urlat, resolution= 'l')# create the basemap 

  #  m.drawcoastlines()
    m.drawcountries()
    shp = ShapeFile('c:/Users/gang/Desktop/nyczipregion')
    dbf = dbflib.open('c:/Users/gang/Desktop/nyczipregion')
    for npoly in range(shp.info()[0]):
        shpsegs = []
        shp_object = shp.read_object(npoly)
        verts = shp_object.vertices()
        rings = len(verts)
        for ring in range(rings):
            lons , lats = zip(*verts[ring])
            x, y = m(lons, lats)
            shpsegs.append(zip(x, y))
            if ring ==0:
                shapedict = dbf.read_record(npoly)
            name = shapedict['Zcta5ce00']
        
        lines = LineCollection(shpsegs, antialiaseds=(1,))
        if name in cluster0:
            lines.set_facecolors('b')
        if name in cluster1:
            lines.set_facecolors('g')
        if name in cluster2:
            lines.set_facecolors('r')
        if name in cluster3:
            lines.set_facecolors('y')
        lines.set_alpha(1)
        lines.set_edgecolors('k')
        ax.add_collection(lines)
    plt.title('Box Clustering Based On Taxi Trips')
    plt.savefig(nameee+'_box_trip_Clustering.png', dpi=300)
    plt.show()   



def average(matrix,label, zipcodes, number, name):
    frame = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes)
    frame1 = frame.copy()
    frame1[frame1 >= 0] = 0
    zipcodes = np.array(zipcodes)
    label = np.array(label)
    label0 = zipcodes[label==0]
    label1 = zipcodes[label==1]
    label2 = zipcodes[label==2]
    label0list = []
    label1list = []
    label2list = []
    label00list = []
    label11list = []
    label22list = []
    l1list = []
    l2list = []
    l0list = []
    
    for x in range(0, len(label0)):
        for y in range(0, len(label0)):
            if frame.ix[[label0[x]],[label0[y]]].values!=0:
                label0list.append(float(np.array(frame.ix[[label0[x]],[label0[y]]])))
                frame1.ix[[label0[x]],[label0[y]]]= 300
    label0ave =  np.array(label0list).sum()/len(label0list)
    for x in range(0, len(label1)):
        for y in range(0, len(label1)):
            if frame.ix[[label1[x]],[label1[y]]].values!=0:
                label1list.append(float(np.array(frame.ix[[label1[x]],[label1[y]]])))
                frame1.ix[[label1[x]],[label1[y]]]= 200
    label1ave =  np.array(label1list).sum()/len(label1list)
    for x in range(0, len(label2)):
        for y in range(0, len(label2)):
            if frame.ix[[label2[x]],[label2[y]]].values!=0:
                label2list.append(float(np.array(frame.ix[[label2[x]],[label2[y]]])))
                frame1.ix[[label2[x]],[label2[y]]]= 100
    label2ave =  np.array(label2list).sum()/len(label2list)   
    plt.imshow(np.array(frame1), cmap=plt.cm.hot_r, extent = [0,len(frame1),0,len(frame1)], aspect = 'auto',interpolation='nearest')
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    plt.savefig(name+'_box_trip_matrix.png', dpi=300)
    plt.show() 
    
    for x in range(0, len(label0)):
        label000list = list(frame[label0[x]][frame[label0[x]]>0].values)
        label000list = np.array(label000list)
        label00list += list(label000list)
    for x in range(0, len(label1)):
        label111list = list(frame[label1[x]][frame[label1[x]]>0].values)
        label111list = np.array(label111list)
        label11list += list(label111list)
    for x in range(0, len(label2)):
        label222list = list(frame[label2[x]][frame[label2[x]]>0].values)
        label222list = np.array(label222list)
        label22list += list(label222list)


    for x in range(0, len(label0)):
        label000list = list(frame[label0[x]].values)
        label000list = np.array(label000list)
        l0list += list(label000list)
    for x in range(0, len(label1)):
        label111list = list(frame[label1[x]].values)
        label111list = np.array(label111list)
        l1list += list(label111list)
    for x in range(0, len(label2)):
        label222list = list(frame[label2[x]].values)
        label222list = np.array(label222list)
        l2list += list(label222list)





        
    return(label0list, label1list, label2list, label00list, label11list, label22list, l0list, l1list, l2list)

def median(s):
    i = len(s)
    if not i%2:
        return (s[(i/2)-1]+s[i/2])/2.0
    return s[i/2]


def static(l1, l2, l3):
    ll1 = len(l1)
    ll2 = len(l2)
    ll3 = len(l3)
    if ll1>0:
        l1ave = float((np.array(l1)).sum())/len(l1)
    else:
        l1ave = 'nan'
    if ll2>0:
        l2ave = float((np.array(l2)).sum())/len(l2)
    else:
        l2ave = 'nan'
    if ll3 >0:
        l3ave = float((np.array(l3)).sum())/len(l3)
    else:
        l3ave = 'nan'
    print 'Connections in the clusters: ' ,len(l1), len(l2), len(l3)
    print 'Average: ', l1ave, l2ave, l3ave
    if ll1 >0:
        l1mean = (max(l1)+min(l1))/float(2)
    else:
        l1mean = 'nan'
    if ll2 > 0:
        l2mean = (max(l2)+min(l2))/float(2)
    else:
        l2mean = 'nan'
    if len(l3)>0:
        l3mean = (max(l3)+min(l3))/float(2)
    else:
        l3mean = 'nan'
    print 'Mean : ', l1mean,l2mean, l3mean
    if ll1 >0:
        l1median = median(l1)
    else:
        l1median = 'nan'
    if ll2 >0:
        l2median = median(l2)
    else:
        l2median = 'nan'
    if len(l3)>0:
        l3median = median(l3)
    else:
        l3median = 'nan'
    print 'Median : ', l1median, l2median, l3median
    l1std = np.std(np.array(l1))
    l2std = np.std(np.array(l2))
    l3std = np.std(np.array(l3))
    print 'Standard deviation :', l1std, l2std, l3std
    if ll1>0 and ll2 >0:
        t12 = ttest_ind(l1, l2)
    else:
        t12 = ['nan', 'nan']
    if len(l3)>0 and ll1>0:
        t13 = ttest_ind(l1, l3)
    else:
        t13 = ['nan','nan']
    if len(l3)>0 and ll2>0:
        t23 = ttest_ind(l2, l3)
    else:
        t23 = ['nan','nan']
    print 'T-test Clusters 1 and 2, 1 and 3, 2 and 3 P-values:'
    print t12[1], t13[1], t23[1]


def silh ( data,target ):
    s = silhouette_score(data, target, metric='precomputed')
    print 'Silhouette score: '+str(s)











#if len(sys.argv) != 7:# check the length of the input
 #   print 'Wrong input! The input format should be: python *.py pickup(or dropoff) longitude1 latitude1 longitude2 latitude2 weekday'
  #  sys.exit()
#data = getspace(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
#if len(x)==0:
 #   print 'No data found! Please check the longitude and latitude'
  #  sys.exit()
#data = gettime(x, sys.argv[6], sys.argv[1])
#data = np.load('boxdata.npy')
#y, z , m, l = getmatrix(data)
#np.save('boxtripmatrix', z)
#np.save('boxzipcodes', l)
#np.save('boxtips',m)
#np.save('boxdata', data)
z = np.load('boxtripmatrix.npy')
l = np.load('boxzipcodes.npy')
#m = np.load('boxtips.npy')
data = np.load('boxdata.npy')
#plt.imshow(np.array(y), cmap= plt.cm.gray_r, extent = [0,len(data),0,len(data)], aspect = 'auto',interpolation='nearest')
#plt.title('NYC Taxi Trips Binary Matrix')
#plt.gca().get_xaxis().set_visible(False)
#plt.gca().get_yaxis().set_visible(False)
#plt.savefig('NYC_BM.png',dpi = 300)
#plt.imshow(np.array(m), cmap= plt.cm.gray_r, extent = [0,len(l),0,len(l)], aspect = 'auto',interpolation='nearest')
#plt.colorbar()
#plt.title('NYC Financial Center Taxi Tips Weighted Matrix')
#plt.gca().get_xaxis().set_visible(False)
#plt.gca().get_yaxis().set_visible(False)
#plt.savefig('Box_WM.png',dpi = 300)

#getmap(sys.argv[6], sys.argv[1], data, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
#unl,sc ,nl,k = clustering(z)
#np.save('nycluster1', unl)
#np.save('nycluster2', sc)
#np.save('nycluster3', nl)
unl = np.load('nycluster1.npy')
sc = np.load('nycluster2.npy')
nl = np.load('nycluster3.npy')
l11, l12, l13, l14, l15, l16, l17, l18, l19 = average(z, unl, l, 3, 'Unl')
l21, l22, l23, l24, l25, l26, l27,l28, l29 = average(z, sc, l, 3, 'Sc')
l31, l32, l33, l34, l35, l36, l37, l38, l39 = average(z, nl, l, 3, 'Nor')
plotclustering(unl, l, 'Unl')
plotclustering(sc, l, 'Sc')
plotclustering(nl, l, 'Nor')
print '\n'+'Unnormalized CLustering:'
print'\n'+'Only have connections in the clusters:'
static(l11, l12, l13)
print '\n'+'Trips > 0:'
static(l14, l15, l16)
print '\n'+ 'All the values:'
static(l17, l18, l19)
score1  = silh(z , unl)
print '\n'+ 'Spectral Clustering Package:'
print'\n'+'Only have connections in the clusters:'
static(l21, l22, l23)
print '\n'+'Trips > 0:'
static(l24, l25, l26)
print '\n'+ 'All the values:'
static(l27, l28, l29)
score2 = silh(z, sc)
print '\n'+ 'Normalized Spectral Clustering Package:'
print'\n'+'Only have connections in the clusters:'
static(l31, l32, l33)
print '\n'+'Trips > 0:'
static(l34, l35, l36)
print '\n'+ 'All the values:'
static(l37, l38, l39)
score3 = silh(z, nl)
