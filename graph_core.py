class Graph:
    def __init__(self, directed = True):
        self.adj= {}
        self.directed = directed

    def add_node(self,node):
        if node not in self.adj:
            self.adj[node] = {}

    def remove_node(self,node):
        self.adj.pop(node,None)
        for u in list(self.adj.keys()):
            if node in self.adj[u]:
                self.adj[u].pop(node)

    def add_edge(self,u,v,weight=1):
        if u not in self.adj:
            self.adj[u] = {}
        if v not in self.adj:
            self.adj[v] = {}
        self.adj[u][v] = weight 

        if not self.directed:
            self.adj[v][u] = weight 

    def remove_edges(self,u,v):
        if u in self.adj:
            self.adj[u].pop(v,None)

    def neighbours(self,node):
        return list(self.adj[node].keys())
    def get_weight(self,u,v):
        return self.adj[u][v]
    
    def nodes(self):
        return list(self.adj.keys())
    
    def edge_list(self):
        edges = []
        for u in self.adj:
            for v,weight in self.adj[u].items():
                edges.append((u,v,weight))
        return edges 
    def sort_edges(self):
        edges = []
        for u in self.adj:
            for v,weight in self.adj[u].items():
                edges.append((weight,u,v))
        return edges 
        
    
    def has_negative_weights(self):
        for u in self.adj:
            for v,weight in self.adj[u].items():
                if weight < 0:
                    return True 
        return False 