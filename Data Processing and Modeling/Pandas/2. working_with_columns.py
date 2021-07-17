import pandas as pd

data = {
    'Name': ['John', 'Tim', 'Rob'],
    'Age': [34, 23, 42],
    'Date': ['12/10/2016', '13/10/2016', '14/10/2016'],
    'Amount': [100, 200, 300]
}

df = pd.DataFrame(data) 

df['Name'] # Grab column 'Name'

df[['Name','Age:']] # 'Name' and 'Age' columns

type(df['Name']) # check the type of 'Name' column

df.dtypes # check the data type of each column

df['New'] = [1,2,3] # add a new column

df.drop('New',axis=1) # drop a column