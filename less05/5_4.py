import itertools
from math import factorial

# количество возможных размещений
n1 = 5
k1 = 5
for p in itertools.permutations('01234', k1):
    print(''.join(str(x) for x in p))
c1 = factorial(n1) / (factorial(k1) * factorial(n1 - k1))
A = c1 * factorial(k1)
print('Число возможных комбинаций равно', A)

# количество возможных сочетаний
n2 = 6
k2 = 3
for p in itertools.combinations('012345', k2):
    print(''.join(p))
c2 = factorial(n2) / (factorial(k2) * factorial(n2 - k2))
print('Число возможных сочетаний равно', c2)