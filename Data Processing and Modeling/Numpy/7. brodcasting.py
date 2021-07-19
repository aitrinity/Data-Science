import numpy as np 

#Creating sample array
arr = np.arange(0,11)

#Setting a value with index range (Broadcasting)
arr[0:5]=100

#Important notes on Slices 
#Slices are just like indexes, except that they can be used on multiple dimensions.
#Slices are useful for selecting subsets of the data and doing operations on them.
#Slices are also useful for assigning to slices.
#Slices can be used anywhere that you can use an index.
#Slices are not the same as indexes.

slice_of_arr = arr[0:6] #first 6 elements
slice_of_arr[:]=99 # assign all elements in slice to 99

#To get a copy, need to be explicit
arr_copy = arr.copy()

arr_copy