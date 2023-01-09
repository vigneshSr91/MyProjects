"""
Unique Paths

Problem Description
Given a matrix of integers A of size N x M . There are 4 types of squares in it:

1. 1 represents the starting square.  There is exactly one starting square.
2. 2 represents the ending square.  There is exactly one ending square.
3. 0 represents empty squares we can walk over.
4. -1 represents obstacles that we cannot walk over.
Find and return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints
2 <= N * M <= 20
-1 <= A[i] <= 2



Input Format
The first argument given is the integer matrix A.



Output Format
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example Input
Input 1:

A = [   [1, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 2, -1]   ]
Input 2:

A = [   [0, 1]
        [2, 0]    ]


Example Output
Output 1:

2
Output 2:

0


Example Explanation
Explanation 1:

We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Explanation 1:

Answer is evident here.

"""

class Solution:
    def solve(self, A):
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    startingPoint = [i,j]
        return self.findPaths(startingPoint[0], startingPoint[1], A, len(A), len(A[0]))
    def findPaths(self, i, j, A, n, m):
        if i < 0 or i >= n or j < 0 or j >= m or A[i][j] == -1:
            return 0        

        if A[i][j] == 2:
            for l in range(n):
                for k in range(m):
                    if A[l][k] == 0:
                        return 0
            return 1
        
        A[i][j] = -1
        result = 0
        result +=  self.findPaths(i, j+1, A, n, m)
        result +=  self.findPaths(i, j-1, A, n, m)
        result +=  self.findPaths(i+1, j, A, n, m)
        result +=  self.findPaths(i-1, j, A, n, m)        

        A[i][j] = 0

        return result

if __name__ == '__main__':
    A = [   [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]   ]
    print(Solution().solve(A))