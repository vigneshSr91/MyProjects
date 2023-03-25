"""
Kadanes Algorithm
"""
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        binstr_len = len(A)
        ones = A.count('1')
        if ones == binstr_len: return []

        nums = [0] * binstr_len
        for i in range(binstr_len):
            if A[i] == '0':
                nums[i] =  1
            else:
                nums[i] = -1

        max_total = float('-inf')
        cur_total = 0
        r , l = 0 , 0
        curr_left = 0
        for i in range(len(A)):
            cur_total += nums[i]
           
            if cur_total < 0:
                cur_total = 0
                curr_left = i + 1
                continue
               
            if cur_total > max_total:
                max_total = cur_total
                l = curr_left
                r = i

        l += 1
        r += 1
        return [l,r]
