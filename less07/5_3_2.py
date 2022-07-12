# Приведите пример матрицы 4х4 с рангом 1
import numpy as np

c = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], float)
print(c)
print(np.linalg.matrix_rank(c, 0.0001))
