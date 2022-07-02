# другие значение n и k
import numpy as np
from math import factorial

k, n = 0, 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
f = np.random.randint(0, 2, n)
x = a + b + c + d + e + f
for i in range(0, n):
    if x[i] == 1:
        k = k + 1
c42 = factorial(6) / (factorial(2) * factorial(6 - 2))
p = c42 * (1 / 2 ** 6)
print('Коэффициэент С из n=6(количество испытаний) по k=2(число возможных исходов) равен', c42)
print('Результат расчета вероятности по формуле Бернулли: P =', p)
print('Вычисления по методу Монте-Карло: k =', k, 'n =', n, 'Отношение k/n =', k / n)
