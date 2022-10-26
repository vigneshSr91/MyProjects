"""
Q1. Delete middle node of a Linked List

Given a singly linked list, delete middle of the linked list.

For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5

If there are even nodes, then there would be two middle nodes, we need to delete the second middle element.

For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.

Return the head of the linked list after removing the middle node.

If the input linked list has 1 node, then this node should be deleted and a null node should be returned.


Input Format

The only argument given is the node pointing to the head node of the linked list

"""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        head = A
        temp = A

        if head == None:
            return None
        elif head.next == None:
            return None
        # Find Length
        index = 1
        while temp.next != None:
            temp = temp.next
            index += 1
        
        mid_element = ( index // 2 ) + 1

        temp = head
        index = 1
        while temp.next != None and index <= mid_element:
            if index == mid_element-1:
                previous = temp
            elif index == mid_element:
                previous.next = temp.next
            index += 1
        
        return A
        

        
        

