def reconstruct_path(prev,start,end):
    path = []
    current = end 
    while current is not None:
        path.append(current)
        current = prev[start][current] 
    path.reverse()
    return path 