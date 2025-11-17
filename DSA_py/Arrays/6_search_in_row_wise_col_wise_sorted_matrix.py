"""
Problem Description

Given a matrix of integers A of size N x M and an integer B.

In the given matrix every row and column is sorted in non-decreasing order. Find and return the position of B in the matrix in the given form:

If B is not present return -1.

Example Input

Input 1:-
A = [[1, 2, 3]
     [4, 5, 6]
     [7, 8, 9]]
B = 2

"""

class Solution:
    def run(self, A, B):
        i = 0
        j = len(A[0])-1
        while(i<len(A) and j>=0):
            if A[i][j] == B:
                return "Yes"
            elif A[i][j] > B:
                j -= 1
            elif A[i][j] < B:
                i += 1
        return "Not Found"

if __name__ == '__main__':
    A = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    B = 5
    print(Solution().run(A, B))
                