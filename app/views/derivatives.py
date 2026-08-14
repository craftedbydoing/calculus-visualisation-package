import numpy as np
import streamlit as st

from calc_package.core.derivatives import (
    calculate_line_slope,
    derivative_at_point,
    derivative_exists,
    line_through_point,
    one_sided_slopes,
)
from calc_package.core.functions import sample_clean
from calc_package.plotting.derivatives_plotly import plot_secant_to_tangent
from calc_package.plotting.functions_plotly import plot_function

functions = {
    "3": {"f": lambda x: 3 + 0*x,
          "a": 2},
    "x^2": {"f": lambda x: x**2,
            "a": -3},
    "e^x": {"f": lambda x: np.exp(x),
            "a": 0},
    "sin(x)": {"f": lambda x: np.sin(x),
               "a": 0},
    "|x|": {"f": lambda x: np.abs(x),
            "a": 0},
}
h_MAX = 5.0
func_name = st.selectbox("Funkce", list(functions.keys()))
h = st.slider(r"$h$", value=3.0, min_value=0.1, max_value=h_MAX, step=0.1)

entry = functions[func_name]
f = entry["f"]
a = entry["a"]
domain = (a-1.5, a+h_MAX+1)
x, f_vals = sample_clean(f, domain=domain)
sec_slope = calculate_line_slope(f, a, h)
sec_vals = line_through_point(x, a, f(a), sec_slope)
numeric_derivative = derivative_at_point(f, a)
tan_vals = line_through_point(x, a, f(a), numeric_derivative)

y_min = np.nanmin(f_vals-0.5)
y_max = np.nanmax(f_vals+0.5)
ylim = (y_min, y_max)

if derivative_exists(f, a):
    fig = plot_secant_to_tangent(x, f_vals, sec_vals, tan_vals,
                                 point_a=(a, f(a)), point_h=(a+h, f(a+h)), ylim=ylim)
    fig.update_layout(
        title=f"$a = {a}$, $f'(a) = {numeric_derivative:.02f}$, secant slope = {sec_slope:.02f}")

else:
    fig = plot_function(x, f_vals, label="f(x)")
    fig.update_yaxes(range=list(ylim))
    left, right = one_sided_slopes(f, a, h)
    st.warning(rf"Derivative at $a = {a}$ does NOT exist — "
               f"one-sided derivatives: left = {left:.2f} vs  right = {right:.2f}")

st.plotly_chart(fig)
