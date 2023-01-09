"""
Serialize Binary Tree
Problem Description
Given the root node of a Binary Tree denoted by A. You have to Serialize the given Binary Tree in the described format.

Serialize means encode it into a integer array denoting the Level Order Traversal of the given Binary Tree.

NOTE:

In the array, the NULL/None child is denoted by -1.
For more clarification check the Example Input.


Problem Constraints
1 <= number of nodes <= 105



Input Format
Only argument is a A denoting the root node of a Binary Tree.



Output Format
Return an integer array denoting the Level Order Traversal of the given Binary Tree.



Example Input
Input 1:

           1
         /   \
        2     3
       / \
      4   5
Input 2:

            1
          /   \
         2     3
        / \     \
       4   5     6


Example Output
Output 1:

 [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
Output 2:

 [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]


Example Explanation
Explanation 1:

 The Level Order Traversal of the given tree will be [1, 2, 3, 4, 5 , -1, -1, -1, -1, -1, -1].
 Since 3, 4 and 5 each has both NULL child we had represented that using -1.
Explanation 2:

 The Level Order Traversal of the given tree will be [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1].
 Since 3 has left child as NULL while 4 and 5 each has both NULL child.


"""

class queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.thisQueue = []
        self.size = 0
        self.f = -1
        self.r = -1
    def enqueue(self,val):
        if self.size == self.capacity:
            return -1
        self.r = (self.r+1) % self.capacity
        self.thisQueue.append(val)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        self.f = (self.f + 1) % self.capacity
        self.size -= 1

    def front(self):
        return self.thisQueue[(self.f + 1) % self.capacity]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def solve(self, A):
		current = A
		q = queue(10**5)
		q.enqueue(current)
		q.enqueue(None)
		result=[]
		thisLevel=[]
		while q.size > 1:
			current = q.front()
			q.dequeue()
			
			if current == None:
				result.extend(thisLevel)
				thisLevel=[]
				q.enqueue(None)
			else:
				thisLevel.append(current.val)
				if current.left != None:
					q.enqueue(current.left)
				elif current.val != -1:
					q.enqueue(TreeNode(-1))
				if current.right != None:
					q.enqueue(current.right)
				elif current.val != -1:
					q.enqueue(TreeNode(-1))
		result.extend(thisLevel)
		return result
          

if __name__ == '__main__':
	rootNode = TreeNode(1)
	newNode = TreeNode(2)
	rootNode.left = newNode
	newNode = TreeNode(3)
	rootNode.right = newNode
	TempNode = rootNode.left # 2
	newNode = TreeNode(4)
	TempNode.left = newNode
	newNode = TreeNode(5)
	TempNode.right = newNode
	TempNode = TempNode.right
	TempNode.right = TreeNode(6)

	print(Solution().solve(rootNode))