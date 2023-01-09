"""
Cycle in Undirected Graph

Problem Description

Given an undirected graph having A nodes labelled from 1 to A with M edges given in a form of matrix B of size M x 2 where (B[i][0], B[i][1]) represents two nodes B[i][0] and B[i][1] connected by an edge.

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain atleast three nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.


Problem Constraints

1 <= A, M <= 3*105

1 <= B[i][0], B[i][1] <= A



Input Format

The first argument given is an integer A representing the number of nodes in the graph.

The second argument given is an matrix B of size M x 2 which represents the M edges such that there is a edge between node B[i][0] and node B[i][1].



Output Format

Return 1 if cycle is present else return 0.



Example Input

Input 1:

 A = 5
 B = [  [1. 2]
        [1, 3]
        [2, 3]
        [1, 4]
        [4, 5]
     ]
Input 2:

 A = 3
 B = [  [1. 2]
        [1, 3]
     ]


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 There is a cycle in the graph i.e 1 -> 2 -> 3 -> 1 so we will return 1
Explanation 2:

 No cycle present in the graph so we will return 0.


"""

class Solution:
    def solve(self, A, B):
        graph = []
        for i in range(A + 1):
            graph.append([])

        for i in range(len(B)):
            u = B[i][0]
            graph[u].append(B[i][1])
            
            v = B[i][1]
            graph[v].append(B[i][0])
        
        visited = []
        for i in range(A + 1):
            visited.append(False)
        components = 0
        for i in range(1, len(A+1)):
            if visited[i] == False:
                self.depthFirstSearch(graph, visited, i, 1)
                components += 1
        
        if len(B) > A-components:
            return 1
        return 0




    def depthFirstSearch(self, graph, visited, node):
        if visited[node] == True:
            return        
        visited[node] = True
        
        for i in range(len(graph[node])):
            v = graph[node][i]
            self.depthFirstSearch(graph, visited, v)