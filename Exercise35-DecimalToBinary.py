def fun(n):
    if (n==0):
        return
    else:
        fun(n//2)
        print(n%2)

if(__name__=='__main__'):
    givenNumber = int(input("Enter the Number to represent in Binary: "))
    fun(givenNumber)