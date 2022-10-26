class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        result_array_len = (len(A) + len(B))
        if result_array_len % 2 == 0:
            is_even = True
        else:
            is_even = False
        
        if is_even == True:
            required_index = [result_array_len//2, (result_array_len//2)+1]
        else:
            required_index = [(result_array_len//2)+1]
        
        min_len_of_array_required = max(required_index)
        p1 = 0
        p2 = 0
        len_covered = 0
        result=[]
        answer = 0
        while p1 < len(A) and p2 < len(B):
            if len_covered > min_len_of_array_required:
                break
            if A[p1] < B[p2]:
                result.append(A[p1])
                p1 += 1
                len_covered += 1
            elif A[p1] == B[p2]:
                result.append(A[p1])
                result.append(B[p2])
                p1 += 1
                p2 += 1
                len_covered += 2
            else:
                result.append(B[p2])
                p2 += 1
                len_covered += 1
        
        while p1 < len(A):
            if len_covered > min_len_of_array_required:
                break
            result.append(A[p1])
            len_covered += 1
            p1 += 1
        while p2 < len(B):
            if len_covered > min_len_of_array_required:
                break
            result.append(B[p2])
            len_covered += 1
            p2 += 1

        if len_covered >= min_len_of_array_required:
            for i in required_index:
                answer += result[i-1]
        if is_even == True:
            return answer / 2.0
        else:
            return answer / 1.0

if __name__ == '__main__':
    print(Solution().findMedianSortedArrays(A=[],B=[20]))