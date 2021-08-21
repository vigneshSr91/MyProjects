def fun(n):
    if(n==1):
        return 0
    else:
        return (1 + fun(n//2))

if(__name__=='__main__'):
    givenNumber = int(input("Enter a number to Calculate the floor of Log(base2):"))
    print(fun(givenNumber))
