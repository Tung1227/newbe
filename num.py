import numpy as np

def findB(x,y):
    transposeX1 = np.matrix.transpose(x)  
    xTx= transposeX1.dot(x)
    B = (((np.linalg.inv(xTx)).dot(transposeX1)).dot(y))
    return B
def GradientDissent(X, Y, theta, alpha, num_iters):
    m = np.size(Y)
    hx = np.matmul(X, theta)
    c1 = Cost(theta, X, Y)
    for i in range(0, num_iters):
        temp = (alpha / m) * np.matmul(X.T, (hx - Y))
        c2 = Cost(theta - temp, X, Y)
 
        if c1 > c2:
            c1 = c2
            theta = theta - temp
        #print (c1, c2, theta)
    return theta

def computecost(x,y,theta):
    a = 1/(2*m)
    b = np.sum(((x@theta)-y)**2)
    j = (a)*(b)
    return j

if __name__ == "__main__":
    X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
    Y = np.array([[15],[32],[66],[45],[90],[153],[170],[200]])
    m = Y.size
    t = X
    X = np.hstack((np.matrix(np.ones(m).reshape(m, 1)), t))

    theta = np.matrix(np.ones(2).reshape(2, 1))
    theta = GradientDissent(X, Y, theta, 0.000001, 100)
    Cost(theta, X, Y)
    print(theta)
    
    print(Cost(theta, X, Y))