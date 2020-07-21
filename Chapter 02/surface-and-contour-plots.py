import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-2, 2)
Y = np.linspace(-1, 1)


x, y = np.meshgrid(X, Y)

z = x**2 * y**3


from mpl_toolkits import mplot3d

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot_surface(x, y, z)

ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")

ax.set_title("Graph of the function $f(x) = x^2y^3$")


plt.show()  # paused here


fig, ax = plt.subplots()
ax.contour(x, y, z)
ax.set_title("Contours of $f(x) = x^2y^3$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")


plt.show()
