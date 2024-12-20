def bfs_tree(tree, start=0):
    queue = [start]
    traversal = []
    visited = set()
    while queue:
        current_node = queue.pop(0)
        if current_node in visited:
            continue
        visited.add(current_node)
        traversal.append(current_node)
        children = tree[current_node]
        for child in children:
            if child not in visited:
                queue.append(child)
    return traversal

graph = [
    [1, 3],  # Neighbors of vertex 0
    [0, 2],  # Neighbors of vertex 1
    [1, 4],  # Neighbors of vertex 2
    [0, 5],  # Neighbors of vertex 3
    [2, 5],  # Neighbors of vertex 4
    [3, 4]   # Neighbors of vertex 5
]
traversal = bfs_tree(graph)
print("\nComplete BFS traversal order:")
print(" -> ".join(map(str,traversal)))
