import numpy as np

# Creates an array of the given shape and populates it with random samples 
# #from a uniform distribution over [0, 1)
rand = np.random.rand(2) 

rand2 = np.random.rand(4,4) # Create a 4x4 array of random numbers
print(rand)

# Returns a sample (or samples) from the "standard normal" distribution [σ = 1]
# . Unlike rand which is uniform, values closer to zero are more likely to appear.

np.random.randn(2) # Returns a sample (or samples) from the “standard normal” distribution

# Randint generates integers from a uniform distribution
# with “shapes” and limits given by the shape parameters

randint1 = np.random.randint(1,100,10) # Generate 10 random integers from 1 to 100
randint2 = np.random.randint(1,10,3) # Create a 3x3 array of random integers

