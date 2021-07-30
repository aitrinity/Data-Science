import numpy as np
from numpy.core.numeric import identity

#  arange() method returns evenly spaced values within a given interval.

array = np.arange(0,11)

# zeros and ones are used to create arrays of zeros and ones.

zeros = np.zeros((3,5)) # 3 rows and 5 columns
ones = np.ones((3,5)) # 3 rows and 5 columns

# linspace() method returns evenly spaced numbers over a specified interval.

lin_space = np.linspace(0,10,5) # 5 evenly spaced values from 0 to 10

# eye() method 

identity = np.eye(4) # 4x4 identity matrix