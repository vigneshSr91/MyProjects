"""
Problem statement:
Maximum subrray sum - subarray that has the maximum sum

step 1:

How to consider all sub arrays in an array
[-1, 2, 3, -4, 6, 9, 2, -1, 8, 3]

step 2:
calculate the sum of each sub-array, then find the subarray with maximum sum

Optimized approach: Maximum sub-array sum (carry forward approach)

"""
import math
if __name__ == '__main__':
    A = [-1, 2, 3, -4, 6, 9, 2, -1, 8, 3]
    """
    Brute force O(N^3)

    for i in range(len(A)+1):
        for j in range(i, len(A)+1):
            result = []
            for k in range(i,j):
                result.append(A[k])
            if len(result) > 0:
                print(result)
    """
    sum = 0
    answer = -math.inf

    for i in A:
        sum += i
        if sum > answer:
            answer = sum
        if sum < 0:
            sum = 0
    print(answer)