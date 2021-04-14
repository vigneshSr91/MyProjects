import numpy as np
if __name__ =='__main__':
    
    
    arr1 = np.random.rand(5,4,3)
    arr2 = np.random.rand(5,3,3)
    print('**********************************arr1*************************************')
    print(arr1)
    print('**********************************arr2*************************************')
    print(arr2)
    print('**********************************result***********************************')
    arr_final = np.zeros((5,7,3))

    row1, column1, depth1 = arr1.shape
    row2, column2, depth2 = arr2.shape
    columns = column1 + column2
    final = np.empty((0,7,3))
    
    for i in range(row1+row2):
        columnList1 = [x for x in range(column1)]
        columnList2 = [x for x in range(column2)]
        temp1 = arr1[i:i+1,columnList1]
        temp2 = arr2[i:i+1,columnList2]
        tempShape1 = temp1.shape
        tempShape2 = temp2.shape
        temp = np.concatenate((temp1,temp2),axis=1)
        final = np.concatenate((final,temp),axis=0)

    print(final)
    print('**********************************Shape***********************************')
    print(final.shape)
    print('**********************************Test HStack*****************************')
    hstack = np.hstack((arr1,arr2))
    print(hstack)
        