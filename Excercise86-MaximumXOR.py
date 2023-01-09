"""
Maximum XOR

Problem Description
Given an array of integers A, find and return the maximum result of A[i] XOR A[j], where i, j are the indexes of the array.



Problem Constraints
1 <= length of the array <= 100000
0 <= A[i] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return an integer denoting the maximum result of A[i] XOR A[j].



Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [5, 17, 100, 11]


Example Output
Output 1:

 7
Output 2:

 117


Example Explanation
Explanation 1:

 Maximum XOR occurs between element of indicies(0-based) 1 and 4 i.e. 2 ^ 5 = 7.
Explanation 2:

 Maximum XOR occurs between element of indicies(0-based) 1 and 2 i.e. 17 ^ 100 = 117.

"""

class NumToBinRepresentation:
    def convert(self, Number):
        temp = Number
        tempResultUnReversed = ""
        while temp > 0:
            if temp == 1:
                tempResultUnReversed += str(temp)
                break
            thisBit = temp % 2
            tempResultUnReversed += str(thisBit)
            temp = temp // 2
        result = tempResultUnReversed[::-1]
        return result

class TreeNode:
    def __init__(self, val):
        self.data = val
        self.childNodes = [None, None]
class Solution:
    def solve(self, A):
        rootNode = TreeNode('#')
        bitsRequired = len(NumToBinRepresentation().convert(max(A)))
        binNumbers =[]
        for i in range(len(A)):
            binRepresentation = NumToBinRepresentation().convert(A[i])
            if len(binRepresentation) < bitsRequired:
                offset = bitsRequired - len(binRepresentation)
                while offset > 0:
                    offset -= 1
                    binRepresentation = "0" + binRepresentation

            binNumbers.append(binRepresentation)
            tempNode = rootNode
        
        # Create the Trie
        for i in range(len(binNumbers)):
            thisNumber = binNumbers[i]
            tempNode = rootNode
            for j in range(len(thisNumber)):
                if thisNumber[j] == "0":
                    if tempNode.childNodes[0] != None:
                        tempNode = tempNode.childNodes[0]
                    else:
                        tempNode.childNodes[0] = TreeNode(0)
                        tempNode = tempNode.childNodes[0]
                else:
                    if tempNode.childNodes[1] != None:
                        tempNode = tempNode.childNodes[1]
                    else:
                        tempNode.childNodes[1] = TreeNode(1)
                        tempNode = tempNode.childNodes[1]
        
        # Finally, find XOR for each Number in binNumbers
        mod = (10**9) + 7
        answer = 0
        for i in range(len(binNumbers)-1):
            xor = 0
            tempNode = rootNode
            for j in range(bitsRequired-1,-1,-1):
                if int(binNumbers[i]) & (1<<j) != 0:
                    if tempNode.childNodes[0] != None:
                        xor |= (1<<j)
                        tempNode = tempNode.childNodes[0]
                    else:
                        tempNode = tempNode.childNodes[1]
                else:
                    if tempNode.childNodes[1] != None:
                        xor |= (1<<j)
                        tempNode = tempNode.childNodes[1]
                    else:
                        tempNode = tempNode.childNodes[0]
                answer = max(xor, answer)
        return answer







if __name__ == '__main__':
    """
    print(NumToBinRepresentation().convert(21))
    print(NumToBinRepresentation().convert(20))
    """
    print(Solution().solve([5, 17, 100, 11]))