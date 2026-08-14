import streamlit as st

st.set_page_config(layout="wide")

pages = [
    st.Page("views/home.py", title="Home", default=True),
    st.Page("views/sequences.py", title="Posloupnosti"),
    st.Page("views/functions.py", title="Funkce"),
    st.Page("views/derivatives.py", title="Derivace"),
    st.Page("views/series.py", title="Taylor"),
]

nav = st.navigation(pages)
nav.run()
