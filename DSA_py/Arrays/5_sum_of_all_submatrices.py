"""
Problem Description

Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.

Example Input

Input 1:
A = [ [1, 1]
      [1, 1] ]
Input 2:
A = [ [1, 2]
      [3, 4] ]


Example Output

Output 1:
16
Output 2:
40
"""

class Solution:
    def solve(self, A):
        result = 0
        for row in range(len(A)):
            for col in range(len(A[row])):
                no_top_left = (row+1) * (col+1)
                no_of_bottom_right = (len(A)-row) * (len(A[row])-col)
                result += no_top_left * no_of_bottom_right * A[row][col]

        return result

if __name__ == '__main__':
    A = [ [1, 2],
        [3, 4] ]
    print(Solution().solve(A))