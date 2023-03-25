import sys
sys.setrecursionlimit(10**6)
class Solution():
    def solve(self, arr):
        maxValue = 0
        return self.findMax([0,0], arr, maxValue)
        
    def findMax(self, currentPosition, arr, currentValue):
        directions=[[-1,0],[1,0],[0,-1],[0,1]]

        if currentPosition[0] == len(arr)-1 and currentPosition[1] == len(arr[0])-1:
            return currentValue

        thisValue = currentValue
        if arr[currentPosition[0]][currentPosition[1]] == 1:
            thisValue += 1
        else :
            thisValue = 0
            
        for i in range(len(directions)):
            u = directions[i][0]
            v = directions[i][1]
            if currentPosition[0]+u >= len(arr) or currentPosition[0]+u < 0 or currentPosition[1]+v >= len(arr[0]) or currentPosition[1]+v < 0:
                continue

            nextStep = [currentPosition[0]+u,currentPosition[1]+v]
            currentValue = max(currentValue, self.findMax(nextStep,arr, thisValue))
        
        return currentValue

if __name__ == '__main__':
    A = [   [1,  0, 0, 1],
            [1,  1, 0, 0 ],
            [0,  0, 0, 1 ],
            [1,  1, 1, 1 ] ]
    print(Solution().solve(A))