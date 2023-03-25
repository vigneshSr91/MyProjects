from queue import PriorityQueue
import math
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        answer = [math.inf for i in range(A)]
        answer[C] = 0

        # Visited Array
        visited =[False for i in range(A)]

        # Adjacency list
        graph=[]
        for i in range(A):
            graph.append([])

        
        for i in B:
            u, v, w = i[0], i[1], i[2]

            graph[u].append([w,v])
            graph[v].append([w,u])
        
        q = PriorityQueue()
        q.put([0, C])
        while not q.empty():
            thisDistance, Node = q.get()
            if visited[Node] == True:
                continue
            visited[Node] = True
            if thisDistance == answer[Node]:
                for i in graph[Node]:
                    w, v = i
                    if answer[v] > answer[Node] + w:
                        answer[v] = answer[Node] + w
                        q.put([answer[v], v])
        for i in range(A):
            if answer[i] == math.inf:
                answer[i] = -1
        return answer