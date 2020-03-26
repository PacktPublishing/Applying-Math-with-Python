
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
complete_part = nx.complete_graph(4)
cycle_part = nx.cycle_graph(range(4, 9))
G.update(complete_part)
G.update(cycle_part)
G.add_edges_from([(0, 8), (3, 4)])

fig, ax = plt.subplots()
nx.draw_circular(G, ax=ax, with_labels=True)
ax.set_title("Network with different clustering behavior")

plt.show()

cluster_coeffs = nx.clustering(G)

for i in [0, 2, 6]:
    print(f"Node {i}, clustering {cluster_coeffs[i]}")
# Node 0, clustering 0.5
# Node 2, clustering 1.0
# Node 6, clustering 0

av_clustering = nx.average_clustering(G)
print(av_clustering)
# 0.3333333333333333
