
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(range(10))
G.add_edges_from([
    (0, 1), (1, 2), (2, 3), (2, 4), 
    (2, 5), (3, 4), (4, 5), (6, 7),
    (6, 8), (6, 9), (7, 8), (8, 9)
])

fig, ax = plt.subplots()
nx.draw_circular(G, ax=ax, with_labels=True)
ax.set_title("Simple network")

plt.show()

print(nx.info(G))
# Name: 
# Type: Graph
# Number of nodes: 10
# Number of edges: 12
# Average degree: 2.4000

for i in [0, 2, 7]:
    degree = G.degree[i]
    print(f"Degree of {i}: {degree}")
# Degree of 0: 1
# Degree of 2: 4
# Degree of 7: 2

components = list(nx.connected_components(G))
print(components)


density = nx.density(G)
print("Density", density)
# Density 0.26666666666666666

is_planar, _ = nx.check_planarity(G)
print("Is planar", is_planar)
# Is planar True

