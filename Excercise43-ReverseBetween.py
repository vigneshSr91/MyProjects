from itertools import count


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution():
    def reverseBetween(self, A, B, C):
        head_main = A
        startPoint = B
        endPoint = C
        counter = 1
        tempNode = head_main
        tailNode = None
        startNode = None
        if head_main == None:
            return
        while ( counter <= startPoint ) and tempNode !=None:
            if counter == startPoint:
                startNode = tempNode
                tempNode = tempNode.next
            #elif counter == endPoint:
            #   endNode = tempNode
            else:
                tailNode = tempNode
                tempNode = tempNode.next
            counter += 1
        
        counter = 1
        tempNode = head_main.next
        while counter < endPoint and tempNode != None:
            counter += 1
            tempNode = tempNode.next
        endNode = tempNode

        currentNode = startNode
        previous = None
        counter = startPoint
        while currentNode != None and counter <= endPoint:
            tempNode = currentNode.next
            currentNode.next = previous
            previous = currentNode
            currentNode = tempNode
            counter += 1

        if tailNode != None:
            tailNode.next = previous
            tempNode = previous
            while tempNode.next != None:
                tempNode = tempNode.next
            tempNode.next = endNode
        else:
            tempNode = previous
            while tempNode.next != None:
                tempNode = tempNode.next
            tempNode.next = endNode
            return previous

        return head_main

if __name__ == '__main__':
    """
    97 -> 63 -> 89 -> 34 -> 82 -> 95 -> 4 -> 70 -> 14 -> 41 -> 38 -> 
    83 -> 49 -> 32 -> 68 -> 56 -> 99 -> 52 -> 33 -> 54
    """
   # setup test data
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

    Solution().reverseBetween(head_node,13,15)




