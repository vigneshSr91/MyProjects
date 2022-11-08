"""
Nearest Smaller Element

Problem Description

Given an array A, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that

j is maximum possible AND

j < i AND

A[j] < A[i]

Elements for which no smaller element exist, consider the next smaller element as -1.



Problem Constraints

1 <= |A| <= 100000

-109 <= A[i] <= 109



Input Format

The only argument given is integer array A.



Output Format

Return the integar array G such that G[i] contains the nearest smaller number than A[i]. If no such element occurs G[i] should be -1.



Example Input

Input 1:

 A = [4, 5, 2, 10, 8]
Input 2:

 A = [3, 2, 1]


Example Output

Output 1:

 [-1, 4, -1, 2, 2]
Output 2:

 [-1, -1, -1]


Example Explanation

Explanation 1:

index 1: No element less than 4 in left of 4, G[1] = -1
index 2: A[1] is only element less than A[2], G[2] = A[1]
index 3: No element less than 2 in left of 2, G[3] = -1
index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
Explanation 2:

index 1: No element less than 3 in left of 3, G[1] = -1
index 2: No element less than 2 in left of 2, G[2] = -1
index 3: No element less than 1 in left of 1, G[3] = -1

"""
class Stack():
    def __init__(self):
        self.stack = [-1]
    
    def top(self):
        return self.stack[len(self.stack)-1]
    
    def pop(self):
        del self.stack[len(self.stack)-1]
    
    def push(self, val):
        self.stack.append(val)
    
    def isEmpty(self):
        return True if len(self.stack) == 0 else False
    
class Solution:
    def prevSmaller(self, A):
        result = []
        #result.append(-1)               # First element has no lesser element to it's left side
        lesserElementStack = Stack()

        for i in range(0,len(A)):
            while lesserElementStack.isEmpty() != True and lesserElementStack.top() >= A[i]:
                lesserElementStack.pop()
            if lesserElementStack.isEmpty() != True:
                result.append(lesserElementStack.top())
            lesserElementStack.push(A[i])
        return result

if __name__=='__main__':
    #print(Solution().prevSmaller(A=[4, 5, 2, 10, 8]))
    print(Solution().prevSmaller(A=[3, 2, 1]))


