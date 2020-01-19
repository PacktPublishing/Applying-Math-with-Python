import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 5, 0.1)
y = x*x

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Graph of $y=x^2$", usetex=True)
ax.set_xlabel("$x$", usetex=True)
ax.set_ylabel("$y$", usetex=True)

fig.savefig("savingfigs.png", dpi=300)
