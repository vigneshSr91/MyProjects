"""
First non-repeating character

Problem Description

Given a string A denoting a stream of lowercase alphabets, you have to make a new string B. 
B is formed such that we have to find the first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found, append '#' at the end of B.



Problem Constraints

1 <= |A| <= 100000



Input Format

The only argument given is string A.



Output Format

Return a string B after processing the stream of lowercase alphabets A.



Example Input

Input 1:

 A = "abadbc"
Input 2:

 A = "abcabc"


Example Output

Output 1:

"aabbdd"
Output 2:

"aaabc#"


Example Explanation

Explanation 1:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"aba"    -   first non repeating character 'b'
"abad"   -   first non repeating character 'b'
"abadb"  -   first non repeating character 'd'
"abadbc" -   first non repeating character 'd'
Explanation 2:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"abc"    -   first non repeating character 'a'
"abca"   -   first non repeating character 'b'
"abcab"  -   first non repeating character 'c'
"abcabc" -   no non repeating character so '#'


"""
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
"""
class Solution:
    def solve(self, A):
        st_result = Stack()
        st_result.push(A[0])
        st_previous = queue(len(A))
        st_previous.enqueue(A[0])
        repeat = set()
        for i in range(1,len(A)):
            if st_result.top() != A[i]:
                st_result.push(st_result.top())
            else:
                Found = False
                while st_previous.size > 0:
                    if st_previous.front() != A[i]:
                        val = st_previous.front()
                        st_previous.dequeue()
                        if val not in repeat:
                            Found = True
                            break
                    else:
                        st_previous.dequeue()
                if Found != True:
                    st_result.push("#")
                else:
                    st_result.push(val)
            repeat.add(st_result.top())
            st_previous.enqueue(A[i])
        
        st_reverse = Stack()
        while st_result.isEmpty() != True:
            st_reverse.push(st_result.top())
            st_result.pop()

        result = ""
        while st_reverse.isEmpty() != True:
            result += st_reverse.top()
            st_reverse.pop()

        return result
"""

class Solution:
    def solve(self, A):
        Elements = dict()
        q = queue(len(A))
        result = ""
        result += A[0]
        previous = A[0]
        q.enqueue(A[0])
        Elements[A[0]] = 1
        for i in range(1,len(A)):
            try:
                Elements[A[i]] += 1
            except KeyError:
                Elements[A[i]] = 1
            q.enqueue(A[i])
            try:
                while q.size > 0 and Elements[ q.front() ] > 1:
                    q.dequeue()
            except KeyError:
                result += q.front()
                previous = q.front()
                continue
            if q.size == 0:
                result += "#"
                previous = "#"
            else:
                result += q.front()
                previous = q.front()
        return result



if __name__ == "__main__":
    print(Solution().solve(A="jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl"))
