import streamlit as st
from a_star import *

st.set_page_config(layout = 'wide')
widget_id = (id for id in range(1, 100_00))

full_world_transposed = [[row[i] for row in full_world] for i in range(len(full_world[0]))]

cols = st.columns(len(full_world_transposed[0]),gap='small')

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Click me', on_click=click_button)


two_buttons = False
for c,col in enumerate(full_world_transposed):
    with cols[c]:
        for r,element in enumerate(col):
            if st.button(full_world_transposed[c][r], key=next(widget_id), on_click=click_button):
                print('1')