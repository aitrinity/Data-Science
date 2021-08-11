import numpy as np

t = np.arange(24).reshape(2, 3, 4)

# Transpose
tt = t.transpose(1, 2, 0)

print(t)
print(tt)