"""
def CalculateSum(num):
    if num == 0:
        return 0
    elif num < 0:
        return num + CalculateSum(num + 1 )
    else:
        return num + CalculateSum(num - 1 )
"""
def CalculateSumOfNIntegers(num):
    return int(num*(num+1)/2)
    
if __name__=='__main__':
    num = int(input("Sum of numbers upto :"))
    #print(CalculateSum(num))
    print(CalculateSumOfNIntegers(num))