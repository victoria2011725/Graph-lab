import streamlit as st 
import pandas as pd 
st.title("Graph Optimisation Lab")
import networkx as nx 
from graph_core import Graph 
import matplotlib.pyplot as plt
import algorithms 
def run_algorithm(name,G):
    if name == "BFS":
        source = st.text_input("Source Node")
        target = st.text_input("Target Node")
        result = algorithms.bfs(G,source,target)
        st.write(result)
    elif name == "Dijkstra":
        source = st.text_input("Source Node")
        if source: 
            source = source.strip()
            if source not in G.nodes():
                st.error("Source node does not exist in the graph")
                return 
            
            dist,prev = algorithms.dijkstra(G,source)
            df = pd.DataFrame(dist.items(),columns = ["Node","Distance"])
            paths = []
            for node in G.nodes():
                path = algorithms.reconstruct_path(prev,source,node)
                paths.append(path)
            st.table(df)
            st.write(paths)
    elif name == "Bellman-Ford":
        source = st.text_input("Source Node")
        if source: 
            source = source.strip()
            if source not in G.nodes():
                st.error("Source node does not exist in the graph")
                return 
            
            result = algorithms.bellman_ford(G,source)
            if result is None:
                st.error("Negative cycle detected in graph.")
                return 
            dist,prev = result 
            df = pd.DataFrame(dist.items(),columns = ["Node","Distance"])
            paths = []
            for node in G.nodes():
                path = algorithms.reconstruct_path(prev,source,node)
                paths.append(path)
            st.table(df)
            st.write(paths)
    elif name == "DFS recursive":
        source = st.text_input("Source Node")
        target = st.text_input("Target Node")
        path = algorithms.dfs_recursive(G,source,target)
        st.write(path)
    elif name == "DFS iterative":
        source = st.text_input("Source Node")
        target = st.text_input("Target Node")
        path = algorithms.dfs_iterative(G,source,target)
        st.write(path)
    elif name == "Floyd-Warshall":
        dist,prev = algorithms.floyd_warshall(G)
        df = pd.DataFrame(dist.items(),columns = ["Node","Distance"])
        st.table(df)
    elif name == "Kruskal":
        mst = algorithms.kruskal(G)
        st.write(mst)
    elif name =="Prim":
        mst = algorithms.find_all_mst(G)
        st.write(mst)
    elif name == "Tarjan":
        SCCs = algorithms.tarjan(G)
        st.write(SCCs)
    elif name == "Kosaraju":
        SCCs = algorithms.kosaraju(G)
        st.write(SCCs)
    elif name == "Edmond Karp":
        source = st.text_input("Source Node")
        sink = st.text_input("Sink Node")
        max_flow = algorithms.edmond_karp(G,source,sink)
        st.write(f"Max flow : {max_flow}")
    elif name == "Johnson":
        dist,prev = algorithms.johnson(G)
        paths = []
        df = pd.DataFrame(dist.items(),columns = ["Node","Distance"])
        st.table(df)
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
    ["Algorithm Mode","Task Mode"]
) 
if mode == "Algorithm Mode":
    algorithm = st.selectbox(
        "Choose Algorithm",
        ["BFS","DFS recursive","DFS iterative","Dijkstra","Bellman-Ford","Floyd-Warshall","Kruskal","Prim","Tarjan","Kosaraju","Hopcraft Karp","Hungarian","Edmond Karp","Johnson"],
        key = "algorithm_select"
    )
if "run_algo" not in st.session_state:
    st.session_state.run_algo = False 
if st.button("Run Algorithm"):
    st.session_state.run_algo = True 
if st.session_state.run_algo:
    run_algorithm(algorithm,G)
if mode == "Task Mode":
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
    if st.button("Solve Task"):
        solve_task(task,G)