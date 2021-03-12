import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 10)

a = list([])
for i in np.arange(-10, 10):
	if i==0:
		a.append(1)
	else:
		a.append(0)

plt.stem(n, a)
plt.show()
