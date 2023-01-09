class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
import sys
sys.setrecursionlimit(10**5)
class Solution:
    def buildTree(self, A, B):
        self.inOrderElementsToIndexMapping = dict()
        for i in range(len(B)):
            # Assuming No Duplicate elements/Nodes with same values
            self.inOrderElementsToIndexMapping[B[i]] = i 
        return self.construct(inOrder=B, preOrder=A, preOrderStart=0, preOrderEnd=len(A)-1, inOrderStart=0, inOrderEnd=len(B)-1)

    def construct(self, inOrder, preOrder, inOrderStart, inOrderEnd, preOrderStart, preOrderEnd):
        if preOrderStart > preOrderEnd:
            return None
        rootElement = preOrder[preOrderStart]
        root = TreeNode(rootElement)
        length = self.inOrderElementsToIndexMapping.get(root.val) - inOrderStart
        root.left = self.construct(inOrder=inOrder, preOrder=preOrder, preOrderStart=preOrderStart+1, preOrderEnd=preOrderStart+length, inOrderStart=inOrderStart, inOrderEnd=self.inOrderElementsToIndexMapping.get(root.val)-1)
        root.right = self.construct(inOrder=inOrder, preOrder=preOrder, preOrderStart=preOrderStart+length+1, preOrderEnd=preOrderEnd, inOrderStart=self.inOrderElementsToIndexMapping.get(root.val)+1, inOrderEnd=inOrderEnd)
        return root