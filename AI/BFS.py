def bfs_tree(tree, start='r'):
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
tree = {
    'r': ['a', 'b'],
    'a': ['c'],
    'b': ['g'],
    'c': ['f', 'd'],
    'g': ['i'],
    'd': [],
    'f': ['k'],
    'i': [],
    'k': []
}
traversal = bfs_tree(tree, 'r')
print("\nComplete BFS traversal order:")
print(" -> ".join(traversal))
