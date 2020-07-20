import numpy as np
from scipy import sparse

T = sparse.diags([-1, 2, -1], (-1, 0, 1), shape=(5, 5), format="csr")
T.toarray()
# array([[ 2, -1,  0,  0,  0],
#        [-1,  2, -1,  0,  0],
#        [ 0, -1,  2, -1,  0],
#        [ 0,  0, -1,  2, -1],
#        [ 0,  0,  0, -1,  2]])

from scipy.sparse import linalg
linalg.spsolve(T.tocsr(), np.array([1, 2, 3, 4, 5]))
# array([ 5.83333333, 10.66666667, 13.5, 13.33333333, 9.16666667])
