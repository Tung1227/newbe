import numpy as np
import math
import matplotlib as plt


def predict(x,interM,interB):
    return  interM* x - interB


if __name__ == "__main__":
    x = np.array([1,2,3,4,5,6,7,8])
    y = np.array([15,32,66,45,90,153,170,200])

    print("X*Y")
    print(x*y)

    m = (len(x) * np.sum(x*y) - np.sum(x) * np.sum(y))/(len(x) * np.sum(x*x) - np.sum(x) ** 2)
    b = (np .sum(y) - m * np.sum(x))/len(x)

    print(m) 
    print(b)

    _,interM = math.modf(m)
    _,interB = math.modf(b)

    print(interM)
    print(interB)
    
    vec = np.arange(10)
    print(vec)

    result = predict(vec,interM,interB) 
    print(result)   