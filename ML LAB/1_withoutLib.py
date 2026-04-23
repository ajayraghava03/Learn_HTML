
# Input numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(numbers)

# Mean
mean = sum(numbers) / n

# Median
numbers.sort()
if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

# Mode
freq = {}
for i in numbers:
    freq[i] = freq.get(i, 0) + 1

mode = max(freq, key=freq.get)

# Variance
variance = 0
for i in numbers:
    variance += (i - mean) ** 2
variance = variance / n

# Standard Deviation
std_dev = variance ** 0.5

# Output
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Variance =", variance)
print("Standard Deviation =", std_dev)