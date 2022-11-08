"""
Perfect Numbers


Problem Description

Given an integer A, you have to find the Ath Perfect Number.

A Perfect Number has the following properties:

It comprises only 1 and 2.

The number of digits in a Perfect number is even.

It is a palindrome number.

For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.



Problem Constraints

1 <= A <= 100000



Input Format

The only argument given is an integer A.



Output Format

Return a string that denotes the Ath Perfect Number.



Example Input

Input 1:

 A = 2
Input 2:

 A = 3


Example Output

Output 1:

 22
Output 2:

 1111


Example Explanation

Explanation 1:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
Explanation 2:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221

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
        self.size -= 1

    def front(self):
        return self.thisQueue[(self.f + 1) % self.capacity]

class Solution:
    def solve(self, A):
        q = queue(capacity=100000)
        q.enqueue("11")
        q.enqueue("22")
        c = 0
        while c < A-1:
            thisElement = q.front()
            q.dequeue()
            q.enqueue(str(thisElement[0:len(thisElement)//2]) + "11" + str(thisElement[len(thisElement)//2:len(thisElement)]))
            q.enqueue(str(thisElement[0:len(thisElement)//2]) + "22" + str(thisElement[len(thisElement)//2:len(thisElement)]))

            c += 1
        return q.front()

if __name__ == "__main__":
    print(Solution().solve(A=3))