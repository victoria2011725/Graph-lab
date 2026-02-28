def bellman_ford(graph,source):
    distances = {}
    prev = {}
    for node in graph.nodes():
        distances[node] = float("inf")
        prev[node] = None
    distances[source] = 0

    for _ in range(len(graph.nodes)-1):
        changed = False 
        for u,v,weight in graph.edges():
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                prev[v] = u 
                changed = True
            if not changed:
                break 
    # negative cycle check
    for weight,u,v in graph.edges():
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                return None
    
    return distances,prev 
    