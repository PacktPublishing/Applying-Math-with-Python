import numpy as np
from numpy import linalg

A = np.array([[3, -2, 1], [1, 1, -2], [-3, -2, 1]])
b = np.array([7, -4, 1])

linalg.solve(A, b)  # array([ 1., -1., 2.])


