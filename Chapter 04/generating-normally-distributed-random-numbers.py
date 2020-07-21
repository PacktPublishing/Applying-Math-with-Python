
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import default_rng
rng = default_rng(12345)


mu = 5.0  # mean value
sigma = 3.0 # standard deviation
rands = rng.normal(loc=mu, scale=sigma, size=10000)


fig, ax = plt.subplots()
ax.hist(rands, bins=20)
ax.set_title("Histogram of normally distributed data")
ax.set_xlabel("Value")
ax.set_ylabel("Density")

def normal_dist_curve(x):
    return 10000*np.exp(-0.5*((x-mu)/sigma)**2)/(sigma*np.sqrt(2*np.pi))

x_range = np.linspace(-5, 15)
y = normal_dist_curve(x_range)
ax.plot(x_range, y, "k--")



plt.show()
