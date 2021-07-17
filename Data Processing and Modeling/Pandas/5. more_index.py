import pandas as pd 
import numpy as np
from numpy.random import randint

columns= ['W', 'X', 'Y', 'Z'] # four columns
index= ['A', 'B', 'C', 'D', 'E'] # five rows

np.random.seed(45)
data = randint(-100,100,(5,4))

df = pd.DataFrame(data, index=index, columns=columns)

df.reset_index() # Reset to default 0,1...n index

states = ['CA', 'NY', 'WY', 'OR', 'CO']
df['States'] = states

df.set_index('States') # Set the index to be the column 'States'