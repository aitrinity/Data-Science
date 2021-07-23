from bokeh.plotting import figure 
from bokeh.io import output_file, show 

a = [3,7.5,10]
b = [3,6,9]

output_file("outcomes/triangle_on_coord_points.html")

z = figure()

z.triangle(a,b)

show(z)