def findTrailingZeroOfFactorial_iterative(num):
    factorial = 1
    if num > 1:
        for i in range(1,num+1):
            factorial *= i
    else:
        return 0

    trailingZeroesInFactorial=0
    while(factorial > 0):
        if(factorial % 10==0):
            trailingZeroesInFactorial += 1
            factorial /= 10
        else:
            break

    return trailingZeroesInFactorial

def findTrailingZeroOfFactorial_logn(num):
    result = 0

    if num >= 5:    
        for i in range(5,num+1,5):
            result += num // i
            
    return(result)

if __name__ =='__main__':
    num = int(input("Enter a Number to find the trailing 0's in it's Factorial :"))
    print("Number of Trailing 0's in Factorial of {num} is {total}".format(num=num, total=findTrailingZeroOfFactorial_logn(num)))
