import numpy as np
import matplotlib.pyplot as plt

allsums = []
for i in range(11):
    x = np.random.rand(10)
    allsums.append(sum(x))
    i += 1
num_bins = 10
n, bins, patches = plt.hist(allsums, num_bins)
plt.xlabel('summa')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()
