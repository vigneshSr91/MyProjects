import sys
import math

sys.setrecursionlimit(10**6)
class Solution:
    def countMinSquares(self, A):
        self.dp = [-1] * (A+1)
        self.dp[0] = 0 

        if self.dp[A] != -1:
            return self.dp[A]
        
        for j in range(1,A+1):
            self.ans = math.inf
            for i in range(1,j+1):
                if i*i <= j:
                    self.ans = min(self.ans, self.dp[j-i*i]+1)
                else:
                    break
            self.dp[j] = self.ans
        return self.dp[A]


if __name__ == '__main__':
    print(Solution().countMinSquares(6))