# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    def reverseList(self, A):
        currentNode = A
        headNode = A

        previous = None

        while currentNode != None:
            temp = currentNode.next
            currentNode.next = previous
            previous = currentNode
            currentNode = temp
        headNode = previous


