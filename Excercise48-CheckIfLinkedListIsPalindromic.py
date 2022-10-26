"""
Q3. Palindrome List

Problem Description

Given a singly linked list A, determine if it's a palindrome. Return 1 or 0, denoting if it's a palindrome or not, respectively.



Problem Constraints

1 <= |A| <= 105



Input Format

The first and the only argument of input contains a pointer to the head of the given linked list.



Output Format

Return 0, if the linked list is not a palindrome.

Return 1, if the linked list is a palindrome.



Example Input

Input 1:

A = [1, 2, 2, 1]
Input 2:

A = [1, 3, 2]


Example Output

Output 1:

 1 
Output 2:

 0 


Example Explanation

Explanation 1:

 The first linked list is a palindrome as [1, 2, 2, 1] is equal to its reversed form.
Explanation 2:

 The second linked list is not a palindrom as [1, 3, 2] is not equal to [2, 3, 1].

"""

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param A : head node of linked list
	# @return an integer    
    def lPalin(self, A):
        headNode2 = self.getSecondHeadNode(A)
        headNode2 = self.reverseSecondHeadnode(headNode2)
        headNode1 = A
        while headNode2 != None:
            if headNode1.val != headNode2.val:
                return 0
            headNode1 = headNode1.next
            headNode2 = headNode2.next
        return 1
    def reverseSecondHeadnode(self, A):
        currentNode = A
        headNode = A

        previous = None

        while currentNode != None:
            temp = currentNode.next
            currentNode.next = previous
            previous = currentNode
            currentNode = temp
        headNode = previous   
        return headNode     

    def getSecondHeadNode(self, A):
        tempNode = A
        counter = 0
        while tempNode != None:
            counter += 1
            tempNode = tempNode.next
        
        fast = A
        slow = A
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 - >7
        # 1st Iter Fast: 3 slow: 2
        # 2nd Iter Fast: 5 slow: 3
        # 3rd Iter Fast: 7 slow: 4
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6
        # 1st Iter Fast: 3 slow: 2
        # 2nd Iter Fast: 5 slow: 3      
        previous = None
        while fast.next != None and fast.next.next != None:
            previous = slow
            slow = slow.next
            fast = fast.next.next
        if counter % 2 == 0:
            headNode2 = slow.next
        else:
            headNode2 = slow.next
        return headNode2
        

if __name__ == '__main__':
    headNode = ListNode(1)
    newNode = ListNode(2)
    headNode.next = newNode
    newNode = headNode.next
    newNode.next = ListNode(3)

    print(Solution().lPalin(headNode))
