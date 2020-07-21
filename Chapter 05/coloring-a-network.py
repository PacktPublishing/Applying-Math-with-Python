
import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(3)
G.add_nodes_from(range(3, 7))
G.add_edges_from([
    (2, 3), (2, 4), (2, 6), (0, 3), (0, 6), (1, 6),
    (1, 5), (2, 5), (4, 5)
])


fig, ax = plt.subplots()
nx.draw_circular(G, ax=ax, with_labels=True)
ax.set_title("Scheduling network")

plt.show()



coloring = nx.greedy_color(G)
print("Coloring", coloring)
# Coloring {2: 0, 0: 1, 1: 2, 5: 1, 6: 3, 3: 2, 4: 2}

different_colors = set(coloring.values())
print("Different colors", different_colors)
# Different colors {0, 1, 2, 3}
