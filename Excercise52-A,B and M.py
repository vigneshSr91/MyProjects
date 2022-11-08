"""
Q2. A, B and Modulo

Problem Description
Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.



Problem Constraints
1 <= A, B <= 109
A != B



Input Format
The first argument is an integer A.
The second argument is an integer B.



Output Format
Return an integer denoting the greatest possible positive M.



Example Input
Input 1:

A = 1
B = 2
Input 2:

A = 5
B = 10


Example Output
Output 1:

1
Output 2:

5


Example Explanation
Explanation 1:

1 is the largest value of M such that A % M == B % M.
Explanation 2:

For M = 5, A % M = 0 and B % M = 0.

No value greater than M = 5, satisfies the condition.

"""
import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = (A - B) if A > B else (B-A)
        answer = 0
        for i in range(int(math.sqrt(N)+1)):
            if A % i == B % i:
                answer = i
        return answer

