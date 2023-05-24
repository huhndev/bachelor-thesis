import networkx as nx
import matplotlib.pyplot as plt
import sys

# Create the graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1,2), (2,3), (3,4)])

# Set edge attributes
edge_colors = {(1,2):'red', (2,3):'blue', (3,4):'green'}
nx.set_edge_attributes(G, edge_colors, 'color')

# Draw the graph
nx.draw(G, with_labels=True, edge_color=list(edge_colors.values()))

# Save the graph as a png file
plt.savefig("graph.png")
