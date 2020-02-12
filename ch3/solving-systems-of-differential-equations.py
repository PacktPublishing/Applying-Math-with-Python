

import numpy as np
import matplotlib.pyplot as plt


def predator_prey_system(t, y):
    return np.array([5*y[0] - 0.1*y[0]*y[1], 0.1*y[1]*y[0] - 6*y[1]])


p = np.linspace(0, 100, 25)
w = np.linspace(0, 100, 25)
P, W = np.meshgrid(p, w)

dp, dw = predator_prey_system(0, np.array([P, W]))

fig, ax = plt.subplots()
ax.quiver(P, W, dp, dw)
ax.set_title("Population dynamics for two competing species")
ax.set_xlabel("P")
ax.set_ylabel("W")


initial_conditions = np.array([85, 40])

from scipy import integrate
sol = integrate.solve_ivp(predator_prey_system, (0., 5.), initial_conditions, max_step=0.01)


ax.plot(initial_conditions[0], initial_conditions[1], "ko")
ax.plot(sol.y[0, :], sol.y[1, :], "k", linewidth=0.5)

plt.show()

