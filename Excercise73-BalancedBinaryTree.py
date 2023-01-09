"""
Balanced Binary Tree

Problem Description
Given a root of binary tree A, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Problem Constraints
1 <= size of tree <= 100000



Input Format
First and only argument is the root of the tree A.



Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.



Example Input
Input 1:

    1
   / \
  2   3
Input 2:

 
       1
      /
     2
    /
   3


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

It is a complete binary tree.
Explanation 2:

Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
Difference = 2 > 1. 
"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.notBalanced = False
    def isBalanced(self, A):
        self.getSubTreeNodeCount(A)

        if self.notBalanced == True:
            return 0
        else: 
            return 1
    def getSubTreeNodeCount(self, node):
        if node == None or self.notBalanced == True:
            return 0
        leftDepth = self.getSubTreeNodeCount(node.left)
        rightDepth = self.getSubTreeNodeCount(node.right)

        if max(leftDepth,rightDepth) - min(leftDepth,rightDepth) > 1:
            self.notBalanced = True
        else:
            return 1 + max(leftDepth,rightDepth)

if __name__ == '__main__':
    rootNode = TreeNode(1)
    rootNode.left = TreeNode(2)
    rootNode.right = TreeNode(3)
    print(Solution().isBalanced(rootNode))