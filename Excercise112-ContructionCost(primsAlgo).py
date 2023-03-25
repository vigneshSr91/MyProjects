"""
Construction Cost

Problem Description
Given a graph with A nodes and C weighted edges. Cost of constructing the graph is the sum of weights of all the edges in the graph.

Find the minimum cost of constructing the graph by selecting some given edges such that we can reach every other node from the 1st node.

NOTE: Return the answer modulo 109+7 as the answer can be large.

Problem Constraints
1 <= A <= 100000
0 <= C <= 100000
1 <= B[i][0], B[i][1] <= N
1 <= B[i][2] <= 109



Input Format
First argument is an integer A.
Second argument is a 2-D integer array B of size C*3 denoting edges. B[i][0] and B[i][1] are connected by ith edge with weight B[i][2]



Output Format
Return an integer denoting the minimum construction cost.



Example Input
Input 1:

A = 3
B = [   [1, 2, 14]
        [2, 3, 7]
        [3, 1, 2]   ]
Input 2:

A = 3
B = [   [1, 2, 20]
        [2, 3, 17]  ]


Example Output
Output 1:

9
Output 2:

37


Example Explanation
Explanation 1:

We can take only two edges (2 -> 3 and 3 -> 1) to construct the graph. 
we can reach the 1st node from 2nd and 3rd node using only these two edges.
So, the total cost of costruction is 9.
Explanation 2:

We have to take both the given edges so that we can reach the 1st node from 2nd and 3rd node.

"""
import heapq as hq
import math
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):     
        selectedVertex = []
        answer = 0
        for i in range(len(A)):
            selectedVertex.append(0)
        
        selectedVertex[0] = True # as our nodes are numbered from 1->N

        # Adjacency Matrix
        graph = [[0] * A for i in range(B)]

        for i in B:
            u, v, w = i[0], i[1], i[2]

            graph[u-1][v-1] = w
            graph[v-1][u-1] = w        

        No_Of_Edges = 0 # initialize the No. Of Edges covered. In MST, this number can go upto 1-No. Of Vertices
        nextVertex = 0
        while No_Of_Edges < (A - 1):
            minCost = math.inf
            for i in range(A):
                if selectedVertex[i]:
                    for j in range(B):
                        if ((not selectedVertex[j]) and graph[i][j]):
                            if minCost > graph[i][j]:
                                minCost = graph[i][j]
                                nextVertex = j
            if minCost != math.inf:
                answer += minCost
            selectedVertex[nextVertex] = True
            No_Of_Edges += 1
        
        return answer


