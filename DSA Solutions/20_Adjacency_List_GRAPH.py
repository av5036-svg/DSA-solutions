graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}

print(graph)
# Output the adjacency list
for node in graph:
    print(f"{node}: {graph[node]}")