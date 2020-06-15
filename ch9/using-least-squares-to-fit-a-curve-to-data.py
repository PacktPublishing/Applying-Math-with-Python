
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import default_rng
rng = default_rng(12345)

from scipy.optimize import curve_fit



SIZE = 100
x_data = rng.uniform(-3.0, 3.0, size=SIZE)
noise = rng.normal(0.0, 0.8, size=SIZE)

y_data = 2.0*x_data**2 - 4*x_data + noise

fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.set(xlabel="x", ylabel="y", title="Scatter plot of sample data")

fig.savefig("least-squares-scatter-plot.png", dpi=300)


def func(x, a, b, c):
    return a*x**2 + b*x + c

coeffs, _ = curve_fit(func, x_data, y_data)
print(coeffs)
# [ 1.99611157 -3.97522213  0.04546998]

x = np.linspace(-3.0, 3.0, SIZE)
y = func(x, coeffs[0], coeffs[1], coeffs[2])
ax.plot(x, y, "k--")



plt.show()
fig.savefig("least-squares-best-fit.png", dpi=300)