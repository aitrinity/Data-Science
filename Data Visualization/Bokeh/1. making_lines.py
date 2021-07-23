from bokeh.plotting import figure 
from bokeh.io import output_file, show 

# prepare some data 

x = [1,2,3,4,5] 
y = [6,7,8,9,10]

# prepar the output file

output_file("outcomes/making_line.html")

# create a figure object 
f = figure()

# create line plot 
f.line(x,y)

#show graph
show(f)