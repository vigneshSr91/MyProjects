import math
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        l0 = 0
        hi = len(A)
        while l0 <= hi:
            cut1 = ( l0 + hi ) // 2
            cut2 = ( ( len(A) + len(B) ) // 2 ) - cut1

            l1 = -math.inf if cut1==0 else A[cut1-1]
            l2 = -math.inf if cut2==0 else B[cut2-1]
            r1 = math.inf if cut1==len(A) else A[cut1]
            r2 = math.inf if cut2==len(B) else B[cut2]

            if l1 > r2:
                hi = cut1-1
            elif l2 > r1:
                l0 = cut1+1
            else:
                return (max(l1,l2)+min(r1,r2))/ 2 if (len(A) + len(B)) % 2 == 0 else min(r1,r2)


