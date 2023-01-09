"""
Return binary

Given a Numpy array of integers as an input to the function binary(), complete the given function to convert each element in the array into its binary representation.

For example: In binary, 5 => 101, 7 => 111, 10 => 1010.

Note: You are not allowed to use the inbuilt bin() function and both input and output array have elements of datatype 'int'.

Input Format:

A list is taken as input which is then typecasted to a NumPy array.
Output Format:

A NumPy array is printed.
Sample Input:

[[2,3,4], [5,6,7]]
Sample Output:

[[ 10  11 100]
 [101 110 111]]  
Note: You can use vectorize() function of NumPy to solve this question.


"""

import numpy as np


def decToBinary(n):
     
    # array to store
    # binary number
    binaryNum = [0] * n;
 
    # counter for binary array
    i = 0;
    while (n > 0):
 
        # storing remainder
        # in binary array
        binaryNum[i] = n % 2;
        n = int(n / 2);
        i += 1;
 
    # printing binary array
    # in reverse order
    temp=""
    for j in range(i - 1, -1, -1):
        temp += str(binaryNum[j])
    return int(temp)
    

def binary(arr):
    """
        arr is a NumPy array 
        return output array consisting of binary representation of each element
    """
    #YOUR CODE GOES HERE
    
    vfunc = np.vectorize(decToBinary)
    return vfunc(arr)


if __name__ == "__main__":
    print(binary([[2,3,4], [5,6,7]]))