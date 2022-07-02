#рулетка
import numpy as np
for i in range(0, 5):
    a = input()
    n = np.random.uniform(0, 37)
    if n == 0:
      print("зеленое")
    elif 1 <= n < 18:
      print("красное")
    else:
       print("черное")