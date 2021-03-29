"""
You are given a 2-D array with dimensions N * M.
Your task is to perform the min function over axis  and then find the max of that.
"""

import numpy as np

def ShapeArr( l1, m, n ):
    array = np.array(l1)
    return(np.reshape(array,(m,n)))

def findMin(arr):
    return np.min(arr, axis=1)

if(__name__=='__main__'):
    m,n = map(int,input().split(' '))
    lst=[]
    for i in range(m):
        temp_list = input().split(' ')
        lst.append([int(i) for i in temp_list])

    arr = ShapeArr( lst, m, n )
    lst_min = findMin(arr)

    arr = np.array(lst_min)
    print(np.max(arr))