def kruskal(graph):
    edges = graph.get_edges()
    edges.sort()
    mst = []
    parent = {}
    rank = {}

    for node in graph.nodes():
        parent[node] = node 
        rank[node] = 0

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(x,y):
        x_root = find(x)
        y_root = find(y)
        if x_root == y_root:
            return 
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root 
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root 
        else:
            parent[y_root] = x_root 
            rank[x_root] += 1 
            
    for weight,u,v in edges:
        if find(u) != find(v):
            mst.append((weight,u,v))
            union(u,v)

    return mst 