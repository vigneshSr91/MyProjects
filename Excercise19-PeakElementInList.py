import scipy.signal as signal

if __name__ == '__main__':
    list_numbers = list(map(int, input('Enter the commma separated numbers: ').split(',')))

    """
        # Finding Peak element with size 1( both on left and right side)
    if list_numbers[0] >= list_numbers[1]:
        print(list_numbers[0])

    for i in range(1,len(list_numbers)-1 ):
        if(list_numbers[i-1]<=list_numbers[i]) and (list_numbers[i]>=list_numbers[i+1]):
            print(list_numbers[i])

    if list_numbers[len(list_numbers)-1] >= list_numbers[len(list_numbers)-2]:
        print(list_numbers[len(list_numbers)-1])

    """
    
        # Finding Peak element with size 2( both on left and right size)

    for i in range(len(list_numbers)):
        startIndex = 0
        endIndex = 0

        if i <= 2:
            startIndex = 0
        else:
            startIndex = i - 2

        if (i+2) >= len(list_numbers):
            endIndex = len(list_numbers) 
        else:
            endIndex = i+2
        
        #for j in range(startIndex, endIndex):
        if list_numbers[i] == max(list_numbers[startIndex:endIndex]):
            print(list_numbers[i])
    

    """
    peaks = signal.find_peaks(x=list_numbers,distance=2, )
    print(peaks)
    """
    