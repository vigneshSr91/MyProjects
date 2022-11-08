"""
Pair Sum divisible by M

Problem Description

Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.

Since the answer may be large, return the answer modulo (109 + 7).



Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 106



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.



Output Format

Return the total number of pairs for which the sum is divisible by B modulo (109 + 7).



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
 B = 2
Input 2:

 A = [5, 17, 100, 11]
 B = 28


Example Output

Output 1:

 4
Output 2:

 1


Example Explanation

Explanation 1:

 All pairs which are divisible by 2 are (1,3), (1,5), (2,4), (3,5). 
 So total 4 pairs.


"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        FreqHashmap = dict()
        for i in range(len(A)):
            remainder = A[i] % B

            if remainder in FreqHashmap:
                FreqHashmap[remainder] += 1
            else:
                FreqHashmap[remainder] = 1
        

        pairs = 0
        # 1  2  3   4   5   6   7           B//2 = 3
        # 1 2   3   4   5   6   7   8       B//2 = 4
        if 0 in FreqHashmap:
            pairs = (FreqHashmap[0] * (FreqHashmap[0]-1))//2
        
        i = 1
        j = B-1

        while i < j:
            if i in FreqHashmap and j in FreqHashmap:
                pairs += FreqHashmap[i] * FreqHashmap[j]
            i += 1
            j -= 1
        if i == j and i in FreqHashmap:
            pairs += (FreqHashmap[i] * (FreqHashmap[i]-1))//2
        
        return pairs

if __name__ == '__main__':
    A = [ 1, 2, 3, 4, 5 ]
    B = 2    
    print(Solution().solve(A,B))
