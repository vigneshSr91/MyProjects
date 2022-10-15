import re


class Solution:
    # @param A : list of integers
    # @return a list of integers
    """
    00 - 0
    01 - 1
    10 - 2
    11 - 3
    100 - 4
    101 - 5
    110 - 6
    111 - 7
    1000 - 8
    1001 - 9
    """
    def plusOne(self, A):
        pointer_A = len(A)-1
        carryForward = 0
        index = 0
        result = []
        while index <= len(A):
            thisNumber = 0
            if pointer_A >= 0:
                thisNumber = A[pointer_A]
                if carryForward == 0 and index == 0:
                    thisNumber = thisNumber + 1
                elif index > 0 and carryForward == 0:
                    thisNumber = A[pointer_A]
                else:
                    thisNumber += carryForward
                    carryForward = 0
                if thisNumber > 9:
                    thisNumber = 0
                    carryForward = 1
                result.append(thisNumber)
            else:
                result.append(carryForward)
                carryForward = 0
            index += 1
            pointer_A -= 1
        result = result[::-1]
        while result[0] == 0:
            result.pop(0)
        return result


     

if __name__ == "__main__":
    print(Solution().plusOne(A=[0, 3, 7, 6, 4, 0, 5, 5, 5]))
