import math 
import numpy as np
def power(a,b):
    if(b==1):
        return a
    if(b%2==0):
        tmp = power(a, b/2)
        return  matrixMultiply(tmp, tmp)
    if(b%2>0):
        tmp = power(a, math.floor(b/2))
        return matrixMultiply( a, matrixMultiply(tmp, tmp) )

def matrixMultiply(arr1, arr2):
    return np.dot(arr1, arr2)

if(__name__ == '__main__'):
    A = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    arr = np.array(A)
    print(power(arr, 100))