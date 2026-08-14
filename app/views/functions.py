import numpy as np
import streamlit as st

from calc_package.core.functions import find_delta_for_limit, sample_clean
from calc_package.plotting.functions_plotly import plot_epsilon_delta

EPS_MAX = 1.0
functions = {
    "sin(x)/x": {"f": lambda x: np.sin(x)/x,
                 "a": 0,
                 "L": 1,
                 "hole_x": 0},
}
with st.sidebar:
    func_name = st.selectbox("Funkce", list(functions.keys()))
    eps = st.slider(r"$\varepsilon$", value=0.3, min_value=0.01,
                    max_value=EPS_MAX, step=0.01)
    radius = st.slider("radius", value=3.0, min_value=0.1,
                       max_value=10.0, step=0.1)

entry = functions[func_name]
L = entry["L"]
a = entry["a"]
domain = (a - radius, a + radius)
x, y = sample_clean(entry["f"], domain)
delta = find_delta_for_limit(x, y, a, L, eps)
ylim = (L - EPS_MAX*1.2, L + EPS_MAX*1.2)

st.markdown(rf"Nepřítel zvolil :red-background[**$\varepsilon$ = {eps:.2f}**]. "
            rf"Stačí volit :green-background[**$\delta = {delta:.2f}$**].")
fig = plot_epsilon_delta(x, y, a, L, eps, delta,
                         entry["hole_x"], ylim=ylim)
st.plotly_chart(fig)
