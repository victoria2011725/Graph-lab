import heapq 
def johnson(graph):
    q = "dummy"
    edges = graph.edge_list()
    for node in graph.nodes():
        edges.append((0,q,node))
    # bellman_ford 
    h = {}
    for node in graph.nodes():
        h[node] = float("inf")
    h[q] = 0 
    for _ in range(len(graph.nodes())):
        changed = False 
        for u,v,weight in edges:
            if h[u] != float("inf") and h[u] + weight < h[v]:
                h[v] = h[u] + weight 
                changed = True 
        if not changed:
            break 
    # negative cycle check
    for u,v,weight in edges:
            if h[u] != float("inf") and h[u] + weight < h[v]:
                return "None"
    # reweight 
    reweighted = {}
    for u,v,weight in edges:
        if u not in reweighted:
            reweighted[u] = {}
        reweighted[u][v] = weight + h[u] - h[v]
    #dijkstra 
    distances = {}
    paths = {}

    for start in graph.nodes():
        distances[start] = {}
        paths[start] = {}
        dist={}
        prev={}
        for node in graph.nodes():
            dist[node] = float("inf")
            prev[node] = None 
        dist[start] = 0 
        priority_queue = [(0,start)]
        while priority_queue:
            current_distance,current_node = heapq.heappop(priority_queue)
            if current_distance > dist[current_node]:
                continue 
            for neighbour,weight in reweighted[current_node].items():
                distance = current_distance + weight
                if distance < dist[neighbour]:
                    dist[neighbour] = distance 
                    prev[neighbour] = current_node 
                    heapq.heappush(priority_queue,(distance,neighbour))
        for target in graph.nodes():
            distances[start][target] = dist[target] - h[start] + h[target]
            if distances[start][target] == float("inf"):
                path[start][target] = None 
            else:
                path = []
                current = target 
                while current is not None:
                    path.append(current)
                    current = prev[current]
                path.reverse()
                paths[start][target] = path 

    return distances,paths
        
