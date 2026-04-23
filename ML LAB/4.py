import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

mean_x = np.mean(x)
mean_y = np.mean(y)

num = np.sum((x - mean_x) * (y - mean_y))
den = np.sum((x - mean_x) ** 2)

b1 = num / den
b0 = mean_y - b1 * mean_x

print(b0)
print(b1)

y_pred = b0 + b1 * x

plt.scatter(x, y)
plt.plot(x, y_pred)
plt.show()