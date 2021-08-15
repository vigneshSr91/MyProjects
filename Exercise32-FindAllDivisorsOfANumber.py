import math
def FindDivisors(num):
    start = stop = math.floor(num**(1/2))
    for i in range(1,stop,1):
        if num % i == 0:
            print (i)

    for i in range(start,0,-1):
        if num % i == 0:
            print (int(num/i))

if __name__ == '__main__':
    # Pre-Requisite - To print the numbers in sorted Order
    num = int(input("Enter the Number to find it's divisors: "))
    FindDivisors(num)