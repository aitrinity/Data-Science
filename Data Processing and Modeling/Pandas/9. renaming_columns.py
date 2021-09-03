import pandas as pd 


data = {"Col a":[1,2,3,4,5] , "Col b":[1,2,3,4,5], "Col c":[1,2,3,4,5]}

df = pd.DataFrame(data)

df.columns = ["Col updated: a", "Col updated: b", "Col updated: c"]