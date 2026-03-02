def reconstruct_path(prev,start,end):
    path = []
    current = end 
    while current is not None:
        path.append(current)
        current = prev.get(current)
    path.reverse()
    if path[0] != start:
        return None
    return path 