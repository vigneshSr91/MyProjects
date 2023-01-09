"""
Unique Paths in a Grid

Problem Description
Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively in the grid.



Problem Constraints
1 <= n, m <= 100
A[i][j] = 0 or 1



Input Format
Firts and only argument A is a 2D array of size n * m.



Output Format
Return an integer denoting the number of unique paths from (1, 1) to (n, m).



Example Input
Input 1:

 A = [
        [0, 0, 0]
        [0, 1, 0]
        [0, 0, 0]
     ]
Input 2:

 A = [
        [0, 0, 0]
        [1, 1, 1]
        [0, 0, 0]
     ]


Example Output
Output 1:

 2
Output 2:

 0

"""
class Solution:
	# @param A : list of list of integers
	# @return an integer
    def uniquePathsWithObstacles(self, A):
        self.dp = []
        self.A = A
        n = len(A)
        m = len(A[0])
        if A[0][0]==1 or A[n-1][m-1]==1:
            return 0
        for i in range(len(A)):
            thisLine = []
            for j in range(len(A[0])):
                thisLine.append(-1)
            self.dp.append(thisLine)
        return self.ways(len(A)-1,len(A[0])-1)
    def ways(self, i, j):
        if self.A[i][j] == 1:
            return 0
        if i == 0 and j == 0:
            return 1
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        
        if i == 0:
            self.dp[i][j] = self.ways(i, j-1)
        elif j == 0:
            self.dp[i][j] = self.ways(i-1, j)
        else:
            self.dp[i][j] = self.ways(i-1,j) + self.ways(i, j-1)
        return self.dp[i][j]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles(A=[[0]]))