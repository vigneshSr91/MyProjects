"""
Path in Directed Graph

Problem Description
Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B of size M x 2such that there is a edge directed from node

B[i][0] to node B[i][1].

Find whether a path exists from node 1 to node A.

Return 1 if path exists else return 0.

NOTE:

There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.


Problem Constraints
2 <= A <= 105

1 <= M <= min(200000,A*(A-1))

1 <= B[i][0], B[i][1] <= A



Input Format
The first argument given is an integer A representing the number of nodes in the graph.

The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].



Output Format
Return 1 if path exists between node 1 to node A else return 0.



Example Input
Input 1:

 A = 5
 B = [  [1, 2] 
        [4, 1] 
        [2, 4] 
        [3, 4] 
        [5, 2] 
        [1, 3] ]
Input 2:

 A = 5
 B = [  [1, 2]
        [2, 3] 
        [3, 4] 
        [4, 5] ]


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 The given doens't contain any path from node 1 to node 5 so we will return 0.
Explanation 2:

 Path from node1 to node 5 is ( 1 -> 2 -> 3 -> 4 -> 5 ) so we will return 1.


"""
from collections import deque
class SolutionBFS:
    def solve(self, A, B):

        # 1. Adjacency List
        adj_list = []
        for i in range(A+1):
            adj_list.append([])
        edges = len(B)
        for i in range(edges):
            u = B[i][0]
            v = B[i][1]
            adj_list[u].append(v)
        # 2. Initialize visited array
        visited=[False] * (A+1)
        # 3. Start Breadth First Search
        q = deque()                         # Use queue DS for FIFO
        q.append(1)                         # Start from source node

        while len(q) > 0:
            for i in range(len(q)):
                currentNode = q.popleft()
                nodes = adj_list[currentNode]
                for j in range(len(nodes)):
                    if visited[nodes[j]] == False:
                        q.append(nodes[j])
                        visited[nodes[j]] = True
        
        if visited[A]:
            return 1
        return 0


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        # 1. Adjacency List
        graph = []                              # Intialize
        for i in range((A+1)):                  # Create the adjacency list for each Node
            graph.append([])

        for i in range(len(B)):                 # For each given Edge,
            u = B[i][0]                         # If unidirected u<->v
            graph[u].append(B[i][1])            # If directed u->v

        # 2. Initialize the visited array
        visited = []
        for i in range(A + 1):
            visited.append(False)

        self.depthFirstSearch(graph, visited, 1)    # Start DFS from Node 1

        if visited[A] == False:                     # Finally, if the destination node was Visited, return True
            return 0
        else:
            return 1

    def depthFirstSearch(self, graph, visited, node):
        visited[node] = True

        for i in range(len(graph[node])):
            v = graph[node][i]
            if visited[v] == False:
                self.depthFirstSearch(graph, visited, v)




if __name__ == '__main__':
    A = 5
    B = [  [1, 2],
        [2, 3] ,
        [3, 4] ,
        [4, 5] ]
    print(Solution().solve(A,B))
        