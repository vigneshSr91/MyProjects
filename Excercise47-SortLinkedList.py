"""
Q2. Sort List

Problem Description

Sort a linked list, A in O(n log n) time using constant space complexity.



Problem Constraints

0 <= |A| = 105



Input Format

The first and the only arugment of input contains a pointer to the head of the linked list, A.



Output Format

Return a pointer to the head of the sorted linked list.



Example Input

Input 1:

A = [3, 4, 2, 8]
Input 2:

A = [1]


Example Output

Output 1:

[2, 3, 4, 8]
Output 2:

[1]


Example Explanation

Explanation 1:

 The sorted form of [3, 4, 2, 8] is [2, 3, 4, 8].
Explanation 2:

 The sorted form of [1] is [1].

"""

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def sortList(self, A):
        return self.MergeSort(A)
        
        
    
    def MergeSort(self, A):
        if A == None or A.next == None:
            return A

        headNode = A
        middleNode = self.getMedianNode(headNode)
        headNode2 = middleNode.next
        middleNode.next = None

        headNode    = self.MergeSort(headNode)
        headNode2   = self.MergeSort(headNode2)

        return self.merge(headNode, headNode2)
    
    def Merge(self, headNode: ListNode, headNode2: ListNode):
        headNode3 = ListNode(-1)
        tailNode = headNode3
        while headNode != None and headNode2 != None:
            if headNode.val >= headNode2.val:
                tailNode.next = headNode
                tailNode = tailNode.next
                headNode = headNode.next
            else:
                tailNode.next = headNode2
                tailNode = tailNode.next
                headNode2 = headNode2.next
            
        while headNode != None: 
            tailNode.next = headNode
        
        while headNode2 != None:
            tailNode.next = headNode2
            
        return headNode3


    
    def getMedianNode(self, A):
        slow = A
        fast = A

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        """
        Odd Nodes
        1-> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
        1st Iteration end:
            slow = 2
            fast = 3
        2nd Iteration end:
            slow = 3
            fast = 5
        3rd Iteration end:
            slow = 4
            fast = 7
        4th Iteration end
            slow = 5
            fast = 9
        5th Iteration Fails ans fast.nwxt == None

        even Node:

        1 -> 2
        1st Iteration end
        Iteration Not possible, it should return 1st node itself

        1 -> 2 -> 3 -> 4 -> 5 -> 6

        1st Iter end:
        slow = 2
        fast = 3
        
        2nd Iter end:
        slow = 3
        fast = 5

        3nd Iter end:
        slow = 4
        fast = NA
        """

        return slow