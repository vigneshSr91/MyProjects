"""
Longest Palindromic List

Problem Description

Given a linked list of integers. Find and return the length of the longest palindrome list that exists in that linked list.

A palindrome list is a list that reads the same backward and forward.

Expected memory complexity : O(1)



Problem Constraints

1 <= length of the linked list <= 2000

1 <= Node value <= 100



Input Format

The only argument given is head pointer of the linked list.



Output Format

Return the length of the longest palindrome list.



Example Input

Input 1:

 2 -> 3 -> 3 -> 3
Input 2:

 2 -> 1 -> 2 -> 1 ->  2 -> 2 -> 1 -> 3 -> 2 -> 2


Example Output

Output 1:

 3
Output 2:

 5


Example Explanation

Explanation 1:

 3 -> 3 -> 3 is largest palindromic sublist
Explanation 2:

 2 -> 1 -> 2 -> 1 -> 2 is largest palindromic sublist.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        previous = None

class Solution:
    def solve(self, A):
        self.convertToDoublyLL(A)
        


    def getMiddleNode(self, A):
        fast = A
        slow = A

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow.next

    def calculateMaxPalindromicLength(self, HeadNode):
        totalLength = self.getLengthOfLL(HeadNode)
        
            
        


    def getLengthOfLL(self, A):
        tempNode = A
        counter = 0
        while tempNode != None:
            counter += 1
            tempNode = tempNode.next
        return counter
    
    def convertToDoublyLL(self, A):
        tempNode = A
        previous = None
        while tempNode != None:
            tempNode.previous = previous
            previous = tempNode
            tempNode = tempNode.next