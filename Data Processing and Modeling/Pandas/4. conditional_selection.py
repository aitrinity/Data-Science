import pandas as pd 
import numpy as np
from numpy.random import randint

columns= ['W', 'X', 'Y', 'Z'] # four columns
index= ['A', 'B', 'C', 'D', 'E'] # five rows

np.random.seed(45)
data = randint(-100,100,(5,4))

df = pd.DataFrame(data, index=index, columns=columns)

df>0 # returns a boolean series

df['X']>0 # returns values of the column 'X' > 0

df[df['X']>0] # returns a dataframe with rows where 'X' is > 0