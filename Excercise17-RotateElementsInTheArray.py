"""
def rotate(arr,index,stop):
    if index == stop:
        return arr
    arr.append(arr[0])
    arr.remove(arr[0])
    return rotate(arr,index+1,stop)

if __name__=='__main__':
    arr = []
    arr = list(map(int,input("Enter the list: ").split(',')))
    n = int(input("Enter the Number of elements to rotate in the list"))
    print(rotate(arr,0,n))
"""
# Alternate Solution
"""
if __name__ == '__main__':
    arr = []
    arr = list(map(int,input("Enter the list: ").split(',')))
    n = int(input("Enter the Number of elements to rotate in the list"))
    arr_temp = arr[:n]
    arr = arr[n:]
    arr.extend(arr_temp)
    print(arr)
"""

# Bloc Swap Algorithm
def rotate(arrA,arrB,i):
    if len(arrA) > len(arrB):

        thisArray = arrA.copy()
        thisArray.extend(arrB)
        startIndex1 = 0
        startIndex2 = len(arrA)
        length = len(arrB)
        thisArray = swap(thisArray,startIndex1,startIndex2,length)

        nextArrayA = thisArray[len(arrB):len(arrA)]
        nextArrayB = thisArray[-i:]
        
        if len(nextArrayA) > len(nextArrayB):
            nextlength = len(nextArrayB)
        elif len(nextArrayB) > len(nextArrayA):
            nextlength = len(nextArrayA)
        else:
            nextlength = len(nextArrayB)

        #thisTemp = thisArray.copy()
        #thisTemp[len(nextArrayA)+len(nextArrayB):] = rotate(nextArrayA,nextArrayB,nextlength)
        thisTemp = rotate(nextArrayA,nextArrayB,nextlength)
        thisArray[len(arrB):len(arrA)+len(arrB)] = thisTemp

        return(thisArray)
        

    elif len(arrB) > len(arrA):

        thisArray = arrA.copy()
        thisArray.extend(arrB)
        startIndex1 = 0
        startIndex2 = len(arrB)
        length = len(arrA)
        thisArray = swap(thisArray,startIndex1,startIndex2,length)
        if (len(arrB)-i > 0):
            nextArrayA = thisArray[:len(arrA)]
            nextArrayB = thisArray[len(arrA):len(arrA)+len(arrB)-i]
            if len(nextArrayA) > len(nextArrayB):
                nextlength = len(nextArrayB)
            elif len(nextArrayB) > len(nextArrayA):
                nextlength = len(nextArrayA)
            else:
                nextlength = len(nextArrayB)

            #thisTemp = thisArray.copy()
            thisTemp = rotate(nextArrayA,nextArrayB,nextlength)

            thisArray[:len(arrA)+len(arrB)-i] = thisTemp
            return(thisArray)
    else:
        thisArray = arrA.copy()
        thisArray.extend(arrB)
        return(swap(arr=thisArray,startIndex1=0,startIndex2=i,n=i))
        

def swap(arr,startIndex1,startIndex2,n):
    temp=arr.copy()
    temp[startIndex1:startIndex1+n] = arr[startIndex2:startIndex2+n]
    temp[startIndex2:startIndex2+n] = arr[startIndex1:startIndex1+n]
    return(temp)

if __name__=='__main__':
    arr = []
    arr = list(map(int,input("Enter the list: ").split(',')))
    n = int(input("Enter the Number of elements to rotate in the list: "))
    print(rotate(arrA=arr[:n],arrB=arr[n:],i=n))

