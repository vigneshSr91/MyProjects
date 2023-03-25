"""
Commutable Islands

Problem Description
There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.

We need to find bridges with minimal cost such that all islands are connected.

It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.



Problem Constraints
1 <= A, M <= 6*104

1 <= B[i][0], B[i][1] <= A

1 <= B[i][2] <= 103



Input Format
The first argument contains an integer, A, representing the number of islands.

The second argument contains an 2-d integer matrix, B, of size M x 3 where Island B[i][0] and B[i][1] are connected using a bridge of cost B[i][2].



Output Format
Return an integer representing the minimal cost required.



Example Input
Input 1:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 4]
        [1, 4, 3]
        [4, 3, 2]
        [1, 3, 10]  ]
Input 2:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 2]
        [3, 4, 4]
        [1, 4, 3]   ]


Example Output
Output 1:

 6
Output 2:

 6


Example Explanation
Explanation 1:

 We can choose bridges (1, 2, 1), (1, 4, 3) and (4, 3, 2), where the total cost incurred will be (1 + 3 + 2) = 6.
Explanation 2:

 We can choose bridges (1, 2, 1), (2, 3, 2) and (1, 4, 3), where the total cost incurred will be (1 + 2 + 3) = 6.

"""

class Solution:
    def solve(self, A, B):
        root = []

        for i in range(1,A+1):
            root[i] = i
        
        # sort B(edges) according to weights
        B.sort(key = lambda B:B[2])
        cost = 0
        for row in B:
            if self.union(root, row[0], row[1]):
                cost += row[2]
        
        return cost


    def find(self, root, node):
        if node == root[node]:
            return node
        
        root[node] = self.find(root[node])
        return root[node]

    def union(self, root, node1, node2):
        rootOfNode1 = self.find(root, node1)
        rootOfNode2 = self.find(root, node2)

        if rootOfNode1 != rootOfNode2:
            root[rootOfNode1] = rootOfNode2
            return True
        
        return False



