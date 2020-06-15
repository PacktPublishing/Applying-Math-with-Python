import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def f(t, y):
    return -0.2*y

t_range = (0, 5)

T0 = np.array([50.])

def true_solution(t):
    return 50.*np.exp(-0.2*t)

sol = integrate.solve_ivp(f, t_range, T0, max_step=0.1)

t_vals = sol.t
T_vals = sol.y[0, :]

fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True)

ax1.plot(t_vals, T_vals)
ax1.set_xlabel("$t$")
ax1.set_ylabel("$T$")
ax1.set_title("Solution of the cooling equation")


err = np.abs(T_vals - true_solution(t_vals))
ax2.semilogy(t_vals, err)
ax2.set_xlabel("$t$")
ax2.set_ylabel("Error")
ax2.set_title("Error in approximation")

plt.show()
