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
        self.size -= 1

    def front(self):
        return self.thisQueue[(self.f + 1) % self.capacity]

class Solution:
    def solve(self, A, B):
        requestedQueue = queue(len(B))
        for i in range(len(B)):
            requestedQueue.enqueue(B[i])
        
        givenQueue = queue(len(A))

        for i in range(len(A)):
            givenQueue.enqueue(A[i])

        count = 0
        while requestedQueue.size != 0 and givenQueue.size != 0:
            if requestedQueue.front() == givenQueue.front():
                givenQueue.dequeue()
                requestedQueue.dequeue()
            else:
                thisElement = givenQueue.front()
                givenQueue.dequeue()
                givenQueue.enqueue(thisElement)
            count += 1
        return count
        