from collections import deque
from algorithms.utils import highlight
class Dinic:
    def __init__(self,G,s,t):
        self.G = G
        self.n = len(G.nodes())
        self.graph = [[] for _ in range(self.n)]
        self.level = [0] * self.n 
        u_index = {u: i for i,u in enumerate(self.G.nodes())}
        self.s = u_index[s]
        self.t = u_index[t]
        for u in self.G.adj:
            for v,cap in self.G.adj[u].items():
                u_idx = u_index[u]
                v_idx = u_index[v]

                forward_edge_pos = len(self.graph[u_idx])
                reverse_edge_pos = len(self.graph[v_idx])

                self.graph[u_idx].append([v_idx, cap, reverse_edge_pos])
                self.graph[v_idx].append([u_idx, 0, forward_edge_pos])
    def bfs(self,):
        queue = deque([self.s])
        self.level = [-1] * self.n 
        self.level[self.s] = 0 

        while queue:
            u = queue.popleft()
            for v,cap,rev_idx in self.graph[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1 
                    queue.append(v)
        return self.level[self.t] >= 0 
    
    def dfs(self,u,flow,ptr):
        if flow == 0 or u == self.t:
            return flow 
        for i in range(ptr[u],len(self.graph[u])):
            i = ptr[u]
            v, cap, rev_idx = self.graph[u][i]
            if cap > 0 and self.level[v] == self.level[u] + 1:
                pushed = self.dfs(v, min(flow, cap), ptr)
                if pushed > 0:
                    highlight(u,v)
                    self.graph[u][i][1] -= pushed 
                    self.graph[v][rev_idx][1] += pushed 
                    return pushed
            ptr[u] += 1 
        return 0 
    
    def max_flow(self):
        max_f = 0 
        while self.bfs():
            ptr = [0] * self.n 
            while True:
                pushed = self.dfs(self.s,float("inf"),ptr)
                if pushed == 0:
                    break 
                max_f += pushed 
        return max_f 


