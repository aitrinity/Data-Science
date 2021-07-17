import pandas as pd 
import numpy as np
from numpy.random import randint

columns= ['W', 'X', 'Y', 'Z'] # four columns
index= ['A', 'B', 'C', 'D', 'E'] # five rows

np.random.seed(45)
data = randint(-100,100,(5,4))

df = pd.DataFrame(data, index=index, columns=columns)

df.loc['A'] # Selecting one row by name

df.loc[['A','C']] # Selecting multiple rows by name

df.iloc[0] # Selecting one row by index

df.iloc[0:2] # Selecting multiple rows by indexes

df.drop('C',axis=0) # Drop one row by name