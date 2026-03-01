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
            dist,prev = algorithms.dijkstra(G,source)
            df = pd.DataFrame(dist.items(),columns = ["Node","Distance"])
            st.table(df)
    elif name == "Bellman_Ford":
        source = st.text_input("Source node")
        if source: 
            dist,prev = algorithms.bellman_ford(G,source)
            st.write(dist)

# Initialise graph in session state
if "graph" not in st.session_state:
    st.session_state.graph = Graph(directed = False)

G = st.session_state.graph 

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

nx_G = nx.Graph()

for u in G.edges:
    for v,w in G.edges[u].items():
        nx_G.add_edge(u,v,weight=w)

fig,ax = plt.subplots()
pos = nx.spring_layout(nx_G)

nx.draw(nx_G,pos,with_labels=True,ax=ax)

edge_labels = nx.get_edge_attributes(nx_G,"weight")
nx.draw_networkx_edge_labels(nx_G,pos,edge_labels=edge_labels)

st.pyplot(fig)

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
if st.button("Run ALgorithm"):
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