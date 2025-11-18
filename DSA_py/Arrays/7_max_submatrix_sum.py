"""
Problem Description

Given a row-wise and column-wise sorted matrix A of size N * M.
Return the maximum non-empty submatrix sum of this matrix.

Example Input

Input 1:-
    -5 -4 -3
A = -1  2  3
     2  2  4


    -12  -7  -3
     4  5   3
     8  6   4

    0    -4  -4
    12   11   7
    8    6    4

Example Output

Output 1:-
12
"""
    
import numpy as np

class Solution:
    def solve(self, A):
        return np.array(self.calculate_pfsum(A)).maximum
    def calculate_pfsum(self, A):
        reverse_pfsum_of_A = A.copy()
        for i in range(len(A)-1,-1,-1):
            for j in range(len(A[i])-1,-1,-1):
                if j == len(A)-1: # last element in the row
                    reverse_pfsum_of_A[i][j] = A[i][j]
                else:
                    reverse_pfsum_of_A[i][j] = A[i][j] + reverse_pfsum_of_A[i][j+1]
        
        for j in range(len(A[0])-1,-1,-1):
            for i in range(len(A)-1,-1,-1): 
                if i < len(A)-1: # do nothing for the last row elements
                    reverse_pfsum_of_A[i][j] += reverse_pfsum_of_A[i+1][j]
        
        return reverse_pfsum_of_A
    

if __name__ == '__main__':
    A = [   [-5,    -4,     -3],
            [-1,    2,      3],
            [2,     2,      4] ]
    print(Solution().solve(A))


