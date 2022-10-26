class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution():
    def reorderList(self,A):
        orginal_ll = self.copyLinkedList(A)

        reversed_ll = A
        currentNode = A
        previous = None
        while currentNode != None:
            tempNode = currentNode.next     # tempNode = 2          # tempNode = 3
            currentNode.next = previous     # 1.next = None         # 2.next = 1
            previous = currentNode          # previous = 1          # previous = 2
            currentNode = tempNode          # currentNode = 2       # currentNode = 3
        
        reversed_ll = previous

        tempNode1 = orginal_ll
        tempNode2 = reversed_ll
        result = ListNode(-1)
        result_temp = result
        while tempNode1 != None and tempNode2 != None:
            if tempNode1.val == tempNode2.val:
                result_temp.next = ListNode( tempNode1.val )
                break
            result_temp.next = ListNode( tempNode1.val )
            result_temp.next.next = ListNode( tempNode2.val )
            result_temp = result_temp.next.next
            tempNode1 = tempNode1.next
            tempNode2 = tempNode2.next
        
        return result.next

    
    def copyLinkedList(self, A):
        tempNode = A
        B = B_Head = ListNode(-1)
        while tempNode != None:
            B.next = ListNode( tempNode.val )
            tempNode = tempNode.next
            B = B.next
        return B_Head.next


if __name__ == "__main__":
   # setup test data
    """
    head_node = Node(data=97)
    temp_node = head_node
    new_node = Node(data=63)
    temp_node.next = new_node
    temp_node = new_node
    new_node = Node(data=89)
    temp_node.next = new_node
    temp_node = new_node 
    new_node = Node(data=34)
    temp_node.next = new_node
    temp_node = new_node  
    new_node = Node(data=82)
    temp_node.next = new_node
    temp_node = new_node  
    new_node = Node(data=95)
    temp_node.next = new_node
    temp_node = new_node  
    new_node = Node(data=4)
    temp_node.next = new_node
    temp_node = new_node    
    new_node = Node(data=70)
    temp_node.next = new_node
    temp_node = new_node  
    new_node = Node(data=14)
    temp_node.next = new_node
    temp_node = new_node  
    new_node = Node(data=41)
    temp_node.next = new_node
    temp_node = new_node  
    new_node = Node(data=38)
    temp_node.next = new_node
    temp_node = new_node    
    new_node = Node(data=83)
    temp_node.next = new_node
    temp_node = new_node     
    new_node = Node(data=49)
    temp_node.next = new_node
    temp_node = new_node  
    new_node = Node(data=32)
    temp_node.next = new_node
    temp_node = new_node  
    new_node = Node(data=68)
    temp_node.next = new_node
    temp_node = new_node    
    new_node = Node(data=56)
    temp_node.next = new_node
    temp_node = new_node   
    new_node = Node(data=99)
    temp_node.next = new_node
    temp_node = new_node  
    new_node = Node(data=52)
    temp_node.next = new_node
    temp_node = new_node  
    new_node = Node(data=33)
    temp_node.next = new_node
    temp_node = new_node    
    new_node = Node(data=54)
    temp_node.next = new_node
    temp_node = new_node       
    """
print(Solution().reorderList(head_node).val)
