from algorithms import hungarian
from algorithms import hopcraft_karp
import numpy as np 
class BipartiteGraph:
    def __init__(self,left_nodes,right_nodes):
        self.left = list(left_nodes)
        self.right = list(right_nodes)
        self.edges = {}

        for u in self.left:
            self.edges[u] = {}

    def add_edge(self,u,v,weight):
        if u not in self.left:
            raise ValueError(f"{u} not in left partition")
        if v not in self.right:
            raise ValueERror(f"{v} not in right partition")
        self.edges[u][v] = weight
    
    def to_cost_matrix(self):
        n = max(len(self.left),len(self.right))
        matrix = np.full((n,n),float("inf"))

        for i,u in enumerate(self.left):
            for j,v in enumerate(self.right):
                if v in self.edges[u]:
                    matrix[i][j] = self.edges[u][v]
        return matrix 
    def extract_matching(self,marked):
        matching = []
        for i,u in enumerate(self.left):
            for j,v in enumerate(self.right):
                if marked[i][j] == 1:
                    matching.append((u,v))
        return matching
    def solve_assignment(self):
        C = self.to_cost_matrix()
        marked = hungarian(C)
        return self.extract_maching(marked)
    def max_matching(self):
        u_count = len(self.left())
        v_count = len(self.right())
        u_index = {u: i+1 for i,u in enumerate(self.left)}
        v_index = {v: i+1 for i,v in enumerate(self.right)}
        adj = {u_index[u]: [] for u in self.left}

        for u in self.edges:
            for v in self.edges[u]:
                adj[u_index[u]].append(v_index[v])
        hk = Hopcraft_Karp(u_count,v_count,adj)
        return hk.max_matching()


    