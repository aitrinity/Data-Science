import numpy as np

# create an array 
arr = np.arange(25)

# reshape to an 5 x 5 matrix
rarr = arr.reshape((5, 5))

# flatten the array
farr = rarr.flatten()

# get the max value
farr.max()

# get the min value
farr.min()

# get argmax 
farr.argmax()

# get argmin value 
farr.argmin()

# get shape     
farr.shape

# get size  
farr.size

# get dtype
farr.size

# get ndim 
farr.ndim
