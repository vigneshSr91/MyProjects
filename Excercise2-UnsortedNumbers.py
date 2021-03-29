def getCountOfUnsortedNumbers(arr, n):
    #count = 0;
    UnorderedList = [];
    for i in range(1, len(arr)):
        current = arr[i];
        for j in range(i, -1, -1):
            previous_sequence_in_array = arr[j]
            if(previous_sequence_in_array > current):
                #count += 1;
                if(UnorderedList.__contains__(i)==False):
                    UnorderedList.append(i);
                if(UnorderedList.__contains__(j)==False):
                    UnorderedList.append(j);
                break;
    print("Total number not in Acending order is {}".format(len(UnorderedList)));


# Driver code
if(__name__ == "__main__"):
    arr = [1,2,6,3,1,4];
    n = len(arr);
    getCountOfUnsortedNumbers(arr, n);
