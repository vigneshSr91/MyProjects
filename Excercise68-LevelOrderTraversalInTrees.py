
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
    def levelOrder(self, A):
        current = A
        st = queue(10**5)
        st.enqueue(current)
        st.enqueue(None)
        result = []
        thisLevel = []
        while st.size > 1:
            current = st.front()
            st.dequeue()
            if current == None:
                result.append(thisLevel)
                st.enqueue(None)
                thisLevel=[]
                continue
            thisLevel.append(current.val)
            if current.left != None:
                st.enqueue(current.left)
            if current.right != None:
                st.enqueue(current.right)
        result.append(thisLevel)
        return result