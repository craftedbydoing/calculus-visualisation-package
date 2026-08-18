import numpy as np
import streamlit as st

from calc_package.core.functions import sample_clean
from calc_package.core.integration import riemann_sum
from calc_package.plotting.integration_plotly import plot_riemann, plot_riemann_sandwich
from calc_package.catalog import INTEGRATION

functions = INTEGRATION
with st.sidebar:
    func_name = st.selectbox("Function", list(functions.keys()))
    n = st.slider("#rectangles", value=4, min_value=1, max_value=300, step=1)
    method = st.selectbox(
        "Method", ["lower", "upper", "midpoint", "left", "right"])
entry = functions[func_name]
f = entry["f"]
a, b = entry["domain"]
x, f_vals = sample_clean(f, (a, b), num_points=1000, factor=200)
edges, heights, width, summation = riemann_sum(f, a, b, n, method)

fig = plot_riemann(x, f_vals, edges, heights, width)
st.markdown(f"Sum of $n={n}$ rectangles: {summation:.04f}")
st.plotly_chart(fig)

st.header("Riemann integrability condition")
edges_low, lower_h, width_low, lower_sum = riemann_sum(f, a, b, n, "lower")
edges_up, upper_h, width_up, upper_sum = riemann_sum(f, a, b, n, "upper")
gap = upper_sum-lower_sum

eps = st.slider("Epsilon", value=2.0, min_value=0.1, max_value=3.0, step=0.1)
if gap < eps:
    st.success(f"U − L = {gap:.4f} < ε = {eps}. We won! :)")
else:
    st.warning("We are losing rn :(")

fig2 = plot_riemann_sandwich(
    x, f_vals, edges, lower_h, upper_h, width_low)
st.markdown(f"lower sum = {lower_sum:.3f},  upper sum = {upper_sum:.3f},  "
            f"gap = {gap:.3f}")
st.plotly_chart(fig2, use_container_width=False)
