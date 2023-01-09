"""
Right View of Binary tree

Problem Description
Given a binary tree of integers denoted by root A. Return an array of integers representing the right view of the Binary tree.

Right view of a Binary Tree is a set of nodes visible when the tree is visited from Right side.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return an array, representing the right view of the binary tree.



Example Input
Input 1:

 
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Input 2:

 
            1
           /  \
          2    3
           \
            4
             \
              5


Example Output
Output 1:

 [1, 3, 7, 8]
Output 2:

 [1, 3, 4, 5]


Example Explanation
Explanation 1:

Right view is described.
Explanation 2:

Right view is described.

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

class Solution:
    def levelOrder(self, A):
        current = A
        st = queue(10**5)
        st.enqueue(current)
        st.enqueue(None)
        result = []
        previous = current.val
        while st.size > 1:
            current = st.front()
            st.dequeue()
            if current == None:
                st.enqueue(None)
                result.append(previous)
                continue
            previous = current.val
            if current.left != None:
                st.enqueue(current.left)
            if current.right != None:
                st.enqueue(current.right)
        result.append(current.val)
        return result