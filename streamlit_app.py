import streamlit as st
from a_star import *\

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
if 'col_list' not in st.session_state:
    st.session_state.col_list = st.columns(len(st.session_state.full_world_transposed[1]),gap='small')
if 'path_length' not in st.session_state:
    st.session_state.path_length = 0

with st.sidebar:
    st.title('A* Algorithm')
    st.write("Usage: Click the start position, pause for the map to reload, then click the destination.")
    st.write("Path Cost: "+str(st.session_state.path_length))
    with st.expander('Terrain Costs:'):
        for tile in COSTS.keys():
            COSTS[tile] = st.slider(tile,min_value=0,max_value=10,value=COSTS[tile])
        # st.slider('🐊',min_value=0,max_value=100,value=7)    #, '🐊', '🌾', '🌾', '⛰', '🌲')

col_list = st.columns(len(st.session_state.full_world_transposed[0]),gap='small')

def reset_buttons():
    with st.empty():
        for c,col in enumerate(st.session_state.full_world_transposed):
            with col_list[c]:
                for r,element in enumerate(col):
                    st.button(st.session_state.full_world_transposed[c][r], key = next(id_nums), on_click=click_button, args=(r,c))
        return

def click_button(r,c):
    if st.session_state.full_world_transposed[c][r] == '🌋':
        st.warning('🌋 tiles are impassible, so that click was ignored')
    elif len(st.session_state.buttons_clicked) == 0:
        st.session_state.buttons_clicked.append((r,c))
        st.session_state.full_world_transposed = [[row[i] for row in full_world] for i in range(len(full_world[0]))]
        st.session_state.full_world_transposed[c][r] = '⭐'
        # reset_buttons()
        # st.session_state.buttons_clicked.append((r,c))
    elif len(st.session_state.buttons_clicked) == 1:
        ro,co = st.session_state.buttons_clicked[0]
        st.session_state.path_length = 0
        for move in a_star_search(full_world, (co,ro), (c,r), COSTS, MOVES, heuristic):
            ro += move[1]
            co += move[0]
            st.session_state.path_length += COSTS[st.session_state.full_world_transposed[co][ro]]
            st.session_state.full_world_transposed[co][ro] = MOVE_ICONS[MOVES.index(move)]
        st.session_state.full_world_transposed[c][r] = '🎁'
        st.session_state.buttons_clicked = []
        # reset_buttons()
        # st.session_state.buttons_clicked = []
    return

reset_buttons()