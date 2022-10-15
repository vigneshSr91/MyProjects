class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        startPoint = 0
        endPoint = len(A) - 1
        answer = 0
        while endPoint > startPoint:
            if A[startPoint] + A[endPoint] > B:
                endPoint -= 1
            elif A[startPoint] + A[endPoint] < B:
                startPoint += 1
            else:
                startPoint += 1
                endPoint -= 1
                answer += 1
        return answer

if __name__ == '__main__':
    print(Solution().solve(A=[1, 2, 3, 4, 5], B=5))
    print(Solution().solve(A=[5, 10, 20, 100, 105], B=110))