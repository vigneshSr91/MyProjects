"""
def splitRope(RemainingLength,possibleSplits,cuts,combinations):
    if ( RemainingLength < 0 ) or len([x for x in possibleSplits if x <= RemainingLength]) == 0 :
        del cuts[-1]
        return combinations,cuts
    for splitAt in possibleSplits:
        if RemainingLength - splitAt == 0:
            cuts.append(splitAt)
            combinations.add(tuple(cuts))
            cuts=[]
        elif RemainingLength - splitAt >= 0:
            cuts.append(splitAt)
            combinations,cuts = splitRope(RemainingLength = (RemainingLength - splitAt), possibleSplits=possibleSplits, cuts=cuts,combinations=combinations )
    return combinations,[]

if __name__ == '__main__':
    TotalLength = int(input('Enter the total length of the rope: '))
    possibleSplits = list(map(int,input("Enter 3 numbers(Comma seperated) for splitting the rope: ").split(',')))
    cuts=list()
    combinations=set()
    combinations,cuts = splitRope(RemainingLength=TotalLength, possibleSplits=possibleSplits, cuts=cuts, combinations=combinations)
    print(combinations)
"""
def maxPieces(n, a, b, c):
    result = 0
    if n == 0:
        return 0
    if n < 0:
        return -1
    
    result = max(maxPieces(n-a,a,b,c),maxPieces(n-b,a,b,c),maxPieces(n-c,a,b,c))

    if result < 0:
        return -1
    return result + 1
    
if __name__ == "__main__":
    TotalLength = int(input('Enter the total length of the rope: '))
    a,b,c=map(int,input("Enter 3 numbers(Comma seperated) for splitting the rope: ").split(','))
    print(maxPieces(TotalLength,a,b,c))