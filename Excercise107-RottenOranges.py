"""
Rotten Oranges

Problem Description

Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

Each cell can have three values:

The value 0 representing an empty cell.

The value 1 representing a fresh orange.

The value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.



Problem Constraints
1 <= N, M <= 1000

0 <= A[i][j] <= 2



Input Format
The first argument given is the integer matrix A.



Output Format
Return the minimum number of minutes that must elapse until no cell has a fresh orange.

If this is impossible, return -1 instead.



Example Input
Input 1:

A = [   [2, 1, 1]
        [1, 1, 0]
        [0, 1, 1]   ]
Input 2:

 
A = [   [2, 1, 1]
        [0, 1, 1]
        [1, 0, 1]   ]


Example Output
Output 1:

 4
Output 2:

 -1


Example Explanation
Explanation 1:

 Max of 4 using (0,0) , (0,1) , (1,1) , (1,2) , (2,2)
Explanation 2:

 Task is impossible

"""
import math
from collections import deque
class Solution:
    def solve(self, A):
        source = []
        x,y = [0,-1,0,1],[-1,0,1,0]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 2:
                    source.append([i,j,0])
        return self.bfs(A, x, y, source, len(A), len(A[0]))
    
    def bfs(self, mat, x, y, source, N, M):
        q = deque()
        for element in source:
            q.append(element)
        answer = 0
        while len(q) > 0:
            element = q.popleft()
            i, j, level = element[0], element[1], element[2]
            if mat[i][j] == 2:
                for k in range(len(x)):
                    if i+x[k] < 0 or i+x[k] > N-1 or j+y[k] < 0 or j+y[k] > M-1:
                        continue
                    elif mat[i+x[k]][j+y[k]] == 1:
                        mat[i+x[k]][j+y[k]] = 2
                        q.append([i+x[k],j+y[k], level+1])
                        answer = max(answer, level+1)
        for i in range(N):
            for j in range(M):
                if mat[i][j] == 1:
                    return -1
        return answer

if __name__ == '__main__':
    A = [
            [2, 0, 2, 2, 2, 0, 2, 1, 1, 0],
            [0, 1, 2, 0, 2, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 2, 0, 1, 1, 2, 1],
            [2, 0, 2, 0, 1, 1, 2, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 2, 0, 2, 2],
            [0, 2, 1, 1, 2, 2, 0, 2, 1, 2],
            [2, 1, 0, 2, 0, 0, 0, 0, 1, 1],
            [2, 2, 0, 2, 2, 1, 1, 1, 2, 2]
            ]
    print(Solution().solve(A))

        
        
        
