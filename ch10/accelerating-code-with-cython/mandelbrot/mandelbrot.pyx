
import numpy as np
cimport numpy as np
cimport cython

ctypedef Py_ssize_t Int
ctypedef np.float64_t Double

cdef int in_mandel(Double cx, Double cy, int max_iter):
    cdef Double x = cx
    cdef Double y = cy
    cdef Double x2, y2
    cdef Int i
    for i in range(max_iter):
        x2 = x**2
        y2 = y**2
        if (x2 + y2) >= 4:
            return i
        y = 2.0*x*y + cy
        x = x2 - y2 + cx
    return max_iter

@cython.boundscheck(False)
@cython.wraparound(False)
def compute_mandel(int N_x, int N_y, int N_iter):
    cdef double xlim_l = -2.5
    cdef double xlim_u = 0.5
    cdef double ylim_l = -1.2
    cdef double ylim_u = 1.2

    cdef np.ndarray x_vals = np.linspace(xlim_l, xlim_u, N_x, dtype=np.float64)
    cdef np.ndarray y_vals = np.linspace(ylim_l, ylim_u, N_y, dtype=np.float64)

    cdef np.ndarray height = np.empty((N_x, N_y), dtype=np.int64)
    cdef Int i, j

    for i in range(N_x):
        for j in range(N_y):
            height[i, j] = in_mandel(x_vals[i], y_vals[j], N_iter)
    return height