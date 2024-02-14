import streamlit as st
from a_star import *

st.set_page_config(layout = 'wide')
widget_id = (id for id in range(1, 100_00))

full_world_transposed = [[row[i] for row in full_world] for i in range(len(full_world[0]))]

cols = st.columns(len(full_world_transposed[0]),gap='small')

if 'buttons_clicked' not in st.session_state:
    st.session_state.buttons_clicked = []

def click_button(button_key):
    if len(st.session_state.buttons_clicked) <= 1:
        st.session_state.buttons_clicked.append(button_key)
        print(st.session_state[button_key])
    else:
        st.session_state.buttons_clicked = [button_key]


for c,col in enumerate(full_world_transposed):
    with cols[c]:
        for r,element in enumerate(col):
            button_key = str(r)+'.'+str(c)
            print(button_key)
            if st.button(full_world_transposed[c][r], key=button_key, on_click=click_button, args=(button_key,)):
                print('1')