# Beggars outside temple

# Array of size N. All elements are zero.
# Q queries -> {index, value}
# Add this 'value' starting from 'index' till end.


class beggarsOutsideTemple():
    def solve(self):
        # # calculate the pre-fix sum array
        # pf_array = [A[0]]
        # for i in range(1,len(A)):
        #     pf_array.append(A[i-1] + A[i])

        # # answer the queries
        # for i in range(len(Q)):
        #     start = Q[i][0]
        #     end = Q[i][1]
        N = int(input())
        A = [0] * N

        keys = list(map(int, input().split(',')))
        values = list(map(int, input().split(',')))

        queries = dict()
        for i in range(len(keys)):
            if keys[i] in queries:
                queries[keys[i]] += values[i]
            else:
                queries[keys[i]] = values[i]

        for i in range(N):
            if i in queries:
                A[i] += queries[i]
        
        # now calculate prefix sum
        result = []
        result.append(A[0])
        for i in range(1,len(A)):
            result.append(result[i-1] + A[i] )

        print(result)


if __name__ == '__main__':
    beggarsOutsideTemple().solve()

