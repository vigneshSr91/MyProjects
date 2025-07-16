"""
Array of size N. All elements are 0 initially
Q queries 
| index | value |
| 1     | 3     |
| 4     | 2     |
| 2     | 1     |
| 1     | -1    |

Add this value starting from index till the end

Return the final array.
"""

"""
Brute force approach

step 1:
    loop through the queries.
    loop through the array from starting index.
    add the value against each element.

    solution O(Q^N)

optimized approach - Prefix sum
"""

if __name__ == '__main__':
    N = 7
    Q = [[1,3], [4,2], [2,1], [1,-1]]

    pf_sum_arr = [0] * N
    for i in range(len(Q)):
        idx = Q[i][0]
        value = Q[i][1]
        
        pf_sum_arr[idx] += value 
    print(pf_sum_arr)

    answer = []

    for i in range(0,len(pf_sum_arr)):
        if i == 0:
            answer.append(pf_sum_arr[i])
        else:
            answer.append(answer[i-1]+pf_sum_arr[i])

    print(answer)




