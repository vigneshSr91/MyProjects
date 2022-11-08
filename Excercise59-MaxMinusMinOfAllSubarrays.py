"""
MAX and MIN

Problem Description

Given an array of integers A.

value of a array = max(array) - min(array).

Calculate and return the sum of values of all possible subarrays of A modulo 109+7.



Problem Constraints

1 <= |A| <= 100000

1 <= A[i] <= 1000000



Input Format

The first and only argument given is the integer array A.



Output Format

Return the sum of values of all possible subarrays of A modulo 109+7.



Example Input

Input 1:

 A = [1]
Input 2:

 A = [4, 7, 3, 8]


Example Output

Output 1:

 0
Output 2:

 26


Example Explanation

Explanation 1:

Only 1 subarray exists. Its value is 0.
Explanation 2:

value ( [4] ) = 4 - 4 = 0
value ( [7] ) = 7 - 7 = 0
value ( [3] ) = 3 - 3 = 0
value ( [8] ) = 8 - 8 = 0
value ( [4, 7] ) = 7 - 4 = 3
value ( [7, 3] ) = 7 - 3 = 4
value ( [3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3] ) = 7 - 3 = 4
value ( [7, 3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3, 8] ) = 8 - 3 = 5
sum of values % 10^9+7 = 26


"""

class Stack():
    def __init__(self):
        self.stack = []
    
    def top(self):
        return self.stack[len(self.stack)-1]
    
    def pop(self):
        del self.stack[len(self.stack)-1]
    
    def push(self, val):
        self.stack.append(val)
    
    def isEmpty(self):
        return True if len(self.stack) == 0 else False

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        leftSmallerIndex=[]
        rightSmallerIndex=[]    

        # LEFT SMALLER

        st = Stack()
        for i in range(len(A)):
            while st.isEmpty() == False and A[i] <= A[st.top()]:
                st.pop()
            
            if st.isEmpty() == False:
                leftSmallerIndex.append(i-st.top())
            else:
                leftSmallerIndex.append(i+1)
            st.push(i)
        
        # RIGHT SMALLER

        st = Stack()
        for i in range(len(A)-1,-1,-1):
            while st.isEmpty() == False and A[i] < A[st.top()]:
                st.pop()
            
            if st.isEmpty() == False:
                rightSmallerIndex.append(st.top()-i)
            else:
                rightSmallerIndex.append(len(A)-i)
            st.push(i)

        rightSmallerIndex = rightSmallerIndex[::-1]         

        leftLargerIndex=[]
        rightLargerIndex=[]              


        # LEFT LARGER

        st = Stack()
        for i in range(len(A)):
            while st.isEmpty() == False and A[i] >= A[st.top()]:
                st.pop()
            
            if st.isEmpty() == False:
                leftLargerIndex.append(i-st.top())
            else:
                # If I'm the largest element to the left most, then I can be max for all subarrays till my position
                # since the formula is i-leftLargerIndex, in this case it must be zero
                leftLargerIndex.append(i+1)
            st.push(i)        
        

        # RIGHT LARGER

        st = Stack()
        for i in range(len(A)-1,-1,-1):
            while st.isEmpty() == False and A[i] > A[st.top()]:
                st.pop()
            
            if st.isEmpty() == False:
                rightLargerIndex.append(st.top()-i)
            else:
                # If I'm the largest element till the right most, then I can be max for all subarrays till end
                rightLargerIndex.append(len(A)-i)
            st.push(i)

        rightLargerIndex = rightLargerIndex[::-1]           

        TotalMax = 0
        TotalMin = 0
        answer = 0
        for i in range(len(A)):
            """
            if leftLargerIndex[i] == -1:
                leftLargeStartVal = 1
            else:
                leftLargeStartVal = i-leftLargerIndex[i]
            """
            leftLargeStartVal = leftLargerIndex[i]
            """
            if rightLargerIndex[i] == -1:
                rightLargeEndVal = len(A)
            else:
                rightLargeEndVal = rightLargerIndex[i]-i
            """
            rightLargeEndVal = rightLargerIndex[i]

            TotalMax += A[i] * (leftLargeStartVal) * (rightLargeEndVal)

            """
            if leftSmallerIndex[i] == -1:
                leftMinStartVal = 1
            else:
                leftMinStartVal = i-leftSmallerIndex[i]
            """
            leftMinStartVal = leftSmallerIndex[i]

            """
            if rightSmallerIndex[i] == -1:
                rightMinEndVal = len(A)
            else:
                rightMinEndVal = rightSmallerIndex[i]-i
            """
            rightMinEndVal = rightSmallerIndex[i]

            TotalMin += A[i] * leftMinStartVal * rightMinEndVal

        answer += (TotalMax-TotalMin) % ((10**9)+7)

        return answer % ((10**9)+7)

if __name__ == '__main__':
    print(Solution().solve([4, 7, 3, 8]))