# Kadanes Algorithm
import math
class MaxSubarraySum:
    def solve(self, A):
        result = -math.inf
        total = 0

        for i in A:
            total += i
            if total > result:
                result = total
            if total < 0:
                total = 0
        print(result)

if __name__ == '__main__':
    MaxSubarraySum().solve([-1,2,3,-4,6,9,2,-1,8,3])