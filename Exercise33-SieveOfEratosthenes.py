# Sieve of Eratosthenes - Find all prime numbers lesser than or equal to a given number
import math
def checkIsPrime_Efficient(num):
    if num == 1:
        return False
    elif num ==2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        stop = math.floor(num**(1/2))
        for i in range(5,stop+1,6):
            if num % i == 0:
                return False
        return True

def NaiveSolution(num):
    for i in range(2,num+1):
        if checkIsPrime_Efficient(i):
            print(i)

def Seive(num):
    list_bool = [ True if i > 1 else False for i in range(num+1)  ]

    for i in range(2,math.floor(num**(1/2))):
        if(checkIsPrime_Efficient(i)):
            if list_bool[i]==True:
                j = 2 * i
                while(j < num):
                    list_bool[j]=False
                    j += i
    
    for i in range(2,num+1):
        if list_bool[i]==True:
            print(i)


def Seive_Optimized(num):
    list_bool = [ True if i > 1 else False for i in range(num+1)  ]

    for i in range(2,num+1):
        if(checkIsPrime_Efficient(i)):
            if list_bool[i]==True:
                print(i)
                j = i * i
                while(j < num):
                    list_bool[j]=False
                    j += i


if __name__ == '__main__':
    num = int(input("Enter a number :"))
    Seive_Optimized(num)