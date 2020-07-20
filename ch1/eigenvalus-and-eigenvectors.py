import numpy as np

from numpy import linalg

A = np.array([[3, -1, 4], [-1, 0, -1], [4, -1, 2]])

v, B = linalg.eig(A)

i = 0  # first eigenvalue/eigenvector pair
lambda0 = v[i]
print(lambda0)
# 6.823156164525971
x0 = B[:, i]  # ith column of B
print(x0)
# array([ 0.73271846, -0.20260301, 0.649672352])

linalg.norm(x0)  # 1.0  - eigenvalues are normalised.


lhs = A @ x0
rhs = lambda0*x0
linalg.norm(lhs - rhs)  # 2.8445583831733384e-15 - very small.

