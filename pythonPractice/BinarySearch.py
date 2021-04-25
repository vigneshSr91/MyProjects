# Pre-Requisite - The given array must be in sorted order
def BinarySearch(myList, SearchElement, Start, End):
    mid = ( End - Start ) // 2

    if mid <= 0:
        print('Not Found')
        return

    if myList[mid] == SearchElement:
        print('Found, ', myList[mid] )
    elif myList[mid] > SearchElement:
        Start   = 0
        End     = mid
        BinarySearch(myList[Start:End], SearchElement, Start, End)
    else:
        Start   = mid
        End     = len(myList)
        BinarySearch(myList[Start:End], SearchElement, Start, End)


if __name__ == '__main__':
    InputList = list(map(int,input("Enter Comma Seperated Integers: ").split(",")))
    SearchElement = int(input("Enter an Integer you wish to search: "))
    InputList.sort()
    BinarySearch(InputList, SearchElement, 0, len(InputList))
