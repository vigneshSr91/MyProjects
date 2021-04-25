def InsertionSort(ListOfIntegers):
    for j in range(1,len(ListOfIntegers)):
        key = ListOfIntegers[j]
        i = j-1
        while(i >= 0 and ListOfIntegers[i]>key):
            ListOfIntegers[i+1] = ListOfIntegers[i]
            i -= 1
        ListOfIntegers[i+1] = key
    return(ListOfIntegers)

if(__name__=='__main__'):
    ListOfIntegers = list(map(int,input("Enter Comma Seperated Integers: ").split(",")))
    print("Ordered result is: ", InsertionSort(ListOfIntegers))
