import networkx as nx


G = nx.Graph()

G.add_node(1)
G.add_node(2)

G.add_nodes_from([3, 4, 5, 6])

G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4), (3, 5), (3, 6), (4, 5), (5, 6)])



print(G.nodes)
print(G.edges)
