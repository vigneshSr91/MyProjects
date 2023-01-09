"""
Binary Tree From Inorder And Postorder


"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def buildTree(self, A, B):
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree        
        self.inOrderElementsToIndexMapping = dict()
        for i in range(len(A)):
            # Assuming No Duplicate elements/Nodes with same values
            self.inOrderElementsToIndexMapping[A[i]] = i 
        return self.construct(inOrder=A, postOrder=B, postOrderStart=0, postOrderEnd=len(A)-1, inOrderStart=0, inOrderEnd=len(A)-1)

    def construct(self, inOrder, postOrder, inOrderStart, inOrderEnd, postOrderStart, postOrderEnd):
        if postOrderStart > postOrderEnd:
            return None
        rootElement = postOrder[postOrderEnd]
        root = TreeNode(rootElement)
        length = self.inOrderElementsToIndexMapping.get(root.val) - inOrderStart
        root.left = self.construct(inOrder=inOrder, postOrder=postOrder, postOrderStart=postOrderStart, postOrderEnd=postOrderStart+length-1, inOrderStart=inOrderStart, inOrderEnd=self.inOrderElementsToIndexMapping.get(root.val)-1)
        root.right = self.construct(inOrder=inOrder, postOrder=postOrder, postOrderStart=postOrderStart+length, postOrderEnd=postOrderEnd-1, inOrderStart=self.inOrderElementsToIndexMapping.get(root.val)+1, inOrderEnd=inOrderEnd)
        return root