from bokeh.plotting import figure 
from bokeh.io import output_file, show 

p = [3,7.5,10]
q = [3,6,9]

output_file("outcomes/circle_on_coord_points.html")

r = figure()

r.circle(p,q)

show(r)