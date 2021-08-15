def CheckIsPrime_Iterative(num):
    if num <= 1:
        return False
    i = 2
    while(i<num):
        if(num % i==0):
            return False
        i += 1
    return True

def CheckIsPrime_sqrtOfN_TimeComplexity(num):
    if num<=1:
        return False
    i=2
    while(i*i <= num):
        if(num % i == 0):
            return False
        i += 1
    return True

def CheckIsPrime_Optimized(num):
    if num==1:
        return False
    if num==2 or num==3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i=5
    while(i*i <= num):
        if(num % i == 0):
            return False
        i += 6
    return True

if __name__=='__main__':
    num = int(input("Enter a Number to check if it Prime: "))
    if CheckIsPrime_Optimized(num):
        print("The Number {num} is Prime".format(num=num))
    else:
        print("The Number {num} is not Prime".format(num=num))