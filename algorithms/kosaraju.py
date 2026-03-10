def kosaraju(graph):
    stack = []
    SCCs = []
    
    def fill_order(u, visited):
        visited.add(u)
        for v in graph.neighbours(u):
            if v not in visited:
                fill_order(v, visited)
        stack.append(u)

  
    def get_transpose():
        transpose = {node: {} for node in graph.nodes()}
        for u in graph.nodes():
            for v, weight in graph.adj[u].items():
                transpose[v][u] = weight 
        return transpose 

    def dfs_collect(u, transpose, scc, visited):
        visited.add(u)
        scc.append(u)
        for v in transpose.get(u, {}):
            if v not in visited:
                dfs_collect(v, transpose, scc, visited)
    visited = set()
    for node in graph.nodes():
        if node not in visited:
            fill_order(node, visited)

    transpose = get_transpose()
    visited = set()
    
    while stack:
        u = stack.pop()
        if u not in visited:
            scc = []
            dfs_collect(u, transpose, scc, visited)
            SCCs.append(scc)
            
    return SCCs