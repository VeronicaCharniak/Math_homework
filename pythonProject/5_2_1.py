# теорема сложения вероятностей на примере орла и решки
import numpy as np

heads, tails = 0, 0
trials = 100
for i in range(1, trials + 1):
    x = np.random.uniform(0, 10)
    if x < 5:
        heads += 1
    else:
        tails += 1
if heads / trials + tails / trials == 1:
    print(True)
else:
    print(False)
print(heads, tails)
