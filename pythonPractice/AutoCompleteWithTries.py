"""
Problem Description
There is a dictionary A of N words, and ith word has a unique weight Wi.

Another string array B of size M contains the prefixes. For every prefix B[i], output atmost 5 words from the dictionary A that start with the same prefix.

Output the words in decreasing order of their weight.

NOTE: If there is no word that starts with the given prefix output -1.
"""
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.childNodes = [None] * 26
        self.weight = list()
class searchNodesForWeightsOfAllWords:
    def __init__(self):
        self.answer = []
        
    def solve(self, node: Node):
        
        if node != None:
            if len(node.weight) >= 1:
                self.answer.extend(node.weight)
            if len(node.childNodes) == 0:
                return
            else:
                for i in range(len(node.childNodes)):
                    nextNode = node.childNodes[i]
                    self.solve(nextNode)

def insert(rootNode, word, weight):
    currentNode = rootNode
    for i in range(len(word)):
        idx = ord(word[i]) - ord('a')

        if currentNode.childNodes[idx] == None:
            newNode = Node(word[i])
            currentNode.childNodes[idx] = newNode
        currentNode = currentNode.childNodes[idx]


    currentNode.weight.append(weight)

    return rootNode



def searchTopFiveWordsWithPrefix(prefix, rootNode, wordForWeight):
    currentNode = rootNode
    topFiveWords = []
    # traverse till the prefix node
    for i in range(len(prefix)):
        idx = ord(prefix[i]) - ord('a')
        if currentNode.childNodes[idx] == None:
            return []
        currentNode = currentNode.childNodes[idx]

    # now recursively find all words with weights
    nodeScanner = searchNodesForWeightsOfAllWords()
    nodeScanner.solve(currentNode)
    nodeScanner.answer.sort(reverse=True)

    TopFiveWeights = nodeScanner.answer[0:5]

    for weight in TopFiveWeights:
        topFiveWords.append(wordForWeight[weight])
    
    return topFiveWords


def main(N, M, words, weights, prefixes):
    # create the root/dummy node as first step
    rootNode = Node("#")
    for i in range(len(words)):
        word = words[i]
        weight = weights[i]
        insert(rootNode, word, weight)

    wordForWeight = dict()
    for i in range(len(words)):
        weight = weights[i]
        wordForWeight[weight] = words[i]

    for i in range(len(prefixes)):
        prefix = prefixes[i]
        currentAnswer = searchTopFiveWordsWithPrefix(prefix, rootNode, wordForWeight)
        if len(currentAnswer) == 0:
            print(-1, end='')
        for word in currentAnswer:
            print(word + " ", end = '')
        
        print()
    return 0

if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        nextLine = str(input()).split()
        N = nextLine[0]
        M = nextLine[1]

        nextLine = str(input()).split()
        words = nextLine

        nextLine = str(input()).split()
        weights = []
        for element in nextLine:
            weights.append(int(element))
        
        nextLine = str(input()).split()
        prefixes = []
        for element in nextLine:
            prefixes.append(element)
        
        main(N, M, words, weights, prefixes)




