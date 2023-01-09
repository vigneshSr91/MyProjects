"""
Deserialize Binary Tree

Problem Description
You are given an integer array A denoting the Level Order Traversal of the Binary Tree.

You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.

NOTE:

In the array, the NULL/None child is denoted by -1.
For more clarification check the Example Input.


Problem Constraints
1 <= number of nodes <= 105

-1 <= A[i] <= 105



Input Format
Only argument is an integer array A denoting the Level Order Traversal of the Binary Tree.



Output Format
Return the root node of the Binary Tree.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
Input 2:

 A = [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]


Example Output
Output 1:

           1
         /   \
        2     3
       / \
      4   5
Output 2:

            1
          /   \
         2     3
        / \ .   \
       4   5 .   6


Example Explanation
Explanation 1:

 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3, 4 and 5 each has both NULL child we had represented that using -1.
Explanation 2:

 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3 has left child as NULL while 4 and 5 each has both NULL child.


"""
class queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.thisQueue = [None] * self.capacity
        self.size = 0
        self.f = -1
        self.r = -1
    def enqueue(self,val):
        if self.size == self.capacity:
            return -1
        self.r = (self.r+1) % self.capacity
        self.thisQueue[self.r] = val
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        
        self.f = (self.f + 1) % self.capacity
        temp = self.thisQueue[self.f]
        self.size -= 1
        return temp

    def front(self):
        return self.thisQueue[(self.f + 1) % self.capacity]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self, A):
        if len(A) == 1:
            return TreeNode(A[0])
        rootNode = TreeNode(A[0])
        self.q = queue(10**5)
        self.q.enqueue(rootNode)
        i=1
        while self.q.front() != None:
            tempNode = self.q.dequeue()

            if A[i] != -1:
                tempNode.left = TreeNode(A[i])
                self.q.enqueue(tempNode.left)
            i += 1

            if A[i] != -1:
                tempNode.right = TreeNode(A[i])
                self.q.enqueue(tempNode.right)
            i += 1

            if i >= len(A):
                break
        return rootNode
if __name__ == '__main__':
    rootNode = Solution().solve(A=[ 1, 2, 3, 4, 5, -1, -1, -1, -1, -1, 6, -1, -1 ])