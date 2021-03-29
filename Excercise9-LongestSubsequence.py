# Given an array A of integers, return the length of the longest arithmetic subsequence in A
def ckeckListElementsAreSame(lst): 
  
    ele = lst[0] 
    chk = True
      
    # Comparing each element with first item  
    for item in lst: 
        if ele != item: 
            chk = False
            break; 
              
    if (chk == True): 
        return True
    else: 
        return False   
  
def findLCS(listA, listB):
    # find the length of the strings 
    m = len(listA) 
    n = len(listB) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n + 1) for i in range(m + 1)] 
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif listA[i-1] == listB[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
# end of function lcs 


if(__name__=='__main__'):
    InputString = str(input())
    
    listA = [int(x) for x in InputString.split(',')]
    if ckeckListElementsAreSame(listA):
        print(len(listA))
    else:
        listB = list(range(max(listA) + 1))
        listC = listA.copy()[::-1]

        print(max(findLCS(listA, listB), findLCS(listC, listB)))
