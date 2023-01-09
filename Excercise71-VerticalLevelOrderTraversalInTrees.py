"""
Vertical Order traversal

Problem Description
Given a binary tree, return a 2-D array with vertical order traversal of it. Go through the example and image for more details.

Problem Constraints
0 <= number of nodes <= 10^5

Input Format
First and only arument is a pointer to the root node of binary tree, A.



Output Format
Return a 2D array denoting the vertical order traversal of tree as shown.

Example Input
Input 1:

      6
    /   \
   3     7
  / \     \
 2   5     9
Input 2:

      1
    /   \
   3     7
  /       \
 2         9


Example Output
Output 1:

 [
    [2],
    [3],
    [6, 5],
    [7],
    [9]
 ]
Output 2:

 [
    [2],
    [3],
    [1],
    [7],
    [9]
 ]

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
    def verticalOrderTraversal(self, A):
        levelMap = dict()
        currentNode = A
        currentLevel = 0
        minLevel = 0
        maxLevel = 0
        q = queue(10**5)
        q.enqueue((currentNode, currentLevel))

        while q.size > 0:
            currentNode = q.front()[0]
            currentLevel = q.front()[1]
            q.dequeue()
            if currentLevel in levelMap:
                elements = levelMap[currentLevel]
                elements.append(currentNode.val)
                levelMap[currentLevel] = elements
            else:
                levelMap[currentLevel] = [currentNode.val]

            if currentNode.left != None:
                q.enqueue((currentNode.left, currentLevel-1))
            if currentNode.right != None:
                q.enqueue((currentNode.right, currentLevel+1))
            
            minLevel = min(minLevel,currentLevel)
            maxLevel = max(maxLevel,currentLevel)
        result=[]
        for i in range(minLevel,maxLevel+1):
            if i in levelMap:
                thisLevelResult = levelMap.get(i)
                result.append(thisLevelResult)
        return result

if __name__ == '__main__':
    rootNode = TreeNode(3)
    rootNode.left = TreeNode(924)
    print(Solution().verticalOrderTraversal(rootNode))