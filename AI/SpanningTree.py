import heapq

def prim_mst(graph, start_node):
    # Number of nodes in the graph
    n = len(graph)
    
    # Create a priority queue (min-heap)
    min_heap = []
    
    # Initialize a list to keep track of nodes included in the MST
    in_mst = [False] * n
    
    # Store the minimum weight edge to add to the MST for each node
    min_edge = [(float('inf'), -1)] * n  # (weight, parent)
    
    # Start with the given node
    min_edge[start_node] = (0, -1)
    heapq.heappush(min_heap, (0, start_node))  # Push the starting node with 0 weight
    
    mst_weight = 0  # The total weight of the MST
    mst_edges = []  # List to store the edges of the MST
    
    while min_heap:
        # Extract the node with the smallest weight edge
        weight, node = heapq.heappop(min_heap)
        
        # Skip if this node is already in the MST
        if in_mst[node]:
            continue
        
        # Include this node in the MST
        in_mst[node] = True
        mst_weight += weight
        
        # If the parent is not -1, add the edge to the MST
        if min_edge[node][1] != -1:
            mst_edges.append((min_edge[node][1], node, weight))
        
        # Update the priority queue for the neighboring nodes
        for neighbor, edge_weight in graph[node]:
            if not in_mst[neighbor] and edge_weight < min_edge[neighbor][0]:
                min_edge[neighbor] = (edge_weight, node)
                heapq.heappush(min_heap, (edge_weight, neighbor))
    
    return mst_weight, mst_edges

def input_graph():
    n = int(input("Enter the number of vertices: "))
    graph = {i: [] for i in range(n)}
    
    print(f"Enter the edges in the format 'u v weight' (enter 'done' to finish):")
    while True:
        edge_input = input()
        if edge_input.lower() == 'done':
            break
        u, v, weight = map(int, edge_input.split())
        graph[u].append((v, weight))
        graph[v].append((u, weight))  # Since it's an undirected graph
    return graph

def main():
    graph = input_graph()
    start_node = int(input("Enter the starting vertex (0-based index): "))
    
    mst_weight, mst_edges = prim_mst(graph, start_node)

    print("\nMinimum Spanning Tree Weight:", mst_weight)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"{u} - {v} ({weight})")

if __name__ == "__main__":
    main()
