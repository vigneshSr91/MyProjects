"""
You are given two integer arrays of size N * P and M * P (N & M are rows, and P is the column). 
The task is to concatenate the arrays along axis 0 ( rows ) 
"""
import numpy as np

if(__name__=='__main__'):
    n,m,p = map(int,input().split(' '))
    list_nxp = []
    for i in range(n):
        list_tmp = input( ).split(' ')
        if(len(list_tmp) > p ):
            print('Error')
            break
        list_nxp.append([int(i) for i in list_tmp])

    list_mxp = []
    for i in range(m):
        list_tmp = input().split(' ')
        if(len(list_tmp) > p ):
            print('Error')
            break
        list_mxp.append([int(i) for i in list_tmp])

    arr1 = np.array(list_nxp)
    arr2 = np.array(list_mxp)

    print(np.concatenate((arr1,arr2),axis=0))