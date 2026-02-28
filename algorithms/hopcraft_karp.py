from collections import deque 
class Hopcraft_Karp:
    def __init__(self,u_count,v_count,adj):
        self.u_count = u_count 
        self.v_count = v_count 
        self.adj = adj 
        self.INF = float("inf")
        self.u_pair = [0] * (self.u_count+1)
        self.v_pair = [0] * (self.v_count+1)
        self.dist = [0] * (self.u_count+1)  
    def bfs(self):
        queue = deque([])
        for u in range(1,self.u_count+1):
            if self.u_pair[u] == 0:
                self.dist[u] = 0 
                queue.append(u)
            else:
                self.dist[u] = self.INF 
        self.dist[0] = self.INF 
        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if self.dist[v_pair[v]] == self.INF:
                    self.dist[v_pair[v]] = self.dist[u] + 1
                    queue.append(v)
        return self.dist[0] != self.INF 
    def dfs(self,u):
        if u != 0:
            for v in self.adj[u]:
                if self.dist[pair_v[v]] == self.dist[u] + 1:
                    if self.dfs(pair_v[v]):
                        self.pair_v[v] = u
                        self.pair_u[u] = v
                        return True 
            self.dist[u] = self.INF 
            return False 
        return True 
    def max_matching(self):
        maximum = 0
        while self.bfs():
            for u in self.adj:
                if self.u_pair[u] == u:
                    if self.dfs(u):
                        maximum += 1 
        return maximum, self.u_pair 


        