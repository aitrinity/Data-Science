import numpy as np


m1 = np.arange(10).reshape(2,5)


mt = m1.T # Transpose

m2 = np.arange(5)
m2 = m2.reshape(1,5)
mt2 = m2.T

n1 = np.arange(10).reshape(2, 5)
n2 = np.arange(15).reshape(5,3)

# Matrix multiplication
n1.dot(n2)

# Matrix dot product
n3 = np.dot(n1,n2)

print(n1)
print(n2)
print(n3)