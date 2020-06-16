from time import time
from functools import wraps
import matplotlib.pyplot as plt

from mandelbrot.python_mandel import compute_mandel as compute_mandel_py
from mandelbrot.hybrid_mandel import compute_mandel as compute_mandel_hy
from mandelbrot.cython_mandel import compute_mandel as compute_mandel_cy

def timer(func, name):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time()
        val = func(*args, **kwargs)
        t_end = time()
        print(f"Time taken for {name}: {t_end - t_start}")
        return val
    return wrapper

mandel_py = timer(compute_mandel_py, "Python")
mandel_hy = timer(compute_mandel_hy, "Hybrid")
mandel_cy = timer(compute_mandel_cy, "Cython")

Nx = 320
Ny = 240
steps = 255

mandel_py(Nx, Ny, steps)
mandel_hy(Nx, Ny, steps)
vals = mandel_cy(Nx, Ny, steps)

fig, ax = plt.subplots()
ax.imshow(vals.T, extent=(-2.5, 0.5, -1.2, 1.2))

plt.show()