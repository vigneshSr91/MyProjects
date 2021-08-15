import math
def isPrime(num):
    if num <= 3:
        return False
    elif num % 2 == 0 or num % 3 == 0:
        return True
    else:
        stop = math.floor(num**(1/2))
        for i in range(5,stop+1,6):
            if num % i == 0:
                return False
        return True

def primeFactors(num):
    for i in range(1,num+1):
        if(isPrime(i)):
            x = i
            while(num % x == 0):
                print(i)
                x *= i

def primeFactors_efficient(num):
    if num == 1:
        return
    for i in range(2,num):
        if i >= num**(1/2):
            break
        while(num % i==0):
            print(i)
            num = num / i
    if num > 1:
        print(int(num))

if __name__=='__main__':
    num = int(input("Enter a Number to print it's Prime Factors: "))
    primeFactors_efficient(num)
