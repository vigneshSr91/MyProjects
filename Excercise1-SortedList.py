DIGITS = 4; MIN = 1000; MAX = 9999;

def getBest(curr, prev):
    StartFrom = max(MIN, prev);

    
    for i in range(StartFrom, MAX + 1):
        count = 0;
        a = i;
        b = curr;
        # Commpare the reminder for each digit
        for k in range(DIGITS):
            # Compare the remainders
            if(a % 10 != b % 10):
                count += 1;
            
            a //= 10;
            b //= 10;
        # Allow only those numbers where atmost a single digit differs
        if(count <= 1):
            return i;
    
    return -1;


def getList(arr, n):

    myList=[];

    possible=True;

    myList.append(0);

    for i in range(n):

        curr = arr[i]
        # Get the best possible next number that could be added to the Ascending list
        myList.append(getBest(curr, myList[-1]));

        if(myList[-1] == -1):
            possible=False;
            break;

    if(possible):
        for i in range(1, len(myList)):
            print(myList[i], end=" ");
    else:
        print("-1");

# Driver code
if __name__ == "__main__":

    arr = [1095, 1094, 1095];
    n = len(arr);
    # Pass the array where we like to adjust the numbers to Ascending number by changing a single digit 
    getList(arr, n);

