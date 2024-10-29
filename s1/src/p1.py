# Main Python file for P1
import streamlit as st


def P1():
    p1 = st.Page("src/p1h.py", title="P1Work", icon=":material/add_circle:")

    p2 = st.Page("src/p2h.py", title="P2Work", icon=":material/delete:")

    pg = st.navigation([p1, p2])
    st.set_page_config(
        page_title="PantySmeller", page_icon=":material/edit:", layout="wide"
    )
    pg.run()
