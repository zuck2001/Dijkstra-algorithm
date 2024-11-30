import heapq

def dijkstra(graph, start):
    """
    Find the shortest path from the start node to all other nodes in the graph.

    Args:
    graph (dict): Adjacency list representation of the graph.
    start (str): Starting node.

    Returns:
    dict: Shortest distances from the start node to each node.
    """
    # Priority queue to hold the nodes and their current distances
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if we find a longer distance in the priority queue
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path is found, update and push to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage
if __name__ == "__main__":
    # Define a graph as an adjacency list
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)

    print(f"Shortest paths from {start_node}:")
    for node, distance in shortest_paths.items():
        print(f" - To {node}: {distance}")
