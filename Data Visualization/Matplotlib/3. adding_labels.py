import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2, 2, 500)
y = x**2

plt.plot(x, y)
plt.title("Square function") # add title
plt.xlabel("x") # add x-axis label
plt.ylabel("y = x**2") # add y-axis label
plt.grid(True) # add grid
plt.show()