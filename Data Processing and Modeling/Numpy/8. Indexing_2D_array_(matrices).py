import numpy as np

# arr_2d[row][col] or arr_2d[row,col]. 
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))

#Indexing row
arr_2d[1]

#Indexing col
arr_2d[:,1]

# Getting indiviual elements
arr_2d[1,1] # arr_2d[1][1]

# 2D array slicing
#Shape (2,2) from top right corner
arr_2d[:2,1:]