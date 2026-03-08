import heapq 
from algorithms.utils import highlight
def dijkstra(graph,source):
    distances={}
    prev ={}
    for u in graph.nodes():
        distances[u]=float("inf")
        prev[u]=None 
    distances[source]=0
    priority_queue=[(0,source)]

    while priority_queue:
        current_distance,current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue 
        for neighbour in graph.neighbours(current_node):
            highlight(current_node,neighbour)
            distance = current_distance + graph.get_weight(current_node,neighbour)
            if distance < distances[neighbour]:
                distances[neighbour]=distance 
                prev[neighbour]=current_node 
                heapq.heappush(priority_queue,(distance,neighbour))
    return distances,prev