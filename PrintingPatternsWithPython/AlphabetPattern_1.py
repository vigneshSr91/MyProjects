def PrintAlphabets(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(chr(64+i),end='')
        print(end='\n')

if __name__=='__main__':
    num = int(input("Enter the levels(1-26) for printing Alphabets :"))
    if num < 1 or num > 26:
        print("Invalid Input, Try Again !!!")
    else:
        PrintAlphabets(num)