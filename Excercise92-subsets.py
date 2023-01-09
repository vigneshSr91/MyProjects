class Solution:
    def __init__(self):
        self.ans = []
    def subsets(self, A):
        A.sort()
        cur = []
        self.getss(A, 0, cur)
        return sorted(self.ans)

    def getss(self, A, i, cur):
        if i== len(A):
            self.ans.append(sorted(cur.copy()))
            return

        cur.append(A[i])

        self.getss(A, i+1, cur)
        cur.pop()
        self.getss(A, i+1, cur)

if __name__ == '__main__':
    print(Solution().subsets([ 12, 13 ]))