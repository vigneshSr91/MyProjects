"""
Max Sum Without Adjacent Elements

Problem Description

Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

Note: You can choose more than 2 numbers.



Problem Constraints

1 <= N <= 20000
1 <= A[i] <= 2000



Input Format

The first and the only argument of input contains a 2d matrix, A.



Output Format

Return an integer, representing the maximum possible sum.



Example Input

Input 1:

 A = [   
        [1]
        [2]    
     ]
Input 2:

 A = [   
        [1, 2, 3, 4]
        [2, 3, 4, 5]    
     ]

"""
import math
class Solution:
    def adjacent(self, A):
        self.dp = [-math.inf] * len(A)
        self.maxsum(A, len(A)-1)
        return self.dp[len(A)-1]
    def maxsum(self, A, i):
        if i < 0:
            return
        if self.dp[i] != -math.inf:
            return self.dp[i]
        
        self.dp[i] = A[i] + max(self.maxsum(A, i-1), self.maxsum(A, i-2))

