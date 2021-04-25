import math
def MergeSort(arr):
    if len(arr) > 1:
        SplitIndex = len(arr) // 2
        left = arr[:SplitIndex]
        right = arr[SplitIndex:]

        MergeSort(left)
        MergeSort(right)


        i=0
        j=0

        k=0

        while(i<len(left) and j<len(right)):

            if(left[i] < right[j]):
               
                arr[k] = left[i]
                i += 1
                
            else:
                
                arr[k] = right[j]
                j += 1
            
            k += 1

        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1

    

if(__name__=='__main__'):
    InputList = list(map(int,input("Enter Comma Seperated Integers: ").split(",")))
    MergeSort(InputList)
    print(InputList)
                
