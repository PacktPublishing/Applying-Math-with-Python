
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

X = np.linspace(-2, 2)
Y = np.linspace(-2, 2)
x, y = np.meshgrid(X, Y)
t = x**2 + y**2  # small efficiency
z = np.cos(2*np.pi*t)*np.exp(-t)


fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(x, y, z, cmap="binary_r")
ax.set_title("Surface with colormap")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")


plt.show()

fig, ax = plt.subplots()
ax.contour(x, y, z, cmap="binary_r")

ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Contour plot with colormap set")

plt.show()
