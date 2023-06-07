import networkx as nx
import matplotlib.pyplot as plt
import sys

# Create the graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
G.add_edges_from([(0,2), (0,3), (0,9),
                  (1,6), (1,7), (1,8),
                  (2,7), (2,8),
                  (3,5), (3,9),
                  (4,5), (4,6), (4,8),
                  (5,9),
                  (6,7),
                  (1,9), (3,7), (0,6), (5,8)])

# Set edge attributes
edge_colors = {(0,2):'black', (0,3):'black', (0,9):'black',
               (1,6):'black', (1,7):'black', (1,8):'black',
               (2,7):'black', (2,8):'black',
               (3,5):'black', (3,9):'black',
               (4,5):'black', (4,6):'black', (4,8):'black',
               (5,9):'black',
               (6,7):'black',
               (1,9):'red', (3,7):'red', (0,6):'red', (5,8):'red'}
nx.set_edge_attributes(G, edge_colors, 'color')

colors = nx.get_edge_attributes(G, 'color').values()

# Draw the graph
nx.draw(G, with_labels=True, edge_color=colors)

# Save the graph as a png file
plt.savefig("graph.png")
