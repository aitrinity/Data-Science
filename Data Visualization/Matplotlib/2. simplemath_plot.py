import matplotlib.pyplot as plt
import numpy as np

# linspace(start, stop, num=50, endpoint=True, retstep=False)
# Return evenly spaced numbers over a specified interval.
x = np.linspace(-2, 2, 500)
y = x**2

plt.plot(x, y)
plt.show()