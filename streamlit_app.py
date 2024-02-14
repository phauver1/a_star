import streamlit as st
from a_star import *

def get_new_id():
    id = 0
    while True:
        id += 1
        yield id

id_nums = get_new_id()

print([next(id_nums) for _ in range(100)])

st.set_page_config(layout = 'wide')
widget_id = (id for id in range(1, 100_00))

full_world_transposed = [[row[i] for row in full_world] for i in range(len(full_world[0]))]

cols = st.columns(len(full_world_transposed[0]),gap='small')

if 'buttons_clicked' not in st.session_state:
    st.session_state.buttons_clicked = []

def click_button(container, button_key):
    if len(st.session_state.buttons_clicked) <= 1:
        st.session_state.buttons_clicked.append(button_key)
        # container.empty()
        # container.button('h', key=next(id_nums), on_click=click_button, args=(container,button_key))
    else:
        st.session_state.buttons_clicked = [button_key]
        container.empty()
        container.button('🎁', key=next(id_nums), on_click=click_button, args=(container,button_key))

# help(st.button)

for c,col in enumerate(full_world_transposed):
    with cols[c]:
        for r,element in enumerate(col):
            button_key = str(r)+'.'+str(c)
            container = st.empty()
            container.button(full_world_transposed[c][r], key = next(id_nums), on_click=click_button, args=(container,button_key))
            help(container.empty)