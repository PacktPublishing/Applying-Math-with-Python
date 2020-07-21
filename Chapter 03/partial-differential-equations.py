import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

alpha = 1
x0 = 0 # Left hand x limit
xL = 2 # Right hand x limit

N = 10
x = np.linspace(x0, xL, N+1)
h = (xL - x0) / N

k = 0.01
steps = 100
t = np.array([i*k for i in range(steps+1)])

r = alpha*k / h**2
assert r < 0.5, f"Must have r < 0.5, currently r={r}"

from scipy import sparse
diag = [1, *(1-2*r for _ in range(N-1)), 1]
abv_diag = [0, *(r for _ in range(N-1))]
blw_diag = [*(r for _ in range(N-1)), 0]

A = sparse.diags([blw_diag, diag, abv_diag], (-1, 0, 1), shape=(N+1, N+1), dtype=np.float64, format="csr")

u = np.zeros((steps+1, N+1), dtype=np.float64)

def initial_profile(x):
    return 3*np.sin(np.pi*x/2)

u[0, :] = initial_profile(x)

for i in range(steps):
    u[i+1, :] = A @ u[i, :]


X, T = np.meshgrid(x, t)
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot_surface(T, X, u, cmap="hot")
ax.set_title("Solution of the heat equation")
ax.set_xlabel("t")
ax.set_ylabel("x")
ax.set_zlabel("u")

plt.show()

