import streamlit as st
from a_star import *
print(full_world)



cols = st.columns([1]*len(full_world[0]))

for c,col in enumerate(cols):
    with col:
        for r,element in full_world:
            if st.button(full_world[r][c]):
                st.write(str(r)+str(c))