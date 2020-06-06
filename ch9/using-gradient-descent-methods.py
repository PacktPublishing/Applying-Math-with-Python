
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from scipy.optimize import minimize_scalar


def descend(func, x0, grad, bounds, tol=1e-8, max_iter=100):
    xn = x0
    xnm1 = np.inf

    for i in range(max_iter):
        
        if np.linalg.norm(xn - xnm1) < tol:
            break

        grad_xn = grad(xn)
        yield i, xn, func(xn), grad_xn

        direction = -grad_xn
        
        alphas = np.array([
            (bounds[0][0] - xn[0]) / direction[0], # x lower
            (bounds[1][0] - xn[1]) / direction[1], # y lower
            (bounds[0][1] - xn[0]) / direction[0], # x upper
            (bounds[1][1] - xn[1]) / direction[1]  # y upper
        ])

        alpha_max = alphas[alphas >= 0].min()
        alpha_min = alphas[alphas < 0].max()
        

        result = minimize_scalar(lambda t: func(xn + t*direction), 
            method="bounded", bounds=(alpha_min, alpha_max))
        amount = result.x


        xnm1 = xn
        xn = xn + amount*direction


def func(x):
    return ((x[0] - 0.5)**2 + (x[1] + 0.5)**2)*np.cos(0.5*x[0]*x[1])


x_r = np.linspace(-1, 1)
y_r = np.linspace(-2, 2)

x, y = np.meshgrid(x_r, y_r)

z = func([x, y])


surf_fig = plt.figure()
surf_ax = surf_fig.add_subplot(projection="3d")
surf_ax.set(xlabel="x", ylabel="y", zlabel="z")
surf_ax.set_title("Objective function")

surf_ax.plot_surface(x, y, z, alpha=0.7)

x0 = np.array([-0.8, 1.3])
surf_ax.plot([x0[0]], [x0[1]], func(x0), "r*")


def grad(x):
    c1 = x[0]**2 - x[0] + x[1]**2 + x[1] + 0.5
    cos_t = np.cos(0.5*x[0]*x[1])
    sin_t = np.sin(0.5*x[0]*x[1])
    return np.array([
        (2*x[0]-1)*cos_t - 0.5*x[1]*c1*sin_t,
        (2*x[1]+1)*cos_t - 0.5*x[0]*c1*sin_t
    ])


cont_fig, cont_ax = plt.subplots()
cont_ax.set(xlabel="x", ylabel="y")
cont_ax.set_title("Contour plot with iterates")
cont_ax.contour(x, y, z, levels=30)

bounds = ((-1, 1), (-2, 2))

for i, xn, fxn, grad_xn in descend(func, x0, grad, bounds):
    if i > 0:
        cont_ax.plot([xnm1[0], xn[0]], [xnm1[1], xn[1]], "k*--")
    xnm1, grad_xnm1 = xn, grad_xn

print(f"iterations={i}")
print(f"min val at {xn}")
print(f"min func value = {fxn}")



plt.show()