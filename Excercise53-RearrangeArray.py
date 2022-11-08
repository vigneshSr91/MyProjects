class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        for i in range(len(A)):
            A[i] *= len(A)
        
        for i in range(len(A)):
            idx = A[i]//len(A)
            new_value = A[idx]//len(A)
            A[i] += new_value
        
        for i in range(len(A)):
            A[i] %= len(A) 