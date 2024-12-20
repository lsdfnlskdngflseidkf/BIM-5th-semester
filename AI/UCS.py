def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start)]
    cost_so_far = {start: 0}
    parent = {start: None}

    while priority_queue:
        priority_queue.sort()
        current_cost, current_node = priority_queue.pop(0)
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1], cost_so_far[goal]

        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = current_node
                priority_queue.append((new_cost, neighbor))

    return None, float('inf')

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_node = 'A'
goal_node = 'D'
path, cost = uniform_cost_search(graph, start_node, goal_node)
if path:
    print("Path found:", path)
    print("Total cost:", cost)
else:
    print("No path found")
