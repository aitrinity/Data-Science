import numpy as np

arr = np.arange(1,11)
arr

# Return boolen values
bool_arr = arr>4 # = [False False False False False False  True  True  True  True] 

# Checking the values 
arr[bool_arr] # = [5  6  7  8  9 10]

