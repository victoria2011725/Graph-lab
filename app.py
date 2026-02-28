import streamlit as st 
st.title("Graph Optimisation Lab")
st.write("It works!")
algorithm = st.selectbox(
    "Choose an algorithm",
    ["BFS","DFS","Dijkstra","A*","Bellman-Ford"]
)
st.write("You selected:", algorithm)
import networkx as nx 
import matplotlib.pyplot as plt

# Initialise graph in session state
if "graph" not in st.session_state:
    st.session_state.graph = nx.Graph()

G = st.session_state.graph 

st.subheader("Add Edge")

col1,col2 = st.columns(2)
with col1:
    node1 = st.text_input("Node 1 ")
with col2:
    node2 = st.text_input("Node 2")

if st.button("Add Edge"):
    if node1 and node2:
        G.add_edge(node1,node2)

# Draw graph 
st.subheader("Current Graph")

fig,ax = plt.subplots()
nx.draw(G,with_labels=True, ax=ax)
st.pyplot(fig)