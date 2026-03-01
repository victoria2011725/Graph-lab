from collections import deque 
def bfs_path(residual_graph,source,sink,parent):
    visited = {source}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        if u == sink:
            return True
        for v,cap in residual_graph[u].items():
            if v not in visited and cap >0:
                visited.add(v)
                queue.append(v)
                parent[v] = u 
    return False 

def edmond_karp(graph,source,sink):
    max_flow = 0
    parent = {}
    for node in graph.edges:
        parent[node] = None 
    residual_graph = {}
    for u in graph.edges:
        if u not in residual_graph:
            residual_graph[u] = {}
        for v,cap in graph.edges[u].items():
            if v not in residual_graph:
                residual_graph[v] = {}
            residual_graph[u][v] = cap 
            residual_graph[v][u] = 0 
    while bfs(residual_graph,source,sink,parent):
        bottleneck = float("inf")
        current = sink 
        while parent[current] is not None:
            prev = parent[current]
            bottleneck = min(bottleneck,residual_graph[prev][current])
            current = prev 
        max_flow += bottleneck
        current = sink 
        while parent[current] is not None:
            prev = parent[current]
            residual_graph[prev][current] -= bottleneck 
            residual_graph[current][prev] += bottleneck 
        for node in parent:
            parent[node] = None 
    return max_flow 