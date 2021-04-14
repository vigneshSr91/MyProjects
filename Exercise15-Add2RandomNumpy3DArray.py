import numpy as np

if __name__ == '__main__':
    result = np.zeros((3,3,3))
    array1 = np.random.rand(3,3,3)
    array2 = np.random.rand(3,3,3)
    print(array1)
    print('############################################')
    print(array2)
    print('###########################################')
    (x, y , z) = np.shape(result)

    for i in range(x):
        for j in range(y):
            for k in range(z):
                result[i,j,k] = array1[i,j,k] + array2[i,j,k]
    
    print(result)
