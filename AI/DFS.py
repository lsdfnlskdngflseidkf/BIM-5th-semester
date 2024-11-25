def dfs_rec(adj, visited, s):
    visited[s] = True
    print(s, end=" ")
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)

V = 5
graph = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]
source = 1
print("DFS from source:", source)
visited = [False] * len(graph)
dfs_rec(graph, visited, source)
