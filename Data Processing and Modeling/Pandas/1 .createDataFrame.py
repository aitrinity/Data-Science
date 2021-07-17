import pandas as pd

data = {
    'Name': ['John', 'Tim', 'Rob'],
    'Age': [34, 23, 42],
    'Date': ['12/10/2016', '13/10/2016', '14/10/2016'],
    'Amount': [100, 200, 300]
}

df = pd.DataFrame(data) # Create a DataFrame