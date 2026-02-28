def tarjan(graph):
    stack = []
    on_stack = set()
    index = 0 
    SCCs = []
    lows = {}
    ids = {}
    def dfs(u):
        nonlocal index 
        ids[u] = index 
        lows[u] = index 
        stack.append(u)
        on_stack.add(u)
        index +=1 
        for v in graph.neighbours(u):
            if v not in ids:
                dfs(v)
                lows[u] = min(lows[u],lows[v])
            elif v in on_stack:
                lows[u] = min(lows[u],ids[v])
        if lows[u] == ids[u]:
            scc = []
            while True:
                node = stack.pop()
                on_stack.remove(node)
                scc.append(node)
                if node == u:
                    break 
            SCCs.append(scc)
    for node in graph.nodes():
        if node not in ids:
            dfs(node)
    return SCCs 