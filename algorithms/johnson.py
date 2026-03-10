import heapq 

def johnson(graph):
    nodes = list(graph.nodes())
    q = "dummy"
    edges = list(graph.edge_list()) 
    
    for node in nodes:
        edges.append((q, node, 0)) 

    # Bellman ford
    h = {node: float("inf") for node in nodes}
    h[q] = 0
    
    num_nodes = len(nodes) + 1
    for _ in range(num_nodes):
        changed = False 
        for u, v, weight in edges:
            if h[u] != float("inf") and h[u] + weight < h[v]:
                h[v] = h[u] + weight 
                changed = True 
        if not changed:
            break 
    for u, v, weight in edges:
            if h[u] != float("inf") and h[u] + weight < h[v]:
                return "Negative cycle present"

    # Reweight
    reweighted = {node: {} for node in nodes}
    for u, v, weight in graph.edge_list():
        reweighted[u][v] = weight + h[u] - h[v]

    # Dijkstra
    distances = {}
    paths = {}

    for start in nodes:
        distances[start] = {}
        paths[start] = {}
        dist = {node: float("inf") for node in nodes}
        prev = {node: None for node in nodes}
        
        dist[start] = 0 
        priority_queue = [(0, start)]
        
        while priority_queue:
            d, u = heapq.heappop(priority_queue)
            if d > dist[u]:
                continue 
            
            for v, weight in reweighted[u].items():
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight 
                    prev[v] = u 
                    heapq.heappush(priority_queue, (dist[v], v))
        
        for target in nodes:
            if dist[target] == float("inf"):
                distances[start][target] = float("inf")
                paths[start][target] = None 
            else:
                distances[start][target] = dist[target] - h[start] + h[target]
                path_list = []
                curr = target 
                while curr is not None:
                    path_list.append(curr)
                    curr = prev[curr]
                paths[start][target] = path_list[::-1]

    return distances, paths