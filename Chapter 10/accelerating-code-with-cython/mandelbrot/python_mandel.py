import numpy as np

def in_mandel(cx, cy, max_iter):
    x = cx
    y = cy
    for i in range(max_iter):
        x2 = x**2
        y2 = y**2
        if (x2 + y2) >= 4:
            return i
        y = 2.0*x*y + cy
        x = x2 - y2 + cx
    return max_iter

def compute_mandel(N_x, N_y, N_iter):
    xlim_l = -2.5
    xlim_u = 0.5
    ylim_l = -1.2
    ylim_u = 1.2
    x_vals = np.linspace(xlim_l, xlim_u, N_x, dtype=np.float64)
    y_vals = np.linspace(ylim_l, ylim_u, N_y, dtype=np.float64)

    height = np.empty((N_x, N_y), dtype=np.int64)
    for i in range(N_x):
        for j in range(N_y):
            height[i, j] = in_mandel(x_vals[i], y_vals[j], N_iter)
    return height