import math
def findDigitsIterative(num):
    n = num
    digits = 0
    while n > 0:
        n //= 10
        digits += 1
    return digits

def findDigitsRecursive(num):
    if num <= 0:
        return 0
    return 1 + findDigitsRecursive(num//10)

def findDigitsLogarithmic(num):
    return 1 + math.floor(math.log(num, 10))

if __name__=='__main__':
    num = int(input("Enter a number :"))
    result = 0
    result = findDigitsIterative(num)
    result = findDigitsRecursive(num)
    result = findDigitsLogarithmic(num)
    print("Numbers of digits in the given number is: ", result)
