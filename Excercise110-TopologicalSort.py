from collections import deque
class Solution:
    def solve(self, A, B):
        graph = []
        for i in range(A):
            graph.append([])

        for i in range(len(B)):
            u = B[i][0]
            graph[u].append(B[i][1])

        inDegree=[]
        for i in range(A+1):
            inDegree.append(0)
        
        answer=[]
        for i in range(len(B)):
            inDegree[B[1]] += 1
        q = deque()
        for i in range(1,A+1):
            if inDegree[i] == 0:
                q.append(i)
                

        while len(q) > 0:
            u = q.popleft()
            answer.append(i)
            for i in range(len(graph[u])):
                v = graph[u][i]
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
        return answer
        
        



