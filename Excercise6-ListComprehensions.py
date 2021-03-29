# Given three integers x,y,z representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k 
# is not equal to n

NUM = 0; FINAL = []

def check_sum_of_list(list):
    i = 0
    for x in list:
        i += x
    if(i != NUM):
        FINAL.append(list)
    
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    NUM = n
    
    output = [ check_sum_of_list([i,j,k]) for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) ]
    print(FINAL)