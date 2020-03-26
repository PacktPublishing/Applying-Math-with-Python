
import networkx as nx
import matplotlib.pyplot as plt

from numpy.random import default_rng
rng = default_rng(12345)

G = nx.gnm_random_graph(10, 17, seed=12345)

fig, ax = plt.subplots()
nx.draw_circular(G, ax=ax, with_labels=True)
ax.set_title("Random network for shortest path finding")

plt.show()

for u, v in G.edges:
    G.edges[u, v]["weight"] = rng.integers(5, 15)


path = nx.shortest_path(G, 7, 9, weight="weight")
print(path)
# [7, 5, 2, 9]

length = nx.shortest_path_length(G, 7, 9, weight="weight")
print("Length", length)
# Length 32

