import pandas as pd
import numpy as np
import random
from random import seed
import math
from scipy.sparse.linalg import eigsh
import pandas as pd
import numpy as np
from scipy.cluster.vq import vq, kmeans2, whiten
from sklearn.metrics import *
    
    
def silh ( data,target ):
    s = silhouette_score(data, target, metric='euclidean')
    print 'Silhouette score: '+str(s)
    return s

if __name__ == '__main__':
    data = pd.read_csv('janjune_data.csv')
    id = data['taxi_id']
    taxi = set(id)
    np.save('taxiid', list(taxi))
    pickup = data['pickup_zipcode']
    dropoff = data['dropoff_zipcode']
    zipcodes = sorted(list(set(pickup).union(set(dropoff))))
    np.save('zips', zipcodes)
    for x in taxi:
        mm = data[data['taxi_id']==x]
        pickupzip = np.array(mm)[:, 18]
        dropoffzip = np.array(mm)[:, 19]
        matrix = np.zeros((len(zipcodes), len(zipcodes)))
        tripframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes)
        for y in range(0, len(mm)):
            tripframe.ix[[pickupzip[y]],[dropoffzip[y]]] += 1
        tripframe = tripframe/(sum(np.array(tripframe.sum())))
        last = (np.array(tripframe)).flatten()
        np.save(str(x), last)


    seed(273827354)
    ta = np.load('taxiid.npy')
    rlist = random.sample(ta, 100)
    rlist = sorted(rlist)
    matrix = np.zeros((len(ta), len(ta)))
    tripframe = pd.DataFrame(matrix, index = ta, columns = ta)
    nn = 0
    for x in rlist:
        for y in ta:
            if x > y:
                xx = np.load(str(x)+'.npy')
                yy = np.load(str(y)+'.npy')
                value = math.exp(-np.dot( (xx-yy).T,(xx-yy))/1)
                tripframe.ix[[x], [y]] = value
                tripframe.ix[[y], [x]] = value
                nn = nn+1
    np.save('tripf', tripframe)
    matrix = np.load('tripf.npy')
    matrix = np.array(matrix)
    a = float(nn)*2/(len(ta)*(len(ta)-1))
    print a
    ght = [a for i in range(0, len(ta))]
    np.fill_diagonal(matrix, ght )
    matrix = np.array(matrix)
    np.save('matrix', matrix)
    np.save('num', a)
    
    k = 5
    weight = matrix.sum(axis = 1)
    dmatrix = np.zeros((len(ta) ,len(ta)))
    np.fill_diagonal(dmatrix, weight)
    lmatrix = dmatrix - matrix
    le_vals, le_vecs = eigsh(lmatrix, 10 , which = 'SM')
    lwrit = le_vecs[:, :5]
    lcenter , llabel = kmeans2(lwrit, k, iter = 100, minit ='random' )
    np.save('cluster', llabel)
    ta = np.array(ta)
    llabel = np.array(llabel)
    label0 = ta[llabel==0]
    label1 = ta[llabel==1]
    label2 = ta[llabel==2]
    label3 = ta[llabel==3]
    label4 = ta[llabel==4]
    lst = [len(label0), float(sum(label0))/len(label0),len(label1), float(sum(label1))/len(label1),len(label2), float(sum(label2))/len(label2), len(label3), float(sum(label3))/len(label3), len(label4), float(sum(label4))/len(label4)]
    np.save('result', lst)

        return s
    k = 5
    le_vecs = np.load('vectors.npy')
    lwrit = le_vecs[:, :5]
    lcenter , llabel = kmeans2(lwrit, k, iter = 100, minit ='random' )
    np.save('cluster1', llabel)
    ta = np.load('taxiid.npy')
    ta = np.array(ta)
    llabel = np.array(llabel)
    label0 = ta[llabel==0]
    label1 = ta[llabel==1]
    label2 = ta[llabel==2]
    label3 = ta[llabel==3]
    label4 = ta[llabel==4]
    lst = [len(label0), float(sum(label0))/len(label0),len(label1), float(sum(label1))/len(label1),len(label2), float(sum(label2))/len(label2), len(label3), float(sum(label3))/len(label3), len(label4), float(sum(label4))/len(label4)]
    np.save('result1', lst)
    print lst
##    lengh = np.load('zips.npy')
#    bigmatrix = np.zeros((len(ta) ,len(lengh)**2))
#    frame = pd.DataFrame(bigmatrix, index = ta)
#    for x in range(0, len(ta)):
#        bb = np.load(str(ta[x])+'.npy')
#        frame.loc[ta[x], :] = bb
#    frame = np.array(frame)
#    np.save('last', frame)
#    silh( frame , llabel)
