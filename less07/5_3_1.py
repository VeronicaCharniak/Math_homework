# Вычислить матрицу, обратную данной
import numpy as np

a = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
print(np.linalg.inv(a))