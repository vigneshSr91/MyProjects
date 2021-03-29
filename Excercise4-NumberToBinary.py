binary=["0","1"]; number=0; bits_requested=1; BinaryStr=[]
def determineNext(x, Obj):

    BinaryStr = [ x + element for element in Obj ]
    return BinaryStr

def getBinaryRepresentation(n):
    if(n == 0 and bits_requested >= 1):
        return [ "0" ]
    elif(n == 1 and bits_requested >= 1):
        return [ "0", "1" ]
    else:
        return ( determineNext("0", getBinaryRepresentation(n-1)) + determineNext("1", getBinaryRepresentation(n-1)) )


    


# Driver code
if(__name__ == "__main__"):
    number = 15
    bits_requested = 20
    ListBinary = getBinaryRepresentation(bits_requested)

    if(len(ListBinary) < number+1):
        # No of requested bites not sufficient
        print("-1")
    else:
        print(ListBinary[number])