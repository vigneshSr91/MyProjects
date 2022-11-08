"""
Double Character Trouble

Problem Description

You are given a string A.

An operation on the string is defined as follows:

Remove the first occurrence of the same consecutive characters. eg for a string "abbcd", the first occurrence of same consecutive characters is "bb".

Therefore the string after this operation will be "acd".

Keep performing this operation on the string until there are no more occurrences of the same consecutive characters and return the final string.



Problem Constraints

1 <= |A| <= 100000



Input Format

First and only argument is string A.



Output Format

Return the final string.



Example Input

Input 1:

 A = abccbc
Input 2:

 A = ab


Example Output

Output 1:

 "ac"
Output 2:

 "ab"
"""
class Node():
    def __init__(self, val, next=None, previous=None ):
        self.val = val
        self.next = next
        self.previous = previous

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        newNode = Node(val=-1)
        headNode = newNode
        tailNode = headNode
        for i in range(len(A)):
            if tailNode.val == A[i]:
                tailNode = tailNode.previous
                tailNode.next = None
                continue
            else:
                tempNode = Node(val=A[i])
                tailNode.next = tempNode
                tempNode.previous = tailNode
                tailNode = tempNode
        tempNode = headNode.next
        result = ""
        while tempNode != None:
            result += tempNode.val
            tempNode = tempNode.next
        return result
        
if __name__ == '__main__':
    print(Solution().solve("abbaj"))


