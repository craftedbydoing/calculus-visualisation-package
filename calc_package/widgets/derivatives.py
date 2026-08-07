import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import FloatSlider, interact

from calc_package.core.derivatives import (
    calculate_slope_secant,
    derivative_at_point,
    get_secant_values,
)
from calc_package.core.functions import sample_clean
from calc_package.plotting.functions import plot_function


def derivative_visualiser():
    functions = {
        "3": {"f": lambda x: 3 + 0*x,
              "a": 2},
        "x^2": {"f": lambda x: x**2,
                "a": -3},
        "1/x": {"f": lambda x: 1/x,
                "a": 1},
        "tan(x)": {"f": lambda x: np.tan(x),
                   "a": 0}
    }
    h_MAX = 5

    fig, ax = plt.subplots(figsize=(6, 6))

    def show(func_name, h):
        entry = functions[func_name]
        f = entry["f"]
        a = entry["a"]
        domain = (a-1.5, a+h_MAX+1)
        x, f_vals = sample_clean(f, domain=domain)
        sec_slope = calculate_slope_secant(f, a, h)
        sec_vals = get_secant_values(f, x, a, sec_slope)

        ax.clear()
        y_min = np.min(f_vals*0.8)
        y_max = np.max(f_vals*1.2)

        ax.set_xlim(domain[0], domain[1])
        ax.set_ylim(y_min, y_max)
        plot_function(ax, x, f_vals)
        plot_function(ax, x, sec_vals)

        numeric_derivative = derivative_at_point(f, a)
        ax.set_title(
            f"$a = {a}$, $f'(a) = {numeric_derivative:.02f}$, secant slope = {sec_slope:.02f}")
        fig.canvas.draw_idle()  # "redraw command"

    interact(
        show,
        func_name=list(functions.keys()),
        h=FloatSlider(value=3, min=0.1, max=h_MAX, step=0.1)
    )
