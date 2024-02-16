import streamlit as st
from a_star import *

def get_new_id():
    id = 0
    while True:
        id += 1
        yield id

id_nums = get_new_id()

st.set_page_config(layout = 'wide')
widget_id = (id for id in range(1, 100_00))

if 'buttons_clicked' not in st.session_state:
    st.session_state.buttons_clicked = []
if 'full_world_transposed' not in st.session_state:
    st.session_state.full_world_transposed = [[row[i] for row in full_world] for i in range(len(full_world[0]))]

def click_button(r,c):
    if len(st.session_state.buttons_clicked) == 0:
        st.session_state.buttons_clicked.append((r,c))
    elif len(st.session_state.buttons_clicked) == 1:
        st.session_state.buttons_clicked = []
        st.session_state.full_world_transposed[c][r] = '🎁'
    # else:
    #     st.session_state.buttons_clicked = [(r,c)]
    #     st.session_state.full_world_transposed[c][r] = [[row[i] for row in full_world] for i in range(len(full_world[0]))]
    return

cols = st.columns(len(st.session_state.full_world_transposed[0]),gap='small')

for c,col in enumerate(st.session_state.full_world_transposed):
    with cols[c]:
        for r,element in enumerate(col):
            if st.button(st.session_state.full_world_transposed[c][r], key = next(id_nums)):
                click_button(r,c)