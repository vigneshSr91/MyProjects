import numpy as np
from statsmodels import robust
import scipy.stats as scst

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

def CalculateMean(array, Doprint=False):
    list = array.tolist()
    mean,total = 0, 0
    for i in list:
        total += i
    # Intialize to total value, if len of list is greater than 1, then calculate the mean
    mean = total
    if len(array) > 1:
        mean = total / len(array)
    if Doprint:
        print("Total Elements in the list is: ", len(array))
        print("Mean of the initialized list is: ", mean)

    return mean

def CalculateMedian(array, DoPrint=False):
    #sorted_array = np.sort(array)
    list = array.tolist()
    MergeSort(list)
    sorted_array = np.array(list)
    medianIndex = len(sorted_array) // 2
    if len(array) % 2 == 0:
        median = ( sorted_array[medianIndex] + sorted_array[medianIndex-1] ) / 2
    else:
        median = sorted_array[len(array)/2]
    if DoPrint:
        print("Median of the initialized list is: ", median)

    return median

def CalculateStdDeviation(array, Doprint=False):
    mean = CalculateMean(array)
    lst = array.tolist()
    variance = sum((x-mean)**2 for x in lst) / len(lst)
    
    stdDeviation = variance**0.5
    if Doprint:
        #print("Variance of the list is: ",variance)
        print("Standard Deviation of the list is: ",stdDeviation)

def CalculateMedianAbsoluteDeviation(array, Doprint=False):
    
    median = CalculateMedian(array)
    lst = array.tolist()
    DistanceOfDataPointsFromMedian = [ abs(i-median) for i in lst ]
    #DistanceOfDataPointsFromMedian = [1 if x==0 else x for x in DistanceOfDataPointsFromMedian]
    MedianAbsoluteDeviation = CalculateMedian(np.array(DistanceOfDataPointsFromMedian))
    if Doprint:
        print("Median Absolute Deviation of the list is: ",MedianAbsoluteDeviation)

def InterQuartileRange(array, Doprint=False):
    lst = np.sort(array).tolist()
    _25thQuartileIndex = len(lst) * 25 // 100
    _75thQuartileIndex = len(lst) * 75 // 100
    _90thPercentile = len(lst) * 90 // 100
    _99thPercentile = len(lst) * 99 // 100
    InterQuartileValue = lst[_75thQuartileIndex] - lst[_25thQuartileIndex]
    if Doprint:
        print("IQR of the list is: ", InterQuartileValue)
        print("90th Percentile is: ", lst[_90thPercentile])
        print("99th Percentile is: ", lst[_99thPercentile])

if __name__ == '__main__':
    random_numbers = np.random.normal(loc=500000,scale=1000000,size=1000000)
    
    CalculateMean(random_numbers, True)
    print("Mean using Numpy is: ", np.mean(random_numbers))
    CalculateMedian(random_numbers, True)
    print("Median using Numpy is: ", np.median(random_numbers) )
    CalculateStdDeviation(random_numbers, True)
    print("Standard Deviation using Numpy is: ",np.std(random_numbers))
    CalculateMedianAbsoluteDeviation(random_numbers, True)
    print("Median Absolute Deviation from Scipy is: ", scst.median_abs_deviation(random_numbers))
    
    InterQuartileRange(random_numbers, True)
    q3, q1 = np.percentile(random_numbers, [75 ,25])
    iqr = q3 - q1
    print("IQR using Numpy is: ", iqr)
    print("90th Percentile using Numpy is: ", np.percentile(random_numbers,90))
    print("99th Percentile using Numpy is: ", np.percentile(random_numbers,99))