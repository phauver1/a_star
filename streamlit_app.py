import streamlit as st
from a_star import *
widget_id = (id for id in range(1, 100_00))

cols = st.columns([1]*len(full_world[0]))

for c,col in enumerate(cols):
    with col:
        for r,element in enumerate(full_world):
            if st.button(full_world[r][c], key=next(widget_id)):
                st.write(str(r)+str(c))