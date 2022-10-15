"""
You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.

Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

NOTE: if B > N, return an empty array.



Input Format

First argument is an integer array A
Second argument is an integer B.



Output Format

Return an integer array.



Example Input

Input 1:

 A = [1, 2, 1, 3, 4, 3]
 B = 3
Input 2:

 A = [1, 1, 2, 2]
 B = 1


Example Output

Output 1:

 [2, 3, 3, 2]
Output 2:

 [1, 1, 1, 1]


Example Explanation

Explanation 1:

 A=[1, 2, 1, 3, 4, 3] and B = 3
 All windows of size B are
 [1, 2, 1]
 [2, 1, 3]
 [1, 3, 4]
 [3, 4, 3]
 So, we return an array [2, 3, 3, 2].
Explanation 2:

 Window size is 1, so the output array is [1, 1, 1, 1].

"""
class Solution():
    def solve(self, A, B):
        if B > len(A):
            return []
        elementsFrequencyHashMap = dict()
        answer = []
        for i in range(B):
            if A[i] not in elementsFrequencyHashMap:
                elementsFrequencyHashMap[A[i]] = 1
            else:
                elementsFrequencyHashMap[A[i]] += 1
        answer.append(len(elementsFrequencyHashMap))
        for i in range(B,len(A)):
            # remove the outgoing element
            frequency = elementsFrequencyHashMap[A[i-B]]
            frequency -= 1
            if frequency == 0:
                elementsFrequencyHashMap.pop(A[i-B])
            else:
                elementsFrequencyHashMap[A[i-B]] = frequency
            
            # Add the incoming element
            if A[i] in elementsFrequencyHashMap:
                elementsFrequencyHashMap[A[i]] += 1
            else:
                elementsFrequencyHashMap[A[i]] = 1
            
            # append the distinct keys to result
            answer.append(len(elementsFrequencyHashMap))
        return answer

if __name__ == '__main__':
    print(Solution().solve(A = [1, 2, 1, 3, 4, 3], B = 3))
    print(Solution().solve(A = [1, 1, 1, 1], B = 1))