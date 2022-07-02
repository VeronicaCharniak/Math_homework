#основное событие - из 4 испытаний выпадает 2 раза орел и 2 раза решка (k=2)
import numpy as np
from math import factorial

k, n = 0, 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
c42 = factorial(4) / (factorial(2) * factorial(4 - 2))
p = c42 * (1 / 2 ** 4)
print('Коэффициэент С из n=4(количество испытаний) по k=2(число возможных исходов)', c42)
print('Результат расчета вероятности по формуле Бернулли: P =', p)
print('Вычисления по методу Монте-Карло: k =', k, 'n =', n, 'Отношение k/n =', k / n)
