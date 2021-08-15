def factorialIterative(num):
    total = 1
    if num <= 1:
        return total
    for i in range(1,num+1):
        total *= i
    return total

def factorialRecursive(num):
    if num <= 1:
        return 1
    return(num * factorialRecursive(num-1))
if __name__=='__main__':
    num = int(input("Enter a Number for Calculating it's Factorial: "))
    print('Factorial of {num} is {total}'.format(num=num,total=factorialRecursive(num)))