import math
class MaxSumSquareSubMatrix():
    def Solve(self, arr, B):
        N = len(arr)
        
        # calculate the prefix sum array for 2D Matrix

        # 1. First initialize the pf sum array of size N * N
        pf_arr = []
        for i in range(N):
            pf_arr.append([0] * N)

        # 2. Calculate the prefix sum (left->right)
        for i in range(N):
            pf_arr[i][0] = arr[i][0]
            for j in range(1,N):
                pf_arr[i][j] = pf_arr[i][j-1] + arr[i][j]
        
        # 3. Calculate the prefix sum (top->bottom)
        for i in range(1,N):
            for j in range(N):
                pf_arr[i][j] += pf_arr[i-1][j]
        
        startRow, startCol = 0, 0
        endRow, endCol = B-1, B-1

        answer = -math.inf
        while(endRow < N and endCol < N):
            if startRow != 0 and startCol != 0:
                currSum = pf_arr[endRow][endCol] - pf_arr[endRow-startRow-1][endCol] - pf_arr[endRow][endCol-startCol-1] + pf_arr[startRow-1][startCol-1]
            elif startRow == 0 and startCol != 0:
                currSum = pf_arr[endRow][endCol] - pf_arr[endRow][endCol-startCol-1]
            elif startRow !=0 and startCol == 0:
                currSum = pf_arr[endRow][endCol] - pf_arr[endRow-startRow-1][endCol]
            else:
                currSum = pf_arr[endRow][endCol]
            
            answer = max(answer, currSum)

            if endCol == B-1:
                startRow += 1
                startCol = 0
                endCol = B-1
                endRow += 1
            else:
                startCol += 1
                endCol += 1
            
            return answer

