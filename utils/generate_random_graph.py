import networkx as nx
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 3:
    print("Usage: python generate_random_graph.py <degree> <number of nodes>")
    sys.exit()

try:
    degree = int(sys.argv[1])
    number_of_nodes = int(sys.argv[2])
except ValueError:
    print("Usage: python generate_random_graph.py <degree> <number of nodes>")
    sys.exit()

if degree < 0 or number_of_nodes < 0:
    print("Usage: python generate_random_graph.py <degree> <number of nodes>")
    sys.exit()

if degree > number_of_nodes:
    print("The degree must be smaller than the number of nodes")
    sys.exit()

G = nx.random_regular_graph(degree, number_of_nodes)

print(G.edges())

nx.draw(G, with_labels=True)

plt.savefig("random_graph.png")
