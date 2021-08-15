def computeGCD_EuclideanAlgorithm(numA,numB):
    if(numB==0):
        return numA
    else:
        return computeGCD_EuclideanAlgorithm(numB,numA % numB)

def computeGCD_Iterative(numA,numB):
    if numA >= numB and numA % numB==0:
        return numB
    elif numB % numA==0:
        return numA
    
    lesserOfTheTwo = numA
    greaterOfTheTwo = numB
    if numB < numA:
        lesserOfTheTwo = numB
        greaterOfTheTwo = numA

    result = 1
    for i in list(range(lesserOfTheTwo+1))[-1:0:-1]:
        if greaterOfTheTwo % i == 0 and lesserOfTheTwo % i == 0:
            result = i
            break
    
    return result
if __name__=='__main__':
    numA, numB = map(int,input("Enter 2 Numbers(seperated by comma) to Compute the GCD :").split(','))
    print("The GCD of the given numbers is {result}".format(result=computeGCD_EuclideanAlgorithm(numA,numB)))