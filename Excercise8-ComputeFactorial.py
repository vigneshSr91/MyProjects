def factorial(num):
    if(num < 0):
        return "Error"
    if(num==0):
        return 1
    previous = num - 1
    return num * factorial(previous)

if(__name__=="__main__"):
    num = int(input())
    print(factorial(num))