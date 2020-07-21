import numpy as np
import matplotlib.pyplot as plt

from numpy.random import default_rng
rng = default_rng(12345)

 
def underlying(x, params):
    return params[0]*x**2 + params[1]*x + params[2]


size = 100
true_params = [2, -7, 6]

x_vals = np.linspace(-5, 5, size)
raw_model = underlying(x_vals, true_params)
noise = rng.normal(loc=0.0, scale=10.0, size=size)
sample = raw_model + noise

fig1, ax1 = plt.subplots()
ax1.scatter(x_vals, sample, label="Sampled data")
ax1.plot(x_vals, raw_model, "k--", label="Underlying model")
ax1.set_title("Sampled data")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

plt.show()


import pymc3 as pm


with pm.Model() as model:
    params = pm.Normal("params", mu=1, sigma=1, shape=3)
    y = underlying(x_vals, params)
    y_obs = pm.Normal("y_obs", mu=y, sigma=2, observed=sample)
    trace = pm.sample(cores=4)




fig2, axs2 = plt.subplots(1, 3, tight_layout=True)

pm.plot_posterior(trace, ax=axs2)

plt.show()

estimated_params = trace["params"].mean(axis=0)
print("Estimated parameters", estimated_params)

estimated = underlying(x_vals, estimated_params)

fig3, ax3 = plt.subplots()
ax3.plot(x_vals, raw_model, "k", label="True model")
ax3.plot(x_vals, estimated, "k--", label="Estimated model")
ax3.set_title("Plot of true and estimated models")
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.legend()



plt.show()


#plt.show()








