import pandas as pd


# Create DataFrame
df_one = pd.DataFrame({'k1':['A','A','B','B','C','C'],
                      'col1':[100,200,300,300,400,500],
                      'col2':['NY','CA','WA','WA','AK','NV']})

# Information on Unique Values
df_one['col1'].unique() # = [100, 200, 300, 400, 500]

# nunique() - Number of unique values
df_one['col1'].nunique() # = 5

# values_counts() - Number of occurrences of each value
df_one['col1'].value_counts() # = [3, 2, 1, 1, 1]

# drop_duplicates() - Drop duplicate values
df_one['col1'].drop_duplicates() # = [100, 200, 300, 400, 500]