import math
def checkIsPrime_Naive(num):
    if num <= 1:
        return "{num} is not prime".format(num=num)
    else:
        for i in range(2,num):
            if num % i == 0:
                return "{num} is not prime".format(num=num)
        return "{num} is prime".format(num=num)

def checkIsPrime_Efficient(num):
    if num <= 3:
        return "{num} is prime".format(num=num)
    elif num % 2 == 0 or num % 3 == 0:
        return "{num} is not prime".format(num=num)
    else:
        stop = math.floor(num**(1/2))
        for i in range(5,stop+1,6):
            if num % i == 0:
                return "{num} is not prime, divisibile by {divisor}".format(num=num, divisor=i)
        return "{num} is prime".format(num=num)

if __name__ == '__main__':
    num = int(input("Enter the number to check for prime: "))
    print(checkIsPrime_Efficient(num))
