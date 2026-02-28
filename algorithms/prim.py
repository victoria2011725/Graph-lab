import heapq 
def prim(graph,source):
    mst = []
    visited = {source}
    priority_queue = []
    for neighbour in graph.neighbours(source):
        weight = graph.get_weight(source,neighbour)
        heapq.heappush(priority_queue,(weight,source,neighbour))
    while priority_queue:
        weight,u,v = heapq.heappop(priority_queue)
        if v in visited:
            continue 
        mst.append((weight,u,v))
        visited.add(v)
        for neighbour in graph.neighbours(v):
            if neighbour not in visited:
                weight = graph.get_weight(v,neighbour)
                heapq.heappush(priority_queue,(weight,v,neighbour))
    return mst,visited
        
def find_all_mst(graph):
    MSTs=[]
    global_visited = set()

    for node in graph.nodes():
        if node not in gloabl_visited:
            mst,visited = prim(graph,node)
            MSTs.append(mst)
            global_visited.update(visited)
    
    return MSTs 
            
    