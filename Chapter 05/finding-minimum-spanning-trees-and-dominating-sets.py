

import networkx as nx
import matplotlib.pyplot as plt


G = nx.gnm_random_graph(15, 22, seed=12345)


fig, ax = plt.subplots()
pos = nx.circular_layout(G)
nx.draw(G, pos=pos, ax=ax, with_labels=True)
ax.set_title("Network with minimum spanning tree overlaid")

min_span_tree = nx.minimum_spanning_tree(G)
print(list(min_span_tree.edges))
# [(0, 13), (0, 7), (0, 5), (1, 13), (1, 11),
#   (2, 5), (2, 9), (2, 8), (2, 3), (2, 12),
#   (3, 4), (4, 6), (5, 14), (8, 10)]

nx.draw_networkx_edges(min_span_tree, pos=pos, ax=ax, width=1.5, edge_color="r")


dominating_set = nx.dominating_set(G)
print("Dominating set", dominating_set)
# Dominating set {0, 1, 2, 4, 10, 14}

plt.show()



