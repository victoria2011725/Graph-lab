import streamlit as st 
import pandas as pd 
st.title("Graph Optimisation Lab")
import networkx as nx 
from graph_core import Graph 
import matplotlib.pyplot as plt
import algorithms 
if "active_algorithm" not in st.session_state:
    st.session_state.active_algorithm = None 
def run_algorithm(name,G,source,target):
    if name == "BFS":
        st.divider()
        st.header("Algorithm Results")
        result = algorithms.bfs(G,source,target)
        st.write(result)
    elif name == "Dijkstra":
        st.divider()
        st.header("Algorithm Results") 
        source = source.strip()
        if source not in G.nodes():
            st.error("Source node does not exist in the graph")
        else:
            dist,prev = algorithms.dijkstra(G,source)
            data = []
            for node,distance in dist.items():
                if distance == float("inf"):
                    distance = None
                data.append([node,distance])
            df = pd.DataFrame(data,columns=["Node","Distance"])
            st.subheader(f"Shortest Paths from {source}")
            st.table(df)
            
    elif name == "Bellman-Ford":
        st.divider()
        st.header("Algorithm Results") 
        source = source.strip()
        if source not in G.nodes():
            st.error("Source node does not exist in the graph")
        else:
            dist,prev = algorithms.bellman_ford(G,source)
            data = []
            for node,distance in dist.items():
                if distance == float("inf"):
                    distance = None
                data.append([node,distance])
            df = pd.DataFrame(data,columns=["Node","Distance"])
            st.subheader(f"Shortest Paths from {source}")
            st.table(df)
    elif name == "DFS recursive":
        st.divider()
        st.header("Algorithm Results")
        path = algorithms.dfs_recursive(G,source,target)
        st.write(path)
    elif name == "DFS iterative":
        st.divider()
        st.header("Algorithm Results")
        path = algorithms.dfs_iterative(G,source,target)
        st.write(path)
    elif name == "Floyd-Warshall":
        st.divider()
        st.header("Algorithm Results")
        dist,prev = algorithms.floyd_warshall(G)
        nodes = list(dist.keys())
        matrix = []
        for u in nodes:
            row = []
            for v in nodes:
                value = dist[u][v]
                if value == float("inf"):
                    row.append("Infinity")
                else:
                    row.append(value) 
            matrix.append(row)
        df = pd.DataFrame(matrix,index =nodes,columns=nodes)
        st.subheader("All-Pairs Shortest Path Matrix")
        st.table(df)
        
    elif name == "Kruskal":
        st.divider()
        st.header("Algorithm Results")
        mst = algorithms.kruskal(G)
        df = pd.DataFrame(mst, columns = ["Weight","From","To"])
        st.subheader("Minimum Spanning Tree")
        st.table(df)

        total_weight = sum(edge[0] for edge in mst)
        st.success(f"Total MST Weight: {total_weight}")
    elif name =="Prim":
        st.divider()
        st.header("Algorithm Results")
        MSTs = algorithms.find_all_mst(G)
        mst = [edge for component in MSTs for edge in component]
        df = pd.DataFrame(mst, columns = ["Weight","From","To"])
        st.subheader("Minimum Spanning Tree")
        st.table(df)

        total_weight = sum(edge[0] for edge in mst)
        st.success(f"Total MST Weight: {total_weight}")
    elif name == "Tarjan":
        st.divider()
        st.header("Algorithm Results")
        SCCs = algorithms.tarjan(G)
        st.subheader("Strongly Connected Components")
        for i,component in enumerate(SCCs,1):
            st.markdown(f"**Component {i}:** {', '.join(component)}")
    elif name == "Kosaraju":
        st.divider()
        st.header("Algorithm Results")
        SCCs = algorithms.kosaraju(G)
        st.subheader("Strongly Connected Components")
        for i,component in enumerate(SCCs,1):
            st.markdown(f"**Component {i}:** {', '.join(component)}")
    elif name == "Edmond Karp":
        st.divider()
        st.header("Algorithm Results")
        max_flow = algorithms.edmond_karp(G,source,target)
        st.success(f"Maximum Flow from {source} to {target} : {max_flow}")
    elif name == "Johnson":
        st.divider()
        st.header("Algorithm Results")
        dist,prev = algorithms.johnson(G)
        nodes = list(dist.keys())
        matrix = []
        for u in nodes:
            row = []
            for v in nodes:
                value = dist[u][v]
                if value == float("inf"):
                    row.append("Infinity")
                else:
                    row.append(value) 
            matrix.append(row)
        df = pd.DataFrame(matrix,index =nodes,columns=nodes)
        st.subheader("All-Pairs Shortest Path Matrix")
        st.table(df)
    else:
        st.write("Confused")
#Initialise graph in session state 
directed = st.checkbox("Directed Graph",value = False)
if "graph" not in st.session_state:
    st.session_state.graph = Graph(directed=directed)

G = st.session_state.graph 

G.directed = directed 

st.subheader("Add Edge")

col1,col2,col3 = st.columns(3)
with col1:
    node1 = st.text_input("Node 1 ")
with col2:
    node2 = st.text_input("To")
with col3:
    weight = st.number_input("Weight",value=1)

if st.button("Add Edge"):
    if node1 and node2:
        G.add_edge(node1,node2,weight)
        st.success(f"Edge {node1} to {node2} added")

# Draw graph 
st.subheader("Current Graph")

nx_G = nx.DiGraph() if G.directed else nx.Graph()

for u in G.adj:
    for v,w in G.adj[u].items():
        nx_G.add_edge(u,v,weight=w)

fig,ax = plt.subplots()
pos = nx.spring_layout(nx_G)

nx.draw(nx_G,pos,with_labels=True,ax=ax)

edge_labels = nx.get_edge_attributes(nx_G,"weight")
nx.draw_networkx_edge_labels(nx_G,pos,edge_labels=edge_labels)

st.pyplot(fig)
# algorithm selection
mode = st.radio(
    "Choose mode",
    ["Algorithm Mode","Task Mode"],
    key = "mode_select"
) 
if mode == "Algorithm Mode":
    algorithm = st.selectbox(
        "Choose Algorithm",
        ["BFS","DFS recursive","DFS iterative","Dijkstra","Bellman-Ford","Floyd-Warshall","Kruskal","Prim","Tarjan","Kosaraju","Hopcraft Karp","Hungarian","Edmond Karp","Johnson"],
        key = "algorithm_select"
    )
    if algorithm == "BFS" or algorithm == "DFS recursive" or algorithm == "DFS iterative":
        source = st.text_input("Source Node",key = "algo_source1")
        target = st.text_input("Target Node",key = "algo_source2")
    elif algorithm == "Edmond Karp":
        source = st.text_input("Source Node",key = "algo_source1")
        target = st.text_input("Sink Node",key = "algo_source2")
    elif algorithm == "Dijkstra" or algorithm == "Bellman-Ford":
        source = st.text_input("Source Node",key = "algo_source1")
        target = None
    else:
        source = None 
        target = None 
         
    if st.button("Run"):
        run_algorithm(algorithm,G,source,target)
elif mode == "Task Mode":
    task = st.selectbox(
        "Choose Task",
        [
            "Find shortest path",
            "Find all pairs shortest paths",
            "Find minimum spanning tree",
            "Find strongly connected components",
            "Find maximum flow"
        ]
    )
    if task == "Find shortest path":
        target = None 
        source = st.text_input("Source Node",key="task_source")
        if st.button("Run"):    
            if G.has_negative_weights():
                st.write("Belllman Ford executing")
                run_algorithm("Bellman_Ford",G,source,target)
            else:
                st.write("Dijkstra executing")
                run_algorithm("Dijkstra",G,source,target)
    elif task == "Find all pairs shortest paths":
        source = None 
        target = None 
        if st.button("Run"):
            if len(G.nodes()) > 40:
                st.write("Johnson executing - optimal as large node number makes it faster than Floyd-Warshall")
                run_algorithm("Johnson", G,source,target)
            else: 
                st.write("Floyd-Warshall executing - small node number so efficient")
                run_algorithm("Floyd-Warshall",G,source,target)
    elif task == "Find minimum spanning tree":
        source = None 
        target = None 
        if st.button("Run"):
            if G.density() < 0.3:
                st.write("Kruskal executing - optimal as graph is sparse")
                run_algorithm("Kruskal",G,source,target)
            else:
                st.write("Prim executing - optimal as graph is dense")
                run_algorithm("Prim",G,source,target)
    elif task == "Find strongly connected components":
        source = None
        target = None 
        if st.button("Run"):
            if not G.directed:
                st.write("Strongly connected components only apply to directed graphs.")
            else:
                st.write("Tarjan executing")
                run_algorithm("Tarjan",G,source,target)
    elif task == "Find maximum flow":
        source = st.text_input("Source node",key="task_source")
        sink = st.text_input("Sink node",key="task_sink")
        if st.button("Run"):
            if not G.directed:
                st.write("Maximum flow requires directed graph")
            else:
                st.write("Edmond-Karp executing")
                run_algorithm("Edmond Karp",G,source,sink)

        

