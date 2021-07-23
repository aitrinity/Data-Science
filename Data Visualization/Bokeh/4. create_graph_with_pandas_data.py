import pandas as pd
from bokeh.plotting import figure 
from bokeh.io import output_file, show 

bdf = pd.read_csv("data/bachelors.csv")
bdf.columns

x = bdf['Year']
y = bdf['Engineering']

output_file("outcomes/women_bachelors.html")

w = figure()

w.line(x,y)

show(w)