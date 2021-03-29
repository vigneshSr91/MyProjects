"""
"""
# Given a String separated by space, reshape it to a 3 * 3 Numpy Array
"""
import numpy

def ShapeArr( l1 ):
    array = numpy.array(l1)
    return(numpy.reshape(array,(3,3)))

if(__name__=='__main__'):
    lst = list(map(int,input( ).split(' ')))
    print(ShapeArr(lst))
"""
"""
"""
# Numpy eye
"""
import numpy as np

if(__name__=='__main__'):
    n,m = map(int,input().split(' '))
    np.set_printoptions(legacy='1.13')
    print( np.eye(n,m,k=0) )
"""
import numpy
if(__name__ == '__main__'):

    n = int(input())
    list1 = []
    for i in range(n):
        list_temp = []
        list_temp = map(int, input().split(' '))
        list1.append([int(i) for i in list_temp])

    list2 = []
    for i in range(n):
        list_temp = []
        list_temp = map(int, input().split(' '))
        list2.append([int(i) for i in list_temp])

    print(numpy.dot(numpy.array(list1), numpy.array(list2)))
