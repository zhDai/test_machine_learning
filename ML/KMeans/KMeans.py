# _*_ coding:utf-8 _*_
#一般KMeans方法
import numpy as np
from numpy import *
import sys
from pylab import *

#open model
def openfile(file):
    file_1=open(file)
    data=[]
    for eachline in file_1.readlines():
        eachline_1=eachline.strip().split('\t')
        data.append(map(float,eachline_1))
    return array(data)

#choose the kth initial point
def choose_initil_point(k,data_1):
    if k >10:
        print 'exist number!(k<=10)'
        sys.exit()
    dataset=[]
    i=0
    while i<k:
        a=np.random.randint(0,len(data_1)-1)
        if a not in dataset:
            dataset.append(a)
            i=i+1
        else:
            continue
    #return dataset
    data_amount=data_1
    data_poly=[]
    for i in range(len(dataset)):
        data_poly.append(data_amount[dataset[i]])
    return array(data_poly)    
    
#cmpute the distannce between ploy point and other point
#data_1 is point amount
#data_2 is poly amount
def k_means(data_1,data_2):
    clusterAssment=np.zeros((len(data_1),2))  
    for i in range(len(data_1)):
        dist=np.inf
        min_index=-1
        for j in range(len(data_2)):
            dist_1=data_1[i]-data_2[j]
            distance=sqrt((dist_1[0])**2+(dist_1[1])**2)
            if distance<dist:
                dist=distance
                min_index=j
        clusterAssment[i,:]=min_index,dist
    
    for i in range(len(data_2)):
        x=[];y=[]
        for j in range(len(data_1)):
            if clusterAssment[j,0]==i:
                x.append(data_1[j][0])
                y.append(data_1[j][1])
        x_1=mean(x)
        y_1=mean(y)
        data_2[i]=[x_1,y_1]
    return clusterAssment, data_2

def hua_tu(amout,amout_1):
    x=[];y=[]
    x_1=[];y_1=[]
    for i in range(len(amout)):
        x.append(amout[i][0])
        y.append(amout[i][1])
    for j in range(len(amout_1)):
        x_1.append(amout_1[j][0])
        y_1.append(amout_1[j][1])
    plot(x,y,'r.',x_1,y_1,'go')
    show()

if __name__ == "__main__":
#     k=input("k：")
    k = 4
    data_1=openfile('Kmean_test.txt')
    data_2=choose_initil_point(k, data_1)
    #initial value
    print "choose_initil_point",data_2
    sum_err=0
    err=0
    while err<0.0000001:
        [outcomes,poly_point]=k_means(data_1, data_2)
        sum_err_1=sum(outcomes[:,1])
        err=sum_err_1-sum_err
        sum_err=sum_err_1
    
    #the last value of poly_point
    print "poly_point:",poly_point
    print "sum_err:",sum_err
    
    hua_tu(data_1,poly_point)

    

     

        

            


            
            
        
    
    

    
    

        


