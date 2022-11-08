"""
Q1. Balanced Paranthesis

Problem Description

Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.

Refer to the examples for more clarity.



Problem Constraints

1 <= |A| <= 100



Input Format

The first and the only argument of input contains the string A having the parenthesis sequence.



Output Format

Return 0 if the parenthesis sequence is not balanced.

Return 1 if the parenthesis sequence is balanced.



Example Input

Input 1:

 A = {([])}
Input 2:

 A = (){
Input 3:

 A = ()[] 


Example Output

Output 1:

 1 
Output 2:

 0 
Output 3:

 1 


Example Explanation

You can clearly see that the first and third case contain valid paranthesis.

In the second case, there is no closing bracket for {, thus the paranthesis sequence is invalid.



"""

class Solution:
    def solve(self, A):
        paranthesis_list = []
        open_paranthesis = set(['{', '[', '('])
        closed_paranthesis = {'}':'{', ')':'(', ']':'['}
        for i in range(len(A)):
            if A[i] in open_paranthesis:
                paranthesis_list.append(A[i])
            else:
                if A[i] not in closed_paranthesis or len(paranthesis_list) == 0:
                    return 0
                if paranthesis_list[len(paranthesis_list)-1] == closed_paranthesis.get(A[i]):
                    paranthesis_list.pop(len(paranthesis_list)-1)

        if len(paranthesis_list) != 0:
            return 0 # Not Balanced
        else:
            return 1 # Balanced



