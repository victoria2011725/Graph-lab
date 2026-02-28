def floyd_warshall(graph):
    distances = {}
    prev = {}
    for i in graph.nodes():
        distances[i] = {}
        prev[i] = {}
        for j in graph.nodes():
            distances[i][j] = float("inf")
            prev[i][j] = None 
    for i in graph.nodes():
        distances[i][i] = 0 
        for j,weight in graph.edges[i].items():
            distances[i][j] = weight 
            prev[i][j] = i 
    for intermediate in graph.nodes():
        for start in graph.nodes():
            for end in graph.nodes():
                if distances[start][intermediate] != float("inf") and distances[intermediate][end] != float("inf"):
                    if distances[start][intermediate] + distances[intermediate][end] < distances[start][end]:
                        distances[start][end] = distances[start][intermediate] + distances[intermediate][end]
                        prev[start][end] = prev[intermediate][end]
    # negative cycle check 
    for i in graph.nodes():
        if distances[i][i] < 0:
            return None 
    return distances,prev 
