class Solution:
    def smallestPrefix(self, A, B):
        """
        elementsHash = dict()

        for i in range(len(A)):
            elementsHash[ord(A[i])] = A[i]
        """
        for i in range(len(A)-1,-1,-1):
            if ord(B[0]) > ord(A[i]):
                return A[:i+1] + B[0]

if __name__ == '__main__':
    A = "harry"
    B = "potter"
    print(Solution().smallestPrefix(A, B))