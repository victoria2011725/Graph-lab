class Edge:
    def __init__(self,to,capacity):
        self.to = to 
        self.capacity = capacity 
        self.flow = 0
        self.rev = None 
    
    @property 
    def residual_capacity(self):
        return self.capacity - self.flow 
class FlowGraph:
    def __init__(self):
        self.adj = {}
    
    def add_node(self,node):
        if node not in self.adj:
            self.adj[node] = []
    def add_edge(self,u,v,capacity):
        if u not in self.adj:
            self.add_node(u)
        if v not in self.adj:
            self.add_node(u)
        
        forward = Edge(v,capacity)
        backward = Edge(u,0)

        forward.rev = backward 
        backward.rev = forward 

        self.adj[u].append(forward)
        self.adj[v].append(backward)
    def get_edges(self,node):
        return self.adj.get(node,[])
    def reset_flows(self):
        for u in self.adj:
            for edge in self.adj[u]:
                edge.flow = 0 