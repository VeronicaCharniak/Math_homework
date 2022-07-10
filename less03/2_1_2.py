# расчет длины вектора
from math import sqrt


x, y, z = int(input('Задайте координаты вектора: ')), int(input()), int(input())
l = sqrt(x * x + y * y + z * z)
print('Длина вектора равна', l)


# Способ 2
my_vector = np.array([13, 4, 7])
len_vector = np.linalg.norm(my_vector)
print(len_vector)