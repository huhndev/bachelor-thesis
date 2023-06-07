import networkx as nx

G = nx.Graph()

G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
G.add_edges_from([(0,2), (0,3), (0,9),
                  (1,6), (1,7), (1,8),
                  (2,7), (2,8),
                  (3,5), (3,9),
                  (4,5), (4,6), (4,8),
                  (5,9),
                  (6,7),
                  (0,4), (1,3), (2,5), (6,9), (7,8)])
paths = nx.shortest_simple_paths(G, 0, 5)

for path in paths:
    print(path)
