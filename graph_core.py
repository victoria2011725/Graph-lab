class Graph:
    def __init__(self, directed = True):
        self.edges= {}
        self.directed = directed

    def add_node(self,node):
        self.edges[node] = {}

    def remove_node(self,node):
        self.edges.pop(node,None)
        for u in list(self.edges.keys()):
            if node in self.edges[u]:
                self.edges[u].pop(node)

    def add_edge(self,u,v,weight=1):
        if u not in self.edges:
            self.edges[u] = {}
        if v not in self.edges:
            self.edges[v] = {}
        # forwards edge
        self.edges[u][v] = weight
        # if not direced add reverse edge
        if not self.directed:
            self.edges[v][u] = weight 

    def remove_edges(self,u,v):
        self.edges[u].pop(v,None)

    def neighbours(self,node):
        return list(self.edges[node].keys())

    def get_weight(self,u,v):
        return self.edges[u][v]
    
    def nodes(self):
        return list(self.edges.keys())
    
    def edges(self):
        edges = []
        for u in self.edges:
            for v,weight in self.edges[u].items():
                edges.append((u,v,weight))
        return edges 
    def has_negative_weights(self):
        for u in self.edges:
            for v,weight in self.edges[u].items():
                if weight < 0:
                    return True 
        return False 