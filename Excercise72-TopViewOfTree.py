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
    def solve(self, A):
        levelMap = dict()
        levelMap[0] = [A.val]
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
            if currentLevel > maxLevel or currentLevel < minLevel:
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
                result.extend(thisLevelResult)
        return result
