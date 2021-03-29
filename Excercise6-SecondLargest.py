def getSecondLargest(lst):
    newlist = [int(x) for x in lst]
    sortedList = sorted(newlist, reverse=True)
    secondLargest = 0
    first = 0
    second = 1
    index = 0
    while(secondLargest == 0):
        if(index >= len(sortedList)):
            break
        if(sortedList[first] > sortedList[second]):
            secondLargest = sortedList[second]
        first = first + 1
        if(second<(len(sortedList)-1)):
            second = second + 1
        else:
            break
        index = index + 1
    if(secondLargest == 0):
        return "Error"
    else:
        return secondLargest

if(__name__=='__main__'):
    lst = list(input( ).split(','))
    print(getSecondLargest(lst))