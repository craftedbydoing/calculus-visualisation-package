import streamlit as st

# import calc_package.plotting.style_plotly # set plotly visuals effect

st.set_page_config(layout="wide",
                   page_title="Calculus visually",
                   page_icon=":material/function:")

pages = {
    "Sequences": [
        st.Page("views/sequences/seq_plot.py", title="Plots"),
        st.Page("views/sequences/seq_convergence.py", title="Convergence"),
        st.Page("views/sequences/seq_divergence.py", title="Divergence"),
    ],
    "Functions": [
        st.Page("views/functions/func_limit.py", title="Limits-definition")
    ],
    "Derivative": [
        st.Page("views/derivative/der_def.py", title="Definition")
    ],
    # "Integral": [st.Page("views/integration.py", title="Integration")],
    "Series": [
        st.Page("views/series/taylor.py", title="Taylor polynom")
    ],
}

nav = st.navigation(pages)
nav.run()
