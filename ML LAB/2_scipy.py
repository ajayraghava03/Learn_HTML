#from scipy import stats

import numpy as np
from scipy import stats, integrate

# Step 1: Take input
nums = input("Enter numbers separated by space: ")

# Step 2: Convert to array
data = np.array(list(map(float, nums.split())))

print("\nData:", data)

# Step 3: Statistical operations
print("\n--- Statistics ---")
print("Mean:", stats.tmean(data))
print("Median:", np.median(data)) #numpy
print("Mode:", stats.mode(data, keepdims=True))
print("Standard Deviation:", np.std(data)) #Numpy

# Step 4: Integration example (simple function)
print("\n--- Integration ---")
result, _ = integrate.quad(lambda x: x**2, 0, 3)
print("Integration of x^2 from 0 to 3:", result)