import numpy as np
import streamlit as st

from calc_package.core.functions import sample_clean
from calc_package.core.integration import riemann_sum
from calc_package.plotting.integration_plotly import plot_riemann, plot_riemann_sandwich

functions = {
    "e^x": {"f": lambda x: np.exp(x),
            "domain": (0, 3)},
    "sin(x)": {"f": lambda x: np.sin(x),
               "domain": (0, np.pi)},
}
with st.sidebar:
    func_name = st.selectbox("Function", list(functions.keys()))
    n = st.slider("#rectangles", value=4, min_value=1, max_value=100, step=1)
    method = st.selectbox(
        "Method", ["lower", "upper", "midpoint", "left", "right"])
entry = functions[func_name]
f = entry["f"]
a, b = entry["domain"]
x, f_vals = sample_clean(f, (a, b))
edges, heights, width, sumation = riemann_sum(f, a, b, n, method)

fig = plot_riemann(x, f_vals, edges[:-1], heights, width)
st.markdown(f"Summation of $N={n}$ terms: {sumation:.04f}")
st.plotly_chart(fig)

st.header("Riemann integrability condition")
_, lower_h, width, lower_sum = riemann_sum(f, a, b, n, "lower")
edges, upper_h, _, upper_sum = riemann_sum(f, a, b, n, "upper")

fig2 = plot_riemann_sandwich(x, f_vals, edges[:-1], lower_h, upper_h, width)
st.markdown(f"lower sum = {lower_sum:.3f},  upper sum = {upper_sum:.3f},  "
            f"gap = {upper_sum - lower_sum:.3f}")
st.plotly_chart(fig2)
