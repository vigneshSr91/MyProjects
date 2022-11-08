import math
class node():
    def __init__(self, val):
        self.val        = val
        self.next       = None
        self.previous   = None

class deque():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_rear(self, val):
        newNode = node(val)
        if self.head == None and self.tail == None:
            self.head = newNode
        elif self.tail == None and self.head != None:
            self.head.next = newNode
            self.tail = self.head.next
            self.tail.previous = self.head
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = self.tail.next
    
    def pop_rear(self):
        if self.tail == None and self.head != None:
            self.head = None
            return
        self.tail = self.tail.previous
        if self.tail != None:
            self.tail.next = None
    
    def peek_rear(self):
        if self.tail == None and self.head != None:
            return self.head.val
        elif self.tail != None:
            return self.tail.val
        else:
            return math.inf
    
    def pop_front(self):
        self.head = self.head.next
        self.head.previous = None
    
    def peek_front(self):
        return self.head.val

class Solution:
    def slidingMaximum(self, A, B):
        result = []
        dq = deque()
        dq.push_rear(A[0])
        for i in range(1,B):
            while A[i] > dq.peek_rear():
                dq.pop_rear()
            dq.push_rear(A[i])
        result.append(dq.peek_front())
        for i in range(B,len(A)):
            while A[i] > dq.peek_rear():
                dq.pop_rear()
            dq.push_rear(A[i])
            if dq.peek_front() == A[i-B]:
                dq.pop_front()

            result.append(dq.peek_front())
        
        return result

if __name__ == '__main__':
    print(Solution().slidingMaximum(A=[10,1,8,9,7,6,5,11,3],B=3))

        

