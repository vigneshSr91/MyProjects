"""
Given 
- Matrix N*M
- Q queries
- Calculate the submatrix sum

Given a matrix of integers A of size N x M and multiple queries Q, 
for each query, find and return the submatrix sum.

Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

Input 1:

 A = [   [1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]   ]
 B = [1, 2]
 C = [1, 2]
 D = [2, 3]
 E = [2, 3]
"""

class Solution:
    def solve(self, A, B, C, D, E):
        pf_sum_of_A = self.calculate_prefix_sum_for_A(A)
        len_of_queries = len(B)
        result = []
        for i in range(len_of_queries):
            if C[i]-1 <= 0 or B[i]-1 <= 0:
                top_left_value = 0
                bottom_left_value = 0
            else:
                top_left_value = pf_sum_of_A[B[i]-2][C[i]-2]
            if C[i]-1 <= 0:
                bottom_left_value = 0
            else:
                bottom_left_value = pf_sum_of_A[D[i]-1][C[i]-2]
            if B[i]-1 <= 0:
                top_right_value = 0
            else:
                top_right_value = pf_sum_of_A[B[i]-2][E[i]-1]
            
            bottom_right_value = pf_sum_of_A[D[i]-1][E[i]-1]
            
            result.append( bottom_right_value - top_right_value - bottom_left_value + top_left_value )

        return result

    
    def calculate_prefix_sum_for_A(self, A):
        pf_sum_of_A = A.copy()
        # first calculate pf sum for each row - that is sum col 1 till m for each row
        for i in range(len(A)):
            for j in range(len(A[i])):
                if j == 0: # the first element has the same value for each row
                    continue
                pf_sum_of_A[i][j] = pf_sum_of_A[i][j-1] + A[i][j]

        # likewise do the same for each column - that is sum each row from 1 till n for each col
        for j in range(len(A[0])):
            for i in range(len(A)):
                if i == 0:
                    continue
                pf_sum_of_A[i][j] = pf_sum_of_A[i-1][j] + A[i][j]
        
        return pf_sum_of_A


