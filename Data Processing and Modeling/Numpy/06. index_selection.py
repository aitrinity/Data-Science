import numpy as np

# create a simple array
arr = np.arange(10)

# Bracket Indexing and Selection
# [start:stop:step]
# start is the index of the first element
# stop is the index of the last element
# step is the number of elements to skip
# [:stop] means start to stop
# [start:] means start to the end
# [:stop:step] means start to stop skipping by step
# [start:stop] means start to stop skipping by 1
# [start:stop:step] means start to stop skipping by step

#Get a value at an index
arr[8]

# Get a slice of the array
arr[1:5]

# Get a slice of the array
arr[1:5:2]