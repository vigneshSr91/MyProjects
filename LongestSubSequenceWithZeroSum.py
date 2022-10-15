class Solution():
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        pf_sum_of_A = []
        pf_sum_of_A.append(A[0])

        for i in range(1, len(A)):
            pf_sum_of_A.append(A[i]+pf_sum_of_A[i-1])

        pf_hashmap = {}

        for i in range(len(pf_sum_of_A)):
            pf_hashmap[pf_sum_of_A[i]] = i

        lengthOfTheSequence = 0
        answer = []
        for i in range(len(pf_sum_of_A)):
            lastPosition = pf_hashmap[pf_sum_of_A[i]]

            if lengthOfTheSequence < (lastPosition - i) and pf_sum_of_A[i] != 0:
                answer = A[i+1: lastPosition+1]
                lengthOfTheSequence = len(answer)
            elif pf_sum_of_A[i] == 0 and lengthOfTheSequence < i+1:
                answer = A[0:i+1]
                lengthOfTheSequence = len(answer)

        return answer

if __name__=='__main__':
    print(Solution().lszero(A=[ 1, 2, -3, 3 ]))
