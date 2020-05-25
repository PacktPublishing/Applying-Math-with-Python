

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


A = np.array([
    [2, 1],     # 2*x0 + x1 <= 6
    [-1, -1]    # -x0 - x1 <= -4
])
b = np.array([6, -4])


x0_bounds = (-3, 14)  # -3 <= x0 <= 14
x1_bounds = (2, 12)   #  2 <= x1 <= 12

c = np.array([1, 5])


def func(x):
    return np.tensordot(c, x, axes=1)


fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set(xlabel="x0", ylabel="x1", zlabel="func")
ax.set_title("Values in feasible region")

X0 = np.linspace(*x0_bounds)
X1 = np.linspace(*x1_bounds)
x0, x1 = np.meshgrid(X0, X1)
z = func([x0, x1])

ax.plot_surface(x0, x1, z, alpha=0.3)


Y = (b[0] - A[0, 0]*X0) / A[0, 1]
I = np.logical_and(Y >= x1_bounds[0], Y <= x1_bounds[1])
ax.plot(X0[I], Y[I], func([X0[I], Y[I]]), "r", lw=1.5)

Y = (b[1] - A[1, 0]*X0) / A[1, 1]
I = np.logical_and(Y >= x1_bounds[0], Y <= x1_bounds[1])
ax.plot(X0[I], Y[I], func([X0[I], Y[I]]), "r", lw=1.5)


B = np.tensordot(A, np.array([x0, x1]), axes=1)
II = np.logical_and(B[0, ...] <= b[0], B[1, ...] <= b[1]) 
ax.plot_trisurf(x0[II], x1[II], z[II], color="b", alpha=0.5)


res = optimize.linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds))
print(res)

ax.plot([res.x[0]], [res.x[1]], [res.fun], "k*")


plt.show()