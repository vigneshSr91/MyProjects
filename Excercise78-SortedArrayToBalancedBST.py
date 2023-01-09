"""
Sorted Array To Balanced BST

Problem Description

Given an array where elements are sorted in ascending order, convert it to a height Balanced Binary Search Tree (BBST).

Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Problem Constraints

1 <= length of array <= 100000



Input Format

First argument is an integer array A.



Output Format

Return a root node of the Binary Search Tree.



Example Input

Input 1:

 A : [1, 2, 3]
Input 2:

 A : [1, 2, 3, 5, 10]


Example Output

Output 1:

      2
    /   \
   1     3
Output 2:

      3
    /   \
   2     5
  /       \
 1         10


Example Explanation

Explanation 1:

 You need to return the root node of the Binary Tree.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        return self.construct(A)
    def construct(self, lst):
        if len(lst) == 1:
            return TreeNode(lst[0])
        elif len(lst) == 0:
            return None

        idx = len(lst) // 2
        node = TreeNode(lst[idx])
        node.left = self.construct(lst[:idx])
        node.right = self.construct(lst[idx+1:])
        return node

if __name__ == '__main__':
    Solution().sortedArrayToBST([3,7,10,15,19,21,25,32])