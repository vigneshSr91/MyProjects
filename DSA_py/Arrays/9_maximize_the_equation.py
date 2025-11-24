class Solution:
    def solve(self, A):
        max1 = 0
        max2 = 0
        min1 = 0
        min2 = 0
        ans  = 0
        for(i in range(len(A))):
            max1 = max(max1, A[i]+i)
            max2 = max(max2, A[i]-i)
            min1 = min(min1, A[i]+i)
            min2 = min(min2, A[i]-i)

            ans = max(max1-min1, max2-min2)
        return ans

if __name__ == '__main__':
    A = [1,3,-1]
    print(Solution().solve(A))

