class Stack():
    def __init__(self):
        self.stack = []
    
    def top(self):
        return self.stack[len(self.stack)-1]
    
    def pop(self):
        del self.stack[len(self.stack)-1]
    
    def push(self, val):
        self.stack.append(val)
    
    def isEmpty(self):
        return True if len(self.stack) == 0 else False

class MinStack:
    
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        """
        while self.minimumElements.isEmpty() != True and x < self.minimumElements.top():
            self.minimumElements.pop()
        """
        if self.minimumElements.isEmpty() == True or x <= self.minimumElements.top():
            self.minimumElements.push(x)
    # @return nothing
    def pop(self):
        if len(self.stack) < 1:
            return
        if self.minimumElements.top() == self.stack[len(self.stack)-1]:
            self.minimumElements.pop()        
        del self.stack[len(self.stack)-1]

    # @return an integer
    def top(self):
        return self.stack[len(self.stack)-1]

    # @return an integer
    def getMin(self):
        if self.minimumElements.isEmpty() == True:
            return -1
        else:
            return self.minimumElements.top()
    
    def __init__(self):
        self.minimumElements = Stack()
        self.stack = []

if __name__ == '__main__':
    # 19 P 10 P 9 g P 8 g P 7 g P 6 g p g p g p g p g p g
    mStack = MinStack()
    mStack.push(19)
    mStack.push(10)
    mStack.push(9)
    print(mStack.getMin())
    mStack.push(8)
    print(mStack.getMin())
    mStack.push(7)
    print(mStack.getMin())
    mStack.push(6)
    print(mStack.getMin())
    mStack.pop()
    print(mStack.getMin())
    mStack.pop()
    print(mStack.getMin())
    mStack.pop()
    print(mStack.getMin())
    mStack.pop()    
    print(mStack.getMin())
    mStack.pop()   
    print(mStack.getMin())         





