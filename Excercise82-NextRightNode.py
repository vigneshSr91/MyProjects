"""
Next Pointer Binary Tree


"""

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        current = root
        while current != None and current.left != None:
            temp = current
            while temp != None:
                temp.left.next = temp.right
                if temp.next != None:
                    temp.right.next = temp.next.left
                temp = temp.next
            current = current.left