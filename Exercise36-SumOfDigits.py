def getSum(num):
    if num == 0:
        return 0
    else:
        lastDigit = num % 10
        remainingDigit = num // 10
        return getSum(remainingDigit) + lastDigit

if(__name__=='__main__'):
    givenNumber = int(input("Enter the number to calculate the sum it's Digits: "))
    print("The Sum of Digits = ", getSum(givenNumber))
