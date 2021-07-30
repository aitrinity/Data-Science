import numpy as np

arr = np.arange(24).reshape(6,4)
print(arr)

arr1, arr2, arr3 = np.vsplit(arr, 3) # create 3 new arrays by splitting arr at the 3rd index
print(arr1)
print(arr2)
print(arr3)

arr4, arr5 = np.hsplit(arr, 2) # create 2 new arrays by splitting arr at the 2nd index
print(arr4)
print(arr5)