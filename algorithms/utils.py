import streamlit as st 
import time 
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

def highlight(u=None,v=None,delay=0.5):
    nodes = set()
    edges = set()

    if u is not None:
        nodes.add(u)
    if v is not None:
        nodes.add(v)
        edges.add((u,v))
    
    st.session_state.highlight_nodes = nodes 
    st.session_state.highlight_edges = edges 

    
    time.sleep(delay)

  