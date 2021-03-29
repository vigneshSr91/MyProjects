def Func(n):
    for i in range(1,n):
        j=i
        while j<i*i:
            j=j+1
            if(j%i==0):
                for k in range(0,j):
                    print("Test")

def CalculateTimeComplexity():
    return

# Driver code
if(__name__=="__main__"):
    Func(3)