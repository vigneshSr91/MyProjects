class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def removeNthFromEnd(self, A: Node, B):
        totalNodes = 0
        headNode=A
        tempNode=headNode

        while tempNode != None:
            totalNodes += 1
            tempNode = tempNode.next
        
        removeNode = max(1, totalNodes + 1 - B )

        tempNode = headNode
        if removeNode == 1:
            return headNode.next
        counter = 1
        """
        Iter    counter     
        1       1           tmp.nxt=2   rem_node=4
        2       2           tmp.nxt=3   rem_node=4
        3       3           tmp.nxt=4   rem_node=4
        4(steps out)
        
        """
        while tempNode.next != None and counter < removeNode:
            if counter+1 == removeNode and tempNode.next != None:
                tempNode.next = tempNode.next.next
            else:
                tempNode = tempNode.next
            counter += 1
        
        return headNode

if __name__ == '__main__':
    # setup test data
    head_node = Node(data=1)
    temp_node = head_node
    new_node = Node(data=2)
    temp_node.next = new_node
    temp_node = new_node
    new_node = Node(data=3)
    temp_node.next = new_node
    temp_node = new_node
    new_node = Node(data=4)
    temp_node.next = new_node
    temp_node = new_node
    new_node = Node(data=5)
    temp_node.next = new_node
    temp_node = new_node    

    print(Solution().removeNthFromEnd(A=head_node, B=1))

