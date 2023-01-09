"""
Shortest Unique Prefix

Problem Description

Given a list of N words, find the shortest unique prefix to represent each word in the list.

NOTE: Assume that no word is the prefix of another. In other words, the representation is always possible



Problem Constraints

1 <= Sum of length of all words <= 106



Input Format

First and only argument is a string array of size N.



Output Format

Return a string array B where B[i] denotes the shortest unique prefix to represent the ith word.



Example Input

Input 1:

 A = ["zebra", "dog", "duck", "dove"]
Input 2:

A = ["apple", "ball", "cat"]


Example Output

Output 1:

 ["z", "dog", "du", "dov"]
Output 2:

 ["a", "b", "c"]


Example Explanation

Explanation 1:

 Shortest unique prefix of each word is:
 For word "zebra", we can only use "z" as "z" is not any prefix of any other word given.
 For word "dog", we have to use "dog" as "d" and "do" are prefixes of "dov".
 For word "du", we have to use "du" as "d" is prefix of "dov" and "dog".
 For word "dov", we have to use "dov" as "d" and do" are prefixes of "dog".  
 
Explanation 2:

 "a", "b" and c" are not prefixes of any other word. So, we can use of first letter of each to represent.


"""
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.childnodes=[None] * 26
        self.isEnd = False
        self.counter = 0

class Solution:
    def prefix(self, A):
        self.rootNode = TreeNode('#')

        for i in range(len(A)):
            self.insert(A[i])

        result = []
        for i in range(len(A)):
            result.append(self.getUniquePrefix(A[i]))
        
        return result

    def getUniquePrefix(self, word):
        answer=""
        tempNode = self.rootNode
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            tempNode = tempNode.childnodes[idx]
            if tempNode.counter > 1:
                answer += tempNode.val
            elif tempNode.counter == 1:
                return answer + tempNode.val


    def insert(self, word):
        tempNode = self.rootNode
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if tempNode.childnodes[idx] == None:
                newNode = TreeNode(word[i])
                tempNode.childnodes[idx] = newNode
            tempNode = tempNode.childnodes[idx]
            tempNode.counter += 1
        tempNode.isEnd = True
    
    def search(self, word):
        tempNode = self.rootNode
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')    
            if tempNode.childnodes[idx] == None:
                return False
            tempNode = tempNode.childnodes[idx]
        if tempNode.isEnd == True:
            return True
        else:
            return False
             


    

