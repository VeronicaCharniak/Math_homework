# Решите линейную систему
import numpy as np

a = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
b = np.array([12, 2, 1])
x = np.linalg.solve(a, b)
print(x)