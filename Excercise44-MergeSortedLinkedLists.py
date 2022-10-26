class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def mergeTwoLists(self, A, B):
        H1 = A
        H2 = B
        H3 = ListNode(-1)
        tail = H3

        while H1 != None and H2 != None:
            if H1.val <= H2.val:
                tail.next = H1
                H1 = H1.next
                tail = tail.next
            else:
                tail.next = H2
                H2 = H2.next
                tail = tail.next
        
        if H1 != None:
            tail.next = H1
        
        if H2 != None:
            tail.next = H2
        
        return H3.next

