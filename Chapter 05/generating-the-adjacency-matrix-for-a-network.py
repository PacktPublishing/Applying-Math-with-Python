import numpy as np
import networkx as nx

G = nx.dense_gnm_random_graph(5, 5, seed=12345)

matrix = nx.adjacency_matrix(G).todense()
print(matrix)
# [[0 0 1 0 0]
#  [0 0 1 1 0]
#  [1 1 0 0 1]
#  [0 1 0 0 1]
#  [0 0 1 1 0]]

paths_len_4 = np.linalg.matrix_power(matrix, 4)
print(paths_len_4)
# [[ 3 5  0  0 5]
#  [ 5 9  0  0 9]
#  [ 0 0 13 10 0]
#  [ 0 0 10  8 0]
#  [ 5 9  0  0 9]]
