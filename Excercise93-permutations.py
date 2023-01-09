class Solution:
    def __init__(self):
        self.ans = []
    def permute(self, A):
        self.perm(i=0, n=len(A), arr=A)
        return self.ans
    def perm(self, i, n, arr):
        if i == n:
            self.ans.append(arr.copy())
            return
        
        j = i

        while j < n:
            arr = self.swap(arr, i, j)
            self.perm(i+1, n, arr)
            arr = self.swap(arr, i, j)
            j += 1

    def swap(self, arr, idx1, idx2):
        temp = arr[idx1]
        arr[idx1] = arr[idx2]
        arr[idx2] = temp
        return arr

if __name__ == '__main__':
    print(Solution().permute(A=[1,2,3]))