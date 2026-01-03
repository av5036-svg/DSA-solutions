def dfs(graph, start, visited=set()):
    print(start, end=" ")
    visited.add(start)

    for nbr in graph[start]:
        if nbr not in visited:
            dfs(graph, nbr, visited)
