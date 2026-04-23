import math

# Step 1: Take number input
num = float(input("Enter a number: "))

# Step 2: Perform math operations
print("\n--- Math Operations ---")
print("Square Root:", math.sqrt(num))
print("Power (num^2):", math.pow(num, 2))
print("Ceiling value:", math.ceil(num))
print("Floor value:", math.floor(num))
print("Absolute value:", math.fabs(num))

# Step 3: Trigonometric functions
print("\n--- Trigonometric ---")
print("sin:", math.sin(num))
print("cos:", math.cos(num))
print("tan:", math.tan(num))

#numpyy

import numpy as np

# Step 1: Take input from user
nums = input("Enter numbers separated by space: ")

# Step 2: Convert input into list → array
num_list = list(map(int, nums.split()))
arr = np.array(num_list)

# Step 3: Display array
print("\nNumPy Array:", arr)

# Step 4: Perform operations
print("\n--- Operations ---")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sorted Array:", np.sort(arr))


