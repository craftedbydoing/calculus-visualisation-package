import math as m

import numpy as np
import streamlit as st

from calc_package.core.functions import sample_clean
from calc_package.core.series import taylor_values
from calc_package.plotting.series_plotly import taylor_plotly
from calc_package.catalog import TAYLOR

functions = TAYLOR
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

fig = taylor_plotly(x, y, taylor_vals, n, ylim)

st.markdown(rf"Taylorův polynom v bodě :orange-background[$a = {a}$], "
            rf"stupně :blue-background[$N = {n}$].")
st.plotly_chart(fig)
