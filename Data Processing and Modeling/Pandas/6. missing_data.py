import numpy as np
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A':[1,2,np.nan,4],'B':[5,np.nan,np.nan,8],'C':[10,20,30,40]})

# Remove rows with NaN values
df.dropna()

# Remove columns with NaN values
df.dropna(axis=1)

# Fill NaN values with 0
df.fillna(0)

# Fill Columns with NaN values with 0
df['A'].fillna(value=0)

# Fill NaN values with mean
df.fillna(df.mean())