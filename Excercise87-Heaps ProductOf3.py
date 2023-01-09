import heapq
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # Base Cases
        if len(A) == 1:
            return [-1]
        if len(A) == 2:
            return [-1,-1]
        if len(A) == 3:
            return [-1,-1, A[0]*A[1]*A[2]]

        result = [-1, -1]
        for i in range(2,len(A)):
            maxHeap=[]
            for j in range(i+1):
                heapq.heappush(maxHeap,-A[j])
            x=3
            thisAnswer = (heapq.heappop(maxHeap) * -1) * (heapq.heappop(maxHeap) * -1) * (heapq.heappop(maxHeap) * -1)
            result.append(thisAnswer)
        return result

if __name__=='__main__':
    print(Solution().solve([1,2,3,4,5]))