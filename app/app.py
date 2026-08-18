import streamlit as st

st.set_page_config(layout="wide")

pages = {
    "Home": [st.Page("views/home.py", title="Home", default=True)],
    "Sequences": [st.Page("views/sequences.py", title="Sequences"),
                  #   st.Page("views/sequences.py", title="Sequences")
                  ],
    "Functions": [st.Page("views/functions.py", title="Functions")],
    "Derivative": [st.Page("views/derivatives.py", title="Derivative")],
    "Integral": [st.Page("views/integration.py", title="Integration")],
    "Series": [st.Page("views/series.py", title="Taylor")],
}

nav = st.navigation(pages)
nav.run()
