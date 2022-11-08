"""
N integers containing only 1, 2 & 3

Problem Description

Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.

NOTE: All the A integers will fit in 32-bit integers.



Problem Constraints

1 <= A <= 29500



Input Format

The only argument given is integer A.



Output Format

Return an integer array denoting the first positive A integers in ascending order containing only digits 1, 2 and 3.



Example Input

Input 1:

 A = 3
Input 2:

 A = 7


Example Output

Output 1:

 [1, 2, 3]
Output 2:

 [1, 2, 3, 11, 12, 13, 21]


Example Explanation

Explanation 1:

 Output denotes the first 3 integers that contains only digits 1, 2 and 3.
Explanation 2:

 Output denotes the first 3 integers that contains only digits 1, 2 and 3.


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
        q = queue(A)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        count = 3
        result = [1,2,3]
        while count <= A:
            thisElement = q.front()
            q.dequeue
            q.enqueue(thisElement * 10 + 1)
            q.enqueue(thisElement * 10 + 2)
            q.enqueue(thisElement * 10 + 3)

            result.extend([thisElement * 10 + 1, thisElement * 10 + 2, thisElement * 10 + 3])
            count += 3
        
        return result[0:A-1]

if __name__ == '__main__':
    print(Solution().solve(7))