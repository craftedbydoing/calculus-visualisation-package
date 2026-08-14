import math as m

import numpy as np
import streamlit as st

from calc_package.core.functions import sample_clean
from calc_package.core.series import taylor_values
from calc_package.plotting.series_plotly import plot_convergence_plotly

functions = {
    "e^x": {"f": lambda x: np.exp(x), "deriv": lambda k, a: np.exp(a) + k*0, "a": 0},
    "sin(x)": {"f": lambda x: np.sin(x), "deriv": lambda k, a: np.sin(a + k*np.pi/2), "a": 0},
    "1/(1-x)": {"f": lambda x: 1/(1-x), "deriv": lambda k, a: m.factorial(k) / (1-a)**(k+1), "a": 0},
    "x^2": {"f": lambda x: x**2, "deriv": lambda k, a: (2*a if k == 0 else (2*a if k == 1 else (2 if k == 2 else 0))), "a": 0}
}
with st.sidebar:
    func_name = st.selectbox("Funkce", list(functions.keys()))
    radius = st.slider(label="Domain radius", value=2.0,
                       min_value=0.3, max_value=10.0, step=0.1)
    n = st.slider(r"$N$", value=0, min_value=0, max_value=20, step=1)

entry = functions[func_name]
f = entry["f"]
deriv = entry["deriv"]
a = entry["a"]
domain = (a-radius, a+radius)

x, y = sample_clean(f, domain)
taylor_vals = taylor_values(x, a, deriv, n)

y_min = np.nanmin(y)
y_max = np.nanmax(y)
pad = (y_max-y_min)*0.15
ylim = (y_min - pad, y_max + pad)

fig = plot_convergence_plotly(x, y, taylor_vals, n, ylim)

st.plotly_chart(fig)
