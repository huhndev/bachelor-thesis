import networkx as nx
import matplotlib.pyplot as plt
import sys

# Check if the user has passed the correct number of parameters
if len(sys.argv) != 3:
    print("Usage: python generate_random_graph.py <degree> <number of nodes>")
    sys.exit()

# Check if the parameters are integers
try:
    degree = int(sys.argv[1])
    number_of_nodes = int(sys.argv[2])
except ValueError:
    print("Usage: python generate_random_graph.py <degree> <number of nodes>")
    sys.exit()

# Check if the parameters are positive
if degree < 0 or number_of_nodes < 0:
    print("Usage: python generate_random_graph.py <degree> <number of nodes>")
    sys.exit()

# Check if the parameters are valid
if degree > number_of_nodes:
    print("The degree must be smaller than the number of nodes")
    sys.exit()

# Create the graph
G = nx.random_regular_graph(degree, number_of_nodes)

# Print the edges of the graph
print(G.edges())

# Draw the graph
nx.draw(G, with_labels=True)

# Save the graph as a png file
plt.savefig("random_graph.png")
