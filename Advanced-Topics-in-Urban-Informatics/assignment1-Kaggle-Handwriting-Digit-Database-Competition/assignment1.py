#ent 1, Urban Informatics
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import neighbors
from sklearn.svm import SVC
import operator
import numpy as np
from scipy.misc import imrotate
from scipy.ndimage import convolve




def nudge_dataset(X, Y):
    """
    This produces a dataset 5 times bigger than the original one,
    by moving the 28x28 images in X around by 1px to left, right, down, up
    """
    direction_vectors = [
        [[0, 1, 0],
         [0, 0, 0],
         [0, 0, 0]],

        [[0, 0, 0],
         [1, 0, 0],
         [0, 0, 0]],

        [[0, 0, 0],
         [0, 0, 1],
         [0, 0, 0]],

        [[0, 0, 0],
         [0, 0, 0],
         [0, 1, 0]],

        [[1, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],

        [[0, 0, 0],
         [0, 0, 0],
         [1, 0, 0]],

        [[0, 0, 1],
         [0, 0, 0],
         [0, 0, 0]],

        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 1]],

]

    shift = lambda x, w: convolve(x.reshape((28, 28)), mode='constant',
                                  weights=w).ravel()
    X = np.concatenate([X] +
                       [np.apply_along_axis(shift, 1, X, vector)
                        for vector in direction_vectors])
    Y = np.concatenate([Y for _ in range(9)], axis=0)
    return X, Y

def rotate_dataset(X, Y):
    """
    This produces a dataset 2 times bigger than the original one,
    by rptating the 28x28 images in 10 degrees clockwise and counter clockwise
    """
    angles = [-30,-20,-10,10, 20,30]

    
    rotate = lambda x, w: imrotate(x.reshape((28, 28)), w).ravel()
    X = np.concatenate([X] +
                       [np.apply_along_axis(rotate, 1, X, angle)
                        for angle in angles])
    Y = np.concatenate([Y for _ in range(7)], axis=0)
    return X, Y


# Averaging Images
def average(data):
    newdata = data.groupby('label').mean()
    fig, axes = plt.subplots(1, 1, sharex= True, sharey= True)
    a = 0
    
    for i in range(1,2):
        for j in range(0,1):
            mm = np.array(newdata.ix[9+j])
            xx = mm.reshape((28, 28))
            plt.imshow(xx, cmap= plt.cm.gray_r, extent = [0,28,0,28], aspect = 'auto')
            plt.gca().get_xaxis().set_visible(False)
            plt.gca().get_yaxis().set_visible(False)
            for spine in ['top','right','left','bottom']:
                plt.gca().spines[spine].set_visible(False)
    ###        plt.show()
            plt.savefig('B9.png')
        a = 5
    plt.subplots_adjust(wspace=0, hspace=0)
 #   plt.show()
    plt.clf()

# Random Forest
def rf(target, train, test):
    ranfor = RandomForestClassifier(n_estimators=500)
    ranfor.fit(train, target)
    print 'Predicting'
    predictpro = ranfor.predict_proba(test)
    predict = ranfor.predict(test)
    bestpro = predictpro.max(axis =1)
    return predict, bestpro, predictpro

# KNN
def kn(target, train, test):
    knn = neighbors.KNeighborsClassifier()
    knn.fit(train, target) 
    predictpro = knn.predict_proba(test)
    print 'Predicting'
    predict = knn.predict(test)
    bestpro = predictpro.max(axis=1)
    return predict, bestpro, predictpro

# SVC
def svcc(target, train, test):
    svcfit = SVC(probability=True)
    svcfit.fit(train, target)
    print 'Predicting'
    predict = svcfit.predict(test)
    predictpro = svcfit.predict_proba(test)
    bestpro = predictpro.max(axis=1)
    return predict, bestpro


if __name__ == '__main__':
    
    traindata = pd.read_csv('train.csv')
    testdata = pd.read_csv('test.csv')
    target = np.array(traindata.ix[:,0])
    train = np.array(traindata.ix[:,1:])
    train = pd.DataFrame(train)
    test = np.array(testdata)
    testar = np.array(testdata.ix[:,0])
    test = pd.DataFrame(np.array(test))

    ntrain,ntarget = rotate_dataset(train,target)
    ntrain,ntarget = nudge_dataset(train,target)
    np.save('ntrain', ntrain)
    np.save('ntarget',ntarget)
    np.save('test', test)
    test = np.load('test.npy')
    ntrain = np.load('ntrain.npy')
    ntarget = np.load('ntarget.npy')
    print 'done one'
#
    rfpredict, rfpro, rfpromatrix = rf(ntarget, ntrain, test)


    output = pd.DataFrame({'ImageId': np.arange(1,len(test)+1),'Label': list(rfpredict)} )
    output.to_csv('final_rf_benchmark.csv', index = False) 


    
  #  f0,f1, f2,f3,f4,f5,f6,f7,f8,f9
  #  average(traindata)
    knnpredict, knnpro, knnpromatrix = kn(ntarget, ntrain, test)



    output = pd.DataFrame({'ImageId': np.arange(1,len(test)+1),'Label': list(knnpredict)} )
    output.to_csv('final_Knn_benchmark.csv', index = False) 


    promatrix = np.array(pd.DataFrame([rfpro, knnpro]).T)
    predictmatrix = np.array(pd.DataFrame([rfpredict, knnpredict]).T)
    firstpredict = predictmatrix[np.arange(len(predictmatrix)), promatrix.argmax(axis=1)]

    output = pd.DataFrame({'ImageId': np.arange(1,len(test)+1),'Label': list(firstpredict)} )
    output.to_csv('final_benchmark.csv', index = False) 

 
