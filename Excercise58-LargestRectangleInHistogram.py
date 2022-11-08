"""
Largest Rectangle in Histogram

Problem Description

Given an array of integers A.

A represents a histogram i.e A[i] denotes the height of the ith histogram's bar. Width of each bar is 1.

Find the area of the largest rectangle formed by the histogram.



Problem Constraints

1 <= |A| <= 100000

1 <= A[i] <= 1000000000



Input Format

The only argument given is the integer array A.



Output Format

Return the area of the largest rectangle in the histogram.



Example Input

Input 1:

 A = [2, 1, 5, 6, 2, 3]
Input 2:

 A = [2]


Example Output

Output 1:

 10
Output 2:

 2


Example Explanation

Explanation 1:

The largest rectangle has area = 10 unit. Formed by A[3] to A[4].
Explanation 2:

Largest rectangle has area 2.


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
    def largestRectangleArea(self, A):

        # A = [2, 1, 5, 6, 2, 3]
        # l = [-1, 1, 1, 1, 1, 1]
        # r = [1, 5, 5, 5, 5, 5]

        leftSmallerIndex=[]
        rightSmallerIndex=[]
        st = Stack()
        for i in range(len(A)):
            while st.isEmpty() == False and A[i] <= A[st.top()]:
                st.pop()
            
            if st.isEmpty() == False:
                leftSmallerIndex.append(st.top())
            else:
                leftSmallerIndex.append(-1)
            st.push(i)
        
        st = Stack()
        st.push(len(A)-1)
        rightSmallerIndex.append(-1)
        for i in range(len(A)-2,-1,-1):
            while st.isEmpty() == False and A[i] <= A[st.top()]:
                st.pop()
            
            if st.isEmpty() == False:
                rightSmallerIndex.append(st.top())
            else:
                rightSmallerIndex.append(-1)
            st.push(i)

        rightSmallerIndex = rightSmallerIndex[::-1]
                
            
        bestAnswer = 0
        currentAnswer = 0
        for i in range(len(A)):
            #answer = max(answer, A[i] * (rightSmallerIndex[i]-leftSmallerIndex[i]))
            if leftSmallerIndex[i] == -1:
                currentAnswer += (i+1) * A[i]
            else:
                currentAnswer += (i-leftSmallerIndex[i]) * A[i]
            
            if rightSmallerIndex[i] == -1:
                currentAnswer += (len(A)-1-i) * A[i]
            else:
                currentAnswer += (rightSmallerIndex[i]-i-1) * A[i]
            
            bestAnswer = max(currentAnswer,bestAnswer)

            currentAnswer = 0
        
        return bestAnswer

if __name__ == '__main__':
    print(Solution().largestRectangleArea(A=[2, 1, 5, 6, 2, 3]))
    print(Solution().largestRectangleArea(A=[1]))
    print(Solution().largestRectangleArea(A=[ 90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ])) 


