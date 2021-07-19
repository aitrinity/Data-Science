import pandas as pd


# Create Dataframe
df_one = pd.DataFrame({'k1':['A','A','B','B','C','C'], 
                        'col1':[100,200,300,300,400,500],                      
                        'col2':['NY','CA','WA','WA','AK','NV']})


# Grab first letter 
def grab_first_letter(state):
    # Given a state, return the first letter
    return state[0]

# Notice we only pass the function, we don't call it with ()
df_one['col2'].apply(grab_first_letter)

#  Creating new col with apply
df_one['first letter'] = df_one['col2'].apply(grab_first_letter)

# more complex function
def stateName(state):
    
    if state[0:2] == "NY":
        return "New York"
    else:
        return 'Error'

df_one['State Check'] = df_one['col2'].apply(stateName)