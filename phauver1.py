import streamlit as st
from a_star import *

# Generate new, non-overlapping key for each widget
def get_new_id():
    id = 0
    while True:
        id += 1
        yield id
id_nums = get_new_id()

# Get more space for the map icons
st.set_page_config(layout = 'wide')

# Initialize session_state variables
if 'buttons_clicked' not in st.session_state:
    st.session_state.buttons_clicked = []
if 'full_world_transposed' not in st.session_state:
    st.session_state.full_world_transposed = [[row[i] for row in full_world] for i in range(len(full_world[0]))]
if 'col_list' not in st.session_state:
    st.session_state.col_list = st.columns(len(st.session_state.full_world_transposed[1]),gap='small')
if 'path_length' not in st.session_state:
    st.session_state.path_length = 0

# Write the sidebar
with st.sidebar:
    st.title('A* Algorithm')
    st.write("Usage: Click the start position, pause for the map to reload, then click the destination.")
    st.write("Path Cost: "+str(st.session_state.path_length))
    with st.expander('Terrain Costs:'):
        for tile in COSTS.keys():
            COSTS[tile] = st.slider(tile,min_value=0,max_value=10,value=COSTS[tile])

# Create a set of 'column' widgets, each corresponsing to a collumn of the full map
col_list = st.columns(len(st.session_state.full_world_transposed[0]),gap='small')

# Draws a grid of buttons, each one representing a terrain square in the map
def reset_buttons():
    with st.empty():
        for c,col in enumerate(st.session_state.full_world_transposed):
            with col_list[c]:
                for r,element in enumerate(col):
                    st.button(st.session_state.full_world_transposed[c][r], key = next(id_nums), on_click=click_button, args=(r,c))
        return

# Calculates A* algorithm when two tiles are selected
def click_button(r,c):
    if st.session_state.full_world_transposed[c][r] == '🌋':
        st.warning('<🌋> tiles are impassible, so that click was ignored')
    elif len(st.session_state.buttons_clicked) == 0:
        st.session_state.buttons_clicked.append((r,c))
        st.session_state.full_world_transposed = [[row[i] for row in full_world] for i in range(len(full_world[0]))]
        st.session_state.full_world_transposed[c][r] = '⭐'
    elif len(st.session_state.buttons_clicked) == 1:
        ro,co = st.session_state.buttons_clicked[0]
        st.session_state.path_length = 0
        for move in a_star_search(full_world, (co,ro), (c,r), COSTS, MOVES, heuristic):
            st.session_state.full_world_transposed[co][ro] = MOVE_ICONS[MOVES.index(move)]
            ro += move[1]
            co += move[0]
            st.session_state.path_length += COSTS[st.session_state.full_world_transposed[co][ro]]
        st.session_state.full_world_transposed[c][r] = '🎁'
        ro,co = st.session_state.buttons_clicked[0]
        st.session_state.full_world_transposed[co][ro] = '⭐'
        st.session_state.buttons_clicked = []
    return

# Initializes the grid when the program begins
reset_buttons()