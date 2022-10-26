"""
        HashSet<Integer> list = new HashSet<>();
        for(int i = 0; i < A.size(); i++){
            int sq = (int) Math.sqrt(A.get(i));
            for(int j = 2; j <= sq; j++){
                if(A.get(i) % j == 0){
                    list.add(j);
                    while(A.get(i) % j == 0){
                        A.set(i, A.get(i) / j);
                    }
                }
            }
            if(A.get(i) > 1){
                list.add(A.get(i));
            }
        }
        return list.size();
"""
import math
class solution():
    def distincPrimes(self,A):
        hashSet = set()
        for i in range(len(A)):
            sqrt  = int(math.sqrt(A[i]))
            for j in range(2,sqrt+1):
                if A[i] % j == 0:
                    hashSet.add(j)
                    while A[i] % j == 0:
                        A[i] //= j
            if A[i] > 1:
                hashSet.add(A[i])
        return len(hashSet)

if __name__ == '__main__':
    print(solution().distincPrimes(A=[1, 2, 3, 4]))
