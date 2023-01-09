import math
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

class Solution:
    def evalRPN(self, A):
        OperatorHashSet = {"+", "-", "*", "/" }
        stOperands = Stack()
        for i in range(len(A)):
            if A[i] in OperatorHashSet:
                if stOperands.isEmpty( ) != True:
                    operand1 = int(stOperands.top())
                    stOperands.pop()
                if stOperands.isEmpty( ) != True:
                    operand2 = int(stOperands.top())
                    stOperands.pop()
                if A[i] == "+":
                    val = operand1 + operand2
                elif A[i] == "-":
                    val = operand2 - operand1
                elif A[i] == "*":
                    val = operand1 * operand2
                elif A[i] == "/":
                    val = operand2 // operand1
                else:
                    return -1
                stOperands.push(val)
            else:
                stOperands.push(A[i])
        return stOperands.top()

if __name__ == "__main__":
    print(Solution().evalRPN(A=["4", "13", "5", "/", "+"]))
    print(Solution().evalRPN(A=["2", "1", "+", "3", "*"]))