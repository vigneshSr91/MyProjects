"""
Recover Binary Search Tree

Problem Description

Two elements of a binary search tree (BST), represented by root A are swapped by mistake. Tell us the 2 values swapping which the tree will be restored.

A solution using O(n) space is pretty straightforward. Could you devise a constant space solution?

Problem Constraints

1 <= size of tree <= 100000



Input Format

First and only argument is the head of the tree,A



Output Format

Return the 2 elements which need to be swapped.



Example Input

Input 1:

 
         1
        / \
       2   3
Input 2:

 
         2
        / \
       3   1



Example Output

Output 1:

 [2, 1]
Output 2:

 [3, 1]


Example Explanation

Explanation 1:

Swapping 1 and 2 will change the BST to be 
         2
        / \
       1   3
which is a valid BST 
Explanation 2:

Swapping 1 and 3 will change the BST to be 
         2
        / \
       1   3
which is a valid BST 
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 1 2 3 10 7 8 9 4 11
class Solution:
    def recoverTree(self, A):
        currentNode = A
        first = None
        second = None
        prevNode = None

        if currentNode == None:
            return 

        self.recoverTree(currentNode.left)

        if prevNode != None and prevNode.val > currentNode.val:
            if first == None:
                first = prevNode.val
            second = currentNode
        
        prevNode = currentNode

        self.recoverTree(currentNode.right)