from collections import deque 
def bfs_path(residual_graph,source,sink,parent):
    visited = {source}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v,cap in residual_graph[u].items():
            if v not in visited and cap >0:
                parent[v] = u 
                visited.add(v)
                queue.append(v)
                if v == sink:
                    return True 
    return False 

def edmond_karp(graph,source,sink):
    max_flow = 0
    parent = {}
    for node in graph.adj:
        parent[node] = None 
    residual_graph = {}
    for u in graph.adj:
        if u not in residual_graph:
            residual_graph[u] = {}
        for v,cap in graph.adj[u].items():
            if v not in residual_graph:
                residual_graph[v] = {}
            residual_graph[u][v] = cap 
            residual_graph[v][u] = 0 
    while bfs_path(residual_graph,source,sink,parent):
        print("Found augmentng path")
        bottleneck = float("inf")
        current = sink 
        while current != source:
            prev = parent[current]
            bottleneck = min(bottleneck,residual_graph[prev][current])
            current = prev 
        max_flow += bottleneck
        current = sink 
        while current !=  source:
            prev = parent[current]
            residual_graph[prev][current] -= bottleneck 
            residual_graph[current][prev] += bottleneck 
            current = prev
        parent = {node: None for node in graph.adj}
    return max_flow 