import numpy as np
import math


def predict(x,interM,interB):
    return  interM* x - interB
def findB(x,y):
    transposeX1 = np.matrix.transpose(x1)  
    xTx= transposeX1.dot(x1)
    B = (((np.linalg.inv(xTx)).dot(transposeX1)).dot(y))
    return B
def GradientDescent():
    for i in range(1,100):

        W0 = 
def Cost(Beta, X, Y):
    m = Y.size
    hx = np.matmul(X, Beta)
    return np.sum(np.power(np.subtract(hx, Y), 2)) / (2 * m)
if __name__ == "__main__":
    x = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
    y = np.array([15,32,66,45,90,153,170,200])
    ones = np.ones(x.shape)
    x1 = np.append(ones,x,1)
    B = findB(x,y)
    print(B)
    