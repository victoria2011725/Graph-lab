from algorithms import hungarian 
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

    