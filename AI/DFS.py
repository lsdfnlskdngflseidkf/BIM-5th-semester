def dfs_rec(adj, visited, s):
    visited[s] = True
    print(s, end=" ")
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)

# Correct adjacency list representation for the graph
graph = [
    [1, 2],  # Neighbors of vertex 0
    [0],     # Neighbors of vertex 1
    [0, 3, 4],  # Neighbors of vertex 2
    [2],     # Neighbors of vertex 3
    [2]      # Neighbors of vertex 4
]

source = 0  # Starting vertex
print("DFS from source:", source)
visited = [False] * len(graph)
dfs_rec(graph, visited, source)
