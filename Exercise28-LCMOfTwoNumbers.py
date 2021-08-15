
def computeLCMIterative(num1,num2):
    result = max(num1,num2)
    while(True):
        if result % num1==0 and result % num2 == 0:
            return result
        result += 1

def gcd(num1,num2):
    if num2 == 0:
        return num1

    return gcd(num2, num1 % num2)

def computeLCM_Logn_TimeComplexity(num1,num2):
    
    # The Solution Uses GCD by Euclidean Algorithm
    # The LCM is the multiple of the two numbers divided by their GCD
    # a * b = GCD(a,b) * LCM(a,b)
    # => LCM(a,b) = a * b / GCD(a,b)
    return ( ( num1 * num2 ) // gcd(num1,num2) )

if __name__=='__main__':
    num1, num2 = map(int,input("Enter 2 comma seperated numbers to compute LCM: ").split(','))
    print("The LCM of the two numbers {num1} and {num2} is: {result}" 
        .format(num1=num1,num2=num2,result=computeLCM_Logn_TimeComplexity(num1,num2)))