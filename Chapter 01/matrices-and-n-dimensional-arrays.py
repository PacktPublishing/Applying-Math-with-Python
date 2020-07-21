import numpy as np

mat = np.array([[1, 2], [3, 4]])
vec = np.array([1, 2])

mat.shape  # (2, 2)
vec.shape  # (2,)


mat.reshape(4,)
# array([1, 2, 3, 4])


mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
mat3 = [[9, 10], [11, 12]]

arr_3d = np.array([mat1, mat2, mat3])
arr_3d.shape  # (3, 2, 2)

mat[0, 0] # 1 - top left element
mat[1, 1] # 4 - bottom right element

mat[:, 0] # array([1, 3])


