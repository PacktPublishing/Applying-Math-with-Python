
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import optimize



def func(x):
    return ((x[0] - 0.5)**2 + (x[1] + 0.5)**2)*np.cos(0.5*x[0]*x[1])

x_r = np.linspace(-1, 1)
y_r = np.linspace(-2, 2)

x, y = np.meshgrid(x_r, y_r)

z = func([x, y])


fig = plt.figure(tight_layout=True)
ax = fig.add_subplot(projection="3d")
ax.tick_params(axis="both", which="major", labelsize=9)
ax.set(xlabel="x", ylabel="y", zlabel="z")
ax.set_title("Objective function")

ax.plot_surface(x, y, z, alpha=0.7)

x0 = np.array([-0.5, 1.0])
ax.plot([x0[0]], [x0[1]], func(x0), "r*")

result = optimize.minimize(func, x0, tol=1e-6, method="Nelder-Mead")
print(result)


ax.plot([result.x[0]], [result.x[1]], [result.fun], "r*")

plt.show()