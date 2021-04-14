from itertools import permutations
FINAL=[];

def permutate(InputList):
    l=[]
    if(len(InputList)==0):
        return
    
    if(len(InputList)==1):
        return InputList

    for i in range(len(InputList)):
        FirstElement = InputList[i]
        RemainingList = []
        RemainingList = InputList[i+1:] + InputList[:i]

        for j in permutate(RemainingList):
            l.append(list(FirstElement) + list(j))
    return l


if __name__ == '__main__':
    list_input = list(list(map(str,input('Enter Comma seperated list: ').split(','))))
    """
    p = permutations(list_input)
    j=0
    for i in p:    
        print(i)
        j += 1 
    print(j)
    """
    p = permutate(list_input)
    j=0
    for i in p:
        print(i)
        j += 1
    print(j)



    
    
    

    

