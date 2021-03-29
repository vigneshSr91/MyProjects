"""
FINAL = []
import math

def climbStairs(list, counter):
    if counter >= len(list):
        return
    l_list = list.copy()
    for i in range(len(list)):
        #if(counter > len(list)):
        #    break
        if(list[ i ]==2 and i == counter):
            l_list.pop(i)
            l_list[i:i] = [(1,1)]
            FINAL.append(l_list.copy())
            climbStairs(list, i+1)
            
    #climbStairs(l_list, 0)
    

# Driver code
if __name__ == "__main__":
    no_of_stairs = int(input())
    # Calculate the shortest path( max 2 steps at a time )
    counter = 0
    list = [ 2 ] * math.floor( no_of_stairs / 2 )
    FINAL.append(list)
    climbStairs(list, counter)
    if(no_of_stairs > 2 ):
        list = [ 1 ] * no_of_stairs
        FINAL.append(list)
    print(len(FINAL))

# python program to demonstrate 
# unique combination of two lists 
# using zip() and permutation of itertools 
  
# import itertools package 
import itertools 
from itertools import permutations  
  
# initialize lists 
list_1 = [(1,1), (1,1), (1,1), (1,1), (1,1)]
list_2 = [2,2,2,2,2] 
  
# create empty list to store the 
# combinations 
unique_combinations = [] 
  
# Getting all permutations of list_1  
# with length of list_2 
permut = itertools.permutations(list_1, len(list_2)) 
  
# zip() is called to pair each permutation 
# and shorter list element into combination 
for comb in permut: 
    zipped = zip(comb, list_2) 
    unique_combinations.append(list(zipped)) 
  
# printing unique_combination list  
print(unique_combinations) 
"""
# Solution is same as Fibonacci sequence

def calculateFibonacciSequence(input1, input2, count):
    if(count == 0):
        return input2
    next = input1 + input2
    input1 = input2
    return(calculateFibonacciSequence(input1, next, count-1))

if __name__ == '__main__':
    no_of_stairs = int(input())
    print(calculateFibonacciSequence(0,1,no_of_stairs))
    
    



