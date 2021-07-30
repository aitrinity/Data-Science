import numpy as np

arr = np.full((3,4), 1.0)

arr2 = np.full((3,4), 2.0)


# vstack 

arrv = np.vstack((arr, arr2))
print(arrv)
print(arrv.shape)

# hstack
arrh = np.hstack((arr, arr2))
print(arrh)
print(arrh.shape)

arrv_con = np.concatenate((arr, arr2), axis=0)
print(arrv_con)  # Equivalent to vstack
print(arrv_con.shape)

arrh_con = np.concatenate((arr, arr2), axis=1)
print(arrh_con)  # Equivalent to hstack
print(arrh_con.shape)

arrs = np.stack((arr, arr2))
print(arrs) # Must be same shape, stack arrays along a new axis.
print(arrs.shape)