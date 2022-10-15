"""
Find subsequence

Given two strings A and B, find if A is a subsequence of B.

Return "YES" if A is a subsequence of B, else return "NO".

Input Format

The first argument given is the string A.
The second argument given is the string B.
Output Format

Return "YES" if A is a subsequence of B, else return "NO".
Constraints

1 <= lenght(A), length(B) <= 100000
'a' <= A[i], B[i] <= 'z'
For Example

Input 1:
    A = "bit"
    B = "dfbkjijgbbiihbmmt"
Output 1:
    YES

Input 2:
    A = "apple"
    B = "appel"
Output 2:
    "NO"
"""
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        pointer_A = 0
        pointer_B = 0
        while pointer_B < len(B):
            if pointer_A == len(A)-1:
                return "YES"
            if A[pointer_A] == B[pointer_B]:
                pointer_A += 1
                pointer_B += 1
            else:
                pointer_B += 1
        return "NO"

if __name__ == '__main__':
    print(Solution().solve(A="bit", B="dfbkjijgbbiihbmmt"))