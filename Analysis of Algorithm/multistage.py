import math

# Define the graph as an adjacency matrix (inf means no direct connection)
graph = {
    0: {1: 1, 2: 9, 3: 5},
    1: {4: 11, 5: 4},
    2: {5: 13},
    3: {6: 2},
    4: {7: 18},
    5: {7: 13},
    6: {7: 2},
}

# Define the number of stages and vertices
num_vertices = 8
destination = 7

# Initialize cost and path arrays
cost = [math.inf] * num_vertices
path = [-1] * num_vertices

# Set cost of destination node to 0
cost[destination] = 0

# Calculate the cost array from destination to source
for i in range(destination - 1, -1, -1):
    for neighbor, weight in graph.get(i, {}).items():
        if cost[neighbor] + weight < cost[i]:
            cost[i] = cost[neighbor] + weight
            path[i] = neighbor

# Build the shortest path
shortest_path = []
current = 0
while current != -1:
    shortest_path.append(current)
    current = path[current]

# Display the results
print("Minimum Cost:", cost[0])
print("Shortest Path:", " -> ".join(map(str, shortest_path)))

# Display the table
print("\nTable:")
print(f"{'Vertex (v)':<10}{'Cost (c)':<10}{'Destination (d)':<15}")
print("-" * 35)
for v in range(num_vertices):
    dest = path[v] if path[v] != -1 else "N/A"
    print(f"{v:<10}{cost[v]:<10}{dest:<15}")
