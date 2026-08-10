import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import IntSlider, interact

from calc_package.core.functions import sample_clean
from calc_package.core.integration import riemann_sum
from calc_package.plotting.integration import plot_riemann, plot_riemann_sandwich


def riemann_visualisation():
    functions = {
        "e^x": {"f": lambda x: np.exp(x),
                "domain": (0, 3)},
        "sin(x)": {"f": lambda x: np.sin(x),
                   "domain": (0, np.pi)},
    }

    fig, ax = plt.subplots()

    def show(func_name, n, method):
        entry = functions[func_name]
        f = entry["f"]
        a, b = entry["domain"]
        x, f_vals = sample_clean(f, (a, b))
        edges, heights, width, sumation = riemann_sum(f, a, b, n, method)

        ax.clear()
        plot_riemann(ax, x, f_vals, edges[:-1], heights, width)
        ax.set_title(f"Summation of $N={n}$ terms: {sumation:.04f}")
        fig.canvas.draw_idle()

    interact(
        show,
        func_name=list(functions.keys()),
        n=IntSlider(value=4, min=1, max=100, step=1),
        method=["lower", "upper", "midpoint", "left", "right"],
    )


def riemann_integrability_definition():
    functions = {
        "e^x": {"f": lambda x: np.exp(x),
                "domain": (0, 3)},
        "sin(x)": {"f": lambda x: np.sin(x),
                   "domain": (0, np.pi)},
    }

    fig, ax = plt.subplots()

    def show(func_name, n):
        entry = functions[func_name]
        f = entry["f"]
        a, b = entry["domain"]
        x, f_vals = sample_clean(f, (a, b))
        _, lower_h, width, lower_sum = riemann_sum(f, a, b, n, "lower")
        edges, upper_h, _, upper_sum = riemann_sum(f, a, b, n, "upper")

        ax.clear()
        plot_riemann_sandwich(
            ax, x, f_vals, edges[:-1], lower_h, upper_h, width)
        ax.set_title(f"lower sum = {lower_sum:.3f},  upper sum = {upper_sum:.3f},  "
                     f"gap = {upper_sum - lower_sum:.3f}")
        fig.canvas.draw_idle()

    interact(
        show,
        func_name=list(functions.keys()),
        n=IntSlider(value=4, min=1, max=200, step=1),
    )
