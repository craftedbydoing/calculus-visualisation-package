import streamlit as st

st.set_page_config(layout="wide")

pages = [
    st.Page("views/home.py", title="Home", default=True),
    st.Page("views/sequences.py", title="Sequences"),
    st.Page("views/functions.py", title="Functions"),
    st.Page("views/derivatives.py", title="Derivative"),
    st.Page("views/integration.py", title="Integration"),
    st.Page("views/series.py", title="Taylor"),
]

nav = st.navigation(pages)
nav.run()
