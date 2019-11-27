import matplotlib.pyplot as plt
import pandas as pd
#import numpy.linalg as np
import numpy as np1
#from scipy.stats.stats import pearsonr

def kernel(point,xmat,k):
    m,n=np1.shape(xmat)
    weights=np1.mat(np1.eye((m)))
    for j in range(m):
        diff=point-x[j]
        weights[j,j]=np1.exp(diff*diff.T/(-2.0*k**2))
    return weights
def localweight(point,xmat,ymat,k):
    wei=kernel(point,xmat,k)
    w=(x.T*(wei*x)).I*(x.T*(wei*ymat.T))
    return w
def localweightregression(xmat,ymat,k):
    m,n=np1.shape(xmat)
    ypred=np1.zeros(m)
    for i in range(m):
        ypred[i]=xmat[i]*localweight(xmat[i],xmat,ymat,k)
    return ypred
data=pd.read_csv('10data.csv')
bill=np1.array(data.total_bill)
tip=np1.array(data.tip)
mbill=np1.mat(bill)
mtip=np1.mat(tip)
m=np1.shape(mbill)[1]
one=np1.mat(np1.ones(m))
x=np1.hstack((one.T,mbill.T))
ypred=localweightregression(x,mtip,2)
sortindex=x[:,1].argsort(0)
xsort=x[sortindex][:,0]
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(bill,tip,color='green')
ax.plot(xsort[:,1],ypred[sortindex],color='red',linewidth=3)
plt.xlabel('total bill')
plt.ylabel('tip')
