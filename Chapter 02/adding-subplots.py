
import numpy as np
import matplotlib.pyplot as plt
from math import fabs

def generate_newton_iters(x0, number):
    yield x0, fabs(x0 - 1.)
    for _ in range(number):
        x0 = x0 - (x0*x0 - 1.)/(2*x0)
        yield x0, fabs(x0 - 1.)


data = np.array(list(generate_newton_iters(2.0, 5)))
iterates, errors = data[:, 0], data[:, 1]

fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True) # 1 row, 2 columns

ax1.plot(iterates, "x")
ax1.set_title("Iterates")
ax1.set_xlabel("$i$", usetex=True)
ax1.set_ylabel("$x_i$", usetex=True)

ax2.semilogy(errors, "x") # plot y on a logarithmic scale
ax2.set_title("Error")
ax2.set_xlabel("$i$", usetex=True)
ax2.set_ylabel("Error")

plt.show()





