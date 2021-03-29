import math
def power(a,b):
    if(b==1):
        return a
    if(b%2==0):
        tmp = power(a, b/2)
        return  tmp * tmp
    if(b%2>0):
        tmp = power(a, math.floor(b/2))
        return a * tmp * tmp
    

if(__name__ == '__main__'):
    a = int(input())
    b = int(input())
    print(power(a,b))
