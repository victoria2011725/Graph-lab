from collections import deque 
def bfs(graph,source,target):
    queue = deque([source])
    parent = {source:None}
    while queue:
        current_node = queue.popleft()
        if current_node == target:
            path = []
            current = target 
            while current is not None:
                path.append(current) 
                current = parent[current] 
            path.reverse()
            return path 
        for neighbour in graph.neighbours(current_node):
            if neighbour not in parent:
                parent[neighbour] = current_node 
                queue.append(neighbour)
    return None 