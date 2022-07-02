import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

n = 100
r = 0.7
x = np.random.rand(n)
y = r * x + (1 - r) * np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x) * np.sum(y) - n * np.sum(x * y)) / (np.sum(x) * np.sum(x) - n * np.sum(x * x))
b = (np.sum(y) - a * np.sum(x)) / n
x_m = np.sum(x) / n
y_m = np.sum(y) / n
r = np.sum((x - x_m) * (y - y_m)) / sqrt(np.sum((x - x_m) * (x - x_m)) * (np.sum((y - y_m) * (y - y_m))))

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print(a, b)
print(a1, b1)
print(r)

plt.plot([0, 1], [b, a + b])
plt.show()
