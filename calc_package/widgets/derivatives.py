import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import FloatSlider, interact

from calc_package.core.derivatives import (
    calculate_line_slope,
    derivative_at_point,
    line_through_point,
)
from calc_package.core.functions import sample_clean
from calc_package.plotting.derivatives import plot_secant_to_tangent


def derivative_visualiser():
    functions = {
        "3": {"f": lambda x: 3 + 0*x,
              "a": 2},
        "x^2": {"f": lambda x: x**2,
                "a": -3},
        "e^x": {"f": lambda x: np.exp(x),
                "a": 0},
        "sin(x)": {"f": lambda x: np.sin(x),
                   "a": 0}
    }
    h_MAX = 5

    fig, ax = plt.subplots(figsize=(5, 3))

    def show(func_name, h):
        entry = functions[func_name]
        f = entry["f"]
        a = entry["a"]
        domain = (a-1.5, a+h_MAX+1)
        x, f_vals = sample_clean(f, domain=domain)
        sec_slope = calculate_line_slope(f, a, h)
        sec_vals = line_through_point(x, a, f(a), sec_slope)
        numeric_derivative = derivative_at_point(f, a)
        tan_vals = line_through_point(x, a, f(a), numeric_derivative)

        ax.clear()
        y_min = np.nanmin(f_vals-0.5)
        y_max = np.nanmax(f_vals+0.5)
        ylim = (y_min, y_max)

        plot_secant_to_tangent(ax, x, f_vals, sec_vals, tan_vals,
                               point_a=(a, f(a)), point_h=(a+h, f(a+h)), ylim=ylim)

        ax.legend()
        ax.set_title(
            f"$a = {a}$, $f'(a) = {numeric_derivative:.02f}$, secant slope = {sec_slope:.02f}")
        fig.canvas.draw_idle()  # "redraw command"

    interact(
        show,
        func_name=list(functions.keys()),
        h=FloatSlider(value=3, min=0.1, max=h_MAX, step=0.1)
    )
