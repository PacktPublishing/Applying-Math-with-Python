

import numpy as np
import matplotlib.pyplot as plt


y1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y2 = np.array([1.2, 1.6, 3.1, 4.2, 4.8])
y3 = np.array([3.2, 1.1, 2.0, 3.9, 2.5])

fig, ax = plt.subplots()

lines = ax.plot(y1, 'o', y2, 'x', y3, '*')


plt.show()
