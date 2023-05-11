import time
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def generate_dense_graph(num_nodes, max_weight=10):
    graph = {i: {} for i in range(num_nodes)}
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                weight = random.randint(1, max_weight)
                graph[i][j] = weight
    return graph

def generate_sparse_graph(num_nodes, max_weight=10, probability=0.2):
    graph = {i: {} for i in range(num_nodes)}
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() <= probability:  # Determine whether to add an edge
                weight = random.randint(1, max_weight)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph

def floyd_algorithm(graph):
    # Get the nodes in the graph and their number.
    nodes = list(graph.keys())
    n = len(nodes)

    # Initialize the distance matrix with infinity for all pairs of nodes.
    dist = np.full((n, n), np.inf)

    # Set the initial distance for adjacent nodes in the graph.
    for i, node in enumerate(nodes):
        dist[i, i] = 0
        for neighbor, weight in graph[node].items():
            j = nodes.index(neighbor)
            dist[i, j] = weight

    # Use dynamic programming to compute the shortest path between all pairs of nodes.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i, k] != np.inf and dist[k, j] != np.inf:
                    new_dist = dist[i, k] + dist[k, j]
                    if new_dist < dist[i, j]:
                        dist[i, j] = new_dist

    # Create a dictionary of shortest paths between all pairs of nodes.
    shortest_paths = {}
    for i in range(n):
        shortest_paths[nodes[i]] = {}
        for j in range(n):
            shortest_paths[nodes[i]][nodes[j]] = dist[i, j]

    return shortest_paths


def dijkstra_algorithm(graph, start_node):
    # Create a dictionary to keep track of the shortest distance to each node from the start node.
    # Initialize all distances to infinity except the start node, which has distance 0.
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    # Create an empty set to keep track of visited nodes.
    visited_nodes = set()

    # Loop until all nodes have been visited.
    while len(visited_nodes) != len(graph):
        # Find the unvisited node with the smallest distance from the start node.
        min_node = None
        for node in distances:
            if node not in visited_nodes:
                if min_node is None or distances[node] < distances[min_node]:
                    min_node = node
        # Mark the node as visited.
        visited_nodes.add(min_node)

        # For each neighbor of the minimum node, calculate a new tentative distance from the start node.
        # If the new distance is smaller than the current distance, update the distance.
        for neighbor_node, weight in graph[min_node].items():
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor_node]:
                distances[neighbor_node] = new_distance

    # Return the dictionary of shortest distances to each node.
    return distances


def draw_graph(graph):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_size=10, font_weight='bold', node_size=700)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): graph[i][j] for i in graph for j in graph[i]})
    plt.show()


# Declare Variables
num_nodes = [5, 10, 15, 20, 30]
dijkstra_t_dense = []
floyd_t_dense = []
dijkstra_t_sparse = []
floyd_t_sparse = []

#calculate the time for each iteration of each algorithm for Dense graph
for n in num_nodes:
    graph = generate_dense_graph(n)
    start_time = time.time()
    dijkstra_algorithm(graph, 0)
    dijkstra_t_dense.append(time.time() - start_time)

    start_time = time.time()
    floyd_algorithm(graph)
    floyd_t_dense.append(time.time() - start_time)

#calculate the time for each iteration of each algorithm for Sparse graph
for n in num_nodes:
    graph = generate_sparse_graph(n)
    start_time = time.time()
    dijkstra_algorithm(graph, 0)
    dijkstra_t_sparse.append(time.time() - start_time)

    start_time = time.time()
    floyd_algorithm(graph)
    floyd_t_sparse.append(time.time() - start_time)

#Plot the time execution of 2 algorithms for Dense graph
plt.plot(num_nodes, dijkstra_t_dense, label="Dijkstra")
plt.plot(num_nodes, floyd_t_dense, label="Floyd")
plt.xlabel("Nr of Nodes")
plt.ylabel("Execution time")
plt.legend()
plt.title("Time Comparison")
plt.show()

#Plot the time execution of 2 algorithms for Sparse graph
plt.plot(num_nodes, dijkstra_t_sparse, label="Dijkstra")
plt.plot(num_nodes, floyd_t_sparse, label="Floyd")
plt.xlabel("Nr of Nodes")
plt.ylabel("Execution time")
plt.legend()
plt.title("Time Comparison")
plt.show()

dense_graph = generate_dense_graph(7)
sparse_graph = generate_sparse_graph(15)

draw_graph(dense_graph)
draw_graph(sparse_graph)

#Floyd's Algorithm Graph Tree
floyd_tree = floyd_algorithm(dense_graph)
draw_graph({node: {neighbor: dense_graph[node][neighbor] for neighbor in dense_graph[node]
                        if floyd_tree[node][neighbor] == dense_graph[node][neighbor]} for node in dense_graph})

#Dijkstra's Algorithm Graph Tree
dijkstra_tree = dijkstra_algorithm(dense_graph, 0)
draw_graph({node: {neighbor: dense_graph[node][neighbor] for neighbor in dense_graph[node]
                        if dijkstra_tree[neighbor] == dijkstra_tree[node] + dense_graph[node][neighbor]} for node in dense_graph})


#--------------------------------------------------------------------------------------------------------------

#Floyd's Algorithm Graph Tree
floyd_tree = floyd_algorithm(sparse_graph)
draw_graph({node: {neighbor: sparse_graph[node][neighbor] for neighbor in sparse_graph[node]
                        if floyd_tree[node][neighbor] == sparse_graph[node][neighbor]} for node in sparse_graph})

#Dijkstra's Algorithm Graph Tree
dijkstra_tree = dijkstra_algorithm(sparse_graph, 0)
draw_graph({node: {neighbor: sparse_graph[node][neighbor] for neighbor in sparse_graph[node]
                        if dijkstra_tree[neighbor] == dijkstra_tree[node] + sparse_graph[node][neighbor]} for node in sparse_graph})

