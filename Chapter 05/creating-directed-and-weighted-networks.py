import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_nodes_from(range(5))

G.add_edge(0, 1, weight=1.0)
G.add_weighted_edges_from([
    (1, 2, 0.5), (1, 3, 2.0), (2, 3, 0.3), (3, 2, 0.3),
    (2, 4, 1.2), (3, 4, 0.8)
])


fig, ax = plt.subplots()
pos = {0: (-1, 0), 1: (0, 0), 2: (1, 1), 3: (1, -1), 4: (2, 0)}
nx.draw(G, ax=ax, pos=pos, with_labels=True)
ax.set_title("Weighted, directed network")

plt.show()


adj_mat = nx.adjacency_matrix(G).todense()
print(adj_mat)
# [[0. 1. 0.  0.  0. ]
#  [0. 0. 0.5 2.  0. ]
#  [0. 0. 0.  0.3 1.2]
#  [0. 0. 0.3 0.  0.8]
#  [0. 0. 0.  0.  0. ]]
