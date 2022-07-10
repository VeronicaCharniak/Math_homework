import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

x = np.linspace(-2, 3, 201)
plt.plot(x, np.exp(x) + x * (2 - x ** 2) - 1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()


def equation(x):
    return (np.exp(x) + x * (2 - x ** 2) - 1)


x1 = fsolve(equation, -2)
print(x1)

x2 = fsolve(equation, 2)
print(x2)

x0 = fsolve(equation, 0.1)
print(x0)

# График выше прямой y = 0: для x от минус бесконечности до х = 1.58,  а также 0 < x < 2.6